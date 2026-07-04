#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from lib.batch3_validator_configs import validate_davinci_handoff_gate
from lib.batch3_validator_core import load_data

VALIDATOR_NAME = "validate_davinci_handoff_gate"
GOLD_FIXTURES = [
    Path("validators/fixtures/gold/davinci_handoff_valid.json"),
    Path("validators/fixtures/gold/davinci_handoff_authorized.json"),
]
BAD_FIXTURES = [
    Path("validators/fixtures/bad/davinci_before_acceptance.json"),
    Path("validators/fixtures/bad/davinci_before_visual_audio_package.json"),
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


def validate_path(path: Path) -> dict:
    data = load_data(path)
    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(data, dict):
        errors.append("input_not_object")
        data = {}
    else:
        validate_davinci_handoff_gate(data, errors, warnings)

    passed = not errors and not warnings
    visual_acceptance_token = data.get("visual_acceptance_token", {}) if isinstance(data, dict) else {}
    davinci_handoff_token = data.get("davinci_handoff_token", {}) if isinstance(data, dict) else {}
    result = {
        "validator": VALIDATOR_NAME,
        "input": str(path),
        "passed": passed,
        "errors": errors,
        "warnings": warnings,
        "visual_acceptance_status": visual_acceptance_token.get("status"),
        "audio_status": "accepted" if data.get("visual_audio_package_status") == "ready" else "blocked",
        "davinci_handoff_status": davinci_handoff_token.get("status"),
        "davinci_authorization_packet": {
            "visual_master_reference": visual_acceptance_token.get("proof_bundle_id"),
            "audio_package_reference": data.get("visual_audio_package_status"),
            "asset_registry_reference": data.get("asset_registry_path"),
            "davinci_token_reference": davinci_handoff_token.get("proof_bundle_id"),
        },
    }
    return result


def emit_result(result: dict, json_mode: bool) -> None:
    if json_mode:
        print(json.dumps(result, indent=2, sort_keys=True))
        return

    print("DAVINCI_HANDOFF_GATE_RESULT")
    print(f"validator={result['validator']}")
    print(f"input={result['input']}")
    print(f"status={'PASS' if result['passed'] else 'FAIL'}")
    print(f"visual_acceptance_status={result.get('visual_acceptance_status') or 'missing'}")
    print(f"davinci_handoff_status={result.get('davinci_handoff_status') or 'missing'}")
    print(f"audio_status={result.get('audio_status') or 'missing'}")
    if result.get("warnings"):
        print(f"warnings={len(result['warnings'])}")
        for warning in result["warnings"]:
            print(f"- {warning}")
    if result.get("errors"):
        print(f"errors={len(result['errors'])}")
        for error in result["errors"]:
            print(f"- {error}")


def run_self_test(json_mode: bool = False) -> int:
    gold_results = [validate_path(path) for path in GOLD_FIXTURES]
    bad_results = [validate_path(path) for path in BAD_FIXTURES]
    ok = all(result["passed"] for result in gold_results) and all(not result["passed"] for result in bad_results)

    if json_mode:
        payload = {
            "validator": VALIDATOR_NAME,
            "mode": "self-test",
            "passed": ok,
            "gold_results": gold_results,
            "bad_results": bad_results,
        }
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print("DAVINCI_HANDOFF_GATE_SELF_TEST")
        for gold_result in gold_results:
            print(f"{gold_result['input']}: {'PASS' if gold_result['passed'] else 'FAIL'}")
        for bad_result in bad_results:
            print(f"{bad_result['input']}: {'FAIL' if not bad_result['passed'] else 'PASS'}")
        print("DAVINCI_HANDOFF_GATE_SUMMARY")
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
