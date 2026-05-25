# SKL-PH1-PLATFORM-FORMAT-SPECIALIST

## 1. Skill Identity
- **Skill ID:** P-302
- **Skill Name:** platform_format_specialist
- **Version:** 1.0.0
- **Phase Scope:** PHASE_1_TOPIC_TO_SCRIPT
- **Classification:** github_source_of_truth
- **Owner Workflow:** SE-N8N-CWF-320-Platform-Packager
- **Consumer Workflows:** CWF-330-Asset-Brief-Generator
- **Vein/Route/Stage:** context_engineering_vein / topic_to_script / Stage_D

## 2. Purpose
Runtime-ready canonical skill artifact for P-302 (platform_format_specialist). This specification follows repository DNA law and enforces deterministic execution, packet lineage, governance-safe escalation, and patch-only mutation discipline.

## 3. DNA Injection
- **Role Definition:** platform-format-specialist_executor
- **DNA Archetype:** Saraswati
- **Behavior Model:** deterministic, registry-bound, escalation-safe
- **Operating Method:** ingest -> validate -> execute -> emit -> index
- **Working Style:** evidence-first, schema-locked, replay-aware

## 4. Workflow Injection
- **Producer:** WF
- **Direct Consumers:** CWF-330-Asset-Brief-Generator
- **Upstream Dependencies:** workflow_registry, skill_loader_registry, dossier packet context
- **Downstream Handoff:** platform-format-specialist_packet -> downstream workflow chain
- **Escalation Path:** SE-N8N-WF-900 on validation failure or critical runtime errors
- **Fallback Path:** return partial packet with status "PARTIAL" and explicit failure reasons
- **Replay Path:** SE-N8N-WF-021 when remodify/replay is requested

## 5. Inputs
**Required:**
- dossier_id (string) - parent dossier identifier
- input_payload (object) - upstream packet payload for this skill
- route_id (string) - active route context

**Optional:**
- constraints (object) - quality/cost/latency constraints
- hints (array) - execution hints from upstream steps

## 6. Execution Logic
```text
1. Validate dossier_id and input_payload schema
2. Resolve runtime context and routing envelope
3. Execute core transformation logic for P-302
4. Apply deterministic validation checks
5. Emit packet and write additive dossier patch
6. Register packet in se_packet_index
7. On critical error: escalate to WF-900
```

## 7. Outputs

**Primary Output Packet:**
```json
{
  "instance_id": "P-302-[timestamp]",
  "artifact_family": "platform-format-specialist_packet",
  "schema_version": "1.0.0",
  "producer_workflow": "SE-N8N-CWF-320-Platform-Packager",
  "dossier_ref": "[dossier_id]",
  "created_at": "[ISO timestamp]",
  "status": "CREATED | PARTIAL | EMPTY",
  "payload": {
    "skill_id": "P-302",
    "skill_name": "platform_format_specialist",
    "result": {}
  }
}
```

**Write Targets:**
- dossier.context_engineering_vein.platform-format-specialist (append_to_array)
- se_packet_index (single index row)

## 8. Governance
- **Director Binding:** Saraswati (owner), Krishna (strategic authority)
- **Authority Level:** CONTROL (runtime execution), ADVISORY (policy)
- **Veto Power:** no
- **Approval Gate:** none unless downstream workflow requires explicit approval
- **Policy Requirements:**
  - Use patch-only mutation law
  - Never overwrite existing dossier fields
  - Maintain packet lineage and audit references

## 9. Tool / Runtime Usage

**Allowed:**
- deterministic transforms
- schema validation and packet shaping
- route-aware dossier patch appends

**Forbidden:**
- destructive mutations
- unauthorized namespace writes
- bypassing governance escalation paths

## 10. Mutation Law

**Reads:**
- dossier scoped context slices
- route/workflow registry contracts
- upstream packet payloads

**Writes:**
- dossier.context_engineering_vein.platform-format-specialist (append_only)
- se_packet_index row for packet traceability

**Forbidden Mutations:**
- overwrite of prior dossier values
- write to unrelated namespaces
- mutation without packet metadata

## 11. Best Practices
- Keep transformations deterministic and replay-safe
- Preserve source evidence/provenance in packet payload
- Emit explicit partial status on non-critical source gaps
- Keep escalation payload machine-readable for WF-900

## 12. Validation / Done

**Acceptance Tests:**
- TEST-PH1-P302-001: valid input produces CREATED packet
- TEST-PH1-P302-002: invalid input escalates to WF-900
- TEST-PH1-P302-003: dossier patch is additive only

**Done Criteria:**
- Output packet schema conforms to family contract
- Additive dossier patch applied with no overwrite
- se_packet_index row produced
- Replay path and escalation path are defined

## MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE

This append-only block upgrades this component to the MAC-06.2B universal component contract standard. Existing behavior above remains intact; this block adds required typed inputs, outputs, pointers, validation, fallback, and lineage expectations.

component_id: P-302-platform-format-specialist.skill
component_layer: SKILL
component_name: P 302 Platform Format Specialist.Skill
route_families: [context_engineering, script_generation]
activation_triggers: route_family in [script_generation, topic_discovery, editing_packaging, quality_gate] or explicit registry selection; mark lineage_profile only when route_family is unknown.
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
input_schema: Must declare atomic input fields before use; lineage_profile if absent upstream.
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
evidence_used_for_resolution: path/pre-contract keyword: context engineering; component_path=skills/context_engineering/P-302-platform-format-specialist.skill.md; component_id=P-302-platform-format-specialist.skill
remaining_unknowns: none
