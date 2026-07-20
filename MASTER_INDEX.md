# Master Index — UK & EU Competency-Based Interview Knowledge Base

The single catalogue of record. Only the orchestrator edits this file.

Tiers: **1** = category foundations · **2** = competency deep-dives & question
banks · **3** = framework & format guides · **4** = techniques & cross-cutting
best practice.

## Documents

| ID | Title | Topic | Tier | Market | Version | Status | Confidence | Path |
|----|-------|-------|------|--------|---------|--------|------------|------|
| competencies-foundation | Competency-Based Interviewing: Competency Families & Question Mapping | Competency families & question mapping | 1 | UK, EU | 1.0.0 | frozen | Medium | `docs/01-competencies/competencies-foundation.md` |
| techniques-foundation | Answer Frameworks & Techniques: STAR and Beyond | Answer frameworks | 1 | UK, EU | 1.0.0 | frozen | Medium | `docs/02-techniques/techniques-foundation.md` |
| uk-frameworks-foundation | UK Competency Frameworks: The Landscape | UK competency frameworks landscape | 1 | UK | 1.0.0 | frozen | Medium | `docs/03-uk-frameworks/uk-frameworks-foundation.md` |
| eu-frameworks-foundation | EU Competency Frameworks: EPSO & the EU Institutions | EU competency frameworks landscape | 1 | EU | 1.0.0 | frozen | Medium | `docs/04-eu-frameworks/eu-frameworks-foundation.md` |
| formats-foundation | Interview Formats & Assessment Methods | Interview formats & assessment methods | 1 | UK, EU | 1.0.0 | frozen | Medium | `docs/05-formats/formats-foundation.md` |
| best-practice-foundation | Interview Best Practice: Preparation, Pitfalls & Scoring Insight | Preparation strategy & pitfalls | 1 | UK, EU | 1.0.0 | frozen | Medium | `docs/06-best-practice/best-practice-foundation.md` |
| teamwork-collaboration | Teamwork & Collaboration: Question Bank & Answer Guidance | Teamwork & collaboration | 2 | UK, EU | 1.0.0 | frozen | Medium | `docs/01-competencies/teamwork-collaboration.md` |
| communication-influencing | Communication & Influencing: Question Bank & Answer Guidance | Communication & influencing | 2 | UK, EU | 1.0.0 | frozen | Medium | `docs/01-competencies/communication-influencing.md` |
| leadership-management | Leadership & Managing Others: Question Bank & Answer Guidance | Leadership & managing others | 2 | UK, EU | 1.0.0 | frozen | Medium | `docs/01-competencies/leadership-management.md` |
| problem-solving-decision-making | Problem-Solving, Analysis & Decision-Making: Question Bank & Answer Guidance | Problem-solving & decision-making | 2 | UK, EU | 1.0.0 | frozen | Medium | `docs/01-competencies/problem-solving-decision-making.md` |
| delivering-results-planning | Delivering Results, Planning & Organising: Question Bank & Answer Guidance | Delivering results & planning | 2 | UK, EU | 1.0.0 | frozen | Medium | `docs/01-competencies/delivering-results-planning.md` |
| resilience-adaptability | Resilience, Adaptability & Working Under Pressure: Question Bank & Answer Guidance | Resilience & adaptability | 2 | UK, EU | 1.0.0 | frozen | Medium | `docs/01-competencies/resilience-adaptability.md` |
| integrity-values-ethics | Integrity, Values & Ethical Behaviour: Question Bank & Answer Guidance | Integrity & values | 2 | UK, EU | 1.0.0 | frozen | Medium | `docs/01-competencies/integrity-values-ethics.md` |
| customer-stakeholder-service | Customer Service & Stakeholder Management: Question Bank & Answer Guidance | Customer & stakeholder focus | 2 | UK, EU | 1.0.1 | frozen | Medium | `docs/01-competencies/customer-stakeholder-service.md` |
| uk-civil-service-success-profiles | Civil Service Success Profiles: The Complete Guide | Success Profiles end-to-end | 3 | UK | 1.0.0 | frozen | High | `docs/03-uk-frameworks/uk-civil-service-success-profiles.md` |
| uk-civil-service-behaviour-questions | Civil Service Behaviours: Question Bank by Behaviour and Grade | Civil Service behaviour questions | 3 | UK | 1.0.0 | frozen | Medium | `docs/03-uk-frameworks/uk-civil-service-behaviour-questions.md` |
| nhs-values-based-interviews | NHS Values-Based Interviews: Framework, Questions & Band Expectations | NHS values-based recruitment | 3 | UK | 1.0.0 | frozen | Medium | `docs/03-uk-frameworks/nhs-values-based-interviews.md` |
| police-competency-values-framework | Police Competency and Values Framework (CVF): Guide & Question Bank | College of Policing CVF | 3 | UK | 1.0.0 | frozen | High | `docs/03-uk-frameworks/police-competency-values-framework.md` |
| uk-graduate-schemes | UK Graduate Schemes: Competency Interviews in Private-Sector Recruitment | Graduate-scheme competency interviews | 3 | UK | 1.0.0 | frozen | Medium | `docs/03-uk-frameworks/uk-graduate-schemes.md` |
| epso-competency-framework | The EPSO Competency Framework: Competencies, Assessment & Question Bank | EPSO general competencies | 3 | EU | 1.0.0 | frozen | Medium | `docs/04-eu-frameworks/epso-competency-framework.md` |
| eu-institutions-assessment-centres | EU Institutions Assessment Centres: Exercises, Structure & Preparation | EU assessment centres | 3 | EU | 1.0.0 | frozen | Medium | `docs/04-eu-frameworks/eu-institutions-assessment-centres.md` |
| panel-interviews | Panel Interviews: Structure, Dynamics & Scoring | Panel interviews | 3 | UK, EU | 1.0.0 | frozen | High | `docs/05-formats/panel-interviews.md` |
| video-asynchronous-interviews | Video & Asynchronous Interviews: Formats, Platforms & Technique | Video and asynchronous interviews | 3 | UK, EU | 1.0.0 | frozen | Medium | `docs/05-formats/video-asynchronous-interviews.md` |
| assessment-centre-exercises | Assessment Centre Exercises: Group Tasks, In-Trays & Presentations | Assessment centre exercises | 3 | UK, EU | 1.0.0 | frozen | Medium | `docs/05-formats/assessment-centre-exercises.md` |

## Knowledge graph

Typed cross-reference edges between documents. Each bullet has the shape below
(append `(planned)` when the target does not exist yet):

```text
- `source-id` *relation* `target-id`
```

- `competencies-foundation` *related* `techniques-foundation` `uk-frameworks-foundation` `eu-frameworks-foundation` `formats-foundation` `best-practice-foundation`
- `uk-frameworks-foundation` *counterpart of* `eu-frameworks-foundation`
- `techniques-foundation` *complements* `formats-foundation` `best-practice-foundation`
- `formats-foundation` *complements* `best-practice-foundation`
- `competencies-foundation` *parent of* `teamwork-collaboration` `communication-influencing` `leadership-management` `problem-solving-decision-making` `delivering-results-planning` `resilience-adaptability` `integrity-values-ethics` `customer-stakeholder-service`
- `teamwork-collaboration` *deepens* `competencies-foundation`
- `teamwork-collaboration` *relates to* `communication-influencing` `leadership-management` `customer-stakeholder-service`
- `communication-influencing` *deepens* `competencies-foundation`
- `communication-influencing` *relates to* `leadership-management` `customer-stakeholder-service` `techniques-foundation`
- `leadership-management` *deepens* `competencies-foundation`
- `leadership-management` *relates to* `delivering-results-planning` `integrity-values-ethics` `resilience-adaptability`
- `problem-solving-decision-making` *deepens* `competencies-foundation`
- `problem-solving-decision-making` *relates to* `delivering-results-planning` `integrity-values-ethics`
- `delivering-results-planning` *deepens* `competencies-foundation`
- `delivering-results-planning` *relates to* `resilience-adaptability` `customer-stakeholder-service`
- `resilience-adaptability` *deepens* `competencies-foundation`
- `resilience-adaptability` *relates to* `integrity-values-ethics` `techniques-foundation`
- `integrity-values-ethics` *deepens* `competencies-foundation`
- `integrity-values-ethics` *relates to* `uk-frameworks-foundation` `customer-stakeholder-service`
- `customer-stakeholder-service` *deepens* `competencies-foundation`
- `customer-stakeholder-service` *relates to* `techniques-foundation`
- `techniques-foundation` *parent of* `star-technique` `alternative-answer-frameworks` `building-evidence-bank` (planned)
- `uk-frameworks-foundation` *parent of* `uk-civil-service-success-profiles` `uk-civil-service-behaviour-questions` `nhs-values-based-interviews` `police-competency-values-framework` `uk-graduate-schemes`
- `uk-civil-service-success-profiles` *deepens* `uk-frameworks-foundation` `competencies-foundation`
- `uk-civil-service-behaviour-questions` *deepens* `uk-civil-service-success-profiles`
- `uk-civil-service-behaviour-questions` *relates to* `techniques-foundation` `competencies-foundation`
- `nhs-values-based-interviews` *deepens* `uk-frameworks-foundation`
- `nhs-values-based-interviews` *relates to* `integrity-values-ethics` `customer-stakeholder-service` `resilience-adaptability`
- `police-competency-values-framework` *deepens* `uk-frameworks-foundation`
- `police-competency-values-framework` *relates to* `integrity-values-ethics` `resilience-adaptability` `teamwork-collaboration`
- `uk-graduate-schemes` *deepens* `uk-frameworks-foundation`
- `uk-graduate-schemes` *relates to* `formats-foundation` `best-practice-foundation` `resilience-adaptability` `teamwork-collaboration`
- `eu-frameworks-foundation` *parent of* `epso-competency-framework` `eu-institutions-assessment-centres`
- `epso-competency-framework` *deepens* `eu-frameworks-foundation`
- `epso-competency-framework` *relates to* `eu-institutions-assessment-centres` `competencies-foundation`
- `epso-competency-framework` *compares with* `uk-civil-service-success-profiles`
- `eu-institutions-assessment-centres` *deepens* `eu-frameworks-foundation`
- `eu-institutions-assessment-centres` *relates to* `assessment-centre-exercises` `formats-foundation`
- `formats-foundation` *parent of* `panel-interviews` `video-asynchronous-interviews` `assessment-centre-exercises`
- `panel-interviews` *deepens* `formats-foundation`
- `panel-interviews` *applies framework* `uk-civil-service-success-profiles` `police-competency-values-framework` `nhs-values-based-interviews`
- `video-asynchronous-interviews` *deepens* `formats-foundation`
- `video-asynchronous-interviews` *relates to* `uk-graduate-schemes` `best-practice-foundation`
- `assessment-centre-exercises` *deepens* `formats-foundation`
- `assessment-centre-exercises` *relates to* `panel-interviews` `video-asynchronous-interviews` `eu-institutions-assessment-centres` `uk-graduate-schemes`
- `best-practice-foundation` *parent of* `building-evidence-bank` `scoring-and-marking` `common-mistakes-recovery` `interviewer-question-design` `fairness-bias-legal` (planned)

## Backlog (pending clusters — approved 2026-07-19)

### Tier 2 — Competency deep-dives & question banks (cluster 2)

| Planned ID | Scope |
|------------|-------|
| teamwork-collaboration | Teamwork & collaboration — definitions across frameworks, question bank, answer guidance |
| communication-influencing | Communication & influencing |
| leadership-management | Leadership & managing others |
| problem-solving-decision-making | Problem-solving, analysis & decision-making |
| delivering-results-planning | Delivering results, planning & organising |
| resilience-adaptability | Resilience, adaptability & working under pressure |
| integrity-values-ethics | Integrity, values & ethical behaviour |
| customer-stakeholder-service | Customer service & stakeholder management |

### Tier 3 — Framework & format guides (clusters 3–4)

| Planned ID | Scope |
|------------|-------|
| uk-civil-service-success-profiles | Success Profiles end-to-end — the five elements, the nine behaviours, levels, application-to-interview flow |
| uk-civil-service-behaviour-questions | Question bank per Civil Service behaviour, with level-calibrated guidance |
| nhs-values-based-interviews | NHS values-based recruitment — values, question styles, band expectations |
| police-competency-values-framework | College of Policing CVF — competencies, values, levels, question bank |
| epso-competency-framework | EPSO general competencies — definitions, assessment methods, question bank |
| eu-institutions-assessment-centres | EU assessment centres — case study, oral presentation, structured interview, SJT |
| uk-graduate-schemes | UK graduate-scheme competency interviews — common frameworks and questions |
| panel-interviews | Panel interview format — composition, dynamics, scoring |
| video-asynchronous-interviews | Video/asynchronous interviews — platforms, formats, adaptation of technique |
| assessment-centre-exercises | Assessment-centre exercises beyond the interview — group, in-tray, presentations |

### Tier 4 — Techniques & cross-cutting best practice (cluster 5)

| Planned ID | Scope |
|------------|-------|
| star-technique | STAR in depth — structure, timing, evidence selection, worked examples |
| alternative-answer-frameworks | CARL, SOAR and other structures — when they beat STAR |
| building-evidence-bank | Building and maintaining a personal evidence bank |
| follow-up-probing-questions | Follow-up and probing questions — what they test, how to handle them |
| scoring-and-marking | How competency answers are scored — published scales and marking guides |
| common-mistakes-recovery | Common candidate mistakes and in-interview recovery |
| interviewer-question-design | Designing competency questions and scoring rubrics (interviewer/HR audience) |
| fairness-bias-legal | Equality Act 2010, EU equal-treatment law, bias, adjustments, candidate data |
