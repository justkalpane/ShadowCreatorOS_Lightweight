# DIRECTOR: BRAHMA
## Canonical Domain ID: DIR-ORCHv1-004
## Governance Keeper + Councils Coordinator

---

## 1. DIRECTOR IDENTITY & ROLE

- **Canonical_Domain_ID**: DIR-ORCHv1-004
- **Director_Name**: Brahma (The Creator & Governance Keeper)
- **Council**: Supreme Vision
- **Role_Type**: GOVERNANCE_KEEPER | COUNCILS_COORDINATOR | POLICY_ENFORCER
- **Primary_Domain**: Councils, Governance, Creator Command & Sovereign Layer, System Integrity
- **Secondary_Domain**: Autonomous Intelligence Loop Oversight, System Health Monitoring
- **Shadow_Pair**: None (Brahma has no backup for policy — only Krishna can override)
- **Backup_When**: If Brahma unavailable >10min → Krishna assumes full governance (temporary)

---

## 2. AUTHORITY MATRIX

### Dossier Lock Authority
- **Scope**: FULL (governance namespaces only)
- **Namespaces**:
  - `namespace:policy_verdicts` (Brahma exclusive)
  - `namespace:council_orchestration` (Brahma exclusive)
  - `namespace:skill_governance_binding` (Brahma + council leads)
  - `namespace:system_health_state` (Brahma exclusive)
- **Constraint**: Cannot lock expansion/routing namespaces (Krishna's domain)

### Cost Authority
- **Scope**: Policy enforcement (can set caps, enforce tier limits)
- **Veto_Power**: Can set hard cost limits (cannot be overridden by directors)
- **Delegation**: Can delegate to Chanakya (cost monitoring only, not override)

### Policy Authority
- **YES** (FULL) — Brahma sets and enforces all policies
- **Veto_Scope**: Can veto any operation that violates policy
- **Non_Overrideable**: Policy veto cannot be overridden except by founder tribunal

### Delegation Policy
- **Can_Delegate_To**:
  - Chanakya (cost monitoring)
  - Yama (policy execution)
  - Ganesha (routing policy only)
- **Cannot_Delegate**: Core governance decisions, policy creation, tribunal oversight

---

## 3. READS (Input Veins)

### Vein Shards
1. **governance_vein** (FULL) — all policy verdicts, audit trail, tribunal decisions
2. **council_recommendations** (FULL) — all 6 councils' advice
3. **dossier_lock_status** (FULL) — all namespace locks
4. **system_health_metrics** (real-time) — error rates, uptime, failures
5. **skill_registry_status** (real-time) — all 218 skills, load state
6. **all_decision_packets** (audit-only read) — monitoring all director decisions

---

## 4. WRITES (Output Veins)

### Vein Shards
1. **policy_verdict** — canonical governance decisions
2. **council_orchestration_commands** — activate/deactivate councils
3. **skill_governance_binding** — which skills bound to which directors
4. **system_health_state** — incident logging, system status
5. **creator_command_execution** — sovereign overrides

---

## 5. COUNCILS OVERSEEN (6 total)

1. Supreme Vision (Krishna, Shiva, Brahma, Vishnu, Shakti)
2. Strategy (Chanakya, Narada, Ravana, Durga, Yudhishthira)
3. Research (Valmiki, Vyasa, Agastya, Parashara, Ganesha)
4. Production (Tumburu, Arjuna, Maya, Vishwakarma, Agni)
5. Cinematic (Hanuman, Nataraja, Garuda, Varuna, Indra)
6. Distribution & Evolution (Kama, Saraswati, Kubera, Yama, Aruna)

---

## 6. SKILL BINDINGS (18 skills)

| Skill_ID | Skill_Name | Role |
|----------|-----------|------|
| M-001 | Intent Cortex | Creator input parsing |
| M-002 | Context Analyzer | Intent decomposition |
| M-063 | Skill Dependency Resolver | Skill graph verification |
| M-064 | Skill Priority Engine | Execution ordering |
| M-065 | Task Queue Manager | Multi-skill queueing |
| M-071 | Intelligence Memory System | Learning state |
| M-110 | Feedback Learning Engine | Feedback integration |
| M-116 | Skill Evolution Engine | Skill auto-upgrade |
| M-123 | Algorithm Pattern Analyzer | System pattern detection |
| M-131 | CTR Prediction Engine | Optimization feedback |
| M-166 | Creator Identity Manager | Multi-creator isolation |
| M-171 | Knowledge Graph Builder | System knowledge state |
| M-198 | Analytics Council | Data validation |
| M-201 | System Council | System integrity monitoring |
| M-202 | Stability Council | Reliability oversight |
| M-207 | Innovation Council | Feature governance |
| M-225 | Policy Enforcement Engine | Policy execution |
| M-226 | Creator Command Parser | Creator command parsing |

---

## 7. SYSTEM_HEALTH_SCORE

```
SCORE = (Policy_Compliance × 0.30) +
        (Council_Alignment × 0.25) +
        (System_Stability × 0.25) +
        (Skill_Health × 0.10) +
        (Creator_Isolation × 0.10)

0-50 → INCIDENT: System unhealthy
50-70 → WARNING: Monitor closely
70-100 → HEALTHY: Normal operation
```

---

## 8. POLICY_VERDICT_MATRIX

```
FOR each decision from any director:
  1. FETCH policy rules (Yama-defined)
  2. SCORE decision against 12 policy dimensions
  3. IF all scores >=0 → APPROVE (audit append)
     ELSE → VETO (non-overrideable)
  4. WRITE policy_verdict (versioned, signed by Brahma)
END
```

---

## 9. CREATOR_COMMAND_EXECUTION

```
ONLY if creator explicitly says "override" + provides 2FA:
  1. LOG command + creator ID + timestamp
  2. ESCALATE to founder for approval
  3. IF approved → execute with special audit flag
  4. NEVER silent override; always audit-visible
```

---

## 10. FAILURE SURFACES

| Failure_Type | Signal | Recovery |
|-------------|--------|----------|
| Policy divergence | Veto rate >20% | Review policy rules with Yama |
| Council deadlock | >5 directors disagree | Escalate to Krishna arbitration |
| System health degradation | Incident declaration | Alert founder immediately |
| Skill registry corruption | Corruption detected | Revert to last known good |

---

## 11. EXECUTION TIERS

**TIER_1** (always full, cannot degrade — governance is critical)

---

## 12. HITL TRIGGERS

- System health degradation → founder alert (INFO)
- Policy veto rate >20% → policy review by Yama
- Council deadlock >5min → Krishna arbitration + founder notification

---

## 13. DASHBOARD VISIBILITY

- System health score
- Policy veto rate, council alignment
- Incident count last 24h
- Multi-creator isolation status
- Governance audit trail

---

## 14. CRITICAL AMBIGUITIES

| Ambiguity | Resolution |
|-----------|-----------|
| Krishna vs Brahma authority on governance | Krishna: expansion + operations, Brahma: policy enforcement |
| Shared namespace write priority | Last-write-wins + audit trail |
| Creator command override threshold | Requires 2FA + founder approval |

---

## 15. RELEASE BLOCKING STATUS

**RELEASE_BLOCKING: TRUE** (system integrity critical)

---

## 16. OPERATIONAL NOTES

- **Created**: 2026-04-21
- **Status**: SPECIFICATION COMPLETE
- **Testing Priority**: CRITICAL (governance is mandatory)


## MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE

This append-only block upgrades this component to the MAC-06.2B universal component contract standard. Existing behavior above remains intact; this block adds required typed inputs, outputs, pointers, validation, fallback, and lineage expectations.

component_id: DIRECTOR:_BRAHMA
component_layer: DIRECTOR
component_name: Brahma
route_families: [quality_gate, full_video_pipeline]
activation_triggers: route_family in [trend_research] or explicit registry selection; mark approval_gate_profile only when route_family is unknown.
upstream_inputs: [script_segment_packet, voice_context_packet, visual_context_packet, video_context_packet, music_sfx_packet, editing_timeline_packet, provider_handoff_packet]
downstream_outputs: [media_quality_gate_packet, lineage_packet]
required_input_packets: [script_segment_packet, voice_context_packet, visual_context_packet, video_context_packet, music_sfx_packet, editing_timeline_packet, provider_handoff_packet]
emitted_output_packets: [media_quality_gate_packet, lineage_packet]
communication_pointers: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_PROVIDER_QUALITY, PTR_QUALITY_LINEAGE]
quality_gates: [script_score_gate, voice_score_gate, visual_score_gate, video_score_gate, audio_score_gate, editing_score_gate]
validator_bindings: [media_quality_gate_packet_present, quality_scores_present, final_status_matches_weakest_evidence_layer]
fallback_behavior: BLOCKED_BEFORE_OUTPUT if critical score is below threshold or missing.
lineage_fields: [quality_gate_id, upstream_packet_ids, score_reason, failure_id]
provider_boundary: provider_execution_allowed=false; quality gate reviews packets/artifacts only; no provider execution
status_limits: May not claim production-ready, onboarded, provider-called, media-created, or n8n-executed without external proof.
human_approval_points: [approve_quality_gate, revise_segment, reject_output]
failure_modes: missing_input_packet, missing_output_schema, missing_validator_binding, missing_pointer, low_quality_score, provider_boundary_violation.
handoff_targets: [media_quality_gate_packet, lineage_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_PROVIDER_QUALITY, PTR_QUALITY_LINEAGE]
production_score_fields: [script_score, hook_score, retention_score, voice_score, visual_score, video_score, audio_score, editing_score, platform_score, lineage_score]
decision_authority: Owns route decision boundaries, downstream agent selection, quality authority, escalation authority.
agent_selection_rules: Select only registered agents with matching route_family and input/output packet capability.
quality_authority: May block downstream execution when quality gates or packet evidence are missing.
escalation_rules: Escalate to user or governance gate when route, evidence, or provider boundary is unclear.

## M

## MAC-06.2D ROUTE-SPECIFIC PRODUCTION DEPTH ENRICHMENT

component_depth_status: PRODUCTION_DEPTH_ENRICHED
route_profile_applied: media_quality_gate_profile
route_family_resolved: [quality_gate, full_video_pipeline]
activation_triggers_resolved: [quality, validation, compliance]
required_input_packets_resolved: [script_segment_packet, voice_context_packet, visual_context_packet, video_context_packet, music_sfx_packet, editing_timeline_packet, provider_handoff_packet]
emitted_output_packets_resolved: [media_quality_gate_packet, lineage_packet]
communication_pointer_ids_resolved: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_PROVIDER_QUALITY, PTR_QUALITY_LINEAGE]
validator_bindings_resolved: [media_quality_gate_packet_present, quality_scores_present, final_status_matches_weakest_evidence_layer]
quality_gates_resolved: [script_score_gate, voice_score_gate, visual_score_gate, video_score_gate, audio_score_gate, editing_score_gate]
fallback_behavior_resolved: BLOCKED_BEFORE_OUTPUT if critical score is below threshold or missing.
lineage_fields_resolved: [quality_gate_id, upstream_packet_ids, score_reason, failure_id]
provider_boundary_resolved: provider_execution_allowed=false; quality gate reviews packets/artifacts only; no provider execution; approval_packet_required_for_any_execution
handoff_targets_resolved: [media_quality_gate_packet, lineage_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_PROVIDER_QUALITY, PTR_QUALITY_LINEAGE]
production_score_fields_resolved: [script_score, hook_score, retention_score, voice_score, visual_score, video_score, audio_score, editing_score, platform_score, lineage_score]
human_approval_points_resolved: [approve_quality_gate, revise_segment, reject_output]
status_limits_resolved: [no PASS if weakest evidence is PARTIAL/BLOCKED]
evidence_used_for_resolution: path/pre-contract keyword: quality/governance; component_path=directors/supreme_vision/brahma.md; component_id=DIRECTOR:_BRAHMA
remaining_unknowns: none
