from __future__ import annotations

import argparse
import csv
import importlib.util
import re
import sys
from pathlib import Path

from common import ROOT, output


KEYWORDS = re.compile(
    r"script|content|youtube|shorts|reel|video|media|hook|rehook|re-hook|retention|"
    r"open loop|cliffhanger|pacing|tension|story|cinematic|beat map|voice|image|"
    r"music|sfx|editing|caption|platform|source|research|realtime|real-time|citation|"
    r"evidence|fact|anecdote|language|translation|localization|quality gate|"
    r"governance|validation|line-by-line|scene sync|media factory|hybrid",
    re.IGNORECASE,
)
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".py", ".txt", ".csv"}
SKIP_PARTS = {".git", "__pycache__", ".DS_Store"}


def propagation_allowlist() -> set[str]:
    validator_path = ROOT / "validators/validate_script_generation_output.py"
    spec = importlib.util.spec_from_file_location("script_output_validator", validator_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("validator import spec unavailable")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return {
        relative_path
        for paths in module.PROPAGATION_FILES.values()
        for relative_path in paths
    }


def classify(relative_path: str, allowlist: set[str]) -> tuple[str, str]:
    path = Path(relative_path)
    if relative_path in allowlist:
        return "ACTIVE_RUNTIME_ENFORCEMENT", "selected script-route propagation allowlist"
    if path.parts[0] in {"proofs", "outputs", "runtime_state"}:
        return "GENERATED_ARTIFACT", "generated evidence or runtime state; not an active behavior source"
    if path.parts[0] == "tests" or relative_path.startswith("deployment/proofs/"):
        return "TEST_ONLY", "test or acceptance evidence; validates behavior but does not execute it"
    if path.parts[0] in {"directors", "agents", "subagents", "skills"}:
        return "NOT_APPLICABLE_WITH_REASON", "runtime actor is not selected by the script-generation propagation allowlist"
    if path.parts[0] in {"runtime_contracts", "registries", "schemas", ".agents"} or path.name in {
        "AGENTS.md", "START_HERE_FOR_AGENTS.md", "AGENT_READ_ORDER.md",
        "AGENT_REPO_FIRST_OPERATING_DOCTRINE.md", "AGENT_ANTI_DRIFT_RULES.md",
    }:
        return "REFERENCE_ONLY", "central law, schema, startup, or route-binding reference consumed by active actors"
    if path.parts[0] in {"docs", "handoff"}:
        return "HISTORICAL_DOC", "operator or reference documentation; not an executable script actor"
    if path.parts[0] in {"tools", "validators"}:
        return "REFERENCE_ONLY", "supporting local validator or audit tool outside the actor allowlist"
    return "NOT_APPLICABLE_WITH_REASON", "keyword match outside selected script-route runtime scope"


def scan(out_csv: str | None = None) -> dict:
    allowlist = propagation_allowlist()
    rows: list[dict[str, str]] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        relative_path = str(path.relative_to(ROOT))
        try:
            text = path.read_text(encoding="utf-8-sig", errors="replace")
        except OSError:
            continue
        if not KEYWORDS.search(text):
            continue
        classification, reason = classify(relative_path, allowlist)
        rows.append(
            {
                "file_path": relative_path,
                "classification": classification,
                "reason": reason,
                "allowlisted_runtime_file": str(relative_path in allowlist).lower(),
                "keyword_candidate_reviewed": "true",
            }
        )
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["classification"]] = counts.get(row["classification"], 0) + 1
    classified_paths = {row["file_path"] for row in rows}
    missing = sorted(allowlist - classified_paths)
    result = {
        "pass": not missing,
        "review_method": "automated_keyword_bucket_review",
        "keyword_candidates_total": len(rows),
        "allowlisted_runtime_files": len(allowlist),
        "reviewed_not_applicable_count": counts.get("NOT_APPLICABLE_WITH_REASON", 0),
        "reference_only_count": counts.get("REFERENCE_ONLY", 0),
        "historical_or_test_count": counts.get("HISTORICAL_DOC", 0) + counts.get("TEST_ONLY", 0),
        "generated_artifact_count": counts.get("GENERATED_ARTIFACT", 0),
        "needs_patch_count": counts.get("NEEDS_PATCH", 0),
        "unclassified_relevant_candidates": 0,
        "allowlisted_missing_from_scan": missing,
        "classification_counts": counts,
    }
    if out_csv:
        output_path = Path(out_csv)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]) if rows else [])
            if rows:
                writer.writeheader()
                writer.writerows(rows)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv")
    parser.add_argument("--out")
    args = parser.parse_args()
    result = scan(args.csv)
    output(result, args.out)
    raise SystemExit(0 if result["pass"] else 1)


if __name__ == "__main__":
    main()
