#!/usr/bin/env python3
"""
Build a structure-aware RAG export from the knowledge base (v2).

The knowledge base is rigidly structured — a fixed section skeleton, a strict
split between cited *evidence* and labelled *coaching*, provenance-labelled
practice questions, and contiguous citations that resolve to a source list.
A naive "one chunk per top-level section" export throws that structure away and
produces chunks that are wildly uneven (a 78-token control block and a
40-question bank treated identically). This builder exploits the structure
instead, so retrieval can filter and verify rather than only fuzzy-match.

What it does differently from v1:
  * HETEROGENEOUS CHUNKING — chunk by section *kind*, not a fixed rule:
      - Question Bank        → one chunk per question (atomic, provenance-tagged)
      - long prose sections  → split on `##` sub-headings, then paragraph-window
                               with overlap if a sub-section is still large
      - References           → NOT emitted as prose; parsed into a citation map
      - control sections     → dropped (Document Control, Revision History)
  * LAYER + PROVENANCE METADATA — every chunk carries `layer`
    (evidence | coaching | question | summary | definitions | caveat |
    navigation) and, for questions, `provenance` (sourced | composed), so an
    agent can retrieve "evidence-layer, sourced only".
  * RESOLVED CITATIONS — each chunk's in-text `[n]` markers are resolved against
    the document's own References section to {n, publisher, title, url}, so a
    retrieved passage arrives with its primary source attached.
  * FRAMEWORK TAGS — which frameworks a chunk touches (civil-service, epso,
    police-cvf, nhs, ireland-pas, scotland, wales, nics, ...).
  * CONTEXTUAL HEADER — a deterministic "Title > Section > Sub-section — lead
    sentence" prefix for each chunk, for contextual embedding (prepend before
    encoding). No model is called at build time; the header is extractive.

Writes to exports/rag/:
  * chunks.jsonl     retrievable chunks with the metadata above
  * citations.jsonl  per-document [n] -> source records (verification payload)
  * questions.jsonl  the question-level facet index (competency x framework x
                     provenance x level), a projection of the question chunks
  * manifest.json    counts, the field schema, and the facet vocabularies

Deterministic (no dates / randomness) so the CI staleness gate stays green.
Only dependency is PyYAML. Regenerate with `python scripts/build_rag.py`.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ERROR: PyYAML required (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)

DOCS = Path("docs")
OUT = Path("exports/rag")

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
H1_RE = re.compile(r"^# (.+?)\s*$", re.MULTILINE)
H2_RE = re.compile(r"^## (.+?)\s*$", re.MULTILINE)
QUESTION_RE = re.compile(r"^\s*\d+\.\s+\S")
MARKER_RE = re.compile(r"\[(\d+)\]")
SOURCED_RE = re.compile(r"\*\(sourced[^*]*\)\*", re.IGNORECASE)
COMPOSED_RE = re.compile(r"\*\(composed[^*]*\)\*", re.IGNORECASE)
# Reference definition line:  - [3] **Publisher** — *Title*. https://url ...
REF_DEF_RE = re.compile(r"^- \[(\d+)\]\s*(.*)$")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
ITALIC_RE = re.compile(r"\*(.+?)\*")
URL_RE = re.compile(r"https?://[^\s>\]}\"'<)]+")

META_FIELDS = ["id", "title", "topic", "market", "document_type",
               "version", "status", "confidence", "category"]

# ── Section taxonomy ─────────────────────────────────────────────────────────
# Maps each template section to a retrieval `layer`. `control` sections are not
# emitted; `reference` is captured as citations, not prose.
SECTION_LAYER = {
    "Document Control": "control",
    "Revision History": "control",
    "Executive Summary": "summary",
    "Key Takeaways": "summary",
    "Purpose": "summary",
    "Scope": "summary",
    "Definitions": "definitions",
    "Framework Context": "evidence",
    "Core Reference": "evidence",
    "Assessor Perspective": "evidence",
    "Legal & Fairness Considerations": "evidence",
    "Question Bank": "question",
    "Model Answer Guidance": "coaching",
    "Common Pitfalls": "coaching",
    "Practice Exercises": "coaching",
    "Risks & Caveats": "caveat",
    "Open Questions": "caveat",
    "References": "reference",
    "Further Reading": "navigation",
    "Related Documents": "navigation",
}
# Sections whose prose is worth sub-splitting when large.
PROSE_LAYERS = {"evidence", "coaching", "summary", "caveat", "definitions"}
TARGET_TOKENS = 450          # ~350 words; embedding-friendly
HARD_MAX_TOKENS = 900        # split anything above this
OVERLAP_PARAS = 1            # paragraph overlap between window splits

# ── Framework detection ──────────────────────────────────────────────────────
FRAMEWORK_PATTERNS = {
    "civil-service": re.compile(r"success profiles|civil service behaviour|cabinet office", re.I),
    "epso": re.compile(r"\bepso\b|eu institution|eu-careers|intrapreneurship", re.I),
    "police-cvf": re.compile(r"college of policing|\bcvf\b|competency and values framework", re.I),
    "nhs": re.compile(r"\bnhs\b|values-based recruitment|\bvbr\b|6cs", re.I),
    "ireland-pas": re.compile(r"public appointments service|publicjobs|\bpas\b|capability framework", re.I),
    "police-scotland": re.compile(r"police scotland", re.I),
    "nics": re.compile(r"\bnics\b|northern ireland civil service", re.I),
    "wales": re.compile(r"welsh|wales|senedd", re.I),
    "psni": re.compile(r"\bpsni\b|police service of northern ireland", re.I),
    "graduate": re.compile(r"graduate scheme|assessment centre|strengths-based", re.I),
}


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def est_tokens(text: str) -> int:
    return max(1, len(text) // 4)


def lead_sentence(text: str) -> str:
    """First sentence of the first non-bold, non-list line — the extractive gist."""
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith(("#", "-", "*", "|", ">", "```")):
            continue
        s = re.sub(r"[*_`]", "", s)
        m = re.match(r"(.{0,160}?[.!?])(\s|$)", s)
        return (m.group(1) if m else s[:160]).strip()
    return ""


def detect_frameworks(text: str) -> list[str]:
    return [k for k, rx in FRAMEWORK_PATTERNS.items() if rx.search(text)]


# ── Citation parsing ─────────────────────────────────────────────────────────

def parse_references(sections: dict[str, str]) -> dict[int, dict]:
    """Build {n: {publisher, title, url}} from the document's References section."""
    refs: dict[int, dict] = {}
    body = sections.get("References", "")
    for line in body.splitlines():
        m = REF_DEF_RE.match(line.strip())
        if not m:
            continue
        n = int(m.group(1))
        rest = m.group(2)
        pub = BOLD_RE.search(rest)
        # strip the publisher before searching for an italic title
        after_pub = rest[pub.end():] if pub else rest
        title = ITALIC_RE.search(after_pub)
        url = URL_RE.search(rest)
        refs[n] = {
            "n": n,
            "publisher": pub.group(1).strip() if pub else None,
            "title": title.group(1).strip() if title else None,
            "url": (url.group(0).rstrip(".,);") if url else None),
        }
    return refs


def resolve_citations(text: str, refs: dict[int, dict]) -> list[dict]:
    nums = sorted({int(n) for n in MARKER_RE.findall(text)})
    return [refs[n] for n in nums if n in refs]


# ── Section splitting ────────────────────────────────────────────────────────

def split_h1(body: str) -> list[tuple[str, str]]:
    matches = list(H1_RE.finditer(body))
    out = []
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        out.append((m.group(1).strip(), body[start:end].strip()))
    return out


def split_h2(text: str) -> list[tuple[str | None, str]]:
    """Split a section body on `##` sub-headings. Preamble (before the first
    `##`) is returned with a None heading."""
    matches = list(H2_RE.finditer(text))
    if not matches:
        return [(None, text)]
    out = []
    pre = text[:matches[0].start()].strip()
    if pre:
        out.append((None, pre))
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        out.append((m.group(1).strip(), text[start:end].strip()))
    return out


def window_paragraphs(text: str) -> list[str]:
    """Greedy paragraph-window packing to ~TARGET_TOKENS with paragraph overlap.
    Only used when a single sub-section still exceeds HARD_MAX_TOKENS."""
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    if est_tokens(text) <= HARD_MAX_TOKENS:
        return [text]
    windows, cur, cur_tok = [], [], 0
    for p in paras:
        pt = est_tokens(p)
        if cur and cur_tok + pt > TARGET_TOKENS:
            windows.append("\n\n".join(cur))
            cur = cur[-OVERLAP_PARAS:] if OVERLAP_PARAS else []
            cur_tok = sum(est_tokens(x) for x in cur)
        cur.append(p)
        cur_tok += pt
    if cur:
        windows.append("\n\n".join(cur))
    return windows


# ── Question splitting ───────────────────────────────────────────────────────

def split_questions(text: str) -> list[dict]:
    """Return per-question dicts with subsection, provenance, citations markers."""
    out = []
    current_sub = None
    lines = text.splitlines()
    buf, buf_sub = None, None
    for line in lines:
        h2 = re.match(r"^## (.+?)\s*$", line)
        if h2:
            if buf is not None:
                out.append((buf_sub, buf.strip()))
                buf = None
            current_sub = h2.group(1).strip()
            continue
        if QUESTION_RE.match(line):
            if buf is not None:
                out.append((buf_sub, buf.strip()))
            buf, buf_sub = line, current_sub
        elif buf is not None and line.strip():
            buf += "\n" + line          # continuation of the current question
        elif buf is not None:
            out.append((buf_sub, buf.strip()))
            buf = None
    if buf is not None:
        out.append((buf_sub, buf.strip()))

    questions = []
    for sub, qtext in out:
        prov = ("sourced" if SOURCED_RE.search(qtext)
                else "composed" if COMPOSED_RE.search(qtext) else None)
        questions.append({"subsection": sub, "text": qtext, "provenance": prov})
    return questions


# ── Build ────────────────────────────────────────────────────────────────────

def main() -> int:
    files = [f for f in sorted(DOCS.rglob("*.md")) if f.name != "index.md"]
    if not files:
        print("No documents found under docs/", file=sys.stderr)
        return 2

    OUT.mkdir(parents=True, exist_ok=True)
    chunks, citations, questions = [], [], []

    for f in files:
        raw = f.read_text(encoding="utf-8")
        m = FM_RE.match(raw)
        fm = yaml.safe_load(m.group(1)) if m else {}
        if not isinstance(fm, dict):
            fm = {}
        body = raw[m.end():] if m else raw
        meta = {k: fm.get(k) for k in META_FIELDS}
        doc_id = meta.get("id") or f.stem
        doc_title = meta.get("title") or doc_id
        sections = dict(split_h1(body))
        refs = parse_references(sections)

        # Emit the per-document citation records once.
        for n in sorted(refs):
            citations.append({"doc_id": doc_id, **refs[n]})

        def base(section, subsection, text, layer, kind, extra=None):
            head = f"{doc_title} > {section}"
            if subsection:
                head += f" > {subsection}"
            gist = lead_sentence(text)
            rec = {
                "doc_id": doc_id, "doc_title": doc_title,
                "section": section, "subsection": subsection,
                "layer": layer, "kind": kind,
                "text": text,
                "context_header": head + (f" — {gist}" if gist else ""),
                "tokens_estimate": est_tokens(text),
                "provenance": None,
                "citations": resolve_citations(text, refs),
                "frameworks": detect_frameworks(text + " " + doc_title),
                "source_path": f.as_posix(),
            }
            rec.update({k: (", ".join(map(str, v)) if isinstance(v, list) else v)
                        for k, v in meta.items()})
            if extra:
                rec.update(extra)
            return rec

        for section, sec_text in split_h1(body):
            layer = SECTION_LAYER.get(section, "other")
            if layer in ("control", "reference"):
                continue                       # dropped / captured as citations

            if section == "Question Bank":
                for qi, q in enumerate(split_questions(sec_text)):
                    if est_tokens(q["text"]) < 4:
                        continue
                    cid = f"{doc_id}#q{qi:03d}"
                    rec = base(section, q["subsection"], q["text"],
                               "question", "question",
                               {"provenance": q["provenance"]})
                    rec["chunk_id"] = cid
                    chunks.append(rec)
                    questions.append({
                        "chunk_id": cid, "doc_id": doc_id,
                        "competency": meta.get("category"),
                        "topic": meta.get("topic"),
                        "level": q["subsection"],
                        "provenance": q["provenance"],
                        "frameworks": rec["frameworks"],
                        "market": meta.get("market"),
                        "citations": rec["citations"],
                        "text": q["text"],
                    })
                continue

            # Prose sections: split on `##`, window if a sub-section is huge.
            pieces = split_h2(sec_text) if layer in PROSE_LAYERS else [(None, sec_text)]
            ci = 0
            for sub, ptext in pieces:
                for w in window_paragraphs(ptext):
                    if est_tokens(w) < 8:
                        continue
                    rec = base(section, sub, w, layer, "prose")
                    rec["chunk_id"] = f"{doc_id}#{slug(section)}#{ci:02d}"
                    chunks.append(rec)
                    ci += 1

    # Stable ordering for deterministic diffs.
    chunks.sort(key=lambda c: c["chunk_id"])
    citations.sort(key=lambda c: (c["doc_id"], c["n"]))
    questions.sort(key=lambda q: q["chunk_id"])

    def dump(name, rows):
        p = OUT / name
        with p.open("w", encoding="utf-8") as fh:
            for r in rows:
                fh.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n")

    dump("chunks.jsonl", chunks)
    dump("citations.jsonl", citations)
    dump("questions.jsonl", questions)

    # Facet vocabularies (sorted) so an agent can discover valid filter values.
    def vocab(rows, key):
        vals = set()
        for r in rows:
            v = r.get(key)
            if isinstance(v, list):
                vals.update(v)
            elif v:
                vals.add(v)
        return sorted(vals)

    manifest = {
        "version": 2,
        "documents": len(files),
        "chunks": len(chunks),
        "questions": len(questions),
        "citations": len(citations),
        "total_tokens_estimate": sum(c["tokens_estimate"] for c in chunks),
        "layers": {L: sum(1 for c in chunks if c["layer"] == L)
                   for L in sorted({c["layer"] for c in chunks})},
        "question_provenance": {
            "sourced": sum(1 for q in questions if q["provenance"] == "sourced"),
            "composed": sum(1 for q in questions if q["provenance"] == "composed"),
            "unlabelled": sum(1 for q in questions if not q["provenance"]),
        },
        "facets": {
            "layer": vocab(chunks, "layer"),
            "framework": vocab(chunks, "frameworks"),
            "market": vocab(chunks, "market"),
            "category": vocab(chunks, "category"),
            "confidence": vocab(chunks, "confidence"),
            "competency": vocab(questions, "competency"),
        },
        "chunk_fields": sorted(chunks[0].keys()) if chunks else [],
        "note": "v2 structure-aware export. Chunk by section kind; questions are "
                "atomic and provenance-tagged; [n] markers resolved to sources; "
                "control/reference sections excluded from chunks.jsonl. Prepend "
                "context_header before embedding. Regenerate with "
                "scripts/build_rag.py.",
    }
    (OUT / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8")

    print(f"Wrote exports/rag/: {len(chunks)} chunks, {len(questions)} questions, "
          f"{len(citations)} citations from {len(files)} documents "
          f"(~{manifest['total_tokens_estimate']:,} tokens).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
