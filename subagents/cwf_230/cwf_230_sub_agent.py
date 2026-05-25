from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from agents.common.workflow_sub_agent_base import WorkflowSubAgentBase
from agents.common.production_agent_base import print_run


class Cwf230SubAgent(WorkflowSubAgentBase):
    def __init__(
        self,
        timeout_seconds: float = 8.0,
        max_retries: int = 2,
        backoff_seconds: float = 0.4,
    ) -> None:
        super().__init__(
            workflow_slug="cwf_230",
            timeout_seconds=timeout_seconds,
            max_retries=max_retries,
            backoff_seconds=backoff_seconds,
        )


if __name__ == "__main__":
    print_run(Cwf230SubAgent())

# MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE
# Append-only MAC-06.2B contract metadata.
# component_id: cwf_230_sub_agent
# component_layer: SUB_AGENT
# component_name: Cwf 230 Sub Agent
# route_families: [non_content_technical_task, general_support]
# activation_triggers: route_family in [approval_gate, repo_write_mode] or explicit registry selection; mark approval_gate_profile only when route_family is unknown.
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
# execution_lane: Owns a bounded execution lane within the selected agent stage.
# route_binding: Activated only when route manifest or parent agent selects this lane.
# skill_activation_rules: May activate only skills with matching input schema and validator binding.
# validation_checkpoint: Must record lane_output_validated=true/false and fallback if false.
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
# evidence_used_for_resolution: fallback: cross-route support component; component_path=subagents/cwf_230/cwf_230_sub_agent.py; component_id=cwf_230_sub_agent
# remaining_unknowns: none
