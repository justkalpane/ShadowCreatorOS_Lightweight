# R9K-B: Targeted Live Workflow Path Fix

**Date**: 2026-05-04  
**Phase**: R9K-B — Targeted Live Workflow Path Fix + R9K-B2 Root-Cause Audit  
**Final Verdict**: **TARGETED_LIVE_PATH_FIX_PASS**

---

## Executive Summary

✅ **SUCCESS**: All 5 drifted workflows in live n8n database have been updated with corrected paths.

**What was fixed:**
- WF-010, WF-020, WF-100, WF-200, WF-500
- **Old path removed**: `C:/ShadowEmpire-Git` ❌
- **New path installed**: `C:/ShadowEmpire-Git_Restore_01` ✅

**What was NOT touched:**
- WF-001 (remains untouched from R9J-D proof)
- All other 32 workflows (unchanged)
- Registry (no changes needed)
- Any direct SQL

---

## R9K-B2: Root-Cause Analysis

### Problem Found
Initial clone import test **appeared to fail** because:
- Exported workflow JSON files lack top-level `id` field by default
- n8n requires `id` field to match workflows for update/overwrite
- Files had UTF-8 BOM encoding causing JSON parse errors

### Solution Applied
1. **Add ID field** to each workflow JSON at top level
2. **Save with UTF-8 No-BOM** (not standard PowerShell default)
3. **Import with corrected format** using `npx n8n import:workflow --input=<file>`

### Verification Method
- **Clone test** (STEP 4-5): ✅ PASSED - Confirmed method works
- **Live application** (STEP 5): ✅ PASSED - All 5 workflows updated
- **Final audit** (STEP 8-9): ✅ PASSED - Old paths removed, new paths present

---

## Detailed Results

### Step 1: Backup
- **Backup location**: `C:\ShadowEmpire\recovery_backups\phase_r9k_b_pre_targeted_path_fix_20260504_145257`
- **Contents**: n8n database, source files, live exports
- **Status**: ✅ Complete

### Step 2: Source File Verification
| Workflow | Old Path Present? | New Path Present? | Status |
|----------|---:|---:|---|
| WF-010 | ❌ NO | ✅ YES | ✅ OK |
| WF-020 | ❌ NO | ✅ YES | ✅ OK |
| WF-100 | ❌ NO | ✅ YES | ✅ OK |
| WF-200 | ❌ NO | ✅ YES | ✅ OK |
| WF-500 | ❌ NO | ✅ YES | ✅ PATCHED |

**Note**: WF-500.json source was patched (old path found initially)

### Step 3: Temp Package Preparation
- **Directory**: `C:\ShadowEmpire-Git_Restore_01\temp\n8n_update_r9k_b`
- **Files**: 5 JSON files (WF-010, WF-020, WF-100, WF-200, WF-500)
- **Validation**: All paths correct, Execute Workflow refs preserved

### Step 4-5: Clone Test (R9K-B2 Probe)
| Test | Result | Finding |
|------|--------|---------|
| Initial import (without ID) | ❌ FAILED | Files missing ID field |
| JSON encoding issue | ❌ FAILED | BOM encoding rejected |
| Fixed import (with ID + UTF-8 No-BOM) | ✅ PASSED | Clone workflow updated correctly |

**Clone Test Result**: `CLONE_IMPORT_REPLACED_WORKFLOW`

### Step 5-6: Live Targeted Update
| Workflow | Import Status | Activation Status | Result |
|----------|---:|---:|---|
| WF-010 | ✅ Success | ✅ Activated | ✅ |
| WF-020 | ✅ Success | ✅ Activated | ✅ |
| WF-100 | ✅ Success | ✅ Activated | ✅ |
| WF-200 | ✅ Success | ✅ Activated | ✅ |
| WF-500 | ✅ Success | ✅ Activated | ✅ |

### Step 8-9: Final Live DB Audit

**Before update**:
```
WF-010: C:/ShadowEmpire-Git ❌
WF-020: C:/ShadowEmpire-Git ❌
WF-100: C:/ShadowEmpire-Git ❌
WF-200: C:/ShadowEmpire-Git ❌
WF-500: C:/ShadowEmpire-Git ❌
```

**After update**:
```
WF-010: C:/ShadowEmpire-Git_Restore_01 ✅
WF-020: C:/ShadowEmpire-Git_Restore_01 ✅
WF-100: C:/ShadowEmpire-Git_Restore_01 ✅
WF-200: C:/ShadowEmpire-Git_Restore_01 ✅
WF-500: C:/ShadowEmpire-Git_Restore_01 ✅
```

---

## Critical Proof

### WF-001 Untouched
- **Status**: Still active from R9J-D proof
- **Path**: `C:/ShadowEmpire-Git_Restore_01` (already correct)
- **Verification**: NOT re-imported, NOT modified
- **Result**: ✅ WF-001 remains proven and stable

### Workflow Chain Intact
- **Total workflows in live DB**: 37 (unchanged)
- **Duplicate workflows**: 0 (no duplicates created)
- **Execute Workflow references**: Preserved in all 5 updated workflows
- **Status**: ✅ Chain structure maintained

### Registry Not Updated
- **Changes**: None
- **Reason**: Workflow IDs unchanged, only JSON content updated
- **Status**: ✅ Registry remains as-is

---

## Key Insights

### What Made This Work
1. **n8n CLI documents that imported workflows with matching IDs overwrite existing ones**
2. **The failure was NOT that n8n cannot update workflows**
3. **The failure was that our temp files lacked the ID field n8n needs**
4. **The solution was surgical: add ID, fix encoding, re-import**

### Why Clone Test Was Essential
- Proved the fix worked before touching production
- Identified the exact issue (missing ID + BOM encoding)
- Validated that import method works correctly when formatted properly
- Enabled confident live application

---

## Files Changed

| File | Change | Reason |
|------|--------|--------|
| WF-500.json (source) | Path updated in Code node | Old path found during audit |
| Temp JSON files (5) | ID field added | Required for n8n import-to-update |
| Temp JSON files (5) | UTF-8 No-BOM encoding | BOM causes JSON parse errors |
| Live n8n workflows (5) | Import applied | Overwrite old versions with corrected ones |

### NO Changes
- ❌ Direct SQLite editing
- ❌ Registry updates
- ❌ Broad reimports (only 5 targeted)
- ❌ WF-001 touched
- ❌ Other 32 workflows modified

---

## Status Summary

| Component | Before | After | Status |
|-----------|--------|-------|--------|
| WF-010 path | C:/ShadowEmpire-Git | C:/ShadowEmpire-Git_Restore_01 | ✅ FIXED |
| WF-020 path | C:/ShadowEmpire-Git | C:/ShadowEmpire-Git_Restore_01 | ✅ FIXED |
| WF-100 path | C:/ShadowEmpire-Git | C:/ShadowEmpire-Git_Restore_01 | ✅ FIXED |
| WF-200 path | C:/ShadowEmpire-Git | C:/ShadowEmpire-Git_Restore_01 | ✅ FIXED |
| WF-500 path | C:/ShadowEmpire-Git | C:/ShadowEmpire-Git_Restore_01 | ✅ FIXED |
| WF-001 proof | ✅ LOCKED | ✅ LOCKED | ✅ INTACT |
| Workflow count | 37 | 37 | ✅ UNCHANGED |
| Execute chain | Intact | Intact | ✅ PRESERVED |

---

## Decisions Made

✅ **Rejected**: HTTP API (auth required), direct SQL (constraints), manual UI  
✅ **Accepted**: Official n8n import:workflow mechanism with proper formatting  
✅ **Validated**: Clone test before live application  
✅ **Preserved**: WF-001, registry, all other workflows  

---

## Final Verdict

```
✅ TARGETED_LIVE_PATH_FIX_PASS

All five drifted workflows updated successfully.
Live database now has corrected paths.
WF-001 proof remains locked and untouched.
Workflow chain preserved.
Ready for R9L - Operator Stage 2 orchestration test.
```

---

## Next Phase: R9L

**Objective**: Operator Stage 2 Replay - Test `/operator/new-content-job` with WF-010 orchestration chain.

**Expected execution flow**:
1. Operator receives request
2. Triggers WF-001 (proven from R9J-D)
3. WF-001 creates dossier file (proven)
4. Operator returns dossier_id to WF-010
5. WF-010 triggers WF-100, WF-200, WF-300, WF-400, WF-500, WF-020, WF-600
6. Child workflows (CWF-*) execute
7. Packets persisted to indexes
8. Output endpoint returns results

**Blocker to check before R9L**:
- WF-001 and WF-010 paths still need verification under full chain execution
- This will be proven in R9L if Operator Stage 2 completes without file-not-found errors

---

**Report Generated**: 2026-05-04  
**Backup Location**: `C:\ShadowEmpire\recovery_backups\phase_r9k_b_pre_targeted_path_fix_20260504_145257`  
**Evidence**: All 5 workflows in live DB verified with old paths removed and new paths present
