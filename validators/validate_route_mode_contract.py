#!/usr/bin/env python3
from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

from lib.claim_normalizer import first_value, normalize_task_mode, parse_claims
from lib.route_slice_truth import resolve_route_slice_claim


BAD_STANDARD_SCRIPT_FIXTURE = Path("validators/fixtures/bad/bad_antigravity_standard_script_mode.md")
BAD_VISUAL_ALIAS_FIXTURE = Path("validators/fixtures/bad/bad_visual_generator_alias_unclassified.md")
BAD_WRONG_SLICE_FIXTURE = Path("validators/fixtures/bad/bad_route_mode_existing_path_wrong_slice.md")
GOLD_SCRIPT_ONLY_FIXTURE = Path("validators/fixtures/gold/gold_script_only_route_mode.md")
GOLD_VISUAL_ALIAS_FIXTURE = Path("validators/fixtures/gold/gold_visual_generation_draft_mode_alias_normalized.md")

CANONICAL_ROUTE_MODES = {
    "SCRIPT_GENERATION": {
        "script_only",
        "script_plus_visual_plan",
        "script_plus_visual_generation_draft",
        "script_plus_media_factory_handoff",
        "full_content_packet",
    },
    "MEDIA_FACTORY_HANDOFF": {
        "visual_media_plan",
        "script_plus_visual_plan",
        "script_plus_visual_generation_draft",
        "script_plus_media_factory_handoff",
        "media_factory_handoff",
    },
}

INVALID_MODES = {"INVALID_STANDARD_SCRIPT", "standard_script"}


@dataclass
class ValidationResult:
    path: Path
    passed: bool
    errors: list[str]
    route_id: str
    task_mode: str
    normalized_task_mode: str
    route_manifest_path_present: bool
    route_slice_present: bool


def validate(path: Path) -> ValidationResult:
    text = path.read_text(encoding="utf-8")
    claims = parse_claims(text)
    route_id = first_value(claims, ["route_id", "canonical_route_id"], "")
    task_mode = first_value(claims, ["task_mode", "output_classification", "route_mode"], "")
    normalized = normalize_task_mode(task_mode)
    route_manifest = first_value(claims, ["route_manifest_path"], "")
    route_slice = first_value(claims, ["selected_route_slice_path", "route_slice_path"], "")
    route_resolution = resolve_route_slice_claim(route_id, normalized, route_manifest, route_slice)
    errors: list[str] = []

    if not route_id:
        errors.append("route_id_missing")

    if not task_mode:
        errors.append("task_mode_missing")

    if normalized in INVALID_MODES:
        errors.append("invalid_task_mode_standard_script")

    if route_id == "SCRIPT_GENERATION" and normalized == "script_plus_visual_generation_draft":
        if "visual_media_generator_draft" in task_mode.lower():
            errors.append("visual_media_generator_draft_alias_requires_canonical_mode_declaration")

    allowed_modes = CANONICAL_ROUTE_MODES.get(route_id)
    if allowed_modes is not None and normalized not in allowed_modes:
        errors.append(f"task_mode_not_allowed_for_route:{route_id}:{normalized}")

    if route_id == "SCRIPT_GENERATION" and normalized != "script_only":
        plain_script_markers = [
            "plain_script_request=true",
            "user_requested_downstream_visual_plan=false",
            "user_requested_media_factory=false",
        ]
        if any(marker in text for marker in plain_script_markers):
            errors.append("plain_script_generation_must_use_script_only")

    if route_id and not route_manifest:
        errors.append("route_manifest_path_missing")

    if route_id and not route_slice:
        errors.append("selected_route_slice_path_missing")
    elif route_slice and not route_resolution["slice_exists"]:
        errors.append("selected_route_slice_path_not_found")

    if route_slice and not route_resolution["source_manifest_matches"]:
        errors.append("selected_route_slice_source_manifest_mismatch")

    if route_slice and not route_resolution["route_id_matches"]:
        errors.append("selected_route_slice_route_id_mismatch")

    if route_slice and not route_resolution["task_mode_matches"]:
        errors.append("selected_route_slice_task_mode_mismatch")

    return ValidationResult(
        path=path,
        passed=not errors,
        errors=errors,
        route_id=route_id,
        task_mode=task_mode,
        normalized_task_mode=normalized,
        route_manifest_path_present=bool(route_manifest),
        route_slice_present=bool(route_slice),
    )


def print_result(result: ValidationResult) -> None:
    print("ROUTE_MODE_CONTRACT_RESULT")
    print(f"fixture={result.path}")
    print(f"result={'PASS' if result.passed else 'FAIL'}")
    print(f"route_id={result.route_id or 'missing'}")
    print(f"task_mode={result.task_mode or 'missing'}")
    print(f"normalized_task_mode={result.normalized_task_mode or 'missing'}")
    print(f"route_manifest_path_present={str(result.route_manifest_path_present).lower()}")
    print(f"route_slice_path_present={str(result.route_slice_present).lower()}")
    print(f"errors={len(result.errors)}")
    for error in result.errors:
        print(f"- {error}")


def self_test() -> int:
    bad_standard = validate(BAD_STANDARD_SCRIPT_FIXTURE)
    bad_visual_alias = validate(BAD_VISUAL_ALIAS_FIXTURE)
    bad_wrong_slice = validate(BAD_WRONG_SLICE_FIXTURE)
    gold_script = validate(GOLD_SCRIPT_ONLY_FIXTURE)
    gold_visual = validate(GOLD_VISUAL_ALIAS_FIXTURE)
    ok = (
        (not bad_standard.passed)
        and (not bad_visual_alias.passed)
        and (not bad_wrong_slice.passed)
        and gold_script.passed
        and gold_visual.passed
    )

    print("ROUTE_MODE_CONTRACT_SELF_TEST")
    print(f"bad_standard_script_expected=FAIL actual={'PASS' if bad_standard.passed else 'FAIL'}")
    if bad_standard.passed:
        print_result(bad_standard)
    print(f"bad_visual_alias_expected=FAIL actual={'PASS' if bad_visual_alias.passed else 'FAIL'}")
    if bad_visual_alias.passed:
        print_result(bad_visual_alias)
    print(f"bad_wrong_slice_expected=FAIL actual={'PASS' if bad_wrong_slice.passed else 'FAIL'}")
    if bad_wrong_slice.passed:
        print_result(bad_wrong_slice)
    print(f"gold_script_only_expected=PASS actual={'PASS' if gold_script.passed else 'FAIL'}")
    if not gold_script.passed:
        print_result(gold_script)
    print(f"gold_visual_alias_expected=PASS actual={'PASS' if gold_visual.passed else 'FAIL'}")
    if not gold_visual.passed:
        print_result(gold_visual)
    print(f"validation_result={'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    if not argv:
        return self_test()
    ok = True
    for arg in argv:
        try:
            result = validate(Path(arg))
        except Exception as exc:  # noqa: BLE001 - CLI validator must report parser failures.
            print("ROUTE_MODE_CONTRACT_RESULT")
            print(f"fixture={arg}")
            print("result=FAIL")
            print("errors=1")
            print(f"- validator_internal_error:{exc}")
            ok = False
            continue
        print_result(result)
        ok = ok and result.passed
    print("ROUTE_MODE_CONTRACT_SUMMARY")
    print(f"files_checked={len(argv)}")
    print(f"validation_result={'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
