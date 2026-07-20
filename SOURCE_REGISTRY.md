# Source Registry

The ranked source-authority list for this knowledge base. Workers reach for
sources in this priority order and classify every reference. Only the
orchestrator edits this file; workers return new sources in their JSON reply.

## Source-priority order (highest first)

1. **UK official / statutory** — GOV.UK (Success Profiles and Civil Service
   Behaviours), Civil Service Jobs guidance, legislation.gov.uk (Equality Act
   2010), NHS England / NHS Employers, College of Policing (Competency and
   Values Framework), ICO (candidate data).
2. **EU official** — EPSO (epso.europa.eu / eu-careers.europa.eu), EUR-Lex
   (directives and regulations), official careers pages of EU institutions.
3. **Professional & advisory bodies** — ACAS, CIPD, British Psychological
   Society (BPS), Institute of Student Employers.
4. **Public careers services** — National Careers Service, Prospects,
   TARGETjobs, named university careers services.
5. **Academic** — peer-reviewed occupational-psychology literature on
   structured/competency interviews (prefer open-access or DOI links).
6. **Practitioner & user evidence** — named, dated articles; Glassdoor/Indeed
   interview-question listings (practitioner evidence only, never the sole
   source for a factual claim about an employer's process).

## Reference classes

Every citation is classified as one of: **Primary** (classes 1–2), **Professional
& Advisory** (class 3), **Practitioner & Careers** (classes 4, 6), **Academic**
(class 5), or **Further Reading** (uncited background).

## Known bot-block hosts (WARN, not FAIL, in `check_links.py`)

These serve real pages to browsers but 403 automated checkers — a human should
eyeball them periodically: glassdoor.co.uk / glassdoor.com, indeed.com /
uk.indeed.com, linkedin.com, reed.co.uk, totaljobs.com, cipd.org,
consilium.europa.eu.

Sweep-confirmed bot-blocks / rate-limits (2026-07-20): **healthcareers.nhs.uk**
now 403s automated fetchers (URL unchanged). **nationalcareers.service.gov.uk**
rate-limits rapid sequential requests by 302-ing to `/alerts/405` — standalone
requests are 200; space out NCS checks and do not mistake this for rot.
`acas-hiring-interviewing` now redirects to the same page as `acas-interviewing`
(ACAS consolidated `/hiring-someone/` into `/recruitment/`) — the two entries are
duplicates. EPSO's legacy `/en/how-to-request-specific-adjustments` now 404s
(the active `/en/reasonable-accommodations` citation is unaffected).

Observed during clusters 1–3 (not allowlisted; workers used alternatives):
**college.police.uk HTML pages** 403 automated fetchers — but the
`assets.college.police.uk` **PDFs download fine** with a browser User-Agent and
pass `check_links.py`, so cite the PDFs. **prospects.ac.uk** — confirmed repeat
block across clusters 2 and 3; treat as unreachable and use
`luminate.prospects.ac.uk`, which works fine. **pwc.co.uk** (and `pwc.com/m1`)
403 automated fetchers — PwC process claims must be attributed to the careers
service reporting them, never to PwC. **cipd.org** is allowlisted but passed
live in cluster 3; the block appears intermittent. **ise.org.uk** full-report
PDF paths return 404 — the survey is genuinely member-gated, so cite ISE's
public insight pages or Luminate reporting. Several legacy epso.europa.eu URLs
404 after EPSO's migration to eu-careers.europa.eu.

**Framework currency warnings (verified 2026-07-20):**

- The **police CVF was updated in 2024**: the 2016 *clusters* were abolished and
  competencies renamed — current names include "We collaborate" and "We support
  and inspire" (not the 2016 "We are collaborative" / "We deliver, support and
  inspire"). The 2024 **framework** PDF (with competency level descriptors) sits
  at the `2025-06/` asset path; the `2024-05/` path is the *guidance* document
  and contains no descriptors.
- **EPSO's current competency framework has no "Leadership" and no standalone
  "Resilience" competency.** Their *absence* is **verified** from the anchors
  leaflet and competition notices. **But the mapping is INFERRED, not published:**
  no EPSO concordance saying Leadership→Intrapreneurship or
  Resilience→Self-management could be located (checked 2026-07-20). Treat the
  absence as fact and the mapping as labelled analysis — earlier registry
  wording overstated this and has been corrected. The cleanest published
  evidence for the old "for administrators only" restriction is the pair of 2021
  SCBI mock exercises: the AD mock assesses six competencies *including*
  Leadership, the AST mock the same five *without* it.
- **Framework dating is genuinely ambiguous — use neutral phrasing.** EPSO's own
  2023 note says "The general competency framework (April 2022) remains valid",
  while the anchors leaflet sits at a `2023-04` asset path and calls the
  framework "new". Say **"the current framework"**; do not assert 2022 or 2023.
- **EPSO's CURRENT competition model has NO competency interview.** Notice
  EPSO/AD/427/26 (OJ C/2026/711, 5 Feb 2026) documents reasoning tests, EU
  knowledge, digital skills and a free-text essay, with **no assessment centre,
  no case study, no oral presentation, no group exercise and no interview**. Anchor-based
  marking survives only in the **written** test. Any document describing an EPSO
  competency *interview* or assessment centre as current is out of date. Note
  this also corrects the common claim that the post-2023 written test is
  "usually a case study" — that wording comes from the 2023 Information Note and
  no longer matches the generalist notice.
- **STALE-PAGE TRAP — EPSO legacy test pages are still live and return 200.**
  `eu-careers.europa.eu/en/epso-tests/{case-study, oral-presentation,
  competency-based-interview-cbi, situational-competency-based-interview-scbi}`
  all resolve, are **not linked from any current staff-category test page**, and
  the oral-presentation page still lists **pre-2023 competency names**. By
  contrast `/en/epso-tests/{group-exercise, e-tray, situational-judgement-test}`
  are 404. Treat the four survivors as archive, cite them as legacy, and never
  present them as current practice. `check_links.py` cannot detect this.
- **NHS VBR: the anchor framework is dated March 2016 and its publisher (Health
  Education England) no longer exists** — HEE merged into NHS England, which
  assumed all its activities. No successor framework has been reissued under
  NHS England branding. VBR remains operative in practice (NHS Employers
  guidance updated 23 May 2024), so cite the 2016 framework as *still
  operative but unreissued*, never as freshly current.
- **Legacy-domain risk:** several primary NHS citations resolve to
  `hee.nhs.uk`, a retirement candidate. All passed live as of 2026-07-20;
  capture Internet Archive snapshots before relying on them long-term.
- **The Civil Service publishes no official behaviour interview question bank**
  — only behaviour definitions and level descriptors. Every "Civil Service
  interview question" in circulation is third-party. Do not imply otherwise.
- **EPSO removed the per-competency pass mark between 2021 and 2022.**
  `eurlex-epso-ad-389-21` sets "3/10 per competency and 40/80 in total";
  `eurlex-epso-ad-399-22` states "There is no pass mark per competency" while
  keeping 40/80 overall. Pass marks are **notice-specific and perishable** —
  never generalise one competition's thresholds to another. Both verified
  in-browser 2026-07-20.
- **No framework mandates an answer structure.** Full-text extraction of
  `co-sp-delegated-grades-2020` confirms **zero occurrences of STAR or any
  answer mnemonic**, while that same document sets the 7-point scale. Assessors
  score evidence against criteria, not adherence to a mnemonic. Official
  guidance *offers* structures (`govuk-brief-guide-competencies` names both STAR
  and CAR) but never requires one.
- **Prepared notes: processes genuinely diverge — do not generalise.** Notes are
  *permitted as reference material* at a COPFS Success Profiles interview, but
  using prepared notes or scripts can trigger an **automatic fail** in the
  College of Policing online assessment process (`cop-oap-candidate-guidance-2024`),
  awarded by an independent QA team regardless of exercise performance and **not
  appealable**. Both verified; this is a real process divergence, not a sourcing
  error. Always check the specific process.
- **ORCE is not policing-only — but the classify-once rule IS. Keep these
  separate.**
  - *Both authorities:* the five ORCE verbs appear in Cabinet Office panel
    guidance and College of Policing guidance alike — "observe, record,
    classify, evaluate and score each question independently". The convergence
    of two independent UK authorities is itself strong evidence.
  - *Policing only:* "**Classify each behaviour once – do not double count**"
    and evaluation on "the quality and quantity of the classified evidence" are
    verified verbatim in `cop-vbr-selection-2018` Appendix 1 **only**. No
    equivalent instruction has been located in Civil Service, EPSO or NHS
    assessor guidance (checked 2026-07-20).
  - Therefore: present classify-once as **strongly evidenced for CVF-based
    assessment and a reasonable working assumption elsewhere** — never as a
    universal rule. Earlier cluster briefs stated it too broadly.
- **CORRECTION (2026-07-20): the Success Profiles 1–7 scale IS central.**
  Clusters 1–2 recorded it as departmental because only the COPFS page had been
  found. Cabinet Office guidance states verbatim that "Experience, technical
  skills and behaviours should be scored using the 7 point scale. Strengths
  should be scored using the 4 point scale", and the identical sentence appears
  in three independent grade-tier packs (EO–G6, Deputy Director, Director).
  Cite `co-sp-delegated-grades-2020` as the authority; COPFS is a departmental
  *publication of* that central scale. Frozen cluster-1/2 documents describing
  the scale as "departmental, not Civil-Service-wide" carry a superseded claim —
  see the corrections backlog in `PROJECT_STATUS.md`.
- **GOV.UK data-quality issue:** the *Success Profiles: Candidate Overview* page
  repeats the Behaviours definition against **Technical**. The Strengths
  Dictionary carries the correct wording ("the demonstration of specific
  professional skills, knowledge or qualifications"). Prefer the Dictionary.
- **Fetcher notes:** `civil-service-careers.gov.uk` returns a title-only shell to
  WebFetch — **workaround: `curl` with a browser User-Agent returns full content**.
  `ico.org.uk` 403s **WebFetch** but serves `curl` with a browser UA — note
  `check_links.py` passes ICO URLs cleanly, so this is a *reading* obstacle
  only, not a link-gate failure; don't annotate ICO citations as blocked.
  EPSO's remotely-proctored-testing page 403s even with a browser UA — do not cite.
- `equalityhumanrights.com` (EHRC) returns 403 to `check_links.py` — name the
  EHRC in prose rather than citing it, or use an archive snapshot.
- **EUR-Lex — worse than a normal block, and INVISIBLE TO THE LINK GATE.**
  EUR-Lex now serves an AWS WAF JavaScript challenge (HTTP 202 + challenge page)
  to both `curl` and WebFetch, on HTML *and* PDF endpoints; the
  `publications.europa.eu` mirror returned 400. **Only a real browser
  (claude-in-chrome) worked.** Critically, `check_links.py` still reports these
  URLs as live, so the gate gives no warning — a worker will believe the URL is
  fine and then be unable to read it. Budget for browser retrieval when citing
  EUR-Lex, and never cite an OJ notice you have not actually opened.
  `assets.publishing.service.gov.uk` PDFs need local text extraction (curl +
  pdftotext/pypdf) rather than WebFetch, which reports them as unreadable binary.
- **STALE-DOCUMENT TRAP — College of Policing, two near-identical filenames.**
  Both live, both at the `2024-09/` path, both "v3.2" — **read the filename
  character by character**:
  - ❌ **STALE, do not cite:** `Online-assessments-candidate-guide-v3.2.pdf`
    (*assessment**s**… guide*; internally labelled v3.1). Still lists the
    abolished *2016* competency and value names (integrity, transparency,
    impartiality, "deliver, support and inspire") for the sift.
  - ✅ **CURRENT, cite this:** `Online-assessment-process-candidate-guidance-v3.2.pdf`
    (*assessment **process**… guidance*) = `cop-oap-candidate-guidance-2024`.
    Verified by local text extraction to use the 2024 CVF names throughout.
  Also use `cop-national-sift-guidance-2026` — note its PDF is internally dated
  May 2026 but sits at the `2025-02/` asset path with a 2025 copyright line;
  the key name is correct, the path is not a typo.
- **CVF 2016 → 2024 transition dates.** *Verified:* force transition deadline
  **1 May 2025** (College news article + CVF main page, both via Internet
  Archive — note this is NOT stated on the "Using the CVF in assessments" page);
  College national sift exercises switched to CVF 2024 on **10 March 2025**
  (`cop-using-cvf-assessments-2025`). *Unverified — do not cite:* a claim that
  the 2016 version was "withdrawn from the College site in May 2025" circulated
  during cluster 3 but could not be corroborated; every Wayback snapshot of the
  CVF main page after Feb 2025 captured a 403 block page rather than content.
  Levels are cumulative in **both** versions ("The levels are cumulative",
  2024 framework p.9) — never present cumulativeness as a 2016-only trait.
- **TOOLING TRAP — WebFetch summarisation can silently DROP page content.** On
  `gov.uk/guidance/a-brief-guide-to-competencies`, WebFetch returned only the
  STAR block and omitted the CAR section entirely, **even when asked directly
  whether the page named any other structure**. The section is present in the
  HTML. This is a silent content-omission failure, distinct from a bot block or
  a PDF-extraction trap: the fetch appears to succeed. **Never trust a negative
  finding about a page's contents from a summarising fetch — extract raw HTML
  before concluding "the source does not mention X".**
- **How to verify a diagram-bearing PDF.** Two traps in this KB
  (`cs-strengths-dictionary` mapping table, `barnsley-vbr-candidates` 70/30
  bracket) are cases where text extraction yields a *plausible but wrong*
  reading from multi-column or bracketed layout. Text extraction alone is not
  sufficient for any figure, bracket or table. In this environment `pdftoppm`
  and `pdftotext -bbox` are unavailable; **PyMuPDF (`fitz`) render-to-PNG then
  Read the image** is the working route. Use it before quoting any layout-bearing
  element.
- **EXTRACTION TRAP — Strengths Dictionary mapping table.** The official
  strengths-to-behaviours mapping (`cs-strengths-dictionary`, p.7) is laid out in
  multiple columns. Automated PDF text extraction interleaves the headings and
  bullet groups, producing a *plausible but wrong* mapping (e.g. "Mediator"
  appears under Managing a Quality Service, which is a column-order artefact).
  The 36 strength definitions extract fine; **the mapping table must be verified
  visually in a browser before any document reproduces it.**

Prefer link-checkable alternatives where possible: gov.uk, epso.europa.eu /
eu-careers.europa.eu, legislation.gov.uk, acas.org.uk, Internet Archive
snapshots.

## Registered sources

### Primary — UK official / statutory

| Key | Source | Publisher | URL |
|-----|--------|-----------|-----|
| govuk-success-profiles | Success Profiles (collection) | GOV.UK (Cabinet Office) | https://www.gov.uk/government/publications/success-profiles |
| govuk-sp-candidate-overview | Success Profiles: Candidate Overview | GOV.UK (Cabinet Office) | https://www.gov.uk/government/publications/success-profiles/success-profiles-candidate-overview |
| govuk-sp-behaviours | Success Profiles: Civil Service Behaviours | GOV.UK (Cabinet Office) | https://www.gov.uk/government/publications/success-profiles/success-profiles-civil-service-behaviours |
| govuk-cs-behaviours-pdf | Success Profiles — Civil Service Behaviours (**PDF**): complete Level 1–6 descriptors for all nine behaviours in one document. Prefer this over the HTML page, which truncates for automated fetchers. **Do not use** the `media/5b27cf2240f0b634b469fb1a/` path — it returns HTTP 410 Gone. | Civil Service HR / GOV.UK | https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1004397/CS_Behaviours_2018.pdf |
| cshr-sp-guide-eo | HR Success Profile Guides: Executive Officer (EO) — source for the "no more than four behaviours per role" recommendation | Civil Service HR | https://assets.publishing.service.gov.uk/media/5f746b188fa8f51890c6ba59/Success_Profile-EO_Collection_v0f.pdf |
| cshr-sp-guide-seo-heo | HR Success Profile Guides: SEO/HEO | Civil Service HR | https://assets.publishing.service.gov.uk/media/5f746b19e90e0740c86c7614/Success_Profile-SEO_HEO_Collection_v0e.pdf |
| cshr-sp-guide-g6-g7 | HR Success Profile Guides: Grade 6/Grade 7 — four-behaviour recommendation; six-month learnability benchmark | Civil Service HR | https://assets.publishing.service.gov.uk/media/5f746b198fa8f5188883f2e0/Success_Profile-G6_7_Collection_v0e.pdf |
| dwp-digital-ace-interview | How to ace your job interview (Barry Traish) — four to six questions on advertised essential criteria | DWP Digital Careers | https://careers.dwp.gov.uk/how-to-ace-your-job-interview/ |
| defra-digital-applications-2023 | How to improve Civil Service job applications and ace your interviews (Polly Whitworth, 14 Apr 2023) | Defra digital, data, technology and security blog | https://defradigital.blog.gov.uk/2023/04/14/how-to-improve-civil-service-job-applications-and-ace-your-interviews/ |
| govuk-sp-strengths | Success Profiles: Strengths | GOV.UK (Cabinet Office) | https://www.gov.uk/government/publications/success-profiles/success-profiles-strengths |
| csc-assessments | Assessments and Interviews | Civil Service Careers | https://www.civil-service-careers.gov.uk/assessments-and-interviews/ |
| csc-behaviours | Behaviours (candidate guidance) | Civil Service Careers | https://www.civil-service-careers.gov.uk/behaviours/ |
| cs-blog-four-steps | Four steps to success: tips for candidates (18 Nov 2024) | Civil Service blog | https://civilservice.blog.gov.uk/2024/11/18/four-steps-to-success-tips-for-candidates-applying-to-the-civil-service/ |
| co-sp-delegated-grades-2020 | Guidance: Application of Success Profile Guides during delegated grade (EO–Grade 6) recruitment (May 2020) — **the CENTRAL scoring rule**: 7-point scale for experience/technical/behaviours, 4-point for strengths; 3-point A/B/C sift; four-behaviour cap; panel reconciliation | Cabinet Office | https://assets.publishing.service.gov.uk/media/5f746b1ae90e0740caae75a7/Guidance-Application_of_Success_Profile_Guides_during_delegated_grade__EO-Grade_6__recruitment_v0b.pdf |
| co-sp-hr-deputy-director-2020 | Guidance: Application of Success Profiles during HR Deputy Director recruitment (Apr 2020) — assessment matrix; unscored ILA and SEE; same scoring scales | Cabinet Office | https://assets.publishing.service.gov.uk/media/5f746b1ad3bf7f286b3d7fcd/Guidance-Application_of_Success_Profiles_during_HR_Deputy_Director_recruitment_v0e.pdf |
| co-sp-hr-director-2020 | Guidance: Application of Success Profiles during HR Director recruitment (Apr 2020) — assessment matrix; scoring scales; leadership presentation | Cabinet Office | https://assets.publishing.service.gov.uk/media/5f746b188fa8f5189a93d144/Guidance-Application_of_Success_Profiles_during_HR_Director_recruitment_v0e.pdf |
| cs-strengths-dictionary | Success Profiles: Civil Service Strengths Dictionary — **36 named strengths with official definitions, mapped to the nine Behaviours**; also carries the corrected Technical definition and "Do not rehearse your answers" | National Crime Agency (publishing Cabinet Office material) | https://www.nationalcrimeagency.gov.uk/who-we-are/publications/661-success-profiles-strengths-dictionary/file |
| govuk-csjt | Preparing for the Civil Service Judgement Test — format, behaviours assessed, rating scale | GOV.UK | https://www.gov.uk/guidance/preparing-for-the-civil-service-judgement-test |
| govuk-work-strengths-test | Preparing for the Civil Service Work Strengths Test — three parts, five strengths by job level, percentile scoring | GOV.UK | https://www.gov.uk/guidance/preparing-for-the-civil-service-work-strengths-test |
| govuk-sp-ability | Success Profiles: Ability — verbal/numerical reasoning, automatic scoring, pass benchmark | GOV.UK (Cabinet Office) | https://www.gov.uk/government/publications/success-profiles/success-profiles-ability |
| govuk-sp-experience | Success Profiles: Experience — assessment via application and interview, STAR | GOV.UK (Cabinet Office) | https://www.gov.uk/government/publications/success-profiles/success-profiles-experience |
| govuk-sp-technical | Success Profiles: Technical — assessment methods, professional qualifications | GOV.UK (Cabinet Office) | https://www.gov.uk/government/publications/success-profiles/success-profiles-technical |
| gss-success-profiles-2019 | Guidance for the adoption of Success Profiles across the GSS (Oct 2019) — departmental: behaviour bands by grade, six-criterion cap (note the source's own typo, "recommemdation"). **Corrected 2026-07-20:** an earlier registry note called the single "3" a *failure threshold* — it is not. It is the trigger for routing a near-miss candidate into the **temporary Statistical Officer pipeline**, not a general fail rule. | Government Statistical Service | https://gss.civilservice.gov.uk/wp-content/uploads/2019/10/Success-Profiles-Guidance-GSS.pdf |
| copfs-assessment | How your application is assessed — Success Profiles. **Note:** a *departmental publication of the central scale* (see `co-sp-delegated-grades-2020`), not a departmental invention. Still the only located source publishing the seven descriptor labels. | Crown Office and Procurator Fiscal Service | https://www.copfs.gov.uk/about-copfs/careers/how-your-application-is-assessed-success-profiles/ |
| ncs-interview-tips | Interview tips | National Careers Service | https://nationalcareers.service.gov.uk/careers-advice/interview-advice |
| govuk-brief-guide-competencies | **A brief guide to competencies** (12 Apr 2016, Civil Service Resourcing) — **the strongest official STAR/CAR answer-technique anchor in the KB.** Carries the only central *proportioning* instruction found: **"Keep the situation and task parts brief. Concentrate on the action and the result"**; also "in most examples you should focus more words on the how than the what"; **"Use I not we"** with "be careful not to take credit of something that you did not do"; **"The sift panel cannot infer what is not included in the example and can only assess what you have actually written"** (a candidate-facing mirror of the ORCE classify rule); "Don't get caught up telling a story"; "use numbers and percentages whenever possible"; unsuccessful-outcome handling; and **names CAR as an alternative** ("Use either STAR or CAR approach"), while noting STAR is "the most common approach" in the Civil Service. ⚠️ **CURRENCY: dated 2016 and written for the SUPERSEDED pre-2018 framework (10 competencies, 3 clusters). Still live with no withdrawal banner. Cite for ANSWER TECHNIQUE ONLY — never for framework content.** ⚠️ **RETRIEVAL: WebFetch silently omits the proportioning, CAR and summary sections — raw HTML extraction is mandatory.** | GOV.UK (Civil Service Resourcing) | https://www.gov.uk/guidance/a-brief-guide-to-competencies |
| ncs-star-method | The STAR method | National Careers Service | https://nationalcareers.service.gov.uk/careers-advice/interview-advice/the-star-method |
| brock-soar | SOAR Technique for Job Interviews — the only *institutional* documentation of SOAR located; undated, Canadian, self-described as adapted from a 2017 Forbes article. **Cite the Internet Archive snapshot**: the live host 403s roughly one request in three under load. | Brock University CareerZone (Canada), via Internet Archive | https://web.archive.org/web/20251115061422/https://careerzone.brocku.ca/content/documents/Link/SOAR%20Interview%20Technique%20for%20Job%20Interviews.pdf |
| ncs-common-questions | How to answer common interview questions | National Careers Service | https://nationalcareers.service.gov.uk/careers-advice/top-10-interview-questions |
| govuk-civil-service-code | The Civil Service Code — the four core values (integrity, honesty, objectivity, impartiality) | GOV.UK (Cabinet Office) | https://www.gov.uk/government/publications/civil-service-code/the-civil-service-code |
| govuk-nolan-principles | The 7 principles of public life (Nolan Principles, first published 31 May 1995) | GOV.UK (Committee on Standards in Public Life) | https://www.gov.uk/government/publications/the-7-principles-of-public-life/the-7-principles-of-public-life--2 |
| csc-recruitment-principles | Recruitment Principles — programme page (selection on merit, fair and open competition) | Civil Service Commission | https://civilservicecommission.independent.gov.uk/recruitment-principles/ |
| csc-recruitment-principles-2018 | Recruitment Principles (April 2018) — **the document**, distinct from the page above: "a selection panel of two or more people must be set up"; chair must be a civil servant (or a Commissioner for the most senior competitions); conflict-of-interest declarations; recommended candidate must be first in order of merit; chair's closing record | Civil Service Commission | https://civilservicecommission.independent.gov.uk/document/02a-recruitment-principles-april-2018-final/ |
| equality-act-s149 | Equality Act 2010, s.149 (Public sector equality duty) — note s.149(7) covers eight characteristics, omitting marriage and civil partnership | legislation.gov.uk | https://www.legislation.gov.uk/ukpga/2010/15/section/149 |
| eqa2010-s39 | Equality Act 2010, s.39 (Employees and applicants) — **the provision that makes discrimination law bite on interview *design***: prohibits discrimination "in the arrangements A makes for deciding to whom to offer employment"; s.39(5) applies the adjustments duty | legislation.gov.uk | https://www.legislation.gov.uk/ukpga/2010/15/section/39 |
| eqa2010-s159 | Equality Act 2010, s.159 (Positive action: recruitment and promotion) — cumulative conditions: as-qualified-as, no standing policy of preference, proportionate means | legislation.gov.uk | https://www.legislation.gov.uk/ukpga/2010/15/section/159 |
| cop-code-of-ethics-poster-2024 | Code of Ethics: ethical policing principles (overview poster, January 2024) | College of Policing | https://assets.college.police.uk/s3fs-public/2024-01/CoE-overview-landscape-A4-poster.pdf |
| glos-nhs-vbr-toolkit | Values based recruitment toolkit: a toolkit for recruiting managers (2020 refresh) — published trust question bank | Gloucestershire Hospitals NHS Foundation Trust | https://www.gloshospitals.nhs.uk/media/documents/Recruitment_Toolkit_Managers_2020_Refresh_Digital.pdf |
| era-1996-s43b | Employment Rights Act 1996, s.43B (Disclosures qualifying for protection) — note: sexual-harassment category effective 6 Apr 2026 | legislation.gov.uk | https://www.legislation.gov.uk/ukpga/1996/18/section/43B |
| govuk-nhs-constitution | The NHS Constitution for England | GOV.UK (DHSC) | https://www.gov.uk/government/publications/the-nhs-constitution-for-england/the-nhs-constitution-for-england |
| hee-vbr-page | Values Based Recruitment (programme page). **Archive (retiring domain):** http://web.archive.org/web/20251209055542/https://www.hee.nhs.uk/our-work/values-based-recruitment | NHS England (HEE legacy site) | https://www.hee.nhs.uk/our-work/values-based-recruitment |
| hee-vbr-framework-2016 | Values Based Recruitment Framework (March 2016). **Archive:** http://web.archive.org/web/20260206085623/https://www.hee.nhs.uk/sites/default/files/documents/VBR_Framework%20March%202016.pdf | Health Education England | https://www.hee.nhs.uk/sites/default/files/documents/VBR_Framework%20March%202016.pdf |
| nhse-vbr-article | Values-based recruitment (article) | NHS Employers | https://www.nhsemployers.org/articles/values-based-recruitment |
| wuth-vbr-questions | Values Based Recruitment: example questions for recruiters to ask during job interviews (published NHS trust question bank) | Wirral University Teaching Hospital NHS Foundation Trust | https://www.wuth.nhs.uk/media/32277/values-based-interview-questions.pdf |
| compassion-in-practice-2012 | Compassion in Practice: Nursing, Midwifery and Care Staff — Our Vision and Strategy (4 Dec 2012) — origin and verbatim definitions of the 6Cs (p.13) | NHS Commissioning Board / Department of Health | https://www.england.nhs.uk/wp-content/uploads/2012/12/compassion-in-practice.pdf |
| hee-vbr-structured-interviews | VBR: How to Design and Deliver Structured Interviews for Values Based Recruitment — VBI definition, worked lead-question/probe/indicator templates, FORCE principles, trust case studies. **Archive:** http://web.archive.org/web/20250804094404/https://www.hee.nhs.uk/sites/default/files/documents/3.%20Structured%20interviews.pdf | Health Education England (with Work Psychology Group) | https://www.hee.nhs.uk/sites/default/files/documents/3.%20Structured%20interviews.pdf |
| hee-merges-nhse | HEE merges with NHS England — NHS England has assumed all activities previously undertaken by HEE. **Archive:** http://web.archive.org/web/20260509215757/https://www.hee.nhs.uk/hee-merges-with-nhs-england | NHS England (HEE legacy site) | https://www.hee.nhs.uk/hee-merges-with-nhs-england |
| barnsley-vbr-candidates | Values Based Recruitment: Guidance and Information for Candidates (April 2015) — **STAR 70/30 weighting: the bracket assigns 70% to Situation+Task+Action COMBINED and 30% to Result alone** (verified visually, p.4). ⚠️ **Extraction trap:** automated text extraction places the "70%"/"30%" markers adjacent to the Task and Action lines and supports the *opposite* reading. Verify visually before quoting. Also carries the "We will / We / We do not" behavioural framework. | Barnsley Hospital NHS Foundation Trust | https://www.barnsleyhospital.nhs.uk/sites/default/files/2023-07/values-based-recruitment-guidance-notes-for-candidates.pdf |
| lypft-vbr-pack | Values Based Recruitment: Candidate Resource Pack (ref. 24/0107, Oct 2024) — interview structure, 40–50 min duration, same values apply at every role level | Leeds and York Partnership NHS Foundation Trust | https://www.leedsandyorkpft.nhs.uk/news/wp-content/uploads/sites/4/2024/10/Values-Based-Recruitment-Resource-Brochure.pdf |
| ouh-vbi-what-to-expect | What to expect from a Value Based Interview (VBI) — two to four questions; no advance preparation needed | Oxford University Hospitals NHS Foundation Trust | https://www.ouh.nhs.uk/working-for-us/application/vbi/what-to-expect/ |
| cop-cvf-guidance-2024 | Competency and values framework guidance (2024) | College of Policing | https://assets.college.police.uk/s3fs-public/2024-05/Competency-and-values-framework-guidance.pdf |
| cop-cvf-2024-framework | Competency and values framework for policing (2024) — full framework incl. competency level descriptors (note: `2025-06/` asset path) | College of Policing | https://assets.college.police.uk/s3fs-public/2025-06/Competency-and-values-framework.pdf |
| cop-cvf-2016 | Competency and Values Framework for policing: Overview (2016) — superseded by the 2024 framework; retained for provenance | College of Policing | https://assets.college.police.uk/s3fs-public/2020-11/competency-and-values-framework-for-policing_4.11.16.pdf |
| cop-using-cvf-assessments-2025 | Using the competency and values framework in assessments (6 Feb 2025) — **authoritative per-assessment CVF-version table**; national sift switched to CVF 2024 on 10 Mar 2025. Cited via Internet Archive because college.police.uk HTML 403s. | College of Policing via Internet Archive | https://web.archive.org/web/20250214053348/https://www.college.police.uk/career-learning/competency-and-values-framework/using-competency-and-values-framework-assessments |
| cop-oap-candidate-guidance-2024 | Online assessment process: Candidate guidance (Sept 2024) — five-question competency interview, written and briefing exercises; CVF assessed per exercise; timings; appeals; resits. **Also the cleanest published evidence of probe-substitution in a no-follow-up format:** on-screen written prompts replace live probes (5 questions, 60s thinking / 300s recording, prompts shown alongside a pre-recorded assessor video). | College of Policing | https://assets.college.police.uk/s3fs-public/2024-09/Online-assessment-process-candidate-guidance-v3.2.pdf |
| cop-national-sift-guidance-2026 | National sift: Candidate guidance (May 2026) — SJT and behavioural styles questionnaire formats, rating scales, two published example SJT scenarios | College of Policing | https://assets.college.police.uk/s3fs-public/2025-02/National-sift-candidate-guidance.pdf |
| cop-vbr-selection-2018 | Values-based recruitment and selection: guidance for using the CVF in recruitment and selection (2018) — A–D rating scale, ORCE model, four-fifths rule, and **Appendix 2: NINETEEN named assessor biases** — expectancy effect, confirmatory information, personal liking, primacy, stereotyping, prototyping, halo/horns, quota, contrast, negative information bias, similar-to-me, non-verbal communication, fundamental attribution error, information overload/selective attention, fatigue, rushing, central tendency, leniency, stringency. Counter-measures are prescribed in **four groups**, not one per barrier. *Count verified by orchestrator extraction 2026-07-20 — earlier briefs said "~13" then "18", both wrong. **Miscounting is easy**: "halo/horns" is ONE barrier and "information overload/selective attention" is ONE, so a naive term count returns 21.* ⚠️ Appendix 2 is a **multi-column table whose names and descriptions extract into separate runs** — same trap class as the Strengths Dictionary; verify pairing visually before reproducing. **Predates the 2024 CVF** — use only its framework-agnostic process content. | College of Policing | https://assets.college.police.uk/s3fs-public/2020-11/Values-Based_Recruitment_Guidance-1.pdf |
| cop-nppf-step-two-handbook-2025 | NPPF step two legal examinations candidate handbook 2025 — sergeant/inspector exam format and pass marks | College of Policing | https://assets.college.police.uk/s3fs-public/2024-09/NPPF-step-two-legal-examinations-candidate-handbook-2025.pdf |
| joiningthepolice-oap | What does the online assessment process involve? | Join The Police (national police recruitment site) | https://www.joiningthepolice.co.uk/application-process/what-does-the-online-assessment-process-involve |
| devon-cornwall-cvf-interview | Force Interviews: Competency Values Framework — candidate guidance, panel format, plus explicit **"Common Mistakes" and "Myths"** slides. **Together with `hampshire-cvf-guidance` these are the only located UK sources that name candidate interview mistakes officially**, and they independently corroborate four: CVF bingo/buzzwords, wrong framework level, not answering the question, pre-empting the board. Undated, but uses 2024-CVF names so is post-transition. | Devon & Cornwall Police | https://recruitment.devon-cornwall.police.uk/media/a40ndu4b/cvf-interview-guidance.pdf |
| dyfed-powys-cvf-marking-guide | Interview Marking Guide: CVF Specialist, level 2 — what good evidence looks like | Dyfed-Powys Police | https://www.dyfed-powys.police.uk/SysSiteAssets/media/downloads/dyfed-powys/careers/New-CVF/specialist-cvf-document.pdf |
| hampshire-cvf-guidance | Transferee and Re-joiners CVF Guidance — STAR; "CVF bingo" buzzword warning. **Verified 2026-07-20 (pypdf): the bingo/buzzword warning appears in BOTH this and `devon-cornwall-cvf-interview`** — either may be cited. A cluster-5 worker reported it absent here, but that was an extraction failure, not an absence. | Hampshire Constabulary | https://www.hampshire.police.uk/SysSiteAssets/media/downloads/hampshire/careers/recruitment-documents/cvf-presentation-powerpoint.pdf |
| nhse-lcf-board-members-2024 | NHS leadership competency framework for board members (ref. B0496i, 28 Feb 2024) — six leadership competency domains | NHS England | https://www.england.nhs.uk/long-read/nhs-leadership-competency-framework-for-board-members/ |
| govuk-recruitment-adjustments | Recruitment and disabled people: Reasonable adjustments | GOV.UK | https://www.gov.uk/recruitment-disabled-people/reasonable-adjustments |
| equality-act-2010 | Equality Act 2010 (contents; Part 5: Work) | legislation.gov.uk | https://www.legislation.gov.uk/ukpga/2010/15/contents |
| equality-act-2010-s4 | Equality Act 2010, s.4 (The protected characteristics) | legislation.gov.uk | https://www.legislation.gov.uk/ukpga/2010/15/section/4 |
| equality-act-s20 | Equality Act 2010, s.20 (Duty to make adjustments) | legislation.gov.uk | https://www.legislation.gov.uk/ukpga/2010/15/section/20 |
| eqa2010-s60 | Equality Act 2010, s.60 (Enquiries about disability and health) | legislation.gov.uk | https://www.legislation.gov.uk/ukpga/2010/15/section/60 |
| ico-recruitment-selection | Employment practices and data protection: recruitment and selection (draft) | Information Commissioner's Office | https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/employment/recruitment-and-selection/ |
| ico-recruitment-rewired-2026 | **Recruitment rewired** (March 2026) — ICO report on automation in recruitment, based on 30+ employers engaged Mar 2025–Jan 2026; finds many employers likely relying on solely automated decisions | Information Commissioner's Office | https://ico.org.uk/about-the-ico/what-we-do/recruitment-rewired/ |
| ico-rewired-key-findings | Recruitment rewired: Key findings — records automated scoring of video-interview transcriptions and evaluation of language/tone/content to predict personality; records **no** observed emotion detection or biometric processing | Information Commissioner's Office | https://ico.org.uk/about-the-ico/what-we-do/recruitment-rewired/key-findings-how-are-employers-automating-their-recruitment-processes/ |
| ico-rewired-meaningful-human-involvement | Recruitment rewired: Meaningful human involvement — UK GDPR art. 22A test; "rubber-stamping" red-rated candidates constitutes solely automated decision-making | Information Commissioner's Office | https://ico.org.uk/about-the-ico/what-we-do/recruitment-rewired/key-findings-how-are-employers-automating-their-recruitment-processes/meaningful-human-involvement/ |
| ico-rewired-mhi-use-cases | Recruitment rewired: Understanding how meaningful human involvement applies — six-part test for human reviewers; worked fit-score and screening cases | Information Commissioner's Office | https://ico.org.uk/about-the-ico/what-we-do/recruitment-rewired/understanding-how-meaningful-human-involvement-applies-use-cases/ |
| ico-rewired-transparency | Recruitment rewired: Transparency and safeguards — the four art. 22C safeguards; three transparency trigger points | Information Commissioner's Office | https://ico.org.uk/about-the-ico/what-we-do/recruitment-rewired/key-findings-how-are-employers-automating-their-recruitment-processes/transparency-and-safeguards/ |
| ico-rewired-fairness | Recruitment rewired: Fairness, bias and discrimination — procurement bias-testing questions; adjustments where candidates cannot access automated methods; records vendor "fairer than humans" marketing **without endorsing it** | Information Commissioner's Office | https://ico.org.uk/about-the-ico/what-we-do/recruitment-rewired/key-findings-how-are-employers-automating-their-recruitment-processes/fairness-bias-and-discrimination/ |
| ico-jobseekers-adm-2026 | Here's what jobseekers need to know about automated recruitment decisions (news, March 2026) — candidate-facing rights; ICO wrote to 16 organisations likely using ADM | Information Commissioner's Office | https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/03/here-s-what-jobseekers-need-to-know-about-automated-recruitment-decisions/ |
| epso-specific-adjustments | **Reasonable Accommodations** (retitled; the old "How to request specific adjustments" URL now 301-redirects here) — EPSO Accessibility Team criteria; case-by-case grant | EPSO / EU Careers | https://eu-careers.europa.eu/en/reasonable-accommodations |

### Primary — EU official

| Key | Source | Publisher | URL |
|-----|--------|-----------|-----|
| epso-cf-page | EPSO's Competency Framework (overview page) | EPSO / EU Careers | https://eu-careers.europa.eu/en/documents/epsos-competency-framework/13068 |
| epso-cf-leaflet | Competency Framework Anchors (EN leaflet, 8 general competencies) | EPSO / EU Careers | https://eu-careers.europa.eu/system/files/2023-04/EN.pdf |
| epso-new-model-note | Information Note: EPSO's New Competition Model (3 May 2023) | EPSO | https://eu-careers.europa.eu/system/files/2023-02/Information_Note_New_Competition_Model.pdf |
| epso-permanent-staff | Permanent staff selection | EPSO / EU Careers | https://eu-careers.europa.eu/en/competitions-permanent-positions |
| epso-testing | EPSO testing | EPSO / EU Careers | https://eu-careers.europa.eu/en/selection-procedure/epso-tests |
| epso-cbi | Competency based interview (CBI) | EPSO / EU Careers | https://eu-careers.europa.eu/en/epso-tests/competency-based-interview-cbi |
| epso-scbi | Situational Competency Based Interview (SCBI) | EPSO / EU Careers | https://eu-careers.europa.eu/en/epso-tests/situational-competency-based-interview-scbi |
| epso-cast-competency-test | Competency-based test for each profile (CAST) | EPSO / EU Careers | https://eu-careers.europa.eu/en/epso-tests/competency-based-test-each-profile |
| epso-contract-staff | Contract staff | EPSO / EU Careers | https://eu-careers.europa.eu/en/node/134 |
| epso-faq-contract-agents | FAQ: Contract agents (FG I, II, III, IV) | EPSO / EU Careers | https://eu-careers.europa.eu/en/help/faq/contract-agents-fg-i-ii-iii-iv |
| epso-recruitment | Recruitment (from reserve lists) | EPSO / EU Careers | https://eu-careers.europa.eu/en/how-be-recruited |
| epso-faq-reserve-list | FAQ: What is a "reserve list"? | EPSO / EU Careers | https://eu-careers.europa.eu/en/help/faq/2049 |
| epso-faq-3104 | FAQ: Competencies candidates must demonstrate during competition tests | EPSO / EU Careers | https://eu-careers.europa.eu/en/help/faq/3104 |
| epso-scbi-365-370 | SCBI assignment, Open Competitions EPSO/AD/365-370/19 | EPSO | https://eu-careers.europa.eu/sites/default/files/documents/general/situational_competency-based_interview_scbi_-_assignments/365-370_assignment/en_ad_365_370_scbi_assignment_epso.pdf |
| epso-ac-faq-archive | What is an Assessment Centre? (FAQ, Internet Archive snapshot 2022-09-24) | EPSO via Internet Archive | https://web.archive.org/web/20220924171745/https://epso.europa.eu/en/help/faq/2026 |
| eurlex-epso-general-rules-2015 | General rules governing open competitions (2015/C 070 A/01) — pre-2023 general competencies incl. "Leadership (for administrators only)" | EUR-Lex / EPSO | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3AC2015%2F070A%2F01 |
| eurlex-epso-ad-399-22 | Notice of open competition EPSO/AD/399/22 — Administrators (AD 7), audit (OJ C 114A, 2022): eight general competencies, test allocation, marking 10 each, combined pass 40/80 | EUR-Lex / EPSO | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:C2022/114A/01 |
| eurlex-epso-ad-389-21 | Notice of open competition EPSO/AD/389/21 — Administrators (AD 6): eight general competencies incl. Leadership; pass 3/10 per competency, 40/80 total; competency passport | EUR-Lex / EPSO | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELLAR%3Aa114d8dd-668a-11eb-aeb5-01aa75ed71a1 |
| eurlex-epso-ad-427-26 | **Notice EPSO/AD/427/26 — Administrators (AD 5), OJ C/2026/711, 5 Feb 2026. THE CURRENT MODEL**: reasoning + EU knowledge + digital skills + free-text essay (EUFTE); **no competency interview**; 35/25/25/15 % weightings; anchor-based written-test marking; 1,490 reserve-list places | EUR-Lex / EPSO | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:C_202600711 |
| epso-written-test-anchors | What is the written test? — the five **published written-test anchors** used to mark WT / FRWT / EUFTE. Proof anchor-based marking survives the abolition of oral tests. (No source states whether these derive from the Communication competency's anchors — **do not assert that.**) | EPSO / EU Careers | https://eu-careers.europa.eu/en/help/what-written-test |
| epso-scbi-mock-ad | Situational Competency-Based Interview — MOCK exercise, AD profiles (2021): 40 minutes, six competencies **including Leadership** | EPSO / EU Careers | https://eu-careers.europa.eu/sites/default/files/documents/general/sample_tests/scbi_ad/epso_ad_scbi_ex_en_mock_webpage.pdf |
| epso-scbi-mock-ast | Situational Competency-Based Interview — mock exercise, AST profile (2021): 35 minutes, same five competencies **without Leadership**. Paired with the AD mock, the cleanest published evidence of the "administrators only" restriction. | EPSO / EU Careers | https://eu-careers.europa.eu/sites/default/files/documents/general/sample_tests/scbi_ast/epso_ast_scbi_ex_en_mock_webpage.pdf |
| epso-case-study-mock-ast | MOCK Case Study, AST profile — three published assignment tasks, 90-minute limit, full document dossier | EPSO | https://eu-careers.europa.eu/sites/default/files/documents/general/sample_tests/cs_ast/ast_cs_ex_en_mock_webpage.pdf |
| epso-ac-brochure-ad244 | EPSO Assessment Centre Brochure (competition EPSO/AD/244) — **legacy** exercise inventory and indicative durations (case study 1h30, structured interview 40 min, oral presentation 50 min, group exercise 60 min); competency-by-exercise matrix; two-assessor rule. Undated and competition-specific. | EPSO | https://europa.eu/epso/application/CotoFiles/file/AD%20244/AD_244_AC%20Brochure%20EN.pdf |
| epso-tests-graduates-ad5 | Graduates (Administrators AD5) — current test list; **no oral test listed** | EPSO / EU Careers | https://eu-careers.europa.eu/en/graduates-administrators-ad5 |
| epso-tests-specialists-ad6-ad9 | Specialists (Administrators AD6–AD9) — current written-test formats (WT / FRWT / EUFTE) and the five published marking anchors. **`/en/help/what-written-test` 301-redirects here — cite this canonical URL.** | EPSO / EU Careers | https://eu-careers.europa.eu/en/specialists-administrators-ad6-ad9 |
| epso-tests-assistants | Assistants (AST 1–AST 9) — current test list and written-test anchors | EPSO / EU Careers | https://eu-careers.europa.eu/en/assistants-ast-1-ast-9 |
| epso-tests-secretaries | Secretaries (AST/SC) — Field-Related Short Text Questionnaire (FRSTQ): 10 questions, 60 minutes | EPSO / EU Careers | https://eu-careers.europa.eu/en/secretaries-ast-sc |
| ema-application-process | Application process for Temporary and Contract Agents — interview/test durations; 3–5 person selection committee; external-provider assessment centres for managerial posts | European Medicines Agency | https://careers.ema.europa.eu/content/Application-process-for-Temporary-Agents-and-Contract-Agents/?locale=en_GB |
| eurojust-selection-process | Selection and recruitment process — interview plus written test; assessment centres for managerial selections | Eurojust | https://www.eurojust.europa.eu/about-us/jobs/selection-and-recruitment-process |
| euphorum-scbi | SCBI (EPSO preparation page) — states the SCBI replaced the group exercise; advance-booklet timing. **Practitioner claim, not EPSO-published** | Euphorum | http://www.euphorum.org/en/training/ac/scbi |
| eurlex-staff-regulations | Staff Regulations of Officials and CEOS (consolidated 2024-01-01) | EUR-Lex | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A01962R0031-20240101 |
| eurlex-2000-78 | Council Directive 2000/78/EC (equal treatment in employment and occupation) | EUR-Lex | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32000L0078 |
| eurlex-gdpr | Regulation (EU) 2016/679 (GDPR) | EUR-Lex | https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng |
| eurlex-2018-1725 | Regulation (EU) 2018/1725 (data protection by Union institutions) | EUR-Lex | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32018R1725 |

### Professional & Advisory

| Key | Source | Publisher | URL |
|-----|--------|-----------|-----|
| acas-interviewing | Interviewing job applicants | ACAS | https://www.acas.org.uk/recruitment/interviewing-job-applicants |
| acas-hiring-interviewing | Hiring someone: Interviewing job applicants | ACAS | https://www.acas.org.uk/hiring-someone/interviewing-job-applicants |
| acas-discrimination-law | Following discrimination law (Recruitment) | ACAS | https://www.acas.org.uk/recruitment/follow-discrimination-law |
| acas-neuroinclusive | Making your organisation neuroinclusive — recruitment review points; questions-in-advance worked example for autistic applicants | ACAS | https://www.acas.org.uk/neurodiversity-at-work/making-your-organisation-neuroinclusive |
| acas-adjustments-neurodiversity | Adjustments for neurodiversity — no diagnosis required; concentration/written-communication adjustment examples | ACAS | https://www.acas.org.uk/reasonable-adjustments/adjustments-for-neurodiversity |
| cipd-neuroinclusion | Neuroinclusion at work (guide, Feb 2024) — interview adjustments; "test of social competence" framing; avoid penalising body language. Bot-block host, intermittent. | CIPD | https://www.cipd.org/en/knowledge/guides/neuroinclusion-work/ |
| govuk-disability-confident-signup | Disability Confident: how to sign up to the employer scheme — three levels; Level 1 interview commitment | GOV.UK (DWP) | https://www.gov.uk/guidance/disability-confident-how-to-sign-up-to-the-employer-scheme |
| epso-ra-flyer | Step-by-step guide to requesting reasonable accommodations in EPSO selection tests (PDF, May 2025) — "no certificates no adjustments"; "compete on an equal basis" | EPSO / EU Careers | https://eu-careers.europa.eu/system/files/2025-05/EN_SpecialAdjustment.pdf |
| cipd-selection-methods | Selection methods (factsheet) | CIPD | https://www.cipd.org/en/knowledge/factsheets/selection-factsheet/ |
| cipd-selection-methods-uk | Selection methods (factsheet, UK path) | CIPD | https://www.cipd.org/uk/knowledge/factsheets/selection-factsheet/ |
| ise-recruitment-survey-2025-trends | 5 trends you need to know from ISE's Recruitment Survey 2025 | Institute of Student Employers | https://ise.org.uk/knowledge/insights/498/5_trends_you_need_to_know_from_ises_recruitment_survey_2025/ |
| ise-srs-2025 | ISE Student Recruitment Survey 2025 (landing page; report member-only) | Institute of Student Employers | https://ise.org.uk/knowledge/research/491/ise_student_recruitment_survey_2025/ |

### Primary — Ireland (Public Appointments Service)

| Key | Source | Publisher | URL |
|-----|--------|-----------|-----|
| pj-capability-overview | The Capability Framework Overview — **the 2024 framework** (four Capabilities, seven dimensions) | Public Appointments Service (publicjobs) | https://www.publicjobs.ie/en/information-hub/capability-framework |
| pj-capability-eo-page | Capability Framework: Executive Officer (per-grade page) | Public Appointments Service (publicjobs) | https://www.publicjobs.ie/en/information-hub/capability-framework/executive-officer |
| pj-capability-eo-pdf | Executive Officer Capability Framework (PDF) | Public Appointments Service (publicjobs) | https://www.publicjobs.ie/documents/CF/EOFramework.pdf |
| pj-capability-award-2025 | publicjobs wins Workforce of the Future Division, Civil Service Excellence Awards 2025 (Capability Framework, seven dimensions) | Public Appointments Service (publicjobs) | https://www.publicjobs.ie/en/information-hub/latest-news-and-events/1017-publicjobs-wins-workforce-of-the-future-division-at-civil-service-excellence-and-innovation-awards-2025 |
| pj-interview-advice | Interview Advice — interview types; competency vs capability; STAR; **published example questions** | Public Appointments Service (publicjobs) | https://www.publicjobs.ie/en/information-hub/our-recruitment-process/interview-advice |
| pj-eo-competency-legacy | Irish Civil Service Competency Models: Executive Officer Level (**legacy** model, still live per role) | Public Appointments Service (publicjobs) | https://www.publicjobs.ie/documents/Executive_Officer_Competencies.pdf |
| pj-heo-competency-legacy | Civil Service Competency Framework Model: Higher Executive Officer Level (legacy) | Public Appointments Service (publicjobs) | https://www.publicjobs.ie/images/pdfs/Higher_Executive_Officer_Level.pdf |
| pj-eo-booklet-2022 | Executive Officer 2022: Information Booklet — competition structure, selection stages, order-of-merit panel | Public Appointments Service (publicjobs) | https://www.publicjobs.ie/documents/EO_InformationBooklet_English.pdf |
| cpsa-code-2022 | Code of Practice for Appointment to Positions in the Civil and Public Service (2022) — six recruitment principles | Commission for Public Service Appointments | https://www.publicjobs.ie/documents/CPSA-Code-of-Practice-2022.pdf |
| cpsa-code-page | Code of Practice (regulator programme page) | Commission for Public Service Appointments | https://www.cpsa.ie/en/collection/8c53f-code-of-practice/ |
| garda-trainee-booklet-2025 | Garda Trainee 2025: Information Booklet — publicjobs-run competency interview + role-play. *Verified negative: the specific competencies are NOT published; the "five competencies" list circulating is third-party.* | An Garda Síochána | https://www.garda.ie/en/careers/garda-trainee-recruitment-it-s-a-job-worth-doing-campaign/information-booklet-garda-trainee-2025.pdf |
| hse-competency-guide | Guide to completing competency questions — competency-based application and interview | Health Service Executive (HSE) | https://about.hse.ie/jobs/hse-recruitment-process/guide-to-completing-competency-questions/ |
| leitrim-co-booklet-2026 | Candidate Information Booklet: Clerical Officer, Mar 2026 — local-authority competency set | Leitrim County Council | https://www.leitrim.ie/council/jobs/current-job-vacancies/candidate-information-booklet-clerical-officer-march-2026.pdf |
| psmra-2004 | Public Service Management (Recruitment and Appointments) Act 2004 — establishes PAS and the CPSA | Irish Statute Book | https://www.irishstatutebook.ie/eli/2004/act/33/enacted/en/html |
| eea-1998 | Employment Equality Act 1998 — nine grounds; discrimination in recruitment arrangements | Irish Statute Book | https://www.irishstatutebook.ie/eli/1998/act/21/enacted/en/html |
| gov-ie-capability-framework | The Civil Service Capability Framework (launched Feb 2024) — **gov.ie is bot-block allowlisted** (200 to browser, 403 to checker) | Department of Public Expenditure, Infrastructure, PSR&D | https://www.gov.ie/en/department-of-public-expenditure-infrastructure-public-service-reform-and-digitalisation/publications/the-civil-service-capability-framework/ |

### Primary — Devolved UK (Scotland)

| Key | Source | Publisher | URL |
|-----|--------|-----------|-----|
| gov-scot-sp-intro | Success profiles: candidate guide — Introduction (**Scottish Government uses Success Profiles**, "also used across the wider Civil Service"; updated 23 Jun 2026) | Scottish Government | https://www.gov.scot/publications/success-profiles-candidate-guide/pages/introduction/ |
| gov-scot-sp-about | Success profiles: candidate guide — Our recruitment framework | Scottish Government | https://www.gov.scot/publications/success-profiles-candidate-guide/pages/about-success-profiles/ |
| gov-scot-sp-behaviour-defs | Success profiles: candidate guide — Behaviour definitions (nine Civil Service Behaviours, verbatim) | Scottish Government | https://www.gov.scot/publications/success-profiles-candidate-guide/pages/behaviour-definitions/ |
| gov-scot-sp-behaviours | Success profiles: candidate guide — Behaviours (assessment methods; sift) | Scottish Government | https://www.gov.scot/publications/success-profiles-candidate-guide/pages/behaviours/ |
| gov-scot-sp-apply | Success profiles: candidate guide — Our application process | Scottish Government | https://www.gov.scot/publications/success-profiles-candidate-guide/pages/our-application-process/ |
| gov-scot-sp-assess | Success profiles: candidate guide — Our assessment process (45–60 min panel of 2–3; **questions shared in advance**; merit order; Reserve list) | Scottish Government | https://www.gov.scot/publications/success-profiles-candidate-guide/pages/our-assessment-process/ |
| gov-scot-sp-experience | Success profiles: candidate guide — Experience (**published example interview questions**) | Scottish Government | https://www.gov.scot/publications/success-profiles-candidate-guide/pages/experience/ |
| gov-scot-sp-technical | Success profiles: candidate guide — Technical skills (published example questions) | Scottish Government | https://www.gov.scot/publications/success-profiles-candidate-guide/pages/technical-skills/ |
| gov-scot-sp-supporting | Success profiles: candidate guide — Supporting Statement (STARR recommended; first person) | Scottish Government | https://www.gov.scot/publications/success-profiles-candidate-guide/pages/your-supporting-statement/ |
| gov-scot-sp-further-info | Success profiles: candidate guide — Recruitment adjustments and guaranteed interview schemes | Scottish Government | https://www.gov.scot/publications/success-profiles-candidate-guide/pages/further-information/ |
| ps-cvf | **Competency & Values Framework for Police Scotland** — "Modified with permission from © College of Policing Ltd"; retains the **pre-2024 three-cluster structure** and its own four values (Integrity, Fairness, Respect, Human Rights) from the Code of Ethics for Policing in Scotland. *Police Scotland runs its OWN CVF, not the current CoP CVF.* | Police Scotland | https://www.scotland.police.uk/spa-media/lkdivnf4/competency-and-values-framework.pdf |
| ps-recruitment-process | Our recruitment process — PSET; assessment day (group task, SJT exercise, 20-min CBI of four questions assessed against the CVF) | Police Scotland | https://www.scotland.police.uk/jobs/police-officer/our-recruitment-process/ |
| nhs-scot-everyone-matters | Everyone matters: 2020 workforce vision — the four NHSScotland values (care and compassion; dignity and respect; openness, honesty and responsibility; quality and teamwork) | Scottish Government | https://www.gov.scot/publications/everyone-matters-2020-workforce-vision/pages/3/ |
| nhs-scot-principles-values | Principles and values (NHSScotland workforce policies) | NHS Scotland | https://workforce.nhs.scot/about/principles-and-values/ |
| nhs-scot-careers-values | Your guide to our core values (1 Jul 2022; four values in recruitment; example prompts; STAR) | NHSScotland Careers | https://www.careers.nhs.scot/blog/your-guide-to-our-core-values/ |
| nhs24-values-behaviours | Values and Behaviours Framework (four values, four behavioural indicators each) | NHS 24 | https://www.nhs24.scot/careers/values-and-behaviours-framework/ |
| scts-interview-guidance | Interview guidance — competency-based interview vs person specification; **0–4 scoring per value** | Scottish Courts and Tribunals Service | https://www.scotcourts.gov.uk/about-us/careers/interview-guidance/ |
| eqa-ssi-2012-162 | The Equality Act 2010 (Specific Duties) (Scotland) Regulations 2012 (SSI 2012/162) — **Scotland-specific PSED duties** | legislation.gov.uk | https://www.legislation.gov.uk/ssi/2012/162/contents/made |
| myjobscotland-help-interviews | Help with interviews (shared Scottish local-government jobs portal) | myjobscotland | https://myjobscotland.gov.uk/help-interviews |

### Primary — Devolved UK (Wales & Northern Ireland)

| Key | Source | Publisher | URL |
|-----|--------|-----------|-----|
| gov-wales-assessment-process | Welsh Government jobs: assessment process — uses standard Success Profiles; shares opening questions ≥5 days in advance; name-free recruitment | Welsh Government (GOV.WALES) | https://www.gov.wales/welsh-government-jobs-assessment-process-html |
| gov-wales-external-candidate-guidance | Welsh Government jobs: external candidate recruitment guidance | Welsh Government (GOV.WALES) | https://www.gov.wales/welsh-government-jobs-external-candidate-recruitment-guidance-html |
| nhs-wales-values-nwssp | Values and Standards of Behaviour Framework — NHS Wales core values | NHS Wales Shared Services Partnership | https://nwssp.nhs.wales/a-wp/governance-e-manual/living-public-service-values/values-and-standards-of-behaviour-framework/ |
| heiw-vbr-policy-2022 | Values Based Recruitment & Selection Policy & Procedure (Dec 2022) — actively consider Welsh-language skills | Health Education and Improvement Wales (HEIW) | https://heiw.nhs.wales/files/values-based-recruitment-selection-policy/ |
| wlc-job-categorisation | Job categorisation and advertising — essential/desirable/need-to-learn Welsh categories; CEFR levels; assessed at interview | Welsh Language Commissioner | https://www.welshlanguagecommissioner.wales/support-resources/the-workforce/job-categorisation-and-advertising |
| senedd-official-languages-recruitment | Official Languages and Recruitment — courtesy-level Welsh minimum; levels 1–5 across four skills | Senedd Commission | https://senedd.wales/commission/work-for-the-senedd-commission/official-languages-and-recruitment/ |
| welsh-language-measure-2011 | Welsh Language (Wales) Measure 2011 — statutory basis for the Welsh Language Standards | legislation.gov.uk | https://www.legislation.gov.uk/mwa/2011/1/contents |
| nics-cf-2014 | **NICS Competency Framework (April 2014)** — ten competencies, three clusters, six cumulative levels. NICS is a **separate civil service**, NOT Home Civil Service; uses Competence Based Interviews, not Success Profiles. Over a decade old but still the live framework as of 2026-07-20. | NI Civil Service Recruitment (HRConnect) | https://irecruit-ext.hrconnect.nigov.net/resources/documents/n/i/c/nics-cf.pdf |
| nics-cf-page | NICS Competency Framework (landing page) | NI Civil Service Recruitment (HRConnect) | https://irecruit-ext.hrconnect.nigov.net/pages/content.aspx?Page=NICS-Competency-Framework |
| nics-selection-process | Selection Process — CIB; sift; Competence Based Interviews | NI Civil Service Recruitment (HRConnect) | https://irecruit-ext.hrconnect.nigov.net/pages/content.aspx?Page=how-do-i-apply%2Fselection-process |
| nics-cbi-guidance | Interview Guidance — Competence Based Interviews; Situation–Task–Action–Result | NI Civil Service Recruitment (HRConnect) | https://irecruit-ext.hrconnect.nigov.net/resources/documents/g/u/i//guidance-on-competence-based-interviews---accessible.pdf |
| nics-commissioners | What We Do — Merit Principle; Recruitment Code | Civil Service Commissioners for Northern Ireland | https://www.nicscommissioners.org/what-we-do |
| psni-cvf-2024 | **PSNI Competency and Values Framework: An Overview** — the CoP CVF **adapted under Licence SF00312** (three values, six competencies; updated June 2025). *Confirms PSNI DOES use the CoP CVF — corrects an earlier assumption that it did not.* | Police Service of Northern Ireland (adapting College of Policing) | https://www.joinpsni.co.uk/uploads/1749992122-PSNI-CVF-2024-updated-June-2025---PDF.pdf |
| psni-assessment-centre-prep | How to prepare for the assessment centre — CVF Level 1; professional + lay assessors mark independently then agree; Deloitte design | Join PSNI | https://www.joinpsni.co.uk/police-officer/information-on-how-to-prepare-for-the-assessment-centre-and-assessment-centre-scheduling |
| hscni-values | Health & Social Care Values — Working Together, Excellence, Openness & Honesty, Compassion | HSC Recruitment (jobs.hscni.net) | https://jobs.hscni.net/Information/23/health-social-care-values |
| civilservicecareers-gos-tips | GOS: tips and guidance for applying — names **both STAR and CAR**, but CAR defined as "Context, Action, Result" and **no proportioning content**; departmental, does NOT supersede the 2016 brief guide | Civil Service Careers | https://www.civil-service-careers.gov.uk/gos-tips-and-guidance-for-applying/ |
| ni-act-1998-s75 | Northern Ireland Act 1998, s.75 — statutory equality duty (nine grounds) + good-relations duty. **Distinct from the Equality Act 2010 PSED.** | legislation.gov.uk | https://www.legislation.gov.uk/ukpga/1998/47/section/75 |

### Practitioner & Careers

| Key | Source | Publisher | URL |
|-----|--------|-----------|-----|
| oxford-example-questions | Example interview questions (PDF, May 2016) | University of Oxford Careers Service | https://www.careers.ox.ac.uk/files/example-interview-questionspdf |
| bath-behavioural-questions | Behavioural questions for interviewing — published bank of 19 behavioural interview questions | University of Bath (Human Resources) | https://www.bath.ac.uk/corporate-information/behavioural-questions-for-interviewing/ |
| cloverhr-cs-behaviour-questions | Competency interview questions for Civil Service behaviours — one example question per behaviour (undated; SME consultancy — never sole support for a claim) | Clover HR | https://www.cloverhr.co.uk/blog/competency-interview-questions-for-civil-service-behaviours/ |
| oxford-interview-technique | Interview Technique | University of Oxford Careers Service | https://www.careers.ox.ac.uk/interview-technique |
| oxford-types-interview | Types of Interview | University of Oxford Careers Service | https://www.careers.ox.ac.uk/types-of-interview |
| cambridge-interviews | Interviews | University of Cambridge Careers Service | https://www.careers.cam.ac.uk/interviews |
| edinburgh-before-interview | Before your interview | University of Edinburgh Careers Service | https://careers.ed.ac.uk/interviews-and-assessment-centres/before-your-interview |
| edinburgh-carl | The CARL framework of reflection (Reflection Toolkit, 15 Oct 2024) | University of Edinburgh | https://reflection.ed.ac.uk/reflectors-toolkit/reflecting-on-experience/carl |
| edinburgh-academic-interview | Prepare for an academic interview — panel size ("usually between two and six") and composition | University of Edinburgh Careers Service | https://careers.ed.ac.uk/phd-and-mres-students/make-it-happen/prepare-for-an-academic-interview |
| nottingham-chair-panel-training | Interview Skills for Chair & Panel Members (Recruitment Services training deck) — **rich interviewer-side source**: chair duty list, panel pre-meet, lead-question + probe sets, note-taking standard, chair represents the panel at a Tribunal. Last modified 2019 — illustrative university practice, not statutory guidance. | University of Nottingham | https://training.nottingham.ac.uk/Public/Presentation-Interview%20Skills%20Chair%20and%20Panel%20Members.pdf |
| reading-star | STAR technique | University of Reading | https://www.reading.ac.uk/essentials/Careers/Applications-and-interviews/STAR-technique |
| arden-starr | STAR(R) Interview Technique | Arden University Careers Portal | https://careers.arden.ac.uk/pages/star-r |
| prospects-competency-interviews | Competency-based interviews: How to prepare and example answers (Rachel Swain, June 2025) | Prospects | https://www.prospects.ac.uk/careers-advice/interview-tips/competency-based-interviews/ |
| prospects-telephone | Telephone interviews (Rachel Swain, June 2025) | Prospects | https://www.prospects.ac.uk/careers-advice/interview-tips/telephone-interviews/ |
| prospects-video | Video interview tips (Rachel Swain, June 2025) | Prospects | https://www.prospects.ac.uk/careers-advice/interview-tips/video-interview-tips/ |
| luminate-ise-2024 | What's the state of graduate recruitment in 2024? (Georgia Greer, ISE, Oct 2024) | Prospects Luminate | https://luminate.prospects.ac.uk/whats-the-state-of-graduate-recruitment-in-2024 |
| luminate-ise-2025 | Early careers recruitment in 2025: integrity, inclusion, entry standards (Stephen Isherwood, Oct 2025) | Prospects Luminate | https://luminate.prospects.ac.uk/early-careers-recruitment-in-2025-integrity-inclusion-entry-standards |
| luminate-grad-recruitment-2022 | How graduate recruitment has changed in 2022 (reports ISE 2022 survey) | Prospects Luminate | https://luminate.prospects.ac.uk/how-graduate-recruitment-has-changed-in-2022 |
| targetjobs-competency-questions | Competency-based interview questions and answers (Rachael Milsom, upd. 2026-03-31) | targetjobs | https://targetjobs.co.uk/careers-advice/interviews-and-assessment-centres/how-answer-competency-based-interview-questions |
| targetjobs-unilever-interview | Applying to the future leaders programme: the Unilever digital interview | targetjobs | https://targetjobs.co.uk/careers-advice/interviews-and-assessment-centres/applying-future-leaders-programme-unilever-digital-interview |
| targetjobs-fidelity-starr | What is the STARR answer technique, and how do I use it? (S. Vaughan, Fidelity International) | targetjobs | https://targetjobs.co.uk/organisations/fidelity-international/what-starr-answer-technique-and-how-do-i-use-it |
| targetjobs-teamwork-questions | Tips to answer teamwork interview questions (Alan Palazon, 1 Aug 2024) — 11 published teamwork questions | targetjobs | https://targetjobs.co.uk/careers-advice/interviews-and-assessment-centres/how-tackle-teamwork-interview-questions-and-improve-your-teamworking-skills |
| targetjobs-ethical-dilemma | "Give us an example of a time when you faced an ethical dilemma" — tricky graduate interview question (upd. 2026-03-31) | targetjobs | https://targetjobs.co.uk/careers-advice/interviews-and-assessment-centres/give-us-example-time-when-you-faced-ethical-dilemma-tricky-graduate-interview-question |
| targetjobs-strengths-interviews | Strength-based interviews for jobs and grad schemes (Abigail Lewis, upd. 21 Aug 2025) — 15 published strengths questions; named adopters | targetjobs | https://targetjobs.co.uk/careers-advice/interviews-and-assessment-centres/strength-based-interviews-jobs-and-grad-schemes |
| targetjobs-pwc-process | The PwC graduate application process explained (Alan Palazon, 29 Apr 2025) — **the citable route for PwC claims**, since pwc.co.uk 403s | targetjobs | https://targetjobs.co.uk/careers-advice/cvs-applications-and-tests/pwc-graduate-application-process-explained |
| targetjobs-pwc-questions | Hints on answering PwC interview questions (Jacky Barrett, upd. 31 Mar 2026) — reported, not official, questions | targetjobs | https://targetjobs.co.uk/careers-advice/interviews-and-assessment-centres/tips-how-answer-pwc-interview-questions |
| targetjobs-deloitte-questions | How do I prepare for Deloitte interview questions? (23 Apr 2025) | targetjobs | https://targetjobs.co.uk/careers-advice/interviews-and-assessment-centres/how-prepare-deloittes-interview-questions |
| targetjobs-aldi-process | Application and interview advice for Aldi's area management graduate programme (27 Feb 2023) | targetjobs | https://targetjobs.co.uk/careers-advice/interviews-and-assessment-centres/application-and-interview-advice-aldis-area-management-graduate-programme |
| targetjobs-nhs-gmts | How to be successful in the recruitment process for the NHS graduate management training scheme (31 Oct 2023) | targetjobs | https://targetjobs.co.uk/careers-advice/cvs-applications-and-tests/how-be-successful-recruitment-process-nhs-graduate-management-training-scheme |
| kent-commercial-awareness | Commercial awareness — published commercial-awareness interview question set | University of Kent Careers and Employability Service | https://student.kent.ac.uk/careers/employability/commercial-awareness-skills |
| kent-assessment-centre-tasks | Assessment centres: Tasks — the clearest located taxonomy of AC exercises (assigned vs unassigned group roles, in-tray competencies, planned vs on-the-spot presentations, case studies, role plays) | University of Kent Careers and Employability Service | https://student.kent.ac.uk/careers/making-applications/assessment-centres/tasks |
| lse-etray-intray | E-tray and in-tray exercises — same exercise in different media; 90-minute worked example with 15-minute read cap; published prioritisation cues; "there is no one right answer" | LSE Careers | https://info.lse.ac.uk/current-students/careers/information-and-resources/interview-assessment-centre-psychometric/e-tray-and-in-tray-exercises |
| york-assessment-centres | Assessment centres — group observation criteria ("cooperatively without dominating"); in-tray justification requirement; warning that candidates may be assessed throughout their time with the employer | University of York Careers and Placements | https://www.york.ac.uk/students/work-volunteering-careers/apply-interview/assessment-centres/ |
| ncs-video-interviews | Video interviews tips — live vs pre-recorded; camera at eye level; check re-record availability | National Careers Service | https://nationalcareers.service.gov.uk/careers-advice/how-to-do-well-in-video-interviews |
| oxford-telephone-video | Telephone and Video Interviews — "no opportunity for the interviewer to ask for clarification"; per-question response time | University of Oxford Careers Service | https://www.careers.ox.ac.uk/telephone-video-interviews |
| targetjobs-video-interview-tips | Expert video interview tips to impress recruiters (20 Aug 2025) — 1–3 min per question with on-screen timer; ~one-week window; retakes vary; names Sonru, SparkHire, HireVue | targetjobs | https://targetjobs.co.uk/careers-advice/interviews-and-assessment-centres/expert-video-interview-tips-impress-recruiters |
| manchester-strengths-recruitment | Strengths recruitment and interviews — named adopters (Civil Service, Mott MacDonald, EY); published calibration question | University of Manchester Careers Service | https://www.careers.manchester.ac.uk/applicationsinterviews/interviews/types/strengthsrecruit/ |
| manchester-professionalism | Professionalism — evidencing skills through studies, part-time work, volunteering, societies, placements, course-rep roles | University of Manchester Careers Service | https://www.careers.manchester.ac.uk/options/skills/professionalism/ |
| targetjobs-leadership-management | Leadership and management: prove you're more than an entry-level hire (Abigail Lewis, upd. 21 Jun 2023) | targetjobs | https://targetjobs.co.uk/careers-advice/skills-for-getting-a-job/leadership-and-management-prove-youre-more-entry-level-hire |
| myworldofwork-competency-guide | A complete guide to competency-based interviews | My World of Work (Skills Development Scotland) | https://www.myworldofwork.co.uk/cvs-applications-and-interviews/a-complete-guide-to-competency-based-interviews |
| pwc-early-careers | Assessment and selection process — Early Careers | PwC UK | https://www.pwc.co.uk/careers/early-careers/applying/assessment-selection-process.html |
| ey-interview-tips | Interview tips | EY UK | https://www.ey.com/en_uk/careers/how-to-join-us/interview-tips |
| unilever-uflp-2026 | UK & Ireland Unilever Future Leaders Programme 2026 — four published selection stages; Discovery Centre | Unilever | https://careers.unilever.com/en/uk-and-ireland-unilever-future-leaders-programme-2026 |
| aldi-graduate-area-manager | Area Manager Graduate Scheme — five published stages incl. one-to-one competency-based interview | Aldi Recruitment UK | https://www.aldirecruitment.co.uk/early-careers/graduate-area-manager-programme |
| deloitte-early-careers-assessment | Early Careers Assessment Support — four published assessed stages; immersive online assessment; job simulation | Deloitte UK | https://www.deloitte.com/uk/en/careers/early-careers/early-careers-assessment.html |
| kpmg-application-process | Our application process — four published stages; AI-avatar video interview with human scoring; Launch Pad | KPMG UK | https://www.kpmgcareers.co.uk/graduate/applying-to-kpmg/application-process/ |
| barclays-grad-application | Internship and Graduate Application Process — three published stages; assessment-centre contents | Barclays | https://search.jobs.barclays/internship-graduate-application |
| amazon-leadership-principles | Leadership Principles — sixteen named principles (closest thing to a published private-sector competency list; **no** level descriptors) | Amazon Jobs | https://www.amazon.jobs/content/en/our-workplace/leadership-principles |
| healthcareers-nhs-gmts | NHS Graduate Management Training Scheme — selection stages; skills assessed. *Now 403s automated fetchers (sweep 2026-07-20) — eyeball in browser.* | NHS Health Careers | https://www.healthcareers.nhs.uk/career-planning/study-and-training/graduate-training-opportunities/nhs-graduate-management-training-scheme |
| cipd-strengths-based-interviews | How to conduct a strengths-based interview — definition, rationale for graduates, example questions | CIPD | https://www.cipd.org/en/about/news-archive/strengths-based-interviews/ |
| ise-top-10-stats-2025 | ISE top 10 stats of 2025 (140 applications per vacancy; AI; development gaps) — public insight page | Institute of Student Employers | https://ise.org.uk/knowledge/insights/513/ise_top_10_stats_of_2025_you_need_to_know/ |
| euronews-epso-2026 | EPSO exam: Record-breaking participation with only 3% success rate (17 Feb 2026) | Euronews | https://www.euronews.com/my-europe/2026/02/17/epso-exam-record-breaking-participation-with-only-3-success-rate |
| prepari-93-questions | 93 EU Job Interview Questions to Prepare For | Prepari.eu | https://prepari.eu/eu-job-interview-questions/ |
| euphorum-structured-interview | The structured interview (EPSO assessment-centre guide, pre-2023 model) | Euphorum | http://www.euphorum.org/en/training/ac/interview |
| interviewguys-soar | The SOAR Method (M. Simpson, 20 Apr 2025) | The Interview Guys | https://blog.theinterviewguys.com/the-soar-method/ |
| indeed-customer-service-questions | Top Customer Service Interview Questions (With Sample Answers) (Indeed Editorial Team, upd. 16 Jun 2026) — bot-block allowlisted; eyeball in browser | Indeed UK | https://uk.indeed.com/career-advice/interviewing/customer-service-interview-questions |

### Academic

| Key | Source | Publisher | URL |
|-----|--------|-----------|-----|
| sackett-2022-jap | Revisiting meta-analytic estimates of validity in personnel selection (J. Applied Psychology 107(11)) | Sackett, Zhang, Berry & Lievens / APA (PubMed record) | https://pubmed.ncbi.nlm.nih.gov/34968080/ |
| levashina-2014-peps | The structured employment interview: narrative and quantitative review (Personnel Psychology 67, 241–293; DOI 10.1111/peps.12052) — **15-component structure taxonomy**; group-difference meta-analysis (high- vs low-structure d = .23 vs .32; post-1996 near-zero); situational vs past-behaviour; anchored-scale validity/reliability. Full text read via open-access author copy. | Levashina, Hartwell, Morgeson & Campion / Wiley | http://www.morgeson.com/downloads/levashina_hartwell_morgeson_campion_2014.pdf |
| spence-2024-pspb | Is your accent right for the job? A meta-analysis on accent bias in hiring (PSPB 50(3), 371–386; DOI 10.1177/01461672221130595) — 139 effect sizes, N=4,576; standard-accented candidates rated more hireable (d=0.47); prejudice over processing-fluency. ⚠️ **Abstract/PubMed record only — full text not read.** | Spence, Hornsey, Stephenson & Imuta / SAGE (PubMed record) | https://pubmed.ncbi.nlm.nih.gov/36326202/ |
| sackett-2023-iop | Revisiting the design of selection systems in light of new findings regarding the validity of widely used predictors (IOP 16(3), open access) | Sackett, Zhang, Berry & Lievens / Cambridge University Press | https://www.cambridge.org/core/services/aop-cambridge-core/content/view/A20984B138319E3D432E643978BF026D/S175494262300024Xa.pdf/revisiting_the_design_of_selection_systems_in_light_of_new_findings_regarding_the_validity_of_widely_used_predictors.pdf |

### Further Reading

| Key | Source | Publisher | URL |
|-----|--------|-----------|-----|
| orseu-eu-careers-guide | Complete Guide to Passing EPSO EU Competitions for EU Careers | ORSEU Concours | https://www.orseu-concours.com/gb/content/21-guide-for-eu-careers |
