#!/usr/bin/env python3
from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path


BAD_FIXTURE = Path("validators/fixtures/bad/bad_packet_ready_without_artifacts.md")
GOLD_FIXTURE = Path("validators/fixtures/gold/gold_packet_ready_with_artifacts.md")

PACKET_READY_FIELDS = {
    "DaVinci_Resolve",
    "FFmpeg",
    "tool_specific_translation_readiness",
}


@dataclass
class ValidationResult:
    path: Path
    passed: bool
    errors: list[str]
    warnings: list[str]
    packet_ready_fields: list[str]


def parse_kv(text: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or "=" not in line:
            continue
        key, value = line.split("=", 1)
        data[key.strip()] = value.strip()
    return data


def is_true(value: str | None) -> bool:
    return (value or "").strip().lower() in {"true", "yes", "1", "pass"}


def non_empty_path(data: dict[str, str], key: str) -> bool:
    value = data.get(key, "").strip()
    return bool(value) and value not in {"-", "None", "null", "N/A"}


def packet_ready_claims(data: dict[str, str]) -> list[str]:
    claims: list[str] = []
    for key, value in data.items():
        if value.strip().upper() == "PACKET_READY":
            claims.append(key)
    return claims


def validate(path: Path) -> ValidationResult:
    text = path.read_text(encoding="utf-8")
    data = parse_kv(text)
    ready_fields = packet_ready_claims(data)
    errors: list[str] = []
    warnings: list[str] = []

    if not ready_fields:
        warnings.append("no_PACKET_READY_claim_detected")
        return ValidationResult(path, True, errors, warnings, ready_fields)

    if "DaVinci_Resolve" in ready_fields and not (
        non_empty_path(data, "davinci_project_path") or non_empty_path(data, "artifact_path")
    ):
        errors.append("DaVinci_Resolve_PACKET_READY_missing_davinci_project_or_artifact_path")

    if "FFmpeg" in ready_fields and not (
        non_empty_path(data, "ffmpeg_command_script_path") or non_empty_path(data, "artifact_path")
    ):
        errors.append("FFmpeg_PACKET_READY_missing_command_script_or_artifact_path")

    if "tool_specific_translation_readiness" in ready_fields and not non_empty_path(data, "payload_path"):
        errors.append("tool_specific_translation_PACKET_READY_missing_payload_path")

    if not non_empty_path(data, "proof_json_path"):
        errors.append("PACKET_READY_missing_proof_json_path")

    if not (
        non_empty_path(data, "artifact_path")
        or non_empty_path(data, "davinci_project_path")
        or non_empty_path(data, "payload_path")
        or non_empty_path(data, "ffmpeg_command_script_path")
    ):
        errors.append("PACKET_READY_without_any_artifact_payload_or_command_path")

    if is_true(data.get("media_artifacts_claimed")) and not is_true(data.get("local_engine_execution_approved")):
        errors.append("media_artifacts_claimed_without_local_engine_execution_approval")

    if data.get("final_status", "").upper() == "PASS" and errors:
        errors.append("final_status_PASS_with_unbacked_PACKET_READY")

    return ValidationResult(path, not errors, errors, warnings, ready_fields)


def print_result(result: ValidationResult) -> None:
    print(f"fixture={result.path}")
    print(f"result={'PASS' if result.passed else 'FAIL'}")
    print(f"packet_ready_fields={','.join(result.packet_ready_fields) if result.packet_ready_fields else 'none'}")
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

    print("PACKET_READY_ARTIFACT_SELF_TEST")
    print(f"bad_fixture: {'FAIL' if not bad.passed else 'PASS'}")
    if bad.passed:
        print_result(bad)
    print(f"gold_fixture: {'PASS' if gold.passed else 'FAIL'}")
    if not gold.passed:
        print_result(gold)

    print("PACKET_READY_ARTIFACT_SUMMARY")
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
        print("PACKET_READY_ARTIFACT_RESULT")
        print_result(result)
        if not result.passed:
            ok = False
    print("PACKET_READY_ARTIFACT_SUMMARY")
    print(f"files_checked={len(argv)}")
    print(f"validation_result={'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
