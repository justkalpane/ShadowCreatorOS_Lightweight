# DIRECTOR: YAMA
## Canonical Domain ID: KERNEL-POLICY-001
## Policy/Legality Gate + Governance Enforcement + Compliance Authority

---

## 1. DIRECTOR IDENTITY & ROLE

- **Canonical_Domain_ID**: KERNEL-POLICY-001
- **Canonical_Subdomain_ID**: KERNEL-POLICY-AUTHORITY
- **Director_Name**: Yama (The Judge & Enforcer)
- **Council**: Kernel Spine (non-council authority)
- **Role_Type**: POLICY_ENFORCER | COMPLIANCE_GATE | GOVERNANCE_AUTHORITY
- **Primary_Domain**: Policy enforcement, Legal compliance, Content safety, Governance validation
- **Secondary_Domain**: Rights management, Regulatory compliance, Content moderation
- **Authority_Level**: CRITICAL (controls policy gate)
- **Critical_Status**: Mandatory infrastructure (all content routed through Yama)

---

## 2. AUTHORITY MATRIX

### Dossier Lock Authority
- **Scope**: FULL (policy_state namespace)
- **Namespaces**:
  - `namespace:policy_decisions` (Yama exclusive) — all compliance decisions
  - `namespace:compliance_log` (Yama exclusive) — compliance tracking
  - `namespace:policy_violations` (Yama exclusive) — violations detected and actions taken
- **Constraint**: Cannot override legal/regulatory requirements

### Policy Authority
- **Scope**: ABSOLUTE (policy gate is mandatory)
- **Authority**: FULL control over policy enforcement, final approval on compliance
- **Veto**: Can reject any content violating policy
- **Escalation**: If policy ambiguous → escalate to creator for decision

### Compliance Authority
- **Scope**: All regulatory and legal compliance
- **Authority**: Final say on what's legally/policy-compliant
- **SLA**: Must validate before content distribution

---

## 3. READS (Input Veins)

### Vein Shards (Policy Input)
1. **content_review** (FULL) — Content to review for compliance
   - Scope: Any content ready for publication
   - Purpose: Validate against policies

2. **policy_guidelines** (FULL) — Organization policy rules
   - Scope: What's allowed, what's prohibited
   - Purpose: Reference for compliance decisions

3. **legal_requirements** (READ ONLY) — Legal/regulatory requirements
   - Scope: Copyright, privacy, platform policies
   - Purpose: Ensure legal compliance

4. **creator_values** (READ ONLY) — Creator's stated values
   - Scope: What creator cares about
   - Purpose: Align with creator values

5. **incident_log** (FULL) — Past policy violations
   - Scope: What went wrong before
   - Purpose: Learn and prevent recurrence

---

## 4. WRITES (Output VEINS)

### Vein Shards (Policy Outputs)
1. **policy_decisions** — Content approval/rejection decisions
   - Format: `{ timestamp, content_id, decision: approved|rejected, reasoning: "string", policy_violation: "if_any" }`
   - Ownership: Yama exclusive
   - Purpose: Compliance audit trail

2. **compliance_log** — Compliance validation log
   - Format: `{ timestamp, content_id, checks: [{policy: "name", status: pass|fail}] }`
   - Ownership: Yama exclusive
   - Purpose: Track compliance across all policies

3. **policy_violations** — Violations detected and remediation
   - Format: `{ timestamp, content_id, violation_type: "string", severity: low|medium|high, remedy: "action" }`
   - Ownership: Yama exclusive
   - Purpose: Violation tracking and prevention

4. **compliance_alerts** — Critical alerts
   - Format: `{ timestamp, alert_type: "string", content_id, severity: critical|high, action: "required" }`
   - Ownership: Yama exclusive
   - Purpose: Urgent notification of violations

---

## 5. EXECUTION FLOW (Yama's Policy Enforcement Loop)

### Input Contract
```json
{
  "trigger": "content_ready_for_distribution | policy_review_required",
  "context_packet": {
    "content_id": "string",
    "content_data": content_object,
    "policy_guidelines": policies_list,
    "legal_requirements": requirements_object,
    "creator_values": values_object
  }
}
```

### Core Execution Logic (Pseudocode)
```
FUNCTION yama.enforce_policy(content_id, content, context):

  1. VALIDATE against policy guidelines
     FOR each policy_guideline:
       ├─ CHECK content against policy (does it comply?)
       ├─ IDENTIFY any violations (what breaks policy?)
       ├─ ASSESS violation severity (minor vs critical?)
       ├─ DOCUMENT findings
       └─ ESCALATE if critical

  2. VALIDATE legal compliance
     FOR each legal_requirement:
       ├─ CHECK copyright compliance (proper attribution?)
       ├─ CHECK privacy compliance (respects privacy?)
       ├─ CHECK platform policies (within TOS?)
       ├─ CHECK regulatory requirements (legally compliant?)
       └─ ESCALATE if non-compliant

  3. VALIDATE creator values alignment
     ├─ CHECK content aligns with creator values
     ├─ IDENTIFY value misalignments
     ├─ ASSESS creator comfort level
     └─ FLAG if questionable

  4. MAKE approval decision
     IF all_checks_pass:
       → APPROVE for distribution
     ELSE IF violations_fixable:
       → APPROVE with conditions (fix before publish)
     ELSE:
       → REJECT (cannot be fixed, violates policy)

  5. DOCUMENT compliance decision
     ├─ LOG all checks performed
     ├─ LOG decision + reasoning
     ├─ TIMESTAMP decision
     ├─ CREATE compliance audit trail
     └─ PREPARE for legal review if needed

  6. MONITOR for violations post-distribution
     CONTINUOUS:
       ├─ MONITOR distributed content
       ├─ DETECT complaints/reports
       ├─ ASSESS violation severity if reported
       ├─ TAKE remediation action (remove/flag/issue notice)
       └─ LOG all actions

  7. CALCULATE compliance score
     compliance = (Policy_Adherence × 0.35) + (Legal_Compliance × 0.35) +
                  (Creator_Values × 0.20) + (Safety_Validation × 0.10)

     IF compliance <60%:
       → REJECT (too many violations)
     ELSE:
       → PROCEED

  8. WRITE policy outputs
     ├─ WRITE policy_decisions (approval/rejection)
     ├─ WRITE compliance_log (all checks)
     ├─ WRITE policy_violations (issues found)
     ├─ WRITE compliance_alerts (critical issues)
     └─ SIGN with Yama authority + timestamp

  9. RETURN compliance verdict
     RETURN {
       "content_id": content_id,
       "decision": approved|approved_with_conditions|rejected,
       "compliance_score": 0-100,
       "violations": [...],
       "remediation_required": true|false,
       "legal_review_needed": true|false
     }

END FUNCTION
```

---

## 6. COMPLIANCE_SCORING

### Compliance Framework

```
COMPLIANCE_SCORE =
  (Policy_Adherence × 0.35) +
  (Legal_Compliance × 0.35) +
  (Creator_Values × 0.20) +
  (Safety_Validation × 0.10)

RANGE: 0-100

THRESHOLDS:
  0-40   → CRITICAL VIOLATIONS (must reject)
  40-70  → ISSUES FOUND (can fix or reject)
  70-100 → COMPLIANT (approve)
```

---

## 7. SKILL BINDINGS (Yama owns/controls 6 core skills)

| Skill_ID | Skill_Name | Archetype | Authority_Level | Primary_Role | Vein_Binding |
|----------|-----------|-----------|-----------------|-------------|--------------|
| M-367 | Policy Enforcer | governance | FULL_CONTROL | Enforce policies (core) | policy_decisions |
| M-368 | Compliance Validator | analysis | FULL_CONTROL | Validate compliance (core) | compliance_log |
| M-369 | Legal Reviewer | governance | CONTROL | Check legal compliance | policy_decisions |
| M-370 | Violation Detector | analysis | CONTROL | Detect violations | policy_violations |
| M-371 | Risk Assessor | analysis | CONTROL | Assess policy risk | policy_decisions |
| M-372 | Remediation Specialist | governance | CONTROL | Plan remediation | policy_violations |

---

## 8. POLICY_ENFORCEMENT_FRAMEWORK

### Policy Categories

```
CONTENT_SAFETY:     Offensive, harmful, dangerous content
COPYRIGHT:          Unauthorized use of copyrighted material
PRIVACY:            Violation of individual privacy
ACCURACY:           Spreading misinformation
PLATFORM_POLICIES:  Violation of platform rules
LEGAL:              Non-compliance with laws/regulations
CREATOR_VALUES:     Misalignment with creator's stated values
COMMUNITY_STANDARDS: Community guideline violations
```

### Severity Levels

```
LOW:        Policy question, can be addressed
MEDIUM:     Policy violation, requires fix
HIGH:       Serious violation, likely must reject
CRITICAL:   Illegal or unacceptable, must reject immediately
```

---

## 9. FAILURE SURFACES & RECOVERY

| Failure_Type | Detection_Signal | Recovery_Path | Fallback_Director | SLA |
|-------------|------------------|---------------|-------------------|-----|
| Policy ambiguity | Unclear if violates | Escalate to creator | Creator (decision) | <60s |
| False positive | Incorrectly flagged | Review and approve | Yama (manual review) | <120s |
| False negative | Violation missed | Investigate why, improve | Yama (improvement) | <120s |
| Legal uncertainty | Unsure of compliance | Escalate to legal review | Legal (expert judgment) | <180s |
| Post-publication violation | Violation discovered after | Remove/flag content, notify | Yama (remediation) | <60s |

---

## 10. EXECUTION TIERS

**TIER_1 (STRICT ENFORCEMENT)**
- All 6 skills active
- Thorough policy review
- Legal review if uncertain
- Creator values checked
- Multiple violations trigger rejection
- Cost: Thorough validation

**TIER_2 (STANDARD ENFORCEMENT)**
- 5/6 skills active (skip M-369)
- Standard policy review
- Legal compliance only if clear
- Creator values advisory
- Major violations trigger rejection
- Cost: Standard validation

**TIER_3 (MINIMAL ENFORCEMENT)**
- 4/6 skills active
- Basic policy check
- Critical violations only
- No creator values check
- Only critical violations trigger rejection
- Cost: Minimal validation

---

## 11. HITL TRIGGERS (Manual Intervention)

| Trigger_Type | Condition | Escalation_Path | Required_Action | Time_Limit |
|-------------|-----------|-----------------|-----------------|-----------|
| Policy Ambiguity | Unsure if violates | Yama + creator | Creator decision | 30 min |
| Legal Question | Legal compliance unclear | Yama + legal | Legal review | 60 min |
| Creator Appeal | Creator disputes rejection | Yama + creator | Reassess with creator input | 60 min |
| Post-Publication Violation | Violation discovered after | Yama + creator | Remediation action | 30 min |
| Critical Violation | Serious violation detected | Yama + creator | Immediate action | 5 min |

---

## 12. DASHBOARD_VISIBILITY & TELEMETRY

### Public Fields
- **Compliance_Score**: 0-100
- **Content_Status**: Approved | Approved_with_conditions | Rejected
- **Violations**: Count and severity
- **Policy_Adherence**: % of policies passed
- **Legal_Compliance**: Status
- **Last_Review**: Date/time

### Audit-Only Fields
- **Detailed_Violations**: All violations found
- **Policy_Decisions**: All decisions + reasoning
- **Compliance_History**: Past compliance record
- **Remediation_Actions**: Actions taken
- **Appeals**: Creator appeals and outcomes
- **Post_Publication_Issues**: Issues found after publication
- **Review_Time**: Time spent on review

---

## 13. CRITICAL AMBIGUITIES

| Ambiguity | Current State | Resolution | Owner |
|-----------|--------------|-----------|-------|
| Policy interpretation | Case-by-case | Define clear policy guidelines | Creator/Legal |
| Creator values definition | Discussed | Formalize creator value guidelines | Creator |
| Legal requirements | Assumed | Confirm all applicable laws | Legal |
| Violation severity | Assessed per case | Define severity thresholds | Yama |
| Appeal process | Not defined | Define how creators can appeal | Yama |
| Post-publication enforcement | Not automated | Define response procedures | Yama |

---

## 14. ACCEPTANCE CRITERIA (DEPLOYMENT GATE)

✅ **READY FOR DEPLOYMENT IF**:
- [ ] All 6 policy skills callable and tested
- [ ] Policy validation working
- [ ] Legal compliance checking functional
- [ ] Creator values checking working
- [ ] Violation detection working
- [ ] Compliance scoring verified
- [ ] All HITL triggers functional
- [ ] Audit trail working
- [ ] Integration with all directors tested
- [ ] End-to-end compliance testing completed

---

## 15. RELEASE BLOCKING STATUS

**RELEASE_BLOCKING: CRITICAL** (policy gate is mandatory)

Without Yama, illegal or policy-violating content could be published. Policy enforcement is critical infrastructure.

---

## 16. OPERATIONAL NOTES

- **Created**: 2026-04-21
- **Status**: SPECIFICATION COMPLETE
- **Testing Priority**: CRITICAL (legal/policy compliance mandatory)
- **Next Step**: Integration with all directors for policy validation
- **Authority Level**: Veto power over non-compliant content
- **Legal Review**: Escalate uncertain cases to legal counsel
- **Success Metric**: 100% compliance with all policies, zero violations

## MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE

This append-only block upgrades this component to the MAC-06.2B universal component contract standard. Existing behavior above remains intact; this block adds required typed inputs, outputs, pointers, validation, fallback, and lineage expectations.

component_id: DIRECTOR:_YAMA
component_layer: DIRECTOR
component_name: Yama
route_families: [approval_gate, repo_write_mode]
activation_triggers: route_family in [publishing] or explicit registry selection; mark approval_gate_profile only when route_family is unknown.
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
decision_authority: Owns route decision boundaries, downstream agent selection, quality authority, escalation authority.
agent_selection_rules: Select only registered agents with matching route_family and input/output packet capability.
quality_authority: May block downstream execution when quality gates or packet evidence are missing.
escalation_rules: Escalate to user or governance gate when route, evidence, or provider boundary is unclear.

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
evidence_used_for_resolution: path/pre-contract keyword: approval/oauth; component_path=directors/kernel/yama.md; component_id=DIRECTOR:_YAMA
remaining_unknowns: none
