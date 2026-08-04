#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


BAD_CURRENT_FIXTURE = Path("validators/fixtures/bad/bad_current_freshness_without_urls.md")
BAD_WEB_FIXTURE = Path("validators/fixtures/bad/bad_web_used_without_source_evidence.md")
GOLD_FIXTURE = Path("validators/fixtures/gold/gold_current_freshness_with_urls.md")

URL_RE = re.compile(r"https?://[^\s)>\"]+")


@dataclass
class ValidationResult:
    path: Path
    passed: bool
    errors: list[str]
    warnings: list[str]
    url_count: int


def parse_kv(text: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or "=" not in line:
            continue
        key, value = line.split("=", 1)
        data[key.strip()] = value.strip()
    return data


def is_true(value: str | None) -> bool:
    return (value or "").strip().lower() in {"true", "yes", "1", "pass"}


def is_false(value: str | None) -> bool:
    return (value or "").strip().lower() in {"false", "no", "0", "fail"}


def int_value(value: str | None) -> int:
    if value is None or value == "":
        return 0
    try:
        return int(value)
    except ValueError:
        return 0


def pass_claimed(data: dict[str, str]) -> bool:
    return (
        data.get("status", "").upper() == "PASS"
        or data.get("final_status", "").upper() == "PASS"
        or data.get("source_research_lock", "").upper() == "PASS"
    )


def validate(path: Path) -> ValidationResult:
    text = path.read_text(encoding="utf-8")
    data = parse_kv(text)
    urls = URL_RE.findall(text)
    url_count = len(urls)
    errors: list[str] = []
    warnings: list[str] = []

    claimed_pass = pass_claimed(data)
    web_used = is_true(data.get("web_used"))
    current_claim = data.get("freshness_class", "").upper() == "CURRENT"
    realtime_sources = is_true(data.get("real_time_sources_used"))
    claimed_url_count = int_value(data.get("source_ledger_urls_count"))
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
    ok = (not bad_current.passed) and (not bad_web.passed) and gold.passed

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

    print("SOURCE_FRESHNESS_URL_LEDGER_SUMMARY")
    print("bad_current_expected=FAIL")
    print("bad_web_expected=FAIL")
    print("gold_expected=PASS")
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
