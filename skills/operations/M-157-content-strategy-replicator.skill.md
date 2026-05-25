# M-157 Content Strategy Replicator

## 1. Skill Identity
- Skill ID: M-157
- Skill Name: Content Strategy Replicator
- Vein Assignment: script_vein
- Phase Assignment: PHASE_2D_EXPANSION
- Owner Director: Kubera
- Strategic Authority Director: Shakti
- Upstream Dependencies: M-156
- Downstream Consumers: M-158
- Escalation Path: WF-900
- Replay Path: WF-021

## 2. Purpose
Deliver deterministic content strategy replicator outputs for governed workflow progression without dossier overwrite behavior.

## 3. DNA Injection
- Apply deterministic-first execution behavior.
- Preserve packet lineage continuity for replay and audit.
- Enforce governance escalation routing to WF-900 for contract failures.
- Enforce replay/remodify routing to WF-021 when rejection or remodify is requested.

## 4. Workflow Injection
- Producer Workflow: CWF-240
- Next Workflow Hint: WF-020
- Runtime Contract: skill_loader -> packet_validator -> dossier_writer -> packet_index_writer

## 5. Inputs
- Required Inputs:
  - dossier_id
  - route_id
  - execution_context
  - upstream_packet_refs
- Optional Inputs:
  - replay_context
  - operator_notes
  - quality_override_flags

## 6. Execution Logic
1. Resolve skill registry row for M-157 and validate deterministic runtime prerequisites.
2. Load dossier namespace target dossier.script_vein.content_strategy_replicator with append-only write intent.
3. A. Validate required inputs are present and type-safe.
   B. Route missing-input failures to WF-900 with rejection metadata.
4. Resolve upstream lineage references and verify packet integrity before transformation.
5. Execute deterministic transformation graph for content_strategy_replicator.
6. A. Compute quality, governance, and confidence checks.
   B. Fail fast to WF-900 if any hard gate is violated.
7. Build typed output packet m157_packet with schema version lock.
8. Validate packet envelope and payload against schemas/packets/m157_packet.schema.json.
9. Append mutation to dossier target and append row to se_packet_index (no overwrite).
10. Emit completion state with next-workflow recommendation and replay-safe metadata.

## 7. Outputs
- Output Packet Family: m157_packet
- JSON Schema Reference: schemas/packets/m157_packet.schema.json
- Dossier Write Target: dossier.script_vein.content_strategy_replicator
- se_packet_index Registration: REQUIRED for every emitted packet instance.

## 8. Governance
- Error Escalation Workflow: WF-900
- Replay Workflow: WF-021
- Required Mutation Metadata:
  - timestamp
  - writer_id
  - skill_id
  - instance_id
  - schema_version
  - lineage_reference
  - audit_entry

## 9. Tool/Runtime Usage
- Allowed Runtime Components:
  - engine/skill_loader/skill_loader.js
  - engine/packets/packet_validator.js
  - engine/dossier/dossier_writer.js
  - engine/packets/packet_index_writer.js
- Forbidden Runtime Behavior:
  - untyped packet emission
  - non-deterministic branching without contract gates
  - bypassing WF-900 error routing

## 10. Mutation Law
- Allowed Mutations:
  - append_to_array
  - create_new_packet
  - create_new_index_row
  - append_audit_entry
- Forbidden Mutations:
  - overwrite existing dossier fields
  - replace arrays
  - delete prior data
  - mutate historical packets
  - mutate historical approval decisions
  - mutate existing se_packet_index rows

## 11. Best Practices
1. Keep execution deterministic and idempotent within the same input contract.
2. Never emit packets before schema validation passes.
3. Preserve lineage references for replay and audit.
4. Use append-only writes for dossier and packet index.
5. Route all unrecoverable errors to WF-900.
6. Route replay/remodify actions to WF-021.
7. Keep owner and strategic director references registry-valid.
8. Keep workflow routing metadata consistent with workflow_bindings.yaml.
9. Avoid destructive mutation keywords in runtime operations.
10. Preserve schema version in every output packet.
11. Maintain explicit input validation and failure reasons.
12. Record audit entries for every mutation event.

## 12. Validation/Done
- TEST-M-157-001: Deterministic contract case 001 passes with WF-900/WF-021 governance preserved.
- TEST-M-157-002: Deterministic contract case 002 passes with WF-900/WF-021 governance preserved.
- TEST-M-157-003: Deterministic contract case 003 passes with WF-900/WF-021 governance preserved.
- TEST-M-157-004: Deterministic contract case 004 passes with WF-900/WF-021 governance preserved.
- TEST-M-157-005: Deterministic contract case 005 passes with WF-900/WF-021 governance preserved.
- TEST-M-157-006: Deterministic contract case 006 passes with WF-900/WF-021 governance preserved.
- TEST-M-157-007: Deterministic contract case 007 passes with WF-900/WF-021 governance preserved.
- TEST-M-157-008: Deterministic contract case 008 passes with WF-900/WF-021 governance preserved.
- TEST-M-157-009: Deterministic contract case 009 passes with WF-900/WF-021 governance preserved.
- TEST-M-157-010: Deterministic contract case 010 passes with WF-900/WF-021 governance preserved.
- TEST-M-157-011: Deterministic contract case 011 passes with WF-900/WF-021 governance preserved.
- TEST-M-157-012: Deterministic contract case 012 passes with WF-900/WF-021 governance preserved.
- TEST-M-157-013: Deterministic contract case 013 passes with WF-900/WF-021 governance preserved.
- TEST-M-157-014: Deterministic contract case 014 passes with WF-900/WF-021 governance preserved.
- TEST-M-157-015: Deterministic contract case 015 passes with WF-900/WF-021 governance preserved.
- TEST-M-157-016: Deterministic contract case 016 passes with WF-900/WF-021 governance preserved.
- TEST-M-157-017: Deterministic contract case 017 passes with WF-900/WF-021 governance preserved.
- TEST-M-157-018: Deterministic contract case 018 passes with WF-900/WF-021 governance preserved.

Acceptance Criteria:
- 12-section template preserved in exact order.
- 18+ deterministic tests defined.
- WF-900 escalation path explicitly declared.
- WF-021 replay path explicitly declared.
- Output packet is schema-bound and append-only dossier mutation law is enforced.

## MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE

This append-only block upgrades this component to the MAC-06.2B universal component contract standard. Existing behavior above remains intact; this block adds required typed inputs, outputs, pointers, validation, fallback, and lineage expectations.

component_id: M-157_Content_Strategy_Replicator
component_layer: SKILL
component_name: M 157 Content Strategy Replicator.Skill
route_families: [lineage_summary, approval_gate]
activation_triggers: route_family in [script_generation, quality_gate, lineage_summary] or explicit registry selection; mark approval_gate_profile only when route_family is unknown.
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
input_schema: Must declare atomic input fields before use; approval_gate_profile if absent upstream.
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
evidence_used_for_resolution: path/pre-contract keyword: lineage/trace; component_path=skills/operations/M-157-content-strategy-replicator.skill.md; component_id=M-157_Content_Strategy_Replicator
remaining_unknowns: none
