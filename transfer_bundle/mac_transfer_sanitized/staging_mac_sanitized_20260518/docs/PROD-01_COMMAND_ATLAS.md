# Shadow Creator OS - PROD-01 Command Atlas (Cheat Sheet)

**Version**: 1.0.0  
**Date**: 2026-05-05  
**Purpose**: Fast reference for all commands organized by use case  
**Tip**: Copy-paste these commands directly into PowerShell

---

## SECTION 1: STARTUP & HEALTH

### Morning Startup (5-10 min)

```powershell
# Start all services (Windows)
npm run stack:start:windows

# Then wait 10 seconds
Start-Sleep -Seconds 10

# Verify all running
npm run health:check
```

### Daily Health Check (30 sec)

```powershell
npm run health:check

# Expected output:
# status: healthy
# All services: ✅
```

### Quick API Health

```powershell
# Operator API
curl http://127.0.0.1:5050/operator/health

# n8n
curl http://localhost:5678/api/v1/health

# Ollama
curl http://localhost:11434/api/tags
```

---

## SECTION 2: CREATE DOSSIER (4 Ways)

### Method 1: Open WebUI Chat (Easiest)

```
1. Browser: http://localhost:3000
2. Message: "Create YouTube script about [topic]"
3. Response: dossier_id in <5 sec
```

### Method 2: Ollama CLI

```powershell
echo "your topic here" | npm run operator:ollama

# Response: JSON with dossier_id
```

### Method 3: Direct API (curl)

```powershell
curl -X POST http://127.0.0.1:5050/operator/new-content-job `
  -Headers @{"Content-Type"="application/json"} `
  -Body (@{
    topic="AI tools for creators"
    context="YouTube video"
    mode="creator"
  } | ConvertTo-Json)
```

### Method 4: MCP (JSON-RPC)

```json
{
  "jsonrpc": "2.0",
  "id": "1",
  "method": "tools/call",
  "params": {
    "name": "create_content_job",
    "arguments": {
      "topic": "AI tools for creators",
      "context": "YouTube video",
      "mode": "creator"
    }
  }
}
```

---

## SECTION 3: MONITOR DOSSIER

### Get Dossier Status

```powershell
npm run dossier:inspect DOSSIER-xxxxx

# Or via API:
curl http://127.0.0.1:5050/operator/dossier/DOSSIER-xxxxx
```

### Poll Until Ready (Script)

```powershell
$dossier_id = "DOSSIER-xxxxx"
$max_wait = 600  # 10 minutes
$poll_interval = 30  # seconds
$end_time = (Get-Date).AddSeconds($max_wait)

while ((Get-Date) -lt $end_time) {
    $status = curl http://127.0.0.1:5050/operator/dossier/$dossier_id | ConvertFrom-Json
    
    Write-Host "Status: $($status.status)"
    
    if ($status.status -like "*READY_FOR_APPROVAL*") {
        Write-Host "✅ Dossier ready for approval!"
        break
    }
    
    Start-Sleep -Seconds $poll_interval
}
```

### List All Dossiers

```powershell
npm run dossier:list

# Shows: ID, Status, Created, Progress
```

---

## SECTION 4: APPROVE / MODIFY (Founder Only)

### Approve Dossier

```powershell
curl -X POST http://127.0.0.1:5050/operator/approve/DOSSIER-xxxxx `
  -Headers @{"Content-Type"="application/json"} `
  -Body (@{reviewer="founder"} | ConvertTo-Json)
```

### Request Changes

```powershell
curl -X POST http://127.0.0.1:5050/operator/remodify/DOSSIER-xxxxx `
  -Headers @{"Content-Type"="application/json"} `
  -Body (@{
    instructions="Make it shorter, add hook, casual tone"
    reviewer="founder"
  } | ConvertTo-Json)

# WF-200 replays with new instructions
# +30-120 seconds
```

### Replay Stage (if error)

```powershell
curl -X POST http://127.0.0.1:5050/operator/replay/DOSSIER-xxxxx `
  -Headers @{"Content-Type"="application/json"} `
  -Body (@{
    stage="WF-200"
    checkpoint="latest"
    instructions="new instructions (optional)"
  } | ConvertTo-Json)
```

---

## SECTION 5: VIEW GENERATED CONTENT

### List Packets (Outputs)

```powershell
npm run packet:list

# Or for specific dossier:
curl http://127.0.0.1:5050/operator/outputs/DOSSIER-xxxxx
```

### Inspect Packet Content

```powershell
npm run packet:inspect PKT-xxxxx

# Or manually:
Get-Content dossiers/DOSSIER-xxxxx/PKT-xxxxx.json | ConvertFrom-Json | Select-Object -ExpandProperty script
```

### View Packet Lineage

```powershell
npm run packet:lineage DOSSIER-xxxxx

# Shows: how packets flow through dossier
```

---

## SECTION 6: SYSTEM HEALTH & ALERTS

### All Alerts

```powershell
curl http://127.0.0.1:5050/operator/alerts

# Or CLI:
npm run operator:health
```

### Acknowledge Alert

```powershell
curl -X POST http://127.0.0.1:5050/operator/alerts/[alert_id]/acknowledge
```

### Escalate Alert (to Founder)

```powershell
curl -X POST http://127.0.0.1:5050/operator/alerts/[alert_id]/escalate `
  -Body (@{note="Critical issue"} | ConvertTo-Json)
```

### Metrics

```powershell
npm run metrics:daily

# Shows:
# - Success rate
# - Avg cycle time
# - Error count
# - Cost (if PROD-02)
```

---

## SECTION 7: TROUBLESHOOTING & RECOVERY

### Check Errors

```powershell
npm run errors:list

# Shows all errors with timestamps and details
```

### Database Verify

```powershell
npm run db:verify

# ✅ PASS: Database consistent
# ❌ FAIL: Inconsistencies found
```

### Validate Everything

```powershell
npm run validate:all

# Checks:
# - Workflows
# - Schemas
# - Registries
# - Dossiers
```

### Get Dossier Debug Trace

```powershell
curl http://127.0.0.1:5050/operator/troubleshoot/dossier/DOSSIER-xxxxx

# Shows:
# - Workflow execution log
# - State transitions
# - Errors at each step
```

### View System Logs

```powershell
npm run logs:view

# Latest logs from all services
# Or:
npm run logs:view | Select-String "ERROR" | head -20
```

---

## SECTION 8: MAINTENANCE & CLEANUP

### Clean Logs

```powershell
npm run logs:clean

# Removes logs older than 30 days
```

### Archive Old Dossiers

```powershell
npm run dossier:archive

# Archive dossiers older than 90 days
```

### Backup Dossiers

```powershell
Copy-Item "dossiers\*" -Destination "D:\Backup_$(Get-Date -Format 'yyyy-MM-dd')" -Recurse

# Or full stack backup:
Copy-Item "C:\ShadowEmpire-Git_Restore_01\dossiers\*" `
  "D:\Backup_$(Get-Date -Format 'yyyy-MM-dd')\dossiers\" -Recurse -Force
```

---

## SECTION 9: MODES & OPERATIONAL STATES

### Check Current Mode

```powershell
curl http://127.0.0.1:5050/operator/mode/state

# Shows: current_mode, enabled_operational_modes, runtime_module
```

### Set Mode (Founder Only)

```powershell
# Creator mode (default)
curl -X POST http://127.0.0.1:5050/operator/modes/set `
  -Body (@{mode="creator"} | ConvertTo-Json)

# Founder mode
curl -X POST http://127.0.0.1:5050/operator/modes/set `
  -Body (@{mode="founder"} | ConvertTo-Json)

# Operator mode
curl -X POST http://127.0.0.1:5050/operator/modes/set `
  -Body (@{mode="operator"} | ConvertTo-Json)

# Builder mode
curl -X POST http://127.0.0.1:5050/operator/modes/set `
  -Body (@{mode="builder"} | ConvertTo-Json)
```

### Enable Operational Mode

```powershell
# Alert Mode
curl -X POST http://127.0.0.1:5050/operator/modes/operational/alert/enable `
  -Body (@{actor_mode="operator"} | ConvertTo-Json)

# Troubleshoot Mode
curl -X POST http://127.0.0.1:5050/operator/modes/operational/troubleshoot/enable `
  -Body (@{actor_mode="builder"} | ConvertTo-Json)

# Debug Mode
curl -X POST http://127.0.0.1:5050/operator/modes/operational/debug/enable `
  -Body (@{actor_mode="builder"} | ConvertTo-Json)

# Analysis Dashboard
curl -X POST http://127.0.0.1:5050/operator/modes/operational/analysis/enable `
  -Body (@{actor_mode="operator"} | ConvertTo-Json)
```

---

## SECTION 10: NPM SCRIPTS (Complete List)

### Operator & API

```
npm run operator:start              ← Start Operator API (localhost:5050)
npm run operator:health             ← Check Operator health
npm run operator:ollama             ← CLI tool runner
npm run operator:mcp                ← Start MCP server (JSON-RPC)
npm run operator:test               ← Run acceptance tests
npm run stack:start:windows         ← Start all services (Windows)
```

### Health & Validation

```
npm run health:check                ← Full system health
npm run db:verify                   ← Database integrity check
npm run validate:all                ← Validate everything
npm run validate:workflows          ← Validate workflows
npm run validate:schemas            ← Validate JSON schemas
npm run validate:registries         ← Validate registries
npm run validate:dossiers           ← Validate dossier files
```

### Dossier Management

```
npm run dossier:list                ← List all dossiers
npm run dossier:inspect [ID]        ← Inspect one dossier
npm run dossier:archive [ID]        ← Archive old dossier
npm run dossier:delete [ID]         ← DELETE dossier (danger!)
```

### Packet & Packet Management

```
npm run packet:list                 ← List all packets
npm run packet:inspect [ID]         ← Inspect packet content
npm run packet:lineage [DOS-ID]     ← View packet flow
```

### Error & Event Management

```
npm run errors:list                 ← List all errors
npm run errors:clear                ← CLEAR all errors (danger!)
```

### Metrics & Reporting

```
npm run metrics:daily               ← Daily performance metrics
npm run metrics:weekly              ← Weekly trend analysis
npm run cost:report                 ← Cost per dossier (PROD-02+)
```

### Logs & Cleanup

```
npm run logs:view                   ← View system logs
npm run logs:clean                  ← Clean logs > 30 days
```

### n8n Workflow Management

```
npm run n8n:start                   ← Start n8n workflows (localhost:5678)
npm run n8n:stop                    ← Stop n8n
npm run n8n:status                  ← Check n8n status
```

### Open WebUI

```
npm run webui:start                 ← Start Open WebUI (localhost:3000)
npm run webui:setup                 ← Setup Open WebUI
```

---

## SECTION 11: API ENDPOINTS (All 28+)

### Core Operations

```
GET  /operator/health                          ← System health
GET  /operator/modes                           ← Available modes
GET  /operator/mode/state                      ← Current mode
POST /operator/modes/set                       ← Change mode
POST /operator/runtime/set                     ← Change runtime
POST /operator/modes/operational/:id/enable    ← Enable operational mode
POST /operator/modes/operational/:id/disable   ← Disable operational mode
POST /operator/modes/permission-check          ← Check access
GET  /operator/routes                          ← Available routes
```

### Dossier Operations

```
POST /operator/new-content-job                 ← Create dossier
GET  /operator/dossier/:id                     ← Inspect dossier
GET  /operator/dossier/:id/timeline            ← Execution timeline
GET  /operator/dossier/:id/outputs             ← List packets
GET  /operator/library                         ← Full library
POST /operator/approve/:id                     ← Approve output
POST /operator/remodify/:id                    ← Request changes
POST /operator/replay/:id                      ← Replay stage
```

### Alerts & Events

```
GET  /operator/alerts                          ← List alerts
POST /operator/alerts/:id/acknowledge          ← Acknowledge alert
POST /operator/alerts/:id/escalate             ← Escalate alert
GET  /operator/events                          ← List events
GET  /operator/runs/:id/status                 ← Run status
```

### Debugging

```
GET  /operator/troubleshoot/dossier/:id        ← Dossier trace
GET  /operator/troubleshoot/packet/:id         ← Packet trace
GET  /operator/providers                       ← List providers
GET  /operator/providers/:id                   ← Provider status
GET  /operator/tasks                           ← List tasks
```

---

## SECTION 12: WORKFLOW REFERENCE

### Workflow IDs & Purposes

```
WF-001    Dossier Create          [Creates fresh dossier]
WF-010    Parent Orchestrator     [Routes to appropriate lane]
WF-100    Topic Intelligence      [Research] (30-60 sec)
WF-200    Script Generation       [Writing] (30-120 sec)
WF-300    Design Planning         [Layout] (STRUCTURE READY)
WF-400    Production Planning     [Assembly prep] (STRUCTURE READY)
WF-500    Publishing Prep         [Distribution] (STRUCTURE READY)
WF-020    Approval Handler        [Final gate] (STRUCTURE READY)
WF-021    Replay-Remodify         [Re-execute with changes] (WORKING)

WF-600+   Provider Handlers       [Media generation] (BLOCKED in PROD-01)
WF-610    Image Generation        (provider_bridge_required)
WF-620    Voice Generation        (provider_bridge_required)
WF-630    Music Generation        (provider_bridge_required)
WF-640    Video Assembly          (provider_bridge_required)
WF-650    Avatar Generation       (provider_bridge_required)
WF-660    Publishing              (provider_bridge_required)

WF-900    Alert Handler           (error recovery)
WF-910    Troubleshoot Engine     (diagnostics)
WF-920    Analytics Aggregator    (metrics)
WF-930    Learning Engine         (optimization)
```

---

## SECTION 13: QUICK PROBLEM SOLVING

### "System won't start"
```powershell
npm run health:check
# If fails, check each service:
# - Ollama: Start from Start menu
# - n8n: npm run n8n:start
# - API: npm run operator:start
```

### "Dossier stuck (>2 min)"
```powershell
curl http://127.0.0.1:5050/operator/troubleshoot/dossier/DOSSIER-xxxxx

# Check for errors in trace
# If timeout: curl http://localhost:11434/api/tags
# (Ollama may be slow)
```

### "Approval not working"
```powershell
# Verify you're in founder mode:
curl http://127.0.0.1:5050/operator/mode/state | Select-String "founder"

# If not founder, set it:
curl -X POST http://127.0.0.1:5050/operator/modes/set `
  -Body (@{mode="founder"} | ConvertTo-Json)
```

### "No outputs generated"
```powershell
curl http://127.0.0.1:5050/operator/outputs/DOSSIER-xxxxx

# Should show: packets list
# If empty: WF-200 failed, check trace
```

### "Tool menu not in Open WebUI"
```powershell
# Clear browser cache
# Ctrl+Shift+Delete in Chrome
# Re-import tool (Admin panel → Tools)
# Refresh browser
```

---

## SECTION 14: WEEKLY CHECKLIST (Copy & Run)

```powershell
Write-Host "=== WEEKLY MAINTENANCE ===" -ForegroundColor Green

Write-Host "1. Cleaning logs..."
npm run logs:clean

Write-Host "2. Archiving old dossiers..."
npm run dossier:archive

Write-Host "3. Database verification..."
npm run db:verify

Write-Host "4. Weekly metrics..."
npm run metrics:weekly

Write-Host "5. Backing up dossiers..."
Copy-Item "dossiers\*" `
  "D:\Backup_$(Get-Date -Format 'yyyy-MM-dd')\dossiers\" `
  -Recurse -Force

Write-Host "=== COMPLETE ===" -ForegroundColor Green
```

---

## SECTION 15: ENVIRONMENT & PORTS

### Service Ports

```
localhost:11434     Ollama (LLM)
localhost:5678      n8n (Workflows)
localhost:5050      Operator API (Control)
localhost:3000      Open WebUI (Chat)
```

### Environment Variables (Optional)

```powershell
$env:LOG_LEVEL="info"               # or "debug", "warn", "error"
$env:NODE_ENV="production"          # or "development"
$env:OLLAMA_HOST="localhost:11434"  # Ollama address
$env:N8N_HOST="localhost:5678"      # n8n address
```

### Important Directories

```
C:\ShadowEmpire-Git_Restore_01\
  ├── dossiers\                      ← Dossier storage
  ├── data\                          ← Indexes and metadata
  ├── engine\                        ← API and workflows
  ├── operator\                      ← CLI and MCP tools
  ├── registries\                    ← Configuration files
  ├── scripts\windows\               ← PowerShell startup scripts
  └── config\                        ← Tool configs
```

---

**Status**: ✅ PROD-01 COMMAND ATLAS COMPLETE  
**Commands Verified**: 60+ npm scripts + 28+ API endpoints  
**Last Updated**: 2026-05-05

---

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

## Current Production Runtime Commands - Restore_01 Profile

A. Check n8n listener:

```powershell
Get-Process node -ErrorAction SilentlyContinue | Select-Object Id,ProcessName,Path,StartTime
Get-NetTCPConnection -LocalPort 5678 -ErrorAction SilentlyContinue
Get-NetTCPConnection -LocalPort 5679 -ErrorAction SilentlyContinue
```

B. Start n8n correctly:

```powershell
cd C:\ShadowEmpire-Git_Restore_01
powershell -ExecutionPolicy Bypass -File .\scripts\windows\start_n8n_shadow_phase1.ps1
```

C. Verify n8n status:

```powershell
npm run n8n:status
```

Expected:

```text
200 {"status":"ok"}
```

D. Correct n8n UI:

```text
http://127.0.0.1:5678/home/workflows
```

E. Do not use:

```text
http://127.0.0.1:5678/workflow/<old-id>
```

F. Verify WAL activity:

```powershell
Get-Item "C:\ShadowEmpire\n8n_user_restore_01\.n8n\database.sqlite-wal" | Select FullName,Length,LastWriteTime
Get-Item "C:\ShadowEmpire\n8n_user\.n8n\database.sqlite-wal" | Select FullName,Length,LastWriteTime
```

G. Verify repo:

```bash
cd /c/ShadowEmpire-Git_Restore_01
git status
git remote -v
git branch -a
git log --oneline -10
git rev-parse HEAD
```

H. Operator/Open WebUI/Ollama placeholders:

Ollama command section: VERIFY FROM REPO BEFORE USE
Open WebUI command section: VERIFY FROM REPO BEFORE USE
Operator API command section: VERIFY FROM REPO BEFORE USE
PowerShell script section: VERIFY FROM REPO BEFORE USE
