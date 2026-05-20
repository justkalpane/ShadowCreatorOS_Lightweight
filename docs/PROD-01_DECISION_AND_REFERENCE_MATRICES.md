# Shadow Creator OS - PROD-01 Decision & Reference Matrices

**Version**: 1.0.0  
**Date**: 2026-05-05  
**Purpose**: 4 reference matrices for quick decision-making and feature classification

---

## MATRIX 1: OPERATING SURFACE DECISION MATRIX

**Use this to pick the right surface for your task**

| User Goal | Best Surface | Alternative | Time | Setup | Status |
|-----------|--------------|-------------|------|-------|--------|
| Create content (GUI) | Open WebUI | Ollama CLI | 5 sec | 5 min | ✅ PROD_READY |
| Create content (CLI) | Ollama CLI | Direct API | 3 sec | 1 min | ✅ PROD_READY |
| Monitor dossier | Open WebUI | PowerShell | 30 sec | 2 min | ✅ PROD_READY |
| Daily health check | PowerShell | Direct API | 1 min | 1 min | ✅ PROD_READY |
| Approve outputs | Open WebUI | Direct API | 1 min | 2 min | ✅ PROD_READY |
| Request changes | Open WebUI | Direct API | 1 min | 2 min | ✅ PROD_READY |
| Replay workflow | PowerShell | Direct API | 2 min | 2 min | ✅ PROD_READY |
| Batch create jobs | Ollama CLI | PowerShell script | 5 min | 5 min | ✅ PROD_READY |
| Check alerts | PowerShell | Open WebUI | 30 sec | 1 min | ✅ PROD_READY |
| System investigation | PowerShell | Direct API | 5 min | 2 min | ✅ PROD_READY |
| External agent access | MCP Server | Direct API | N/A | 5 min | ✅ PROD_READY |
| One-time test | Open WebUI | Ollama CLI | 5 sec | 5 min | ✅ PROD_READY |

---

## MATRIX 2: OPERATING MODE CAPABILITY MATRIX

**What can each user role actually do?**

| Capability | Creator | Founder | Operator | Builder |
|------------|---------|---------|----------|---------|
| Create dossiers | ✅ | ✅ | ❌ | ❌ |
| View own dossiers | ✅ | ✅ | ✅ (all) | ❌ |
| List outputs | ✅ | ✅ | ✅ (all) | ❌ |
| Check health | ✅ | ✅ | ✅ | ✅ |
| Check alerts | ✅ | ✅ | ✅ | ✅ |
| **Approve output** | ❌ | ✅ | ❌ | ❌ |
| **Request changes** | ✅ | ✅ | ❌ | ❌ |
| **Replay stage** | ❌ | ✅ | ✅ | ✅ |
| **Set mode** | ❌ | ✅ | ❌ | ❌ |
| **Enable op mode** | ❌ | ✅ | ✅ | ✅ |
| Access mission control | ❌ | ✅ | ❌ | ❌ |
| View RCA | ❌ | ✅ | ✅ | ✅ |
| Edit registry | ❌ | ✅ | ❌ | ✅ |
| Validate workflows | ❌ | ❌ | ❌ | ✅ |
| Modify n8n | ❌ | ❌ | ❌ | ❌ |

**Key**: ✅ = allowed, ❌ = blocked, (all) = can see all dossiers not just own

---

## MATRIX 3: OPERATIONAL MODE NESTING & COMBINATION MATRIX

**Can these operational modes be used together? Which combinations are valid?**

| Mode | Safe | Alert | Troubleshoot | Replay | Analysis | Debug | Learning |
|------|------|-------|--------------|--------|----------|-------|----------|
| Safe | 🟢 (default) | ❌ no | ❌ no | ❌ no | ❌ no | ❌ no | ❌ no |
| Alert | ❌ conflicts | 🟢 yes | ✅ ok | ❌ no | ✅ ok | ✅ ok | ❌ no |
| Troubleshoot | ❌ conflicts | ✅ ok | 🟢 yes | ✅ ok | ✅ ok | ✅ ok | ❌ no |
| Replay | ❌ conflicts | ❌ no | ✅ ok | 🟢 yes | ❌ no | ❌ no | ❌ no |
| Analysis | ❌ conflicts | ✅ ok | ✅ ok | ❌ no | 🟢 yes | ✅ ok | ✅ ok |
| Debug | ❌ conflicts | ✅ ok | ✅ ok | ❌ no | ✅ ok | 🟢 yes | ❌ no |
| Learning | ❌ conflicts | ❌ no | ❌ no | ❌ no | ✅ ok | ❌ no | 🟢 yes |

**Key**: 🟢 = single mode, ✅ = safe together, ❌ = conflict/incompatible, "no" = explicitly blocked

**Example Combinations**:
- ✅ Alert Mode + Troubleshoot Mode = Together (investigate alerts)
- ✅ Analysis Dashboard + Debug Mode = Together (observe + log details)
- ❌ Safe Mode + Alert Mode = Incompatible (safe mode is mutually exclusive)
- ✅ Troubleshoot Mode + Replay Mode = Together (replay with debug logging)

---

## MATRIX 4: FEATURE CLASSIFICATION (Installed/Designed/Executable/Stub/Simulated/Provider-Gated)

**Current status of all major system areas in PROD-01**

| Area | Installed | Designed | Executable | Stub | Simulated | Provider-Gated | Evidence | Target |
|------|-----------|----------|-----------|------|-----------|-----------------|----------|--------|
| **Text Generation** | ✅ | ✅ | ✅ | - | - | - | WF-100, WF-200 functional | PROD-01 |
| **Dossier System** | ✅ | ✅ | ✅ | - | - | - | dossiers/ directory, API endpoints | PROD-01 |
| **Audit Trail** | ✅ | ✅ | ✅ | - | - | - | Every dossier has audit_trail | PROD-01 |
| **Approval Gate** | ✅ | ✅ | ✅ | - | - | - | approve_output endpoint works | PROD-01 |
| **Replay/Remodify** | ✅ | ✅ | ✅ | - | - | - | WF-021 registered & tested | PROD-01 |
| **Alert System** | ✅ | ✅ | ✅ | - | - | - | check_alerts API responds | PROD-01 |
| **Metadata Gen** | ✅ | ✅ | ✅ | - | - | - | PKT-metadata packets created | PROD-01 |
| **Image Generation** | - | ✅ | - | - | - | 🌉 | PKT-image-plan packets only | PROD-02 |
| **Voice Generation** | - | ✅ | - | - | - | 🌉 | PKT-voice-plan packets only | PROD-02 |
| **Music Generation** | - | ✅ | - | - | - | 🌉 | PKT-music-plan packets only | PROD-02 |
| **Video Assembly** | - | ✅ | - | - | - | 🌉 | PKT-video-plan packets only | PROD-02 |
| **Avatar Rendering** | - | ✅ | - | - | - | 🌉 | PKT-avatar-plan packets only | PROD-03 |
| **Publishing** | - | ✅ | - | - | - | 🌉 | PKT-publish-plan packets only | PROD-03 |
| **Cloud LLM Support** | - | ✅ | - | ✅ | ✅ | - | Designed in registries; not wired | PROD-02 |
| **User Auth & RBAC** | - | ✅ | - | ✅ | - | - | Mode system exists; no login | PROD-02 |
| **Team Collaboration** | - | - | - | ✅ | - | - | Planned, not designed | PROD-03 |
| **Cost Tracking** | - | ✅ | - | ✅ | - | - | cost_report script stub | PROD-02 |
| **Multi-Platform** | - | - | - | ✅ | - | - | YouTube only; others planned | PROD-03 |
| **Advanced Agents** | - | ✅ | - | - | - | - | WF-930 structure exists | PROD-03 |
| **Custom Skills** | - | ✅ | - | - | - | - | skill_registry ready for additions | PROD-02 |

**Legend**:
- ✅ Installed = Code exists and runs
- ✅ Designed = Architecture defined in registries
- ✅ Executable = Tested and working end-to-end
- ✅ Stub = Placeholder code, not production
- ✅ Simulated = Works locally only, not with real data
- 🌉 Provider-Gated = Blocked by provider bridge

**Key Finding**: 
- **PROD-01 Ready**: Text generation, dossier mgmt, approval, alerting, replay
- **Zero Real Media in PROD-01**: All media modes produce planning packets only
- **No Credentials Exposed**: All provider operations blocked in PROD-01

---

## MATRIX 5: WORKFLOW EXECUTION TIME ESTIMATES

**How long does each workflow take?**

| Workflow | Purpose | Min | Typical | Max | Bottleneck | Notes |
|----------|---------|-----|---------|-----|-------------|-------|
| WF-001 | Dossier create | <0.5 | 0.5 | 2 | File write | Fast |
| WF-010 | Orchestration | <0.5 | 0.5 | 1 | Routing decision | Fast |
| WF-100 | Research | 30 | 45 | 60 | Ollama speed | Depends on topic complexity |
| WF-200 | Script generation | 30 | 75 | 120 | Ollama speed | Longer for complex topics |
| WF-300 | Metadata | <1 | <1 | 2 | Template fill | Very fast (template-based) |
| WF-400 | Production planning | 2 | 5 | 10 | Media spec building | Medium |
| WF-500 | Publish prep | <1 | <1 | 2 | Format conversion | Very fast |
| WF-020 | Approval | <1 | <1 | 2 | State update | Very fast |
| WF-021 | Replay-remodify | 30 | 60 | 120 | Same as WF-200 | Re-executes target stage |

**Full Cycle Time** (WF-001 → WF-200):
- **Minimum**: 2 min (very simple topic)
- **Typical**: 3-5 min
- **Maximum**: 7 min (complex topic, multiple retries)

**When Adding Providers** (PROD-02+):
- Image gen: +45-90 sec (external API latency)
- Voice gen: +30-60 sec
- Video assembly: +120-300 sec (slowest)
- Full production: +10-15 minutes

---

## MATRIX 6: ERROR RECOVERY DECISION TREE

**When something fails, what do you do?**

```
System down?
├─ YES → Check health:check
│   ├─ n8n: npm run n8n:start
│   ├─ Ollama: Start from Start menu
│   └─ API: npm run operator:start
│
└─ NO → Dossier stuck?
    ├─ YES (>2 min) → curl troubleshoot endpoint
    │   ├─ Timeout error → Ollama slow (Issue 2)
    │   ├─ WF-* error → Check n8n logs
    │   └─ Unknown → Replay stage
    │
    └─ NO → Data problem?
        ├─ YES → npm run db:verify
        │   ├─ FAIL → Rebuild index (Issue 16)
        │   └─ PASS → Dossier file corrupt? (Issue 12)
        │
        └─ NO → Performance issue?
            ├─ YES → npm run metrics:daily
            │   ├─ Low success rate → Investigate errors
            │   ├─ Slow speed → Ollama slow
            │   └─ Memory high → Reduce model size
            │
            └─ NO → Approval issue?
                ├─ Mode not founder → Set founder mode
                ├─ Tool not working → Re-import tool (Issue 7)
                └─ Dossier stuck APPROVED → WF-020 bug (Issue 8)
```

---

## MATRIX 7: MODE TRANSITION SAFETY

**Can you safely switch modes? What happens to in-flight dossiers?**

| From | To | Safe? | Effect on Dossiers | Effect on Alerts |
|------|----|----|-------------------|-----------------|
| Creator | Founder | ✅ YES | Continue normally | Can now approve |
| Founder | Creator | ⚠️ CAREFUL | Continue, lose approval rights | Still see (read-only) |
| Creator | Operator | ❌ NO | Lose create rights | Can monitor |
| Operator | Builder | ✅ YES | Can debug execution | Can investigate |
| Builder | Operator | ✅ YES | Can replay & monitor | Limited access |
| Any | Safe Mode | ✅ YES (default) | Continue with restrictions | No external calls |
| Any | Alert Mode | ✅ YES | No change | Start monitoring |
| Troubleshoot | Safe Mode | ⚠️ CAUTION | Debug logging stops | Lose diagnostic detail |

**Key Rules**:
- ✅ Mode transitions are instantaneous
- ✅ In-flight dossiers complete normally
- ✅ No data loss on mode switch
- ⚠️ Some operations become inaccessible (e.g., approve in Creator mode)
- ❌ Safe Mode cannot coexist with other operational modes

---

## MATRIX 8: PROVIDER READINESS (PROD-02+ Planning)

**When can we enable each provider?**

| Provider | Type | Minimum | Provider | Cost Est | Setup Time | Status |
|----------|------|---------|----------|----------|-----------|--------|
| OpenAI (DALL-E 3) | Image | PROD-02 | openai | $0.12-0.20/image | 5 min | PLANNED_Q2_2026 |
| Midjourney | Image | PROD-02 | midjourney | $0.04-0.10/image | 10 min | PLANNED_Q2_2026 |
| Stable Diffusion 3 | Image | PROD-03 | stabilityai | $0.01-0.03/image | 5 min | PLANNED_Q3_2026 |
| ElevenLabs | Voice | PROD-02 | elevenlabs | $0.008/1K_chars | 3 min | PLANNED_Q2_2026 |
| Google Cloud TTS | Voice | PROD-02 | google | $0.004-0.016/1K_chars | 10 min | PLANNED_Q2_2026 |
| Mubert | Music | PROD-02 | mubert | $0.01-0.05/minute | 5 min | PLANNED_Q2_2026 |
| Runway ML | Video | PROD-02 | runway | $0.50-2.00/video | 15 min | PLANNED_Q2_2026 |
| Synthesia | Avatar | PROD-03 | synthesia | $1.50-3.00/avatar | 10 min | PLANNED_Q3_2026 |
| YouTube API | Publishing | PROD-03 | google | Free | 10 min | PLANNED_Q3_2026 |

**Cost Per Full Dossier** (with all providers):
- PROD-01: $0 (all text)
- PROD-02: ~$1-2 (text + images + voice + music)
- PROD-03: ~$3-5 (with video + avatar + publishing)

---

## MATRIX 9: ALERT SEVERITY & RESPONSE SLA

**Alert priority levels and how quickly to respond**

| Severity | Examples | Impact | SLA | Action | Status |
|----------|----------|--------|-----|--------|--------|
| **CRITICAL** 🔴 | System down, data loss, auth bypass | No content creation possible | 5 min | Immediate escalation to Founder | Implemented |
| **HIGH** 🟠 | Workflow timeout, cost overrun, policy violation | Dossier stuck but system running | 15 min | Operator investigates, escalates if needed | Implemented |
| **MEDIUM** 🟡 | Single dossier error, slow response, quota warning | One user affected | 60 min | Operator logs, fixes if obvious, escalates for complex | Implemented |
| **LOW** 🟢 | Info message, deprecation warning, optimization tip | No immediate impact | 1 day | Log and batch with daily review | Implemented |

**Response Procedures**:
1. CRITICAL: Escalate immediately → curl escalate_alert
2. HIGH: Acknowledge → Try replay → If still fail, escalate
3. MEDIUM: Acknowledge → Investigate → Fix or document
4. LOW: Acknowledge → Log → Include in weekly metrics review

---

## MATRIX 10: DOSSIER STATE MACHINE

**All possible dossier states and transitions**

```
[CREATED]
  ↓ (WF-001 complete)
[ROUTED]
  ↓ (WF-010 routes to appropriate lane)
[WF-100 EXECUTING] → [WF-100 COMPLETE]
  ↓
[WF-200 EXECUTING] → [WF-200 COMPLETE]
  ↓
[WF-300 EXECUTING] → [WF-300 COMPLETE]
  ↓
[READY_FOR_APPROVAL]
  ├─ Founder approves
  │  ↓
  │  [WF-020 EXECUTING] → [APPROVED] → [LOCKED]
  │
  ├─ Founder requests changes
  │  ↓
  │  [WF-021 REPLAY] → [WF-200 EXECUTING] → [READY_FOR_APPROVAL] (loop)
  │
  ├─ System error
  │  ↓
  │  [ERROR] → [NEEDS_RECOVERY]
  │  └─ Operator: replay_stage → [WF-200 EXECUTING] (retry)
  │
  └─ Operator escalates
     ↓
     [ESCALATED] → Founder decides
```

**Key States**:
- WF-*00 EXECUTING: Workflow in progress
- READY_FOR_APPROVAL: Waiting for founder decision
- ERROR: Failed (operator can replay)
- APPROVED: Passed approval gate (locked from changes)
- LOCKED: Final state (cannot modify)

---

## SUMMARY: QUICK REFERENCE

**Pick a matrix above to answer:**
- "Which surface should I use?" → Matrix 1
- "Can I do this in my mode?" → Matrix 2
- "Can I enable alert + troubleshoot modes together?" → Matrix 3
- "Is this feature in PROD-01?" → Matrix 4
- "How long should this take?" → Matrix 5
- "What do I do if [error]?" → Matrix 6
- "Is it safe to switch modes?" → Matrix 7
- "When can we use providers?" → Matrix 8
- "What's the response time for this alert?" → Matrix 9
- "What state is my dossier in?" → Matrix 10

---

**Status**: ✅ PROD-01 DECISION MATRICES COMPLETE  
**Purpose**: Fast reference for operational decisions  
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

## Runtime Profile Decision Matrix - 2026-05-06

| Decision Area | Correct Choice | Wrong Choice | Evidence | Action |
|---|---|---|---|---|
| n8n profile | C:\ShadowEmpire\n8n_user_restore_01 | C:\ShadowEmpire\n8n_user | Restore_01 WAL updates, 37 workflows | use Restore_01 |
| n8n DB | C:\ShadowEmpire\n8n_user_restore_01\.n8n\database.sqlite | old database.sqlite | read-only count 37/37 | use Restore_01 |
| UI URL | /home/workflows | old workflow editor bookmarks | old IDs cause permission errors | open home |
| workflow IDs | registry_full_url / Restore_01 IDs | stale workflow IDs | resolver 6/6 PASS | use registry |
| recovery status | PARTIALLY RECOVERED | RECOVERED | WF-001 -> WF-010 pending | run smoke |
| repo | C:\ShadowEmpire-Git_Restore_01 | older repos unless verified | latest build target | use Restore_01 repo |

## Recovery Verdict Decision Matrix

| Evidence | PARTIAL | RECOVERED |
|---|---|---|
| Profile fixed | yes | yes |
| 37 workflows active | yes | yes |
| WF-000 HTTP 200 | yes | yes |
| WF-001 -> WF-010 smoke | pending | passed |
| restart persistence | pending | passed |
