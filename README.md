# UK & EU Competency-Based Interview Knowledge Base

Evidence-based, source-cited reference on competency-based interviews in the
UK & EU — frameworks, practice question banks, answer techniques, and
assessment best practice for **candidates** preparing and **interviewers/HR**
designing and scoring.

> **Not careers or legal advice.** Framework and process facts are cited to
> official and authoritative sources; answer guidance and composed practice
> questions are labelled as such. Employers change their frameworks — verify
> against the current guidance for your target employer before relying.

## What's inside

- `docs/` — the knowledge-base documents, one folder per category:
  Competencies · Techniques · UK Frameworks · EU Frameworks · Formats ·
  Best Practice.
- `MASTER_INDEX.md` — the catalogue of record and knowledge graph.
- `SOURCE_REGISTRY.md` — the ranked source-authority list every citation
  follows (GOV.UK / EPSO / legislation → ACAS / CIPD / BPS → public careers
  services → academic → practitioner).
- `exports/` — machine-readable artefacts: knowledge graph (JSON + Mermaid),
  document matrix (CSV/JSON), coverage report, and a **structure-aware RAG
  export** (`exports/rag/`).

## Retrieval (RAG) for agentic use

`scripts/build_rag.py` produces a retrieval export that exploits the KB's
structure rather than flattening it:

- **`chunks.jsonl`** — chunked by section *kind*: one chunk per practice
  question (atomic, provenance-tagged), prose split on `##` sub-headings, control
  sections dropped. Each chunk carries a `layer`
  (`evidence`/`coaching`/`question`/…), `frameworks`, resolved `citations`
  (`[n]` → publisher/title/URL), a `confidence`, and a deterministic
  `context_header` to prepend before embedding.
- **`questions.jsonl`** — the 1,418 questions as a faceted index
  (competency × level × framework × provenance).
- **`citations.jsonl`** — per-document `[n]` → source records (verification).
- **`manifest.json`** — counts, schema, and the facet vocabularies.

`scripts/rag_query.py` is a dependency-free reference retriever (pure-Python
BM25 + metadata filters + knowledge-graph expansion + citation resolution):

```bash
# passage search, evidence layer only, with graph expansion
python scripts/rag_query.py "how are behaviours scored" \
    --layer evidence --framework civil-service -k 5 --expand

# faceted question picker (for building a mock interview)
python scripts/rag_query.py --questions \
    --competency Competencies --provenance sourced -k 5 "conflict in a team"

python scripts/rag_query.py --facets      # discover valid filter values
python scripts/rag_query.py ... --json     # machine-readable output for agents
```

Dense embeddings plug in via reciprocal-rank fusion over `context_header + text`
without changing the filters, graph expansion, or citation resolution — see the
header of `scripts/rag_query.py`.

## Quality gates

Every document passes four automated gates before merge, enforced locally and
in CI (`.github/workflows/qa.yml`):

1. `scripts/validate.py` — front matter, 20-section structure, citation
   integrity ([n] markers contiguous and fully resolved).
2. `scripts/audit_genre.py --strict` — evidence sections cite; every practice
   question carries a *(sourced)* [n] or *(composed)* provenance label.
3. `markdownlint-cli2` — style.
4. `scripts/check_links.py` — 0 dead links (bot-blocking hosts warn only).

## Local development

```bash
pip install pyyaml mkdocs-material
python scripts/validate.py
python scripts/audit_genre.py --strict
python scripts/build_graph.py && python scripts/build_rag.py
python scripts/build_site.py && mkdocs serve
```

## Licence & provenance

Produced by an automated, human-gated research pipeline. Each document's front
matter records its version, confidence rating, source-verification date and
revision history.
