from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
MATRIX_PATH = ROOT / "registries" / "sub_agent_matrix.json"


def _assert(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


@lru_cache(maxsize=1)
def load_sub_agent_matrix() -> dict[str, Any]:
    _assert(MATRIX_PATH.exists(), f"Missing sub-agent matrix registry: {MATRIX_PATH}")
    with MATRIX_PATH.open(encoding="utf-8") as handle:
        data = json.load(handle)
    _assert(isinstance(data, dict), "Sub-agent matrix must be a JSON object.")
    _assert("entries" in data, "Sub-agent matrix missing entries block.")
    _assert(isinstance(data["entries"], list), "Sub-agent matrix entries must be a list.")
    return data


def iter_sub_agent_entries() -> list[dict[str, Any]]:
    return list(load_sub_agent_matrix()["entries"])


def get_sub_agent_entry(workflow_slug: str) -> dict[str, Any]:
    for entry in iter_sub_agent_entries():
        if entry.get("workflow_slug") == workflow_slug:
            return entry
    raise KeyError(workflow_slug)


def get_sub_agent_entries_by_family(workflow_family: str) -> list[dict[str, Any]]:
    return [entry for entry in iter_sub_agent_entries() if entry.get("workflow_family") == workflow_family]

# MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE
# Append-only MAC-06.2B contract metadata.
# component_id: sub_agent_matrix
# component_layer: AGENT
# component_name: Sub Agent Matrix
# route_families: [non_content_technical_task, general_support]
# activation_triggers: route_family in [script_generation] or explicit registry selection; mark script_generation_profile only when route_family is unknown.
# upstream_inputs: [stage_execution_packet, component_control_packet, lineage_packet]
# downstream_outputs: [component_result_packet, quality_report_packet, lineage_packet]
# required_input_packets: [stage_execution_packet, component_control_packet, lineage_packet]
# emitted_output_packets: [component_result_packet, quality_report_packet, lineage_packet]
# communication_pointers: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_QUALITY_LINEAGE]
# quality_gates: [component_integrity_gate, fallback_gate, lineage_gate]
# validator_bindings: [universal_component_contract_present, selected_components_are_registered, quality_scores_present]
# fallback_behavior: BLOCKED_BEFORE_OUTPUT if stage_execution_packet or component_result_packet cannot be produced.
# lineage_fields: [stage_execution_packet_id, component_result_packet_id, source_component_id, evidence_path]
# provider_boundary: provider_execution_allowed=false; no provider/media/n8n execution unless approval_packet authorizes specific scope
# status_limits: May not claim production-ready, onboarded, provider-called, media-created, or n8n-executed without external proof.
# human_approval_points: [approve_support_action, request_manual_review, reject_support_action]
# failure_modes: missing_input_packet, missing_output_schema, missing_validator_binding, missing_pointer, low_quality_score, provider_boundary_violation.
# handoff_targets: [component_result_packet, quality_report_packet, lineage_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_QUALITY_LINEAGE]
# production_score_fields: [component_quality_score, reliability_score, lineage_score]
# workflow_ownership: Owns one workflow stage from input packet consumption to output packet emission.
# input_packet_consumption_rules: Must read and cite required upstream packet before stage execution.
# output_packet_emission_rules: Must emit structured downstream packet with lineage and quality score.
# cross_agent_handoff_rules: Must hand off only through communication pointer registry packets.
#
# MAC-06.2D ROUTE-SPECIFIC PRODUCTION DEPTH ENRICHMENT
# component_depth_status: PRODUCTION_DEPTH_ENRICHED
# route_profile_applied: general_support_profile
# route_family_resolved: [non_content_technical_task, general_support]
# activation_triggers_resolved: [supporting component, control plane, kernel, recovery]
# required_input_packets_resolved: [stage_execution_packet, component_control_packet, lineage_packet]
# emitted_output_packets_resolved: [component_result_packet, quality_report_packet, lineage_packet]
# communication_pointer_ids_resolved: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_QUALITY_LINEAGE]
# validator_bindings_resolved: [universal_component_contract_present, selected_components_are_registered, quality_scores_present]
# quality_gates_resolved: [component_integrity_gate, fallback_gate, lineage_gate]
# fallback_behavior_resolved: BLOCKED_BEFORE_OUTPUT if stage_execution_packet or component_result_packet cannot be produced.
# lineage_fields_resolved: [stage_execution_packet_id, component_result_packet_id, source_component_id, evidence_path]
# provider_boundary_resolved: provider_execution_allowed=false; no provider/media/n8n execution unless approval_packet authorizes specific scope
# handoff_targets_resolved: [component_result_packet, quality_report_packet, lineage_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_QUALITY_LINEAGE]
# production_score_fields_resolved: [component_quality_score, reliability_score, lineage_score]
# human_approval_points_resolved: [approve_support_action, request_manual_review, reject_support_action]
# status_limits_resolved: [support components cannot claim production output alone]
# evidence_used_for_resolution: fallback: cross-route support component; component_path=agents/common/sub_agent_matrix.py; component_id=sub_agent_matrix
# remaining_unknowns: none
