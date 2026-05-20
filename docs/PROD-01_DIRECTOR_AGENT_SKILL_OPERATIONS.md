# Shadow Creator OS - PROD-01 Director, Agent, Skill Operations Guide

**Version**: 1.0.0  
**Date**: 2026-05-05  
**Classification**: OPERATIONAL REFERENCE FOR ADVANCED CUSTOMIZATION  
**Purpose**: How to safely understand, inspect, and (in PROD-02+) modify directors, agents, skills, and sub-skills

---

## CRITICAL PREAMBLE: PROD-01 is READ-ONLY for These Systems

**Current Policy**:

✅ **You CAN**:
- Read all director/skill/agent registries
- Inspect active directors and skills
- Understand how they work
- Plan modifications for PROD-02

❌ **You CANNOT** (in PROD-01):
- Add new skills
- Modify existing director bindings
- Add new agents or sub-agents
- Create custom providers
- Edit workflow bindings

**Why**: PROD-01 is a production system with live dossier data. Component modifications require:
1. Code review (someone besides the developer)
2. Validator sign-off (automated tests)
3. Deployment gate verification
4. Production acceptance testing

**When You CAN Modify**: PROD-02 (4-6 weeks after PROD-01 launch) with proper procedures.

---

## PART 1: UNDERSTANDING DIRECTORS

### What is a Director?

**Definition**: A routing/decision component that chooses which skill to invoke based on dossier context.

**Analogy**: Think of a film director - evaluates the scene (dossier) and chooses the right actor (skill) for the role.

**Architecture**:
```
Workflow (WF-100, WF-200, etc.)
    ↓
Director_WF100 evaluates topic
    ├─ Topic: "AI tools" → research_skill_ai_analysis
    ├─ Topic: "cooking" → research_skill_recipe_analysis
    └─ Topic: "fitness" → research_skill_health_analysis
    ↓
Skill selected
    ↓
Workflow continues
```

### Directors in PROD-01

**Registered Directors** (read-only):

```yaml
director_wf100_topic:      # Route WF-100 based on topic category
  skill_selected: research_skill_general
  status: ACTIVE_PHASE_1
  
director_wf200_writer:     # Route WF-200 based on script style
  skill_selected: script_writing_skill_standard
  status: ACTIVE_PHASE_1
  
director_wf300_designer:   # Route WF-300 based on design approach
  skill_selected: design_planning_skill_visual
  status: STRUCTURE_READY
  
director_wf400_producer:   # Route WF-400 based on media type
  skill_selected: production_planning_skill_standard
  status: STRUCTURE_READY
  
director_wf500_publish:    # Route WF-500 based on platform
  skill_selected: publish_prep_skill_youtube
  status: STRUCTURE_READY
```

### How Directors Work (Internal)

**File Location**: `registries/director_binding_wf100.yaml` (and `_wf200.yaml`, etc.)

**Structure**:
```yaml
director_id: director_wf100_topic
class: director_component
purpose: "Evaluate topic category and select research skill"
enabled: true
decision_criteria:
  - field: "dossier.namespaces.intake.topic"
    type: "text_classification"
    model: "keyword_matcher"  # or "regex" or "llm"
    
routing_rules:
  - condition: "topic contains 'AI' OR 'machine learning'"
    skill_to_invoke: "research_skill_ai_analysis"
    confidence: 0.95
    
  - condition: "topic contains 'cooking' OR 'recipe'"
    skill_to_invoke: "research_skill_recipe_analysis"
    confidence: 0.95
    
  - condition: "DEFAULT"
    skill_to_invoke: "research_skill_general"
    confidence: 1.0

nesting_allowed: true
can_override: true
validation_required: true
```

### Reading Director Config (PROD-01)

```powershell
# List all directors
Get-Content registries/director_binding.yaml | ConvertFrom-Yaml

# Inspect specific director
Get-Content registries/director_binding_wf100.yaml | ConvertFrom-Yaml

# Or via API (coming in PROD-02):
# curl http://127.0.0.1:5050/operator/directors
```

### Observing Directors in Action (PROD-01)

```powershell
# Enable debug mode
curl -X POST http://127.0.0.1:5050/operator/modes/operational/debug/enable `
  -Body (@{actor_mode="builder"} | ConvertTo-Json)

# Create dossier
curl -X POST http://127.0.0.1:5050/operator/new-content-job `
  -Body (@{topic="AI tools for content creators"; mode="creator"} | ConvertTo-Json)

# Get dossier_id, then trace
curl http://127.0.0.1:5050/operator/troubleshoot/dossier/DOSSIER-xxxxx

# Look for in logs:
# [Director] director_wf100_topic evaluating topic="AI tools..."
# [Director] selected skill=research_skill_ai_analysis (confidence=0.95)
```

---

## PART 2: UNDERSTANDING SKILLS

### What is a Skill?

**Definition**: A reusable sub-component that performs a specific function within a workflow.

**Examples**:
- `research_skill_ai_analysis` - Research AI topics
- `script_writing_skill_standard` - Write scripts in standard format
- `design_planning_skill_visual` - Plan visual assets
- `production_planning_skill_standard` - Plan production timeline

**File Locations**:
```
registries/
  ├─ skill_registry.yaml                 (master list)
  ├─ skill_registry_wf100.yaml           (WF-100 skills)
  ├─ skill_registry_wf200.yaml           (WF-200 skills)
  ├─ skill_registry_wf300.yaml           (WF-300 skills)
  ├─ skill_registry_wf400.yaml           (WF-400 skills)
  ├─ skill_registry_wf500.yaml           (WF-500 skills)
  ├─ skill_registry_wf600.yaml           (WF-600 skills)
  ├─ skill_loader_registry.yaml          (where to load from)
  └─ subskill_runtime_registry.yaml      (sub-skill definitions)
```

### Skills in PROD-01

**Active Skills** (actually used):

```yaml
research_skill_general:
  workflow: WF-100
  purpose: "General topic research"
  inputs: {topic: string}
  outputs: {research_packet: json}
  status: ACTIVE_PHASE_1
  model: ollama/mistral
  validation: PASS
  
script_writing_skill_standard:
  workflow: WF-200
  purpose: "Standard script writing"
  inputs: {research_packet: json, context: string}
  outputs: {script_packet: json}
  status: ACTIVE_PHASE_1
  model: ollama/mistral
  validation: PASS
```

**Registered But Not Yet Tested**:

```yaml
research_skill_ai_analysis:
  workflow: WF-100
  purpose: "Specialized AI topic research"
  inputs: {topic: string, depth: 'deep' | 'shallow'}
  outputs: {research_packet: json}
  status: STRUCTURE_READY
  notes: "Registered but not yet tested at scale"

design_planning_skill_visual:
  workflow: WF-300
  purpose: "Visual design planning"
  inputs: {script_packet: json}
  outputs: {design_plan_packet: json}
  status: STRUCTURE_READY
  notes: "Framework in place, needs validation"
```

### Reading Skill Registries (PROD-01)

```powershell
# Master skill list
Get-Content registries/skill_registry.yaml | Select-String "skill_id" | head -20

# WF-100 specific skills
Get-Content registries/skill_registry_wf100.yaml

# Or via validator
npm run validate:schemas

# Output shows which skills are registered and their status
```

### Inspecting Skill Usage in Dossiers

```powershell
# When troubleshooting, see which skill was invoked
curl http://127.0.0.1:5050/operator/troubleshoot/dossier/DOSSIER-xxxxx

# Look for:
# {
#   "workflow": "WF-100",
#   "skill_invoked": "research_skill_general",
#   "status": "completed",
#   "output_packet": "PKT-research-001"
# }
```

---

## PART 3: UNDERSTANDING AGENTS & SUB-AGENTS

### What is an Agent?

**Definition**: An autonomous system component that can operate semi-independently within the workflow.

**In PROD-01**: Not yet implemented. Design exists but no runtime wiring.

**Future (PROD-02+)**:
- Evaluation Agent: Assess quality of generated content
- Learning Agent: Improve system performance based on feedback
- Cost Agent: Optimize spend across providers
- Recovery Agent: Auto-fix common errors

### Sub-Skills vs Sub-Agents

**Sub-Skill**: A skill that's invoked by another skill
```
WF-100 skill: research_skill_ai_analysis
  ├─ Invokes sub-skill: web_search_subskill
  ├─ Invokes sub-skill: fact_checking_subskill
  └─ Combines results
```

**Sub-Agent**: An independent agent that operates during workflow
```
WF-200 script generation
  ├─ Main skill: script_writing_skill_standard
  └─ Spawns: Evaluation Agent (checks script quality)
       ├─ Checks readability
       ├─ Checks hook strength
       └─ Requests changes if score < 0.80
```

### Sub-Skill Registry (PROD-01)

**File**: `registries/subskill_runtime_registry.yaml`

**Structure** (read-only):
```yaml
subskill_id: web_search_subskill
parent_skill: research_skill_ai_analysis
purpose: "Search web for topic information"
inputs: {query: string}
outputs: {search_results: json}
status: READY_PHASE_2
handler: "external_api"  # calls external web search
cost_per_call_usd: 0.01
timeout_sec: 10
```

---

## PART 4: UNDERSTANDING PROVIDERS

### What is a Provider?

**Definition**: An external service that generates real media (images, video, voice, etc.)

**Types**:
1. **LLM Providers**: OpenAI, Anthropic, Google, Mistral, etc.
2. **Image Providers**: DALL-E, Midjourney, Stable Diffusion, Leonardo
3. **Voice Providers**: ElevenLabs, Google Cloud TTS, AWS Polly
4. **Video Providers**: Runway, HeyGen, Synthesia
5. **Platform Providers**: YouTube API, LinkedIn API, TikTok API

### Provider Registry (PROD-01)

**File**: `registries/provider_registry.yaml`

**Structure** (read-only in PROD-01):
```yaml
provider_id: provider_openai
class: provider
status: provider_bridge_required
enabled: false  # ← BLOCKED in PROD-01
tier: premium
cost_model: "per_api_call"
estimated_cost_per_dossier_usd: 0.30

credentials_required:
  - api_key
  - org_id (optional)

quota_tracking:
  monthly_budget_usd: null  # Set by Founder when enabled
  current_month_used_usd: 0.00

fallback_provider: null  # No fallback for images
```

### Provider Access in PROD-01

```powershell
# Check provider status
curl http://127.0.0.1:5050/operator/providers

# Response:
# {
#   "providers": [
#     {
#       "provider_id": "provider_openai",
#       "status": "provider_bridge_required",
#       "enabled": false,
#       "reason": "Safe Mode active; enable in PROD-02"
#     },
#     {
#       "provider_id": "provider_elevenlabs",
#       "status": "provider_bridge_required",
#       "enabled": false,
#       "reason": "Safe Mode active; enable in PROD-02"
#     }
#   ]
# }
```

---

## PART 5: ADDING COMPONENTS (PROD-02+ ONLY)

**⚠️ DO NOT ATTEMPT IN PROD-01**

### Process for Adding a New Skill (PROD-02)

**Prerequisites**:
1. Builder role (not Creator or Operator)
2. Code review approval (from another builder)
3. Validator sign-off
4. Controlled deployment gate

**Steps**:

**Step 1: Design the Skill**
```yaml
# Create registries/skill_registry_new_skill_name.yaml

skill_id: my_new_skill
workflow: WF-100  # Which workflow this skill is for
purpose: "Short description of what this skill does"
inputs:
  - field: topic
    type: string
    required: true
  - field: depth
    type: 'shallow' | 'deep'
    required: false
outputs:
  - packet_type: research_packet
    description: "Output packet structure"
status: STRUCTURE_READY
model: ollama/mistral  # (PROD-02: can be cloud model)
estimated_execution_time_sec: 45
max_retries: 3
timeout_sec: 60
```

**Step 2: Validate**
```powershell
npm run validate:schemas
npm run validate:registries

# Output:
# ✅ skill_registry_my_new_skill.yaml: VALID
# ✅ No conflicts with existing skills
# ✅ All required fields present
```

**Step 3: Add to Director** (optional)
```yaml
# Update registries/director_binding_wf100.yaml

routing_rules:
  - condition: "topic contains 'my_domain'"
    skill_to_invoke: "my_new_skill"
    confidence: 0.90
```

**Step 4: Test in Isolated Dossier**
```powershell
# Run test suite with new skill
npm run test:e2e --filter="my_new_skill"

# Manual test
npm run operator:test

# Create dossier, monitor for success
curl -X POST http://127.0.0.1:5050/operator/new-content-job `
  -Body (@{topic="test topic"; mode="creator"} | ConvertTo-Json)

# Trace execution
curl http://127.0.0.1:5050/operator/troubleshoot/dossier/DOSSIER-xxxxx
```

**Step 5: Code Review & Approval**
```
- Another builder reviews skill definition
- Validator confirms no conflicts
- Deployment gate checks production impact
- Founder approves skill addition
```

**Step 6: Deploy to Production**
```powershell
npm run deploy:skills
# Or as part of PROD-02 general deployment
```

---

### Process for Adding a New Director (PROD-02)

Similar to skills, but also requires:
1. Understand all existing directors
2. Ensure no circular routing
3. Validation that all possible conditions are handled
4. Fallback routing to default skill

**Template**:
```yaml
director_id: director_wf200_my_decision
class: director_component
workflow: WF-200
purpose: "Route script writing based on [criteria]"
enabled: true
decision_criteria:
  field: "dossier.namespaces.intake.script_style"
  type: "categorical"

routing_rules:
  - condition: "script_style = 'formal'"
    skill: "script_writing_skill_academic"
  - condition: "script_style = 'casual'"
    skill: "script_writing_skill_conversational"
  - condition: "DEFAULT"
    skill: "script_writing_skill_standard"

validation: PASS
testing: REQUIRED
```

---

### Process for Adding a New Agent (PROD-02+)

**Agents are more complex** because they operate autonomously:

1. **Define agent interface**:
```yaml
agent_id: agent_evaluation_quality
class: agent_component
purpose: "Evaluate content quality and request changes if needed"
autonomy_level: "semi_autonomous"  # vs "fully_autonomous" or "advisory"
decision_threshold: 0.80  # Confidence needed to act
max_iterations: 3  # Max retry attempts

actions_available:
  - request_changes
  - escalate_to_founder
  - approve_conditionally
```

2. **Define decision logic** (in code or prompt-based)

3. **Add to workflow** (WF-XXX) with clear spawn/termination points

4. **Test extensively** (agents can cause loops/deadlocks)

5. **Deployment gate review** (critical)

---

## PART 6: SAFETY LAWS (Never Break These)

### Law 1: Routing Law

**Statement**: All content modifications must flow through Operator API. Never bypass to direct n8n.

**Why**: Ensures:
- Audit trail is complete
- Mode/role checks are enforced
- Provider bridge is respected

**How to Check**: No dossier files should have `direct_n8n_execution: true`

---

### Law 2: Dossier Immutability

**Statement**: Dossiers can only be mutated through documented routes (request_changes, replay, escalate).

**Why**: Prevents:
- Data loss from blind overwrites
- Audit trail gaps
- Approval circumvention

**How to Enforce**: 
```powershell
# Validator checks:
npm run validate:dossiers

# Output:
# ✅ All dossier mutations through routes
# ✅ No blind overwrites detected
# ✅ Audit trail complete
```

---

### Law 3: Provider Bridge Requirement

**Statement**: All real media generation goes through provider bridge. No exceptions.

**Why**: Prevents:
- Unauthorized API calls
- Cost overruns
- Credential exposure

**How to Enforce**:
- Provider bridge defaults to DISABLED (PROD-01)
- Must be explicitly enabled (PROD-02+)
- Cost tracking mandatory when enabled

---

### Law 4: No Silent Mutations

**Statement**: Every change to a dossier must be logged with actor, timestamp, and reason.

**Why**: Enables:
- Root cause analysis
- Audit compliance
- Dispute resolution

**How to Check**:
```powershell
curl http://127.0.0.1:5050/operator/dossier/DOSSIER-xxxxx | Select audit_trail

# Should show every action:
# [
#   {"action": "created", "actor": "creator", "timestamp": "..."},
#   {"action": "wf-100-started", "actor": "system", "timestamp": "..."},
#   {"action": "request_changes", "actor": "founder", "instructions": "...", "timestamp": "..."},
#   {"action": "wf-200-replayed", "actor": "system", "timestamp": "..."}
# ]
```

---

## PART 7: CHECKLIST FOR PROD-02 PLANNING

**When designing new skills/directors for PROD-02**:

- [ ] Understand existing skill/director landscape
- [ ] Identify gap or improvement opportunity
- [ ] Write YAML spec (copy template from above)
- [ ] Validate against schema
- [ ] Plan code changes needed (if any)
- [ ] Identify test cases
- [ ] Plan code review process
- [ ] Plan rollback strategy (in case of failure)
- [ ] Document in skill/director documentation
- [ ] Present to technical team for approval
- [ ] Plan controlled deployment (not to all dossiers at once)

---

## SUMMARY

**PROD-01**:
- ✅ Read all registries
- ✅ Observe directors and skills in action
- ✅ Understand the architecture
- ❌ Do NOT modify, add, or delete

**PROD-02** (4-6 weeks):
- ✅ Add new skills (with approval process)
- ✅ Modify director routing (with approval process)
- ✅ Add agents for quality evaluation
- ✅ Enable providers (image, voice, video, etc.)

**PROD-03+**:
- ✅ Full customization capabilities
- ✅ Custom agents
- ✅ Custom providers
- ✅ Multi-platform publishing

---

**Status**: ✅ PROD-01 READ-ONLY; PROD-02 PROCESS DOCUMENTED  
**Next Step**: Gather improvement ideas for PROD-02 planning phase

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

## Runtime Binding Requirement for Director / Agent / Skill Execution

Directors, agents, and skills are only valid when routed through the corrected runtime profile.

Correct runtime profile:
C:\ShadowEmpire\n8n_user_restore_01

Correct workflow registry:
C:\ShadowEmpire-Git_Restore_01\registries\n8n_webhook_registry.yaml

Correct startup launcher:
C:\ShadowEmpire-Git_Restore_01\scripts\windows\start_n8n_shadow_phase1.ps1

No director, agent, or skill should be treated as operational if:
- n8n loaded old profile.
- only old workflows are visible.
- workflow IDs do not match registry.
- webhook resolver fails.
- WF-000 fails.
- WF-001 -> WF-010 smoke has not passed after recovery.
