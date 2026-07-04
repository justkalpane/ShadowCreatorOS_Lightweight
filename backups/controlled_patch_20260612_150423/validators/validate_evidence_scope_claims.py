#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

ALLOWED = {"current_cycle", "previous_cycle_with_step_reference", "persisted_route_state_with_hash"}


def parse(path: Path) -> dict[str, str]:
    data = {}
    for line in path.read_text().splitlines():
        if "=" in line:
            k, v = line.split("=", 1)
            data[k.strip()] = v.strip()
    return data


def check(path: Path) -> bool:
    data = parse(path)
    if data.get("status") != "PASS":
        return True
    return (
        data.get("evidence_scope") in ALLOWED
        and bool(data.get("evidence_path"))
        and bool(data.get("command_output_or_file_reference"))
    )


def validate_paths(paths: list[Path]) -> int:
    ok = True
    for path in paths:
        data = parse(path)
        passed = check(path)
        print("EVIDENCE_SCOPE_CLAIM_RESULT")
        print(f"fixture={path}")
        print(f"result={'PASS' if passed else 'FAIL'}")
        print(f"status={data.get('status', 'missing')}")
        print(f"evidence_scope={data.get('evidence_scope', 'missing')}")
        if data.get("status") == "PASS" and not passed:
            if data.get("evidence_scope") not in ALLOWED:
                print("error=PASS_claim_without_allowed_evidence_scope")
            if not data.get("evidence_path"):
                print("error=PASS_claim_missing_evidence_path")
            if not data.get("command_output_or_file_reference"):
                print("error=PASS_claim_missing_command_output_or_file_reference")
        ok = ok and passed
    print("EVIDENCE_SCOPE_CLAIM_SUMMARY")
    print(f"files_checked={len(paths)}")
    print(f"validation_result={'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def self_test() -> int:
    good = Path("validators/fixtures/gold/evidence_scope_good.md")
    current = Path("validators/fixtures/gold/evidence_scope_current_cycle.md")
    bad_memory = Path("validators/fixtures/bad/evidence_scope_bad_memory_only.md")
    bad_scope = Path("validators/fixtures/bad/evidence_scope_bad_no_scope.md")
    ok = check(good) and check(current) and not check(bad_memory) and not check(bad_scope)
    print(f"good_fixture: {'PASS' if check(good) else 'FAIL'}")
    print(f"current_cycle_fixture: {'PASS' if check(current) else 'FAIL'}")
    print(f"bad_memory_only_fixture: {'FAIL' if not check(bad_memory) else 'PASS'}")
    print(f"bad_no_scope_fixture: {'FAIL' if not check(bad_scope) else 'PASS'}")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    if argv:
        return validate_paths([Path(arg) for arg in argv])
    return self_test()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
