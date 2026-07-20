# Changelog

All notable changes to this knowledge base.

## rag-v2.1 — 2026-07-20 — dense embeddings + hybrid (RRF) retrieval

Optional layer; the BM25 core stays zero-dependency and unchanged.

### Added

- **`scripts/embeddings.py`** — pluggable embedding providers with graceful
  precedence `openai → local → hash`: OpenAI `text-embedding-3-small` (1536-d),
  sentence-transformers `all-MiniLM-L6-v2` (384-d, offline), and a deterministic
  hashing fallback (256-d, no semantics — for offline plumbing/CI). All return
  L2-normalised vectors so cosine is a dot product.
- **`scripts/build_embeddings.py`** — embeds each chunk's `context_header + text`
  (contextual retrieval) → `exports/rag/embeddings.npz` + `.meta.json`.
  **Git-ignored**: large, binary, model-version-dependent — deliberately outside
  the deterministic CI staleness gate.
- **`scripts/rag_query.py` `--retriever {bm25,dense,hybrid}`** — hybrid fuses the
  BM25 and dense rankings with reciprocal-rank fusion (`Σ 1/(k+rank)`, `--rrf-k`
  default 60) *after* the metadata pre-filter, so filtering/graph-expansion/
  citation-resolution are unchanged. Results annotated `[b#<rank> d#<rank>]`.
  Degrades to BM25 with a note when no index is present. Verified: on a
  paraphrase query ("avoid waffling / keep it concise") hybrid lifted the actual
  concision passage from BM25 rank 29 into the top 3 via the dense ranking.
- CI smoke-tests the fusion path offline with the hash provider; README
  documents providers and usage.

## rag-v2 — 2026-07-20 — structure-aware retrieval

Infrastructure, not content — no document changed.

### Added

- **`scripts/build_rag.py` v2** — structure-aware RAG export replacing the flat
  one-chunk-per-section builder. Heterogeneous chunking (one chunk per practice
  question; prose split on `##` sub-headings with paragraph-window overlap;
  control/reference sections excluded). Every chunk carries a `layer`
  (evidence / coaching / question / summary / definitions / caveat / navigation),
  `frameworks`, resolved `citations` (`[n]` → publisher/title/URL from the doc's
  own References), `confidence`, and a deterministic `context_header` for
  contextual embedding. Emits `chunks.jsonl`, `questions.jsonl` (1,418 atomic
  provenance-tagged questions), `citations.jsonl`, and a faceted `manifest.json`.
  Chunk p90 dropped from ~1,678 to ~553 tokens; chunks over 1,200 tokens from
  142 to 1. Deterministic (CI staleness gate stays green).
- **`scripts/rag_query.py`** — dependency-free reference retriever: pure-Python
  BM25 + metadata pre-filters + knowledge-graph expansion + citation resolution,
  with a passage-search mode and a faceted question-picker mode. `--json` for
  agent consumption; `--facets` to discover filter vocabularies. Documents the
  reciprocal-rank-fusion extension point for dense embeddings.
- CI now smoke-tests the query tool; README documents the retrieval workflow.

## cluster6-v1.0.0 — 2026-07-20 — depth pass

### Added

- Six documents from a backlog-driven depth pass, all frozen at v1.0.0:
  Ireland / Public Appointments Service; Scotland public-sector frameworks
  (**High**); Wales & NI public-sector frameworks (**High**); neurodivergent &
  disabled candidates / adjustments; the evidence base (validity research); plus
  a report-only currency maintenance sweep.
- Knowledge base now **37 documents, 1,418 practice questions, 647 sourced**.
  11 High / 26 Medium. 104 glossary terms; ~230 registered sources.
- Closes the biggest scope gap: **Ireland** (previously EPSO-only EU coverage)
  and the **devolved UK nations** (previously one passing mention each).

### Findings

- **Ireland launched a Civil Service Capability Framework (Feb 2024)** — seven
  dimensions, four Capabilities — coexisting with the legacy competency model.
- **Police Scotland runs its own CVF** (pre-2024 structure), not the current
  College of Policing one; **PSNI does** use the CoP CVF (adapted under licence).
- **NICS is a separate civil service** with its own 2014 framework; **Welsh
  language** is a statutorily assessed requirement; **Section 75** is a distinct
  NI equality duty.
- **The evidence base answered five open questions** — including a rigorous "no
  research located" on whether answer structure affects scores.
- **Adequate neurodiversity recruitment guidance exists** (ACAS 2025, CIPD 2024).

### Maintenance & tooling

- Currency sweep (report-only): confirmed **no KB anchor has been superseded**;
  the sought post-2018 restatement of the 2016 proportioning guidance does not
  exist. Captured Internet Archive snapshots for the retiring `hee.nhs.uk`
  citations; fixed three URL redirects; flagged new bot-blocks.
- `gov.ie` and `healthcareers.nhs.uk` added to the `check_links.py` bot-block
  allowlist (real pages, 403 to the checker).

## cluster5-v1.0.0 — 2026-07-20 — **scope complete**

### Added

- Eight Tier-4 documents, all frozen at v1.0.0: STAR in depth (**High**),
  alternative answer frameworks, building an evidence bank, follow-up and
  probing questions (**High**), scoring and marking (**High**), common mistakes
  and recovery (**High**), interviewer question design (**High**), fairness,
  bias and the law (**High**).
- **343 practice questions** in the new documents. **Knowledge base complete at
  32 documents, 1,234 questions, 593 sourced.** 9 High / 23 Medium.
- Directive 2000/78/EC **restored** — read in a browser after curl and WebFetch
  were confirmed blocked, closing a gap left in cluster 2.

### Fixed

- `techniques-foundation` v1.0.1 — CAR reclassified official-guidance-backed.
- `star-technique` — proportioning negative finding narrowed to "no numeric
  ratio"; re-anchored on GOV.UK; raised to High.

### Corrected in `SOURCE_REGISTRY.md`

- **CoP assessor-bias count is 19**, not the "~13" then "18" of earlier briefs
  (halo/horns and information-overload/selective-attention are each ONE barrier;
  a naive term count returns 21).
- **Classify-once is policing-scoped**, not universal — the ORCE *verbs* appear
  in both Cabinet Office and CoP guidance, but "classify each behaviour once"
  is verified only in CoP guidance.
- **No framework mandates an answer structure** — the Cabinet Office pack that
  sets the 7-point scale contains zero mnemonics.
- New trap: **WebFetch summarisation silently drops page content** (it omitted
  the entire CAR section of a GOV.UK page even when asked directly about other
  structures). Never trust a negative finding from a summarising fetch.
- New trap: `govuk-brief-guide-competencies` is **2016 and describes the
  superseded pre-2018 framework** with no withdrawal banner — answer technique
  only.

## cluster4-v1.0.0 — 2026-07-20

### Added

- Five Tier-3 documents, all frozen at v1.0.0: EPSO competency framework, EU
  institutions assessment centres, panel interviews (**High**), video &
  asynchronous interviews, assessment centre exercises.
- **218 practice questions** in the new documents; knowledge base total now
  **891 questions, 412 sourced**. 26 new glossary terms (84 total).
- **Major new regulator source:** the ICO's *Recruitment rewired* (March 2026)
  on automated decision-making in recruitment, based on 30+ employers.

### Fixed

- `formats-foundation` v1.0.0 → v1.0.1: Open Question on regulator guidance for
  algorithmic/AI scoring resolved and cited; a narrower remainder kept open.
- **`scripts/audit_genre.py` bug fixed** — the provenance regex used `[^)]*`,
  which stopped at the first `)` and *silently* reported correctly-labelled
  questions containing nested parentheses (e.g. `*(sourced: GOV.UK (Cabinet
  Office))*`) as unlabelled. Now `[^*]*`; verified against nested-parenthesis
  labels and an unlabelled control.

### Corrected in `SOURCE_REGISTRY.md`

- **The EPSO supersession mapping was overstated.** The *absence* of Leadership
  and Resilience from the current framework is verified; the mapping to
  Intrapreneurship / Self-management is **inferred** — no EPSO concordance
  exists. Registry now separates verified absence from labelled analysis.
- **EPSO framework dating is ambiguous** (2022 vs 2023) — neutral phrasing
  ("the current framework") is now mandated.
- **EPSO's current competition has no competency interview or assessment
  centre** at all (Notice EPSO/AD/427/26, Feb 2026).
- New traps recorded: EPSO's legacy test pages return 200 but are unlinked
  archive; two near-identical College of Policing filenames (one stale, one
  current); EUR-Lex serves a JS challenge that `check_links.py` cannot detect.

## cluster3-v1.0.0 — 2026-07-20

### Added

- Five Tier-3 UK framework guides, all frozen at v1.0.0: Civil Service Success
  Profiles (**High**), Civil Service Behaviours question bank, NHS values-based
  interviews, Police CVF (**High**), UK graduate schemes.
- **259 practice questions** in the new documents (144 sourced, 115 composed);
  knowledge base total now **673 questions, 323 sourced**.
- The KB's first two **High-confidence** documents.

### Fixed

- `uk-frameworks-foundation` v1.0.0 → v1.0.1: corrected the implication that
  cumulative CVF levels were a 2016-only trait (the 2024 framework states "The
  levels are cumulative", p.9), and dated the 2016→2024 transition.

### Notable findings recorded in `SOURCE_REGISTRY.md`

- The Success Profiles 1–7 scale is **central**, not departmental (see
  Corrections below).
- The Civil Service publishes **no official behaviour question bank**; the
  College of Policing publishes **no official CVF interview questions**; no major
  private-sector graduate employer publishes a full levelled competency
  dictionary. All three recorded as verified negatives.
- A **still-live but stale** College of Policing sift PDF lists abolished 2016
  competency names — registered as do-not-cite.
- An **extraction trap**: the Strengths Dictionary's strengths-to-behaviours
  mapping is multi-column and scrambles under automated PDF extraction.

## Corrections — 2026-07-20

### Fixed

- **Superseded claim corrected across eight frozen documents (v1.0.0 → v1.0.1).**
  Clusters 1–2 recorded the Success Profiles 1–7 scoring scale as
  "departmental, not universal", having found only the COPFS page. A cluster-3
  worker located Cabinet Office guidance mandating it centrally — *"Experience,
  technical skills and behaviours should be scored using the 7 point scale.
  Strengths should be scored using the 4 point scale"* — confirmed verbatim in
  three independent grade-tier packs and independently re-verified by local PDF
  text extraction before any edit was made.
- Affected: `competencies-foundation`, `teamwork-collaboration`,
  `communication-influencing`, `leadership-management`, `resilience-adaptability`,
  `integrity-values-ethics`, `customer-stakeholder-service` (plus
  `uk-civil-service-behaviour-questions`, corrected pre-freeze by its author).
- Three Open Questions resolved; residual caveats deliberately retained (central
  packs date from 2020; benchmarks remain campaign-specific; COPFS is still the
  only source publishing the seven descriptor labels).

## cluster2-v1.0.0 — 2026-07-20

### Added

- Eight Tier-2 competency deep-dives, all frozen at v1.0.0: teamwork &
  collaboration, communication & influencing, leadership & managing others,
  problem-solving & decision-making, delivering results & planning, resilience
  & adaptability, integrity & values, customer & stakeholder service.
- **322 practice questions** across the cluster (133 sourced with same-line
  citations, 189 composed and labelled).
- 30 new glossary terms (58 total); 16 new registered sources, including the
  College of Policing 2024 CVF framework PDF, EUR-Lex EPSO competition notices,
  the Civil Service Code, the Nolan Principles, and two NHS trust
  values-based question banks.

### Changed

- `SOURCE_REGISTRY.md` now records framework-currency warnings: the 2024 police
  CVF renaming and asset-path correction, and EPSO's 2023 replacement of the
  Leadership competency with Intrapreneurship.

## cluster1-v1.0.0 — 2026-07-20

### Added

- Six Tier-1 foundation documents, all frozen at v1.0.0: Competencies,
  Techniques (STAR and beyond), UK Frameworks, EU Frameworks (EPSO), Interview
  Formats & Assessment Methods, Best Practice. All four QA gates green;
  83/83 unique URLs independently re-verified live.
- Merged catalogue (`MASTER_INDEX.md`), knowledge graph (56 edges), 29-term
  glossary, and 60+-source registry from worker returns.

## [Unreleased]

### Added

- 2026-07-19 — Repo scaffolded from the KB-factory chassis; genre adapted to
  reference (20-section template, question provenance labels); governance
  files and proposed taxonomy created; scope approved same day.
