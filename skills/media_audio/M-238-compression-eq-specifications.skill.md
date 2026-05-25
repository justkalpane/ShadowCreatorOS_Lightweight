# SKL-PH3C-M-238-COMPRESSION_EQ_SPECIFICATIONS

## 1. Skill Identity
- Skill ID: M-238
- Skill Name: Compression and EQ Specifications
- Legacy Alias (Compatibility): Compression & EQ Specification
- Alias Names: Compression & EQ Specification
- Vein Assignment: media_vein
- Phase Assignment: PHASE_3C_AUDIO
- Owner Director: Shiva
- Strategic Authority Director: Krishna

## 2. Purpose
Specify deterministic compression and EQ processing chain settings.

## 3. DNA Injection
- Archetype: Shiva (tonal and dynamics transformer)
- Behavior Model: deterministic, packet-typed, governance-bound, append-only
- Operating Pattern: ingest -> validate -> transform -> verify -> emit -> append -> route
- Operating Constraint: no randomization, no untyped packet emission, no destructive mutations

## 4. Workflow Injection
- Producer Workflow: CWF-430
- Consumer Workflows: CWF-430
- Upstream Dependencies: levels_optimization (from M-237), audio_characteristics
- Upstream Skill IDs: M-237
- Downstream Consumers: M-239 Reverb and Effects Designer
- Downstream Skill IDs: M-239
- Escalation Path: WF-900
- Replay Path: WF-021
- Fallback Mode: emit status PARTIAL only when optional inputs are missing and schema integrity is preserved

## 5. Inputs
**Required Inputs**
- dossier_id (string): target dossier identity
- route_id (string): active orchestration route
- instance_id (string): runtime execution instance
- workflow_context (object): workflow metadata and lineage envelope
- upstream_packets (array): packet set required by upstream dependencies
- governance_context (object): policy and mutation-law controls

**Optional Inputs**
- audio_environment_constraints (object): production environment and delivery constraints
- creator_brand_guidelines (object): brand and identity constraints
- prior_replay_packet (object): replay context from WF-021
- execution_hints (object): deterministic operator hints

## 6. Execution Logic
STEP 1: Validate input envelope and required fields against declared contract.
STEP 2: Resolve upstream packet lineage and dependency closure.
STEP 3: Load deterministic audio policy profile for Compression and EQ Specifications.
STEP 4: Build transformation frame.
  A. Normalize upstream specs and constraints.
  B. Apply deterministic audio sequencing and scoring rules.
  C. Preserve narrative and brand integrity boundaries.
STEP 5: Generate primary output payload field eq_curve_specs.
STEP 6: Generate bounded variants and ranking keys where applicable.
STEP 7: Run governance and safety checks.
  A. Validate schema and packet typing readiness.
  B. Validate append-only mutation compliance.
  C. Validate WF-900 and WF-021 routing completeness.
STEP 8: Assemble typed output packet compression_eq_packet.
STEP 9: Append packet to dossier.media_vein.compression_eq_specifications and append se_packet_index row.
STEP 10: Emit deterministic routing decision to M-239 or WF-900/WF-021.

## 7. Outputs
- Output Packet Family: m238_packet
- JSON Schema Reference: schemas/packets/m238_packet.schema.json
- Dossier Write Target: dossier.media_vein.compression_eq_specifications
- se_packet_index Registration: required append row with lineage and audit metadata

~~~json
{
  "instance_id": "M-238-[timestamp]-[instance]",
  "artifact_family": "compression_eq_packet",
  "schema_version": "1.0.0",
  "producer_workflow": "CWF-430",
  "dossier_ref": "[dossier_id]",
  "created_at": "[ISO-8601]",
  "status": "CREATED|PARTIAL|FAILED",
  "payload": {
    "skill_id": "M-238",
    "skill_name": "Compression and EQ Specifications",
    "primary_output": {
      "eq_curve_specs": "[artifact]"
    },
    "routing": {
      "on_success": "M-239",
      "on_error": "WF-900",
      "on_replay": "WF-021"
    }
  }
}
~~~

## 8. Governance
- Governance Owner: Shiva
- Strategic Authority: Krishna
- Approval Contract: deterministic execution, typed packets, append-only mutation enforcement
- Escalation Trigger Classes: validation failure, schema failure, lineage failure, mutation-law violation
- Mandatory Escalation Workflow: WF-900
- Replay or Remodify Workflow: WF-021

## 9. Tool/Runtime Usage
**Allowed**
- Deterministic audio analysis and transformation engines
- Registered schema validation
- Registry lookups (skill_registry.yaml, workflow_bindings.yaml, schema_registry.yaml, director_binding.yaml)
- Append-only dossier and packet-index writers

**Forbidden**
- Non-deterministic generation paths
- Randomized scoring or routing behavior
- Untyped packet emission
- Direct overwrite, delete, or replace mutation behavior
- Bypassing WF-900 or WF-021 obligations

## 10. Mutation Law
**Allowed Mutations**
- append_to_array
- create_new_packet
- create_new_index_row
- append_audit_entry

**Required Mutation Metadata**
- timestamp
- writer_id
- skill_id
- instance_id
- schema_version
- lineage_reference
- audit_entry

**Forbidden Mutations**
- overwrite existing dossier fields
- replace arrays
- delete prior data
- mutate historical packets
- mutate historical approval decisions
- mutate existing se_packet_index rows

## 11. Best Practices
- Keep all audio decisions deterministic and rule-based.
- Preserve lineage from script, video, and upstream audio packets into outputs.
- Enforce technical constraints before optimization and transformation.
- Validate accessibility and metadata contracts where applicable.
- Keep packet payloads schema-bound and typed.
- Route policy or validation failures to WF-900 immediately.
- Route replay and remodify requests to WF-021 with stable metadata.
- Keep dossier writes append-only under owned media namespace.
- Never overwrite historical packets or index rows.
- Keep downstream routing deterministic and registry-aligned.
- Record complete mutation metadata for every write.
- Keep alias naming in metadata for cross-section compatibility.

## 12. Validation/Done
**Test Cases**
- TEST-PH3C-M-238-001: Valid required inputs produce deterministic compression_eq_packet output
- TEST-PH3C-M-238-002: Missing dossier_id routes to WF-900 with explicit validation details
- TEST-PH3C-M-238-003: Missing route_id routes to WF-900 without packet emission
- TEST-PH3C-M-238-004: Missing required upstream packet fails closed and escalates to WF-900
- TEST-PH3C-M-238-005: Lineage references are preserved for all upstream dependencies
- TEST-PH3C-M-238-006: Primary output field eq_curve_specs is present and non-empty
- TEST-PH3C-M-238-007: Deterministic logic yields same output structure for identical input state
- TEST-PH3C-M-238-008: Schema validation rejects untyped payload prior to dossier mutation
- TEST-PH3C-M-238-009: Dossier writes target only dossier.media_vein.compression_eq_specifications
- TEST-PH3C-M-238-010: Mutation uses append_to_array and never overwrites prior data
- TEST-PH3C-M-238-011: se_packet_index append row includes lineage_reference and instance_id
- TEST-PH3C-M-238-012: Replay branch routes to WF-021 for remodify requests
- TEST-PH3C-M-238-013: Escalation branch routes to WF-900 for validation or policy failures
- TEST-PH3C-M-238-014: Output packet includes timestamp, writer_id, skill_id, instance_id, schema_version
- TEST-PH3C-M-238-015: Forbidden mutation attempt is blocked and audited
- TEST-PH3C-M-238-016: Downstream routing hints are registry-bound and deterministic
- TEST-PH3C-M-238-017: Audit entry includes operation, route_id, source packet, and confidence markers
- TEST-PH3C-M-238-018: Acceptance gate fails closed when governance metadata is incomplete

**Acceptance Criteria**
- All 12 required sections are present in exact order.
- Execution logic has at least 10 deterministic steps.
- Output packet family is typed and schema-bound.
- Dossier mutation is append-only and restricted to dossier.media_vein namespace.
- se_packet_index append row includes full lineage metadata.
- Escalation path WF-900 and replay path WF-021 are explicitly wired.
- Minimum 18 tests are defined and traceable to requirements.
- Upstream and downstream contract references are complete and non-ambiguous.

## MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE

This append-only block upgrades this component to the MAC-06.2B universal component contract standard. Existing behavior above remains intact; this block adds required typed inputs, outputs, pointers, validation, fallback, and lineage expectations.

component_id: SKL-PH3C-M-238-COMPRESSION_EQ_SPECIFICATIONS
component_layer: SKILL
component_name: M 238 Compression Eq Specifications.Skill
route_families: [lineage_summary, approval_gate]
activation_triggers: route_family in [script_generation, music_sfx_context, avatar_video_context, lineage_summary] or explicit registry selection; mark lineage_profile only when route_family is unknown.
upstream_inputs: [media_quality_gate_packet, lineage_packet, approval_packet]
downstream_outputs: [lineage_packet, approval_packet]
required_input_packets: [media_quality_gate_packet, lineage_packet, approval_packet]
emitted_output_packets: [lineage_packet, approval_packet]
communication_pointers: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_QUALITY_LINEAGE, PTR_LINEAGE_APPROVAL]
quality_gates: [lineage_completeness_gate, decision_trace_gate, approval_options_gate]
validator_bindings: [lineage_approval_packet_present, segment_level_regeneration_actions_present, quality_scores_present]
fallback_behavior: NEEDS_HUMAN_REVIEW if upstream packet IDs or approval choices are missing.
lineage_fields: [upstream_packet_ids, downstream_packet_ids, decision_log, evidence_paths]
provider_boundary: provider_execution_allowed=false; approval may authorize future execution; default is no provider/media/n8n execution
status_limits: May not claim production-ready, onboarded, provider-called, media-created, or n8n-executed without external proof.
human_approval_points: [approve, revise_segment, regenerate_media, reject]
failure_modes: missing_input_packet, missing_output_schema, missing_validator_binding, missing_pointer, low_quality_score, provider_boundary_violation.
handoff_targets: [lineage_packet, approval_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_QUALITY_LINEAGE, PTR_LINEAGE_APPROVAL]
production_score_fields: [lineage_score, approval_clarity_score, risk_score]
skill_activation_contract: Activated by skill_activation_packet from subagent or route manifest.
input_schema: Must declare atomic input fields before use; lineage_profile if absent upstream.
output_schema: Must emit atomic output packet with evidence path and validation status.
subskill_hooks: May call subskills only through atomic_task_packet.
quality_metric: Must emit skill_quality_score and quality_threshold.

## M

## MAC-06.2D ROUTE-SPECIFIC PRODUCTION DEPTH ENRICHMENT

component_depth_status: PRODUCTION_DEPTH_ENRICHED
route_profile_applied: lineage_profile
route_family_resolved: [lineage_summary, approval_gate]
activation_triggers_resolved: [lineage, trace, decision log]
required_input_packets_resolved: [media_quality_gate_packet, lineage_packet, approval_packet]
emitted_output_packets_resolved: [lineage_packet, approval_packet]
communication_pointer_ids_resolved: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_QUALITY_LINEAGE, PTR_LINEAGE_APPROVAL]
validator_bindings_resolved: [lineage_approval_packet_present, segment_level_regeneration_actions_present, quality_scores_present]
quality_gates_resolved: [lineage_completeness_gate, decision_trace_gate, approval_options_gate]
fallback_behavior_resolved: NEEDS_HUMAN_REVIEW if upstream packet IDs or approval choices are missing.
lineage_fields_resolved: [upstream_packet_ids, downstream_packet_ids, decision_log, evidence_paths]
provider_boundary_resolved: provider_execution_allowed=false; approval may authorize future execution; default is no provider/media/n8n execution; approval_packet_required_for_any_execution
handoff_targets_resolved: [lineage_packet, approval_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_QUALITY_LINEAGE, PTR_LINEAGE_APPROVAL]
production_score_fields_resolved: [lineage_score, approval_clarity_score, risk_score]
human_approval_points_resolved: [approve, revise_segment, regenerate_media, reject]
status_limits_resolved: [no silent approval, no execution without explicit approval]
evidence_used_for_resolution: path/pre-contract keyword: lineage/trace; component_path=skills/media_audio/M-238-compression-eq-specifications.skill.md; component_id=SKL-PH3C-M-238-COMPRESSION_EQ_SPECIFICATIONS
remaining_unknowns: none
