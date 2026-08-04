#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


BAD_FIXTURE = Path("validators/fixtures/bad/bad_shallow_fake_pass_claims_68_reads.md")
GOLD_FIXTURE = Path("validators/fixtures/gold/gold_script_reconstructed.md")
URL_RE = re.compile(r"https?://[^\s)>\"]+")


@dataclass
class ValidationResult:
    path: Path
    passed: bool
    errors: list[str]
    blockers: list[str]
    pass_claimed: bool


def parse_kv(text: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or "=" not in line:
            continue
        key, value = line.split("=", 1)
        data[key.strip()] = value.strip()
    return data


def load_data(path: Path) -> tuple[str, dict[str, Any]]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return text, json.loads(text)
    return text, parse_kv(text)


def is_true(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value or "").strip().lower() in {"true", "yes", "1", "pass"}


def is_false(value: Any) -> bool:
    if isinstance(value, bool):
        return not value
    return str(value or "").strip().lower() in {"false", "no", "0", "fail"}


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
    pass_keys = [
        "status",
        "final_status",
        "FINAL_PROOF_STATUS",
        "final_proof_classification",
        "validation_result",
        "VALIDATION_STATUS",
    ]
    if any(str(data.get(key, "")).strip().upper() == "PASS" for key in pass_keys):
        return True
    return any(marker in text for marker in ["final_status=PASS", "FINAL_PROOF_STATUS=PASS", "VALIDATION_STATUS=PASS"])


def blocked_claimed(data: dict[str, Any], text: str) -> bool:
    block_keys = ["status", "final_status", "FINAL_PROOF_STATUS", "validation_result"]
    if any(str(data.get(key, "")).strip().upper() == "BLOCKED" for key in block_keys):
        return True
    return "final_status=BLOCKED" in text or "FINAL_PROOF_STATUS=BLOCKED" in text


def p0_blockers(data: dict[str, Any], text: str) -> list[str]:
    blockers: list[str] = []
    url_count = len(URL_RE.findall(text))

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
    source_count = int_value(data.get("source_ledger_urls_count")) or 0
    if freshness_current and source_count == 0 and url_count == 0:
        blockers.append("freshness_CURRENT_without_URL")

    if is_true(data.get("web_used")) and source_count == 0 and url_count == 0 and not data.get("command_output_or_file_reference"):
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
    ok = (not bad.passed) and gold.passed

    print("DOMINANT_FAILURE_CLASSIFIER_SELF_TEST")
    print(f"bad_fixture: {'FAIL' if not bad.passed else 'PASS'}")
    if bad.passed:
        print_result(bad)
    print(f"gold_fixture: {'PASS' if gold.passed else 'FAIL'}")
    if not gold.passed:
        print_result(gold)

    print("DOMINANT_FAILURE_CLASSIFIER_SUMMARY")
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
