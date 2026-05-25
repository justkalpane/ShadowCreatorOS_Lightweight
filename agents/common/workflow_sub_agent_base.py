from __future__ import annotations

from typing import Any

from agents.common.production_agent_base import ProductionAgentBase
from agents.common.workflow_binding_contracts import get_workflow_contract


class WorkflowSubAgentBase(ProductionAgentBase):
    def __init__(
        self,
        workflow_slug: str,
        timeout_seconds: float = 8.0,
        max_retries: int = 2,
        backoff_seconds: float = 0.4,
    ) -> None:
        self.workflow_slug = workflow_slug
        self.workflow_contract = get_workflow_contract(workflow_slug)
        super().__init__(
            agent_slug=workflow_slug,
            director_binding=self.workflow_contract.get("primary_director", "Krishna"),
            artifact_family=f"{workflow_slug}-sub-agent-packet",
            timeout_seconds=timeout_seconds,
            max_retries=max_retries,
            backoff_seconds=backoff_seconds,
        )

    def execute_core(self, input_payload: dict[str, Any]) -> dict[str, Any]:
        contract = self.workflow_contract
        gate = contract.get("gate_rules", {})
        required_inputs = contract.get("required_inputs", [])
        allowed_directors = contract.get("allowed_directors", [])

        errors: list[str] = []

        if gate.get("require_dossier_id", True) and not input_payload.get("dossier_id"):
            errors.append("missing_dossier_id")

        acting_director = str(input_payload.get("acting_director", contract.get("primary_director", "Krishna")))
        if gate.get("enforce_director_binding", True) and allowed_directors and acting_director not in allowed_directors:
            errors.append("invalid_director_binding")

        if gate.get("require_declared_inputs", True):
            missing_inputs = [k for k in required_inputs if k not in input_payload]
            if missing_inputs:
                errors.append("missing_required_inputs:" + ",".join(missing_inputs))

        if gate.get("require_governance_ack_on_release", False):
            release_candidate = bool(input_payload.get("release_candidate", False))
            governance_ack = bool(input_payload.get("governance_ack", False))
            if release_candidate and not governance_ack:
                errors.append("missing_governance_ack")

        if errors:
            return {
                "status": "error",
                "attempts": 0,
                "elapsed_ms": 0,
                "error": ";".join(errors),
                "result": {
                    "mode": "workflow_contract_enforced",
                    "workflow_contract": contract,
                    "acting_director": acting_director,
                    "decision": {
                        "decision": "escalate",
                        "reason": "workflow_contract_gate_failed",
                        "next_route": "ROUTE_PHASE1_REPLAY",
                    },
                    "escalation_workflow": gate.get("escalate_to", "WF-900"),
                },
            }

        return {
            "status": "ok",
            "attempts": 0,
            "elapsed_ms": 0,
            "result": {
                "mode": "workflow_contract_enforced",
                "workflow_contract": contract,
                "acting_director": acting_director,
                "decision": {
                    "decision": "approve",
                    "reason": "workflow_contract_gate_passed",
                    "next_route": input_payload.get("route_id", "ROUTE_PHASE1_STANDARD"),
                },
                "escalation_workflow": None,
            },
        }

# MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE
# Append-only MAC-06.2B contract metadata.
# component_id: workflow_sub_agent_base
# component_layer: AGENT
# component_name: Workflow Sub Agent Base
# route_families: [quality_gate, full_video_pipeline]
# activation_triggers: route_family in [approval_gate, repo_write_mode] or explicit registry selection; mark approval_gate_profile only when route_family is unknown.
# upstream_inputs: [script_segment_packet, voice_context_packet, visual_context_packet, video_context_packet, music_sfx_packet, editing_timeline_packet, provider_handoff_packet]
# downstream_outputs: [media_quality_gate_packet, lineage_packet]
# required_input_packets: [script_segment_packet, voice_context_packet, visual_context_packet, video_context_packet, music_sfx_packet, editing_timeline_packet, provider_handoff_packet]
# emitted_output_packets: [media_quality_gate_packet, lineage_packet]
# communication_pointers: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_PROVIDER_QUALITY, PTR_QUALITY_LINEAGE]
# quality_gates: [script_score_gate, voice_score_gate, visual_score_gate, video_score_gate, audio_score_gate, editing_score_gate]
# validator_bindings: [media_quality_gate_packet_present, quality_scores_present, final_status_matches_weakest_evidence_layer]
# fallback_behavior: BLOCKED_BEFORE_OUTPUT if critical score is below threshold or missing.
# lineage_fields: [quality_gate_id, upstream_packet_ids, score_reason, failure_id]
# provider_boundary: provider_execution_allowed=false; quality gate reviews packets/artifacts only; no provider execution
# status_limits: May not claim production-ready, onboarded, provider-called, media-created, or n8n-executed without external proof.
# human_approval_points: [approve_quality_gate, revise_segment, reject_output]
# failure_modes: missing_input_packet, missing_output_schema, missing_validator_binding, missing_pointer, low_quality_score, provider_boundary_violation.
# handoff_targets: [media_quality_gate_packet, lineage_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_PROVIDER_QUALITY, PTR_QUALITY_LINEAGE]
# production_score_fields: [script_score, hook_score, retention_score, voice_score, visual_score, video_score, audio_score, editing_score, platform_score, lineage_score]
# workflow_ownership: Owns one workflow stage from input packet consumption to output packet emission.
# input_packet_consumption_rules: Must read and cite required upstream packet before stage execution.
# output_packet_emission_rules: Must emit structured downstream packet with lineage and quality score.
# cross_agent_handoff_rules: Must hand off only through communication pointer registry packets.
#
# MAC-06.2D ROUTE-SPECIFIC PRODUCTION DEPTH ENRICHMENT
# component_depth_status: PRODUCTION_DEPTH_ENRICHED
# route_profile_applied: media_quality_gate_profile
# route_family_resolved: [quality_gate, full_video_pipeline]
# activation_triggers_resolved: [quality, validation, compliance]
# required_input_packets_resolved: [script_segment_packet, voice_context_packet, visual_context_packet, video_context_packet, music_sfx_packet, editing_timeline_packet, provider_handoff_packet]
# emitted_output_packets_resolved: [media_quality_gate_packet, lineage_packet]
# communication_pointer_ids_resolved: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_PROVIDER_QUALITY, PTR_QUALITY_LINEAGE]
# validator_bindings_resolved: [media_quality_gate_packet_present, quality_scores_present, final_status_matches_weakest_evidence_layer]
# quality_gates_resolved: [script_score_gate, voice_score_gate, visual_score_gate, video_score_gate, audio_score_gate, editing_score_gate]
# fallback_behavior_resolved: BLOCKED_BEFORE_OUTPUT if critical score is below threshold or missing.
# lineage_fields_resolved: [quality_gate_id, upstream_packet_ids, score_reason, failure_id]
# provider_boundary_resolved: provider_execution_allowed=false; quality gate reviews packets/artifacts only; no provider execution; approval_packet_required_for_any_execution
# handoff_targets_resolved: [media_quality_gate_packet, lineage_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_PROVIDER_QUALITY, PTR_QUALITY_LINEAGE]
# production_score_fields_resolved: [script_score, hook_score, retention_score, voice_score, visual_score, video_score, audio_score, editing_score, platform_score, lineage_score]
# human_approval_points_resolved: [approve_quality_gate, revise_segment, reject_output]
# status_limits_resolved: [no PASS if weakest evidence is PARTIAL/BLOCKED]
# evidence_used_for_resolution: path/pre-contract keyword: quality/governance; component_path=agents/common/workflow_sub_agent_base.py; component_id=workflow_sub_agent_base
# remaining_unknowns: none
