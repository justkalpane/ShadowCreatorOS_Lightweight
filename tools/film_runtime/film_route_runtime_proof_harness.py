#!/usr/bin/env python3
"""Read-only proof harness preflight for the film screenplay route.

This harness does not execute runtime or claim PASS. It gathers the repo-state
evidence needed before a future governed runtime proof can be attempted.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
from pathlib import Path
from typing import Any


ROUTE_ID = "FILM_SCREENPLAY_GENERATION"
ROUTE_MODE = "film_screenplay_generation"
SCRIPT_ROUTE_ID = "SCRIPT_GENERATION"

STATUS_PREFLIGHT_READY = "FILM_RUNTIME_PROOF_HARNESS_PREFLIGHT_READY"
STATUS_BLOCKED_NO_GOVERNED_INVOCATION = "FILM_RUNTIME_PROOF_BLOCKED_NO_GOVERNED_INVOCATION"
STATUS_BLOCKED_ROUTE_STATE_SCHEMA_GAP = "FILM_RUNTIME_PROOF_BLOCKED_ROUTE_STATE_SCHEMA_GAP"
STATUS_BLOCKED_SKELETON_VALIDATORS = "FILM_RUNTIME_PROOF_BLOCKED_SKELETON_VALIDATORS"
STATUS_BLOCKED_SCRIPT_ROUTE_REGRESSION = "FILM_RUNTIME_PROOF_BLOCKED_SCRIPT_ROUTE_REGRESSION"
STATUS_BLOCKED_FAKE_PASS_ATTEMPT = "FILM_RUNTIME_PROOF_BLOCKED_FAKE_PASS_ATTEMPT"
STATUS_BLOCKED_MISSING_FILE = "FILM_RUNTIME_PROOF_BLOCKED_MISSING_FILE"
STATUS_BLOCKED_PARSE_ERROR = "FILM_RUNTIME_PROOF_BLOCKED_PARSE_ERROR"

POST_BINDING_READY = "POST_BINDING_FILM_ROUTE_STATE_READY"

REQUIRED_FILES = [
    "runtime/state/route_chain_mode_selector.yaml",
    "registries/route_manifests/film_screenplay_generation.yaml",
    "registries/route_slices/film_screenplay_generation.registry_slice.yaml",
    "registries/route_manifests/script_generation.yaml",
    "registries/route_slices/script_generation.registry_slice.yaml",
    "runtime/state/route_state_contract.md",
    "runtime/state/route_state.schema.json",
    "schemas/film/output_packet/film_screenplay_output_packet.schema.json",
    "validators/film/validate_film_route_post_binding_state.py",
    "validators/film/output_packet/validate_film_screenplay_packet.py",
    "validators/film/validation/validate_no_fake_film_pass.py",
    "validators/film/validation/validate_film_content_packet_separation.py",
    "validators/film/route/validate_film_route_selection.py",
]

CRITICAL_VALIDATORS = [
    "validators/film/output_packet/validate_film_screenplay_packet.py",
    "validators/film/validation/validate_no_fake_film_pass.py",
    "validators/film/validation/validate_film_content_packet_separation.py",
    "validators/film/route/validate_film_route_selection.py",
]

FORBIDDEN_PROOF_FIELDS = [
    "repository_lock_id",
    "proof_contract_id",
    "context_packet_id",
    "prompt_package_id",
    "evaluation_report_id",
    "completion_certificate",
]


def repo_root_from_here() -> Path:
    return Path(__file__).resolve().parents[2]


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_module(path: Path, name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def git_stdout(repo_root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=repo_root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return result.stdout.strip()


def load_yaml_subset(repo_root: Path, rel_path: str) -> dict[str, Any]:
    checker = load_module(
        repo_root / "validators/film/validate_film_route_post_binding_state.py",
        "phase_13e34_post_binding_checker",
    )
    return checker.load_yaml_subset(repo_root / rel_path)


def validator_status(repo_root: Path, rel_path: str) -> dict[str, Any]:
    path = repo_root / rel_path
    module = load_module(path, path.stem)
    if not hasattr(module, "validate"):
        return {
            "path": rel_path,
            "status": "VALIDATE_FUNCTION_MISSING",
            "passed": False,
            "enforced": False,
        }
    result = module.validate({})
    return {
        "path": rel_path,
        "status": result.get("status"),
        "passed": result.get("passed"),
        "enforced": result.get("enforced"),
        "validator_bound_to_runtime": result.get("validator_bound_to_runtime"),
        "governed_runtime_proof_claimed": result.get("governed_runtime_proof_claimed"),
    }


def build_route_state_template(repo_root: Path) -> dict[str, Any]:
    manifest = repo_root / "registries/route_manifests/film_screenplay_generation.yaml"
    consumed = [
        "runtime/state/route_chain_mode_selector.yaml",
        "registries/route_manifests/film_screenplay_generation.yaml",
        "registries/route_slices/film_screenplay_generation.registry_slice.yaml",
        "registries/route_manifests/script_generation.yaml",
        "registries/route_slices/script_generation.registry_slice.yaml",
        "runtime/state/route_state_contract.md",
        "runtime/state/route_state.schema.json",
        "schemas/film/output_packet/film_screenplay_output_packet.schema.json",
    ]
    file_hashes = {rel: sha256_file(repo_root / rel) for rel in consumed if (repo_root / rel).is_file()}
    return {
        "route_id": ROUTE_ID,
        "route_manifest_path": str(manifest.relative_to(repo_root)),
        "route_manifest_hash": sha256_file(manifest),
        "task_mode": ROUTE_MODE,
        "route_phase": "BLOCKED",
        "files_consumed": consumed,
        "file_hashes": file_hashes,
        "dependencies_complete": False,
        "output_phase_started": False,
        "last_completed_step": "POST_BINDING_STATIC_PREFLIGHT",
        "next_required_step": "RECONCILE_FILM_TASK_MODE_SCHEMA_AND_ENFORCE_VALIDATORS",
        "compaction_recovery_ready": True,
        "historical_files_allowed": False,
        "active_runtime_scope": [ROUTE_ID],
        "read_ledger": [
            {
                "file_path": rel,
                "file_hash": file_hashes.get(rel, ""),
                "first_read_phase": "PHASE_13E_34",
                "last_read_phase": "PHASE_13E_34",
                "read_count": 1,
                "reread_reason": "validator_mode",
                "route_required": True,
                "semantic_use_required": True,
                "semantic_use_status": "USED",
            }
            for rel in consumed
            if rel in file_hashes
        ],
    }


def evaluate(repo_root: Path) -> dict[str, Any]:
    missing = [rel for rel in REQUIRED_FILES if not (repo_root / rel).is_file()]
    if missing:
        return {
            "status": STATUS_BLOCKED_MISSING_FILE,
            "first_blocker": "missing_required_file",
            "missing_files": missing,
            "runtime_execution_performed": False,
            "film_output_generated": False,
            "pass_claimed": False,
            "governed_runtime_proof_claimed": False,
        }

    try:
        selector = load_yaml_subset(repo_root, "runtime/state/route_chain_mode_selector.yaml")
        manifest = load_yaml_subset(repo_root, "registries/route_manifests/film_screenplay_generation.yaml")
        route_slice = load_yaml_subset(repo_root, "registries/route_slices/film_screenplay_generation.registry_slice.yaml")
        script_slice = load_yaml_subset(repo_root, "registries/route_slices/script_generation.registry_slice.yaml")
        route_state_schema = json.loads((repo_root / "runtime/state/route_state.schema.json").read_text(encoding="utf-8"))
        film_output_schema = json.loads(
            (repo_root / "schemas/film/output_packet/film_screenplay_output_packet.schema.json").read_text(encoding="utf-8")
        )
    except Exception as exc:  # pragma: no cover - defensive report path
        return {
            "status": STATUS_BLOCKED_PARSE_ERROR,
            "first_blocker": "parse_error",
            "error": str(exc),
            "runtime_execution_performed": False,
            "film_output_generated": False,
            "pass_claimed": False,
            "governed_runtime_proof_claimed": False,
        }

    post_binding_checker = load_module(
        repo_root / "validators/film/validate_film_route_post_binding_state.py",
        "phase_13e34_post_binding_state",
    )
    post_binding_status, post_binding_details = post_binding_checker.evaluate(repo_root)

    film_mode = selector.get("modes", {}).get(ROUTE_MODE, {})
    default_mode_before = selector.get("default_mode")
    default_mode_after = selector.get("default_mode")
    selector_mode_resolved = film_mode.get("allowed_route_ids") == [ROUTE_ID]
    script_generation_preserved = default_mode_before == "script_only" and script_slice.get("route_id") == SCRIPT_ROUTE_ID

    route_state_task_modes = (
        route_state_schema.get("properties", {}).get("task_mode", {}).get("enum", [])
    )
    route_state_schema_compatible = ROUTE_MODE in route_state_task_modes

    output_required_fields = film_output_schema.get("required", [])
    film_output_schema_enforceable = bool(output_required_fields)

    validators = [validator_status(repo_root, rel) for rel in CRITICAL_VALIDATORS]
    film_validators_enforceable = all(
        item.get("status") != "SKELETON_ONLY"
        and item.get("passed") is not False
        and item.get("enforced") is not False
        for item in validators
    )

    forbidden_claim_attempt = any(
        manifest.get(key) not in {None, False} or route_slice.get(key) not in {None, False}
        for key in ["pass_claimed", "governed_runtime_proof_claimed", "runtime_behavior_changed"]
    )
    forbidden_runtime_tokens_present = [
        token
        for token in FORBIDDEN_PROOF_FIELDS
        if token in "\n".join(
            [
                (repo_root / "registries/route_manifests/film_screenplay_generation.yaml").read_text(encoding="utf-8"),
                (repo_root / "registries/route_slices/film_screenplay_generation.registry_slice.yaml").read_text(encoding="utf-8"),
            ]
        )
    ]

    first_blocker = "none"
    status = STATUS_PREFLIGHT_READY
    if post_binding_status != POST_BINDING_READY:
        status = STATUS_BLOCKED_NO_GOVERNED_INVOCATION
        first_blocker = f"post_binding_checker_status={post_binding_status}"
    elif not script_generation_preserved or not selector_mode_resolved:
        status = STATUS_BLOCKED_SCRIPT_ROUTE_REGRESSION
        first_blocker = "selector_or_script_generation_boundary_not_preserved"
    elif forbidden_claim_attempt or forbidden_runtime_tokens_present:
        status = STATUS_BLOCKED_FAKE_PASS_ATTEMPT
        first_blocker = "fake_pass_or_runtime_proof_claim_detected"
    elif not route_state_schema_compatible:
        status = STATUS_BLOCKED_ROUTE_STATE_SCHEMA_GAP
        first_blocker = "runtime/state/route_state.schema.json lacks film_screenplay_generation task_mode"
    elif not film_validators_enforceable:
        status = STATUS_BLOCKED_SKELETON_VALIDATORS
        first_blocker = "critical film validators remain skeleton-only or unenforced"
    elif not film_output_schema_enforceable:
        status = "FILM_RUNTIME_PROOF_BLOCKED_OUTPUT_SCHEMA_SKELETON"
        first_blocker = "film screenplay output schema has no required fields"

    route_state_template = build_route_state_template(repo_root)

    return {
        "status": status,
        "repo_root": str(repo_root),
        "head_sha": git_stdout(repo_root, "rev-parse", "HEAD"),
        "route_mode": ROUTE_MODE,
        "route_id": ROUTE_ID,
        "default_mode_before": default_mode_before,
        "default_mode_after": default_mode_after,
        "selector_mode_resolved": selector_mode_resolved,
        "manifest_path": "registries/route_manifests/film_screenplay_generation.yaml",
        "manifest_hash": sha256_file(repo_root / "registries/route_manifests/film_screenplay_generation.yaml"),
        "slice_path": "registries/route_slices/film_screenplay_generation.registry_slice.yaml",
        "slice_hash": sha256_file(repo_root / "registries/route_slices/film_screenplay_generation.registry_slice.yaml"),
        "script_generation_preserved": script_generation_preserved,
        "post_binding_checker_status": post_binding_status,
        "post_binding_checker_details": post_binding_details,
        "route_state_capsule_template_created": True,
        "route_state_capsule_written": False,
        "route_state_schema_compatible": route_state_schema_compatible,
        "route_state_task_modes": route_state_task_modes,
        "film_output_schema_enforceable": film_output_schema_enforceable,
        "film_output_schema_required_field_count": len(output_required_fields),
        "film_validators_enforceable": film_validators_enforceable,
        "validator_ledger": validators,
        "dirty_worktree_present": bool(git_stdout(repo_root, "status", "--porcelain")),
        "runtime_execution_performed": False,
        "film_output_generated": False,
        "runtime_behavior_changed": False,
        "pass_claimed": False,
        "governed_runtime_proof_claimed": False,
        "first_blocker": first_blocker,
        "next_safe_action": "reconcile film route state schema and make critical film validators enforceable before runtime proof",
        "route_state_capsule_template": route_state_template,
    }


def bool_text(value: Any) -> str:
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def render_text(report: dict[str, Any]) -> str:
    lines = [
        "FILM_RUNTIME_PROOF_HARNESS_REPORT",
        f"phase=13E_34",
        f"status={report['status']}",
        f"repo_root={report.get('repo_root')}",
        f"head_sha={report.get('head_sha')}",
        f"route_mode={report.get('route_mode')}",
        f"route_id={report.get('route_id')}",
        f"default_mode_before={report.get('default_mode_before')}",
        f"default_mode_after={report.get('default_mode_after')}",
        f"selector_mode_resolved={bool_text(report.get('selector_mode_resolved'))}",
        f"manifest_path={report.get('manifest_path')}",
        f"manifest_hash={report.get('manifest_hash')}",
        f"slice_path={report.get('slice_path')}",
        f"slice_hash={report.get('slice_hash')}",
        f"script_generation_preserved={bool_text(report.get('script_generation_preserved'))}",
        f"post_binding_checker_status={report.get('post_binding_checker_status')}",
        f"route_state_capsule_template_created={bool_text(report.get('route_state_capsule_template_created'))}",
        f"route_state_capsule_written={bool_text(report.get('route_state_capsule_written'))}",
        f"route_state_schema_compatible={bool_text(report.get('route_state_schema_compatible'))}",
        f"film_output_schema_enforceable={bool_text(report.get('film_output_schema_enforceable'))}",
        f"film_output_schema_required_field_count={report.get('film_output_schema_required_field_count')}",
        f"film_validators_enforceable={bool_text(report.get('film_validators_enforceable'))}",
        f"dirty_worktree_present={bool_text(report.get('dirty_worktree_present'))}",
        f"runtime_execution_performed={bool_text(report.get('runtime_execution_performed'))}",
        f"film_output_generated={bool_text(report.get('film_output_generated'))}",
        f"runtime_behavior_changed={bool_text(report.get('runtime_behavior_changed'))}",
        f"pass_claimed={bool_text(report.get('pass_claimed'))}",
        f"governed_runtime_proof_claimed={bool_text(report.get('governed_runtime_proof_claimed'))}",
        f"first_blocker={report.get('first_blocker')}",
        f"next_safe_action={report.get('next_safe_action')}",
        "validator_ledger:",
    ]
    for item in report.get("validator_ledger", []):
        lines.append(
            "- "
            + ",".join(
                [
                    f"path={item.get('path')}",
                    f"status={item.get('status')}",
                    f"passed={bool_text(item.get('passed'))}",
                    f"enforced={bool_text(item.get('enforced'))}",
                    f"validator_bound_to_runtime={bool_text(item.get('validator_bound_to_runtime'))}",
                ]
            )
        )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only film route runtime proof harness preflight.")
    parser.add_argument("--repo-root", default=None, help="Repository root. Defaults to this tool's repo root.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text.")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve() if args.repo_root else repo_root_from_here()
    report = evaluate(repo_root)
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(render_text(report))
    return 0 if report.get("status") == STATUS_PREFLIGHT_READY else 1


if __name__ == "__main__":
    raise SystemExit(main())
