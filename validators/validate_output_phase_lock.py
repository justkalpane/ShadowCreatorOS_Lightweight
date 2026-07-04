#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from lib.claim_normalizer import is_truthy, parse_claims


BAD_FIXTURE = Path("validators/fixtures/bad/bad_output_phase_not_started_after_completion.json")
GOLD_FIXTURE = Path("validators/fixtures/gold/gold_route_state_resume_capsule.json")
BAD_TEXT_FIXTURE = Path("validators/fixtures/bad/bad_text_output_phase_not_started_after_completion.md")
GOLD_TEXT_FIXTURE = Path("validators/fixtures/gold/gold_text_output_phase_started_after_completion.md")


@dataclass
class ValidationResult:
    path: Path
    passed: bool
    errors: list[str]
    warnings: list[str]
    dependencies_complete: bool
    output_phase_started: bool
    required_files_missing_count: int | None


def load_data(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return json.loads(text)
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        parsed = None
    if isinstance(parsed, dict):
        return parsed
    return {key: values[-1] for key, values in parse_claims(text).items() if values}


def is_true(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return is_truthy(value)


def is_false(value: Any) -> bool:
    if isinstance(value, bool):
        return not value
    return str(value or "").strip().lower() in {"false", "no", "0", "fail"}


def maybe_int(value: Any) -> int | None:
    if value is None or value == "":
        return None
    if isinstance(value, int):
        return value
    try:
        return int(str(value))
    except ValueError:
        return None


def validate(path: Path) -> ValidationResult:
    data = load_data(path)
    errors: list[str] = []
    warnings: list[str] = []

    required_missing = maybe_int(data.get("required_files_missing_count"))
    dependencies_complete = is_true(data.get("dependencies_complete"))
    output_started = is_true(data.get("output_phase_started"))
    additional_reads_continue = is_true(data.get("additional_repo_reads_continue"))
    final_deliverable_generated = is_true(data.get("final_deliverable_generated"))
    last_completed_lock = str(data.get("last_completed_lock", "") or "")
    next_required_lock = str(data.get("next_required_lock", "") or "")
    phase = str(data.get("phase", "") or "")

    completion_claimed = dependencies_complete or required_missing == 0 or last_completed_lock == "DEPENDENCIES_CONSUMED"

    if not completion_claimed:
        warnings.append("dependency_completion_not_claimed")
        return ValidationResult(path, True, errors, warnings, dependencies_complete, output_started, required_missing)

    if required_missing == 0 and not output_started:
        errors.append("required_files_complete_but_output_phase_not_started")

    if dependencies_complete and not output_started:
        errors.append("dependencies_complete_but_output_phase_not_started")

    if last_completed_lock == "DEPENDENCIES_CONSUMED" and next_required_lock == "OUTPUT_PHASE_STARTED" and not output_started:
        errors.append("route_lock_stuck_between_dependencies_and_output_phase")

    if additional_reads_continue and not output_started:
        errors.append("additional_repo_reads_continue_before_output_phase")

    if phase == "OUTPUT_PHASE_STARTED" and not output_started:
        errors.append("phase_claims_output_started_but_flag_false")

    if final_deliverable_generated and not output_started:
        errors.append("final_deliverable_generated_without_output_phase")

    return ValidationResult(path, not errors, errors, warnings, dependencies_complete, output_started, required_missing)


def print_result(result: ValidationResult) -> None:
    missing = "unknown" if result.required_files_missing_count is None else str(result.required_files_missing_count)
    print(f"fixture={result.path}")
    print(f"result={'PASS' if result.passed else 'FAIL'}")
    print(f"dependencies_complete={str(result.dependencies_complete).lower()}")
    print(f"output_phase_started={str(result.output_phase_started).lower()}")
    print(f"required_files_missing_count={missing}")
    print(f"errors={len(result.errors)}")
    for error in result.errors:
        print(f"- {error}")
    if result.warnings:
        print(f"warnings={len(result.warnings)}")
        for warning in result.warnings:
            print(f"- {warning}")


def run_self_test() -> int:
    bad = validate(BAD_FIXTURE)
    gold = validate(GOLD_FIXTURE)
    bad_text = validate(BAD_TEXT_FIXTURE)
    gold_text = validate(GOLD_TEXT_FIXTURE)
    ok = (not bad.passed) and gold.passed and (not bad_text.passed) and gold_text.passed

    print("OUTPUT_PHASE_LOCK_SELF_TEST")
    print(f"bad_fixture: {'FAIL' if not bad.passed else 'PASS'}")
    if bad.passed:
        print_result(bad)
    print(f"gold_fixture: {'PASS' if gold.passed else 'FAIL'}")
    if not gold.passed:
        print_result(gold)
    print(f"bad_text_fixture: {'FAIL' if not bad_text.passed else 'PASS'}")
    if bad_text.passed:
        print_result(bad_text)
    print(f"gold_text_fixture: {'PASS' if gold_text.passed else 'FAIL'}")
    if not gold_text.passed:
        print_result(gold_text)

    print("OUTPUT_PHASE_LOCK_SUMMARY")
    print("bad_expected=FAIL")
    print("gold_expected=PASS")
    print("bad_text_expected=FAIL")
    print("gold_text_expected=PASS")
    print(f"validation_result={'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    if not argv:
        return run_self_test()

    ok = True
    for arg in argv:
        result = validate(Path(arg))
        print("OUTPUT_PHASE_LOCK_RESULT")
        print_result(result)
        if not result.passed:
            ok = False
    print("OUTPUT_PHASE_LOCK_SUMMARY")
    print(f"files_checked={len(argv)}")
    print(f"validation_result={'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
