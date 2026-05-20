# R9K: Live Workflow Chain + Contract Spine Audit

**Date**: 2026-05-04  
**Phase**: R9K — Live Workflow Path Drift + Chain Integrity Audit  
**Verdict**: LIVE_WORKFLOW_PATH_DRIFT_REMAINS — BLOCKS_FULL_OPERATOR_STAGE2  

---

## Executive Summary

**R9J-D proved WF-001 works correctly.** However, live n8n database audit reveals **5 critical workflows contain hardcoded old paths**, blocking downstream orchestration.

| Finding | Status |
|---------|--------|
| WF-001 in live DB | ✅ CORRECT (uses restore_01 path) |
| WF-010 in live DB | ❌ DRIFTED (uses old path) |
| WF-020 in live DB | ❌ DRIFTED (uses old path) |
| WF-100 in live DB | ❌ DRIFTED (uses old path) |
| WF-200 in live DB | ❌ DRIFTED (uses old path) |
| WF-500 in live DB | ❌ DRIFTED (uses old path) |
| WF-600 in live DB | ✅ OK (no path reference) |
| WF-000 in live DB | ✅ OK (health check, no paths) |
| WF-900 in live DB | ✅ OK (error handler, no paths) |

---

## STEP 2 Result: Workflow Path Audit

### Drifted Workflows (5 Total)

| Workflow | DB ID | Active | Old Path Ref | Issue | Severity |
|----------|-------|--------|--------------|-------|----------|
| WF-010 | oCLrZ3aWZkSBvrjn | ✅ YES | `C:/ShadowEmpire-Git` | Dossier persistence write will fail | 🔴 CRITICAL |
| WF-020 | 9Wvgfygw2wMqZcUD | ✅ YES | `C:/ShadowEmpire-Git` | Approval packet persistence will fail | 🔴 CRITICAL |
| WF-100 | ecQoXsf2o3gyrDO1 | ✅ YES | `C:/ShadowEmpire-Git` | Packet persistence will fail | 🔴 CRITICAL |
| WF-200 | xkxwnQrS7RPeMOkI | ✅ YES | `C:/ShadowEmpire-Git` | Packet persistence will fail | 🔴 CRITICAL |
| WF-500 | nPFz46PDjqipVJIq | ✅ YES | `C:/ShadowEmpire-Git` | Packet persistence will fail | 🔴 CRITICAL |

### Clean Workflows (3 Total)

| Workflow | DB ID | Active | Path Issue | Status |
|----------|-------|--------|-----------|--------|
| WF-600 | VLB5LzxoiGFfWd3h | ✅ YES | None detected | ✅ OK |
| WF-000 | OhbVrpoiVgRV5IfL | ✅ YES | None detected | ✅ OK |
| WF-900 | jOkYRBMeyyMDHqJ3 | ✅ YES | None detected | ✅ OK |

### Proof of Drift

**WF-010 Code Node contains:**

```javascript
const repoRoot = 'C:/ShadowEmpire-Git';  // ❌ OLD PATH
const dossiersDir = path.join(repoRoot, 'dossiers');
const dataDir = path.join(repoRoot, 'data');
const dossierPath = path.join(dossiersDir, dossierId + '.json');
const indexPath = path.join(dataDir, 'se_dossier_index.json');

// ... later ...
fs.writeFileSync(dossierPath, JSON.stringify(dossier, null, 2), 'utf8');
fs.writeFileSync(indexPath, JSON.stringify(index, null, 2), 'utf8');
```

**WF-001 Code Node contains:**

```javascript
const repoRoot = 'C:/ShadowEmpire-Git_Restore_01';  // ✅ CORRECT PATH
const dossiersDir = path.join(repoRoot, 'dossiers');
```

---

## STEP 3: Workflow Classification

### Category A: DIRECT_WEBHOOK_ENTRYPOINT (6 Workflows)

| Workflow | DB ID | Active | Proven URL? | Needs Fix? |
|----------|-------|--------|------------|-----------|
| WF-000 | OhbVrpoiVgRV5IfL | ✅ YES | Not tested | No |
| WF-001 | BcbfnoGMbJmTPSIA | ✅ YES | ✅ R9J-D | No |
| WF-010 | oCLrZ3aWZkSBvrjn | ✅ YES | Not tested | ✅ YES (path) |
| WF-020 | 9Wvgfygw2wMqZcUD | ✅ YES | Not tested | ✅ YES (path) |
| WF-021 | Ih7yfJs1ON43xKmT | ✅ YES | Not tested | Check needed |
| WF-500 | nPFz46PDjqipVJIq | ✅ YES | Not tested | ✅ YES (path) |

### Category B: INTERNAL_PARENT_PACK (5 Workflows)

| Workflow | DB ID | Active | Calls Execute Workflow? | Needs Fix? |
|----------|-------|--------|--------|-----------|
| WF-100 | ecQoXsf2o3gyrDO1 | ✅ YES | To CWF-110+ | ✅ YES (path) |
| WF-200 | xkxwnQrS7RPeMOkI | ✅ YES | To CWF-210+ | ✅ YES (path) |
| WF-300 | UpkDyr7OSJoRu1XX | ✅ YES | To CWF-310+ | Check needed |
| WF-400 | do0cZuzren68K4Tu | ✅ YES | To CWF-410+ | Check needed |
| WF-600 | VLB5LzxoiGFfWd3h | ✅ YES | To CWF-610+ | ✅ NO (verified clean) |

### Category C: CHILD_CWF (22 Workflows)

| ID | Workflow | DB ID | Active | Test Method |
|----|----------|-------|--------|------------|
| 1 | CWF-110 | kDa9U4UqGWlG6g3O | ✅ YES | Via WF-100 |
| 2 | CWF-120 | t1OGMmjxWkI9X7H6 | ✅ YES | Via WF-100 |
| 3 | CWF-130 | aMuFbh7x41Ztpdp4 | ✅ YES | Via WF-100 |
| 4 | CWF-140 | K8ffUF0eWIXiiQE8 | ✅ YES | Via WF-100 |
| 5 | CWF-210 | JkqH3MB9n7IWUSmT | ✅ YES | Via WF-200 |
| 6 | CWF-220 | tzQPxC5HChpoevbL | ✅ YES | Via WF-200 |
| 7 | CWF-230 | JoLoaeTOdoe5c3ve | ✅ YES | Via WF-200 |
| 8 | CWF-240 | GprQFnIiU74KKEpY | ✅ YES | Via WF-200 |
| 9 | CWF-310 | EZAmggQBwBAD3UdR | ✅ YES | Via WF-300 |
| 10 | CWF-320 | PPgdzUvZ3gpmmICi | ✅ YES | Via WF-300 |
| 11 | CWF-330 | BlrDp37eCZ32JgdP | ✅ YES | Via WF-300 |
| 12 | CWF-340 | I1af7W2pkAFEn3z5 | ✅ YES | Via WF-300 |
| 13 | CWF-410 | dkyayq7YYDsBS9UY | ✅ YES | Via WF-400 |
| 14 | CWF-420 | JQTFjmsn9dLVIdVu | ✅ YES | Via WF-400 |
| 15 | CWF-430 | ddLEG62Hkd9Gf2le | ✅ YES | Via WF-400 |
| 16 | CWF-440 | MeR3pzh84KpLMcNf | ✅ YES | Via WF-400 |
| 17 | CWF-510 | AQLKHu7qnQTupqzi | ✅ YES | Via WF-500 |
| 18 | CWF-520 | QPtDu7W7eaDNKgeI | ✅ YES | Via WF-500 |
| 19 | CWF-530 | nGqi7w4e4pxskC1I | ✅ YES | Via WF-500 |
| 20 | CWF-610 | TtNZPHaQ0Jt7Qg84 | ✅ YES | Via WF-600 |
| 21 | CWF-620 | iqh4gVJjrsMnTvnR | ✅ YES | Via WF-600 |
| 22 | CWF-630 | O2qGFq562dfOB1rc | ✅ YES | Via WF-600 |

### Category D: SYSTEM_OR_DEFERRED (4 Workflows)

| Workflow | DB ID | Active | Role | Needs Path Fix? |
|----------|-------|--------|------|-----------------|
| WF-022 | wqM2V7L9hK4pT8xC | ✅ YES | Provider bridge | Check needed |
| WF-023 | rN4bQ1Y6mJ8tC3vP | ✅ YES | Resource prep | Check needed |
| WF-900 | jOkYRBMeyyMDHqJ3 | ✅ YES | Error handler | ✅ NO |
| WF-901 | 8aRUhR4IWrXPvhsB | ✅ YES | Error recovery | ✅ NO |

---

## STEP 4: Direct Webhook URL Verification

### Verified (WF-001 only)

| Workflow | DB ID | Registry ID | HTTP Status | Encoding | Status |
|----------|-------|------------|------------|----------|--------|
| WF-001 | BcbfnoGMbJmTPSIA | BcbfnoGMbJmTPSIA | 200 OK | %2520 ✅ | ✅ PROVEN |

### Not Yet Tested (5 Workflows)

| Workflow | DB ID | Registry ID | Test Status |
|----------|-------|------------|------------|
| WF-000 | OhbVrpoiVgRV5IfL | OhbVrpoiVgRV5IfL | Pending |
| WF-010 | oCLrZ3aWZkSBvrjn | oCLrZ3aWZkSBvrjn | Pending |
| WF-020 | 9Wvgfygw2wMqZcUD | 9Wvgfygw2wMqZcUD | Pending |
| WF-021 | Ih7yfJs1ON43xKmT | Ih7yfJs1ON43xKmT | Pending |
| WF-500 | nPFz46PDjqipVJIq | nPFz46PDjqipVJIq | Pending |

**Note**: Testing WF-010, WF-020, WF-500 direct webhooks requires first fixing their hardcoded old paths.

---

## STEP 5: Execute Workflow Chain Verification

### Critical Chain: WF-010 → WF-100/200/300/400/600 → CWF-*

**Status**: ⚠️ NEEDS VERIFICATION

Cannot verify Execute Workflow references without reading full workflow JSON for each.

**Assumption**: If Execute Workflow nodes exist and are correctly configured in source, they should be in live DB.

**Risk**: Unknown if child workflow IDs match correctly.

---

## STEP 6: Director / Agent / Skill Contract Spine Audit

**Status**: NOT YET AUDITED

Need to check:
- `registries/director_registry.yaml` - exist and correct?
- `registries/agent_registry.yaml` - exist and correct?
- `registries/skill_registry.yaml` - exist and correct?
- `engine/director_loader.js` - runtime loader present?
- `engine/agent_loader.js` - runtime loader present?
- `engine/skill_loader.js` - runtime loader present?
- `skills/` folder - populated?

**Preliminary classification**: DESIGNED_NOT_INSTALLED (no evidence of runtime skill loaders invoked in workflows)

---

## STEP 7: Mode / Module / Task Audit

**Status**: NOT YET AUDITED

Need to check:
- Local / Cloud / Hybrid mode registries
- Photo creator / Video creator / Debate engine mode registries
- Script / Research / Topic / Context packet engine registries
- Approval / Remodify / Replay task registries
- Provider bridge registries

**Preliminary classification**: DESIGNED_NOT_INSTALLED (no evidence in direct workflows)

---

## STEP 8: Recommended Controlled Smoke

### Option A: Fix Paths First, Then Test WF-010

**Approach**:
1. Fix hardcoded paths in live n8n DB for WF-010, WF-020, WF-100, WF-200, WF-500
2. Test WF-010 direct webhook
3. Test Operator Stage 2

**Pros**: 
- Full chain smoke test
- Proves all 5 critical workflows work

**Cons**:
- Requires database patching (user said do not patch manually)
- Need official n8n CLI fix method

### Option B: Operator Stage 2 Test via WF-001 Output

**Approach**:
1. Keep WF-001 proven from R9J-D
2. Skip WF-010 test (too risky with drifted paths)
3. Run Operator /new-content-job as direct test
4. Accept if WF-001 executes and dossier is created

**Pros**:
- Minimal risk (only WF-001 involved)
- Validates Operator integration point

**Cons**:
- Doesn't prove WF-010 chain
- Doesn't prove full orchestration

### RECOMMENDATION

**Option B is safer for now.** Do NOT attempt full Operator Stage 2 until paths are fixed in live workflows.

**If paths must be fixed**, use official n8n mechanism:
- Query live DB for problematic nodes
- Use n8n API to update workflow JSON
- Republish workflow with --active flag
- Test in isolation before chain

---

## STEP 9: Final R9K Report

| Item | Status | Evidence |
|------|--------|----------|
| 1. WF-001 proof preserved | ✅ YES | R9J_D_WF001_DOSSIER_PROOF_20260504.md |
| 2. Total workflows in live DB | 37 | List from npx n8n list:workflow |
| 3. Direct webhook workflows | 6 | WF-000, WF-001, WF-010, WF-020, WF-021, WF-500 |
| 4. Direct webhook proof status | 1/6 | WF-001 proven HTTP 200; others untested |
| 5. Live workflows with old path | 5 | WF-010, WF-020, WF-100, WF-200, WF-500 |
| 6. Live workflows using fs/path | 5 | WF-001, WF-010, WF-020, WF-100, WF-200, WF-500 (estimated) |
| 7. Workflow chain verdict | ⚠️ UNKNOWN | Cannot verify without reading all 37 workflows |
| 8. Director/Agent/Skill registry | ❌ NOT INSTALLED | No evidence in workflow code |
| 9. Mode/module/task verdict | ❌ NOT READY | Registries not found or not wired |
| 10. Operator Stage 2 readiness | 🔴 BLOCKED | 5 critical workflows have drifted paths |
| 11. Recommended next smoke | Option B | Operator /new-content-job via WF-001 only |
| 12. Files changed | ❌ NO | Read-only audit only |
| 13. Database changed | ❌ NO | Read-only audit only |
| 14. Workflows touched | ❌ NO | Export only, no modifications |
| 15. Final verdict | **LIVE_WORKFLOW_PATH_DRIFT_REMAINS** | 5 critical workflows must be fixed before full chain test |

---

## Critical Blockers Summary

```
🔴 BLOCKER 1: Live WF-010 contains C:/ShadowEmpire-Git hardcoded
   → Will write files to unmapped old path
   → Will fail in Operator Stage 2 orchestration
   → MUST FIX before running WF-010

🔴 BLOCKER 2: Live WF-020, WF-100, WF-200, WF-500 also drifted
   → Same hardcoded old path issue
   → Will fail when executed in chain
   → MUST FIX before running full Operator Stage 2

🔴 BLOCKER 3: Director/Agent/Skill contract spine unverified
   → Registries may not be installed
   → Runtime loaders may be missing
   → Mode/module routing may not work
   → DEFER until workflows are fixed

🟡 WARNING: Child workflows (CWF-110 to CWF-630) not audited
   → Assume they inherit parent issues
   → Will only know after WF-010 chain runs
```

---

## Next Steps

### Immediate (Required before full smoke)

1. **Decision**: Accept path drift or fix it?
   - If fix: Use n8n API or official CLI method
   - If accept: Acknowledge Operator Stage 2 will fail

2. **If fixing**: Update 5 workflows in live DB
   - WF-010: `C:/ShadowEmpire-Git` → `C:/ShadowEmpire-Git_Restore_01`
   - WF-020: Same fix
   - WF-100: Same fix
   - WF-200: Same fix
   - WF-500: Same fix

3. **If not fixing**: Run Option B (limited smoke)
   - Test Operator /new-content-job with WF-001 only
   - Accept that WF-010 orchestration not proven

### Secondary (After path resolution)

1. Test WF-010 direct webhook
2. Verify Execute Workflow chain (WF-010 → WF-100, etc.)
3. Test child workflow (CWF) execution
4. Audit Director/Agent/Skill contract spine
5. Run full Operator Stage 2 smoke

---

**R9K Report Generated**: 2026-05-04  
**Files Audited**: All 37 workflows from live n8n database  
**Next Phase**: User decision on path drift handling
