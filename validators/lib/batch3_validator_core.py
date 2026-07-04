#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from lib.claim_normalizer import parse_claims
from lib.error_catalog import format_error


def load_data(path: Path):
    text = path.read_text(encoding="utf-8")
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {key: values[-1] for key, values in parse_claims(text).items() if values}


def get_in(data, dotted: str, default=None):
    cur = data
    for part in dotted.split("."):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        else:
            return default
    return cur


def is_nonempty(value) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict, tuple, set)):
        return len(value) > 0
    return True


def err(errors: list[str], code: str, detail: str = ""):
    errors.append(format_error(code, detail))


def require_fields(data, errors: list[str], fields: list[str]):
    for field in fields:
        if not is_nonempty(get_in(data, field)):
            err(errors, "missing_required_field", field)


def expect_const(data, errors: list[str], field: str, value):
    actual = get_in(data, field)
    if actual != value:
        err(errors, "const_mismatch", f"{field} expected={value!r} actual={actual!r}")


def expect_enum(data, errors: list[str], field: str, values: list):
    actual = get_in(data, field)
    if actual not in values:
        err(errors, "enum_mismatch", f"{field} actual={actual!r}")


def expect_pattern(data, errors: list[str], field: str, pattern: str):
    actual = get_in(data, field)
    if not isinstance(actual, str) or not re.match(pattern, actual):
        err(errors, "pattern_mismatch", field)


def expect_bool(data, errors: list[str], field: str):
    actual = get_in(data, field)
    if not isinstance(actual, bool):
        err(errors, "boolean_required", field)


def expect_number_range(data, errors: list[str], field: str, minimum=None, maximum=None):
    actual = get_in(data, field)
    if not isinstance(actual, (int, float)):
        err(errors, "number_required", field)
        return
    if minimum is not None and actual < minimum:
        err(errors, "number_below_minimum", field)
    if maximum is not None and actual > maximum:
        err(errors, "number_above_maximum", field)


def expect_array_min(data, errors: list[str], field: str, minimum: int):
    actual = get_in(data, field)
    if not isinstance(actual, list) or len(actual) < minimum:
        err(errors, "array_too_small", field)


def execute_from_config(config: dict) -> int:
    def validate_path(path: Path):
        data = load_data(path)
        errors = []
        warnings = []
        config["validate"](data, errors, warnings)
        return data, errors, warnings

    if len(sys.argv) > 1:
        target = Path(sys.argv[1])
        _, errors, warnings = validate_path(target)
        print(f"fixture={target}")
        print(f"result={'PASS' if not errors else 'FAIL'}")
        print(f"errors={len(errors)}")
        for item in errors:
            print(f"- {item}")
        if warnings:
            print(f"warnings={len(warnings)}")
            for item in warnings:
                print(f"- {item}")
        return 0 if not errors else 1

    print(f"{config['banner']}_SELF_TEST")
    ok = True
    for label, path in config["bad_fixtures"]:
        _, errors, _ = validate_path(Path(path))
        passed = bool(errors)
        print(f"{label}: {'FAIL' if passed else 'PASS'}")
        ok = ok and passed
    for label, path in config["gold_fixtures"]:
        _, errors, _ = validate_path(Path(path))
        passed = not errors
        print(f"{label}: {'PASS' if passed else 'FAIL'}")
        ok = ok and passed
    print(f"validation_result={'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1
