# LOCAL OLLAMA MODEL BRAIN SMOKE TEST (2026-05-07)

## Classification
This test is **MODEL_ONLY_SMOKE_TEST**.

## What It Proves
- Local Ollama runtime endpoint health (`/api/tags`, `/api/generate`)
- Local model generation quality and structured output capability

## What It Does NOT Prove
- Operator API workflow orchestration
- WF-001 dossier creation
- WF-010 parent orchestration
- packet index and route run evidence
- WF-020/WF-021 approval/replay state

## Rule
Direct Ollama generation becomes workflow proof only when the user surface calls Operator API and a real n8n workflow execution trace is recorded.

---
# DIRECT OLLAMA OPERATOR METHOD - PRODUCTION TEST (2026-05-07)

## 1) Purpose
Validate that the local LLM layer (Ollama) is healthy and can generate production-grade long-form content output for the test topic **AI vs Human** using a local-first path.

## 2) What Direct Ollama Proves
- Ollama runtime endpoint is reachable (`http://localhost:11434`).
- A local model can execute a production prompt and return structured output.
- Operator can persist local output files deterministically for review.

## 3) What Direct Ollama Does NOT Prove
- It does **not** trigger n8n workflows (WF-001/WF-010/packs).
- It does **not** auto-create dossier records.
- It does **not** auto-update packet indexes.
- It does **not** auto-update approval queue.
- It does **not** prove operator orchestration/routing behavior.

## 4) Prerequisites
- Repo path: `C:\ShadowEmpire-Git_Restore_01`
- n8n profile (protected): `C:\ShadowEmpire\n8n_user_restore_01`
- Ollama endpoint: `http://localhost:11434`
- Operator API endpoint: `http://localhost:5002`
- n8n UI: `http://127.0.0.1:5678/home/workflows`
- Open WebUI: `http://localhost:3000`

## 5) Exact Health-Check Commands (PowerShell)
```powershell
Set-Location C:\ShadowEmpire-Git_Restore_01

# Core operator + n8n + profile safety check
powershell -ExecutionPolicy Bypass -File .\scripts\operator\check-shadow-health.ps1

# n8n API status
npm run n8n:status

# Operator API health
Invoke-WebRequest -Uri "http://localhost:5002/operator/health" -UseBasicParsing | Select-Object StatusCode

# Ollama API primary health check (authoritative)
Invoke-WebRequest -Uri "http://localhost:11434/api/tags" -UseBasicParsing | Select-Object StatusCode

# Optional CLI checks (only if ollama is in PATH)
ollama --version
ollama list
```

## 6) Diagnosis Rule (CLI vs Runtime)
- `ollama` CLI fails + `/api/tags` passes = **CLI PATH issue**, not Ollama runtime failure.
- `/api/tags` fails = Ollama runtime/service issue.

## 7) API-Only Model Inventory (Primary)
```powershell
Set-Location C:\ShadowEmpire-Git_Restore_01
$tags = Invoke-RestMethod "http://localhost:11434/api/tags"
$tags.models | Select-Object name, modified_at, size | Format-Table
```

## 8) API-Only AI vs Human Production Test (`/api/generate`)
```powershell
Set-Location C:\ShadowEmpire-Git_Restore_01

$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$outDir = "C:\ShadowEmpire-Git_Restore_01\data\ollama_direct_runs"
New-Item -ItemType Directory -Force -Path $outDir | Out-Null

$prompt = @"
You are operating as Shadow Creator OS local model brain.

Production test topic:
AI vs Human

Create a 5-minute YouTube script package.

Return the output with these sections:
1. Topic interpretation
2. Hook
3. Intro
4. Full 5-minute script
5. Debate / critique notes
6. Refined final script
7. Thumbnail idea
8. 5 title options
9. Description
10. Hashtags
11. Context packet JSON
12. Approval recommendation

Important:
Return clean structured output.
Do not claim n8n workflow execution.
Do not claim dossier creation.
Do not claim approval queue update.
"@

$payload = @{
  model = "llama3.2:3b"
  prompt = $prompt
  stream = $false
} | ConvertTo-Json -Depth 10

$response = Invoke-RestMethod `
  -Method Post `
  -Uri "http://localhost:11434/api/generate" `
  -ContentType "application/json" `
  -Body $payload

$response.response | Tee-Object -FilePath "$outDir\AI_vs_Human_direct_ollama_$timestamp.md"
$response | ConvertTo-Json -Depth 10 | Out-File "$outDir\AI_vs_Human_direct_ollama_$timestamp.raw.json" -Encoding UTF8
```

## 9) Save-Output Location
- `C:\ShadowEmpire-Git_Restore_01\data\ollama_direct_runs\AI_vs_Human_direct_ollama_<timestamp>.md`
- `C:\ShadowEmpire-Git_Restore_01\data\ollama_direct_runs\AI_vs_Human_direct_ollama_<timestamp>.raw.json`

## 10) Dossier Clarification
Direct Ollama output is a manual draft artifact only.
- No automatic dossier creation occurs.
- No WF-001/WF-010 orchestration occurs.

## 11) Approval Queue Clarification
Direct Ollama output does **not** update `se_approval_queue` automatically.

## 12) Manual Approval Method (Direct Ollama)
```powershell
Set-Location C:\ShadowEmpire-Git_Restore_01
$ts = Get-Date -Format "yyyyMMdd_HHmmss"
$approvalDir = ".\data\approvals\manual"
New-Item -ItemType Directory -Force -Path $approvalDir | Out-Null

$approval = @{
  approval_type = "manual_direct_ollama"
  topic = "AI vs Human"
  reviewer = "founder"
  decision = "approved"   # or "needs_changes"
  reason = "Direct Ollama draft reviewed"
  approved_at = (Get-Date).ToString("o")
}

$approvalPath = Join-Path $approvalDir "DIRECT_OLLAMA_APPROVAL_$ts.json"
$approval | ConvertTo-Json -Depth 10 | Set-Content -Path $approvalPath
Write-Host "Saved: $approvalPath"
```

## 13) Move from Direct Ollama to n8n/Operator Flow
1. Start operator API.
2. Run `new-content-job.ps1` to create official dossier and governed flow.
3. Inspect outputs via operator scripts.
4. Use governed approval/replay scripts for production records.

## 14) Troubleshooting
- **CLI missing (`ollama` not recognized)**
  - Use API-only flow (`/api/tags`, `/api/generate`) as primary method.
  - Optional PATH checks:
  ```powershell
  where.exe ollama
  Test-Path "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe"
  & "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe" --version
  & "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe" list
  ```
- **Model missing**
  - API pull:
  ```powershell
  $pullPayload = @{ name = "llama3.2:3b"; stream = $false } | ConvertTo-Json
  Invoke-RestMethod -Method Post -Uri "http://localhost:11434/api/pull" -ContentType "application/json" -Body $pullPayload
  ```
- **`/api/tags` fails**
  - Ollama runtime/service is down; start/restart runtime and retest.

## 15) Pass/Fail Checklist
**PASS**
- `/api/tags` returns success.
- target model is listed (or successfully pulled).
- `/api/generate` returns content.
- timestamped `.md` and `.raw.json` output files are created.

**FAIL**
- `/api/tags` fails.
- `/api/generate` fails.
- output files are not created.

## 16) Next Operator Method to Test
Next: **PowerShell Operator Method**.
Reason: proves dossier creation, workflow orchestration, packet/index updates, and approval/replay path.

