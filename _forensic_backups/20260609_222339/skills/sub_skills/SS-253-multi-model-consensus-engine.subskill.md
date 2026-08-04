# SUBSKILL SS-253 - Multi-Model Consensus Engine

## SECTION 1: SKILL IDENTITY & OWNERSHIP
- Skill_ID: SS-253
- Canonical_Name: Multi-Model Consensus Engine
- Archetype: integration
- Role_Type: PRIMARY_ROLE
- Owner_Director: Ganesha
- Domain: Model Alignment & Consensus

## SECTION 2: AUTHORITY MATRIX
- Can_Execute: response comparison, contradiction mapping, agreement scoring, schema alignment
- Cannot_Execute: model parameter override, model selection override, policy bypass
- Requires_Approval: premium multi-route evaluation criteria updates
- Escalation_Required: absolute split consensus (no majority matching)
- Veto_Authority: NO

## SECTION 3: READS (INPUT VEINS)
### 3.1 Primary Inputs
- dossier_id:string
- candidate_responses:array
- evaluation_criteria:object

### 3.2 Provider Context
  - gemini_provider
  - openrouter_api
  - ollama_local

## SECTION 4: WRITES (OUTPUT VEINS)
- artifact_family:multi-model-consensus-engine_packet
- aligned_response:string
- consensus_score:number
- status:success|failed|degraded
- write_target: dossier.prompt_intelligence.multi-model-consensus-engine (append_only)
- write_target: se_packet_index (append_only)

## SECTION 5: EXECUTION FLOW & ALGORITHM
1. Validate required fields (`dossier_id`, `candidate_responses`).
2. Align candidate response formats to a standard schema.
3. Compare responses against evaluation criteria and score mutual similarity/overlap.
4. Select the candidate response with the highest consensus score.
5. Emitted consensus packet, append dossier patch, and escalate if consensus is critically low.

## SECTION 6: SCORING FRAMEWORK
- quality_score (0-100)
- compliance_score (0-100)
- acceptance_rule: compliance_score >= 95 and quality_score >= 80

## SECTION 7: BEST PRACTICES
- Evaluate semantic consensus, not just exact character matches.
- Log individual model performance metrics in consensus metadata.
- Track consensus drift over repeated invocations.

## SECTION 8: EXECUTION RULES & CONSTRAINTS
- Enforce patch-only mutation law on all writes.
- Minimum consensus score threshold is 0.70.

## SECTION 9: FAILURE MODES & RECOVERY
- split_consensus -> degrade status, output fallback primary response with warnings
- empty_candidates_list -> fail and trigger escalation path

## SECTION 10: TOOL POLICY
- Allowed_Tools: text similarity metrics, fuzzy string matching, schema checkers
- Forbidden_Tools: external execution or network fetches during consensus evaluation

## SECTION 11: N8N + OLLAMA PLUGGABILITY
- n8n_consumer_workflows:
  - WF-010
  - WF-100
  - WF-200
- ollama_reasoning_injection: true
- packet_contract: multi-model-consensus-engine_packet
- replay_path: WF-021
- escalation_path: WF-900

## SECTION 12: VALIDATION & ACCEPTANCE
- Consensus output must have aligned schema format.
- Similarity scores must be recorded.
- Output status must be populated.

## MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE
component_id: SS-253-multi-model-consensus-engine.subskill
component_layer: SKILL
component_name: Ss 253 Multi Model Consensus Engine.Subskill
route_families: [prompt_generation, repo_write_mode]
activation_triggers: route_family in [prompt_generation, script_generation] or explicit registry selection; mark prompt_generation_profile only when route_family is unknown.
upstream_inputs: [lineage_packet, approval_packet]
downstream_outputs: [multi-model-consensus-engine_packet, approval_packet]
required_input_packets: [lineage_packet, approval_packet]
emitted_output_packets: [multi-model-consensus-engine_packet, approval_packet]
communication_pointers: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_LINEAGE_APPROVAL]
quality_gates: [typed_input_gate, format_validation_gate]
validator_bindings: [no_n8n_provider_media_execution, provider_boundary_present]
fallback_behavior: BLOCKED_BEFORE_OUTPUT unless approval_packet is present.
lineage_fields: [approval_packet_id, user_decision, scope]
provider_boundary: provider_execution_allowed=false; dry-run/simulation mode only.
status_limits: May not claim production-ready, onboarded, provider-called, media-created, or n8n-executed without external proof.
human_approval_points: [approve_prompt, revise_variables, reject]
failure_modes: missing_input_packet, missing_output_schema, missing_validator_binding, missing_pointer, low_quality_score, provider_boundary_violation.
handoff_targets: [multi-model-consensus-engine_packet, approval_packet]
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
emitted_output_packets_resolved: [multi-model-consensus-engine_packet, approval_packet]
communication_pointer_ids_resolved: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_LINEAGE_APPROVAL]
validator_bindings_resolved: [no_n8n_provider_media_execution, provider_boundary_present]
quality_gates_resolved: [typed_input_gate, format_validation_gate]
fallback_behavior_resolved: BLOCKED_BEFORE_OUTPUT unless approval_packet is present.
lineage_fields_resolved: [approval_packet_id, user_decision, scope]
provider_boundary_resolved: provider_execution_allowed=false; dry-run/simulation mode only.
handoff_targets_resolved: [multi-model-consensus-engine_packet, approval_packet]
production_score_fields_resolved: [format_clarity_score, prompt_safety_score]
human_approval_points_resolved: [approve_prompt, revise_variables, reject]
status_limits_resolved: [no external LLM API execution without permission]
evidence_used_for_resolution: path/pre-contract keyword: prompt/template; component_path=skills/sub_skills/SS-253-multi-model-consensus-engine.subskill.md; component_id=SS-253-multi-model-consensus-engine.subskill
remaining_unknowns: none
