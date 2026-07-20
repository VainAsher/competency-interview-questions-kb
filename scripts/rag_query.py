#!/usr/bin/env python3
"""
Reference retrieval tool over the structure-aware RAG export (build_rag.py v2).

This is a *reference implementation*, not a production service — it shows how
the export is meant to be used: lexical ranking fused with the metadata and
graph structure the knowledge base already carries, with citations resolved so
every hit is verifiable. It is pure-Python (only PyYAML elsewhere in the repo;
this file needs nothing beyond the standard library) so it runs anywhere the
rest of the pipeline runs.

Two retrieval modes:

  1. PASSAGE SEARCH — BM25 over chunk text + context header, narrowed by metadata
     filters (layer / framework / market / confidence / provenance / kind), with
     optional knowledge-graph expansion to neighbouring documents.

       python scripts/rag_query.py "how are behaviours scored" \
           --layer evidence --framework civil-service -k 5 --expand

  2. QUESTION PICKER — faceted retrieval over the atomic question index, the way
     an agent building a mock interview actually queries it (competency x level
     x framework x provenance), optionally BM25-ranked by a theme string.

       python scripts/rag_query.py --questions \
           --competency Competencies --framework civil-service \
           --provenance sourced -k 5 "conflict in a team"

Add --json for machine-consumable output (the shape an agent tool would return).

WHERE DENSE EMBEDDINGS PLUG IN
------------------------------
This tool ranks lexically (BM25). The corpus is dense with exact-match terms —
"Managing a Quality Service", "s.60", "EPSO/AD/427/26", "ORCE" — that lexical
search handles well, which is why BM25 alone is a strong, dependency-free
baseline. To add semantic recall, embed each chunk's `context_header + text`
(the header is a deterministic contextual prefix, already built for this), then
fuse the dense ranking with the BM25 ranking below via reciprocal-rank fusion:
    fused[id] = sum(1 / (60 + rank_in_each_list)).
The metadata pre-filter (`apply_filters`) should run *before* both rankers so the
candidate set is already scoped. That is the only change needed; everything else
here — filters, graph expansion, citation resolution — is retriever-agnostic.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import defaultdict
from pathlib import Path

# The corpus contains em-dashes and curly quotes; on Windows stdout defaults to
# cp1252 and would crash. Force UTF-8 and never fail on an un-encodable glyph.
try:  # pragma: no cover
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # pragma: no cover
    pass

RAG = Path("exports/rag")
GRAPH = Path("exports/knowledge-graph.json")
TOKEN_RE = re.compile(r"[a-z0-9]+")
K1, B = 1.5, 0.75


def load_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall(text.lower())


# ── BM25 (pure Python) ───────────────────────────────────────────────────────

class BM25:
    def __init__(self, docs_tokens: list[list[str]]):
        self.docs = docs_tokens
        self.N = len(docs_tokens)
        self.len = [len(d) for d in docs_tokens]
        self.avg = (sum(self.len) / self.N) if self.N else 0.0
        df: dict[str, int] = defaultdict(int)
        self.tf: list[dict[str, int]] = []
        for d in docs_tokens:
            counts: dict[str, int] = defaultdict(int)
            for t in d:
                counts[t] += 1
            self.tf.append(counts)
            for t in counts:
                df[t] += 1
        self.idf = {t: math.log(1 + (self.N - n + 0.5) / (n + 0.5)) for t, n in df.items()}

    def score(self, query: list[str], i: int) -> float:
        if not self.avg:
            return 0.0
        s, tf, dl = 0.0, self.tf[i], self.len[i]
        for t in query:
            f = tf.get(t, 0)
            if not f:
                continue
            s += self.idf.get(t, 0.0) * (f * (K1 + 1)) / (f + K1 * (1 - B + B * dl / self.avg))
        return s


# ── Filtering ────────────────────────────────────────────────────────────────

def apply_filters(chunks: list[dict], a) -> list[dict]:
    out = []
    for c in chunks:
        if a.layer and c.get("layer") != a.layer:
            continue
        if a.kind and c.get("kind") != a.kind:
            continue
        if a.provenance and c.get("provenance") != a.provenance:
            continue
        if a.confidence and (c.get("confidence") or "").lower() != a.confidence.lower():
            continue
        if a.market and a.market.lower() not in (c.get("market") or "").lower():
            continue
        if a.doc and a.doc not in (c.get("doc_id") or ""):
            continue
        if a.framework:
            fw = set(c.get("frameworks") or [])
            if not set(a.framework) & fw:
                continue
        if a.category and (c.get("category") or "").lower() != a.category.lower():
            continue
        out.append(c)
    return out


def snippet(text: str, width: int = 220) -> str:
    t = re.sub(r"\s+", " ", text).strip()
    return t if len(t) <= width else t[:width - 1] + "…"


def fmt_citations(cits: list[dict]) -> str:
    if not cits:
        return ""
    parts = [f"[{c['n']}] {c.get('publisher') or ''} — {c.get('url') or ''}".strip(" —")
             for c in cits]
    return "  cites: " + " · ".join(parts)


# ── Graph expansion ──────────────────────────────────────────────────────────

def neighbours(doc_ids: set[str], rels: set[str] | None = None) -> list[tuple[str, str, str]]:
    if not GRAPH.exists():
        return []
    g = json.loads(GRAPH.read_text(encoding="utf-8"))
    out = []
    for e in g.get("edges", []):
        if e.get("target") != "known":
            continue
        rel = e.get("rel", "related")
        if rels and not (set(rel.split("; ")) & rels):
            pass
        if e["from"] in doc_ids and e["to"] not in doc_ids:
            out.append((e["from"], rel, e["to"]))
        elif e["to"] in doc_ids and e["from"] not in doc_ids:
            out.append((e["to"], "rev:" + rel, e["from"]))
    seen, uniq = set(), []
    for a, r, b in out:
        if (a, b) in seen:
            continue
        seen.add((a, b))
        uniq.append((a, r, b))
    return uniq


def representative_chunk(chunks: list[dict], doc_id: str) -> dict | None:
    prefer = ["Executive Summary", "Core Reference", "Framework Context"]
    cand = [c for c in chunks if c["doc_id"] == doc_id]
    for section in prefer:
        for c in cand:
            if c.get("section") == section:
                return c
    return cand[0] if cand else None


# ── Modes ────────────────────────────────────────────────────────────────────

def passage_search(chunks: list[dict], a) -> None:
    pool = apply_filters(chunks, a)
    if not pool:
        print("No chunks match those filters.")
        return
    q = tokenize(a.query or "")
    if q:
        bm = BM25([tokenize(c["context_header"] + " " + c["text"]) for c in pool])
        scored = sorted(((bm.score(q, i), c) for i, c in enumerate(pool)),
                        key=lambda x: -x[0])
    else:
        scored = [(0.0, c) for c in pool]
    top = scored[:a.k]

    if a.json:
        out = [{"score": round(s, 3), **{k: c[k] for k in
                ("chunk_id", "doc_id", "section", "subsection", "layer",
                 "provenance", "frameworks", "confidence", "citations", "text")}}
               for s, c in top]
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return

    for rank, (s, c) in enumerate(top, 1):
        sub = f" › {c['subsection']}" if c.get("subsection") else ""
        prov = f" · {c['provenance']}" if c.get("provenance") else ""
        fw = f" · {', '.join(c['frameworks'])}" if c.get("frameworks") else ""
        print(f"\n[{rank}] {s:5.2f}  {c['doc_id']} › {c['section']}{sub}")
        print(f"      {c['layer']}{prov}{fw} · {c.get('confidence','?')} · {c['chunk_id']}")
        print(f"      {snippet(c['text'])}")
        cit = fmt_citations(c.get("citations") or [])
        if cit:
            print("     " + cit)

    if a.expand and top:
        top_docs = {c["doc_id"] for _, c in top[:3]}
        nb = neighbours(top_docs)
        if nb:
            print("\n── graph expansion (neighbouring documents) ──")
            for src, rel, dst in nb[:a.k]:
                rc = representative_chunk(chunks, dst)
                if rc:
                    print(f"  {src} —{rel}→ {dst}")
                    print(f"      {snippet(rc['text'], 160)}")


def question_picker(chunks: list[dict], a) -> None:
    qs = [c for c in chunks if c.get("kind") == "question"]
    qs = apply_filters(qs, a)
    if a.level:
        qs = [c for c in qs if a.level.lower() in (c.get("subsection") or "").lower()]
    if not qs:
        print("No questions match those facets.")
        return
    if a.query:
        bm = BM25([tokenize(c["text"]) for c in qs])
        tq = tokenize(a.query)
        qs = [c for _, c in sorted(((bm.score(tq, i), c) for i, c in enumerate(qs)),
                                   key=lambda x: -x[0])]
    picks = qs[:a.k]

    if a.json:
        out = [{"chunk_id": c.get("chunk_id"), "doc_id": c.get("doc_id"),
                "competency": c.get("category"), "topic": c.get("topic"),
                "subsection": c.get("subsection"), "provenance": c.get("provenance"),
                "frameworks": c.get("frameworks"), "citations": c.get("citations"),
                "text": c.get("text")} for c in picks]
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return

    print(f"{len(qs)} questions match; showing {len(picks)}:\n")
    for c in picks:
        lvl = f"  [{c['subsection']}]" if c.get("subsection") else ""
        print(f"• {snippet(c['text'], 200)}")
        print(f"    {c['doc_id']} · {c.get('provenance','?')}{lvl}")
        cit = fmt_citations(c.get("citations") or [])
        if cit:
            print("   " + cit)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query", nargs="?", default="", help="free-text query / theme")
    ap.add_argument("-k", type=int, default=8, help="results to return (default 8)")
    ap.add_argument("--questions", action="store_true", help="faceted question picker mode")
    ap.add_argument("--layer", help="evidence | coaching | question | summary | definitions | caveat | navigation")
    ap.add_argument("--kind", help="prose | question")
    ap.add_argument("--framework", action="append", help="repeatable: civil-service, epso, police-cvf, nhs, ...")
    ap.add_argument("--market", help="substring match, e.g. EU or UK")
    ap.add_argument("--provenance", help="sourced | composed")
    ap.add_argument("--confidence", help="High | Medium | Low")
    ap.add_argument("--category", help="exact category, e.g. Competencies")
    ap.add_argument("--competency", dest="category", help="alias for --category (question mode)")
    ap.add_argument("--level", help="question sub-heading substring, e.g. senior")
    ap.add_argument("--doc", help="restrict to doc_id substring")
    ap.add_argument("--expand", action="store_true", help="add knowledge-graph neighbours")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--facets", action="store_true", help="print the manifest facet vocabularies and exit")
    a = ap.parse_args()

    if a.facets:
        man = json.loads((RAG / "manifest.json").read_text(encoding="utf-8"))
        print(json.dumps(man.get("facets", {}), indent=2, ensure_ascii=False))
        return 0

    chunks = load_jsonl(RAG / "chunks.jsonl")
    if not chunks:
        print("No export found — run: python scripts/build_rag.py")
        return 2

    if a.questions:
        question_picker(chunks, a)
    else:
        passage_search(chunks, a)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
