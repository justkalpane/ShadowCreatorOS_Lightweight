#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from lib.batch3_validator_configs import validate_pilot_cut_gate
from lib.batch3_validator_core import load_data

VALIDATOR_NAME = "validate_pilot_cut_gate"
GOLD_FIXTURES = [
    Path("validators/fixtures/gold/pilot_c04a_valid.json"),
    Path("validators/fixtures/gold/pilot_cut_c04a_valid.json"),
]
BAD_FIXTURES = [
    Path("validators/fixtures/bad/pilot_wrong_cut_id.json"),
    Path("validators/fixtures/bad/full_render_before_pilot.json"),
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
        validate_pilot_cut_gate(data, errors, warnings)

    passed = not errors and not warnings
    result = {
        "validator": VALIDATOR_NAME,
        "input": str(path),
        "passed": passed,
        "errors": errors,
        "warnings": warnings,
        "pilot_cut_id": data.get("pilot_cut_id") if isinstance(data, dict) else None,
        "pilot_verdict": "PASS" if passed else "FAIL",
        "full_render_unlock_state": "LOCKED" if not (isinstance(data, dict) and data.get("full_render_unlock_allowed")) else "UNLOCKED",
        "source_vs_render_frame_points": data.get("source_vs_render_frame_points", []) if isinstance(data, dict) else [],
        "human_review_status": data.get("human_review_packet", {}).get("review_status") if isinstance(data, dict) else None,
    }
    return result


def emit_result(result: dict, json_mode: bool) -> None:
    if json_mode:
        print(json.dumps(result, indent=2, sort_keys=True))
        return

    print("PILOT_CUT_GATE_RESULT")
    print(f"validator={result['validator']}")
    print(f"input={result['input']}")
    print(f"status={'PASS' if result['passed'] else 'FAIL'}")
    print(f"pilot_cut_id={result.get('pilot_cut_id') or 'missing'}")
    print(f"pilot_verdict={result.get('pilot_verdict')}")
    print(f"full_render_unlock_state={result.get('full_render_unlock_state')}")
    print(f"source_vs_render_frame_points={len(result.get('source_vs_render_frame_points', []))}")
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
        print("PILOT_CUT_GATE_SELF_TEST")
        for gold_result in gold_results:
            print(f"{gold_result['input']}: {'PASS' if gold_result['passed'] else 'FAIL'}")
        for bad_result in bad_results:
            print(f"{bad_result['input']}: {'FAIL' if not bad_result['passed'] else 'PASS'}")
        print("PILOT_CUT_GATE_SUMMARY")
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
