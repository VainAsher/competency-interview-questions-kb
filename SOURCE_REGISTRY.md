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

Observed during cluster 1 (not allowlisted; workers used alternatives):
college.police.uk HTML pages 403 (the assets.college.police.uk PDFs check
fine); prospects.ac.uk and ise.org.uk intermittently 403 fetchers but pass the
checker; several legacy epso.europa.eu URLs 404 after EPSO's migration to
eu-careers.europa.eu.

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
| govuk-sp-strengths | Success Profiles: Strengths | GOV.UK (Cabinet Office) | https://www.gov.uk/government/publications/success-profiles/success-profiles-strengths |
| csc-assessments | Assessments and Interviews | Civil Service Careers | https://www.civil-service-careers.gov.uk/assessments-and-interviews/ |
| csc-behaviours | Behaviours (candidate guidance) | Civil Service Careers | https://www.civil-service-careers.gov.uk/behaviours/ |
| cs-blog-four-steps | Four steps to success: tips for candidates (18 Nov 2024) | Civil Service blog | https://civilservice.blog.gov.uk/2024/11/18/four-steps-to-success-tips-for-candidates-applying-to-the-civil-service/ |
| copfs-assessment | How your application is assessed — Success Profiles (1–7 scale, benchmarks) | Crown Office and Procurator Fiscal Service | https://www.copfs.gov.uk/about-copfs/careers/how-your-application-is-assessed-success-profiles/ |
| ncs-interview-tips | Interview tips | National Careers Service | https://nationalcareers.service.gov.uk/careers-advice/interview-advice |
| ncs-star-method | The STAR method | National Careers Service | https://nationalcareers.service.gov.uk/careers-advice/interview-advice/the-star-method |
| ncs-common-questions | How to answer common interview questions | National Careers Service | https://nationalcareers.service.gov.uk/careers-advice/top-10-interview-questions |
| govuk-nhs-constitution | The NHS Constitution for England | GOV.UK (DHSC) | https://www.gov.uk/government/publications/the-nhs-constitution-for-england/the-nhs-constitution-for-england |
| hee-vbr-page | Values Based Recruitment (programme page) | NHS England (HEE legacy site) | https://www.hee.nhs.uk/our-work/values-based-recruitment |
| hee-vbr-framework-2016 | Values Based Recruitment Framework (March 2016) | Health Education England | https://www.hee.nhs.uk/sites/default/files/documents/VBR_Framework%20March%202016.pdf |
| nhse-vbr-article | Values-based recruitment (article) | NHS Employers | https://www.nhsemployers.org/articles/values-based-recruitment |
| cop-cvf-guidance-2024 | Competency and values framework guidance (2024) | College of Policing | https://assets.college.police.uk/s3fs-public/2024-05/Competency-and-values-framework-guidance.pdf |
| cop-cvf-2016 | Competency and Values Framework for policing: Overview (2016) | College of Policing | https://assets.college.police.uk/s3fs-public/2020-11/competency-and-values-framework-for-policing_4.11.16.pdf |
| govuk-recruitment-adjustments | Recruitment and disabled people: Reasonable adjustments | GOV.UK | https://www.gov.uk/recruitment-disabled-people/reasonable-adjustments |
| equality-act-2010 | Equality Act 2010 (contents; Part 5: Work) | legislation.gov.uk | https://www.legislation.gov.uk/ukpga/2010/15/contents |
| equality-act-2010-s4 | Equality Act 2010, s.4 (The protected characteristics) | legislation.gov.uk | https://www.legislation.gov.uk/ukpga/2010/15/section/4 |
| equality-act-s20 | Equality Act 2010, s.20 (Duty to make adjustments) | legislation.gov.uk | https://www.legislation.gov.uk/ukpga/2010/15/section/20 |
| eqa2010-s60 | Equality Act 2010, s.60 (Enquiries about disability and health) | legislation.gov.uk | https://www.legislation.gov.uk/ukpga/2010/15/section/60 |
| ico-recruitment-selection | Employment practices and data protection: recruitment and selection (draft) | Information Commissioner's Office | https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/employment/recruitment-and-selection/ |

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
| oxford-interview-technique | Interview Technique | University of Oxford Careers Service | https://www.careers.ox.ac.uk/interview-technique |
| oxford-types-interview | Types of Interview | University of Oxford Careers Service | https://www.careers.ox.ac.uk/types-of-interview |
| cambridge-interviews | Interviews | University of Cambridge Careers Service | https://www.careers.cam.ac.uk/interviews |
| edinburgh-before-interview | Before your interview | University of Edinburgh Careers Service | https://careers.ed.ac.uk/interviews-and-assessment-centres/before-your-interview |
| edinburgh-carl | The CARL framework of reflection (Reflection Toolkit, 15 Oct 2024) | University of Edinburgh | https://reflection.ed.ac.uk/reflectors-toolkit/reflecting-on-experience/carl |
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
| myworldofwork-competency-guide | A complete guide to competency-based interviews | My World of Work (Skills Development Scotland) | https://www.myworldofwork.co.uk/cvs-applications-and-interviews/a-complete-guide-to-competency-based-interviews |
| pwc-early-careers | Assessment and selection process — Early Careers | PwC UK | https://www.pwc.co.uk/careers/early-careers/apply/video-interview.html |
| ey-interview-tips | Interview tips | EY UK | https://www.ey.com/en_uk/careers/how-to-join-us/interview-tips |
| unilever-uflp-2026 | UK & Ireland Unilever Future Leaders Programme 2026 | Unilever | https://careers.unilever.com/en/uk-and-ireland-unilever-future-leaders-programme-2026 |
| euronews-epso-2026 | EPSO exam: Record-breaking participation with only 3% success rate (17 Feb 2026) | Euronews | https://www.euronews.com/my-europe/2026/02/17/epso-exam-record-breaking-participation-with-only-3-success-rate |
| prepari-93-questions | 93 EU Job Interview Questions to Prepare For | Prepari.eu | https://prepari.eu/eu-job-interview-questions/ |
| euphorum-structured-interview | The structured interview (EPSO assessment-centre guide, pre-2023 model) | Euphorum | http://www.euphorum.org/en/training/ac/interview |
| interviewguys-soar | The SOAR Method (M. Simpson, 20 Apr 2025) | The Interview Guys | https://blog.theinterviewguys.com/the-soar-method/ |

### Academic

| Key | Source | Publisher | URL |
|-----|--------|-----------|-----|
| sackett-2022-jap | Revisiting meta-analytic estimates of validity in personnel selection (J. Applied Psychology 107(11)) | Sackett, Zhang, Berry & Lievens / APA (PubMed record) | https://pubmed.ncbi.nlm.nih.gov/34968080/ |
| sackett-2023-iop | Revisiting the design of selection systems in light of new findings regarding the validity of widely used predictors (IOP 16(3), open access) | Sackett, Zhang, Berry & Lievens / Cambridge University Press | https://www.cambridge.org/core/services/aop-cambridge-core/content/view/A20984B138319E3D432E643978BF026D/S175494262300024Xa.pdf/revisiting_the_design_of_selection_systems_in_light_of_new_findings_regarding_the_validity_of_widely_used_predictors.pdf |

### Further Reading

| Key | Source | Publisher | URL |
|-----|--------|-----------|-----|
| orseu-eu-careers-guide | Complete Guide to Passing EPSO EU Competitions for EU Careers | ORSEU Concours | https://www.orseu-concours.com/gb/content/21-guide-for-eu-careers |
