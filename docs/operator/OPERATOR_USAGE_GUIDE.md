# Shadow Operator Core — Usage Guide

**Target Audience**: Content operators, automation engineers, system administrators  
**Environment**: Windows, Local-First, n8n-Governed

---

## Quick Start

### 1. Start the Operator API

```powershell
cd C:\ShadowEmpire-Git
.\scripts\operator\start-operator.ps1
```

The API will start on `http://localhost:5002`.

Keep this terminal open while operating.

### 2. Health Check (in another terminal)

```powershell
.\scripts\operator\check-shadow-health.ps1
```

Expected output:
```
✅ Operator API: OK
✅ n8n: OK
✅ Repo Path: OK
✅ Data Files: OK
```

### 3. Create a Content Job

```powershell
.\scripts\operator\new-content-job.ps1 "Create a YouTube script about procrastination"
```

Expected output:
```
Status: accepted
Dossier ID: DOSSIER-xxx
Workflow Chain: WF-001 → WF-010
```

### 4. Inspect Output

```powershell
.\scripts\operator\inspect-output.ps1 DOSSIER-xxx
```

### 5. Approve Output

```powershell
.\scripts\operator\approve-output.ps1 DOSSIER-xxx
```

---

## Command Reference

### Health & Monitoring

#### check-shadow-health.ps1
Check if all systems are operational.

```powershell
.\scripts\operator\check-shadow-health.ps1
.\scripts\operator\check-shadow-health.ps1 -Verbose
```

**Output**: ✅/❌ status for each system component

---

### Task Creation

#### new-content-job.ps1
Create a new content job.

```powershell
.\scripts\operator\new-content-job.ps1 "Your topic here"
.\scripts\operator\new-content-job.ps1 "Create script about AI" -Context "YouTube video" -Mode creator
```

**Parameters**:
- `Topic` (required): What you want to create
- `Context` (optional): Platform context (default: "YouTube video")
- `Mode` (optional): Operating mode (default: "creator")
  - `creator`: Can create content
  - `founder`: Full access
  - `builder`: Can edit workflows
  - `operator`: Can inspect/replay

**Output**: Dossier ID, workflow status, next steps

---

### Output Inspection

#### inspect-output.ps1
See what outputs have been generated for a dossier.

```powershell
.\scripts\operator\inspect-output.ps1 DOSSIER-xxx
```

**Shows**:
- Dossier creation date and status
- Count of each output type
- Approval state
- Available actions

#### list-outputs.ps1
Get detailed list of all outputs grouped by type.

```powershell
.\scripts\operator\list-outputs.ps1 DOSSIER-xxx
```

**Shows**:
- Scripts generated
- Research packets
- Debate/critique outputs
- Context packets
- Thumbnails, metadata, etc.

---

### Output Approval & Modification

#### approve-output.ps1
Approve the generated output for publication.

```powershell
.\scripts\operator\approve-output.ps1 DOSSIER-xxx
.\scripts\operator\approve-output.ps1 DOSSIER-xxx -Reason "Ready for YouTube"
```

**Confirmation**: Requires "yes" confirmation  
**Result**: Triggers WF-020, approves dossier  
**Effect**: Output is marked ready for publishing

#### request-changes.ps1
Request modifications to the output.

```powershell
.\scripts\operator\request-changes.ps1 DOSSIER-xxx "Make it shorter and funnier"
.\scripts\operator\request-changes.ps1 DOSSIER-xxx "Add more examples" -TargetWorkflow WF-200
```

**Parameters**:
- `DossierId`: Dossier to modify
- `Instructions`: What to change
- `TargetWorkflow` (optional): Which workflow to replay (default: WF-200)

**Confirmation**: Requires "yes" confirmation  
**Result**: Triggers WF-021 with replay instructions

#### replay-stage.ps1
Replay a workflow stage from checkpoint.

```powershell
.\scripts\operator\replay-stage.ps1 DOSSIER-xxx WF-200
.\scripts\operator\replay-stage.ps1 DOSSIER-xxx WF-100 -Action checkpoint_restore
```

**Parameters**:
- `DossierId`: Which dossier
- `TargetWorkflow`: Which workflow (WF-100, WF-200, etc.)
- `Action` (optional): How to replay (default: reexecute)

**Confirmation**: Requires "yes" confirmation  
**Result**: Workflow restarts from saved checkpoint

---

### Error & Alert Management

#### check-errors.ps1
View system errors and workflow failures.

```powershell
.\scripts\operator\check-errors.ps1
.\scripts\operator\check-errors.ps1 -DossierId DOSSIER-xxx
```

**Shows**:
- Error count and types
- Workflow that failed
- Error message and timestamp
- Suggested fixes

---

### Server Management

#### start-operator.ps1
Start the Shadow Operator Core API.

```powershell
.\scripts\operator\start-operator.ps1
.\scripts\operator\start-operator.ps1 -Port 5002
```

**Default Port**: 5002  
**Access**: http://localhost:5002

---

## Workflows

### Standard Content Creation Workflow

```
1. new-content-job.ps1 "Your topic"
   ↓ Creates DOSSIER-xxx
   
2. WF-001 runs (creates dossier)
   ↓
   
3. WF-010 runs (orchestrates workflow chain)
   ├→ WF-100 (generates topics)
   ├→ WF-200 (generates script)
   ├→ WF-300 (adds context)
   ├→ WF-400 (plans media)
   └→ WF-500 (prepares metadata)
   ↓
   
4. inspect-output.ps1 DOSSIER-xxx
   ↓ Shows all generated packets
   
5. EITHER:
   a) approve-output.ps1 DOSSIER-xxx
      ↓ Approves for publication
      
   OR
   
   b) request-changes.ps1 DOSSIER-xxx "instructions"
      ↓ Triggers WF-021 replay with new instructions
      ↓ Go to step 4
```

### Error Recovery Workflow

```
1. check-errors.ps1
   ↓ Shows failed workflows
   
2. Identify problem dossier
   
3. EITHER:
   a) replay-stage.ps1 DOSSIER-xxx WF-200
      ↓ Re-run script generation
      
   OR
   
   b) request-changes.ps1 DOSSIER-xxx "Fix X"
      ↓ Re-run with new instructions
      
4. inspect-output.ps1 DOSSIER-xxx
   ↓ Verify new output
```

---

## Understanding Status Values

### Dossier Status
- `ACCEPTED` — Created, awaiting workflow
- `RUNNING` — Workflows executing
- `PARTIAL_OUTPUT` — Some packets generated
- `OUTPUT_READY` — All packets generated, ready for review
- `APPROVED` — Approved for publication
- `REJECTED` — Rejected, awaiting remodification
- `REPLAY_REQUESTED` — Replay in progress
- `FAILED` — Workflow failure, needs troubleshooting

### Workflow Status
- `NOT_STARTED` — Not yet triggered
- `QUEUED` — Waiting to execute
- `RUNNING` — Currently executing
- `COMPLETED` — Finished successfully
- `FAILED` — Failed with error

### Output Types
- **Scripts**: Content text (original, debate, refined, final)
- **Research**: Research summaries and source citations
- **Context**: Background information, extended narratives
- **Thumbnails**: Thumbnail concept descriptions
- **Image Prompts**: Detailed image generation prompts
- **Voice Scripts**: Text formatted for voice-over
- **Video Packages**: Complete video production plan
- **Metadata**: SEO, description, tags, scheduling info

---

## Mode System

### Operating Modes
- **creator**: Can create content, cannot approve premium/cloud
- **builder**: Can edit repo/workflows, cannot trigger live execution
- **operator**: Can inspect/replay, cannot modify registry
- **founder**: Full access (subject to policy/consent gates)

### Check Current Mode
```powershell
curl http://localhost:5002/operator/mode/state
```

### Change Mode
Requires setting via API or config file (manual state file edit at operator/se_operator_runtime_state.json)

---

## Troubleshooting

### Operator API won't start
```powershell
# Check if port is in use
netstat -ano | grep 5002

# Check if npm modules are installed
npm install
```

### n8n not responding
```powershell
# Check n8n service
Invoke-WebRequest http://localhost:5678/api/v1/health

# If not running, start n8n manually
```

### Dossier not generating packets
1. Check workflow status: `inspect-output.ps1 DOSSIER-xxx`
2. Check errors: `check-errors.ps1`
3. View dossier timeline: `curl http://localhost:5002/operator/dossier/DOSSIER-xxx/timeline`
4. Replay workflow: `replay-stage.ps1 DOSSIER-xxx WF-200`

### "Unknown error" message
- Check operator logs in the terminal where you started `start-operator.ps1`
- Use `check-errors.ps1` to see detailed error info
- Verify n8n is running and accessible

---

## Environment Variables (Optional)

```powershell
$env:PORT = 5002
$env:N8N_BASE_URL = "http://localhost:5678"
$env:OLLAMA_URL = "http://localhost:11434"
```

---

## API Access via PowerShell/Curl

### Direct API Call
```powershell
# Create job via API
curl -X POST http://localhost:5002/operator/new-content-job `
  -H "Content-Type: application/json" `
  -d @{
    topic = "Your topic"
    context = "YouTube video"
    mode = "creator"
  } | ConvertFrom-Json
```

---

## Safety Guarantees

✅ No fake outputs — only real generated packets  
✅ No fake approval — requires explicit action  
✅ No unauthorized replay — confirms before executing  
✅ No provider calls without approval — safe mode default  
✅ Full audit trail — every action traced to dossier  

---

## Next: See Full API Reference

For detailed API endpoint information, see: **OPERATOR_API_REFERENCE.md**

For acceptance test results, see: **OPERATOR_ACCEPTANCE_TEST_REPORT.md**

---

**Last Updated**: 2026-04-30  
**Version**: 1.0  
**Status**: Operational

============================================================
2026-05-06 RUNTIME PROFILE RECOVERY CORRECTION
============================================================

This section is append-only production hardening. Preserve the original document above this section.

Confirmed wrong profile:
C:\ShadowEmpire\n8n_user

Confirmed correct latest runtime profile:
C:\ShadowEmpire\n8n_user_restore_01

Correct active n8n database path:
C:\ShadowEmpire\n8n_user_restore_01\.n8n\database.sqlite

Active WAL evidence path:
C:\ShadowEmpire\n8n_user_restore_01\.n8n\database.sqlite-wal

Old/wrong WAL path that must not update:
C:\ShadowEmpire\n8n_user\.n8n\database.sqlite-wal

Corrected startup script:
C:\ShadowEmpire-Git_Restore_01\scripts\windows\start_n8n_shadow_phase1.ps1

Corrected webhook registry:
C:\ShadowEmpire-Git_Restore_01\registries\n8n_webhook_registry.yaml

Recovery evidence report:
C:\ShadowEmpire-Git_Restore_01\docs\recovery\RUNTIME_PROFILE_RECOVERY_CORRECTION_20260506.md

Correct n8n UI URL:
http://127.0.0.1:5678/home/workflows

Expected canonical workflow count after correct startup:
37 total canonical workflows
37 active canonical workflows

Current recovery status:
PARTIALLY RECOVERED until WF-001 -> WF-010 smoke test passes.

Final RECOVERED condition:
- Correct profile is loaded from C:\ShadowEmpire\n8n_user_restore_01.
- 37 canonical workflows are visible and active.
- npm run n8n:status returns 200 {"status":"ok"}.
- Webhook resolver passes 6/6 using registry_full_url.
- WF-000 returns HTTP 200.
- WF-001 -> WF-010 live smoke passes.
- Restart persistence is verified after a fresh n8n restart.

GLOBAL DO-NOT-DO RULES

DO NOT:
- start n8n using C:\ShadowEmpire\n8n_user.
- start n8n without confirming N8N_USER_FOLDER.
- create a new n8n owner account during recovery.
- open old workflow editor bookmarks.
- assume workflows are deleted just because they are not visible.
- import workflows into the wrong profile.
- overwrite database.sqlite.
- delete database.sqlite-wal during active runtime.
- delete old backups.
- reset user management.
- run git reset --hard without backup and explicit approval.
- run provider/media workflows before runtime recovery is complete.
- claim RECOVERED before WF-001 -> WF-010 smoke passes.

Migration / New Laptop Restore Checklist

1. Copy production repo:
C:\ShadowEmpire-Git_Restore_01

2. Copy correct n8n profile:
C:\ShadowEmpire\n8n_user_restore_01

3. Copy ShadowEmpire data folders if present:
C:\ShadowEmpire\data
C:\ShadowEmpire\data\dossiers
C:\ShadowEmpire\data\packets
C:\ShadowEmpire\data\scripts
C:\ShadowEmpire\data\approvals
C:\ShadowEmpire\data\logs
C:\ShadowEmpire\data\cache

4. Preserve n8n encryption/config files inside:
C:\ShadowEmpire\n8n_user_restore_01\.n8n

5. Do not migrate only workflow JSONs if the database/profile contains ownership, credential, or project mappings.

6. After migration:
- install compatible Node/npm/n8n versions.
- restore repo.
- restore n8n profile.
- start with start_n8n_shadow_phase1.ps1.
- open /home/workflows.
- verify 37 workflows.
- run npm run n8n:status.
- run webhook resolver.
- run WF-000.
- run WF-001 -> WF-010 smoke.
- only then call environment RECOVERED.

7. Do not use old profile C:\ShadowEmpire\n8n_user unless all Restore_01 backups are unavailable and the user explicitly approves fallback.

## Current Shadow Creator OS Production Runtime Map - 2026-05-06

| Component | Current Confirmed Path / Host / Port | Status | Verification |
|---|---|---|---|
| Production repo | C:\ShadowEmpire-Git_Restore_01 | active target | git status required |
| n8n profile | C:\ShadowEmpire\n8n_user_restore_01 | corrected | WAL updating |
| n8n DB | C:\ShadowEmpire\n8n_user_restore_01\.n8n\database.sqlite | corrected | read-only count 37 |
| n8n WAL | C:\ShadowEmpire\n8n_user_restore_01\.n8n\database.sqlite-wal | active | LastWriteTime updates |
| wrong old profile | C:\ShadowEmpire\n8n_user | do not use | old WAL stopped / moved to n8n Old Backup |
| n8n host | 127.0.0.1 | active | browser/status |
| n8n port | 5678 | active | TCP/status |
| task broker port | 5679 | active | TCP/log |
| n8n UI | http://127.0.0.1:5678/home/workflows | use this | avoid bookmarks |
| start script | C:\ShadowEmpire-Git_Restore_01\scripts\windows\start_n8n_shadow_phase1.ps1 | corrected | start from here |
| webhook registry | C:\ShadowEmpire-Git_Restore_01\registries\n8n_webhook_registry.yaml | corrected | resolver 6/6 |
| recovery evidence | C:\ShadowEmpire-Git_Restore_01\docs\recovery\RUNTIME_PROFILE_RECOVERY_CORRECTION_20260506.md | created | read first |
| canonical workflows | 37 total / 37 active | verified | DB read-only |
| WF-000 | HTTP 200 | verified | safe POST |
| WF-001 -> WF-010 | pending | must test | final recovery proof |
| Ollama | VERIFY FROM REPO | unknown in this evidence | do not assume |
| Open WebUI | VERIFY FROM REPO | unknown in this evidence | do not assume |
| Operator API | VERIFY FROM REPO | unknown in this evidence | do not assume |
