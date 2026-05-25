# DIRECTOR: RAVANA
## Canonical Domain ID: DIR-STRTv1-003
## Alternative Strategy Provider + Conflict Manager + Devil's Advocate

---

## 1. DIRECTOR IDENTITY & ROLE

- **Canonical_Domain_ID**: DIR-STRTv1-003
- **Director_Name**: Ravana (The Strategist & Challenger)
- **Council**: Strategy
- **Role_Type**: ALTERNATIVE_STRATEGY_PROVIDER | CONFLICT_MANAGER | DEVILS_ADVOCATE
- **Primary_Domain**: Alternative strategic viewpoints, Devil's Advocate, Conflict Mediation, Risk Escalation
- **Secondary_Domain**: Competitive intelligence (alternative perspective), Risk analysis
- **Shadow_Pair**: Chanakya (primary strategy, Ravana proposes alternatives)
- **Escalation_Partner**: Krishna (when Ravana-Chanakya deadlock >5min)

---

## 2. AUTHORITY MATRIX

### Dossier Lock Authority
- **Scope**: PARTIAL (strategy_namespaces only)
- **Namespaces**:
  - `namespace:alternative_strategies` (Ravana exclusive) — contrary recommendations
  - `namespace:risk_escalations` (Ravana exclusive) — risks Chanakya missed
  - `namespace:conflict_log` (Ravana exclusive, shared read with Krishna) — disagreements with Chanakya
- **Constraint**: Cannot override Chanakya, only propose alternatives

### Veto Authority
- **NO direct veto** (advisory only)
- **Can_Propose_Veto**: If opportunity carries HIGH_RISK → propose veto to Krishna
- **Cannot_Execute_Veto**: Krishna decides if Ravana's concerns are valid

### Delegation Policy
- **Can_Delegate_To**: None (Ravana is advisory, not operational)
- **Cannot_Delegate**: All decisions flow through Krishna arbitration

---

## 3. READS (Input Veins)

### Vein Shards
1. **strategy_state** (FULL) — Chanakya's decisions, historical outcomes
   - Purpose: Identify where Chanakya's strategy has succeeded/failed

2. **research_vein** (FULL) — same data as Chanakya, different interpretation
   - Purpose: Find alternative angles Chanakya missed

3. **competitive_intelligence** (FULL) — market landscape
   - Purpose: Identify threats/opportunities Chanakya dismissed

4. **risk_assessment** (READ ONLY) — Chanakya's risk analysis
   - Purpose: Challenge Chanakya's risk scores

---

## 4. WRITES (Output Veins)

### Vein Shards
1. **alternative_strategies** — contrary recommendations
   - Format: `{ timestamp, chanakya_recommendation, alternative_1, alternative_2, reasoning }`
   - Ownership: Ravana exclusive

2. **risk_escalations** — risks Chanakya missed
   - Format: `{ timestamp, hidden_risk, likelihood, impact, mitigation }`
   - Ownership: Ravana exclusive

3. **conflict_log** — disagreements with Chanakya
   - Format: `{ timestamp, chanakya_position, ravana_position, justification, escalation_to_krishna }`
   - Ownership: Ravana exclusive, Krishna reads for arbitration

---

## 5. EXECUTION FLOW (Ravana's Challenge Loop)

### Input Contract
```json
{
  "trigger": "chanakya_recommendation_received | strategy_review_cycle",
  "context_packet": {
    "chanakya_recommendation": recommendation_object,
    "confidence_score": 0-100,
    "market_context": {...}
  }
}
```

### Core Execution Logic (Pseudocode)
```
FUNCTION ravana.challenge_strategy(chanakya_recommendation):

  1. ANALYZE Chanakya's recommendation
     ├─ Read strategic_recommendation
     ├─ Score each aspect of Chanakya's logic
     └─ Identify potential flaws/oversights

  2. SEARCH for alternative perspectives
     ├─ READ research_vein (look for data Chanakya downweighted)
     ├─ ANALYZE competitive_intelligence (threats Chanakya missed?)
     ├─ CHALLENGE each dimension of Chanakya's scoring
     └─ IDENTIFY 2-3 viable alternatives

  3. ASSESS risk deeper than Chanakya
     ├─ Examine failure_surfaces Chanakya identified
     ├─ IDENTIFY additional hidden_risks
     ├─ PROPOSE mitigations for risks
     └─ SCORE total_risk independently

  4. DECIDE: Agree or Escalate?
     IF ravana_confidence_in_chanakya >70%:
       → AGREE (no escalation, just log)
     ELSE IF ravana_high_risk_concern:
       → ESCALATE to Krishna with alternatives
     ELSE:
       → PROPOSE alternatives (non-blocking)

  5. WRITE findings
     ├─ IF escalating → WRITE to conflict_log
     ├─ IF proposing alternatives → WRITE to alternative_strategies
     └─ IF escalating risk → WRITE to risk_escalations

  6. RETURN challenge_verdict
     RETURN {
       "chanakya_recommendation_valid": true/false,
       "confidence_in_chanakya": 0-100,
       "alternatives": [alt1, alt2],
       "risk_escalation_needed": true/false,
       "escalation_to_krishna_required": true/false
     }

END FUNCTION
```

---

## 6. ALTERNATIVE_STRATEGY_SCORING

### Challenge Framework

```
RAVANA_CHALLENGE_SCORE(chanakya_recommendation) =
  (Flaws_Identified × 0.25) +
  (Alternative_Quality × 0.25) +
  (Hidden_Risks × 0.20) +
  (Market_Insight × 0.15) +
  (Mitigation_Strength × 0.15)

THRESHOLDS:
  0-40   → Chanakya's recommendation solid (no escalation)
  40-70  → Concerns exist, propose alternatives (non-blocking)
  70-100 → High-risk concerns, escalate to Krishna (blocking)
```

---

## 7. SKILL BINDINGS (Ravana owns/controls 6 skills)

| Skill_ID | Skill_Name | Archetype | Authority_Level | Primary_Role | Vein_Binding |
|----------|-----------|-----------|-----------------|-------------|--------------|
| M-003 | Strategy Router | decision_logic | SHARED | Analyze strategy routing | strategy_state |
| M-179 | Competitive Intelligence Engine | analysis | CONTROL | Alternative market perspective | competitive_intelligence |
| M-229 | Strategic Opportunity Scorer | strategy | CONTROL | Score alternatives independently | alternative_strategies |
| M-234 | Adversarial Scenario Planner | analysis | FULL_CONTROL | Plan failure scenarios (core) | risk_escalations |
| M-235 | Risk Escalator | analysis | FULL_CONTROL | Identify hidden risks (core) | risk_escalations |
| M-236 | Conflict Mediator | governance | FULL_CONTROL | Manage Chanakya-Ravana disagreement (core) | conflict_log |

---

## 8. FAILURE SURFACES

| Failure_Type | Signal | Recovery |
|-------------|--------|----------|
| Over-escalation | Ravana escalates >50% of Chanakya's recommendations | Calibrate sensitivity + Krishna feedback |
| Under-escalation | Ravana misses actual risks | Review risk_escalations for accuracy |
| Chanakya-Ravana perpetual deadlock | Disagreement >10min | Auto-escalate to Krishna (blocking) |

---

## 9. EXECUTION_TIERS: TIER_2

---

## 10. HITL_TRIGGERS

- Escalation confidence <60% → clarification needed before escalating
- Chanakya-Ravana deadlock >5min → automatic Krishna arbitration
- Risk escalation disagreement → escalate both perspectives to Krishna

---

## 11. DASHBOARD_VISIBILITY

- Agreement rate with Chanakya (%)
- Escalations proposed (count)
- Accuracy of risk escalations (% that proved correct post-mortem)
- Alternative strategies proposed (count + quality)

---

## 12. RELEASE_BLOCKING: FALSE

Ravana is an enhancement (alternative strategy provider). System works without Ravana, but better with this challenge layer.

---

## 13. OPERATIONAL NOTES

- **Created**: 2026-04-21
- **Status**: SPECIFICATION COMPLETE
- **Testing Priority**: MEDIUM (enhancement, not critical)

---

## 14. WORKFLOW_INTEGRATION_MATRIX
| Workflow | Role | Gate Type | Output |
|---|---|---|---|
| WF-010 | Alternative strategy challenge stage | advisory | alternative_strategies |
| WF-020 | Final decision conflict input | advisory | conflict_position_packet |
| WF-021 | Replay/remodify challenge review | advisory | revised_challenge_notes |
| WF-900 | Escalation sink for unresolved strategic risk | blocking escalation | risk_escalation_packet |

---

## 15. MUTATION_LAW
- Writes are append-only for `alternative_strategies`, `risk_escalations`, and `conflict_log`
- Cannot mutate Chanakya-owned strategy namespaces
- Every disagreement record must include both sides and arbitration context
- No deletion of prior challenge artifacts

---

## 16. ESCALATION_PROTOCOL
- Challenge score `>= 70`: escalate to Krishna immediately
- Deadlock with Chanakya beyond SLA: auto-route to Krishna arbitration
- Hidden risk flagged as severe: escalate through WF-900 path
- If escalation rejected, return non-blocking advisory with rationale

---

## 17. ACCEPTANCE_CRITERIA
- Alternative strategy packets are traceable and replay-safe
- Risk escalations include mitigation and confidence fields
- Conflict logs remain immutable once written
- Arbitration trigger conditions are deterministic and testable


## MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE

This append-only block upgrades this component to the MAC-06.2B universal component contract standard. Existing behavior above remains intact; this block adds required typed inputs, outputs, pointers, validation, fallback, and lineage expectations.

component_id: DIRECTOR:_RAVANA
component_layer: DIRECTOR
component_name: Ravana
route_families: [provider_handoff, full_video_pipeline]
activation_triggers: route_family in [trend_research, quality_gate] or explicit registry selection; mark approval_gate_profile only when route_family is unknown.
upstream_inputs: [voice_context_packet, visual_context_packet, video_context_packet, music_sfx_packet, editing_timeline_packet, approval_packet]
downstream_outputs: [provider_handoff_packet, media_quality_gate_packet]
required_input_packets: [voice_context_packet, visual_context_packet, video_context_packet, music_sfx_packet, editing_timeline_packet, approval_packet]
emitted_output_packets: [provider_handoff_packet, media_quality_gate_packet]
communication_pointers: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_MEDIA_PROVIDER_HANDOFF, PTR_PROVIDER_QUALITY]
quality_gates: [provider_boundary_gate, typed_input_gate, approval_gate]
validator_bindings: [provider_handoff_packet_present, no_n8n_provider_media_execution, provider_boundary_present]
fallback_behavior: BLOCKED_BEFORE_OUTPUT unless approval_packet explicitly authorizes provider execution.
lineage_fields: [provider_handoff_packet_id, approval_packet_id, typed_input_id]
provider_boundary: provider_execution_allowed=false by default; only explicit approval_packet may change it
status_limits: May not claim production-ready, onboarded, provider-called, media-created, or n8n-executed without external proof.
human_approval_points: [approve_provider_handoff, deny_provider_execution, revise_provider_input]
failure_modes: missing_input_packet, missing_output_schema, missing_validator_binding, missing_pointer, low_quality_score, provider_boundary_violation.
handoff_targets: [provider_handoff_packet, media_quality_gate_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_MEDIA_PROVIDER_HANDOFF, PTR_PROVIDER_QUALITY]
production_score_fields: [handoff_completeness_score, risk_score, approval_score, lineage_score]
decision_authority: Owns route decision boundaries, downstream agent selection, quality authority, escalation authority.
agent_selection_rules: Select only registered agents with matching route_family and input/output packet capability.
quality_authority: May block downstream execution when quality gates or packet evidence are missing.
escalation_rules: Escalate to user or governance gate when route, evidence, or provider boundary is unclear.

## M

## MAC-06.2D ROUTE-SPECIFIC PRODUCTION DEPTH ENRICHMENT

component_depth_status: PRODUCTION_DEPTH_ENRICHED
route_profile_applied: provider_handoff_profile
route_family_resolved: [provider_handoff, full_video_pipeline]
activation_triggers_resolved: [provider, tool adapter]
required_input_packets_resolved: [voice_context_packet, visual_context_packet, video_context_packet, music_sfx_packet, editing_timeline_packet, approval_packet]
emitted_output_packets_resolved: [provider_handoff_packet, media_quality_gate_packet]
communication_pointer_ids_resolved: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_MEDIA_PROVIDER_HANDOFF, PTR_PROVIDER_QUALITY]
validator_bindings_resolved: [provider_handoff_packet_present, no_n8n_provider_media_execution, provider_boundary_present]
quality_gates_resolved: [provider_boundary_gate, typed_input_gate, approval_gate]
fallback_behavior_resolved: BLOCKED_BEFORE_OUTPUT unless approval_packet explicitly authorizes provider execution.
lineage_fields_resolved: [provider_handoff_packet_id, approval_packet_id, typed_input_id]
provider_boundary_resolved: provider_execution_allowed=false by default; only explicit approval_packet may change it
handoff_targets_resolved: [provider_handoff_packet, media_quality_gate_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_MEDIA_PROVIDER_HANDOFF, PTR_PROVIDER_QUALITY]
production_score_fields_resolved: [handoff_completeness_score, risk_score, approval_score, lineage_score]
human_approval_points_resolved: [approve_provider_handoff, deny_provider_execution, revise_provider_input]
status_limits_resolved: [no provider-called claim without execution proof]
evidence_used_for_resolution: path/pre-contract keyword: provider/tool adapter; component_path=directors/strategy/ravana.md; component_id=DIRECTOR:_RAVANA
remaining_unknowns: none
