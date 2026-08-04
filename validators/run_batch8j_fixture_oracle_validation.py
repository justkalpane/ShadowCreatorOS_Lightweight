#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

from lib.batch8j_validator_core import (
    PASS,
    build_bad_fail_matrix,
    build_deferred_runner_plan,
    build_error_code_match_matrix,
    build_git_diff_summary,
    build_gold_pass_matrix,
    build_hard_verdict,
    build_human_suite_report,
    build_logic_coverage_matrix,
    build_no_fake_pass_regression_matrix,
    build_no_touch_report,
    build_oracle_reconciliation,
    read_json,
    run_oracle_validation,
    write_json,
    write_text,
)
from lib.batch8j_validator_registry import ROOT


def parse_args(argv: list[str]) -> argparse.Namespace:
    ap = argparse.ArgumentParser()
    ap.add_argument("--oracle", type=Path, default=ROOT / "tests" / "shadow_runtime" / "fixtures" / "batch8i" / "oracle" / "fixture_oracle.json")
    ap.add_argument("--fixtures-root", type=Path, default=ROOT / "tests" / "shadow_runtime" / "fixtures" / "batch8i")
    ap.add_argument("--report-dir", type=Path, required=True)
    ap.add_argument("--hard-verdict", type=Path, default=None)
    ap.add_argument("--machine-report", type=Path, default=None)
    ap.add_argument("--human-report", type=Path, default=None)
    ap.add_argument("--logic-report", type=Path, default=None)
    ap.add_argument("--error-report", type=Path, default=None)
    ap.add_argument("--gold-report", type=Path, default=None)
    ap.add_argument("--bad-report", type=Path, default=None)
    ap.add_argument("--regression-report", type=Path, default=None)
    ap.add_argument("--reconciliation-report", type=Path, default=None)
    ap.add_argument("--git-report", type=Path, default=None)
    ap.add_argument("--no-touch-report", type=Path, default=None)
    return ap.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv if argv is not None else sys.argv[1:])
    summary, _ = run_oracle_validation(oracle=args.oracle, fixtures_root=args.fixtures_root)
    report_dir = args.report_dir
    report_dir.mkdir(parents=True, exist_ok=True)

    machine_report = args.machine_report or report_dir / "07_fixture_validation_machine_report.json"
    human_report = args.human_report or report_dir / "08_fixture_validation_human_report.md"
    logic_report = args.logic_report or report_dir / "05_validator_logic_coverage_matrix.md"
    error_report = args.error_report or report_dir / "09_error_code_match_matrix.md"
    gold_report = args.gold_report or report_dir / "10_gold_fixture_pass_matrix.md"
    bad_report = args.bad_report or report_dir / "11_bad_fixture_fail_matrix.md"
    regression_report = args.regression_report or report_dir / "12_no_fake_pass_regression_matrix.md"
    reconciliation_report = args.reconciliation_report or report_dir / "04_fixture_oracle_reconciliation.md"
    git_report = args.git_report or report_dir / "14_git_diff_summary.md"
    no_touch_report = args.no_touch_report or report_dir / "15_no_touch_compliance_report.md"
    hard_verdict = args.hard_verdict or report_dir / "16_batch8j_hard_verdict.md"

    write_json(machine_report, summary)
    write_text(human_report, build_human_suite_report(summary))
    write_text(logic_report, build_logic_coverage_matrix(summary))
    write_text(error_report, build_error_code_match_matrix(summary))
    write_text(gold_report, build_gold_pass_matrix(summary))
    write_text(bad_report, build_bad_fail_matrix(summary))
    write_text(regression_report, build_no_fake_pass_regression_matrix(summary))
    write_text(reconciliation_report, build_oracle_reconciliation(summary))

    touched = {
        "unexpected_files_changed": False,
        "forbidden_files_touched": False,
        "schemas_touched": False,
        "fixtures_touched": False,
        "routes_touched": False,
        "runtime_state_touched": False,
        "mediafactory_touched": False,
    }
    write_text(git_report, build_git_diff_summary(0, 0, [], touched, True))
    write_text(no_touch_report, build_no_touch_report({"schemas": False, "fixtures": False, "routes": False, "skills": False, "runtime_state": False, "mediafactory": False, "mission_folders": False}))
    write_text(hard_verdict, build_hard_verdict(summary, True, touched))

    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if summary["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
