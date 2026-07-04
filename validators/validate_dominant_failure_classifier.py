#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from lib.claim_normalizer import (
    ARTIFACT_PRESENT_KEYS,
    PROOF_PRESENT_KEYS,
    SOURCE_URL_COUNT_KEYS,
    WEB_USED_KEYS,
    all_values,
    count_urls,
    has_blocked_claim,
    has_pass_claim,
    is_falsey,
    is_truthy,
    parse_claims,
)
from lib.route_slice_truth import resolve_route_slice_claim

BAD_FIXTURE = Path("validators/fixtures/bad/bad_shallow_fake_pass_claims_68_reads.md")
GOLD_FIXTURE = Path("validators/fixtures/gold/gold_script_reconstructed.md")
BAD_ALIAS_FIXTURE = Path("validators/fixtures/bad/bad_latest_antigravity_alias_fake_pass.md")
GOLD_ALIAS_FIXTURE = Path("validators/fixtures/gold/gold_alias_claims_with_complete_evidence.md")
BAD_SLICE_TRUE_REGISTRY_FALSE_FIXTURE = Path("validators/fixtures/bad/bad_dominant_failure_claims_slice_true_but_registry_false.md")


@dataclass
class ValidationResult:
    path: Path
    passed: bool
    errors: list[str]
    blockers: list[str]
    pass_claimed: bool


def parse_kv(text: str) -> dict[str, str]:
    return {key: values[-1] for key, values in parse_claims(text).items() if values}


def load_data(path: Path) -> tuple[str, dict[str, Any]]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return text, {str(key).lower(): value for key, value in json.loads(text).items()}
    return text, parse_kv(text)


def is_true(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return is_truthy(value)


def is_false(value: Any) -> bool:
    if isinstance(value, bool):
        return not value
    return is_falsey(value)


def int_value(value: Any) -> int | None:
    if value is None or value == "":
        return None
    if isinstance(value, int):
        return value
    try:
        return int(str(value))
    except ValueError:
        return None


def float_value(value: Any) -> float | None:
    if value is None or value == "":
        return None
    if isinstance(value, (int, float)):
        return float(value)
    try:
        return float(str(value))
    except ValueError:
        return None


def pass_claimed(data: dict[str, Any], text: str) -> bool:
    if path_claims := parse_claims(text):
        return has_pass_claim(path_claims)
    return has_pass_claim({key: [str(value)] for key, value in data.items()})


def blocked_claimed(data: dict[str, Any], text: str) -> bool:
    claims = parse_claims(text)
    return has_blocked_claim(claims) or has_blocked_claim({key: [str(value)] for key, value in data.items()})


def p0_blockers(data: dict[str, Any], text: str) -> list[str]:
    blockers: list[str] = []
    claims = parse_claims(text)
    url_count = count_urls(text)
    route_resolution = resolve_route_slice_claim(
        route_id=data.get("route_id") or data.get("canonical_route_id"),
        task_mode=data.get("task_mode") or data.get("route_mode") or data.get("output_classification"),
        route_manifest_path=data.get("route_manifest_path"),
        route_slice_path=data.get("selected_route_slice_path") or data.get("route_slice_path"),
    )

    mandatory_reads = int_value(data.get("mandatory_files_read") or data.get("total_route_scope_files_read"))
    actual_reads = int_value(data.get("actual_files_read") or data.get("actual_reads"))
    if mandatory_reads is not None and actual_reads is not None and actual_reads < mandatory_reads:
        blockers.append("mandatory_files_claim_mismatch")

    if is_false(data.get("route_manifest_read")):
        blockers.append("route_manifest_read_false")

    if is_false(data.get("selected_route_slice_read")):
        blockers.append("selected_route_slice_read_false")

    if is_false(data.get("mandatory_route_slice_paths_consumed")):
        blockers.append("mandatory_route_slice_paths_consumed_false")

    if (data.get("selected_route_slice_path") or data.get("route_slice_path")) and not route_resolution["slice_exists"]:
        blockers.append("route_slice_registry_missing")

    if not route_resolution["source_manifest_matches"]:
        blockers.append("route_slice_source_manifest_mismatch")

    if not route_resolution["route_id_matches"]:
        blockers.append("route_slice_route_id_mismatch")

    if not route_resolution["task_mode_matches"]:
        blockers.append("route_slice_task_mode_mismatch")

    if is_true(data.get("component_consumption_unproven")):
        blockers.append("component_consumption_unproven")

    if is_false(data.get("semantic_influence_map_present")):
        blockers.append("semantic_influence_map_missing")

    if is_false(data.get("output_phase_started")):
        blockers.append("output_phase_started_false")

    if is_false(data.get("final_script_generated")):
        blockers.append("final_script_generated_false")

    if is_false(data.get("validators_run")):
        blockers.append("validators_not_run")

    if str(data.get("evidence_scope", "")) == "memory_only":
        blockers.append("memory_only_evidence_scope")

    if is_true(data.get("compaction_detected")) or is_true(data.get("continuation_after_compaction")):
        if not data.get("route_state_hash") and not data.get("route_state_path"):
            blockers.append("route_state_missing_for_compaction_or_continuation")

    freshness_current = str(data.get("freshness_class", "")).upper() == "CURRENT"
    source_count_values = [int_value(value) or 0 for value in all_values(claims, SOURCE_URL_COUNT_KEYS)]
    source_count = max(source_count_values or [int_value(data.get("source_ledger_urls_count")) or 0])
    if freshness_current and source_count == 0 and url_count == 0:
        blockers.append("freshness_CURRENT_without_URL")

    web_used = is_true(data.get("web_used")) or any(is_true(value) for value in all_values(claims, WEB_USED_KEYS))
    if web_used and source_count == 0 and url_count == 0 and not data.get("command_output_or_file_reference"):
        blockers.append("web_used_without_source_evidence")

    packet_ready_fields = [key for key, value in data.items() if str(value).upper() == "PACKET_READY"]
    if packet_ready_fields:
        proof_paths = [
            "artifact_path",
            "proof_json_path",
            "payload_path",
            "ffmpeg_command_script_path",
            "davinci_project_path",
        ]
        if not any(str(data.get(key, "")).strip() for key in proof_paths):
            blockers.append("PACKET_READY_without_artifact")

    production_pass_allowed = is_true(data.get("production_pass_allowed")) or any(
        is_true(value) for value in all_values(claims, ["production_pass_allowed"])
    )
    artifact_present = any(is_true(value) for value in all_values(claims, ARTIFACT_PRESENT_KEYS))
    proof_present = any(is_true(value) for value in all_values(claims, PROOF_PRESENT_KEYS))
    if production_pass_allowed and not (artifact_present and proof_present):
        blockers.append("production_pass_allowed_without_artifact_or_proof")

    total_runtime = int_value(data.get("total_runtime_seconds"))
    cinematic_broll = int_value(data.get("cinematic_broll_seconds"))
    if total_runtime is not None and cinematic_broll is not None:
        if cinematic_broll < math.ceil(total_runtime * 0.12):
            blockers.append("broll_ratio_below_12")

    if is_false(data.get("sfx_timestamp_map_present")) or str(data.get("sfx_clip_count", "")).lower() == "generic":
        blockers.append("sfx_depth_fail")

    if is_false(data.get("davinci_track_map_present")) or is_false(data.get("ffmpeg_command_plan_present")):
        blockers.append("davinci_depth_fail")

    required_missing = int_value(data.get("required_files_missing_count"))
    if required_missing == 0 and is_false(data.get("output_phase_started")):
        blockers.append("generation_stopped_before_output")

    return sorted(set(blockers))


def validate(path: Path) -> ValidationResult:
    text, data = load_data(path)
    blockers = p0_blockers(data, text)
    pass_status = pass_claimed(data, text)
    block_status = blocked_claimed(data, text)
    errors: list[str] = []

    if blockers and pass_status and not block_status:
        errors.append("P0_failure_markers_with_PASS_status_must_be_BLOCKED")

    if "production_pass_allowed_without_artifact_or_proof" in blockers:
        errors.append("production_pass_allowed_requires_artifact_and_proof")

    return ValidationResult(path, not errors, errors, blockers, pass_status)


def print_result(result: ValidationResult) -> None:
    print(f"fixture={result.path}")
    print(f"result={'PASS' if result.passed else 'FAIL'}")
    print(f"pass_claimed={str(result.pass_claimed).lower()}")
    print(f"dominant_failure_class={','.join(result.blockers) if result.blockers else 'none'}")
    print(f"errors={len(result.errors)}")
    for error in result.errors:
        print(f"- {error}")


def run_self_test() -> int:
    bad = validate(BAD_FIXTURE)
    gold = validate(GOLD_FIXTURE)
    bad_alias = validate(BAD_ALIAS_FIXTURE)
    gold_alias = validate(GOLD_ALIAS_FIXTURE)
    bad_slice_registry = validate(BAD_SLICE_TRUE_REGISTRY_FALSE_FIXTURE)
    ok = (
        (not bad.passed)
        and gold.passed
        and (not bad_alias.passed)
        and gold_alias.passed
        and (not bad_slice_registry.passed)
    )

    print("DOMINANT_FAILURE_CLASSIFIER_SELF_TEST")
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
    print(f"bad_slice_registry_fixture: {'FAIL' if not bad_slice_registry.passed else 'PASS'}")
    if bad_slice_registry.passed:
        print_result(bad_slice_registry)

    print("DOMINANT_FAILURE_CLASSIFIER_SUMMARY")
    print("bad_expected=FAIL")
    print("gold_expected=PASS")
    print("bad_alias_expected=FAIL")
    print("gold_alias_expected=PASS")
    print("bad_slice_registry_expected=FAIL")
    print(f"validation_result={'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    if not argv:
        return run_self_test()

    ok = True
    for arg in argv:
        result = validate(Path(arg))
        print("DOMINANT_FAILURE_CLASSIFIER_RESULT")
        print_result(result)
        if not result.passed:
            ok = False
    print("DOMINANT_FAILURE_CLASSIFIER_SUMMARY")
    print(f"files_checked={len(argv)}")
    print(f"validation_result={'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
