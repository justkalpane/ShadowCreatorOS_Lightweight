from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


TARGETS = {
    "pilot_cut_manifest": {
        "schema_name": "pilot_cut_manifest.schema.json",
        "schema_path": ROOT / "schemas" / "media_factory" / "pilot_cut_manifest.schema.json",
        "validator_file": ROOT / "validators" / "validate_pilot_cut_manifest.py",
    },
    "source_vs_render_artifact": {
        "schema_name": "source_vs_render_artifact.schema.json",
        "schema_path": ROOT / "schemas" / "media_factory" / "source_vs_render_artifact.schema.json",
        "validator_file": ROOT / "validators" / "validate_source_vs_render_artifact.py",
    },
    "visual_qa_artifact": {
        "schema_name": "visual_qa_artifact.schema.json",
        "schema_path": ROOT / "schemas" / "media_factory" / "visual_qa_artifact.schema.json",
        "validator_file": ROOT / "validators" / "validate_visual_qa_artifact.py",
    },
    "contact_sheet": {
        "schema_name": "contact_sheet.schema.json",
        "schema_path": ROOT / "schemas" / "media_factory" / "contact_sheet.schema.json",
        "validator_file": ROOT / "validators" / "validate_contact_sheet.py",
    },
    "human_review_packet": {
        "schema_name": "human_review_packet.schema.json",
        "schema_path": ROOT / "schemas" / "governance" / "human_review_packet.schema.json",
        "validator_file": ROOT / "validators" / "validate_human_review_packet.py",
    },
    "approval_token": {
        "schema_name": "approval_token.schema.json",
        "schema_path": ROOT / "schemas" / "governance" / "approval_token.schema.json",
        "validator_file": ROOT / "validators" / "validate_approval_token.py",
    },
    "c04a_asset_manifest": {
        "schema_name": "c04a_asset_manifest.schema.json",
        "schema_path": ROOT / "schemas" / "media_factory" / "c04a_asset_manifest.schema.json",
        "validator_file": ROOT / "validators" / "validate_c04a_asset_manifest.py",
    },
    "approval_gate_matrix": {
        "schema_name": "approval_gate_matrix.schema.json",
        "schema_path": ROOT / "schemas" / "governance" / "approval_gate_matrix.schema.json",
        "validator_file": ROOT / "validators" / "validate_approval_gate_matrix.py",
    },
    "route_state_capsule": {
        "schema_name": "route_state_capsule.schema.json",
        "schema_path": ROOT / "schemas" / "runtime_state" / "route_state_capsule.schema.json",
        "validator_file": ROOT / "validators" / "validate_route_state_capsule.py",
    },
    "evidence_bundle": {
        "schema_name": "evidence_bundle.schema.json",
        "schema_path": ROOT / "schemas" / "runtime_state" / "evidence_bundle.schema.json",
        "validator_file": ROOT / "validators" / "validate_evidence_bundle.py",
    },
    "chitragupta_audit_event": {
        "schema_name": "chitragupta_audit_event.schema.json",
        "schema_path": ROOT / "schemas" / "governance" / "chitragupta_audit_event.schema.json",
        "validator_file": ROOT / "validators" / "validate_chitragupta_audit_event.py",
    },
    "vayu_preflight": {
        "schema_name": "vayu_preflight.schema.json",
        "schema_path": ROOT / "schemas" / "governance" / "vayu_preflight.schema.json",
        "validator_file": ROOT / "validators" / "validate_vayu_preflight.py",
    },
    "kubera_gate": {
        "schema_name": "kubera_gate.schema.json",
        "schema_path": ROOT / "schemas" / "governance" / "kubera_gate.schema.json",
        "validator_file": ROOT / "validators" / "validate_kubera_gate.py",
    },
    "yama_policy_gate": {
        "schema_name": "yama_policy_gate.schema.json",
        "schema_path": ROOT / "schemas" / "governance" / "yama_policy_gate.schema.json",
        "validator_file": ROOT / "validators" / "validate_yama_policy_gate.py",
    },
    "creative_intent_packet": {
        "schema_name": "creative_intent_packet.schema.json",
        "schema_path": ROOT / "schemas" / "media_factory" / "creative_intent_packet.schema.json",
        "validator_file": ROOT / "validators" / "validate_creative_intent_packet.py",
    },
    "packet_handoff_chain": {
        "schema_name": "packet_handoff_chain.schema.json",
        "schema_path": ROOT / "schemas" / "media_factory" / "packet_handoff_chain.schema.json",
        "validator_file": ROOT / "validators" / "validate_packet_handoff_chain.py",
    },
    "cut_level_visual_ledger": {
        "schema_name": "cut_level_visual_ledger.schema.json",
        "schema_path": ROOT / "schemas" / "media_factory" / "cut_level_visual_ledger.schema.json",
        "validator_file": ROOT / "validators" / "validate_cut_level_visual_ledger.py",
    },
    "full_render_unlock_packet": {
        "schema_name": "full_render_unlock_packet.schema.json",
        "schema_path": ROOT / "schemas" / "media_factory" / "full_render_unlock_packet.schema.json",
        "validator_file": ROOT / "validators" / "validate_full_render_unlock_packet.py",
    },
    "c18_comfyui_failure_state": {
        "schema_name": "c18_comfyui_failure_state.schema.json",
        "schema_path": ROOT / "schemas" / "media_factory" / "c18_comfyui_failure_state.schema.json",
        "validator_file": ROOT / "validators" / "validate_c18_comfyui_failure_state.py",
    },
    "tool_provider_boundary": {
        "schema_name": "tool_provider_boundary.schema.json",
        "schema_path": ROOT / "schemas" / "governance" / "tool_provider_boundary.schema.json",
        "validator_file": ROOT / "validators" / "validate_tool_provider_boundary.py",
    },
    "ffmpeg_filtergraph_governance": {
        "schema_name": "ffmpeg_filtergraph_governance.schema.json",
        "schema_path": ROOT / "schemas" / "media_factory" / "ffmpeg_filtergraph_governance.schema.json",
        "validator_file": ROOT / "validators" / "validate_ffmpeg_filtergraph_governance.py",
    },
    "depth_true_parallax": {
        "schema_name": "depth_true_parallax.schema.json",
        "schema_path": ROOT / "schemas" / "media_factory" / "depth_true_parallax.schema.json",
        "validator_file": ROOT / "validators" / "validate_depth_true_parallax.py",
    },
    "hyperframes_composition": {
        "schema_name": "hyperframes_composition.schema.json",
        "schema_path": ROOT / "schemas" / "media_factory" / "hyperframes_composition.schema.json",
        "validator_file": ROOT / "validators" / "validate_hyperframes_composition.py",
    },
}


SCHEMA_NAME_TO_TARGET = {spec["schema_name"]: target for target, spec in TARGETS.items()}


def fixture_root() -> Path:
    return ROOT / "tests" / "shadow_runtime" / "fixtures" / "batch8i"


def oracle_path() -> Path:
    return fixture_root() / "oracle" / "fixture_oracle.json"


def fixture_path_from_row(row: dict) -> Path:
    root = fixture_root() / ("gold" if row.get("expected_result") == "PASS" else "bad")
    return root / row["fixture_file"]

