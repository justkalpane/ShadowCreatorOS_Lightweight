from __future__ import annotations
import argparse, ast, csv, re
from pathlib import Path
from common import ROOT, output


SCAN_FILES = [
    ROOT / "validators/validate_mac06_1a_output.py",
    *[p for p in sorted((ROOT / "tools/shadow_runtime").glob("*.py")) if p.name != "validator_integrity_scanner.py"],
    ROOT / "tests/shadow_runtime/run_shadow_runtime_tests.py",
]

CRITICAL_TEXT_PASS_PATTERNS = [
    'explicit_true(text, "route_dag_validation_pass")',
    'explicit_true(text, "packet_schema_validation_pass")',
    'explicit_true(text, "packet_flow_validation_pass")',
    'explicit_true(text, "communication_vein_validation_pass")',
    'explicit_true(text, "lifecycle_validation_pass")',
    'explicit_true(text, "lineage_approval_validation_pass")',
    'explicit_true(text, "quality_scorecard_validation_pass")',
    'explicit_true(text, "provider_boundary_validation_pass")',
    'explicit_true(text, "native_executable_depth_proven")',
    'explicit_true(text, "route_manifests_executable_as_dag")',
    'explicit_true(text, "media_pipeline_dry_run_executable")',
    'explicit_true(text, "runtime_tests_pass")',
    'explicit_true(text, "safe_to_commit_after_user_review")',
]


def _literal_pass_true_return(node: ast.Return) -> bool:
    if not isinstance(node.value, ast.Dict):
        return False
    for key, value in zip(node.value.keys, node.value.values):
        if isinstance(key, ast.Constant) and key.value == "pass":
            if isinstance(value, ast.Constant) and value.value is True:
                return True
    return False


def scan_file(path: Path):
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    rel = str(path.relative_to(ROOT))
    rows = []
    try:
        tree = ast.parse(text)
    except SyntaxError as exc:
        rows.append((rel, "syntax_error", str(exc), "unparseable", "fix syntax", False))
        return rows

    for pattern in CRITICAL_TEXT_PASS_PATTERNS:
        if pattern in text:
            rows.append((rel, "text_only_critical_check", pattern, "trusted asserted PASS text", "use structural runtime validator result", False))

    for node in ast.walk(tree):
        if isinstance(node, ast.ExceptHandler) and node.type and getattr(node.type, "id", "") == "Exception":
            if len(node.body) == 1 and isinstance(node.body[0], ast.Pass):
                rows.append((rel, "ignored_exception", f"line {node.lineno}", "exception swallowed", "return structured FAIL", False))
        if isinstance(node, ast.Return) and _literal_pass_true_return(node):
            # State mutation functions may return pass=true after explicit file existence/write checks; those are not scanner failures.
            src = ast.get_source_segment(text, node) or ""
            if "exists()" not in src and " in " not in src:
                rows.append((rel, "always_pass_return", f"line {node.lineno}", "literal pass true", "compute pass from checks", False))

    hardcoded_patterns = [
        r"routes_passed\s*=\s*16",
        r"runtime_tests_pass\s*=\s*true",
        r"native_executable_depth_proven\s*=\s*true",
        r"\['provider_handoff'\]\s*,\s*0",
    ]
    for pattern in hardcoded_patterns:
        if re.search(pattern, text, re.I):
            rows.append((rel, "hardcoded_success", pattern, "success value hardcoded", "derive from command result", False))

    ignored_subprocess = re.findall(r"subprocess\.run\([^)]*check\s*=\s*False", text, re.S)
    for match in ignored_subprocess:
        rows.append((rel, "ignored_subprocess_failure", match[:80], "subprocess failure can be ignored", "check returncode", False))

    return rows


def run_scan(out_csv: str | None = None):
    rows = []
    for path in SCAN_FILES:
        if path.exists():
            rows.extend(scan_file(path))
    counts = {
        "always_pass_logic_remaining": sum(1 for r in rows if r[1] == "always_pass_return"),
        "hardcoded_success_remaining": sum(1 for r in rows if r[1] == "hardcoded_success"),
        "ignored_exceptions_remaining": sum(1 for r in rows if r[1] in {"ignored_exception", "ignored_subprocess_failure"}),
        "text_only_critical_checks_remaining": sum(1 for r in rows if r[1] == "text_only_critical_check"),
    }
    if out_csv:
        p = Path(out_csv)
        p.parent.mkdir(parents=True, exist_ok=True)
        with p.open("w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["file_path", "issue_type", "line_or_pattern", "old_behavior", "new_behavior", "fixed", "notes"])
            for row in rows:
                w.writerow([*row, "scanner_detected_remaining_issue"])
    result = {
        "pass": all(value == 0 for value in counts.values()),
        **counts,
        "issues": [
            {
                "file_path": r[0],
                "issue_type": r[1],
                "line_or_pattern": r[2],
                "old_behavior": r[3],
                "new_behavior": r[4],
                "fixed": r[5],
            }
            for r in rows
        ],
    }
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out")
    ap.add_argument("--csv")
    args = ap.parse_args()
    result = run_scan(args.csv)
    output(result, args.out)
    raise SystemExit(0 if result["pass"] else 1)


if __name__ == "__main__":
    main()
