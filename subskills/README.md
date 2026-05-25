This folder is reserved for subskill contracts. Source top-level subskills folder was not present during Wave 2. Do not invent subskills. Use registry truth or mark NEEDS_CONFIRMATION.

## MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE

This append-only block upgrades this component to the MAC-06.2B universal component contract standard. Existing behavior above remains intact; this block adds required typed inputs, outputs, pointers, validation, fallback, and lineage expectations.

component_id: README
component_layer: SUB_SKILL
component_name: Readme
route_families: [trend_research, topic_discovery, script_generation]
activation_triggers: route_family in [approval_gate, repo_write_mode] or explicit registry selection; mark approval_gate_profile only when route_family is unknown.
upstream_inputs: [topic_intake_packet, trend_signal_packet, source_evidence_packet]
downstream_outputs: [research_brief_packet, source_evidence_packet, claim_risk_packet]
required_input_packets: [topic_intake_packet, trend_signal_packet, source_evidence_packet]
emitted_output_packets: [research_brief_packet, source_evidence_packet, claim_risk_packet]
communication_pointers: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_RESEARCH_SCRIPT]
quality_gates: [source_breadth_gate, claim_confidence_gate, freshness_gate]
validator_bindings: [source_breadth_lock_status, per_tool_source_map_present, exact_rule_evidence_present]
fallback_behavior: NEEDS_CONFIRMATION if source breadth is insufficient.
lineage_fields: [source_url, source_date, claim_id, confidence_score, research_brief_packet_id]
provider_boundary: provider_execution_allowed=false; web research may cite sources; provider/media execution remains disabled without approval_packet
status_limits: May not claim production-ready, onboarded, provider-called, media-created, or n8n-executed without external proof.
human_approval_points: [approve_research_brief, request_more_sources, reject_claim]
failure_modes: missing_input_packet, missing_output_schema, missing_validator_binding, missing_pointer, low_quality_score, provider_boundary_violation.
handoff_targets: [research_brief_packet, source_evidence_packet, claim_risk_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_RESEARCH_SCRIPT]
production_score_fields: [source_score, freshness_score, claim_confidence_score, lineage_score]
atomic_operation: Reusable micro-operation selected by skill atomic_task_packet.
micro_input: Smallest required input; must be explicit and typed.
micro_output: Smallest output packet; must include validation and lineage.
evidence_path: Must point to input packet, rule, or source evidence.
validation_behavior: Return PASS/FAIL/NEEDS_HUMAN_REVIEW with reason; do not silently continue.

## M

## MAC-06.2D ROUTE-SPECIFIC PRODUCTION DEPTH ENRICHMENT

component_depth_status: PRODUCTION_DEPTH_ENRICHED
route_profile_applied: research_synthesis_profile
route_family_resolved: [trend_research, topic_discovery, script_generation]
activation_triggers_resolved: [freshness-sensitive task, source-backed claim]
required_input_packets_resolved: [topic_intake_packet, trend_signal_packet, source_evidence_packet]
emitted_output_packets_resolved: [research_brief_packet, source_evidence_packet, claim_risk_packet]
communication_pointer_ids_resolved: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_RESEARCH_SCRIPT]
validator_bindings_resolved: [source_breadth_lock_status, per_tool_source_map_present, exact_rule_evidence_present]
quality_gates_resolved: [source_breadth_gate, claim_confidence_gate, freshness_gate]
fallback_behavior_resolved: NEEDS_CONFIRMATION if source breadth is insufficient.
lineage_fields_resolved: [source_url, source_date, claim_id, confidence_score, research_brief_packet_id]
provider_boundary_resolved: provider_execution_allowed=false; web research may cite sources; provider/media execution remains disabled without approval_packet
handoff_targets_resolved: [research_brief_packet, source_evidence_packet, claim_risk_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_RESEARCH_SCRIPT]
production_score_fields_resolved: [source_score, freshness_score, claim_confidence_score, lineage_score]
human_approval_points_resolved: [approve_research_brief, request_more_sources, reject_claim]
status_limits_resolved: [no fake realtime claim, no provider execution]
evidence_used_for_resolution: path/pre-contract keyword: research/source/fact; component_path=subskills/README.md; component_id=README
remaining_unknowns: none
