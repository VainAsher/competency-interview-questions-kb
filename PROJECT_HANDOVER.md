# Project Handover

How to pick this project up cold.

## What this is

An evidence-based reference knowledge base on **competency-based interview
questions and best practice in the UK & EU**, for both candidates and
interviewers/HR. Built by a multi-agent pipeline: an orchestrator spawns one
worker per document; workers follow `prompts/worker_contract.md` verbatim and
return machine-readable JSON; the orchestrator owns all shared files, git and
releases.

## The rules that matter

Read `CLAUDE.md` first — the genre rule (evidence vs coaching, question
provenance) and process rules (one writer per file, QA gates, human gate,
freeze/version/release) are binding.

## Key files

- `MASTER_INDEX.md` — catalogue of record + knowledge-graph edges + backlog.
- `SOURCE_REGISTRY.md` — ranked source authorities + registered sources.
- `templates/document_template.md` — the 20-section skeleton (validator-enforced).
- `scripts/` — `validate.py`, `audit_genre.py`, `check_links.py` (QA gates);
  `build_graph.py`, `build_rag.py`, `build_site.py` (generated artefacts).
- `.github/workflows/qa.yml` — CI gates; `pages.yml` — MkDocs Material publish.

## Operating loop (per cluster)

1. Pick the next cluster from the `MASTER_INDEX.md` backlog.
2. Spawn one worker per document with the contract + scope; workers self-gate.
3. Orchestrator merges JSON returns into shared files, re-runs all four gates
   independently (including `check_links.py` — 0 dead links).
4. Human gate → freeze docs at v1.0.0, `git tag`, update status/changelog.
5. Repeat. Publishing to GitHub/Pages only on explicit authorization.
