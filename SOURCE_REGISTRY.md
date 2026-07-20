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
| gss-success-profiles-2019 | Guidance for the adoption of Success Profiles across the GSS (Oct 2019) — departmental: behaviour bands by grade, six-criterion cap, single-"3" failure threshold | Government Statistical Service | https://gss.civilservice.gov.uk/wp-content/uploads/2019/10/Success-Profiles-Guidance-GSS.pdf |
| copfs-assessment | How your application is assessed — Success Profiles. **Note:** a *departmental publication of the central scale* (see `co-sp-delegated-grades-2020`), not a departmental invention. Still the only located source publishing the seven descriptor labels. | Crown Office and Procurator Fiscal Service | https://www.copfs.gov.uk/about-copfs/careers/how-your-application-is-assessed-success-profiles/ |
| ncs-interview-tips | Interview tips | National Careers Service | https://nationalcareers.service.gov.uk/careers-advice/interview-advice |
| ncs-star-method | The STAR method | National Careers Service | https://nationalcareers.service.gov.uk/careers-advice/interview-advice/the-star-method |
| ncs-common-questions | How to answer common interview questions | National Careers Service | https://nationalcareers.service.gov.uk/careers-advice/top-10-interview-questions |
| govuk-civil-service-code | The Civil Service Code — the four core values (integrity, honesty, objectivity, impartiality) | GOV.UK (Cabinet Office) | https://www.gov.uk/government/publications/civil-service-code/the-civil-service-code |
| govuk-nolan-principles | The 7 principles of public life (Nolan Principles, first published 31 May 1995) | GOV.UK (Committee on Standards in Public Life) | https://www.gov.uk/government/publications/the-7-principles-of-public-life/the-7-principles-of-public-life--2 |
| csc-recruitment-principles | Recruitment Principles — programme page (selection on merit, fair and open competition) | Civil Service Commission | https://civilservicecommission.independent.gov.uk/recruitment/recruitment-principles/ |
| csc-recruitment-principles-2018 | Recruitment Principles (April 2018) — **the document**, distinct from the page above: "a selection panel of two or more people must be set up"; chair must be a civil servant (or a Commissioner for the most senior competitions); conflict-of-interest declarations; recommended candidate must be first in order of merit; chair's closing record | Civil Service Commission | https://civilservicecommission.independent.gov.uk/document/02a-recruitment-principles-april-2018-final/ |
| equality-act-s149 | Equality Act 2010, s.149 (Public sector equality duty) | legislation.gov.uk | https://www.legislation.gov.uk/ukpga/2010/15/section/149 |
| cop-code-of-ethics-poster-2024 | Code of Ethics: ethical policing principles (overview poster, January 2024) | College of Policing | https://assets.college.police.uk/s3fs-public/2024-01/CoE-overview-landscape-A4-poster.pdf |
| glos-nhs-vbr-toolkit | Values based recruitment toolkit: a toolkit for recruiting managers (2020 refresh) — published trust question bank | Gloucestershire Hospitals NHS Foundation Trust | https://www.gloshospitals.nhs.uk/media/documents/Recruitment_Toolkit_Managers_2020_Refresh_Digital.pdf |
| era-1996-s43b | Employment Rights Act 1996, s.43B (Disclosures qualifying for protection) — note: sexual-harassment category effective 6 Apr 2026 | legislation.gov.uk | https://www.legislation.gov.uk/ukpga/1996/18/section/43B |
| govuk-nhs-constitution | The NHS Constitution for England | GOV.UK (DHSC) | https://www.gov.uk/government/publications/the-nhs-constitution-for-england/the-nhs-constitution-for-england |
| hee-vbr-page | Values Based Recruitment (programme page) | NHS England (HEE legacy site) | https://www.hee.nhs.uk/our-work/values-based-recruitment |
| hee-vbr-framework-2016 | Values Based Recruitment Framework (March 2016) | Health Education England | https://www.hee.nhs.uk/sites/default/files/documents/VBR_Framework%20March%202016.pdf |
| nhse-vbr-article | Values-based recruitment (article) | NHS Employers | https://www.nhsemployers.org/articles/values-based-recruitment |
| wuth-vbr-questions | Values Based Recruitment: example questions for recruiters to ask during job interviews (published NHS trust question bank) | Wirral University Teaching Hospital NHS Foundation Trust | https://www.wuth.nhs.uk/media/32277/values-based-interview-questions.pdf |
| compassion-in-practice-2012 | Compassion in Practice: Nursing, Midwifery and Care Staff — Our Vision and Strategy (4 Dec 2012) — origin and verbatim definitions of the 6Cs (p.13) | NHS Commissioning Board / Department of Health | https://www.england.nhs.uk/wp-content/uploads/2012/12/compassion-in-practice.pdf |
| hee-vbr-structured-interviews | VBR: How to Design and Deliver Structured Interviews for Values Based Recruitment — VBI definition, worked lead-question/probe/indicator templates, FORCE principles, trust case studies | Health Education England (with Work Psychology Group) | https://www.hee.nhs.uk/sites/default/files/documents/3.%20Structured%20interviews.pdf |
| hee-merges-nhse | HEE merges with NHS England — NHS England has assumed all activities previously undertaken by HEE | NHS England (HEE legacy site) | https://www.hee.nhs.uk/hee-merges-with-nhs-england |
| barnsley-vbr-candidates | Values Based Recruitment: Guidance and Information for Candidates (April 2015) — STAR 70/30 weighting; "We will / We / We do not" behavioural framework | Barnsley Hospital NHS Foundation Trust | https://www.barnsleyhospital.nhs.uk/sites/default/files/2023-07/values-based-recruitment-guidance-notes-for-candidates.pdf |
| lypft-vbr-pack | Values Based Recruitment: Candidate Resource Pack (ref. 24/0107, Oct 2024) — interview structure, 40–50 min duration, same values apply at every role level | Leeds and York Partnership NHS Foundation Trust | https://www.leedsandyorkpft.nhs.uk/news/wp-content/uploads/sites/4/2024/10/Values-Based-Recruitment-Resource-Brochure.pdf |
| ouh-vbi-what-to-expect | What to expect from a Value Based Interview (VBI) — two to four questions; no advance preparation needed | Oxford University Hospitals NHS Foundation Trust | https://www.ouh.nhs.uk/working-for-us/application/vbi/what-to-expect/ |
| cop-cvf-guidance-2024 | Competency and values framework guidance (2024) | College of Policing | https://assets.college.police.uk/s3fs-public/2024-05/Competency-and-values-framework-guidance.pdf |
| cop-cvf-2024-framework | Competency and values framework for policing (2024) — full framework incl. competency level descriptors (note: `2025-06/` asset path) | College of Policing | https://assets.college.police.uk/s3fs-public/2025-06/Competency-and-values-framework.pdf |
| cop-cvf-2016 | Competency and Values Framework for policing: Overview (2016) — superseded by the 2024 framework; retained for provenance | College of Policing | https://assets.college.police.uk/s3fs-public/2020-11/competency-and-values-framework-for-policing_4.11.16.pdf |
| cop-using-cvf-assessments-2025 | Using the competency and values framework in assessments (6 Feb 2025) — **authoritative per-assessment CVF-version table**; national sift switched to CVF 2024 on 10 Mar 2025. Cited via Internet Archive because college.police.uk HTML 403s. | College of Policing via Internet Archive | https://web.archive.org/web/20250214053348/https://www.college.police.uk/career-learning/competency-and-values-framework/using-competency-and-values-framework-assessments |
| cop-oap-candidate-guidance-2024 | Online assessment process: Candidate guidance (Sept 2024) — five-question competency interview, written and briefing exercises; CVF assessed per exercise; timings; appeals; resits | College of Policing | https://assets.college.police.uk/s3fs-public/2024-09/Online-assessment-process-candidate-guidance-v3.2.pdf |
| cop-national-sift-guidance-2026 | National sift: Candidate guidance (May 2026) — SJT and behavioural styles questionnaire formats, rating scales, two published example SJT scenarios | College of Policing | https://assets.college.police.uk/s3fs-public/2025-02/National-sift-candidate-guidance.pdf |
| cop-vbr-selection-2018 | Values-based recruitment and selection: guidance for using the CVF in recruitment and selection (2018) — A–D rating scale, ORCE model, assessment barriers, four-fifths rule. **Predates the 2024 CVF** — use only its framework-agnostic process content. | College of Policing | https://assets.college.police.uk/s3fs-public/2020-11/Values-Based_Recruitment_Guidance-1.pdf |
| cop-nppf-step-two-handbook-2025 | NPPF step two legal examinations candidate handbook 2025 — sergeant/inspector exam format and pass marks | College of Policing | https://assets.college.police.uk/s3fs-public/2024-09/NPPF-step-two-legal-examinations-candidate-handbook-2025.pdf |
| joiningthepolice-oap | What does the online assessment process involve? | Join The Police (national police recruitment site) | https://www.joiningthepolice.co.uk/application-process/what-does-the-online-assessment-process-involve |
| devon-cornwall-cvf-interview | Force Interviews: Competency Values Framework — candidate guidance, panel format, common mistakes incl. answering at the wrong CVF level | Devon & Cornwall Police | https://recruitment.devon-cornwall.police.uk/media/a40ndu4b/cvf-interview-guidance.pdf |
| dyfed-powys-cvf-marking-guide | Interview Marking Guide: CVF Specialist, level 2 — what good evidence looks like | Dyfed-Powys Police | https://www.dyfed-powys.police.uk/SysSiteAssets/media/downloads/dyfed-powys/careers/New-CVF/specialist-cvf-document.pdf |
| hampshire-cvf-guidance | Transferee and Re-joiners CVF Guidance — STAR; "CVF bingo" buzzword warning | Hampshire Constabulary | https://www.hampshire.police.uk/SysSiteAssets/media/downloads/hampshire/careers/recruitment-documents/cvf-presentation-powerpoint.pdf |
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
| epso-specific-adjustments | How to request specific adjustments for the selection tests — EPSO Accessibility Team criteria; case-by-case grant | EPSO / EU Careers | https://eu-careers.europa.eu/en/how-request-specific-adjustments-selection-tests |

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
| cipd-selection-methods | Selection methods (factsheet) | CIPD | https://www.cipd.org/en/knowledge/factsheets/selection-factsheet/ |
| cipd-selection-methods-uk | Selection methods (factsheet, UK path) | CIPD | https://www.cipd.org/uk/knowledge/factsheets/selection-factsheet/ |
| ise-recruitment-survey-2025-trends | 5 trends you need to know from ISE's Recruitment Survey 2025 | Institute of Student Employers | https://ise.org.uk/knowledge/insights/498/5_trends_you_need_to_know_from_ises_recruitment_survey_2025/ |
| ise-srs-2025 | ISE Student Recruitment Survey 2025 (landing page; report member-only) | Institute of Student Employers | https://ise.org.uk/knowledge/research/491/ise_student_recruitment_survey_2025/ |

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
| pwc-early-careers | Assessment and selection process — Early Careers | PwC UK | https://www.pwc.co.uk/careers/early-careers/apply/video-interview.html |
| ey-interview-tips | Interview tips | EY UK | https://www.ey.com/en_uk/careers/how-to-join-us/interview-tips |
| unilever-uflp-2026 | UK & Ireland Unilever Future Leaders Programme 2026 — four published selection stages; Discovery Centre | Unilever | https://careers.unilever.com/en/uk-and-ireland-unilever-future-leaders-programme-2026 |
| aldi-graduate-area-manager | Area Manager Graduate Scheme — five published stages incl. one-to-one competency-based interview | Aldi Recruitment UK | https://www.aldirecruitment.co.uk/early-careers/graduate-area-manager-programme |
| deloitte-early-careers-assessment | Early Careers Assessment Support — four published assessed stages; immersive online assessment; job simulation | Deloitte UK | https://www.deloitte.com/uk/en/careers/early-careers/early-careers-assessment.html |
| kpmg-application-process | Our application process — four published stages; AI-avatar video interview with human scoring; Launch Pad | KPMG UK | https://www.kpmgcareers.co.uk/graduate/applying-to-kpmg/application-process/ |
| barclays-grad-application | Internship and Graduate Application Process — three published stages; assessment-centre contents | Barclays | https://search.jobs.barclays/internship-graduate-application |
| amazon-leadership-principles | Leadership Principles — sixteen named principles (closest thing to a published private-sector competency list; **no** level descriptors) | Amazon Jobs | https://www.amazon.jobs/content/en/our-workplace/leadership-principles |
| healthcareers-nhs-gmts | NHS Graduate Management Training Scheme — selection stages; skills assessed | NHS Health Careers | https://www.healthcareers.nhs.uk/career-planning/study-and-training/graduate-training-opportunities/nhs-graduate-management-training-scheme |
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
| sackett-2023-iop | Revisiting the design of selection systems in light of new findings regarding the validity of widely used predictors (IOP 16(3), open access) | Sackett, Zhang, Berry & Lievens / Cambridge University Press | https://www.cambridge.org/core/services/aop-cambridge-core/content/view/A20984B138319E3D432E643978BF026D/S175494262300024Xa.pdf/revisiting_the_design_of_selection_systems_in_light_of_new_findings_regarding_the_validity_of_widely_used_predictors.pdf |

### Further Reading

| Key | Source | Publisher | URL |
|-----|--------|-----------|-----|
| orseu-eu-careers-guide | Complete Guide to Passing EPSO EU Competitions for EU Careers | ORSEU Concours | https://www.orseu-concours.com/gb/content/21-guide-for-eu-careers |
