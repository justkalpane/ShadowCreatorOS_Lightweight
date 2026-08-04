#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

from lib.claim_normalizer import count_urls, has_pass_claim, parse_claims, truncation_markers


BAD_FIXTURE = Path("validators/fixtures/bad/bad_antigravity_truncated_export_pass_claims.md")
GOLD_FIXTURE = Path("validators/fixtures/gold/gold_tool_ledger_with_concrete_file_reads.md")

ACTION_MARKERS = [
    "view_file",
    "read_file",
    "open_file",
    "grep_search",
    "run_command",
    "list_dir",
    "rg ",
    "sed ",
    "cat ",
]

ROUTE_CONSUMPTION_MARKERS = [
    "repo consumption",
    "route consumption",
    "route_scope_file_audit",
    "files_read",
    "mandatory_files_read",
    "total_route_scope_files_read",
    "selected_route_slice_read",
    "route_manifest_read",
]

ZERO_LOSS_MARKERS = [
    "zero-loss",
    "zero loss",
    "complete forensic",
    "full transcript",
    "export complete",
]

PATH_RE = re.compile(r"(?:^|[\\s`\"(])((?:[A-Za-z0-9_.-]+/)+(?:[A-Za-z0-9_.-]+))(?:$|[\\s`\"),])")
ROUTE_MANIFEST_RE = re.compile(r"registries/route_manifests/[A-Za-z0-9_.-]+\.ya?ml")
ROUTE_SLICE_RE = re.compile(r"registries/route_slices/[A-Za-z0-9_.-]+\.registry_slice\.ya?ml")


@dataclass
class ValidationResult:
    path: Path
    passed: bool
    errors: list[str]
    truncation_count: int
    concrete_file_paths: int
    route_manifest_paths: int
    route_slice_paths: int
    action_markers: int
    url_count: int


def marker_count(text: str, markers: list[str]) -> int:
    lowered = text.lower()
    return sum(lowered.count(marker.lower()) for marker in markers)


def concrete_file_paths(text: str) -> list[str]:
    paths = []
    for match in PATH_RE.findall(text):
        if "/" in match and not match.startswith("http"):
            paths.append(match)
    return paths


def claims_zero_loss(text: str) -> bool:
    lowered = text.lower()
    return any(marker in lowered for marker in ZERO_LOSS_MARKERS)


def claims_route_consumption(text: str, claims: dict[str, list[str]]) -> bool:
    lowered = text.lower()
    if any(marker in lowered for marker in ROUTE_CONSUMPTION_MARKERS):
        return True
    return any(key in claims for key in ["route_manifest_read", "selected_route_slice_read", "mandatory_files_read"])


def validate(path: Path) -> ValidationResult:
    text = path.read_text(encoding="utf-8")
    claims = parse_claims(text)
    errors: list[str] = []

    truncations = truncation_markers(text)
    file_paths = concrete_file_paths(text)
    route_manifests = ROUTE_MANIFEST_RE.findall(text)
    route_slices = ROUTE_SLICE_RE.findall(text)
    actions = marker_count(text, ACTION_MARKERS)
    urls = count_urls(text)

    pass_claimed = has_pass_claim(claims) or claims_zero_loss(text)
    route_consumption_claimed = claims_route_consumption(text, claims)

    if pass_claimed and claims_zero_loss(text) and truncations:
        errors.append("zero_loss_or_full_proof_claim_contains_truncation_markers")

    if route_consumption_claimed and not file_paths:
        errors.append("route_consumption_claim_without_concrete_file_paths")

    if "route_manifest_read" in claims and not route_manifests:
        errors.append("route_manifest_read_claim_without_route_manifest_path")

    if "selected_route_slice_read" in claims and not route_slices:
        errors.append("selected_route_slice_read_claim_without_route_slice_path")

    if ("tool ledger" in text.lower() or route_consumption_claimed) and actions == 0:
        errors.append("tool_or_route_ledger_claim_without_action_markers")

    return ValidationResult(
        path=path,
        passed=not errors,
        errors=errors,
        truncation_count=len(truncations),
        concrete_file_paths=len(file_paths),
        route_manifest_paths=len(route_manifests),
        route_slice_paths=len(route_slices),
        action_markers=actions,
        url_count=urls,
    )


def print_result(result: ValidationResult) -> None:
    print("TOOL_LEDGER_EVIDENCE_RESULT")
    print(f"fixture={result.path}")
    print(f"result={'PASS' if result.passed else 'FAIL'}")
    print(f"truncation_markers={result.truncation_count}")
    print(f"concrete_file_paths={result.concrete_file_paths}")
    print(f"route_manifest_paths={result.route_manifest_paths}")
    print(f"route_slice_paths={result.route_slice_paths}")
    print(f"action_markers={result.action_markers}")
    print(f"url_count={result.url_count}")
    print(f"errors={len(result.errors)}")
    for error in result.errors:
        print(f"- {error}")


def self_test() -> int:
    bad = validate(BAD_FIXTURE)
    gold = validate(GOLD_FIXTURE)
    ok = (not bad.passed) and gold.passed
    print("TOOL_LEDGER_EVIDENCE_SELF_TEST")
    print(f"bad_fixture_expected=FAIL actual={'PASS' if bad.passed else 'FAIL'}")
    if bad.passed:
        print_result(bad)
    print(f"gold_fixture_expected=PASS actual={'PASS' if gold.passed else 'FAIL'}")
    if not gold.passed:
        print_result(gold)
    print(f"validation_result={'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    if not argv:
        return self_test()
    ok = True
    for arg in argv:
        try:
            result = validate(Path(arg))
        except Exception as exc:  # noqa: BLE001 - CLI validator must surface internal parser errors.
            print("TOOL_LEDGER_EVIDENCE_RESULT")
            print(f"fixture={arg}")
            print("result=FAIL")
            print("errors=1")
            print(f"- validator_internal_error:{exc}")
            ok = False
            continue
        print_result(result)
        ok = ok and result.passed
    print("TOOL_LEDGER_EVIDENCE_SUMMARY")
    print(f"files_checked={len(argv)}")
    print(f"validation_result={'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
