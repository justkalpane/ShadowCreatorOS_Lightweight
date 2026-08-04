#!/usr/bin/env python3
"""Static dry-run checker for Batch 8K route/runtime/evidence bindings.

This script performs text-level validation only. It does not invoke validators,
routes, renderers, providers, or any media pipeline. It confirms that the
Media Factory handoff route surface references the route/runtime binding
contracts, the audit-event contract, and the blocked-first route defaults.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


REQUIRED_VALIDATORS = [
    "validators/validate_pilot_cut_manifest.py",
    "validators/validate_source_vs_render_artifact.py",
    "validators/validate_visual_qa_artifact.py",
    "validators/validate_contact_sheet.py",
    "validators/validate_human_review_packet.py",
    "validators/validate_approval_token.py",
    "validators/validate_c04a_asset_manifest.py",
    "validators/validate_approval_gate_matrix.py",
    "validators/validate_route_state_capsule.py",
    "validators/validate_evidence_bundle.py",
    "validators/validate_chitragupta_audit_event.py",
    "validators/validate_vayu_preflight.py",
    "validators/validate_kubera_gate.py",
    "validators/validate_yama_policy_gate.py",
    "validators/validate_creative_intent_packet.py",
    "validators/validate_packet_handoff_chain.py",
    "validators/validate_cut_level_visual_ledger.py",
    "validators/validate_full_render_unlock_packet.py",
    "validators/validate_c18_comfyui_failure_state.py",
    "validators/validate_tool_provider_boundary.py",
    "validators/validate_ffmpeg_filtergraph_governance.py",
    "validators/validate_depth_true_parallax.py",
    "validators/validate_hyperframes_composition.py",
]

CHECKS = [
    (
        "route_manifest_binding_contracts",
        "registries/route_manifests/media_factory_handoff.yaml",
        [
            "runtime_contracts/MEDIA_FACTORY_ROUTE_RUNTIME_BINDING_CONTRACT.md",
            "runtime_contracts/CHITRAGUPTA_AUDIT_EVENT_BINDING_CONTRACT.md",
        ],
    ),
    (
        "route_manifest_runtime_rules",
        "registries/route_manifests/media_factory_handoff.yaml",
        [
            "chitragupta_audit_event_required_for_route_state_transitions: true",
            "route_state_transition_requires_evidence_bundle: true",
            "route_state_transition_requires_audit_event: true",
            "pilot_prep_allowed: false",
            "pilot_execution_allowed: false",
            "full_render_allowed: false",
            "audio_allowed: false",
            "provider_allowed: false",
            "davinci_allowed: false",
            "no_fake_pass_route_regression_required: true",
        ],
    ),
    (
        "route_slice_binding_contracts",
        "registries/route_slices/media_factory_handoff.registry_slice.yaml",
        [
            "runtime_contracts/MEDIA_FACTORY_ROUTE_RUNTIME_BINDING_CONTRACT.md",
            "runtime_contracts/CHITRAGUPTA_AUDIT_EVENT_BINDING_CONTRACT.md",
        ],
    ),
    (
        "route_state_contract_binding",
        "runtime/state/route_state_contract.md",
        [
            "route_runtime_binding_contract=runtime_contracts/MEDIA_FACTORY_ROUTE_RUNTIME_BINDING_CONTRACT.md",
            "chitragupta_audit_event_binding_contract=runtime_contracts/CHITRAGUPTA_AUDIT_EVENT_BINDING_CONTRACT.md",
            "route_state_transition_audit_required=true",
            "route_state_transition_evidence_required=true",
            "route_state_transition_validation_required=true",
            "route_state_transition_no_fake_pass_required=true",
            "pilot_prep_allowed=false",
            "pilot_execution_allowed=false",
            "full_render_allowed=false",
            "audio_allowed=false",
            "provider_allowed=false",
            "davinci_allowed=false",
        ],
    ),
    (
        "evidence_scope_claim_contract",
        "runtime_contracts/EVIDENCE_SCOPE_CLAIM_CONTRACT.md",
        [
            "route_state_capsule_id=",
            "route_state_capsule_hash=",
            "audit_event_id=",
            "persisted_route_state_with_hash",
        ],
    ),
    (
        "no_fake_pass_gate",
        "runtime_contracts/NO_FAKE_PASS_GATE.md",
        [
            "MEDIA_FACTORY_HANDOFF",
            "route_pass_evidence_matrix.txt",
            "route_state_truth_without_evidence_bundle",
            "route_state_truth_without_audit_event",
            "route_unlock_without_validator_pass",
        ],
    ),
    (
        "route_execution_state_machine",
        "runtime_contracts/TASK_EXECUTION_STATE_MACHINE_CONTRACT.md",
        [
            "chitragupta_audit_event_present=true/false",
            "chitragupta_audit_event_schema_path=",
            "pilot_prep_allowed=false",
            "pilot_execution_allowed=false",
            "full_render_allowed=false",
            "audio_allowed=false",
            "provider_allowed=false",
            "davinci_allowed=false",
            "MEDIA_FACTORY_HANDOFF must remain blocked",
        ],
    ),
    (
        "route_dag_execution_contract",
        "runtime_contracts/ROUTE_DAG_EXECUTION_CONTRACT.md",
        [
            "route_bindings=[MEDIA_FACTORY_HANDOFF]",
            "route_state_capsule_required=true",
            "evidence_bundle_required=true",
            "chitragupta_audit_event_required=true",
            "pilot_prep_allowed=false",
            "pilot_execution_allowed=false",
            "full_render_allowed=false",
            "audio_allowed=false",
            "provider_allowed=false",
            "davinci_allowed=false",
        ],
    ),
    (
        "provider_adapter_boundary",
        "runtime_contracts/PROVIDER_ADAPTER_EXECUTION_BOUNDARY.md",
        [
            "MEDIA_FACTORY_HANDOFF",
            "route_state_capsule",
            "evidence_bundle",
            "chitragupta_audit_event",
            "provider_execution_enabled: false",
        ],
    ),
    (
        "pilot_cut_validation_gate",
        "runtime_contracts/PILOT_CUT_VALIDATION_GATE.md",
        [
            "MEDIA_FACTORY_HANDOFF",
            "evidence_bundle",
            "route_state_capsule",
            "chitragupta_audit_event",
        ],
    ),
    (
        "visual_qa_acceptance_gate",
        "runtime_contracts/VISUAL_QA_ACCEPTANCE_GATE.md",
        [
            "MEDIA_FACTORY_HANDOFF",
            "evidence_bundle",
            "route_state_capsule",
            "chitragupta_audit_event",
        ],
    ),
    (
        "audio_authorization_gate",
        "runtime_contracts/AUDIO_AUTHORIZATION_AND_SYNC_GATE.md",
        [
            "MEDIA_FACTORY_HANDOFF",
            "evidence_bundle",
            "route_state_capsule",
            "chitragupta_audit_event",
        ],
    ),
    (
        "davinci_handoff_gate",
        "runtime_contracts/DAVINCI_HANDOFF_AUTHORIZATION_GATE.md",
        [
            "MEDIA_FACTORY_HANDOFF",
            "evidence_bundle",
            "route_state_capsule",
            "chitragupta_audit_event",
        ],
    ),
]


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--report-dir", required=True)
    parser.add_argument(
        "--regression-report",
        default="/tmp/shadow_patch_batch8k_route_runtime_binding/batch8j_regression/07_fixture_validation_machine_report.json",
    )
    args = parser.parse_args()

    repo = Path(args.repo)
    report_dir = Path(args.report_dir)
    report_dir.mkdir(parents=True, exist_ok=True)

    results = []
    failed = []

    for check_id, rel_path, tokens in CHECKS:
        path = repo / rel_path
        exists = path.exists()
        text = load_text(path) if exists else ""
        missing = [token for token in tokens if token not in text]
        passed = exists and not missing
        results.append(
            {
                "check_id": check_id,
                "file_path": rel_path,
                "exists": exists,
                "required_tokens": tokens,
                "missing_tokens": missing,
                "passed": passed,
            }
        )
        if not passed:
            failed.append(check_id)

    regression_ok = False
    regression_summary = {}
    reg_path = Path(args.regression_report)
    if reg_path.exists():
        regression_summary = load_json(reg_path)
        regression_ok = (
            regression_summary.get("success") is True
            and regression_summary.get("expected_total") == 101
            and regression_summary.get("actual_total") == 101
            and regression_summary.get("gold_pass") == 46
            and regression_summary.get("bad_fail") == 55
            and regression_summary.get("unexpected_pass") == 0
            and regression_summary.get("unexpected_fail") == 0
            and regression_summary.get("wrong_error_code") == 0
        )
    else:
        failed.append("batch8j_regression_report_missing")

    machine_report = {
        "route_runtime_binding_pass": not failed and regression_ok,
        "batch8j_regression_ok": regression_ok,
        "check_count": len(results),
        "failed_checks": failed,
        "results": results,
        "regression_summary": regression_summary,
    }
    machine_path = report_dir / "route_runtime_binding_machine_report.json"
    machine_path.write_text(json.dumps(machine_report, indent=2, sort_keys=True), encoding="utf-8")

    md_lines = [
        "# Batch 8K Route Runtime Binding Dry Run",
        "",
        f"route_runtime_binding_pass={str(machine_report['route_runtime_binding_pass']).lower()}",
        f"batch8j_regression_ok={str(regression_ok).lower()}",
        f"checks={len(results)}",
        f"failed_checks={', '.join(failed) if failed else 'none'}",
        "",
        "| check_id | file_path | passed | missing_tokens |",
        "| --- | --- | --- | --- |",
    ]
    for row in results:
        md_lines.append(
            f"| {row['check_id']} | {row['file_path']} | {str(row['passed']).lower()} | "
            f"{', '.join(row['missing_tokens']) if row['missing_tokens'] else 'none'} |"
        )
    md_path = report_dir / "route_runtime_binding_human_report.md"
    md_path.write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    if machine_report["route_runtime_binding_pass"]:
        return 0
    print("ROUTE_RUNTIME_BINDING_DRY_RUN_FAIL")
    print(json.dumps(machine_report, indent=2, sort_keys=True))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
