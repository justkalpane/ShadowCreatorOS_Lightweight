#!/usr/bin/env python3
from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path


BAD_FIXTURE = Path("validators/fixtures/bad/bad_shallow_fake_pass_claims_68_reads.md")
GOLD_FIXTURE = Path("validators/fixtures/gold/gold_script_reconstructed.md")


@dataclass
class ValidationResult:
    path: Path
    passed: bool
    errors: list[str]
    warnings: list[str]


def parse_kv(text: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("|") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        data[key.strip()] = value.strip()
    return data


def is_true(value: str | None) -> bool:
    return (value or "").strip().lower() in {"true", "yes", "1", "pass"}


def is_false(value: str | None) -> bool:
    return (value or "").strip().lower() in {"false", "no", "0", "fail"}


def int_value(value: str | None) -> int | None:
    if value is None or value == "":
        return None
    try:
        return int(value)
    except ValueError:
        return None


def pass_claimed(data: dict[str, str], text: str) -> bool:
    final_status = data.get("final_status", "")
    status = data.get("status", "")
    proof = data.get("final_proof_classification", "")
    return (
        final_status.upper() == "PASS"
        or status.upper() == "PASS"
        or proof.upper() == "PASS"
        or "final_status=PASS" in text
        or "FINAL_PROOF_STATUS=PASS" in text
    )


def has_route_manifest_evidence(data: dict[str, str]) -> bool:
    if is_false(data.get("route_manifest_read")):
        return False
    return is_true(data.get("route_manifest_read")) or bool(data.get("route_manifest_path"))


def has_semantic_influence(data: dict[str, str], text: str) -> bool:
    if is_false(data.get("semantic_influence_map_present")):
        return False
    if "SEMANTIC_INFLUENCE_MAP" in text and data.get("status") in {"USED", "PASS"}:
        return True
    return is_true(data.get("semantic_influence_map_present"))


def has_final_output(data: dict[str, str], text: str) -> bool:
    if is_false(data.get("final_script_generated")):
        return False
    return is_true(data.get("final_script_generated")) or "FINAL_SCRIPT" in text


def validate(path: Path) -> ValidationResult:
    text = path.read_text(encoding="utf-8")
    data = parse_kv(text)
    errors: list[str] = []
    warnings: list[str] = []
    claimed_pass = pass_claimed(data, text)

    mandatory_reads = int_value(data.get("mandatory_files_read") or data.get("total_route_scope_files_read"))
    actual_reads = int_value(data.get("actual_files_read") or data.get("actual_reads"))
    if mandatory_reads is not None and actual_reads is not None and actual_reads < mandatory_reads:
        errors.append(
            f"mandatory_files_claim_mismatch: claimed={mandatory_reads} actual={actual_reads}"
        )

    if claimed_pass and not has_route_manifest_evidence(data):
        errors.append("route_manifest_read_or_path_missing_for_PASS")

    if claimed_pass and is_false(data.get("selected_route_slice_read")):
        errors.append("selected_route_slice_read_false_for_PASS")

    if claimed_pass and is_false(data.get("mandatory_route_slice_paths_consumed")):
        errors.append("mandatory_route_slice_paths_consumed_false_for_PASS")

    if claimed_pass and is_true(data.get("component_consumption_unproven")):
        errors.append("component_consumption_unproven_with_PASS")

    if claimed_pass and not has_semantic_influence(data, text):
        errors.append("semantic_influence_map_missing_for_PASS")

    if claimed_pass and is_false(data.get("output_phase_started")):
        errors.append("output_phase_started_false_for_PASS")

    if claimed_pass and not has_final_output(data, text):
        errors.append("final_output_missing_for_PASS")

    if claimed_pass and is_false(data.get("validators_run")):
        errors.append("validators_run_false_for_PASS")

    if claimed_pass and data.get("evidence_scope") == "memory_only":
        errors.append("memory_only_evidence_scope_cannot_PASS")

    if claimed_pass and "CLAIM_EVIDENCE_STATUS" in text:
        evidence_path = data.get("evidence_path", "")
        command_ref = data.get("command_output_or_file_reference", "")
        if not evidence_path and not command_ref:
            errors.append("claim_evidence_status_PASS_missing_path_or_command_reference")

    if data.get("route_id") == "SCRIPT_GENERATION" and claimed_pass:
        if not is_true(data.get("selected_route_slice_read")) and not data.get("route_manifest_path"):
            errors.append("script_generation_PASS_without_route_scope_evidence")

    return ValidationResult(path=path, passed=not errors, errors=errors, warnings=warnings)


def print_result(result: ValidationResult) -> None:
    print(f"fixture={result.path}")
    print(f"result={'PASS' if result.passed else 'FAIL'}")
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

    print("ROUTE_CLAIM_EVIDENCE_CONSISTENCY_SELF_TEST")
    print(f"bad_fixture: {'FAIL' if not bad.passed else 'PASS'}")
    if bad.passed:
        print_result(bad)
    print(f"gold_fixture: {'PASS' if gold.passed else 'FAIL'}")
    if not gold.passed:
        print_result(gold)

    ok = (not bad.passed) and gold.passed
    print("ROUTE_CLAIM_EVIDENCE_CONSISTENCY_SUMMARY")
    print("bad_fixture_expected=FAIL")
    print("gold_fixture_expected=PASS")
    print(f"validation_result={'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    if not argv:
        return run_self_test()

    ok = True
    for arg in argv:
        result = validate(Path(arg))
        print("ROUTE_CLAIM_EVIDENCE_CONSISTENCY_RESULT")
        print_result(result)
        if not result.passed:
            ok = False
    print("ROUTE_CLAIM_EVIDENCE_CONSISTENCY_SUMMARY")
    print(f"files_checked={len(argv)}")
    print(f"validation_result={'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
