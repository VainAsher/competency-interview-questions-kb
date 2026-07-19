# AGENTS.md

Instructions for AI agents working in this repository.

- Read `CLAUDE.md` for the binding genre and process rules.
- **Workers**: follow `prompts/worker_contract.md` literally. You write exactly
  one document, self-check with the four QA gates, and return the JSON block.
  Never edit shared files (`MASTER_INDEX.md`, `GLOSSARY.md`,
  `SOURCE_REGISTRY.md`, status/roadmap/changelog files) and never run git.
- **Orchestrator**: owns shared files, git, releases, the human gate, and
  independent link re-verification (`python scripts/check_links.py` — 0 dead).
- Generated files (`exports/**`, `mkdocs.yml`, `docs/index.md`) are never
  hand-edited; regenerate with `scripts/build_graph.py`, `scripts/build_rag.py`,
  `scripts/build_site.py`.
- QA gates: `python scripts/validate.py`, `python scripts/audit_genre.py
  --strict`, `npx markdownlint-cli2 "docs/**/*.md" "*.md"`,
  `python scripts/check_links.py`.
