#!/usr/bin/env python3
from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

from lib.claim_normalizer import has_pass_claim, is_falsey, is_truthy, parse_claims
from lib.route_slice_truth import resolve_route_slice_claim

BAD_FIXTURE = Path("validators/fixtures/bad/bad_shallow_fake_pass_claims_68_reads.md")
GOLD_FIXTURE = Path("validators/fixtures/gold/gold_script_reconstructed.md")
BAD_ALIAS_FIXTURE = Path("validators/fixtures/bad/bad_latest_antigravity_alias_fake_pass.md")
GOLD_ALIAS_FIXTURE = Path("validators/fixtures/gold/gold_alias_claims_with_complete_evidence.md")
BAD_FAKE_SLICE_FIXTURE = Path("validators/fixtures/bad/bad_route_claim_pass_with_fake_slice_path.md")
BAD_SLICE_MISMATCH_FIXTURE = Path("validators/fixtures/bad/bad_route_claim_pass_with_manifest_slice_mismatch.md")
GOLD_SLICE_LINEAGE_FIXTURE = Path("validators/fixtures/gold/gold_route_claim_with_verified_slice_lineage.md")


@dataclass
class ValidationResult:
    path: Path
    passed: bool
    errors: list[str]
    warnings: list[str]


def parse_kv(text: str) -> dict[str, str]:
    return {key: values[-1] for key, values in parse_claims(text).items() if values}


def is_true(value: str | None) -> bool:
    return is_truthy(value)


def is_false(value: str | None) -> bool:
    return is_falsey(value)


def int_value(value: str | None) -> int | None:
    if value is None or value == "":
        return None
    try:
        return int(value)
    except ValueError:
        return None


def pass_claimed(data: dict[str, str], text: str) -> bool:
    return has_pass_claim(parse_claims(text))


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
    route_resolution = resolve_route_slice_claim(
        route_id=data.get("route_id") or data.get("canonical_route_id"),
        task_mode=data.get("task_mode") or data.get("route_mode") or data.get("output_classification"),
        route_manifest_path=data.get("route_manifest_path"),
        route_slice_path=data.get("selected_route_slice_path") or data.get("route_slice_path"),
    )

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

    if claimed_pass and route_resolution["expected"] and not route_resolution["slice_exists"]:
        errors.append("route_slice_missing_for_PASS")

    if claimed_pass and not route_resolution["source_manifest_matches"]:
        errors.append("route_slice_source_manifest_mismatch_for_PASS")

    if claimed_pass and not route_resolution["route_id_matches"]:
        errors.append("route_slice_route_id_mismatch_for_PASS")

    if claimed_pass and not route_resolution["task_mode_matches"]:
        errors.append("route_slice_task_mode_mismatch_for_PASS")

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
    bad_alias = validate(BAD_ALIAS_FIXTURE)
    gold_alias = validate(GOLD_ALIAS_FIXTURE)
    bad_fake_slice = validate(BAD_FAKE_SLICE_FIXTURE)
    bad_slice_mismatch = validate(BAD_SLICE_MISMATCH_FIXTURE)
    gold_slice_lineage = validate(GOLD_SLICE_LINEAGE_FIXTURE)

    print("ROUTE_CLAIM_EVIDENCE_CONSISTENCY_SELF_TEST")
    print(f"bad_fixture: {'FAIL' if not bad.passed else 'PASS'}")
    if bad.passed:
        print_result(bad)
    print(f"gold_fixture: {'PASS' if gold.passed else 'FAIL'}")
    if not gold.passed:
        print_result(gold)

    print(f"bad_alias_fixture: {'FAIL' if not bad_alias.passed else 'PASS'}")
    if bad_alias.passed:
        print_result(bad_alias)
    print(f"gold_alias_fixture: {'PASS' if gold_alias.passed else 'FAIL'}")
    if not gold_alias.passed:
        print_result(gold_alias)
    print(f"bad_fake_slice_fixture: {'FAIL' if not bad_fake_slice.passed else 'PASS'}")
    if bad_fake_slice.passed:
        print_result(bad_fake_slice)
    print(f"bad_slice_mismatch_fixture: {'FAIL' if not bad_slice_mismatch.passed else 'PASS'}")
    if bad_slice_mismatch.passed:
        print_result(bad_slice_mismatch)
    print(f"gold_slice_lineage_fixture: {'PASS' if gold_slice_lineage.passed else 'FAIL'}")
    if not gold_slice_lineage.passed:
        print_result(gold_slice_lineage)

    ok = (
        (not bad.passed)
        and gold.passed
        and (not bad_alias.passed)
        and gold_alias.passed
        and (not bad_fake_slice.passed)
        and (not bad_slice_mismatch.passed)
        and gold_slice_lineage.passed
    )
    print("ROUTE_CLAIM_EVIDENCE_CONSISTENCY_SUMMARY")
    print("bad_fixture_expected=FAIL")
    print("gold_fixture_expected=PASS")
    print("bad_alias_fixture_expected=FAIL")
    print("gold_alias_fixture_expected=PASS")
    print("bad_fake_slice_fixture_expected=FAIL")
    print("bad_slice_mismatch_fixture_expected=FAIL")
    print("gold_slice_lineage_fixture_expected=PASS")
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
