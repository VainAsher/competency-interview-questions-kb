# Project Status

**As of:** 2026-07-20

## Where we are

**The approved 32-document scope plus a depth pass are complete.** All six
clusters are frozen and tagged.

| Cluster | Contents | Docs | Tag |
|---------|----------|------|-----|
| 1 | Tier-1 category foundations | 6 | `cluster1-v1.0.0` |
| 2 | Tier-2 competency deep-dives | 8 | `cluster2-v1.0.0` |
| 3 | Tier-3 UK framework guides | 5 | `cluster3-v1.0.0` |
| 4 | EU frameworks + interview formats | 5 | `cluster4-v1.0.0` |
| 5 | Tier-4 techniques & cross-cutting | 8 | `cluster5-v1.0.0` |
| 6 | Depth pass: Ireland, devolved UK, neurodiversity, evidence base | 5 + sweep | `cluster6-v1.0.0` |

- **37 documents · 1,418 practice questions · 647 sourced with citations.**
- **11 High-confidence · 26 Medium.** No document is rated High on synthesis.
- 104 glossary terms; ~230 registered sources.
- Final gate run: validate 0 issues, genre audit clean, markdownlint 0,
  **265/267 links live, 2 allowlisted warn, 0 dead** (independently re-verified).
- Knowledge graph: 37 nodes, 277 edges, **all resolving to real documents**.
- **Coverage now genuinely UK & EU:** Ireland/PAS, Scotland, Wales, NI added;
  the currency sweep confirmed no anchor source has been superseded.

## Verified negatives (do not re-research)

- The **Civil Service publishes no official behaviour interview question bank**.
- The **College of Policing publishes no official CVF interview questions**.
- **No major UK graduate employer** publishes a full levelled competency
  dictionary; Amazon's 16 Leadership Principles are the closest.
- **No central UK or EU source publishes a numeric STAR proportioning ratio** —
  though GOV.UK does publish the *direction* ("keep the situation and task parts
  brief").
- **No published descriptors exist for the Civil Service 4-point strengths
  scale**, checked directly against the GOV.UK Strengths page.

## Corrections applied during the build

Each cut a new document version with a revision note; none was a silent edit.

- **Success Profiles 1–7 scale is CENTRAL, not departmental** — nine documents
  corrected to v1.0.1 after Cabinet Office guidance was found.
- **Cumulative CVF levels are not 2016-only** — `uk-frameworks-foundation`
  v1.0.1.
- **AI-scoring Open Question resolved** via the ICO's *Recruitment rewired* —
  `formats-foundation` v1.0.1.
- **CAR is official-guidance-backed, not university-taught** —
  `techniques-foundation` v1.0.1, `alternative-answer-frameworks` corrected.
- **STAR proportioning negative finding narrowed** — `star-technique` corrected
  and raised to High.
- **`scripts/audit_genre.py` bug fixed** — the provenance regex silently
  reported correctly-labelled questions containing nested parentheses as
  unlabelled.
- Registry errors of the orchestrator's own, corrected on evidence: the EPSO
  supersession *mapping* (inferred, not published); the GSS "single-3" rule (a
  routing trigger, not a fail threshold); the CoP bias count (19, not "~13" or
  "18"); the classify-once rule (policing-scoped, not universal).

## Open items for a human

- **Unverified and deliberately uncited:** that the 2016 CVF was "withdrawn from
  the College site in May 2025". The 1 May 2025 force deadline and 10 Mar 2025
  sift switch ARE verified.
- Central Cabinet Office scoring packs date from **2020**; no refresh located.
  Three named documents ("Success Profiles: Interview methodology", "Scoring case
  studies", "Designing Strengths Questions") sit behind Civil Service Learning —
  **an FOI request is the obvious route** and would resolve several open items.
- `govuk-brief-guide-competencies` is **dated 2016 and describes the superseded
  pre-2018 framework** with no withdrawal banner. Cited for answer technique
  only. If a post-2018 restatement is found, several caveats can be dropped.
- NHS VBR anchor framework is **2016** and its publisher (HEE) no longer exists.
  Several NHS citations sit on the retiring `hee.nhs.uk` domain — **capture
  Internet Archive snapshots**.
- `communication-influencing` has the thinnest sourcing in the KB (8 of 42
  questions sourced, 6 from one 2016 set).
- ICO recruitment/selection guidance cited is a **draft**; CoP 2018 selection
  guidance predates the 2024 CVF (framework-agnostic content only).

## Possible next steps (not committed)

Publishing to GitHub/Pages (needs explicit authorization); the ROADMAP's "later
ideas" — sector expansions, Ireland-specific frameworks, printable worksheets;
or a maintenance pass against the open items above.
