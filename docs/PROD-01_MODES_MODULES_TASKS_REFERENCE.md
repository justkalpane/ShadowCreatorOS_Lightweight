# Shadow Creator OS - PROD-01 Modes, Modules, Tasks & Skills Reference

**Version**: 1.0.0  
**Date**: 2026-05-05  
**Classification**: OPERATIONAL REFERENCE  
**Purpose**: Map operating modes, modules, tasks, and skills for PROD-01

---

## SECTION 1: OPERATING MODES (User Role)

### Mode 1: Creator (Default)

**Purpose**: Daily content creation  
**Default**: YES  
**Requirements**: None (default access)

**What you can do**:
- Create new content jobs
- Inspect your own dossiers
- List outputs
- Request changes (before approval)

**What you CANNOT do**:
- Approve outputs (Founder only)
- Set system modes
- Enable operational modes

**How to set**:
```powershell
# Set creator mode (usually default)
$body = @{mode="creator"} | ConvertTo-Json
curl -X POST http://127.0.0.1:5050/operator/modes/set `
     -Headers @{"Content-Type"="application/json"} `
     -Body $body

# Or in Open WebUI chat:
# Use any shadow empire tool - creator mode is default
```

**Tools available**:
- create_youtube_script_outline ✅
- create_content_job ✅
- inspect_dossier ✅
- list_outputs ✅
- request_changes ✅
- replay_stage ⚠️ (conditional, see troubleshoot mode)
- health_check ✅
- check_alerts ✅

---

### Mode 2: Founder (Governance Authority)

**Purpose**: Content approval, governance decisions  
**Default**: NO (must be set by Founder)  
**Requirements**: Authorization / trust

**What you can do**:
- Everything Creator can do
- Approve outputs (final gate)
- Set system modes
- Enable operational modes
- Access governance registries
- Make director decisions

**What you CANNOT do**:
- Modify workflows (that's Builder)
- Change provider configurations (that's System Admin)

**How to set**:
```powershell
$body = @{mode="founder"} | ConvertTo-Json
curl -X POST http://127.0.0.1:5050/operator/modes/set `
     -Headers @{"Content-Type"="application/json"} `
     -Body $body

# Verify
curl http://127.0.0.1:5050/operator/mode/state
```

**Tools available**:
- create_youtube_script_outline ✅
- create_content_job ✅
- inspect_dossier ✅
- list_outputs ✅
- approve_output ✅ (Founder exclusive)
- request_changes ✅
- replay_stage ✅
- health_check ✅
- check_alerts ✅

---

### Mode 3: Operator (System Monitoring)

**Purpose**: System health, error recovery  
**Default**: NO  
**Requirements**: System admin role

**What you can do**:
- Check system health
- View all alerts
- Replay failed stages
- Enable operational modes
- Monitor metrics

**Tools available**:
- health_check ✅
- check_alerts ✅
- replay_stage ✅
- inspect_dossier ✅ (read-only)
- list_outputs ✅ (read-only)

---

### Mode 4: Builder (Development/Debug)

**Purpose**: Workflow development, debugging  
**Default**: NO  
**Requirements**: Developer authorization

**What you can do**:
- Access debug logging
- View workflow details
- Test replay scenarios
- Access context engineering

**Status in PROD-01**: Partially implemented

---

## SECTION 2: OPERATIONAL MODES (Can Enable Multiple Simultaneously)

### Operational Mode: Alert

**Purpose**: Monitor for errors and warnings  
**Minimum role**: operator  
**Enable/Disable**: Via API or CLI

**How to enable**:
```powershell
$body = @{actor_mode="operator"} | ConvertTo-Json
curl -X POST http://127.0.0.1:5050/operator/modes/operational/alert/enable `
     -Headers @{"Content-Type"="application/json"} `
     -Body $body

# Or in PowerShell
npm run health:check   # Will show alert status
```

**When enabled**:
- System monitors for errors in real-time
- `check_alerts()` returns active alerts
- Dossier failures logged immediately
- Operator notified of issues

---

### Operational Mode: Troubleshoot

**Purpose**: Error investigation and recovery  
**Minimum role**: builder  
**Enable**: Requires investigation intent

**How to enable**:
```powershell
$body = @{actor_mode="builder"} | ConvertTo-Json
curl -X POST http://127.0.0.1:5050/operator/modes/operational/troubleshoot/enable `
     -Headers @{"Content-Type"="application/json"} `
     -Body $body
```

**When enabled**:
- Extra logging on failures
- Root cause analysis available
- Can replay specific stages
- Error patterns detected

---

### Operational Mode: Replay

**Purpose**: Re-execute workflow stages  
**Minimum role**: operator  
**Enable**: Per incident

**How to enable**:
```powershell
curl -X POST http://127.0.0.1:5050/operator/modes/operational/replay/enable `
     -Headers @{"Content-Type"="application/json"} `
     -Body (@{actor_mode="operator"} | ConvertTo-Json)
```

**Tools**: `replay_stage(dossier_id, "WF-100")`

---

### Operational Mode: Analysis

**Purpose**: Metrics and performance analysis  
**Minimum role**: operator  
**Enable**: For reporting

---

### Operational Mode: Debug

**Purpose**: Verbose logging and diagnostics  
**Minimum role**: builder  
**Enable**: When investigating issues

**Effect**: System logs every operation with full details

---

### Operational Mode: Context Engineering

**Purpose**: Advanced prompt engineering  
**Minimum role**: founder  
**Enable**: For custom behaviors

---

### Operational Mode: Safe (Default)

**Purpose**: Conservative mode, validate everything  
**Default**: YES  
**Enable/Disable**: Usually on by default

**Behavior**:
- Provider execution blocked until enabled
- Validates all dossier operations
- Audits every action
- Preserves provider_bridge_required boundary

---

## SECTION 3: TASKS & INTENT RESOLUTION

### Task Resolution System

When you send a message to Operator API (via any surface), the **TaskRouter** analyzes it:

```powershell
# Examples of task resolution from messages:

"Create a YouTube script about AI tools"
  ↓
{intent_id: "task_create_content", task_contract: {...}}

"Check system status"
  ↓
{intent_id: "task_health_check", task_contract: {...}}

"Approve this dossier"
  ↓
{intent_id: "task_approve_output", task_contract: {...}}

"Replay WF-200 for dossier"
  ↓
{intent_id: "task_replay_stage", task_contract: {...}}
```

### Core Task Types

```
task_create_content       ← New content job
task_inspect_dossier      ← View dossier status
task_list_outputs         ← See packets
task_approve_output       ← Governance gate
task_request_changes      ← Remodify workflow
task_replay_stage         ← Re-execute WF
task_health_check         ← System status
task_check_alerts         ← Error monitoring
```

### Permission Check

After task is resolved, mode/role is checked:

```powershell
# Example: Creator trying to approve

POST /operator/modes/permission-check
{
  "mode": "creator",
  "task": "task_approve_output"
}

Response:
{
  "allowed": false,
  "reason": "task_approve_output requires founder mode"
}
```

---

## SECTION 4: MODULES (Runtime Execution)

### Runtime Modules

Not fully exposed in PROD-01, but available:

```
module_local      ← Local Ollama only
module_hybrid     ← Local + Cloud (PROD-02)
module_cloud      ← Cloud only (PROD-03)
```

### How to set (if exposed):

```powershell
$body = @{runtime_mode="local"} | ConvertTo-Json
curl -X POST http://127.0.0.1:5050/operator/runtime/set `
     -Headers @{"Content-Type"="application/json"} `
     -Body $body
```

---

## SECTION 5: SKILLS & DIRECTORS

### What are Skills?

Skills are reusable workflow sub-components:

```
skill_topic_research     ← WF-100 sub-task
skill_script_writing     ← WF-200 sub-task
skill_design_planning    ← WF-300 sub-task
skill_assembly          ← WF-400 sub-task
skill_publish_prepare   ← WF-500 sub-task
```

### Where Skills are Registered

```
registries/skill_registry.yaml
registries/skill_registry_wf100.yaml
registries/skill_registry_wf200.yaml
registries/skill_registry_wf300.yaml
registries/skill_registry_wf400.yaml
registries/skill_registry_wf500.yaml
registries/skill_loader_registry.yaml
registries/subskill_runtime_registry.yaml
```

### Adding a New Skill (PROD-02+)

**DO NOT do in PROD-01** (no workflow modifications)

Process (future):
1. Define skill in `skill_registry.yaml`
2. Create workflow in n8n
3. Register handler in `skill_loader_registry.yaml`
4. Run: `npm run validate:skills`
5. Test with: `npm run operator:test`

### What are Directors?

Directors are intelligent routing decisions:

```
director_wf100_topic    ← Route topic research
director_wf200_writer   ← Select writing style
director_wf300_designer ← Choose design approach
director_wf400_producer ← Pick assembly method
director_wf500_publish  ← Select distribution format
```

### Where Directors are Defined

```
registries/director_binding.yaml
registries/director_binding_wf100.yaml
registries/director_binding_wf200.yaml
registries/director_binding_wf300.yaml
registries/director_binding_wf400.yaml
registries/director_binding_wf500.yaml
```

### How Directors Work (Internal)

During workflow execution:
```
WF-100 starts
  ↓
Director_WF100 evaluates topic
  ↓
Selects appropriate research skill
  ↓
Executes skill
  ↓
Passes results to WF-200
```

User doesn't need to invoke directors directly in PROD-01.

---

## SECTION 6: CONTENT/WORKFLOW CONTEXT TASKS

### Content Context

When creating a job, you can specify context:

```powershell
# In Open WebUI or via API
$body = @{
    topic = "My topic"
    context = "YouTube video"  # or "Blog post", "Twitter thread", etc.
    mode = "creator"
} | ConvertTo-Json

curl -X POST http://127.0.0.1:5050/operator/new-content-job `
     -Headers @{"Content-Type"="application/json"} `
     -Body $body
```

**Available Contexts**:
- "YouTube video" (10-30 min format)
- "Blog post" (500-2000 word)
- "Twitter thread" (5-15 tweets)
- "Email newsletter" (structured)
- "Documentation" (technical)

**Effect**: Router selects appropriate workflow and director for context.

### Workflow Context Tasks

| Task | Workflow | Context | Usage |
|------|----------|---------|-------|
| Research | WF-100 | Topic intelligence | Automatic in all jobs |
| Script | WF-200 | Content writing | Automatic in all jobs |
| Design | WF-300 | Visual planning | Framework ready |
| Produce | WF-400 | Assembly | Framework ready |
| Publish | WF-500 | Distribution prep | Framework ready |
| Approve | WF-020 | Governance | Requires Founder |
| Replay | WF-021 | Remodify | Request changes |

---

## SECTION 7: PERMISSION MATRIX

### Creator Mode

```
✅ create_content_job
✅ inspect_dossier
✅ list_outputs
✅ health_check
✅ check_alerts
✅ request_changes (before approval)
❌ approve_output
❌ replay_stage (unless troubleshoot enabled)
❌ set_mode
```

### Founder Mode

```
✅ create_content_job
✅ inspect_dossier
✅ list_outputs
✅ health_check
✅ check_alerts
✅ request_changes
✅ approve_output
✅ replay_stage
✅ set_mode
✅ enable_operational_mode
```

### Operator Mode

```
✅ inspect_dossier (read-only)
✅ list_outputs (read-only)
✅ health_check
✅ check_alerts
✅ replay_stage
❌ create_content_job
❌ approve_output
❌ request_changes
```

---

## SECTION 8: DAILY OPERATING PATTERNS

### Pattern 1: Creator Flow (Most Common)

```
Creator
  ↓
Open WebUI Chat
  ↓
create_youtube_script_outline("my topic")
  ↓
Get dossier_id
  ↓
inspect_dossier(dossier_id) every 30s
  ↓
Status = READY_FOR_APPROVAL
  ↓
Chat: "Founder, please approve DOSSIER-xxxxx"
```

### Pattern 2: Founder Approval Flow

```
Founder
  ↓
Open WebUI or API
  ↓
inspect_dossier("DOSSIER-xxxxx")
  ↓
list_outputs("DOSSIER-xxxxx")
  ↓
Read packets, review quality
  ↓
Either:
  approve_output("DOSSIER-xxxxx")
  ↓ OR
  request_changes("DOSSIER-xxxxx", "Make it shorter")
```

### Pattern 3: Operator Monitoring

```
Operator
  ↓
npm run health:check (hourly)
  ↓
curl /operator/alerts (every 30 min)
  ↓
If alerts:
  ↓
  inspect_dossier(alert.dossier_id)
  ↓
  replay_stage(dossier_id, "WF-200")
```

### Pattern 4: Batch Processing (PowerShell)

```
foreach ($topic in $topics) {
  echo $topic | npm run operator:ollama
  → get dossier_id
  → log to file
  → sleep 2 sec
}
```

---

## CRITICAL RULE MATRIX

### What NEVER Changes

✅ **ALWAYS** route through Operator API  
✅ **ALWAYS** preserve audit trail  
✅ **ALWAYS** mark media as provider_bridge_required (honest)  
✅ **ALWAYS** validate permissions  
✅ **ALWAYS** backup weekly  

### What CAN Change (Future)

⏳ Add new skills (PROD-02+)  
⏳ Add new directors (PROD-02+)  
⏳ Enable real providers (PROD-03+)  
⏳ Multi-user mode (PROD-02+)  

### What NEVER Gets Modified During Production

❌ **DO NOT** edit n8n workflows  
❌ **DO NOT** modify SQLite directly  
❌ **DO NOT** change webhook registry  
❌ **DO NOT** bypass Operator API  
❌ **DO NOT** commit API keys to git  

---

## REFERENCE: All Available Tasks

```yaml
creator_mode_tasks:
  - create_youtube_script_outline
  - create_content_job
  - inspect_dossier
  - list_outputs
  - request_changes
  - health_check
  - check_alerts

founder_mode_tasks:
  - (all creator_mode_tasks)
  - approve_output
  - replay_stage
  - set_mode
  - enable_operational_mode

operator_mode_tasks:
  - inspect_dossier (read-only)
  - list_outputs (read-only)
  - health_check
  - check_alerts
  - replay_stage
  - enable_operational_mode (alert/troubleshoot)

builder_mode_tasks:
  - debug_logging
  - context_engineering (future)
  - workflow_introspection
```

---

**Status**: ✅ PROD-01 MODES, MODULES, TASKS FULLY DOCUMENTED  
**Reference**: Use in conjunction with MASTER_OPERATOR_HANDBOOK.md  
**Routing Law**: PRESERVED IN ALL MODES AND TASKS

---

**Created**: 2026-05-05  
**For**: PROD-01 Production Operations  
**Next Phase**: PROD-02 Cloud Model Onboarding
