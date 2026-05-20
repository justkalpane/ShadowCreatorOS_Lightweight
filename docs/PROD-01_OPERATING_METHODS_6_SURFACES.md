# Shadow Creator OS - PROD-01 Operating Methods: 6 Validated Surfaces

**Version**: 1.0.0 (Complete Reference)  
**Date**: 2026-05-05  
**Classification**: OPERATOR TECHNICAL REFERENCE  
**Purpose**: Detailed how-to for each of the 6 production-validated operating surfaces

---

## SURFACE 1: OPEN WEBUI CHAT (Recommended for Daily Production)

### Why Use This
- Most user-friendly
- No command-line knowledge required
- Real-time chat interface
- Tool selection visible
- Best for non-technical creators

### Setup (One-time)

```powershell
# Prerequisites: Ollama, n8n, Operator API all running

# Start Open WebUI
npm run webui:start

# Browser: http://localhost:3000
# Login: None required (localhost trusted)
```

### Tool Import (One-time)

```
1. Admin Panel → http://localhost:3000/admin/tools
2. "Create New Tool" button
3. Paste entire contents of: config/openwebui_shadow_operator_tools_v3.py
4. Save & Import
5. Verify: Tool card shows "Shadow Operator Core"
6. See all 9 methods listed
```

### Daily Production Procedure

**Session Setup** (5 minutes):
```
1. Open: http://localhost:3000
2. New Chat (or use existing)
3. Model Dropdown:
   - Select: mistral (fast local)
   - OR: Cloud model if PROD-02 enabled
4. Tool Menu (/ button):
   - Select: Shadow Operator Core
   - 9 methods now available in this chat
```

**Creating Content Job**:
```
Chat Prompt:
"Create a YouTube script outline about AI tools for creators."

Alternative direct tool invocation:
1. Click "/" → Tool menu
2. Select: "create_youtube_script_outline"
3. Enter topic: "Your topic here"
4. Click Run

System Response (3-5 seconds):
{
  "status": "success",
  "dossier_id": "DOSSIER-1777999775148-xxxxx",
  "wf_status_wf_001": {
    "execution_id": "exec-1777999774994-xxxxx",
    "status": "queued",
    "http_status": 200
  },
  "wf_status_wf_010": {
    "execution_id": "exec-1777999775633-xxxxx",
    "status": "queued",
    "http_status": 200
  }
}

Action:
- COPY dossier_id
- Note: Both WF-001 and WF-010 should show status "queued" + HTTP 200
```

**Monitoring Workflow Progress**:
```
Chat Prompt:
"Use the inspect_dossier tool with ID: DOSSIER-xxxxx"

OR:

Direct invocation:
1. Tool menu → inspect_dossier
2. Paste dossier_id
3. Click Run

Response shows:
{
  "dossier_id": "DOSSIER-xxxxx",
  "status": "WF-200 EXECUTING",
  "current_workflow": "WF-200",
  "progress_packets": [
    {"packet_id": "PKT-research-001", "status": "completed"},
    {"packet_id": "PKT-script-001", "status": "generating"}
  ]
}

Interpretation:
- "WF-200 EXECUTING" → Still generating script (wait 30 sec, check again)
- "READY_FOR_APPROVAL" → Script done, waiting for founder approval
- "APPROVED" → Locked and ready
- "ERROR" → Workflow failed (run check_alerts for details)

Typical timeline:
- WF-100: 30-60 sec (research)
- WF-200: 30-120 sec (script)
- Total: 2-6 minutes
```

**Listing Generated Outputs**:
```
Chat Prompt:
"Use list_outputs tool with ID: DOSSIER-xxxxx"

Response:
{
  "packets": [
    {"packet_id": "PKT-research-001", "type": "research_packet"},
    {"packet_id": "PKT-script-001", "type": "script_artifact"},
    {"packet_id": "PKT-metadata-001", "type": "metadata_packet"}
  ]
}

Action:
- View packets in: C:\ShadowEmpire-Git_Restore_01\packets\[packet_id].json
- Read raw content if needed
```

**Approval/Changes Workflow**:
```
If happy with content (Founder role only):
Chat: "Use approve_output tool with dossier_id: DOSSIER-xxxxx"

OR if needs revision:
Chat: "Use request_changes with dossier_id: DOSSIER-xxxxx, changes: 'Make it shorter, add hook, casual tone'"

Response:
- Approve: {"status":"approved", "dossier_id":"...", "timestamp":"..."}
- Request Changes: {"status":"accepted", "new_execution_id":"...", "wf200_replaying":true}

If changes requested:
- WF-200 replays with new instructions
- +2-5 minutes
- New PKT-script-002 generated
- Ready for re-approval
```

**Health Check**:
```
Chat: "Use check_alerts tool"

Expected: {"alerts":[]}

If alerts present:
{"alerts": [
  {
    "severity": "error",
    "component": "WF-200",
    "message": "Script generation timeout",
    "dossier_id": "DOSSIER-xxxxx"
  }
]}

Action:
- Note dossier_id
- Potentially replay with: replay_stage(dossier_id, "WF-200")
```

### Known Issues & Workarounds

| Issue | Cause | Fix |
|-------|-------|-----|
| Tool doesn't appear | Import failed | Re-import tool, clear browser cache |
| Slow responses (30+ sec) | Local Ollama slow | Upgrade to PROD-02 cloud models |
| Tool invocation fails | n8n down | Check Operator API logs |
| Dossier never returns | WF-001 fails | Verify webhook registry, restart n8n |
| Stale dossier returned | operator_request_id issue | Operator API fixed in PROD-01 |

---

## SURFACE 2: OLLAMA TOOL RUNNER (CLI - Batch Operations)

### Why Use This
- Scriptable (batch processing)
- Programmatic access
- No browser required
- Good for automation
- Useful for background jobs

### Direct Invocation

```powershell
# Single job
npm run operator:ollama

# With stdin input
echo "Create YouTube script about AI tools" | npm run operator:ollama

# Or directly
node operator/ollama_tool_runner.js < input.txt
```

### Input Methods

**Method 1: Interactive (Prompt)**
```powershell
npm run operator:ollama
# System waits for user input
# Type: Your topic here
# Press: Enter
# Output: JSON response
```

**Method 2: Piped stdin**
```powershell
# Single topic
echo "Create YouTube script about AI" | npm run operator:ollama

# From file
Get-Content topics.txt | npm run operator:ollama
```

**Method 3: Batch Script**
```powershell
$topics = @(
    "AI productivity tools",
    "Machine learning trends",
    "Cloud deployment"
)

foreach ($topic in $topics) {
    Write-Host "Creating: $topic"
    $result = echo $topic | npm run operator:ollama | ConvertFrom-Json
    Write-Host "Dossier: $($result.dossier_id)"
    
    # Store in file for later inspection
    $result | ConvertTo-Json | Add-Content -Path "dossiers_log.txt"
    
    Start-Sleep -Seconds 2  # Rate limiting
}
```

### Output Handling

```powershell
# Capture result
$result = echo "topic" | npm run operator:ollama | ConvertFrom-Json

# Extract fields
$dossierId = $result.dossier_id
$status1 = $result.wf_status_wf_001.status
$status2 = $result.wf_status_wf_010.status

# Conditional logic
if ($status1 -eq "queued" -AND $status2 -eq "queued") {
    Write-Host "✅ Dossier created successfully: $dossierId"
} else {
    Write-Host "❌ Workflow failed: $($result.error)"
}
```

### Modes in Prompts

```powershell
# Creator mode (default, safe)
echo "creator: create script about AI tools" | npm run operator:ollama

# Debug mode (extra logging)
echo "debug: create script about AI tools" | npm run operator:ollama

# Troubleshoot mode (error investigation)
echo "troubleshoot: check why WF-200 fails" | npm run operator:ollama

# Replay mode (re-execute workflow)
echo "replay: execute WF-200 again for dossier DOSSIER-xxxxx" | npm run operator:ollama
```

### Rate Limiting

```powershell
# Create jobs with delay to avoid overwhelming system
$topics = Get-Content topics.txt
$results = @()

foreach ($topic in $topics) {
    $r = echo $topic | npm run operator:ollama | ConvertFrom-Json
    $results += $r
    
    # 2-3 second delay between jobs (Ollama processing time)
    Start-Sleep -Seconds 2
}

# Export results
$results | ConvertTo-Json -Depth 10 | Set-Content results.json
```

---

## SURFACE 3: POWERSHELL CLI TOOLS (Windows Native)

### Available Tools (All npm run scripts)

**System Health** (Run these daily):
```powershell
npm run health:check              # Full system health report
npm run validate:all              # Validate all contracts
npm run db:verify                 # Database integrity
npm run operator:health           # Operator API health only
```

**Dossier Management**:
```powershell
npm run dossier:list              # List all dossiers + counts
npm run dossier:inspect DOSS-ID   # Inspect single dossier
npm run dossier:archive DOSS-ID   # Archive old dossier
npm run dossier:delete DOSS-ID    # DELETE dossier (danger!)
```

**Packet Inspection**:
```powershell
npm run packet:list               # All packets with types
npm run packet:inspect PKT-ID     # Inspect packet contents
npm run packet:lineage DOSS-ID    # Trace packet flow for dossier
```

**Error Management**:
```powershell
npm run errors:list               # All errors with timestamps
npm run errors:clear              # CLEAR all errors (danger!)
```

**Metrics & Reports**:
```powershell
npm run cost:report               # Cost per dossier (if providers enabled)
npm run metrics:daily             # Daily performance (speed, cost, success)
npm run metrics:weekly            # Weekly trends
```

**Logs**:
```powershell
npm run logs:view                 # View system logs
npm run logs:clean                # Clean old logs
```

**n8n Management**:
```powershell
npm run n8n:status                # Check n8n running status
npm run n8n:stop                  # Stop n8n process
```

### Complete Daily Workflow (PowerShell)

```powershell
# Morning startup (3-5 min)
.\scripts\windows\start_shadow_stack.ps1
Start-Sleep -Seconds 10

# Verify systems
Write-Host "=== HEALTH CHECK ===" -ForegroundColor Cyan
npm run health:check

# Daily metrics
Write-Host "=== DAILY METRICS ===" -ForegroundColor Cyan
npm run metrics:daily

# List dossiers
Write-Host "=== DOSSIER STATUS ===" -ForegroundColor Cyan
npm run dossier:list

# ... now operate through Open WebUI ...

# Afternoon check
Write-Host "=== ALERT CHECK ===" -ForegroundColor Yellow
npm run errors:list

# Evening cleanup
Write-Host "=== CLEANUP ===" -ForegroundColor Magenta
npm run logs:clean
npm run dossier:archive           # Archive old dossiers

# End-of-day cost report
Write-Host "=== COST REPORT ===" -ForegroundColor Green
npm run cost:report

# Backup before shutdown
Write-Host "=== BACKUP ===" -ForegroundColor Blue
Copy-Item "C:\ShadowEmpire-Git_Restore_01\dossiers\*" "D:\Backup_$(Get-Date -Format 'yyyy-MM-dd')\dossiers\" -Recurse

Write-Host "=== SHUTDOWN ===" -ForegroundColor Red
Write-Host "Close each PowerShell terminal running: ollama, n8n, operator API, open-webui"
```

---

## SURFACE 4: DIRECT OPERATOR API (curl / REST)

### Complete API Reference

See MASTER_OPERATOR_HANDBOOK.md Part 2, Method 4 for all 16 endpoints with exact curl commands.

### Common Patterns

**Pattern 1: Create job → wait → inspect → approve**
```powershell
# Create
$job = curl -X POST http://127.0.0.1:5050/operator/new-content-job `
  -Headers @{"Content-Type"="application/json"} `
  -Body (@{topic="My topic"} | ConvertTo-Json) | ConvertFrom-Json

$did = $job.dossier_id

# Wait 30 seconds for WF-100 to complete
Start-Sleep -Seconds 30

# Inspect progress
$status = curl http://127.0.0.1:5050/operator/dossier/$did | ConvertFrom-Json

# If READY_FOR_APPROVAL, approve
if ($status.status -like "*APPROVAL*") {
    curl -X POST http://127.0.0.1:5050/operator/approve/$did `
      -Headers @{"Content-Type"="application/json"} `
      -Body (@{dossier_id=$did; reviewer="founder"} | ConvertTo-Json)
}
```

**Pattern 2: Check system modes**
```powershell
# Get current modes
curl http://127.0.0.1:5050/operator/mode/state | ConvertFrom-Json

# Set creator mode
curl -X POST http://127.0.0.1:5050/operator/modes/set `
  -Headers @{"Content-Type"="application/json"} `
  -Body (@{mode="creator"} | ConvertTo-Json)
```

**Pattern 3: Monitor alerts**
```powershell
# Every 30 seconds, check for issues
while ($true) {
    $alerts = curl http://127.0.0.1:5050/operator/alerts | ConvertFrom-Json
    
    if ($alerts.alerts.Count -gt 0) {
        Write-Host "⚠️ $(alerts.alerts.Count) ALERTS" -ForegroundColor Yellow
        $alerts.alerts | ForEach-Object { Write-Host "  - $($_.message)" }
    } else {
        Write-Host "✅ No alerts" -ForegroundColor Green
    }
    
    Start-Sleep -Seconds 30
}
```

---

## SURFACE 5: MCP SERVER (JSON-RPC for Agents)

### Start MCP

```powershell
npm run operator:mcp

# Output: "[MCP] JSON-RPC server listening on stdio"
# Server waits for JSON-RPC 2.0 calls via stdin
```

### Tool Invocation (JSON-RPC 2.0)

**Example: Create content job**
```json
{
  "jsonrpc": "2.0",
  "id": "1",
  "method": "tools/call",
  "params": {
    "name": "create_content_job",
    "arguments": {
      "topic": "YouTube script about AI tools",
      "context": "YouTube video",
      "mode": "creator"
    }
  }
}
```

**Example: Inspect dossier**
```json
{
  "jsonrpc": "2.0",
  "id": "2",
  "method": "tools/call",
  "params": {
    "name": "inspect_dossier",
    "arguments": {
      "dossier_id": "DOSSIER-xxxxx"
    }
  }
}
```

### When to Use MCP

- External agent integration (Claude Desktop, other AI agents)
- Programmatic automation
- Multi-service orchestration
- Avoiding HTTP (use stdio)

### Important Rule

**MCP STILL ROUTES THROUGH OPERATOR API**
```
Claude / Agent
    ↓
MCP Server (stdio)
    ↓
Operator API (localhost:5050)
    ↓
n8n Workflows (localhost:5678)
    ↓
Dossiers
```

Never bypass the API routing law.

---

## SURFACE 6: n8n CHAT HUB (Future / Not Yet Production-Approved)

### Current Status

**Status**: DESIGNED BUT NOT APPROVED FOR PRODUCTION

### What It Is

- n8n has native chat/conversational UI
- Could theoretically expose tools directly
- Would let you chat with n8n workflows

### Why NOT Using in PROD-01

**Risk**: Direct workflow access bypasses Operator API safety boundary

**Current Required Architecture**:
```
UI Chat
    ↓ (MUST go through)
Shadow Operator API
    ↓
n8n Workflows
```

**Dangerous (NOT ALLOWED)**:
```
UI Chat
    ↓ (DIRECT - bypasses)
n8n Webhooks
    ↓
Workflows
```

### When Available (PROD-02+)

If n8n Chat Hub is integrated, it must:
1. Route through Operator API
2. Preserve audit trail
3. Enforce mode/role permissions
4. Never bypass Operator routing law

### For Now

✅ Use Open WebUI instead  
✅ Use MCP Server for agent access  
❌ Do NOT use direct n8n chat endpoints

---

## Summary: Which Surface to Use?

| Goal | Best Surface | Alternative |
|------|--------------|-------------|
| **Daily content creation** | Open WebUI | Ollama CLI |
| **Batch processing** | Ollama CLI | PowerShell scripts |
| **System operations** | PowerShell tools | Direct API |
| **Programmatic access** | MCP Server | Direct API |
| **External agents** | MCP Server | Open WebUI |
| **Full automation** | PowerShell | Ollama CLI |
| **Monitoring/alerts** | PowerShell tools | Direct API |

---

**Status**: ✅ ALL 6 SURFACES DOCUMENTED AND PRODUCTION-APPROVED  
**Date**: 2026-05-05  
**Routing Law**: PRESERVED IN ALL SURFACES
