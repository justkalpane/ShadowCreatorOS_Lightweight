# Operator Runbook: Before-Test and Execution Procedures

## Pre-Test Checklist (Before Running Any Workflow)

**5 minutes to verify system is ready:**

- [ ] Ollama is running: `ollama serve` in terminal
- [ ] Node/npm installed: `node -v && npm -v` (should be 18+ and 8+)
- [ ] Repository cloned: `cd Shadow-Creator-OS-Phase_01`
- [ ] Dependencies installed: `npm install` completed
- [ ] Environment configured: `.env` file exists with OLLAMA_BASE_URL
- [ ] n8n running: `npm run n8n:start` (check http://localhost:5678)
- [ ] Workflows imported: 31 workflows visible in n8n sidebar
- [ ] System validates: `npm run validate:all` passes
- [ ] Health check passes: WF-000 returns healthy status

**If any fails, fix before proceeding.**

---

## Test Execution Sequence

### Phase 1: Initialization (2 minutes)

**Step 1: Create Test Dossier**
```bash
# In n8n: WF-001-dossier-create
# Inputs:
dossier_id: "test_first_run"
route_id: "ROUTE_PHASE1_STANDARD"
topic: "The history of artificial intelligence"

# Expected Output:
# ✓ Dossier created
# ✓ Status: "pending"
# ✓ Dossier visible in se_dossier_index
```

### Phase 2: Full Pipeline Execution (15 minutes)

**Step 2: Run Parent Orchestrator**
```bash
# In n8n: WF-010-parent-orchestrator
# Inputs:
dossier_id: "test_first_run"
mode: "creator"
selected_model: "ollama_local_llama3.2"

# Expected Timeline:
# 0:00 - Start
# 2:00 - Topic discovery completes
# 4:00 - Research synthesis completes
# 8:00 - Script generation completes
# 10:00 - Script debate/refinement completes
# 12:00 - Context engineering completes
# 13:00 - Approval gate (YAMA, KUBERA, directors check)
# 14:00 - Analytics collection
# 15:00 - Complete

# Monitor in n8n:
# - Watch each node execute (green = success)
# - Check Executions tab for timing
# - If any node turns red → check error tab
```

### Phase 3: Output Verification (3 minutes)

**Step 3: Inspect Dossier**
```bash
npm run dossier:inspect test_first_run

# Expected Output:
# dossier_id: test_first_run
# status: completed
# dossier_version: 45+

# Namespaces should contain:
# - intake: original topic
# - discovery: entities, themes, scope
# - research: sources, claims, evidence_map
# - script: outline, draft, quality_score ~0.85-0.92
# - approval: approval_status: approved
# - analytics: metrics, quality_scores
# - evolution: feedback_signals

echo "✓ Dossier structure complete"
```

**Step 4: Check Packets**
```bash
npm run packet:list --dossier test_first_run

# Expected Output: 8 packets
# 1. topic_discovery_packet (CWF-110)
# 2. research_synthesis_packet (CWF-140)
# 3. script_generation_packet (CWF-210)
# 4. script_debate_packet (CWF-220)
# 5. script_refinement_packet (CWF-230)
# 6. final_script_packet (CWF-240)
# 7. approval_packet (WF-020)
# 8. analytics_collection_packet (CWF-610)

echo "✓ All packets emitted"
```

**Step 5: Verify Error Handling**
```bash
npm run errors:list --dossier test_first_run

# Expected Output: 0 errors (or all recovered)
# If errors exist, they should have recovery_successful: true

echo "✓ No unrecovered errors"
```

---

## Advanced Test Scenarios

### Scenario 1: Fast Route (5 minutes)
```bash
# In WF-010: Change route_id to "ROUTE_PHASE1_FAST"
# Expected runtime: 3-5 minutes (vs 15)
# Outcome: Abbreviated pipeline, quality threshold 0.75 (vs 0.85)
```

### Scenario 2: Replay from Checkpoint (20 minutes)
```bash
# Step 1: Run WF-010 with quality set to <0.85 (force rejection)
# Step 2: In WF-020, Script Director rejects
# Step 3: In WF-021, Replay from "script" checkpoint
#   checkpoint_stage: "script"
#   dossier_id: "test_first_run"
# Step 4: System restores to before script generation, re-runs
# Expected: New script packets generated (version 2)
# Outcome: Approval passes on second attempt

echo "✓ Replay/remodify cycle complete"
```

### Scenario 3: Mode Testing (Creator vs Builder)
```bash
# Test 1: Creator Mode
# - mode: "creator"
# - Must cite sources: ✓
# - Cannot suppress contradictions: ✓
# - Quality threshold: 0.85

# Test 2: Builder Mode
# - mode: "builder"
# - Can omit citations: ✓
# - Can suppress contradictions: ✓
# - Quality threshold: 0.70

# Expected: Same topic, builder mode completes faster
```

---

## Monitoring During Execution

**n8n Dashboard Tips:**
- Click workflow name → see full pipeline
- Click node → see inputs/outputs
- Click Executions tab → see all runs with timing
- Red nodes = error occurred (click for details)
- Green nodes = success
- Yellow nodes = in progress

**Real-Time Monitoring:**
```bash
# In separate terminal:
# Windows PowerShell:
#   Get-Content -Path logs/n8n.log -Wait -Tail 50
# Mac/Linux:
#   tail -f logs/n8n.log
# Or cross-platform via npm:
npm run logs:view -- --lines 50
npm run dossier:inspect test_first_run  # Check current dossier state
```

---

## Post-Test Verification

**After execution completes:**

1. **Check Status:**
   ```bash
   npm run dossier:inspect test_first_run | grep status
   # Expected: "completed" (not "pending" or "in_progress")
   ```

2. **Check Quality:**
   ```bash
   npm run dossier:inspect test_first_run | grep quality_score
   # Expected: ≥0.85 for creator mode, ≥0.70 for builder
   ```

3. **Check Cost:**
   ```bash
   npm run dossier:inspect test_first_run | grep cost_usd
   # Expected: $0.00 for Ollama (Phase-1)
   ```

4. **Check Governance:**
   ```bash
   npm run dossier:inspect test_first_run | grep approval_status
   # Expected: "approved"
   ```

5. **Check Learning:**
   ```bash
   npm run dossier:inspect test_first_run | grep evolution
   # Expected: feedback_records and learning_cycle_count > 0
   ```

**If all ✓:** System is working correctly!

---

## Cleanup After Testing

```bash
# Keep dossier for future replay:
npm run dossier:archive test_first_run

# Or clean up completely:
npm run dossier:delete test_first_run

# Optional: Clear old logs
npm run logs:clean --days 7
```

---

## Running Multiple Tests

**Parallel Testing (3 different topics simultaneously):**

The Phase-1 orchestrator runner accepts a topic seed via env var. Run multiple topics in separate terminals:

```bash
# Terminal 1: Topic 1
SHADOW_TOPIC_SEED="AI in 2026" node engine/directors/parent_orchestrator_runner.js

# Terminal 2: Topic 2
SHADOW_TOPIC_SEED="Remote work trends" node engine/directors/parent_orchestrator_runner.js

# Terminal 3: Topic 3
SHADOW_TOPIC_SEED="Blockchain adoption" node engine/directors/parent_orchestrator_runner.js

# On Windows PowerShell:
#   $env:SHADOW_TOPIC_SEED="AI in 2026"; node engine/directors/parent_orchestrator_runner.js

# Monitor all dossiers afterward:
npm run dossier:list
```

---

## Stopping n8n

```bash
# If running in foreground:
Ctrl+C

# If running in background:
npm run n8n:stop

# Kill manually (if needed):
# Windows PowerShell:
#   Get-Process node | Where-Object { $_.CommandLine -like '*n8n*' } | Stop-Process -Force
# Windows CMD:
#   wmic process where "name='node.exe'" get processid,commandline /format:csv
#   taskkill /PID <PID> /F
# Mac/Linux:
#   ps aux | grep n8n
#   kill -9 <PID>
```

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
