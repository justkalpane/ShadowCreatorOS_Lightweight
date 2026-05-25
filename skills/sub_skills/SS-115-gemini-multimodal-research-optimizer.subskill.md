# SUBSKILL SS-115 - Gemini Multimodal Research Optimizer

## SECTION 1: SKILL IDENTITY & OWNERSHIP
- Skill_ID: SS-115
- Canonical_Name: Gemini Multimodal Research Optimizer
- Archetype: integration
- Role_Type: PRIMARY_ROLE
- Owner_Director: Vyasa
- Domain: Research Intelligence

## SECTION 2: AUTHORITY MATRIX
- Can_Execute: provider optimization, payload shaping, quality gating, fallback routing
- Cannot_Execute: policy override, budget override, unauthorized namespace mutation
- Requires_Approval: premium provider route when budget/policy token required
- Escalation_Required: critical provider auth/callback failures
- Veto_Authority: NO

## SECTION 3: READS (INPUT VEINS)
### 3.1 Primary Inputs
- dossier_id:string
- research_brief:object
- mode:string

### 3.2 Provider Context
  - gemini_provider
  - openrouter_fallback

## SECTION 4: WRITES (OUTPUT VEINS)
- artifact_family:gemini-research-optimizer_packet
- research_findings:object
- evidence_index:array
- status:success|failed|degraded
- write_target: dossier.platform_subskills.gemini-multimodal-research-optimizer (append_only)
- write_target: se_packet_index (append_only)

## SECTION 5: EXECUTION FLOW & ALGORITHM
1. Validate required fields and provider legality posture.
2. Apply platform-specific optimization rules and constraints.
3. Execute guarded transformation and collect runtime telemetry.
4. Validate output packet fields and quality floor criteria.
5. Emit packet, append dossier patch, and route escalation if required.

## SECTION 6: SCORING FRAMEWORK
- quality_score (0-100)
- latency_score (0-100)
- cost_efficiency_score (0-100)
- governance_compliance_score (0-100)
- acceptance_rule: governance_compliance_score >= 90 and quality_score >= 75

## SECTION 7: BEST PRACTICES
- Use multimodal prompt envelopes with strict evidence sections
- Enforce citation-required output for research packets
- Separate exploration mode from finalization mode
- Cache high-confidence evidence summaries for reuse
- Fallback to local summarization when provider path is unavailable

## SECTION 8: EXECUTION RULES & CONSTRAINTS
- Enforce patch-only mutation law on dossier writes.
- Never bypass provider auth/callback contracts.
- Record deterministic replay metadata for every execution.
- Respect route_id, cost_tier, and policy verdict constraints.

## SECTION 9: FAILURE MODES & RECOVERY
- provider_auth_error -> route to fallback model path
- citation_missing -> reject and regenerate response
- policy_block -> escalate to governance gate
- timeout -> partial packet with explicit evidence gaps

## SECTION 10: TOOL POLICY
- Allowed_Tools: n8n workflow nodes, provider adapters, packet validators, local runtime utilities
- Forbidden_Tools: destructive filesystem operations, unauthorized secret writes
- Secret_Scope: local secure store and approved secret manager only

## SECTION 11: N8N + OLLAMA PLUGGABILITY
- n8n_consumer_workflows:
  - WF-100
  - CWF-110
  - CWF-140
- ollama_reasoning_injection: true
- packet_contract: gemini-multimodal-research-optimizer_packet
- replay_path: WF-021
- escalation_path: WF-900

## SECTION 12: VALIDATION & ACCEPTANCE
- Must emit status, artifact_family, payload, and provider_execution_summary.
- Must include deterministic error codes on failed/degraded runs.
- Must pass field-level schema checks before downstream handoff.

## MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE

This append-only block upgrades this component to the MAC-06.2B universal component contract standard. Existing behavior above remains intact; this block adds required typed inputs, outputs, pointers, validation, fallback, and lineage expectations.

component_id: SS-115-gemini-multimodal-research-optimizer.subskill
component_layer: SKILL
component_name: Ss 115 Gemini Multimodal Research Optimizer.Subskill
route_families: [approval_gate, repo_write_mode]
activation_triggers: route_family in [trend_research, quality_gate] or explicit registry selection; mark approval_gate_profile only when route_family is unknown.
upstream_inputs: [lineage_packet, approval_packet, media_quality_gate_packet]
downstream_outputs: [approval_packet, execution_authorization_packet]
required_input_packets: [lineage_packet, approval_packet, media_quality_gate_packet]
emitted_output_packets: [approval_packet, execution_authorization_packet]
communication_pointers: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_LINEAGE_APPROVAL]
quality_gates: [explicit_user_approval_gate, scope_lock_gate, risk_acceptance_gate]
validator_bindings: [lineage_approval_packet_present, no_n8n_provider_media_execution, provider_boundary_present]
fallback_behavior: BLOCKED_BEFORE_OUTPUT until explicit user approval is present.
lineage_fields: [approval_packet_id, user_decision, scope, risk_acknowledged]
provider_boundary: provider_execution_allowed=false; may authorize future execution only when approval_packet explicitly states scope
status_limits: May not claim production-ready, onboarded, provider-called, media-created, or n8n-executed without external proof.
human_approval_points: [approve_patch, approve_commit, approve_provider_execution, reject]
failure_modes: missing_input_packet, missing_output_schema, missing_validator_binding, missing_pointer, low_quality_score, provider_boundary_violation.
handoff_targets: [approval_packet, execution_authorization_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_LINEAGE_APPROVAL]
production_score_fields: [approval_clarity_score, risk_score, lineage_score]
skill_activation_contract: Activated by skill_activation_packet from subagent or route manifest.
input_schema: Must declare atomic input fields before use; approval_gate_profile if absent upstream.
output_schema: Must emit atomic output packet with evidence path and validation status.
subskill_hooks: May call subskills only through atomic_task_packet.
quality_metric: Must emit skill_quality_score and quality_threshold.

## M

## MAC-06.2D ROUTE-SPECIFIC PRODUCTION DEPTH ENRICHMENT

component_depth_status: PRODUCTION_DEPTH_ENRICHED
route_profile_applied: approval_gate_profile
route_family_resolved: [approval_gate, repo_write_mode]
activation_triggers_resolved: [approval, oauth, permission]
required_input_packets_resolved: [lineage_packet, approval_packet, media_quality_gate_packet]
emitted_output_packets_resolved: [approval_packet, execution_authorization_packet]
communication_pointer_ids_resolved: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_LINEAGE_APPROVAL]
validator_bindings_resolved: [lineage_approval_packet_present, no_n8n_provider_media_execution, provider_boundary_present]
quality_gates_resolved: [explicit_user_approval_gate, scope_lock_gate, risk_acceptance_gate]
fallback_behavior_resolved: BLOCKED_BEFORE_OUTPUT until explicit user approval is present.
lineage_fields_resolved: [approval_packet_id, user_decision, scope, risk_acknowledged]
provider_boundary_resolved: provider_execution_allowed=false; may authorize future execution only when approval_packet explicitly states scope
handoff_targets_resolved: [approval_packet, execution_authorization_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_LINEAGE_APPROVAL]
production_score_fields_resolved: [approval_clarity_score, risk_score, lineage_score]
human_approval_points_resolved: [approve_patch, approve_commit, approve_provider_execution, reject]
status_limits_resolved: [no commit/push/provider/n8n without approval]
evidence_used_for_resolution: path/pre-contract keyword: approval/oauth; component_path=skills/sub_skills/SS-115-gemini-multimodal-research-optimizer.subskill.md; component_id=SS-115-gemini-multimodal-research-optimizer.subskill
remaining_unknowns: none
