#!/usr/bin/env python3
from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

from lib.claim_normalizer import has_pass_claim, parse_claims
from lib.route_slice_truth import resolve_route_slice_claim


DEFAULT_TARGETS = [
    Path("registries/route_manifests/script_generation.yaml"),
    Path("registries/task_intent_routing_matrix.yaml"),
]

BAD_FIXTURE = Path("validators/fixtures/bad/bad_route_scope_68_pass_authority.yaml")
GOLD_FIXTURE = Path("validators/fixtures/gold/gold_route_scope_telemetry_only.yaml")

FORBIDDEN_MARKERS = [
    "minimum_route_scope_files_for_pass",
    "route_scope_pass_requires_file_count_by_layer",
    "route_scope_status PASS with fewer than 68 route scope files read",
    "68 route scope files read",
]

REQUIRED_MARKERS = [
    "route_scope_file_counts_are_telemetry_only: true",
    "route_scope_file_count_telemetry_reference: 68",
    "route_scope_pass_authority:",
    "selected_route_manifest_read: true",
    "selected_route_slice_read: true",
    "mandatory_route_slice_paths_consumed: true",
    "semantic_influence_map_present: true",
    "dependencies_complete: true",
    "output_phase_started: true",
    "final_deliverable_generated: true",
]


@dataclass
class ValidationResult:
    path: Path
    passed: bool
    errors: list[str]


def validate(path: Path) -> ValidationResult:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    claims = parse_claims(text)
    data = {key: values[-1] for key, values in claims.items() if values}

    for marker in FORBIDDEN_MARKERS:
        if marker in text:
            errors.append(f"forbidden_count_pass_authority_marker:{marker}")

    for marker in REQUIRED_MARKERS:
        if marker not in text:
            errors.append(f"missing_telemetry_or_pass_authority_marker:{marker}")

    if has_pass_claim(claims):
        route_resolution = resolve_route_slice_claim(
            route_id=data.get("route_id") or data.get("canonical_route_id"),
            task_mode=data.get("task_mode") or data.get("route_mode"),
            route_manifest_path=data.get("route_manifest_path"),
            route_slice_path=data.get("selected_route_slice_path") or data.get("route_slice_path"),
        )
        if (data.get("selected_route_slice_path") or data.get("route_slice_path")) and not route_resolution["slice_exists"]:
            errors.append("pass_authority_route_slice_missing")
        if not route_resolution["source_manifest_matches"]:
            errors.append("pass_authority_route_slice_source_manifest_mismatch")
        if not route_resolution["route_id_matches"]:
            errors.append("pass_authority_route_slice_route_id_mismatch")
        if not route_resolution["task_mode_matches"]:
            errors.append("pass_authority_route_slice_task_mode_mismatch")

    return ValidationResult(path=path, passed=not errors, errors=errors)


def print_result(result: ValidationResult) -> None:
    print("ROUTE_SCOPE_TELEMETRY_LAW_RESULT")
    print(f"file={result.path}")
    print(f"result={'PASS' if result.passed else 'FAIL'}")
    print(f"errors={len(result.errors)}")
    for error in result.errors:
        print(f"- {error}")


def run_self_test() -> int:
    bad = validate(BAD_FIXTURE)
    gold = validate(GOLD_FIXTURE)
    ok = (not bad.passed) and gold.passed

    print("ROUTE_SCOPE_TELEMETRY_LAW_SELF_TEST")
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
        return run_self_test()

    targets = [Path(arg) for arg in argv] if argv else DEFAULT_TARGETS
    ok = True
    for target in targets:
        try:
            result = validate(target)
        except Exception as exc:  # noqa: BLE001 - CLI validator must report parser failures.
            result = ValidationResult(target, False, [f"validator_internal_error:{exc}"])
        print_result(result)
        ok = ok and result.passed

    print("ROUTE_SCOPE_TELEMETRY_LAW_SUMMARY")
    print(f"files_checked={len(targets)}")
    print(f"validation_result={'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
