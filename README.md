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
  document matrix (CSV/JSON), coverage report, section-level RAG export.

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
