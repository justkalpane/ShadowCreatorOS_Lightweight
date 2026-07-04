#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any


BAD_FIXTURE = Path("validators/fixtures/bad/bad_duplicate_reads_after_manifest_complete.json")
GOLD_FIXTURE = Path("validators/fixtures/gold/gold_no_duplicate_reads_route_ledger.json")

ALLOWED_REREAD_REASONS = {
    "file_hash_changed",
    "audit_mode",
    "validator_mode",
    "explicit_user_requested_compare",
    "route_manifest_changed",
    "compaction_recovery_validation",
}


@dataclass
class ValidationResult:
    path: Path
    passed: bool
    errors: list[str]
    warnings: list[str]
    duplicate_count: int
    read_entries: int


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def is_true(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value or "").strip().lower() in {"true", "yes", "1", "pass"}


def int_value(value: Any) -> int:
    if isinstance(value, int):
        return value
    try:
        return int(str(value or "0"))
    except ValueError:
        return 0


def reason_allowed(reason: Any) -> bool:
    return str(reason or "").strip() in ALLOWED_REREAD_REASONS


def validate(path: Path) -> ValidationResult:
    data = load_json(path)
    errors: list[str] = []
    warnings: list[str] = []
    ledger = data.get("read_ledger")
    if not isinstance(ledger, list):
        return ValidationResult(path, False, ["read_ledger_missing_or_not_list"], warnings, 0, 0)

    duplicate_count = 0
    identity_counter: Counter[tuple[str, str]] = Counter()
    dependencies_complete = is_true(data.get("dependencies_complete"))
    output_phase_started = is_true(data.get("output_phase_started"))

    for index, entry in enumerate(ledger):
        if not isinstance(entry, dict):
            errors.append(f"read_ledger_entry_not_object:index={index}")
            continue

        file_path = str(entry.get("file_path", "") or "")
        file_hash = str(entry.get("file_hash", "") or "")
        read_count = int_value(entry.get("read_count"))
        reread_reason = str(entry.get("reread_reason", "") or "")

        if not file_path:
            errors.append(f"read_ledger_file_path_missing:index={index}")
        if not file_hash:
            errors.append(f"read_ledger_file_hash_missing:{file_path or index}")

        if file_path and file_hash:
            identity_counter[(file_path, file_hash)] += max(read_count, 1)

        if read_count > 1:
            duplicate_count += read_count - 1
            if not reason_allowed(reread_reason):
                errors.append(
                    "repeat_read_without_allowed_reason:"
                    f"file={file_path}:hash={file_hash}:read_count={read_count}:reason={reread_reason or 'missing'}"
                )

        if dependencies_complete and not output_phase_started and read_count > 1 and not reason_allowed(reread_reason):
            errors.append(f"duplicate_read_after_dependencies_complete_without_output_phase:file={file_path}")

    for (file_path, file_hash), total_reads in identity_counter.items():
        if total_reads > 1:
            matching_entries = [
                entry for entry in ledger
                if isinstance(entry, dict)
                and entry.get("file_path") == file_path
                and entry.get("file_hash") == file_hash
            ]
            allowed = all(reason_allowed(entry.get("reread_reason", "")) or int_value(entry.get("read_count")) <= 1 for entry in matching_entries)
            if not allowed:
                errors.append(
                    "same_unchanged_file_hash_read_multiple_times_without_reason:"
                    f"file={file_path}:hash={file_hash}:total_reads={total_reads}"
                )

    if duplicate_count == 0:
        warnings.append("no_duplicate_reads_detected")

    return ValidationResult(path, not errors, errors, warnings, duplicate_count, len(ledger))


def print_result(result: ValidationResult) -> None:
    print(f"fixture={result.path}")
    print(f"result={'PASS' if result.passed else 'FAIL'}")
    print(f"read_entries={result.read_entries}")
    print(f"duplicate_read_count={result.duplicate_count}")
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
    ok = (not bad.passed) and gold.passed

    print("DUPLICATE_READ_GUARD_SELF_TEST")
    print(f"bad_fixture: {'FAIL' if not bad.passed else 'PASS'}")
    if bad.passed:
        print_result(bad)
    print(f"gold_fixture: {'PASS' if gold.passed else 'FAIL'}")
    if not gold.passed:
        print_result(gold)

    print("DUPLICATE_READ_GUARD_SUMMARY")
    print("bad_expected=FAIL")
    print("gold_expected=PASS")
    print(f"validation_result={'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    if not argv:
        return run_self_test()

    ok = True
    for arg in argv:
        result = validate(Path(arg))
        print("DUPLICATE_READ_GUARD_RESULT")
        print_result(result)
        if not result.passed:
            ok = False
    print("DUPLICATE_READ_GUARD_SUMMARY")
    print(f"files_checked={len(argv)}")
    print(f"validation_result={'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
