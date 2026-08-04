#!/usr/bin/env python3
"""Post-binding state checker for the film route.

This checker is intentionally read-only. It verifies repo metadata after the
film route has active registry files and a selector mode. It does not execute
runtime, weaken the pre-promotion checker, or claim PASS.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any


READY = "POST_BINDING_FILM_ROUTE_STATE_READY"
BLOCKED_MISSING_FILE = "POST_BINDING_BLOCKED_MISSING_FILE"
BLOCKED_PARSE_ERROR = "POST_BINDING_BLOCKED_PARSE_ERROR"
BLOCKED_SELECTOR_DEFAULT_MODE_CHANGED = "POST_BINDING_BLOCKED_SELECTOR_DEFAULT_MODE_CHANGED"
BLOCKED_SELECTOR_MISSING_FILM_MODE = "POST_BINDING_BLOCKED_SELECTOR_MISSING_FILM_MODE"
BLOCKED_SELECTOR_ROUTE_ID_MISMATCH = "POST_BINDING_BLOCKED_SELECTOR_ROUTE_ID_MISMATCH"
BLOCKED_MANIFEST_NOT_ACTIVE_REGISTERED = "POST_BINDING_BLOCKED_MANIFEST_NOT_ACTIVE_REGISTERED"
BLOCKED_MANIFEST_NOT_SELECTOR_BOUND = "POST_BINDING_BLOCKED_MANIFEST_NOT_SELECTOR_BOUND"
BLOCKED_SLICE_NOT_ACTIVE_REGISTERED = "POST_BINDING_BLOCKED_SLICE_NOT_ACTIVE_REGISTERED"
BLOCKED_SLICE_NOT_SELECTOR_BOUND = "POST_BINDING_BLOCKED_SLICE_NOT_SELECTOR_BOUND"
BLOCKED_SCRIPT_ROUTE_NOT_PRESERVED = "POST_BINDING_BLOCKED_SCRIPT_ROUTE_NOT_PRESERVED"
BLOCKED_NO_FAKE_PASS_BOUNDARY_MISSING = "POST_BINDING_BLOCKED_NO_FAKE_PASS_BOUNDARY_MISSING"
BLOCKED_RUNTIME_PROOF_CLAIM = "POST_BINDING_BLOCKED_RUNTIME_PROOF_CLAIM"
BLOCKED_DOWNSTREAM_BOUNDARY_MISSING = "POST_BINDING_BLOCKED_DOWNSTREAM_BOUNDARY_MISSING"

ROUTE_ID = "FILM_SCREENPLAY_GENERATION"
SCRIPT_ROUTE_ID = "SCRIPT_GENERATION"

REQUIRED_FILES = [
    "runtime/state/route_chain_mode_selector.yaml",
    "registries/route_manifests/film_screenplay_generation.yaml",
    "registries/route_slices/film_screenplay_generation.registry_slice.yaml",
    "registries/route_manifests/script_generation.yaml",
    "registries/route_slices/script_generation.registry_slice.yaml",
    "PHASE_12L_K_SELECTOR_BINDING_PATCH_REPORT.md",
    "PHASE_13E_29_ACTIVE_FILM_ROUTE_BINDING_METADATA_RECONCILIATION_PATCH_REPORT.md",
]

FORBIDDEN_RUNTIME_PROOF_TOKENS = [
    "repository_lock_id",
    "proof_contract_id",
    "context_packet_id",
    "prompt_package_id",
    "evaluation_report_id",
    "completion_certificate",
]

REQUIRED_DOWNSTREAM_ROUTES = [
    "VISUAL_MEDIA_PLAN",
    "VOICE_CONTEXT",
    "EDITING_PACKAGING",
    "MEDIA_FACTORY_HANDOFF",
    "FULL_VIDEO_PIPELINE",
]

CONTENT_ROUTE_NEGATIVE_TRIGGERS = [
    "YouTube script",
    "Shorts script",
    "Instagram reel script",
    "TikTok script",
    "voiceover script",
    "explainer video script",
    "content script",
    "creator video",
    "hook-focused script",
    "retention-focused script",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if not value:
        return ""
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
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
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [parse_scalar(item.strip()) for item in inner.split(",")]
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
    parsed, _ = parse_block(read_text(path).splitlines(), 0, 0)
    if not isinstance(parsed, dict):
        raise ValueError(f"Top-level YAML document in {path} is not a mapping")
    return parsed


def build_report(status: str, details: list[str], repo_root: Path) -> str:
    lines = [
        "POST_BINDING_FILM_ROUTE_STATE_CHECKER_REPORT",
        f"status={status}",
        f"repo_root={repo_root}",
        "checker=validators/film/validate_film_route_post_binding_state.py",
    ]
    if details:
        lines.append("details:")
        lines.extend(f"- {detail}" for detail in details)
    return "\n".join(lines)


def fail(status: str, detail: str) -> tuple[str, list[str]]:
    return status, [detail]


def evaluate(repo_root: Path) -> tuple[str, list[str]]:
    missing = [rel for rel in REQUIRED_FILES if not (repo_root / rel).is_file()]
    if missing:
        return fail(BLOCKED_MISSING_FILE, f"missing_files={','.join(missing)}")

    selector_path = repo_root / "runtime/state/route_chain_mode_selector.yaml"
    manifest_path = repo_root / "registries/route_manifests/film_screenplay_generation.yaml"
    slice_path = repo_root / "registries/route_slices/film_screenplay_generation.registry_slice.yaml"
    script_manifest_path = repo_root / "registries/route_manifests/script_generation.yaml"
    script_slice_path = repo_root / "registries/route_slices/script_generation.registry_slice.yaml"

    try:
        selector = load_yaml_subset(selector_path)
        manifest = load_yaml_subset(manifest_path)
        route_slice = load_yaml_subset(slice_path)
        script_manifest = load_yaml_subset(script_manifest_path)
        script_slice = load_yaml_subset(script_slice_path)
    except Exception as exc:  # pragma: no cover - conservative blocked path
        return fail(BLOCKED_PARSE_ERROR, f"parse_error={exc}")

    if selector.get("default_mode") != "script_only":
        return fail(
            BLOCKED_SELECTOR_DEFAULT_MODE_CHANGED,
            f"default_mode={selector.get('default_mode')!r}",
        )

    film_mode = selector.get("modes", {}).get("film_screenplay_generation")
    if not isinstance(film_mode, dict):
        return fail(BLOCKED_SELECTOR_MISSING_FILM_MODE, "missing_mode=film_screenplay_generation")
    if film_mode.get("allowed_route_ids") != [ROUTE_ID]:
        return fail(
            BLOCKED_SELECTOR_ROUTE_ID_MISMATCH,
            f"allowed_route_ids={film_mode.get('allowed_route_ids')!r}",
        )

    if not (
        manifest.get("route_id") == ROUTE_ID
        and manifest.get("active_route") is True
        and manifest.get("registered") is True
    ):
        return fail(BLOCKED_MANIFEST_NOT_ACTIVE_REGISTERED, "manifest_active_registered=false")
    if not (
        manifest.get("bound_to_route_selector") is True
        and manifest.get("selector_binding_reconciled") is True
        and manifest.get("selector_binding_source_phase") == "12L-K"
        and manifest.get("selector_binding_reconciliation_phase") == "13E_29"
    ):
        return fail(BLOCKED_MANIFEST_NOT_SELECTOR_BOUND, "manifest_selector_binding_metadata_invalid")

    if not (
        route_slice.get("route_id") == ROUTE_ID
        and route_slice.get("active_slice") is True
        and route_slice.get("registered") is True
    ):
        return fail(BLOCKED_SLICE_NOT_ACTIVE_REGISTERED, "slice_active_registered=false")
    requirements = route_slice.get("runtime_state_requirements", {})
    laws = route_slice.get("laws", {})
    if not (
        route_slice.get("bound_to_route_selector") is True
        and route_slice.get("selector_binding_reconciled") is True
        and requirements.get("selector_binding_required") is True
        and requirements.get("route_activation_requires_later_selector_patch") is False
        and laws.get("FILM_SCREENPLAY_GENERATION_NOT_SELECTOR_BOUND") is False
    ):
        return fail(BLOCKED_SLICE_NOT_SELECTOR_BOUND, "slice_selector_binding_metadata_invalid")

    if not (
        script_manifest.get("route_id") == SCRIPT_ROUTE_ID
        and script_slice.get("route_id") == SCRIPT_ROUTE_ID
        and manifest.get("preserves_content_route") == SCRIPT_ROUTE_ID
        and laws.get("SCRIPT_GENERATION_PRESERVED") is True
    ):
        return fail(BLOCKED_SCRIPT_ROUTE_NOT_PRESERVED, "script_generation_preservation_invalid")

    for document_name, document in [("manifest", manifest), ("slice", route_slice)]:
        if document.get("pass_claimed") is not False:
            return fail(BLOCKED_NO_FAKE_PASS_BOUNDARY_MISSING, f"{document_name}.pass_claimed=true")
        if document.get("governed_runtime_proof_claimed") is not False:
            return fail(
                BLOCKED_RUNTIME_PROOF_CLAIM,
                f"{document_name}.governed_runtime_proof_claimed=true",
            )
        if document.get("runtime_behavior_changed") is not False:
            return fail(
                BLOCKED_RUNTIME_PROOF_CLAIM,
                f"{document_name}.runtime_behavior_changed=true",
            )

    combined_text = "\n".join(read_text(repo_root / rel) for rel in REQUIRED_FILES)
    for token in FORBIDDEN_RUNTIME_PROOF_TOKENS:
        if token in combined_text:
            return fail(BLOCKED_RUNTIME_PROOF_CLAIM, f"forbidden_token={token}")

    downstream_routes = route_slice.get("downstream_allowed_routes", [])
    missing_downstream = [
        route_id for route_id in REQUIRED_DOWNSTREAM_ROUTES if route_id not in downstream_routes
    ]
    if missing_downstream:
        return fail(
            BLOCKED_DOWNSTREAM_BOUNDARY_MISSING,
            f"missing_downstream_routes={','.join(missing_downstream)}",
        )

    non_triggers = manifest.get("non_triggers", [])
    missing_content_triggers = [
        trigger for trigger in CONTENT_ROUTE_NEGATIVE_TRIGGERS if trigger not in non_triggers
    ]
    if missing_content_triggers:
        return fail(
            BLOCKED_SCRIPT_ROUTE_NOT_PRESERVED,
            f"missing_content_non_triggers={','.join(missing_content_triggers)}",
        )

    details = [
        "selector_mode=film_screenplay_generation",
        f"selector_allowed_route_id={ROUTE_ID}",
        "default_mode=script_only",
        "active_film_manifest_registered=true",
        "active_film_slice_registered=true",
        "manifest_bound_to_route_selector=true",
        "slice_bound_to_route_selector=true",
        "script_generation_preserved=true",
        "downstream_boundary_preserved=true",
        "content_route_negative_triggers_preserved=true",
        "runtime_behavior_changed=false",
        "pass_claimed=false",
        "governed_runtime_proof_claimed=false",
    ]
    return READY, details


def main() -> int:
    parser = argparse.ArgumentParser(description="Check post-binding film route repository state.")
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
