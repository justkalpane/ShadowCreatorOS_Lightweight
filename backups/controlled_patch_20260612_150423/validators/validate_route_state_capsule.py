#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


BAD_FIXTURE = Path("validators/fixtures/bad/bad_route_state_missing.md")
GOLD_FIXTURE = Path("validators/fixtures/gold/gold_route_state_resume_capsule.json")

REQUIRED_SCALAR_FIELDS = [
    "route_id",
    "route_manifest_path",
    "route_manifest_hash",
    "task_intent",
    "output_mode",
    "phase",
    "last_completed_lock",
    "next_required_lock",
    "evidence_scope",
]

REQUIRED_LIST_FIELDS = [
    "files_read",
    "selected_directors",
    "selected_agents",
    "selected_subagents",
    "selected_skills",
    "selected_subskills",
]

ALLOWED_PASS_EVIDENCE_SCOPES = {
    "current_cycle",
    "previous_cycle_with_step_reference",
    "persisted_route_state_with_hash",
}


@dataclass
class ValidationResult:
    path: Path
    passed: bool
    errors: list[str]
    warnings: list[str]
    route_id: str
    evidence_scope: str


def parse_kv(text: str) -> dict[str, Any]:
    data: dict[str, Any] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or "=" not in line:
            continue
        key, value = line.split("=", 1)
        data[key.strip()] = value.strip()
    return data


def load_capsule(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return json.loads(text)
    try:
        parsed = json.loads(text)
        if isinstance(parsed, dict):
            return parsed
    except json.JSONDecodeError:
        pass
    return parse_kv(text)


def is_true(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return str(value or "").strip().lower() in {"true", "yes", "1", "pass"}


def is_pass(value: Any) -> bool:
    return str(value or "").strip().upper() == "PASS"


def is_non_empty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip()) and value.strip().lower() not in {"none", "null", "n/a", "-"}
    if isinstance(value, (list, tuple, set, dict)):
        return len(value) > 0
    return True


def as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    if isinstance(value, str) and value.strip():
        return [item.strip() for item in value.split(",") if item.strip()]
    return []


def final_or_continuation_claimed(data: dict[str, Any]) -> bool:
    return (
        is_true(data.get("compaction_detected"))
        or is_true(data.get("continuation_after_compaction"))
        or is_true(data.get("compaction_recovery_allowed"))
        or is_true(data.get("final_output_allowed"))
        or is_pass(data.get("status"))
        or is_pass(data.get("final_status"))
    )


def validate(path: Path) -> ValidationResult:
    data = load_capsule(path)
    errors: list[str] = []
    warnings: list[str] = []
    route_id = str(data.get("route_id", "") or "")
    evidence_scope = str(data.get("evidence_scope", "") or "")
    sensitive_claim = final_or_continuation_claimed(data)

    if not sensitive_claim:
        warnings.append("no_compaction_continuation_or_final_output_claim_detected")
        return ValidationResult(path, True, errors, warnings, route_id, evidence_scope)

    for field in REQUIRED_SCALAR_FIELDS:
        if not is_non_empty(data.get(field)):
            errors.append(f"required_route_state_field_missing:{field}")

    for field in REQUIRED_LIST_FIELDS:
        if not as_list(data.get(field)):
            errors.append(f"required_route_state_list_missing:{field}")

    file_hashes = data.get("file_hashes")
    if not isinstance(file_hashes, dict) or not file_hashes:
        errors.append("file_hashes_missing_or_empty")
    else:
        missing_hashes = [file_path for file_path in as_list(data.get("files_read")) if not is_non_empty(file_hashes.get(file_path))]
        if missing_hashes:
            errors.append("file_hashes_missing_for_files_read:" + ",".join(missing_hashes))

    if evidence_scope == "memory_only":
        errors.append("memory_only_evidence_scope_cannot_authorize_route_state_PASS")

    if evidence_scope and evidence_scope not in ALLOWED_PASS_EVIDENCE_SCOPES:
        errors.append(f"unsupported_evidence_scope:{evidence_scope}")

    if (
        is_true(data.get("compaction_detected"))
        or is_true(data.get("continuation_after_compaction"))
        or is_true(data.get("compaction_recovery_allowed"))
    ) and evidence_scope != "persisted_route_state_with_hash":
        errors.append("compaction_recovery_requires_persisted_route_state_with_hash")

    if is_true(data.get("final_output_allowed")):
        if not is_true(data.get("dependencies_complete")):
            errors.append("final_output_allowed_without_dependencies_complete")
        if not is_true(data.get("output_phase_started")):
            errors.append("final_output_allowed_without_output_phase_started")

    route_manifest_hash = str(data.get("route_manifest_hash", "") or "")
    if route_manifest_hash and not route_manifest_hash.startswith("sha256:"):
        errors.append("route_manifest_hash_must_use_sha256_prefix")

    return ValidationResult(path, not errors, errors, warnings, route_id, evidence_scope)


def print_result(result: ValidationResult) -> None:
    print(f"fixture={result.path}")
    print(f"result={'PASS' if result.passed else 'FAIL'}")
    print(f"route_id={result.route_id or 'missing'}")
    print(f"evidence_scope={result.evidence_scope or 'missing'}")
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

    print("ROUTE_STATE_CAPSULE_SELF_TEST")
    print(f"bad_fixture: {'FAIL' if not bad.passed else 'PASS'}")
    if bad.passed:
        print_result(bad)
    print(f"gold_fixture: {'PASS' if gold.passed else 'FAIL'}")
    if not gold.passed:
        print_result(gold)

    print("ROUTE_STATE_CAPSULE_SUMMARY")
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
        print("ROUTE_STATE_CAPSULE_RESULT")
        print_result(result)
        if not result.passed:
            ok = False
    print("ROUTE_STATE_CAPSULE_SUMMARY")
    print(f"files_checked={len(argv)}")
    print(f"validation_result={'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
