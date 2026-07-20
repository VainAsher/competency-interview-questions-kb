#!/usr/bin/env python3
"""
Genre-discipline auditor for the reference knowledge base.

The house rule is "never let a judgement wear the costume of a fact". That rule
is easy for a strong model to honour by feel and easy for a weaker model to
drift on. This auditor makes the rule *mechanical* so quality does not depend on
model judgement:

  1. The evidence-layer sections ("Framework Context", "Core Reference",
     "Assessor Perspective", "Legal & Fairness Considerations") actually cite —
     each contains at least one [n] citation marker.
  2. "Question Bank" contains at least one numbered question, and every
     question is provenance-labelled: *(sourced …)* with a [n] citation for
     questions drawn from a published source, or *(composed)* for questions
     written for this knowledge base in the style of a cited framework.
  3. Every *(sourced …)* question carries a [n] marker on the same line.

Read-only. Exit 0 by default (report); pass --strict to fail (exit 1) on any
finding so it can gate CI. Runs over docs/**/*.md or specific files.

Usage:  python scripts/audit_genre.py [--strict] [FILE ...]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
MARKER_RE = re.compile(r"\[(\d+)\]")

EVIDENCE_SECTIONS = [
    "Framework Context", "Core Reference", "Assessor Perspective",
    "Legal & Fairness Considerations",
]

# A question entry is an ordered-list line inside "Question Bank":  "1. ..."
QUESTION_LINE_RE = re.compile(r"^\s*\d+\.\s+\S")
# NB: the label body is matched with [^*]* (not [^)]*) so that a label may
# contain inner parentheses — e.g. *(sourced: GOV.UK (Cabinet Office))* or a
# quoted anchor containing "(e.g. ...)". The earlier [^)]* form stopped at the
# FIRST ")" and silently failed such labels, reporting a correctly-labelled
# question as unlabelled.
SOURCED_RE = re.compile(r"\*\(sourced[^*]*\)\*", re.IGNORECASE)
COMPOSED_RE = re.compile(r"\*\(composed[^*]*\)\*", re.IGNORECASE)


def sections(body: str) -> dict[str, str]:
    """Map each top-level (#) heading to the text until the next # heading."""
    out: dict[str, str] = {}
    parts = re.split(r"^# (.+?)\s*$", body, flags=re.MULTILINE)
    # parts = [pre, h1, text, h1, text, ...]
    for i in range(1, len(parts), 2):
        out[parts[i].strip()] = parts[i + 1] if i + 1 < len(parts) else ""
    return out


def audit_file(path: Path) -> list[str]:
    findings: list[str] = []
    text = path.read_text(encoding="utf-8")
    m = FM_RE.match(text)
    body = text[m.end():] if m else text
    secs = sections(body)

    # 1. evidence sections must cite
    for name in EVIDENCE_SECTIONS:
        if name not in secs:
            findings.append(f"missing evidence section: '{name}'")
        elif not MARKER_RE.search(secs[name]):
            findings.append(f"evidence section '{name}' contains no [n] citation marker")

    # 2/3. question bank — every numbered question provenance-labelled
    qb = secs.get("Question Bank")
    if qb is None:
        findings.append("missing section: 'Question Bank'")
        return findings

    questions = [ln for ln in qb.splitlines() if QUESTION_LINE_RE.match(ln)]
    if not questions:
        findings.append("'Question Bank' has no numbered questions "
                        "(expected ordered-list entries '1. …')")
        return findings

    for ln in questions:
        sourced = SOURCED_RE.search(ln)
        composed = COMPOSED_RE.search(ln)
        if not sourced and not composed:
            findings.append("question missing provenance label "
                            f"*(sourced …)* / *(composed)*: '{ln.strip()[:60]}'")
        elif sourced and not MARKER_RE.search(ln):
            findings.append("*(sourced)* question has no [n] citation on the "
                            f"same line: '{ln.strip()[:60]}'")
    return findings


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--docs", default="docs")
    ap.add_argument("--strict", action="store_true", help="exit 1 on any finding")
    ap.add_argument("paths", nargs="*")
    args = ap.parse_args()

    if args.paths:
        files = [Path(p) for p in args.paths]
    else:
        files = [f for f in sorted(Path(args.docs).rglob("*.md")) if f.name != "index.md"]

    total = 0
    for f in files:
        fnd = audit_file(f)
        if fnd:
            total += len(fnd)
            print(f"FLAG  {f.as_posix()}")
            for x in fnd:
                print(f"        - {x}")
        else:
            print(f"ok    {f.as_posix()}")

    print("-" * 60)
    if total:
        print(f"GENRE AUDIT: {total} finding(s) across {len(files)} file(s)")
        return 1 if args.strict else 0
    print(f"GENRE AUDIT CLEAN: {len(files)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
