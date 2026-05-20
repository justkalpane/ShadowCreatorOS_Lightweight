# Shadow Creator OS - PROD-01 Troubleshooting & Recovery Guide

**Version**: 2.0.0  
**Date**: 2026-05-05  
**Classification**: OPERATIONAL REFERENCE  
**Purpose**: Comprehensive guide to 20+ common issues and proven recovery procedures

---

## QUICK REFERENCE: ISSUE CATEGORIES

| Category | Issues | Impact | Priority |
|----------|--------|--------|----------|
| **Startup** | 1-5 | Can't start system | 🔴 CRITICAL |
| **Workflow** | 6-10 | Dossier stuck/failing | 🔴 CRITICAL |
| **Open WebUI** | 11-14 | Can't use UI | 🟡 HIGH |
| **Ollama** | 15-17 | Slow/no responses | 🟠 MEDIUM |
| **Data** | 18-20 | Data loss/corruption | 🔴 CRITICAL |

---

## ISSUE 1: n8n Fails to Start

**Symptom**: 
```
Error: n8n process exited with code 1
Port 5678 not responding
```

**Causes**:
- Port 5678 already in use (another process)
- n8n database corrupted
- SQLite lock file stale
- Node.js version mismatch

**Recovery**:

**Step 1: Check if port is in use**
```powershell
netstat -ano | Select-String "5678"
# If output shows a PID, the port is in use

# Kill the process using port
Get-Process -Id [PID] | Stop-Process -Force
```

**Step 2: Clear n8n locks**
```powershell
# n8n creates lock files, delete stale ones
Remove-Item "$env:APPDATA\.n8n" -Recurse -Force -ErrorAction SilentlyContinue

# Or for global install:
Remove-Item "C:\Program Files\n8n" -Recurse -Force -ErrorAction SilentlyContinue
```

**Step 3: Restart n8n**
```powershell
npm run n8n:start

# Or if that fails:
n8n start --forceStart
```

**Step 4: Verify startup**
```powershell
Start-Sleep -Seconds 10
curl http://localhost:5678/api/v1/health

# Should return: {"status": "ok"}
```

**If Still Failing**:
- Check if Node.js is installed: `node --version` (should be 18+)
- Check npm: `npm --version` (should be 8+)
- Reinstall n8n: `npm install -g n8n`

---

## ISSUE 2: Ollama Not Responding (localhost:11434 timeout)

**Symptom**:
```
curl: (28) Operation timed out
Ollama health check failed
ollama_request_timeout: 30000ms
```

**Causes**:
- Ollama service crashed or hung
- GPU memory exhausted (if using GPU)
- Model loading incomplete
- Firewall blocking localhost

**Recovery**:

**Step 1: Check if Ollama is running**
```powershell
Get-Process ollama -ErrorAction SilentlyContinue

# If not found, Ollama is not running
Start ollama serve
# Or from Start menu: Ollama
```

**Step 2: Check Ollama logs**
```powershell
# Ollama logs location (Windows):
# %APPDATA%\Ollama\logs\
Get-Content "$env:APPDATA\Ollama\logs\*" -Tail 50

# Look for error messages or OOM (Out of Memory)
```

**Step 3: If OOM error, reduce model size**
```powershell
# Current: mistral (7B parameters, ~4GB RAM)
# Alternative: phi2 (2.7B parameters, ~2GB RAM)

# Stop Ollama
Stop-Process -Name ollama

# Pull smaller model
ollama pull phi2

# Start Ollama again
ollama serve
```

**Step 4: Verify Ollama health**
```powershell
curl http://localhost:11434/api/tags

# Should list available models:
# {
#   "models": [
#     {"name": "mistral:latest", "size": 4200000000},
#     {"name": "llama3.2:latest", "size": 5500000000}
#   ]
# }
```

**If Still Hanging**:
- Kill and restart: `Stop-Process -Name ollama; Start-Sleep 5; ollama serve`
- Check system RAM: `Get-ComputerInfo | Select-Object Total*Memory`
- If RAM < 8GB, close other applications

---

## ISSUE 3: Operator API Returns 502 Bad Gateway

**Symptom**:
```
Error: 502 Bad Gateway
POST /operator/new-content-job returned 502
```

**Causes**:
- Operator API crashed
- n8n not responding (can't trigger workflows)
- SQLite database locked
- Missing environment variables

**Recovery**:

**Step 1: Check API is running**
```powershell
curl http://localhost:5050/operator/health

# If timeout or refused connection:
npm run operator:start
```

**Step 2: Verify n8n is running and healthy**
```powershell
curl http://localhost:5678/api/v1/health

# If fails, restart n8n (see Issue 1)
```

**Step 3: Check Operator API logs**
```powershell
npm run logs:view | Select-String "ERROR" | head -20

# Look for database locks or n8n connection errors
```

**Step 4: Clear database locks**
```powershell
# Find and remove SQLite lock file
Get-ChildItem -Path "dossiers" -Filter "*.db*" -Force

# If found, delete:
Remove-Item "dossiers\*.db-wal" -Force
Remove-Item "dossiers\*.db-shm" -Force

# Restart Operator API
npm run operator:start
```

**Step 5: Verify recovery**
```powershell
curl http://localhost:5050/operator/health

# Should return healthy status
```

---

## ISSUE 4: Dossier Creation Times Out (>30 seconds)

**Symptom**:
```
Timeout waiting for dossier creation
Error: "Dossier creation timed out after 30 seconds"
WF-001 triggered but no dossier file created
```

**Causes**:
- WF-001 failed silently (n8n error)
- Dossier index not updated
- Slow disk I/O
- Operator correlation issue

**Recovery**:

**Step 1: Check if WF-001 is registered**
```powershell
curl http://localhost:5678/api/v1/workflows

# Look for workflow_name = "WF-001" (Dossier Create)
# If not found, n8n workflows may not have loaded properly
```

**Step 2: Manually check dossiers directory**
```powershell
Get-ChildItem dossiers\ -Filter "DOSSIER-*.json" | Sort-Object LastWriteTime -Descending | head -3

# Should show recently created dossier files
# If nothing new, WF-001 is not executing
```

**Step 3: Check dossier index**
```powershell
Get-Content data/se_dossier_index.json | ConvertFrom-Json

# Count records
# If count hasn't changed, WF-001 didn't create dossier
```

**Step 4: Inspect WF-001 execution in n8n**
```powershell
# Open n8n: http://localhost:5678
# Click Workflows → WF-001 (Dossier Create)
# Look for execution errors in the logs
# If webhook didn't fire, check webhook registry
```

**Step 5: Restart webhook registry**
```powershell
# n8n webhooks are registered in memory
# Restart n8n to reload:
npm run n8n:stop
Start-Sleep 5
npm run n8n:start

# Try creating dossier again
```

---

## ISSUE 5: Dossier Stuck in "WF-100 EXECUTING" Status (>2 minutes)

**Symptom**:
```
inspect_dossier returns:
  "status": "WF-100 EXECUTING"
  (for 5+ minutes with no progress)
```

**Causes**:
- WF-100 (research workflow) hit timeout in Ollama
- Ollama generating response indefinitely
- WF-100 node error (not catching exception)

**Recovery**:

**Step 1: Check Ollama is responsive**
```powershell
# Try a quick Ollama request
curl -X POST http://localhost:11434/api/generate `
  -Body (@{model="mistral"; prompt="Hi"} | ConvertTo-Json) `
  -Headers @{"Content-Type"="application/json"}

# Should return within 10 seconds
# If timeout, Ollama is stuck (see Issue 2)
```

**Step 2: Check n8n WF-100 execution**
```powershell
# http://localhost:5678 → Workflows → WF-100
# Look at execution queue
# Is there a "running" execution that's not progressing?

# If yes, manually stop it:
# (In n8n UI) Right-click execution → Stop
```

**Step 3: Operator can trigger replay**
```powershell
curl -X POST http://127.0.0.1:5050/operator/replay/DOSSIER-xxxxx `
  -Headers @{"Content-Type"="application/json"} `
  -Body (@{
    stage="WF-100"
    checkpoint="latest"
  } | ConvertTo-Json)

# This will restart WF-100 from scratch
```

**Step 4: If replay also times out**
```powershell
# Escalate to Founder for decision
curl -X POST http://127.0.0.1:5050/operator/alerts/[alert_id]/escalate `
  -Body (@{note="WF-100 consistent timeout; possible Ollama issue"} | ConvertTo-Json)

# May need to reduce model size or enable cloud models (PROD-02)
```

---

## ISSUE 6: Open WebUI Chat Tool Not Appearing in Dropdown

**Symptom**:
```
Click "/" in Open WebUI chat
Tool menu appears but "Shadow Operator Core" not listed
```

**Causes**:
- Tool not imported
- Tool import failed
- Browser cache issue
- n8n not connected to Open WebUI

**Recovery**:

**Step 1: Clear browser cache**
```powershell
# Close Open WebUI browser tab
# Clear Chrome/Edge cache:
#   Settings → Privacy and security → Clear browsing data
#   (Check: Cookies and other site data, Cached images and files)
# Refresh: http://localhost:3000
```

**Step 2: Re-import tool**
```
Open WebUI Admin Panel:
  1. http://localhost:3000/admin
  2. Click "Tools"
  3. "Create New Tool"
  4. Paste entire contents of: config/openwebui_shadow_operator_tools_v3.py
  5. Click "Save"
  6. Refresh chat page
```

**Step 3: Verify tool appears**
```
Open WebUI Chat:
  1. New Chat
  2. Click "/" button
  3. Should see "Shadow Operator Core" in list
  4. Click it, see 9 methods listed
```

**If Still Not Appearing**:
- Check if n8n is running: `curl http://localhost:5678/api/v1/health`
- Check Operator API: `curl http://localhost:5050/operator/health`
- Check Open WebUI logs: `npm run logs:view`
- Restart Open WebUI: `npm run webui:start`

---

## ISSUE 7: Tool Invocation Fails (OpenWebUI Says "Tool Error")

**Symptom**:
```
Chat message: Use create_content_job tool
Error displayed: "Tool error: ..."
No response from tool
```

**Causes**:
- Operator API not running
- Tool parameters malformed
- Network connectivity issue
- API endpoint URL incorrect in tool config

**Recovery**:

**Step 1: Verify Operator API health**
```powershell
curl http://127.0.0.1:5050/operator/health

# If fails, restart:
npm run operator:start
```

**Step 2: Test tool directly via curl**
```powershell
curl -X POST http://127.0.0.1:5050/operator/new-content-job `
  -Headers @{"Content-Type"="application/json"} `
  -Body (@{
    topic="test"
    context="YouTube video"
    mode="creator"
  } | ConvertTo-Json)

# Should return valid JSON response
# If fails, check API logs
```

**Step 3: Verify tool Python code**
```powershell
# Tool location (if using): config/openwebui_shadow_operator_tools_v3.py
# Check:
#  1. API endpoint URL is http://127.0.0.1:5050
#  2. Method names match (no typos)
#  3. Parameters are optional with guards
#  4. Return is JSON string (not dict)
```

**Step 4: Re-import tool if code correct**
```
Open WebUI → Admin → Tools
Delete existing "Shadow Operator Core"
Re-import from config/openwebui_shadow_operator_tools_v3.py
```

---

## ISSUE 8: Script Approval Works But Dossier Stays in APPROVED Status Too Long

**Symptom**:
```
Founder approved dossier → status became "APPROVED"
But WF-020 (approval handler) not triggering
Dossier stuck for 5+ minutes
```

**Causes**:
- WF-020 not registered in n8n
- Webhook for approval event not firing
- Dossier update not reflected in index

**Recovery**:

**Step 1: Check WF-020 is registered**
```powershell
curl http://localhost:5678/api/v1/workflows | Select-String "WF-020"

# If not found, workflows may not have loaded
```

**Step 2: Manually inspect dossier state**
```powershell
curl http://127.0.0.1:5050/operator/dossier/DOSSIER-xxxxx

# Check:
#  - approval_status: should be "APPROVED"
#  - approval_timestamp: should be recent
#  - wf020_status: should show execution details
```

**Step 3: If WF-020 didn't execute, manually trigger it**
```powershell
# n8n direct webhook (use with caution)
# Only if approve endpoint returned success (HTTP 200)

curl -X POST http://localhost:5678/webhook/approval-handler `
  -Body (@{
    dossier_id="DOSSIER-xxxxx"
    decision="approved"
  } | ConvertTo-Json)
```

**Step 4: Verify approval completed**
```powershell
curl http://127.0.0.1:5050/operator/dossier/DOSSIER-xxxxx

# Status should now show: "LOCKED_FOR_DISTRIBUTION" or similar
```

---

## ISSUE 9: Request Changes Works But WF-200 Replay Generates Same Script

**Symptom**:
```
Founder requests changes with instructions
WF-200 replays
But PKT-script-002 is identical to PKT-script-001
(instructions were ignored)
```

**Causes**:
- Instructions not passed to Ollama prompt
- Ollama caching responses (rare)
- WF-200 not reading instructions from dossier

**Recovery**:

**Step 1: Verify instructions were saved**
```powershell
curl http://127.0.0.1:5050/operator/dossier/DOSSIER-xxxxx | Select-Object audit_trail

# Should show entry like:
# {
#   "action": "request_changes",
#   "actor": "founder",
#   "instructions": "Make it shorter, add hook",
#   "timestamp": "2026-05-05T13:00:00Z"
# }
```

**Step 2: Check WF-200 execution logs**
```powershell
# Enable debug mode
curl -X POST http://127.0.0.1:5050/operator/modes/operational/debug/enable `
  -Body (@{actor_mode="builder"} | ConvertTo-Json)

# Trace WF-200 execution
curl http://127.0.0.1:5050/operator/troubleshoot/dossier/DOSSIER-xxxxx | Select-String "WF-200"

# Look for: "Instructions provided: [should show founder instructions]"
```

**Step 3: If instructions not in trace, WF-021 issue**
```powershell
# Check WF-021 (replay-remodify) passed instructions correctly
# Look in n8n logs at http://localhost:5678

# WF-021 should:
#  1. Read dossier
#  2. Extract latest instructions
#  3. Pass to WF-200 as context
```

**Step 4: Manual fix (last resort)**
```powershell
# Operator can manually trigger replay with new topic/context
# (Developer intervention needed; file issue for PROD-02 fix)
```

---

## ISSUE 10: Error Alert Never Clears (Stuck in Alert History)

**Symptom**:
```
check_alerts returns same error 10+ times
Acknowledging alert doesn't remove it
```

**Causes**:
- Alert immutability (by design - can't be deleted)
- Error condition still active (triggering re-alerts)
- Alert escalated and stuck in escalation queue

**Recovery**:

**Step 1: Check alert status**
```powershell
curl http://127.0.0.1:5050/operator/alerts | Select-String "acknowledged"

# Should show: "acknowledged": true (if you acknowledged it)
```

**Step 2: If acknowledged but still appears, it's immutable**
```powershell
# Alerts CANNOT be deleted (safety feature)
# They move to "acknowledged" status but remain in history

# To check acknowledged vs active:
curl http://127.0.0.1:5050/operator/alerts | Select-Object -ExpandProperty alerts | Where acknowledged -eq false

# This shows only UN-acknowledged alerts (active ones)
```

**Step 3: If error keeps re-triggering**
```powershell
# The root cause is still active
# E.g., if "Ollama timeout" alert keeps firing, Ollama is still timing out

# Acknowledge the alert and fix root cause
curl -X POST http://127.0.0.1:5050/operator/alerts/[alert_id]/acknowledge

# Then fix Ollama (see Issue 2)
# Once Ollama is healthy, no new alerts should fire
```

---

## ISSUE 11: Unicode Error When Starting Services

**Symptom**:
```
Error: UnicodeEncodeError: 'utf-8' codec can't encode...
PowerShell output contains non-ASCII characters
```

**Causes**:
- PowerShell default encoding not UTF-8
- Terminal environment encoding issue
- System locale not configured for UTF-8

**Recovery**:

**Step 1: Force UTF-8 encoding in PowerShell**
```powershell
# Add to PowerShell profile or run before startup:
$OutputEncoding = [System.Text.UTF8Encoding]::new($true)
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($true)
```

**Step 2: Use alternative startup command**
```powershell
# Instead of: npm run webui:start
# Use: open-webui serve --port 3000

# Or with explicit Python UTF-8:
$env:PYTHONIOENCODING="utf-8"
open-webui serve --port 3000
```

**Step 3: Verify encoding**
```powershell
$OutputEncoding

# Should show: System.Text.UTF8Encoding
```

---

## ISSUE 12: Dossier File Corrupted (Invalid JSON)

**Symptom**:
```
inspect_dossier returns error:
"Invalid JSON in dossier file"
File exists but cannot be read
```

**Causes**:
- Crash during write (incomplete file)
- Manual file edit corruption
- Disk write failure (out of space)

**Recovery**:

**Step 1: Check available disk space**
```powershell
Get-Volume | Where-Object DriveLetter -eq "C" | Select-Object SizeRemaining

# If < 1GB free, clean up:
npm run logs:clean
npm run dossier:archive

# If still full, move old dossiers to backup
```

**Step 2: Attempt to read and repair**
```powershell
# Backup corrupted file
Copy-Item "dossiers/DOSSIER-xxxxx.json" "dossiers/DOSSIER-xxxxx.json.bak"

# Try to repair using validator
npm run validate:dossiers

# Output should flag corrupted files
```

**Step 3: If repair fails**
```powershell
# Check if backup exists:
Get-ChildItem dossiers/ -Filter "DOSSIER-xxxxx*"

# If multiple backups exist, restore from older one:
Copy-Item "dossiers/DOSSIER-xxxxx.json.bak" "dossiers/DOSSIER-xxxxx.json"
```

**Step 4: Last resort - rollback from external backup**
```powershell
# If you have weekly backups (as recommended):
Copy-Item "D:\Backup_2026-05-05\dossiers\DOSSIER-xxxxx.json" "dossiers\"

# Verify restoration
curl http://127.0.0.1:5050/operator/dossier/DOSSIER-xxxxx
```

---

## ISSUE 13: API Endpoint Not Found (404)

**Symptom**:
```
curl: (22) HTTP error 404
GET /operator/health returns 404 (instead of 200)
```

**Causes**:
- Operator API routing not loaded
- Wrong port (not 5050)
- API process crashed partially

**Recovery**:

**Step 1: Verify API is running**
```powershell
netstat -ano | Select-String "5050"

# If no output, API not listening on 5050
npm run operator:start
```

**Step 2: Verify routes are registered**
```powershell
# Check operator.js file exists and loads all routes
Get-Content engine/api/operator.js | Select-String "router.get.*health" | head -1

# Should show: router.get('/health', ...)
```

**Step 3: Check for startup errors**
```powershell
npm run operator:start 2>&1 | Select-String "error" -ErrorAction SilentlyContinue

# Look for route registration errors
```

**Step 4: Restart from clean state**
```powershell
# Kill any hanging processes
Stop-Process -Name node -Force -ErrorAction SilentlyContinue

# Start fresh
npm run operator:start
Start-Sleep 5

# Verify health
curl http://127.0.0.1:5050/operator/health
```

---

## ISSUE 14: Rate Limiting - Too Many Requests (429)

**Symptom**:
```
HTTP 429: Too Many Requests
"Rate limit exceeded"
```

**Causes**:
- Creating dossiers too fast (no delay between requests)
- Polling inspect_dossier too frequently
- Batch script without rate limiting

**Recovery**:

**Step 1: Reduce request rate**
```powershell
# If creating multiple dossiers:
foreach ($topic in $topics) {
    Write-Host "Creating: $topic"
    
    $result = echo $topic | npm run operator:ollama | ConvertFrom-Json
    Write-Host "Dossier: $($result.dossier_id)"
    
    # ADD DELAY (required)
    Start-Sleep -Seconds 2-3  # ← CRITICAL
}
```

**Step 2: Reduce polling frequency**
```powershell
# Instead of: polling every 5 seconds
# Do: polling every 30 seconds

Start-Sleep -Seconds 30
curl http://127.0.0.1:5050/operator/dossier/$dossierId
```

**Step 3: If rate limit still hit**
```powershell
# Check Operator API rate limit settings
Get-Content engine/api/operator.js | Select-String "rateLimit"

# Default rate limit is typically:
# 100 requests per minute per IP

# Contact developer if limit is too restrictive
```

---

## ISSUE 15: Metrics Report Shows 0% Success Rate

**Symptom**:
```
npm run metrics:daily
Success rate: 0%
All dossiers: "FAILED"
```

**Causes**:
- All dossiers actually failed (WF-001 or WF-010 errors)
- Metrics aggregation broken
- No dossiers in index

**Recovery**:

**Step 1: Check dossier count**
```powershell
npm run dossier:list

# Should show: "Total dossiers: X"
# If 0, no dossiers created yet (not an error, just no data)
```

**Step 2: Check individual dossier status**
```powershell
npm run dossier:list | Select-String "status" | head -10

# Look for: "READY_FOR_APPROVAL", "APPROVED", "ERROR", "WF-200 EXECUTING"
# If all show "ERROR", check last dossier for root cause
```

**Step 3: Inspect latest failed dossier**
```powershell
npm run dossier:list | tail -3  # Get 3 most recent

# Then:
npm run dossier:inspect [LATEST_DOSSIER_ID]

# Check error field for reason
```

**Step 4: Fix root cause**
```powershell
# Common causes:
# 1. WF-001 failed → Check n8n workflow
# 2. WF-010 failed → Check routing configuration
# 3. Ollama timeout → See Issue 2
# 4. No storage space → See Issue 12

# After fix, create new test dossier
curl -X POST http://127.0.0.1:5050/operator/new-content-job `
  -Body (@{topic="test"; context="YouTube video"; mode="creator"} | ConvertTo-Json)

# Wait 5 minutes, check status
```

---

## ISSUE 16: Missing Dossier Index File (se_dossier_index.json)

**Symptom**:
```
File not found: data/se_dossier_index.json
Operator can't find dossiers
```

**Causes**:
- Index never created (first startup issue)
- File deleted accidentally
- Permission error preventing creation

**Recovery**:

**Step 1: Create index manually**
```powershell
# Create empty index if missing:
$emptyIndex = @{
    version = "1.0.0"
    generated_at = (Get-Date).ToUniversalTime().ToString("o")
    records = @()
} | ConvertTo-Json

$emptyIndex | Set-Content data/se_dossier_index.json -Encoding UTF8
```

**Step 2: Rebuild index from existing dossier files**
```powershell
# Scan dossiers directory and rebuild
npm run validate:dossiers --rebuild-index

# Or manually:
$dossiers = @()
Get-ChildItem dossiers/ -Filter "DOSSIER-*.json" | ForEach-Object {
    $content = Get-Content $_.FullName | ConvertFrom-Json
    $dossiers += @{
        dossier_id = $content.dossier_id
        created_at = $content.created_at
        status = $content.status
    }
}

$index = @{
    version = "1.0.0"
    records = $dossiers
} | ConvertTo-Json -Depth 10

$index | Set-Content data/se_dossier_index.json -Encoding UTF8
```

**Step 3: Verify index**
```powershell
curl http://127.0.0.1:5050/operator/dossier/[ANY_ID]

# Should now find dossier
```

---

## ISSUE 17: System Running Out of Disk Space

**Symptom**:
```
Error: "No space left on device"
Dossier creation fails
```

**Causes**:
- Large number of dossiers accumulated
- Log files not cleaned up
- Backup directory on same drive

**Recovery**:

**Step 1: Check disk usage**
```powershell
Get-Volume | Select-Object DriveLetter, Size, SizeRemaining | Format-Table

# Find % used:
$vol = Get-Volume -DriveLetter C
$percentUsed = [math]::Round(($vol.Size - $vol.SizeRemaining) / $vol.Size * 100, 1)
Write-Host "Drive C: $percentUsed% used"
```

**Step 2: Clean logs**
```powershell
npm run logs:clean

# This deletes logs older than 30 days
# Typical cleanup: 500MB-2GB freed
```

**Step 3: Archive old dossiers**
```powershell
# Archive dossiers older than 90 days
npm run dossier:archive --older-than=90

# Moves to archive directory (keeps them, just organized)
# Typical cleanup: 1-5GB freed depending on count
```

**Step 4: Move backups if on same drive**
```powershell
# If backup is on C:\, move to external drive
Get-ChildItem D:\Backup* -ErrorAction SilentlyContinue | Move-Item -Destination E:\Archives\

# Frees space for new dossiers
```

**Step 5: Monitor going forward**
```powershell
# Weekly: npm run logs:clean
# Monthly: npm run dossier:archive
# This keeps disk usage under control
```

---

## ISSUE 18: Provider Credentials Exposed in Logs (PROD-02+)

**Symptom**:
```
API key visible in log file
npm run logs:view shows "api_key: sk_xxxxx"
```

**Causes**:
- Debug logging enabled during provider activation
- Error traceback includes full environment
- Credential not masked in log message

**Recovery**:

**Step 1: Immediately revoke exposed credential**
```powershell
# For OpenAI:
# 1. Go to https://platform.openai.com/account/api-keys
# 2. Revoke the exposed key
# 3. Create new key
# 4. Update Operator API with new key

# For ElevenLabs:
# 1. Go to https://elevenlabs.io/account
# 2. Revoke exposed key
# 3. Create new key
# 4. Update configuration
```

**Step 2: Clear logs**
```powershell
npm run logs:clean

# Removes all log files containing the exposed credential
```

**Step 3: Enable secure logging**
```powershell
# In PROD-02, disable debug mode after issue fixed
curl -X POST http://127.0.0.1:5050/operator/modes/operational/debug/disable `
  -Body (@{actor_mode="operator"} | ConvertTo-Json)

# Set log level to WARNING (not DEBUG)
$env:LOG_LEVEL="warning"
npm run operator:start
```

**Step 4: Audit dossiers for cost abuse**
```powershell
# Check if exposed key was used to generate unauthorized requests
npm run cost:report

# If cost spike detected, contact provider support for dispute
```

---

## ISSUE 19: Dossier Approval Locked in Unknown State

**Symptom**:
```
Dossier status shows: "APPROVAL_LOCKED_UNKNOWN"
Can't create, can't approve, can't modify
```

**Causes**:
- WF-020 crashed mid-execution
- Approval gate deadlock
- Data corruption during approval

**Recovery**:

**Step 1: Check dossier audit trail**
```powershell
curl http://127.0.0.1:5050/operator/dossier/DOSSIER-xxxxx | Select-Object audit_trail

# Look for: "approval_status: LOCKED_UNKNOWN"
# Previous action should show what happened
```

**Step 2: Try operator replay of WF-020**
```powershell
curl -X POST http://127.0.0.1:5050/operator/replay/DOSSIER-xxxxx `
  -Body (@{
    stage="WF-020"
    checkpoint="latest"
  } | ConvertTo-Json)

# This re-executes approval handler
# May unstick the state
```

**Step 3: If replay fails**
```powershell
# Escalate to Founder - manually unlock
curl -X POST http://127.0.0.1:5050/operator/alerts/[alert_id]/escalate `
  -Body (@{note="Dossier stuck in APPROVAL_LOCKED_UNKNOWN; needs manual intervention"} | ConvertTo-Json)

# Developer intervention needed
# (Not a standard recovery in PROD-01)
```

---

## ISSUE 20: Database Consistency Check Fails

**Symptom**:
```
npm run db:verify
Result: FAILED
Database inconsistency detected
```

**Causes**:
- Dossier not in index but file exists
- Packet referenced but file missing
- Audit trail incomplete

**Recovery**:

**Step 1: Run detailed validation**
```powershell
npm run validate:dossiers

# Output shows:
# ✅ 145 dossiers valid
# ⚠️  3 dossiers missing from index
# ❌ 1 packet orphaned
```

**Step 2: Rebuild index**
```powershell
# Remove old index
Remove-Item data/se_dossier_index.json

# Rebuild from dossier files
# (See Issue 16 for detailed steps)

npm run db:verify

# Should now show PASS
```

**Step 3: Clean orphaned packets**
```powershell
# Identify packets with no dossier reference
npm run packet:list | Where-Object orphaned -eq true

# Manual cleanup (requires developer if critical):
# Verify packet isn't needed
# Delete: Remove-Item "packets/[PKT-ID].json"
```

**Step 4: Verify recovery**
```powershell
npm run db:verify

# Should return: "Database consistent"
npm run health:check

# All components healthy
```

---

## RECOVERY CHECKLISTS

### Daily Health Check

```
☐ npm run health:check                    (should all show ✅)
☐ curl http://127.0.0.1:5050/operator/alerts  (should be empty)
☐ npm run dossier:list | head -5          (should show recent dossiers)
☐ npm run errors:list | Select-String ERROR  (check for new errors)
☐ npm run metrics:daily                   (success rate > 95%)
```

### Weekly Maintenance

```
☐ npm run logs:clean                      (deletes logs > 30 days)
☐ npm run dossier:archive                 (archives dossiers > 90 days)
☐ npm run db:verify                       (check consistency)
☐ npm run cost:report                     (if PROD-02, check spend)
☐ Copy-Item dossiers\* -Destination D:\Backup_$(date)  (backup)
```

### Monthly Review

```
☐ npm run metrics:weekly                  (review trends)
☐ npm run validate:all                    (full validation)
☐ Check disk usage: Get-Volume            (ensure < 80% used)
☐ Review error patterns: npm run errors:list
☐ Plan infrastructure changes if needed
```

---

**Status**: ✅ PROD-01 COMPREHENSIVE TROUBLESHOOTING GUIDE  
**Coverage**: 20+ issues with recovery procedures  
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

## n8n Wrong-Profile Recovery Protocol - 2026-05-06

Incident summary:
The system showed only old workflows because n8n was started from the wrong profile path. The repo was not proven damaged. The runtime profile was misdirected.

Symptoms:
- only old workflows visible.
- "workflow without permissions" errors.
- old editor bookmarks failing.
- workflows appear missing even though repo and another DB/profile may be intact.

Root cause:
n8n started from C:\ShadowEmpire\n8n_user instead of C:\ShadowEmpire\n8n_user_restore_01.

Recovery evidence:
- 37 canonical workflows active.
- npm run n8n:status returns 200 {"status":"ok"}.
- webhook resolver passes 6/6.
- WF-000 HTTP 200.

Recovery steps:
1. Stop n8n.
2. Verify no stale listeners on ports 5678 and 5679.
3. Verify the Restore_01 WAL is the only active WAL.
4. Start n8n via C:\ShadowEmpire-Git_Restore_01\scripts\windows\start_n8n_shadow_phase1.ps1.
5. Open only http://127.0.0.1:5678/home/workflows.
6. Verify 37 canonical workflows.
7. Run WF-000.
8. Run WF-001 -> WF-010 smoke.

Do-not-do protocol:
- do not open old workflow bookmarks.
- do not create a new owner account.
- do not import workflows before DB/profile verification.
- do not start n8n from C:\ShadowEmpire\n8n_user.
- do not overwrite database.sqlite.
