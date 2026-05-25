from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from agents.common.production_agent_base import ProductionAgentBase, print_run


class AgentMedia006Agent(ProductionAgentBase):
    def __init__(
        self,
        timeout_seconds: float = 8.0,
        max_retries: int = 2,
        backoff_seconds: float = 0.4,
    ) -> None:
        super().__init__(
            agent_slug="agent_media_006",
            director_binding="Maya",
            artifact_family="media-worker-agent-packet",
            timeout_seconds=timeout_seconds,
            max_retries=max_retries,
            backoff_seconds=backoff_seconds,
        )


if __name__ == "__main__":
    print_run(AgentMedia006Agent())

# MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE
# Append-only MAC-06.2B contract metadata.
# component_id: agent_media_006_agent
# component_layer: AGENT
# component_name: Agent Media 006 Agent
# route_families: [trend_research, topic_discovery, script_generation]
# activation_triggers: route_family in [approval_gate, repo_write_mode] or explicit registry selection; mark approval_gate_profile only when route_family is unknown.
# upstream_inputs: [topic_intake_packet, trend_signal_packet, source_evidence_packet]
# downstream_outputs: [research_brief_packet, source_evidence_packet, claim_risk_packet]
# required_input_packets: [topic_intake_packet, trend_signal_packet, source_evidence_packet]
# emitted_output_packets: [research_brief_packet, source_evidence_packet, claim_risk_packet]
# communication_pointers: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_RESEARCH_SCRIPT]
# quality_gates: [source_breadth_gate, claim_confidence_gate, freshness_gate]
# validator_bindings: [source_breadth_lock_status, per_tool_source_map_present, exact_rule_evidence_present]
# fallback_behavior: NEEDS_CONFIRMATION if source breadth is insufficient.
# lineage_fields: [source_url, source_date, claim_id, confidence_score, research_brief_packet_id]
# provider_boundary: provider_execution_allowed=false; web research may cite sources; provider/media execution remains disabled without approval_packet
# status_limits: May not claim production-ready, onboarded, provider-called, media-created, or n8n-executed without external proof.
# human_approval_points: [approve_research_brief, request_more_sources, reject_claim]
# failure_modes: missing_input_packet, missing_output_schema, missing_validator_binding, missing_pointer, low_quality_score, provider_boundary_violation.
# handoff_targets: [research_brief_packet, source_evidence_packet, claim_risk_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_RESEARCH_SCRIPT]
# production_score_fields: [source_score, freshness_score, claim_confidence_score, lineage_score]
# workflow_ownership: Owns one workflow stage from input packet consumption to output packet emission.
# input_packet_consumption_rules: Must read and cite required upstream packet before stage execution.
# output_packet_emission_rules: Must emit structured downstream packet with lineage and quality score.
# cross_agent_handoff_rules: Must hand off only through communication pointer registry packets.
#
# MAC-06.2D ROUTE-SPECIFIC PRODUCTION DEPTH ENRICHMENT
# component_depth_status: PRODUCTION_DEPTH_ENRICHED
# route_profile_applied: research_synthesis_profile
# route_family_resolved: [trend_research, topic_discovery, script_generation]
# activation_triggers_resolved: [freshness-sensitive task, source-backed claim]
# required_input_packets_resolved: [topic_intake_packet, trend_signal_packet, source_evidence_packet]
# emitted_output_packets_resolved: [research_brief_packet, source_evidence_packet, claim_risk_packet]
# communication_pointer_ids_resolved: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_RESEARCH_SCRIPT]
# validator_bindings_resolved: [source_breadth_lock_status, per_tool_source_map_present, exact_rule_evidence_present]
# quality_gates_resolved: [source_breadth_gate, claim_confidence_gate, freshness_gate]
# fallback_behavior_resolved: NEEDS_CONFIRMATION if source breadth is insufficient.
# lineage_fields_resolved: [source_url, source_date, claim_id, confidence_score, research_brief_packet_id]
# provider_boundary_resolved: provider_execution_allowed=false; web research may cite sources; provider/media execution remains disabled without approval_packet
# handoff_targets_resolved: [research_brief_packet, source_evidence_packet, claim_risk_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_RESEARCH_SCRIPT]
# production_score_fields_resolved: [source_score, freshness_score, claim_confidence_score, lineage_score]
# human_approval_points_resolved: [approve_research_brief, request_more_sources, reject_claim]
# status_limits_resolved: [no fake realtime claim, no provider execution]
# evidence_used_for_resolution: path/pre-contract keyword: research/source/fact; component_path=agents/agent_media_006/agent_media_006_agent.py; component_id=agent_media_006_agent
# remaining_unknowns: none
