# R9F Evidence Report: Operator URL Resolution Fixed

**Date**: 2026-05-04  
**Phase**: R9F — System-wide Operator n8n Client Registry URL Fix  
**Verdict**: OPERATOR_URL_RESOLUTION_FIXED_BUT_DOSSIER_TIMEOUT_BLOCKS_STAGE2

## What Was Fixed

### Code Changes
- **File Modified**: `engine/chat/n8n_workflow_client.js`
- **Lines Modified**: 89-167 (resolveWebhookPath function)
- **Backup Location**: `docs/recovery/R9F_BACKUP_20260504_143200/`

### Key Improvements
1. Registry lookup now supports multiple shapes: `workflows:`, `webhooks:`, direct keys
2. URL resolution priority correctly implemented:
   - PRIORITY 1: Use `registry.full_url` if absolute (http/https)
   - PRIORITY 2: Use `registry.webhook_path` + baseUrl
   - PRIORITY 3: Use `registry.path` + `/webhook/` prefix
   - FALLBACK: Only use JSON if no registry entry exists
3. Silent fallback bug eliminated with `REGISTRY_ENTRY_PRESENT_BUT_URL_UNRESOLVED` exception
4. All URL resolutions now logged with source tracking

## Proof Evidence

### WF-001 Direct Webhook (Proven)
- **Resolved URL**: `http://127.0.0.1:5678/webhook/BcbfnoGMbJmTPSIA/trigger%2520node/wf-001-dossier-create`
- **URL Source**: `registry_full_url` (not JSON fallback)
- **Encoding**: ✅ %2520 double-encoding preserved
- **HTTP Result**: 200 OK
- **Execution ID**: `exec-1777881980473-mx25hi6c6`
- **n8n Response**: `{"message":"Workflow was started"}`

### WF-010 Direct Webhook (Proven in isolation)
- **Resolved URL**: `http://127.0.0.1:5678/webhook/oCLrZ3aWZkSBvrjn/trigger%2520node/wf-010-parent-orchestrator`
- **URL Source**: `registry_full_url` (not JSON fallback)
- **Encoding**: ✅ %2520 double-encoding preserved
- **Validation Test**: ✅ PASS (from validate_webhook_resolution.js)

### Operator Logs (Direct Proof)
```
[N8N Client] resolved webhook URL for WF-001: http://127.0.0.1:5678/webhook/BcbfnoGMbJmTPSIA/trigger%2520node/wf-001-dossier-create (from registry full_url)
[N8N Client] Triggering WF-001
[N8N Client] URL source: registry_full_url
[N8N Client] POST http://127.0.0.1:5678/webhook/BcbfnoGMbJmTPSIA/trigger%2520node/wf-001-dossier-create
[N8N Client] Workflow WF-001 triggered successfully. Execution ID: exec-1777881980473-mx25hi6c6
```

### Validation Results
All 6 direct webhook workflows validated:
| Workflow | Status | URL Source | Encoding |
|----------|--------|-----------|----------|
| WF-000 | ✅ PASS | registry_full_url | No spaces |
| WF-001 | ✅ PASS | registry_full_url | %2520 ✅ |
| WF-010 | ✅ PASS | registry_full_url | %2520 ✅ |
| WF-020 | ✅ PASS | registry_full_url | No spaces |
| WF-021 | ✅ PASS | registry_full_url | No spaces |
| WF-500 | ✅ PASS | registry_full_url | No spaces |

## What Was NOT Proven in Stage 2

1. ❌ **Dossier creation completion**: Timeout occurred in waitForNewDossier()
2. ❌ **WF-001 output**: Dossier file existence not verified
3. ❌ **se_dossier_index.json update**: New entry not found in index
4. ❌ **WF-010 through Operator**: Not triggered (blocked by WF-001 timeout)
5. ❌ **Real dossier_id**: Not returned to client
6. ❌ **Outputs endpoint**: Not tested

## Blockers

**Current Blocker**: Dossier timeout in /operator/new-content-job at line 146  
**Root Cause**: Unknown (triage required in R9G)  
**Possible Causes**:
- WF-001 execution failed inside n8n
- WF-001 created dossier in wrong path
- Operator polling wrong path/index
- WF-001 still executing after timeout (15 second window)
- Payload schema mismatch between Operator and WF-001
- Windows file path / permission issue

## Test Commands Used

**Operator Stage 2 replay**:
```bash
curl.exe -X POST http://127.0.0.1:5050/operator/new-content-job \
  -H "Content-Type: application/json" \
  -d '{"topic":"Create a YouTube script...","mode":"creator"}'
```

**Result**: HTTP 502, WF-001 HTTP 200 (execution_id: exec-1777881980473-mx25hi6c6), dossier timeout error

## Status

| Component | Status |
|-----------|--------|
| n8n webhook endpoints | ✅ HTTP 200 reachable |
| Operator URL resolver | ✅ Fixed and proven |
| Registry full_url format | ✅ Correct |
| %2520 encoding preservation | ✅ Verified |
| WF-001 trigger from Operator | ✅ HTTP 200 |
| WF-001 dossier output | ❌ Not verified |
| Operator Stage 2 completion | ❌ Blocked by timeout |

## Next Phase

**Phase R9G**: Dossier Timeout Triage + WF-001 Output Proof

Goal: Determine if timeout is caused by:
1. WF-001 execution failure
2. Dossier written to wrong path
3. Operator polling wrong location
4. Timeout too short
5. Payload schema mismatch

---

**Report Generated**: 2026-05-04 08:06:35 UTC  
**Backup Evidence**: R9F_BACKUP_20260504_143200/
