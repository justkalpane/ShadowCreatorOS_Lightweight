from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from agents.common.production_agent_base import ProductionAgentBase, print_run


class AgentGovernance008Agent(ProductionAgentBase):
    def __init__(
        self,
        timeout_seconds: float = 8.0,
        max_retries: int = 2,
        backoff_seconds: float = 0.4,
    ) -> None:
        super().__init__(
            agent_slug="agent_governance_008",
            director_binding="Yama",
            artifact_family="governance-worker-agent-packet",
            timeout_seconds=timeout_seconds,
            max_retries=max_retries,
            backoff_seconds=backoff_seconds,
        )


if __name__ == "__main__":
    print_run(AgentGovernance008Agent())

# MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE
# Append-only MAC-06.2B contract metadata.
# component_id: agent_governance_008_agent
# component_layer: AGENT
# component_name: Agent Governance 008 Agent
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
# evidence_used_for_resolution: path/pre-contract keyword: quality/governance; component_path=agents/agent_governance_008/agent_governance_008_agent.py; component_id=agent_governance_008_agent
# remaining_unknowns: none
