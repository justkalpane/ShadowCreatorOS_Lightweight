# SKILL DNA UPGRADE TEMPLATE

This template shows the exact structure for upgrading flat skill files to full DNA-injected skills.

## TEMPLATE STRUCTURE

Use this template for all remaining skill markdown files. Replace placeholders with actual values from the skill's role, dependencies, and manifest relationships.

```markdown
# SKL-PH1-[SKILL-NAME-UPPERCASE]

## 1. Skill Identity
- **Skill ID:** [M-XXX or S-XXX]
- **Skill Name:** [Full name from current file]
- **Version:** 1.0.0
- **Phase Scope:** PHASE_1_TOPIC_TO_SCRIPT
- **Classification:** github_source_of_truth
- **Owner Workflow:** SE-N8N-CWF-[workflow-id]-[workflow-name]
- **Consumer Workflows:** [list of workflows that consume this skill]
- **Vein/Route/Stage:** [discovery_vein|research_vein|narrative_vein] / topic_to_script / [Stage_B|Stage_C]

## 2. Purpose
[Existing ROLE text, expanded with context about downstream usage]

## 3. DNA Injection
- **Role Definition:** [one-line function descriptor]
- **DNA Archetype:** [Narada|Chanakya|Krishna|Vyasa|Saraswati|Durga|Chandra|etc]
- **Behavior Model:** [adjectives describing decision/execution style]
- **Operating Method:** [step1 → step2 → step3 → output]
- **Working Style:** [working approach descriptors]

## 4. Workflow Injection
- **Producer:** [which workflow produces input for this skill]
- **Direct Consumers:** [which workflows consume output from this skill]
- **Upstream Dependencies:** [which registries/files/packets must exist before this runs]
- **Downstream Handoff:** [what packet is emitted → which workflow/skill consumes it]
- **Escalation Path:** SE-N8N-WF-900 on [specific error type]
- **Fallback Path:** [what to do if primary execution path fails]
- **Replay Path:** SE-N8N-WF-021 if user requests [specific remodify condition]

## 5. Inputs
**Required:**
- `dossier_id` (string) — parent dossier identifier
- [other required inputs with types and descriptions]

**Optional:**
- [optional inputs with defaults]

## 6. Execution Logic
```
1. [High-level step 1]
2. [High-level step 2]
   a. [Sub-step a]
   b. [Sub-step b]
3. [Continue as needed]
4. Return [output packet type]
5. On error: escalate to WF-900
```

## 7. Outputs

**Primary Output Packet:**
```json
{
  "instance_id": "[PKT-PREFIX-timestamp]",
  "artifact_family": "[family name]",
  "schema_version": "1.0.0",
  "producer_workflow": "SE-N8N-CWF-XXX",
  "dossier_ref": "[dossier_id]",
  "created_at": "[ISO timestamp]",
  "status": "CREATED | PARTIAL | EMPTY",
  "payload": {
    [schema-specific fields]
  }
}
```

**Write Targets:**
- `dossier.[namespace].[field]` (patch-only append)
- `se_packet_index` (one row with file_path reference)

## 8. Governance
- **Director Binding:** [Director name] (owner), [other director] (strategic authority)
- **Veto Power:** [yes|no]
- **Approval Gate:** [yes with which director|none]
- **Policy Requirements:**
  - [Requirement 1]
  - [Requirement 2]

## 9. Tool / Runtime Usage

**Allowed:**
- [Tool/capability 1]
- [Tool/capability 2]

**Forbidden:**
- [Forbidden tool/capability 1]
- [Forbidden tool/capability 2]

## 10. Mutation Law

**Reads:**
- `dossier.[namespace].[fields]`
- [Registry files]
- [External sources if any]

**Writes:**
- `dossier.[namespace].[field]` (patch-only append, never overwrite)
- `se_packet_index` (one row)

**Forbidden Mutations:**
- Do NOT overwrite existing fields
- Do NOT mutate dossier identity fields
- Do NOT write to unauthorized namespaces

## 11. Best Practices
- [Best practice 1]
- [Best practice 2]
- [Handling of edge cases or partial data]

## 12. Validation / Done

**Acceptance Tests:**
- TEST-PH1-[SKL-ID]-001: [Test description]
- TEST-PH1-[SKL-ID]-002: [Test description]

**Done Criteria:**
- Packet schema matches family contract
- All outputs have proper types and structure
- Dossier patch is additive only
- se_packet_index row created with file_path
- Escalation to WF-900 works on critical error
```

## ARCHETYPE GUIDE

Use these DNA archetypes for skills (from director councils):

**Intelligence Gathering:**
- Narada — trend spotting, broad pattern recognition, signal discovery
- Chanakya — strategic analysis, evidence weighing, qualification logic
- Krishna — synthesis, orchestration, final decisions

**Research & Context:**
- Vyasa — narrative shaping, knowledge assembly, document building
- Saraswati — knowledge management, retrieval, graph building
- Durga — protection, risk assessment, safety checking

**Audience & Market:**
- Chandra — audience mood, demographic mapping, audience insights
- [Other specialists as needed]

## VEIN MAPPING

Skills belong to one of these veins:

- **discovery_vein:** M-001 through M-025 (topic intelligence)
- **qualification_vein:** M-016, M-023 (gatekeeping)
- **research_vein:** M-009 through M-022 (research synthesis)
- **narrative_vein:** S-201 through S-210 (script intelligence)

## NAMESPACE OWNERSHIP

Each skill should write to ONE primary dossier namespace:

- `dossier.discovery` — owned by discovery_vein skills (M-001 to M-024)
- `dossier.research` — owned by research synthesis skills (M-009 to M-022)
- `dossier.narrative` — owned by script intelligence skills (S-201 to S-210)
- `dossier.approval` — owned by approval workflow (WF-020)
- `dossier.runtime` — system metadata only

Do NOT write to namespaces you don't own.

## QUICK CHECKLIST FOR EACH SKILL

- [ ] Skill ID and name correct
- [ ] Producer/consumer workflows identified from manifests
- [ ] Upstream dependencies listed (from skill_registry, manifests)
- [ ] Output packet family named
- [ ] Governance owner (director) assigned
- [ ] Mutation law specifies only ONE namespace owner
- [ ] Escalation path to WF-900 defined
- [ ] Fallback behavior for partial/missing data defined
- [ ] Input/output schemas clear
- [ ] Test references follow pattern TEST-PH1-[SKL-ID]-NNN
- [ ] Best practices address edge cases

## MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE

This append-only block upgrades this component to the MAC-06.2B universal component contract standard. Existing behavior above remains intact; this block adds required typed inputs, outputs, pointers, validation, fallback, and lineage expectations.

component_id: SKILL_DNA_UPGRADE_TEMPLATE
component_layer: SKILL
component_name: Skill Dna Upgrade Template
route_families: [approval_gate, repo_write_mode]
activation_triggers: route_family in [script_generation, trend_research, topic_discovery] or explicit registry selection; mark provider_handoff_profile only when route_family is unknown.
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
input_schema: Must declare atomic input fields before use; provider_handoff_profile if absent upstream.
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
evidence_used_for_resolution: path/pre-contract keyword: approval/oauth; component_path=skills/SKILL_DNA_UPGRADE_TEMPLATE.md; component_id=SKILL_DNA_UPGRADE_TEMPLATE
remaining_unknowns: none
