# Source Registry

The ranked source-authority list for this knowledge base. Workers reach for
sources in this priority order and classify every reference. Only the
orchestrator edits this file; workers return new sources in their JSON reply.

## Source-priority order (highest first)

1. **UK official / statutory** — GOV.UK (Success Profiles and Civil Service
   Behaviours), Civil Service Jobs guidance, legislation.gov.uk (Equality Act
   2010), NHS England / NHS Employers, College of Policing (Competency and
   Values Framework), ICO (candidate data).
2. **EU official** — EPSO (epso.europa.eu / eu-careers), EUR-Lex (directives
   and regulations), official careers pages of EU institutions.
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

Prefer link-checkable alternatives where possible: gov.uk, epso.europa.eu,
legislation.gov.uk, acas.org.uk, Internet Archive snapshots.

## Registered sources

| Key | Source | Class | Publisher | URL |
|-----|--------|-------|-----------|-----|
