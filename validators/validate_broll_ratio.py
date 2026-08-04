#!/usr/bin/env python3
from __future__ import annotations

import math
import sys
from pathlib import Path


def parse(path: Path) -> tuple[int, int, int]:
    data = {}
    for line in path.read_text().splitlines():
        if "=" in line:
            k, v = line.split("=", 1)
            key = k.strip()
            value = v.strip()
            if key in {"total_runtime_seconds", "cinematic_broll_seconds", "required_cinematic_broll_seconds"}:
                data[key] = int(value)
    return data["total_runtime_seconds"], data["cinematic_broll_seconds"], data["required_cinematic_broll_seconds"]


def check(path: Path) -> bool:
    total, broll, required = parse(path)
    return broll >= required and required == math.ceil(total * 0.12)


def validate_paths(paths: list[Path]) -> int:
    ok = True
    for path in paths:
        try:
            total, broll, required = parse(path)
            passed = broll >= required and required == math.ceil(total * 0.12)
            print("BROLL_RATIO_RESULT")
            print(f"fixture={path}")
            print(f"result={'PASS' if passed else 'FAIL'}")
            print(f"total_runtime_seconds={total}")
            print(f"cinematic_broll_seconds={broll}")
            print(f"required_cinematic_broll_seconds={required}")
            print(f"computed_required_seconds={math.ceil(total * 0.12)}")
        except Exception as exc:
            passed = False
            print("BROLL_RATIO_RESULT")
            print(f"fixture={path}")
            print("result=FAIL")
            print(f"error={exc}")
        ok = ok and passed
    print("BROLL_RATIO_SUMMARY")
    print(f"files_checked={len(paths)}")
    print(f"validation_result={'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def self_test() -> int:
    good = Path("validators/fixtures/gold/broll_ratio_good_13_1.md")
    bad = Path("validators/fixtures/bad/broll_ratio_bad_5_2.md")
    good_total, good_broll, good_required = parse(good)
    bad_total, bad_broll, bad_required = parse(bad)
    print(f"good_fixture: {'PASS' if check(good) else 'FAIL'}")
    print(f"good_math: total={good_total} broll={good_broll} required={good_required}")
    print(f"bad_fixture: {'FAIL' if not check(bad) else 'PASS'}")
    print(f"bad_math: total={bad_total} broll={bad_broll} required={bad_required}")
    return 0 if check(good) and not check(bad) else 1


def main(argv: list[str]) -> int:
    if argv:
        return validate_paths([Path(arg) for arg in argv])
    return self_test()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
