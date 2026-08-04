#!/usr/bin/env python3
from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path


DEFAULT_TARGETS = [Path(".agents/skills")]
BAD_FIXTURE = Path("validators/fixtures/bad/bad_active_skill_contaminated_script.md")
GOLD_FIXTURE = Path("validators/fixtures/gold/gold_active_skill_clean.md")

CONTAMINATION_MARKERS = [
    "FINAL 5-MINUTE MASTER SCRIPT",
    "Task: 5 Minutes youtube script",
    "Task: Write a 5 min youtube script",
    "Stop scrolling, stop hallucinating, and start investing in yourself",
    "Rocking star Yash",
    "The Ekalavya Blueprint",
    "The ₹300 Empire",
    "₹300 TO EMPIRE",
    "He arrived in Bengaluru with exactly ₹300",
    "No godfather, no backup plan",
    "Are you waiting for a call from God",
    "self made shehzada",
    "Pasted Text",
    "<USER_REQUEST>",
    "ZERO-LOSS CHAT TRANSCRIPT",
]


@dataclass
class ContaminationHit:
    path: Path
    line_number: int
    marker: str


@dataclass
class ValidationResult:
    paths_checked: list[Path]
    passed: bool
    hits: list[ContaminationHit]


def iter_markdown_files(target: Path) -> list[Path]:
    if target.is_file():
        return [target]
    if not target.exists():
        return []
    return sorted(path for path in target.rglob("*.md") if path.is_file())


def validate_targets(targets: list[Path]) -> ValidationResult:
    files: list[Path] = []
    for target in targets:
        files.extend(iter_markdown_files(target))

    hits: list[ContaminationHit] = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            for marker in CONTAMINATION_MARKERS:
                if marker.lower() in line.lower():
                    hits.append(ContaminationHit(path=path, line_number=line_number, marker=marker))

    return ValidationResult(paths_checked=files, passed=not hits, hits=hits)


def print_result(result: ValidationResult) -> None:
    print("ACTIVE_SKILL_CONTAMINATION_RESULT")
    print(f"files_checked={len(result.paths_checked)}")
    print(f"result={'PASS' if result.passed else 'FAIL'}")
    print(f"contamination_hits={len(result.hits)}")
    for hit in result.hits:
        print(f"- file={hit.path} line={hit.line_number} marker={hit.marker}")


def self_test() -> int:
    bad = validate_targets([BAD_FIXTURE])
    gold = validate_targets([GOLD_FIXTURE])
    ok = (not bad.passed) and gold.passed

    print("ACTIVE_SKILL_CONTAMINATION_SELF_TEST")
    print(f"bad_fixture_expected=FAIL actual={'PASS' if bad.passed else 'FAIL'}")
    if bad.passed:
        print_result(bad)
    print(f"gold_fixture_expected=PASS actual={'PASS' if gold.passed else 'FAIL'}")
    if not gold.passed:
        print_result(gold)
    print(f"validation_result={'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    if argv == ["--self-test"]:
        return self_test()

    targets = [Path(arg) for arg in argv] if argv else DEFAULT_TARGETS
    result = validate_targets(targets)
    print_result(result)
    return 0 if result.passed else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
