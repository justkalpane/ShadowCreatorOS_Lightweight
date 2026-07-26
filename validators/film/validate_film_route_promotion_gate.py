#!/usr/bin/env python3
"""Promotion gate checker for the film route.

This checker is intentionally unbound. It only reads repository files and
reports whether the inactive film route drafts are ready for a later owner
decision about promotion.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


READY = "PROMOTION_GATE_READY_FOR_OWNER_DECISION"
BLOCKED_MISSING_DRAFT = "PROMOTION_GATE_BLOCKED_MISSING_DRAFT"
BLOCKED_PARSE_ERROR = "PROMOTION_GATE_BLOCKED_PARSE_ERROR"
BLOCKED_ACTIVE_FILE_ALREADY_EXISTS = "PROMOTION_GATE_BLOCKED_ACTIVE_FILE_ALREADY_EXISTS"
BLOCKED_SELECTOR_ALREADY_REFERENCES_FILM_ROUTE = (
    "PROMOTION_GATE_BLOCKED_SELECTOR_ALREADY_REFERENCES_FILM_ROUTE"
)
BLOCKED_MISSING_REQUIRED_MARKER = "PROMOTION_GATE_BLOCKED_MISSING_REQUIRED_MARKER"
BLOCKED_RUNTIME_PROOF_CLAIM = "PROMOTION_GATE_BLOCKED_RUNTIME_PROOF_CLAIM"
BLOCKED_MISSING_PREP_ARTIFACT = "PROMOTION_GATE_BLOCKED_MISSING_PREP_ARTIFACT"

REQUIRED_PREP_ARTIFACTS = [
    "tests/fixtures/phase_12a_fixture_manifest.json",
    "schemas/film/phase_12b_schema_manifest.json",
    "validators/film/phase_12c_validator_manifest.json",
    "PHASE_12L_B_ACTIVE_REGISTRY_INERTNESS_AUDIT.md",
    "PHASE_12L_C_PROMOTION_PREFLIGHT_GATE.md",
]

FORBIDDEN_RUNTIME_PROOF_TOKENS = [
    "repository_lock_id",
    "proof_contract_id",
    "context_packet_id",
    "prompt_package_id",
    "evaluation_report_id",
    "completion_certificate",
]

FUTURE_ACTIVE_FILES = [
    "registries/route_manifests/film_screenplay_generation.yaml",
    "registries/route_slices/film_screenplay_generation.registry_slice.yaml",
]

CONTENT_ROUTE_SURFACES = [
    "registries/route_manifests/script_generation.yaml",
    "registries/route_slices/script_generation.registry_slice.yaml",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if not value:
        return ""
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    if value.lower() == "null":
        return None
    if re.fullmatch(r"-?\d+", value):
        try:
            return int(value)
        except ValueError:
            return value
    return value


def skip_blank_and_comment(lines: list[str], idx: int) -> int:
    while idx < len(lines):
        stripped = lines[idx].strip()
        if stripped and not stripped.startswith("#"):
            return idx
        idx += 1
    return idx


def line_indent(line: str) -> int:
    if "\t" in line:
        raise ValueError("Tabs are not allowed in the YAML subset parser")
    return len(line) - len(line.lstrip(" "))


def parse_block(lines: list[str], idx: int, indent: int) -> tuple[Any, int]:
    idx = skip_blank_and_comment(lines, idx)
    if idx >= len(lines):
        return {}, idx

    first_indent = line_indent(lines[idx])
    if first_indent < indent:
        return {}, idx
    if first_indent > indent:
        raise ValueError(f"Unexpected indentation at line {idx + 1}")

    content = lines[idx][indent:]
    if content.startswith("- "):
        items: list[Any] = []
        while idx < len(lines):
            idx = skip_blank_and_comment(lines, idx)
            if idx >= len(lines):
                break
            current_indent = line_indent(lines[idx])
            if current_indent < indent:
                break
            if current_indent > indent:
                raise ValueError(f"Unexpected indentation in list at line {idx + 1}")
            entry = lines[idx][indent:]
            if not entry.startswith("- "):
                break
            items.append(parse_scalar(entry[2:].strip()))
            idx += 1
        return items, idx

    mapping: dict[str, Any] = {}
    while idx < len(lines):
        idx = skip_blank_and_comment(lines, idx)
        if idx >= len(lines):
            break
        current_indent = line_indent(lines[idx])
        if current_indent < indent:
            break
        if current_indent > indent:
            raise ValueError(f"Unexpected indentation in mapping at line {idx + 1}")

        entry = lines[idx][indent:]
        if entry.startswith("- "):
            break
        if ":" not in entry:
            raise ValueError(f"Invalid mapping entry at line {idx + 1}")

        key, raw_value = entry.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()
        if not key:
            raise ValueError(f"Empty key at line {idx + 1}")

        if raw_value:
            mapping[key] = parse_scalar(raw_value)
            idx += 1
            continue

        child, child_end = parse_block(lines, idx + 1, indent + 2)
        mapping[key] = child
        idx = max(child_end, idx + 1)

    return mapping, idx


def load_yaml_subset(path: Path) -> dict[str, Any]:
    text = read_text(path)
    lines = text.splitlines()
    parsed, _ = parse_block(lines, 0, 0)
    if not isinstance(parsed, dict):
        raise ValueError(f"Top-level YAML document in {path} is not a mapping")
    return parsed


def check_required_markers(document: dict[str, Any], required: dict[str, Any]) -> list[str]:
    missing: list[str] = []
    for key, expected in required.items():
        actual = document.get(key)
        if actual != expected:
            missing.append(f"{key}={expected!r}")
    return missing


def build_report(status: str, details: list[str], repo_root: Path) -> str:
    lines = [
        "PROMOTION_GATE_CHECKER_REPORT",
        f"status={status}",
        f"repo_root={repo_root}",
        f"checker=validators/film/validate_film_route_promotion_gate.py",
    ]
    if details:
        lines.append("details:")
        lines.extend(f"- {item}" for item in details)
    return "\n".join(lines)


def evaluate(repo_root: Path) -> tuple[str, list[str]]:
    details: list[str] = []

    draft_manifest_path = repo_root / "route_drafts/film_screenplay_generation/film_screenplay_generation.manifest.draft.yaml"
    draft_slice_path = repo_root / "route_drafts/film_screenplay_generation/film_screenplay_generation.registry_slice.draft.yaml"
    draft_json_path = repo_root / "route_drafts/film_screenplay_generation/phase_12h_inactive_route_draft_manifest.json"

    if not draft_manifest_path.is_file() or not draft_slice_path.is_file() or not draft_json_path.is_file():
        missing = [
            str(path.relative_to(repo_root))
            for path in [draft_manifest_path, draft_slice_path, draft_json_path]
            if not path.is_file()
        ]
        return BLOCKED_MISSING_DRAFT, [f"missing_draft_files={','.join(missing)}"]

    active_target_paths = [repo_root / rel for rel in FUTURE_ACTIVE_FILES]
    existing_active = [str(path.relative_to(repo_root)) for path in active_target_paths if path.exists()]
    if existing_active:
        return BLOCKED_ACTIVE_FILE_ALREADY_EXISTS, [f"existing_active_files={','.join(existing_active)}"]

    selector_path = repo_root / "runtime/state/route_chain_mode_selector.yaml"
    selector_text = read_text(selector_path)
    if "FILM_SCREENPLAY_GENERATION" in selector_text:
        return BLOCKED_SELECTOR_ALREADY_REFERENCES_FILM_ROUTE, [str(selector_path.relative_to(repo_root))]

    for rel_path in CONTENT_ROUTE_SURFACES + REQUIRED_PREP_ARTIFACTS:
        if not (repo_root / rel_path).exists():
            return BLOCKED_MISSING_PREP_ARTIFACT, [f"missing_required_artifact={rel_path}"]

    phase_12l_b_audit = repo_root / "PHASE_12L_B_ACTIVE_REGISTRY_INERTNESS_AUDIT.md"
    phase_12l_c_rollback = repo_root / "PHASE_12L_C_PROMOTION_ROLLBACK_AND_OWNER_DECISION.md"
    if "ACTIVE_REGISTRY_AUTO_DISCOVERY_RISK_CONFIRMED" not in read_text(phase_12l_b_audit):
        return BLOCKED_MISSING_PREP_ARTIFACT, [f"missing_required_marker={phase_12l_b_audit.name}:ACTIVE_REGISTRY_AUTO_DISCOVERY_RISK_CONFIRMED"]
    if "Phase 12L-D: build promotion checker/validator only" not in read_text(phase_12l_c_rollback):
        return BLOCKED_MISSING_PREP_ARTIFACT, [
            f"missing_required_marker={phase_12l_c_rollback.name}:Phase 12L-D recommendation"
        ]

    try:
        manifest = load_yaml_subset(draft_manifest_path)
        slice_doc = load_yaml_subset(draft_slice_path)
        json.loads(read_text(draft_json_path))
    except Exception as exc:  # pragma: no cover - conservative blocked path
        return BLOCKED_PARSE_ERROR, [f"parse_error={exc}"]

    manifest_required = {
        "status": "inactive_draft_only",
        "registered": False,
        "bound_to_route_selector": False,
        "runtime_behavior_changed": False,
        "governed_runtime_proof_claimed": False,
        "pass_claimed": False,
        "route_id": "FILM_SCREENPLAY_GENERATION",
        "preserves_content_route": "SCRIPT_GENERATION",
    }
    missing_manifest = check_required_markers(manifest, manifest_required)
    if missing_manifest:
        return BLOCKED_MISSING_REQUIRED_MARKER, [f"manifest_missing={','.join(missing_manifest)}"]

    slice_required = {
        "status": "inactive_draft_only",
        "registered": False,
        "bound_to_route_selector": False,
        "runtime_behavior_changed": False,
        "governed_runtime_proof_claimed": False,
        "pass_claimed": False,
    }
    missing_slice = check_required_markers(slice_doc, slice_required)
    if missing_slice:
        return BLOCKED_MISSING_REQUIRED_MARKER, [f"slice_missing={','.join(missing_slice)}"]

    manifest_text = read_text(draft_manifest_path)
    slice_text = read_text(draft_slice_path)
    for token in FORBIDDEN_RUNTIME_PROOF_TOKENS:
        if token in manifest_text or token in slice_text:
            return BLOCKED_RUNTIME_PROOF_CLAIM, [f"forbidden_token={token}"]

    details.extend(
        [
            f"inactive_manifest={draft_manifest_path.relative_to(repo_root)}",
            f"inactive_slice={draft_slice_path.relative_to(repo_root)}",
            f"draft_manifest_json={draft_json_path.relative_to(repo_root)}",
            "selector_reference_absent=true",
            "active_registry_targets_absent=true",
            "required_prep_artifacts_present=true",
        ]
    )
    return READY, details


def main() -> int:
    parser = argparse.ArgumentParser(description="Check inactive-to-active promotion safety for the film route.")
    parser.add_argument(
        "--repo-root",
        default=None,
        help="Optional repository root. Defaults to the repo containing this script.",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve() if args.repo_root else Path(__file__).resolve().parents[2]
    status, details = evaluate(repo_root)
    print(build_report(status, details, repo_root))
    return 0 if status == READY else 1


if __name__ == "__main__":
    raise SystemExit(main())
