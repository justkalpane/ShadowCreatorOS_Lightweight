# SUBSKILL SS-251 - Context Window Optimizer

## SECTION 1: SKILL IDENTITY & OWNERSHIP
- Skill_ID: SS-251
- Canonical_Name: Context Window Optimizer
- Archetype: integration
- Role_Type: PRIMARY_ROLE
- Owner_Director: Ganesha
- Domain: Context Window Management

## SECTION 2: AUTHORITY MATRIX
- Can_Execute: token estimation, context truncation, segment ranking, context window enforcement
- Cannot_Execute: model parameter override, model selection override, policy bypass
- Requires_Approval: premium trimming rules modification
- Escalation_Required: severe input length exceeding absolute model maximums
- Veto_Authority: NO

## SECTION 3: READS (INPUT VEINS)
### 3.1 Primary Inputs
- dossier_id:string
- input_payload:object
- max_context_limit:integer
- priority_keys:array

### 3.2 Provider Context
  - gemini_provider
  - openrouter_api
  - ollama_local

## SECTION 4: WRITES (OUTPUT VEINS)
- artifact_family:context-window-optimizer_packet
- optimized_payload:object
- tokens_removed:integer
- status:success|failed|degraded
- write_target: dossier.prompt_intelligence.context-window-optimizer (append_only)
- write_target: se_packet_index (append_only)

## SECTION 5: EXECUTION FLOW & ALGORITHM
1. Validate required fields (`dossier_id`, `input_payload`, `max_context_limit`).
2. Estimate the token length of the input payload (e.g. character count divided by 4 as a proxy, or model-specific tokenizer).
3. If the input exceeds `max_context_limit`, rank and prioritize segments using `priority_keys`.
4. Prune lower priority fields/segments until the total fits within `max_context_limit`.
5. Return the optimized payload, the delta tokens removed, and success/degraded status.

## SECTION 6: SCORING FRAMEWORK
- quality_score (0-100)
- compliance_score (0-100)
- acceptance_rule: compliance_score >= 95 and quality_score >= 80

## SECTION 7: BEST PRACTICES
- Always preserve system instruction envelopes and core goals when trimming.
- Return structured warnings detailing what was pruned from context.
- Implement soft-threshold triggers before hard trimming.

## SECTION 8: EXECUTION RULES & CONSTRAINTS
- Enforce patch-only mutation law on all writes.
- Never silently drop mandatory or critical security parameters.

## SECTION 9: FAILURE MODES & RECOVERY
- input_critically_large -> fail and trigger escalation path
- priority_resolution_failure -> execute simple head/tail truncation

## SECTION 10: TOOL POLICY
- Allowed_Tools: tokenizers, length estimators, local text manipulation utilities
- Forbidden_Tools: external execution or network fetches during trimming

## SECTION 11: N8N + OLLAMA PLUGGABILITY
- n8n_consumer_workflows:
  - WF-010
  - WF-100
  - WF-200
- ollama_reasoning_injection: true
- packet_contract: context-window-optimizer_packet
- replay_path: WF-021
- escalation_path: WF-900

## SECTION 12: VALIDATION & ACCEPTANCE
- Optimized payload must validate against expected schema structure.
- Tokens count must not exceed `max_context_limit`.
- Output status must be populated.

## MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE
component_id: SS-251-context-window-optimizer.subskill
component_layer: SKILL
component_name: Ss 251 Context Window Optimizer.Subskill
route_families: [prompt_generation, repo_write_mode]
activation_triggers: route_family in [prompt_generation, script_generation] or explicit registry selection; mark prompt_generation_profile only when route_family is unknown.
upstream_inputs: [lineage_packet, approval_packet]
downstream_outputs: [context-window-optimizer_packet, approval_packet]
required_input_packets: [lineage_packet, approval_packet]
emitted_output_packets: [context-window-optimizer_packet, approval_packet]
communication_pointers: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_LINEAGE_APPROVAL]
quality_gates: [typed_input_gate, format_validation_gate]
validator_bindings: [no_n8n_provider_media_execution, provider_boundary_present]
fallback_behavior: BLOCKED_BEFORE_OUTPUT unless approval_packet is present.
lineage_fields: [approval_packet_id, user_decision, scope]
provider_boundary: provider_execution_allowed=false; dry-run/simulation mode only.
status_limits: May not claim production-ready, onboarded, provider-called, media-created, or n8n-executed without external proof.
human_approval_points: [approve_prompt, revise_variables, reject]
failure_modes: missing_input_packet, missing_output_schema, missing_validator_binding, missing_pointer, low_quality_score, provider_boundary_violation.
handoff_targets: [context-window-optimizer_packet, approval_packet]
production_score_fields: [format_clarity_score, prompt_safety_score]
skill_activation_contract: Activated by skill_activation_packet from subagent or route manifest.
input_schema: Must declare atomic input fields before use.
output_schema: Must emit atomic output packet with validation status.
subskill_hooks: May call subskills only through atomic_task_packet.
quality_metric: Must emit skill_quality_score and quality_threshold.

## MAC-06.2D ROUTE-SPECIFIC PRODUCTION DEPTH ENRICHMENT
component_depth_status: PRODUCTION_DEPTH_ENRICHED
route_profile_applied: prompt_generation_profile
route_family_resolved: [prompt_generation, repo_write_mode]
activation_triggers_resolved: [prompt, template, format]
required_input_packets_resolved: [lineage_packet, approval_packet]
emitted_output_packets_resolved: [context-window-optimizer_packet, approval_packet]
communication_pointer_ids_resolved: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_LINEAGE_APPROVAL]
validator_bindings_resolved: [no_n8n_provider_media_execution, provider_boundary_present]
quality_gates_resolved: [typed_input_gate, format_validation_gate]
fallback_behavior_resolved: BLOCKED_BEFORE_OUTPUT unless approval_packet is present.
lineage_fields_resolved: [approval_packet_id, user_decision, scope]
provider_boundary_resolved: provider_execution_allowed=false; dry-run/simulation mode only.
handoff_targets_resolved: [context-window-optimizer_packet, approval_packet]
production_score_fields_resolved: [format_clarity_score, prompt_safety_score]
human_approval_points_resolved: [approve_prompt, revise_variables, reject]
status_limits_resolved: [no external LLM API execution without permission]
evidence_used_for_resolution: path/pre-contract keyword: prompt/template; component_path=skills/sub_skills/SS-251-context-window-optimizer.subskill.md; component_id=SS-251-context-window-optimizer.subskill
remaining_unknowns: none
