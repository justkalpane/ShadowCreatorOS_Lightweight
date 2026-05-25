# SUBSKILL SS-001 - Context Packet Sanitizer

## SECTION 1: SKILL IDENTITY & OWNERSHIP
- Skill_ID: SS-001
- Canonical_Name: Context Packet Sanitizer
- Archetype: integration
- Role_Type: PRIMARY_ROLE
- Owner_Director: Krishna
- Domain: Context Engineering

## SECTION 2: AUTHORITY MATRIX
- Can_Execute: provider optimization, payload shaping, quality gating, fallback routing
- Cannot_Execute: policy override, budget override, unauthorized namespace mutation
- Requires_Approval: premium provider route when budget/policy token required
- Escalation_Required: critical provider auth/callback failures
- Veto_Authority: NO

## SECTION 3: READS (INPUT VEINS)
### 3.1 Primary Inputs
- dossier_id:string
- input_payload:object
- route_id:string(optional)

### 3.2 Provider Context
  - internal_packet_runtime

## SECTION 4: WRITES (OUTPUT VEINS)
- artifact_family:context-packet-sanitizer_packet
- sanitized_payload:object
- status:success|failed
- write_target: dossier.platform_subskills.context-packet-sanitizer (append_only)
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
- Normalize whitespace and key casing before workflow handoff
- Drop null and empty fields while preserving lineage keys
- Keep transformations idempotent for replay safety

## SECTION 8: EXECUTION RULES & CONSTRAINTS
- Enforce patch-only mutation law on dossier writes.
- Never bypass provider auth/callback contracts.
- Record deterministic replay metadata for every execution.
- Respect route_id, cost_tier, and policy verdict constraints.

## SECTION 9: FAILURE MODES & RECOVERY
- missing_dossier_id -> escalate WF-900
- non_object_input_payload -> return failed packet
- lineage_fields_missing -> route WF-021 for remodify

## SECTION 10: TOOL POLICY
- Allowed_Tools: n8n workflow nodes, provider adapters, packet validators, local runtime utilities
- Forbidden_Tools: destructive filesystem operations, unauthorized secret writes
- Secret_Scope: local secure store and approved secret manager only

## SECTION 11: N8N + OLLAMA PLUGGABILITY
- n8n_consumer_workflows:
  - WF-300
  - CWF-310
  - CWF-320
- ollama_reasoning_injection: true
- packet_contract: context-packet-sanitizer_packet
- replay_path: WF-021
- escalation_path: WF-900

## SECTION 12: VALIDATION & ACCEPTANCE
- Must emit status, artifact_family, payload, and provider_execution_summary.
- Must include deterministic error codes on failed/degraded runs.
- Must pass field-level schema checks before downstream handoff.

## MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE

This append-only block upgrades this component to the MAC-06.2B universal component contract standard. Existing behavior above remains intact; this block adds required typed inputs, outputs, pointers, validation, fallback, and lineage expectations.

component_id: SS-001-context-packet-sanitizer.subskill
component_layer: SKILL
component_name: Ss 001 Context Packet Sanitizer.Subskill
route_families: [context_engineering, script_generation]
activation_triggers: route_family in [quality_gate, lineage_summary] or explicit registry selection; mark approval_gate_profile only when route_family is unknown.
upstream_inputs: [final_script_packet, script_segment_packet, research_brief_packet]
downstream_outputs: [voice_context_packet, visual_context_packet, video_context_packet, music_sfx_packet, editing_timeline_packet, provider_handoff_packet]
required_input_packets: [final_script_packet, script_segment_packet, research_brief_packet]
emitted_output_packets: [voice_context_packet, visual_context_packet, video_context_packet, music_sfx_packet, editing_timeline_packet, provider_handoff_packet]
communication_pointers: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_FINAL_SCRIPT_VOICE, PTR_FINAL_SCRIPT_IMAGE, PTR_FINAL_SCRIPT_VIDEO, PTR_FINAL_SCRIPT_MUSIC_SFX, PTR_FINAL_SCRIPT_EDITING, PTR_MEDIA_PROVIDER_HANDOFF]
quality_gates: [context_completeness_gate, asset_consistency_gate, provider_boundary_gate]
validator_bindings: [provider_handoff_packet_present, media_quality_gate_packet_present, lineage_approval_packet_present]
fallback_behavior: BLOCKED_BEFORE_OUTPUT if any media context packet lacks segment_id.
lineage_fields: [script_segment_packet_id, context_packet_id, provider_handoff_packet_id]
provider_boundary: handoff planning only; provider_execution_allowed=false until approval_packet
status_limits: May not claim production-ready, onboarded, provider-called, media-created, or n8n-executed without external proof.
human_approval_points: [approve_context_packet, revise_asset_brief, block_provider_handoff]
failure_modes: missing_input_packet, missing_output_schema, missing_validator_binding, missing_pointer, low_quality_score, provider_boundary_violation.
handoff_targets: [voice_context_packet, visual_context_packet, video_context_packet, music_sfx_packet, editing_timeline_packet, provider_handoff_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_FINAL_SCRIPT_VOICE, PTR_FINAL_SCRIPT_IMAGE, PTR_FINAL_SCRIPT_VIDEO, PTR_FINAL_SCRIPT_MUSIC_SFX, PTR_FINAL_SCRIPT_EDITING, PTR_MEDIA_PROVIDER_HANDOFF]
production_score_fields: [voice_score, visual_score, video_score, audio_score, editing_score, lineage_score]
skill_activation_contract: Activated by skill_activation_packet from subagent or route manifest.
input_schema: Must declare atomic input fields before use; approval_gate_profile if absent upstream.
output_schema: Must emit atomic output packet with evidence path and validation status.
subskill_hooks: May call subskills only through atomic_task_packet.
quality_metric: Must emit skill_quality_score and quality_threshold.

## M

## MAC-06.2D ROUTE-SPECIFIC PRODUCTION DEPTH ENRICHMENT

component_depth_status: PRODUCTION_DEPTH_ENRICHED
route_profile_applied: context_engineering_profile
route_family_resolved: [context_engineering, script_generation]
activation_triggers_resolved: [context packet, asset brief, media handoff]
required_input_packets_resolved: [final_script_packet, script_segment_packet, research_brief_packet]
emitted_output_packets_resolved: [voice_context_packet, visual_context_packet, video_context_packet, music_sfx_packet, editing_timeline_packet, provider_handoff_packet]
communication_pointer_ids_resolved: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_FINAL_SCRIPT_VOICE, PTR_FINAL_SCRIPT_IMAGE, PTR_FINAL_SCRIPT_VIDEO, PTR_FINAL_SCRIPT_MUSIC_SFX, PTR_FINAL_SCRIPT_EDITING, PTR_MEDIA_PROVIDER_HANDOFF]
validator_bindings_resolved: [provider_handoff_packet_present, media_quality_gate_packet_present, lineage_approval_packet_present]
quality_gates_resolved: [context_completeness_gate, asset_consistency_gate, provider_boundary_gate]
fallback_behavior_resolved: BLOCKED_BEFORE_OUTPUT if any media context packet lacks segment_id.
lineage_fields_resolved: [script_segment_packet_id, context_packet_id, provider_handoff_packet_id]
provider_boundary_resolved: handoff planning only; provider_execution_allowed=false until approval_packet
handoff_targets_resolved: [voice_context_packet, visual_context_packet, video_context_packet, music_sfx_packet, editing_timeline_packet, provider_handoff_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_FINAL_SCRIPT_VOICE, PTR_FINAL_SCRIPT_IMAGE, PTR_FINAL_SCRIPT_VIDEO, PTR_FINAL_SCRIPT_MUSIC_SFX, PTR_FINAL_SCRIPT_EDITING, PTR_MEDIA_PROVIDER_HANDOFF]
production_score_fields_resolved: [voice_score, visual_score, video_score, audio_score, editing_score, lineage_score]
human_approval_points_resolved: [approve_context_packet, revise_asset_brief, block_provider_handoff]
status_limits_resolved: [no tool execution, no media creation]
evidence_used_for_resolution: path/pre-contract keyword: context engineering; component_path=skills/sub_skills/SS-001-context-packet-sanitizer.subskill.md; component_id=SS-001-context-packet-sanitizer.subskill
remaining_unknowns: none
