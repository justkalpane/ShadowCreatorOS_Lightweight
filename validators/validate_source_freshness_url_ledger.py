#!/usr/bin/env python3
from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

from lib.claim_normalizer import (
    SOURCE_URL_COUNT_KEYS,
    WEB_USED_KEYS,
    all_values,
    count_urls,
    first_value,
    has_pass_claim,
    is_falsey,
    is_truthy,
    parse_claims,
)

BAD_CURRENT_FIXTURE = Path("validators/fixtures/bad/bad_current_freshness_without_urls.md")
BAD_WEB_FIXTURE = Path("validators/fixtures/bad/bad_web_used_without_source_evidence.md")
GOLD_FIXTURE = Path("validators/fixtures/gold/gold_current_freshness_with_urls.md")
BAD_ALIAS_FIXTURE = Path("validators/fixtures/bad/bad_latest_antigravity_alias_fake_pass.md")
GOLD_ALIAS_FIXTURE = Path("validators/fixtures/gold/gold_alias_claims_with_complete_evidence.md")


@dataclass
class ValidationResult:
    path: Path
    passed: bool
    errors: list[str]
    warnings: list[str]
    url_count: int


def parse_kv(text: str) -> dict[str, str]:
    return {key: values[-1] for key, values in parse_claims(text).items() if values}


def is_true(value: str | None) -> bool:
    return is_truthy(value)


def is_false(value: str | None) -> bool:
    return is_falsey(value)


def int_value(value: str | None) -> int:
    if value is None or value == "":
        return 0
    try:
        return int(value)
    except ValueError:
        return 0


def pass_claimed(data: dict[str, str]) -> bool:
    return has_pass_claim({key: [value] for key, value in data.items()})


def validate(path: Path) -> ValidationResult:
    text = path.read_text(encoding="utf-8")
    data = parse_kv(text)
    url_count = count_urls(text)
    errors: list[str] = []
    warnings: list[str] = []

    claimed_pass = pass_claimed(data)
    claims = parse_claims(text)
    web_used = any(is_true(value) for value in all_values(claims, WEB_USED_KEYS))
    current_claim = data.get("freshness_class", "").upper() == "CURRENT"
    realtime_sources = is_true(first_value(claims, ["real_time_sources_used"]))
    claimed_url_count = max([int_value(value) for value in all_values(claims, SOURCE_URL_COUNT_KEYS)] or [0])
    labels_only = data.get("source_list_format", "").lower() == "labels_only"
    command_ref = data.get("command_output_or_file_reference", "").strip()

    if claimed_pass and current_claim and url_count == 0:
        errors.append("freshness_CURRENT_without_exact_url_ledger")

    if claimed_pass and web_used and url_count == 0 and not command_ref:
        errors.append("web_used_without_url_or_command_evidence")

    if claimed_pass and realtime_sources and url_count == 0:
        errors.append("real_time_sources_used_without_url_evidence")

    if claimed_pass and is_false(data.get("exact_url_ledger_present")):
        errors.append("exact_url_ledger_present_false_with_PASS")

    if claimed_pass and labels_only:
        errors.append("source_list_labels_only_with_PASS")

    if claimed_pass and claimed_url_count == 0 and (web_used or current_claim or realtime_sources):
        errors.append("source_ledger_urls_count_zero_with_realtime_or_web_PASS")

    if claimed_url_count > 0 and url_count < claimed_url_count:
        errors.append(f"source_ledger_urls_count_mismatch: claimed={claimed_url_count} actual={url_count}")

    if claimed_pass and "CLAIM_EVIDENCE_STATUS" in text:
        evidence_path = data.get("evidence_path", "").strip()
        if not evidence_path and not command_ref and url_count == 0:
            errors.append("claim_evidence_status_missing_path_command_and_url")

    if not (web_used or current_claim or realtime_sources):
        warnings.append("no_web_or_current_claim_detected")

    return ValidationResult(path=path, passed=not errors, errors=errors, warnings=warnings, url_count=url_count)


def print_result(result: ValidationResult) -> None:
    print(f"fixture={result.path}")
    print(f"result={'PASS' if result.passed else 'FAIL'}")
    print(f"url_count={result.url_count}")
    print(f"errors={len(result.errors)}")
    for error in result.errors:
        print(f"- {error}")
    if result.warnings:
        print(f"warnings={len(result.warnings)}")
        for warning in result.warnings:
            print(f"- {warning}")


def run_self_test() -> int:
    bad_current = validate(BAD_CURRENT_FIXTURE)
    bad_web = validate(BAD_WEB_FIXTURE)
    gold = validate(GOLD_FIXTURE)
    bad_alias = validate(BAD_ALIAS_FIXTURE)
    gold_alias = validate(GOLD_ALIAS_FIXTURE)
    ok = (not bad_current.passed) and (not bad_web.passed) and gold.passed and (not bad_alias.passed) and gold_alias.passed

    print("SOURCE_FRESHNESS_URL_LEDGER_SELF_TEST")
    print(f"bad_current_fixture: {'FAIL' if not bad_current.passed else 'PASS'}")
    if bad_current.passed:
        print_result(bad_current)
    print(f"bad_web_fixture: {'FAIL' if not bad_web.passed else 'PASS'}")
    if bad_web.passed:
        print_result(bad_web)
    print(f"gold_fixture: {'PASS' if gold.passed else 'FAIL'}")
    if not gold.passed:
        print_result(gold)
    print(f"bad_alias_fixture: {'FAIL' if not bad_alias.passed else 'PASS'}")
    if bad_alias.passed:
        print_result(bad_alias)
    print(f"gold_alias_fixture: {'PASS' if gold_alias.passed else 'FAIL'}")
    if not gold_alias.passed:
        print_result(gold_alias)

    print("SOURCE_FRESHNESS_URL_LEDGER_SUMMARY")
    print("bad_current_expected=FAIL")
    print("bad_web_expected=FAIL")
    print("gold_expected=PASS")
    print("bad_alias_expected=FAIL")
    print("gold_alias_expected=PASS")
    print(f"validation_result={'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    if not argv:
        return run_self_test()

    ok = True
    for arg in argv:
        result = validate(Path(arg))
        print("SOURCE_FRESHNESS_URL_LEDGER_RESULT")
        print_result(result)
        if not result.passed:
            ok = False
    print("SOURCE_FRESHNESS_URL_LEDGER_SUMMARY")
    print(f"files_checked={len(argv)}")
    print(f"validation_result={'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
