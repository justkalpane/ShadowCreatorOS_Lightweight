#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from lib.batch3_validator_configs import validate_no_fake_pass_gate
from lib.batch3_validator_core import load_data

VALIDATOR_NAME = "validate_no_fake_pass_gate"
GOLD_FIXTURES = [Path("validators/fixtures/gold/pass_with_evidence_bundle.json")]
BAD_FIXTURES = [
    Path("validators/fixtures/bad/pass_reason_ffprobe_only.json"),
    Path("validators/fixtures/bad/pass_reason_file_exists_only.json"),
    Path("validators/fixtures/bad/pass_reason_exit_code_0_only.json"),
    Path("validators/fixtures/bad/pass_reason_contract_exists_only.json"),
]
def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog=VALIDATOR_NAME)
    parser.add_argument("--input", type=Path, help="Path to a JSON or claim-text input file.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as blockers.")
    parser.add_argument("path", nargs="?", type=Path, help=argparse.SUPPRESS)
    return parser.parse_args(argv)


def resolve_input_path(args: argparse.Namespace) -> Path | None:
    if args.input and args.path:
        raise ValueError("use either --input or a positional path, not both")
    return args.input or args.path


def build_pass_evidence_matrix(data: dict) -> list[dict]:
    matrix: list[dict] = []
    for claim in data.get("pass_claims", []) or []:
        matrix.append(
            {
                "claim_id": claim.get("claim_id"),
                "claim": claim.get("claim"),
                "status": claim.get("status"),
                "pass_reason": claim.get("pass_reason"),
                "validator_status": claim.get("validator_status"),
                "artifact_paths": claim.get("artifact_paths", []),
                "evidence_bundle_id": data.get("evidence_bundle_id"),
                "route_id": data.get("route_id"),
                "claim_context": data.get("claim_context"),
                "route_state_capsule_id": data.get("route_state_capsule_id"),
                "audit_event_id": data.get("audit_event_id"),
            }
        )
    return matrix


def validate_path(path: Path) -> dict:
    data = load_data(path)
    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(data, dict):
        errors.append("input_not_object")
        data = {}
    else:
        validate_no_fake_pass_gate(data, errors, warnings)

    passed = not errors and not warnings
    result = {
        "validator": VALIDATOR_NAME,
        "input": str(path),
        "passed": passed,
        "errors": errors,
        "warnings": warnings,
        "evidence_bundle_id": data.get("evidence_bundle_id") if isinstance(data, dict) else None,
        "route_id": data.get("route_id") if isinstance(data, dict) else None,
        "human_review_status": data.get("human_review_status") if isinstance(data, dict) else None,
        "pass_reason": data.get("pass_reason") if isinstance(data, dict) else None,
        "claim_context": data.get("claim_context") if isinstance(data, dict) else None,
        "route_state_capsule_id": data.get("route_state_capsule_id") if isinstance(data, dict) else None,
        "audit_event_id": data.get("audit_event_id") if isinstance(data, dict) else None,
        "pass_evidence_matrix": build_pass_evidence_matrix(data if isinstance(data, dict) else {}),
        "route_pass_evidence_matrix": build_pass_evidence_matrix(data if isinstance(data, dict) else {}),
    }
    if passed:
        result["summary"] = "PASS points to concrete evidence artifacts."
    else:
        result["summary"] = "FAIL"
    return result


def emit_result(result: dict, json_mode: bool) -> None:
    if json_mode:
        print(json.dumps(result, indent=2, sort_keys=True))
        return

    print("NO_FAKE_PASS_GATE_RESULT")
    print(f"validator={result['validator']}")
    print(f"input={result['input']}")
    print(f"status={'PASS' if result['passed'] else 'FAIL'}")
    print(f"evidence_bundle_id={result.get('evidence_bundle_id') or 'missing'}")
    print(f"route_id={result.get('route_id') or 'missing'}")
    print(f"pass_reason={result.get('pass_reason') or 'missing'}")
    print(f"claim_context={result.get('claim_context') or 'missing'}")
    print(f"route_state_capsule_id={result.get('route_state_capsule_id') or 'missing'}")
    print(f"audit_event_id={result.get('audit_event_id') or 'missing'}")
    print(f"pass_evidence_matrix_rows={len(result.get('pass_evidence_matrix', []))}")
    if result.get("warnings"):
        print(f"warnings={len(result['warnings'])}")
        for warning in result["warnings"]:
            print(f"- {warning}")
    if result.get("errors"):
        print(f"errors={len(result['errors'])}")
        for error in result["errors"]:
            print(f"- {error}")


def run_self_test(json_mode: bool = False) -> int:
    gold = validate_path(GOLD_FIXTURES[0])
    bad_results = [validate_path(path) for path in BAD_FIXTURES]
    ok = gold["passed"] and all(not item["passed"] for item in bad_results)

    if json_mode:
        payload = {
            "validator": VALIDATOR_NAME,
            "mode": "self-test",
            "passed": ok,
            "gold_result": gold,
            "bad_results": bad_results,
        }
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print("NO_FAKE_PASS_GATE_SELF_TEST")
        print(f"gold_fixture: {'PASS' if gold['passed'] else 'FAIL'}")
        for bad_result in bad_results:
            print(f"{bad_result['input']}: {'FAIL' if not bad_result['passed'] else 'PASS'}")
        print("NO_FAKE_PASS_GATE_SUMMARY")
        print("gold_expected=PASS")
        print("bad_expected=FAIL")
        print(f"validation_result={'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if args.input is None and args.path is None:
        return run_self_test(json_mode=args.json)

    try:
        input_path = resolve_input_path(args)
    except ValueError as error:
        print(str(error), file=sys.stderr)
        return 2

    if input_path is None:
        return run_self_test(json_mode=args.json)

    if not input_path.exists():
        print(f"input_not_found: {input_path}", file=sys.stderr)
        return 2

    result = validate_path(input_path)
    if args.strict and result["warnings"]:
        result["passed"] = False
        result["errors"] = list(result["errors"]) + ["strict_mode_warning_blocker"]

    emit_result(result, args.json)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
