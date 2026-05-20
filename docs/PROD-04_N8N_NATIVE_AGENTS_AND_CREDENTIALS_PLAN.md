# PROD-04: n8n Native Agents and Credentials Integration Plan

**Document Type**: Strategic Architecture + Implementation Roadmap  
**Phase**: PROD-04 (NOT_YET_IMPLEMENTED, planned after PROD-03)  
**Status**: DESIGN_ONLY — No runtime execution in PROD-01/02/03  
**Last Updated**: 2026-05-06  
**Audience**: Founder (decision authority), Builder (implementation), Operator (integration testing)

---

## EXECUTIVE SUMMARY

Shadow Creator OS currently routes all operations through the **Operator API → n8n workflow registry → dossier/packet system** (the "Routing Law"). This ensures audit trail, cost gates, and dossier discipline. However, n8n offers three native surfaces that could accelerate certain workflows if properly constrained:

1. **Personal Agents** — Autonomous decision-making in n8n workflows
2. **Workflow Agents** — Agent-aware workflow execution with agentic loops
3. **Chat Hub** — Direct chat interface to workflow agents (user-facing)

This document defines:
- **Why** these surfaces are valuable (speed, context-awareness, credential leverage)
- **Why** they are dangerous (bypass Operator API, lose dossier discipline, no audit trail)
- **The immutable law** that prevents danger (agents may ONLY call Shadow Operator API)
- **The exact 11-phase implementation path** to safely introduce agents in PROD-04
- **The complete provider credential matrix** required for agents to execute real operations
- **The validation gates** before any agent touches production data

---

## PART 1: n8n NATIVE SURFACES — WHAT THEY ARE

### 1.1 Personal Agents (n8n Native)

**Definition**: Stateful, context-aware decision-makers within n8n workflows.

**Capability**:
- Read workflow execution history
- Analyze input/output patterns
- Make conditional routing decisions based on learned patterns
- Update variables and routing rules dynamically
- No direct access to external providers

**Current Status in Shadow**: NOT_IMPLEMENTED, no repo code, no n8n config

**Use Case Example**:
```
Dossier → WF-100 (Topic Intelligence)
  ↓
Personal Agent observes output quality
  ↓
IF quality < threshold: Route to reanalysis
ELSE: Pass to WF-200 (Script Generation)
```

**Constraint for PROD-04**:
- Agent may NOT call external provider directly
- Agent may ONLY write to workflow variables and dossier state
- All external calls must go through `CallShadowOperatorAPI` node

### 1.2 Workflow Agents (n8n Native)

**Definition**: Full workflow orchestrators with agentic loops (think: Claude inside n8n).

**Capability**:
- Read task description and execution context
- Call workflow execution endpoints
- Monitor execution status
- Retry/escalate based on error analysis
- Maintain conversation history with user

**Current Status in Shadow**: NOT_IMPLEMENTED, no repo code, no n8n config

**Use Case Example**:
```
User asks (via Chat Hub): "Create a video about AI trends"

Workflow Agent receives:
  - Task: "Create video"
  - Context: dossier_id, previous outputs, user preferences
  
Agent decides:
  - Step 1: Call WF-100 (topic research)
  - Step 2: Wait for WF-100 result
  - Step 3: Call WF-200 (script generation)
  - Step 4: Wait for WF-200 result
  - Step 5: Call WF-600 (video assembly) IF user has video provider enabled
  - Step 6: Return output to user
  
All calls go through Shadow Operator API ← ROUTING LAW PRESERVED
```

**Constraint for PROD-04**:
- Agent orchestrates workflow calls, does not execute them directly
- Agent may NOT invoke provider endpoints (DALL-E, ElevenLabs, HeyGen, etc.)
- Agent must write all dossier mutations through Operator API /operator/dossier/:id/mutate
- Agent conversation history must be stored in dossier.audit_trail

### 1.3 Chat Hub (n8n Native)

**Definition**: User-facing chat interface connected to Workflow Agents.

**Capability**:
- Accept natural language task descriptions
- Route to appropriate Workflow Agent
- Display streaming agent responses
- Show execution progress
- Offer "approve" / "reject" / "modify" buttons

**Current Status in Shadow**: NOT_IMPLEMENTED, no repo code, no n8n config

**Use Case Example**:
```
User (in Chat Hub): "Create a YouTube script about renewable energy"

Chat Hub receives message
  ↓
Routes to Workflow Agent
  ↓
Agent creates dossier with topic="renewable energy"
  ↓
Agent orchestrates WF-100 → WF-200 → outputs
  ↓
Chat Hub displays: "Script ready for approval"
  ↓
User clicks "APPROVE" OR "Request changes"
  ↓
Operator API records decision, triggers WF-020 (approval handler)
```

**Constraint for PROD-04**:
- Chat Hub is read-only until user clicks "APPROVE"
- All mutations (approval, remodify) must go through Operator API
- Chat Hub must not show sensitive data (credentials, cost, internal state)
- Chat Hub must enforce role-based visibility (Creator sees only dossier outputs, Founder sees approvals, etc.)

---

## PART 2: WHY AGENTS ARE VALUABLE

### 2.1 Speed & Responsiveness

**Current Flow (WF-001 → WF-100 → WF-200)**: 2-5 minutes end-to-end
- WF-001 dossier creation: ~10 sec
- WF-100 topic intelligence: 30-60 sec
- WF-200 script generation: 30-120 sec
- User polls via `/operator/dossier/:id` every 5 sec

**With Workflow Agent (Future)**:
- Agent watches WF-100 completion
- Immediately triggers WF-200 (no polling gap)
- Streams progress to Chat Hub in real-time
- **Estimated savings**: 15-30 sec per dossier

### 2.2 Context & Conversation Continuity

**Current**: Each dossier is stateless; user must repeat context in approval requests

**With Chat Hub**: Agent maintains conversation history:
```
User: "Create a script about climate change"
Agent: "Created dossier-xyz. Script ready."
User: "Make it shorter and more casual"
Agent: (accesses conversation history) "I'll remodify with tone=casual, length=short"
Agent: (calls WF-021 with new instructions)
```

**Result**: Faster iteration, fewer misunderstandings

### 2.3 Credential Leverage

**Current**: Each provider requires manual setup in Operator API config

**With Agent Credential Vault**: 
- Provider credentials stored once in n8n credential vault
- Agent reads credential at execution time
- No re-entry per dossier
- Enables just-in-time provider enablement ("User has ElevenLabs? Use it.")

---

## PART 3: WHY AGENTS ARE DANGEROUS

### 3.1 Risk 1: Operator API Bypass

**Danger**: Agent calls provider directly (e.g., `POST /voice-api.elevenlabs.com/synthesize`)

**Why Bad**:
- No dossier mutation recorded
- No cost tracking
- No audit trail
- No approval gate
- Could violate compliance/governance policies

**Example Disaster**:
```
Agent gets ElevenLabs credential from vault
Agent calls ElevenLabs directly: voice_synthesis(topic_text)
ElevenLabs charges $0.50 to account
Dossier shows $0 cost (because API call bypassed cost gate)
Founder later reviews costs: "Budget exceeded, but why?"
```

**Mitigation Law** (PROD-04): **Agents may ONLY call Shadow Operator API**

### 3.2 Risk 2: Dossier Discipline Loss

**Danger**: Agent mutates dossier state without coordination (race conditions, inconsistent state)

**Why Bad**:
- Multiple agents could run concurrently on same dossier
- Agent A writes approver="founder"
- Agent B writes approver="operator" (overwrites A)
- Dossier state becomes incoherent

**Example Disaster**:
```
Agent-1 running WF-100 on dossier-xyz
Agent-2 running WF-200 on same dossier-xyz (because user restarted workflow)

Agent-1 writes: status="topic_research_complete"
Agent-2 writes: status="script_generation_running"
Both write simultaneously → dossier file corrupted or inconsistent

Later, WF-300 reads dossier and fails: "Expected status=topic_research_complete but got status=script_generation_running"
```

**Mitigation Law** (PROD-04): **All dossier mutations must go through Operator API with distributed lock**

### 3.3 Risk 3: Audit Trail Loss

**Danger**: Agent actions not recorded; impossible to answer "who approved this?" or "why did this fail?"

**Why Bad**:
- Compliance requirement: every decision must be auditable
- Debugging: need full trace of agent logic path
- Cost accountability: need to know which agent triggered which provider calls

**Example Disaster**:
```
Dossier-xyz outputs bad script
Founder asks: "Who approved this?"
Audit log shows: "No approval record" (because agent auto-approved without recording)
Founder asks: "What was the decision logic?"
Audit log shows nothing → impossible to debug

Compare to Routing Law:
Dossier-xyz has approval_decision in audit_trail:
  {
    "actor": "agent_workflow_orchestrator_001",
    "action": "approve",
    "decision_logic": "quality_score >= 0.8",
    "timestamp": "2026-05-06T14:32:00Z",
    "dossier_ref": "dossier-xyz"
  }
```

**Mitigation Law** (PROD-04): **All agent decisions must be written to dossier.audit_trail via Operator API**

---

## PART 4: THE IMMUTABLE AGENT LAW FOR PROD-04+

### 4.1 The Law (Enforced at Architecture Level)

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  AGENT EXECUTION LAW (PROD-04+)                                │
│                                                                 │
│  An n8n Agent (Personal, Workflow, or Chat) may ONLY:         │
│                                                                 │
│  1. Call Shadow Operator API endpoints                         │
│     ├─ POST /operator/new-content-job (create dossier)        │
│     ├─ GET  /operator/dossier/:id (read state)                │
│     ├─ POST /operator/dossier/:id/mutate (update state)       │
│     ├─ POST /operator/approve/:id (approval decision)         │
│     ├─ POST /operator/remodify/:id (request changes)          │
│     ├─ POST /operator/replay/:id (retry stage)                │
│     └─ GET  /operator/outputs/:id (read outputs)              │
│                                                                 │
│  2. Read from n8n internal state (workflow vars, history)      │
│                                                                 │
│  3. Write conversation history to dossier.audit_trail          │
│     via /operator/dossier/:id/mutate endpoint                 │
│                                                                 │
│  Agents may NOT:                                               │
│                                                                 │
│  ✗ Call external providers directly (DALL-E, ElevenLabs, etc) │
│  ✗ Read credentials from vault except for API_KEY_VAULT_MGMT  │
│  ✗ Write dossier files directly (only via Operator API)       │
│  ✗ Bypass cost gates or approval workflows                    │
│  ✗ Execute n8n workflows directly; only call Operator API     │
│  ✗ Skip audit trail logging                                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 4.2 Architecture Enforcement

**Implementation Pattern** (All Agents Follow This):

```json
{
  "agent_id": "workflow_orchestrator_001",
  "agent_type": "Workflow Agent",
  "execution_flow": {
    "step_1_receive_task": "User asks: 'Create YouTube script'",
    "step_2_create_dossier": {
      "call": "Operator API POST /operator/new-content-job",
      "payload": {
        "topic": "AI trends",
        "context": "YouTube video",
        "mode": "creator"
      },
      "response": {
        "dossier_id": "dossier-xyz",
        "status": "CREATED"
      }
    },
    "step_3_monitor_stage": {
      "loop": [
        "Poll Operator API GET /operator/dossier/dossier-xyz",
        "If status = topic_research_complete, proceed",
        "If status = timeout_error, call /operator/replay with instructions"
      ]
    },
    "step_4_no_direct_provider_calls": "❌ NEVER call ElevenLabs, DALL-E, etc directly",
    "step_5_record_decision": {
      "call": "Operator API POST /operator/dossier/dossier-xyz/mutate",
      "payload": {
        "audit_entry": {
          "actor": "workflow_orchestrator_001",
          "action": "workflow_orchestration_complete",
          "decision_logic": "wf_100_success and quality_score >= 0.8",
          "timestamp": "2026-05-06T14:32:00Z"
        }
      }
    },
    "step_6_return_to_user": "Display output via Chat Hub with APPROVE/REJECT buttons"
  }
}
```

### 4.3 Verification & Testing

**Every agent deployment must prove**:

1. ✅ Agent code reviewed for direct provider calls (grep for `elevenlabs`, `openai`, `heygen`, `youtube`, etc.)
2. ✅ Agent test run on non-production dossier, verified zero external API calls
3. ✅ Agent mutations written to audit trail (read dossier.audit_trail, confirm entries exist)
4. ✅ Cost gates respected (agent checks user's budget_remaining before calling WF-600+)
5. ✅ No credentials in agent code or logs (use Operator API endpoints that read vault)

---

## PART 5: PROVIDER CREDENTIAL MATRIX FOR AGENTS

### 5.1 Why Agents Need Credentials

**Current (PROD-01/02/03)**: Credentials hardcoded in environment vars or n8n node config

**With Agents (PROD-04+)**: Credentials stored in n8n credential vault, accessed by agents at runtime

**Benefit**: Agents can check "does user have X provider?" and use it conditionally

**Example**:
```
User enables ElevenLabs credential in Chat Hub
  ↓
Credential stored in n8n vault with user_id reference
  ↓
Workflow Agent asks Operator API: "Can I use ElevenLabs for dossier-xyz?"
  ↓
Operator API checks dossier.capabilities.providers = ["ElevenLabs"]
  ↓
Agent includes WF-610 (Voice Generation) in workflow orchestration
```

### 5.2 Provider Credential Types Required for PROD-04

| Provider | Purpose | Credential Type | Status | Needed for Agent? |
|----------|---------|-----------------|--------|-------------------|
| **ollama_local** | LLM inference (local) | None (socket connection) | ACTIVE | No (no credential) |
| **elevenlabs** | Voice synthesis | API_KEY | DEFERRED_PROD-03 | Yes (if enabled) |
| **heygen** | Avatar video generation | API_KEY + USER_ID | DEFERRED_PROD-03 | Yes (if enabled) |
| **youtube_data_api** | Publishing metadata, analytics | OAUTH_2_CLIENT_CREDENTIALS | DEFERRED_PROD-05 | Yes (if enabled) |
| **openai** | Cloud LLM (GPT-4) | API_KEY | DEFERRED_PROD-02 | Yes (optional speedup) |
| **gemini** | Cloud LLM (Gemini) | API_KEY | DEFERRED_PROD-02 | Yes (optional speedup) |
| **claude_anthropic** | Cloud LLM (Claude) via API | API_KEY | DEFERRED_PROD-02 | Yes (optional speedup) |
| **perplexity** | Cloud LLM (research-focused) | API_KEY | DEFERRED_PROD-02 | Yes (optional) |
| **openrouter** | Multi-provider cloud LLM gateway | API_KEY | DEFERRED_PROD-02 | Yes (optional) |
| **groq** | Fast cloud LLM inference | API_KEY | DEFERRED_PROD-03 | Yes (optional) |
| **deepseek** | Cloud LLM (research-grade) | API_KEY | DEFERRED_PROD-03 | Yes (optional) |
| **mistral** | Cloud LLM (Mistral) | API_KEY | DEFERRED_PROD-02 | Yes (optional) |
| **kimi_k2** | Cloud LLM (K2) | API_KEY | DEFERRED_PROD-03 | Yes (optional) |
| **nano_banana** | Serverless GPU provider | API_KEY | DEFERRED_PROD-04 | Yes (if model-acceleration enabled) |

### 5.3 Credential Vault Integration Pattern

**Location**: n8n native credential vault (built-in, no external service needed)

**Access Pattern** (Agent code):

```javascript
// In n8n Workflow Agent Node (pseudocode)
const userCredentials = await getCredentialsByUserIdAndProvider({
  user_id: "user-001",
  provider: "elevenlabs"
});

if (userCredentials) {
  // User has ElevenLabs enabled
  const canUseElevenLabs = true;
  const api_key = userCredentials.api_key;
  
  // Agent does NOT call ElevenLabs directly
  // Instead, agent tells Operator API to use it
  const result = await operatorAPI.POST("/operator/dossier/dossier-xyz/execute-stage", {
    stage: "WF-610",
    providers_enabled: ["elevenlabs"],
    user_credentials_ref: userCredentials.id
  });
} else {
  // User does not have ElevenLabs
  // Agent skips WF-610, outputs script as-is
  const result = await operatorAPI.GET("/operator/dossier/dossier-xyz");
}
```

### 5.4 Credential Rotation & Expiry (Future: PROD-06)

**For PROD-04**, credentials are static (user adds, never expires).

**For PROD-06+**, implement:
- Credential expiry dates
- Refresh token handling (OAuth providers)
- Rotation alerts (e.g., "ElevenLabs API key expires in 7 days")
- Automatic disablement if credential invalid

---

## PART 6: IMPLEMENTATION PHASES FOR PROD-04

### 6.1 Overview: 11-Phase Path from Design to Production

```
PHASE 1: DISCOVERY & VALIDATION
  ↓
PHASE 2: CREDENTIAL VAULT SETUP
  ↓
PHASE 3: PROVIDER PACKET SCHEMA DEFINITION
  ↓
PHASE 4: WRAPPER WORKFLOW DESIGN (Agent ↔ Operator API bridge)
  ↓
PHASE 5: COST GATE ENFORCEMENT
  ↓
PHASE 6: DRY RUN (non-production dossier, agents observe no-ops)
  ↓
PHASE 7: SINGLE REAL RUN (production dossier, single controlled execution)
  ↓
PHASE 8: DOSSIER WRITEBACK VERIFICATION (check audit trail, state consistency)
  ↓
PHASE 9: OUTPUT INSPECTION & VALIDATION
  ↓
PHASE 10: APPROVAL GATE TESTING (founder approval flow with agents)
  ↓
PHASE 11: PRODUCTION RELEASE & MONITORING
```

### 6.2 Phase 1: Discovery & Validation (Duration: 2-3 days)

**Goal**: Understand n8n native agent capabilities, identify current state in Shadow project

**Deliverables**:
1. n8n Personal Agent demo workflow (read-only, no mutations)
2. n8n Workflow Agent demo workflow (orchestrates dossier creation only)
3. Document: "Agent Capability Matrix" (what agents can/cannot do in n8n v1.x)
4. Decision: "Will Shadow use Personal Agents, Workflow Agents, or both?"

**Validation Gate**:
- [ ] Agents successfully execute /operator/health endpoint
- [ ] Agents successfully read dossier via GET /operator/dossier/:id
- [ ] Agents fail gracefully when attempting direct provider call (test guard rails)

**Files to Create**:
- `workflows/n8n/WF-931_Personal_Agent_Demo.json`
- `workflows/n8n/WF-932_Workflow_Agent_Demo.json`
- `docs/PROD-04_Agent_Capability_Matrix.md`

### 6.3 Phase 2: Credential Vault Setup (Duration: 1-2 days)

**Goal**: Establish n8n credential vault, define schema for all 13 providers

**Deliverables**:
1. Credential schema for each provider (API_KEY format, OAuth scopes, expiry handling)
2. User onboarding guide: "How to add ElevenLabs credential to n8n vault"
3. Audit trail for credential access (who accessed, when, for which dossier)

**Validation Gate**:
- [ ] Can store API_KEY credential for ElevenLabs
- [ ] Can retrieve credential in agent code without exposing key in logs
- [ ] Audit trail records credential access with dossier_id

**Files to Create**:
- `registries/credential_vault_schema.yaml` (defines all 13 provider credential structures)
- `docs/PROD-04_Credential_Onboarding_Guide.md` (user-facing setup instructions)
- `scripts/windows/credential-vault-init.ps1` (initialize vault with test credentials)

**Example Credential Schema**:
```yaml
provider: elevenlabs
credential_type: API_KEY
required_fields:
  - api_key (string, min_length: 32)
optional_fields:
  - voice_id (string, default: "alloy")
  - model_id (string, default: "eleven_monolingual_v1")
expiry: null  # never expires in PROD-04, future: implement refresh logic
cost_limit: optional  # user can set per-dossier spend cap

provider: youtube_data_api
credential_type: OAUTH_2_CLIENT_CREDENTIALS
required_fields:
  - client_id (string)
  - client_secret (string)
  - refresh_token (string)
optional_fields:
  - scopes (list, default: ["youtube.upload", "youtube.readonly"])
expiry: 3600  # seconds until access_token refresh needed
cost_limit: null  # YouTube API free tier
```

### 6.4 Phase 3: Provider Packet Schema Definition (Duration: 2-3 days)

**Goal**: Define JSON schema for each provider's input/output in dossier.packets

**Current State** (PROD-01/02/03):
```
dossier.packets: {
  "pkt_100_topic_research": { ... },
  "pkt_200_script": { ... },
  "pkt_300_metadata": { ... }
}
```

**New State** (PROD-04 with agents calling providers):
```
dossier.packets: {
  "pkt_100_topic_research": { ... },
  "pkt_200_script": { ... },
  "pkt_300_metadata": { ... },
  "pkt_610_voice_generation": {    ← NEW (agent triggered)
    "input": {
      "script_text": "...",
      "voice_provider": "elevenlabs",
      "voice_id": "alloy"
    },
    "output": {
      "audio_file_path": "/dossiers/dossier-xyz/audio_elevenlabs_001.mp3",
      "duration_seconds": 120,
      "cost_usd": 0.18,
      "provider_response_time_ms": 2500
    },
    "audit": {
      "agent_id": "workflow_orchestrator_001",
      "credential_ref": "user-001_elevenlabs_001",
      "timestamp": "2026-05-06T14:32:00Z"
    }
  }
}
```

**Validation Gate**:
- [ ] Schema validates real ElevenLabs response
- [ ] Schema validates cost tracking
- [ ] Schema validates credential reference (no hardcoded keys)

**Files to Create**:
- `registries/packet_schema_WF-610_voice.yaml` (voice output packet structure)
- `registries/packet_schema_WF-620_image.yaml` (image output packet structure)
- `registries/packet_schema_WF-630_music.yaml` (music output packet structure)
- `registries/packet_schema_WF-640_video.yaml` (video output packet structure)
- `registries/packet_schema_WF-650_avatar.yaml` (avatar output packet structure)

### 6.5 Phase 4: Wrapper Workflow Design (Duration: 3-4 days)

**Goal**: Design n8n "bridge" workflows that agents call, which ensure Routing Law compliance

**Pattern**:

```
Agent calls Operator API
  ↓
Operator API receives request
  ↓
Operator API triggers n8n webhook: POST /webhook/agent-request-handler
  ↓
n8n CallShadowOperatorAPI Node executes (wrapper)
  ├─ Validates: request came from authorized agent
  ├─ Validates: dossier_id is valid
  ├─ Checks: user budget_remaining > cost of operation
  ├─ Logs: audit entry with agent_id, decision_logic, timestamp
  ├─ Executes: original n8n workflow (e.g., WF-610 for voice)
  └─ Returns: response to agent via Operator API
  
Agent receives response, displays in Chat Hub
```

**Validation Gate**:
- [ ] Agent calls Operator API endpoint
- [ ] Operator API routes to n8n webhook
- [ ] n8n executes wrapped workflow
- [ ] Response returned to agent with audit trail entry
- [ ] Dossier.audit_trail shows agent action

**Files to Create**:
- `workflows/n8n/WF-940_Agent_Request_Handler.json` (bridge workflow)
- `workflows/n8n/WF-941_Agent_Authorization_Check.json` (security gate)
- `workflows/n8n/WF-942_Agent_Cost_Gate.json` (budget validation)
- `workflows/n8n/WF-943_Agent_Audit_Logger.json` (mutation tracking)

### 6.6 Phase 5: Cost Gate Enforcement (Duration: 2 days)

**Goal**: Ensure agents respect user budgets and cost caps

**Mechanism**:

```
Before Agent Executes Provider:

1. Get user's budget_remaining from dossier.user_profile
2. Get operation's estimated_cost (from provider_registry.yaml)
3. IF budget_remaining < estimated_cost:
     → Escalate to Founder for approval
     → Set dossier.approval_required = true
     → Return "Budget exceeded" to agent
   ELSE:
     → Proceed with provider call
     → Decrement budget_remaining by actual_cost
     → Log cost to dossier.packets.cost_tracking
```

**Example Cost Gate**:

```yaml
operation: elevenlabs_voice_synthesis
estimated_cost_usd: 0.25  # for typical script
max_cost_usd: 1.00  # hardcoded safety limit

operation: openai_gpt4
estimated_cost_usd: 0.10
max_cost_usd: 0.50

operation: heygen_avatar
estimated_cost_usd: 2.00
max_cost_usd: 10.00
```

**Validation Gate**:
- [ ] Agent requests operation with cost > budget
- [ ] Cost gate returns error, does NOT execute provider
- [ ] Operator API escalates to Founder for approval
- [ ] Founder approves, budget_remaining updated, operation executes

**Files to Create**:
- `registries/cost_gate_policy.yaml` (operation costs, budget limits)
- `workflows/n8n/WF-944_Cost_Gate_Validator.json` (enforcement workflow)
- `workflows/n8n/WF-945_Cost_Budget_Updater.json` (ledger management)

### 6.7 Phase 6: Dry Run (Duration: 2 days)

**Goal**: Test agents end-to-end on non-production dossier without triggering real provider charges

**Setup**:
- Create test dossier with flag: `dossier.mode = "dry_run_no_actual_providers"`
- Configure agents to return mock responses instead of calling providers

**Process**:
1. Agent receives: "Create YouTube script about coffee"
2. Agent creates dossier with topic="coffee", mode="dry_run"
3. Agent calls WF-100 (Topic Intelligence) → returns mock research
4. Agent calls WF-200 (Script Generation) → returns mock script
5. Agent calls WF-610 (Voice) → returns mock audio path (no ElevenLabs call)
6. Agent records all actions to dossier.audit_trail
7. Founder reviews: "All dry-run actions recorded. No charges incurred."

**Validation Gate**:
- [ ] Agent creates dossier with dry_run=true
- [ ] Agent orchestrates WF-100 → WF-200 → WF-610 with mocks
- [ ] Zero charges in dossier.cost_tracking
- [ ] All agent actions logged to audit_trail
- [ ] Chat Hub displays output without errors

**Test Checklist**:
- [ ] 5 different agent requests (each testing different workflow path)
- [ ] 10 audit trail entries total (agent decides, logs decision, moves to next step)
- [ ] Zero external API calls (mock all providers)
- [ ] Dossier state transitions correctly (CREATED → TOPIC_RESEARCH → SCRIPT_GENERATED → etc.)

### 6.8 Phase 7: Single Real Run (Duration: 2-3 days)

**Goal**: Execute ONE real production dossier with agent orchestration, with all safety gates active

**Setup**:
- Select low-cost operation (e.g., Ollama voice is free, no external provider call needed)
- Founder pre-approves the test dossier
- Agent has budget of $5.00 USD available

**Process**:
1. Founder creates dossier via Chat Hub: "Create a podcast script about AI"
2. Agent receives task
3. Agent calls WF-100 (Ollama local) → research complete
4. Agent calls WF-200 (Ollama local) → script generated
5. Agent checks: Can I call WF-610 (voice)? → NO, ElevenLabs not enabled for this user
6. Agent returns output to Chat Hub
7. Founder clicks "APPROVE"
8. Operator API records approval, dossier marked READY_FOR_PUBLICATION

**Validation Gate**:
- [ ] Dossier created by agent, not user
- [ ] WF-100 executed successfully, topic_research packet created
- [ ] WF-200 executed successfully, script packet created
- [ ] Agent did NOT attempt WF-610 (correctly detected provider not enabled)
- [ ] Dossier.audit_trail shows: agent_created, agent_orchestrated_wf_100, agent_orchestrated_wf_200, founder_approved
- [ ] Dossier status transitioned correctly through state machine
- [ ] Zero unexpected external API calls

**Test Dossier**:
- Dossier ID: `PROD-04-TEST-SINGLE-REAL-001`
- Topic: "AI trends in 2026"
- Expected cost: $0.00 (Ollama only)
- Expected execution time: 2-3 minutes
- Expected outputs: topic_research packet, script packet

### 6.9 Phase 8: Dossier Writeback Verification (Duration: 1 day)

**Goal**: Confirm that all agent mutations are correctly recorded in dossier files and audit trail

**Verification Checklist**:

For the test dossier from Phase 7, verify:

1. **Dossier File Integrity**:
   ```bash
   Read: /dossiers/PROD-04-TEST-SINGLE-REAL-001/dossier.json
   
   Check:
   ✓ status = "APPROVED_BY_FOUNDER"
   ✓ dossier.workflow_history shows WF-100, WF-200 in order
   ✓ dossier.packets contains pkt_100 and pkt_200
   ✓ dossier.approval_decision = {"actor": "founder", "decision": "approve"}
   ✓ dossier.cost_tracking = {"total": 0.00, "currency": "USD"}
   ```

2. **Audit Trail Completeness**:
   ```bash
   Read: /dossiers/PROD-04-TEST-SINGLE-REAL-001/audit_trail.json
   
   Check:
   ✓ Entry 1: action="dossier_created", actor="workflow_orchestrator_001"
   ✓ Entry 2: action="wf_100_executed", actor="workflow_orchestrator_001"
   ✓ Entry 3: action="wf_200_executed", actor="workflow_orchestrator_001"
   ✓ Entry 4: action="provider_check_wf_610", result="NOT_ENABLED"
   ✓ Entry 5: action="dossier_approved", actor="founder"
   
   Each entry must have:
   ✓ timestamp (ISO 8601)
   ✓ agent_id or actor (not null)
   ✓ decision_logic (why agent took this action)
   ✓ dossier_ref = "PROD-04-TEST-SINGLE-REAL-001"
   ```

3. **Credential Reference Audit**:
   ```bash
   Search dossier.audit_trail and dossier.packets for:
   ✗ Raw API keys (should NOT exist)
   ✗ Hardcoded credentials (should NOT exist)
   ✓ Credential refs like "user-001_ollama_001" (should exist)
   ```

4. **No Orphaned Files**:
   ```bash
   List: /dossiers/PROD-04-TEST-SINGLE-REAL-001/
   
   Expected files:
   ✓ dossier.json
   ✓ audit_trail.json
   ✓ pkt_100_topic_research.json
   ✓ pkt_200_script.json
   
   Unexpected files (danger signs):
   ✗ temp_wf_output.json (orphaned workflow output)
   ✗ agent_debug_log.txt (debug logs should be in audit trail)
   ```

5. **State Machine Correctness**:
   ```bash
   Verify state transitions:
   CREATED → TOPIC_RESEARCH_RUNNING → TOPIC_RESEARCH_COMPLETE 
     → SCRIPT_GENERATION_RUNNING → SCRIPT_GENERATION_COMPLETE 
     → READY_FOR_APPROVAL → APPROVED_BY_FOUNDER
   
   No backwards transitions or skips
   No time reversals (timestamp_2 > timestamp_1 always)
   ```

**Validation Gate**:
- [ ] All 5 audit trail entries exist and are correct
- [ ] Zero raw credentials in dossier
- [ ] State machine transitions valid
- [ ] All output files correspond to executed workflows
- [ ] Cost tracking accurate (even if $0.00)

### 6.10 Phase 9: Output Inspection & Validation (Duration: 1-2 days)

**Goal**: Verify agent-generated outputs are correct and meet quality standards

**Output Quality Checks**:

1. **Script Packet (pkt_200)**:
   ```json
   {
     "artifact_type": "youtube_script",
     "word_count": 450,  // reasonable for YouTube
     "readability_score": 8.2,  // Flesch-Kincaid
     "structure": ["hook", "intro", "body", "cta", "outro"],
     "metadata": {
       "agent_id": "workflow_orchestrator_001",
       "generation_time_ms": 4500,
       "model_used": "ollama:llama2"
     }
   }
   ```

2. **Topic Research Packet (pkt_100)**:
   ```json
   {
     "artifact_type": "topic_research",
     "research_points": 12,  // sufficient depth
     "sources_cited": 5,      // credible references
     "key_insights": ["insight_1", "insight_2", ...],
     "metadata": {
       "search_queries_executed": 4,
       "total_research_time_ms": 3200,
       "confidence_score": 0.92
     }
   }
   ```

**Validation Gate**:
- [ ] Script is valid JSON, parseable
- [ ] Script word count >= 300 (minimum for video)
- [ ] Topic research contains >= 5 distinct points
- [ ] No duplicate content between topic_research and script
- [ ] Metadata correct (agent_id, timestamps, model used)

### 6.11 Phase 10: Approval Gate Testing (Duration: 2 days)

**Goal**: Verify founder approval workflow works correctly with agent-created dossiers

**Test Scenario**:

1. **Setup**:
   - Create 3 test dossiers via agent:
     - Test-A: "YouTube video script" (low complexity)
     - Test-B: "Podcast episode" (medium complexity)
     - Test-C: "Multi-language content" (high complexity)

2. **Founder Workflow**:
   - Founder logs into Operator API
   - Endpoint: `GET /operator/dossier/test-a`
   - Founder sees: topic_research, script, metadata
   - Founder chooses: "APPROVE", "REQUEST REMODIFY", or "REJECT"

3. **If APPROVE**:
   - Endpoint: `POST /operator/approve/test-a`
   - Dossier status → APPROVED_BY_FOUNDER
   - WF-020 (approval handler) triggers
   - Output marked ready for publication

4. **If REQUEST REMODIFY**:
   - Endpoint: `POST /operator/remodify/test-a`
   - Payload: `{instructions: "Make script shorter, add humor"}`
   - WF-021 (replay) triggers
   - Agent receives feedback, orchestrates WF-200 again
   - Script regenerated with new instructions
   - Back to founder for re-approval

5. **If REJECT**:
   - Endpoint: `POST /operator/reject/test-a`
   - Dossier status → REJECTED
   - Agent notified, dossier archived
   - User receives feedback

**Validation Gate**:
- [ ] Founder can approve Test-A (should succeed immediately)
- [ ] Founder can request remodify on Test-B, agent regenerates script
- [ ] Founder can reject Test-C
- [ ] Dossier status transitions correctly for all three paths
- [ ] Audit trail records founder's decision for all three
- [ ] No emails sent during test (manually confirm zero outbound notifications)

**Test Matrix**:

| Test | Initial Status | Founder Action | Expected New Status | Expected Workflow |
|------|---|---|---|---|
| Test-A | READY_FOR_APPROVAL | APPROVE | APPROVED_BY_FOUNDER | WF-020 (approval handler) |
| Test-B | READY_FOR_APPROVAL | REQUEST_REMODIFY | SCRIPT_GENERATION_RUNNING | WF-021 (replay) + WF-200 |
| Test-C | READY_FOR_APPROVAL | REJECT | REJECTED | None (archive) |

### 6.12 Phase 11: Production Release & Monitoring (Duration: 1 week)

**Goal**: Deploy agent functionality to production with monitoring and runbook

**Pre-Release Checklist**:

- [ ] All 10 phases passed validation
- [ ] Zero outstanding security findings
- [ ] Zero outstanding audit trail gaps
- [ ] Cost gates validated (no budget overages)
- [ ] Founder has runbook for troubleshooting agent issues

**Deployment Steps**:

1. **Enable Agent Mode in Production**:
   ```powershell
   npm run operator:modes:set -- --mode=founder --enable-agents=true
   
   # Verify:
   npm run health:check  # should show: agents_enabled=true
   ```

2. **Activate Chat Hub** (Agent-facing UI):
   - Update Open WebUI config: `enable_chat_hub = true`
   - Import Chat Hub tool to Open WebUI
   - Restart Open WebUI: `npm run webui:start`

3. **Activate Workflow Agents in n8n**:
   - Import WF-932 (Workflow Agent) into n8n
   - Set webhook trigger: `/webhook/agent-task-from-chat-hub`
   - Test: send sample Chat Hub request

4. **Monitor for 24 Hours**:
   ```powershell
   npm run operator:health
   # Watch for:
   # - agents_status = online
   # - agent_error_count = 0
   # - chat_hub_requests_last_hour = (reasonable number)
   # - budget_remaining (should decrease as agents work)
   
   npm run logs:view | Select-String "agent"
   # Should see: "Agent workflow started", "Agent approved dossier", etc.
   # Should NOT see: "Agent bypassed cost gate", "Direct provider call detected"
   ```

5. **Weekly Validation**:
   ```powershell
   npm run metrics:weekly
   # Check:
   # - Agent success rate >= 95%
   # - Agent avg execution time <= 5 minutes
   # - Zero unauthorized provider calls
   # - Zero credential leaks in logs
   ```

**Runbook: Agent Troubleshooting**

| Issue | Diagnosis | Recovery |
|---|---|---|
| Agent hangs (>5 min) | Ollama timeout or WF-100 stuck | `npm run operator:replay dossier-xyz --stage WF-100` |
| Chat Hub not responding | Webhook route broken or n8n down | Verify WF-932 is active: `npm run n8n:status` |
| Agent approved without founder | Routing Law violation, agent bypassed approval gate | Immediate: disable agents. Review: audit trail for incident. Run: `npm run validate:agent-safety-gates` |
| Cost gate not enforced | Budget_remaining not checked before provider call | Disable agents immediately. Implement: cost gate policy enforcement test in CI/CD |
| Audit trail missing entries | Agent action not logged | Verify WF-943 (Agent Audit Logger) executing. Check: dossier.audit_trail for gaps. |

**Ongoing Monitoring Metrics** (PROD-04+):

```yaml
metrics:
  agent_requests_per_day:          # should be > 0 after release
  agent_success_rate:              # should be >= 95%
  agent_avg_execution_time_sec:    # should be 150-300 (2.5-5 min)
  agent_budget_spent_per_dossier:  # should track actual vs estimated cost
  agent_error_count:               # should be 0 in normal operation
  agent_unauthorized_provider_calls: # should ALWAYS be 0
  agent_credential_leaks:          # should ALWAYS be 0
  agent_audit_trail_gaps:          # should ALWAYS be 0
```

---

## PART 7: SUCCESS CRITERIA FOR PROD-04

**Agent integration is COMPLETE when**:

✅ All 11 implementation phases passed validation gates
✅ 3 test dossiers created by agents, approved by founder, status verified
✅ Zero credentials exposed in any log or output file
✅ Cost gates enforced (agent cannot exceed budget)
✅ Audit trail complete (100% of agent actions recorded)
✅ Approval workflow functions (founder can approve/reject/remodify agent outputs)
✅ Chat Hub displays outputs correctly (agents → Chat Hub → founder approval)
✅ Monitoring shows: zero unauthorized provider calls, zero state machine violations
✅ Weekly runbook executed successfully (no outstanding issues)
✅ Founder sign-off: "Agents are safe and improving workflow velocity"

---

## PART 8: DEPENDENCIES & BLOCKERS

**Blockers to Agent Release (PROD-04)**:

1. **n8n Credential Vault Stability**: Requires n8n v1.x with working credential storage
   - Current Status: Available in latest n8n (verified in setup)
   - Mitigation: Test credential vault before Phase 2

2. **Provider Cost Estimates**: All providers must publish accurate pricing
   - Current Status: Documented in Phase 6 section
   - Mitigation: Use conservative cost estimates (round up by 20%)

3. **Founder Governance Policy**: Company policy on automation must be approved
   - Current Status: Not present in registries
   - Action Item: Draft policy document before PROD-04 release
   - Example policy: "Agents may execute up to $50 per dossier without approval"

4. **OpenRouter or Cloud Model Access**: If using cloud LLMs in agents
   - Current Status: API keys required, not yet integrated
   - Blocker: Must complete PROD-02 (Cloud Model Onboarding) first
   - Mitigation: Phase 1 agents use Ollama only (local, free)

---

## PART 9: APPENDIX — AGENT CODE EXAMPLES

### 9.1 Example: Workflow Agent Code (Pseudocode)

```javascript
// Workflow Agent entry point (n8n Workflow Execution)
async function orchestrateContentCreation(task) {
  
  // STEP 1: Create dossier via Operator API (NOT direct n8n node)
  const dossier = await operatorAPI.POST("/operator/new-content-job", {
    topic: task.topic,
    context: task.context,
    mode: "creator",
    
    // Agent indicates its identity
    requested_by_agent: "workflow_orchestrator_001",
    agent_request_id: generateUUID()  // for correlation
  });
  
  logToAuditTrail(dossier.id, {
    action: "dossier_created_by_agent",
    agent_id: "workflow_orchestrator_001",
    decision_logic: "User asked for content via Chat Hub"
  });
  
  // STEP 2: Monitor dossier and decide next action
  let status = "CREATED";
  let stage = 0;
  
  while (status !== "READY_FOR_APPROVAL" && stage < 5) {
    
    // Wait a bit
    await sleep(5000);
    
    // Poll Operator API (NOT direct dossier file read)
    const dossierState = await operatorAPI.GET(
      `/operator/dossier/${dossier.id}`
    );
    status = dossierState.status;
    
    if (status === "TOPIC_RESEARCH_COMPLETE") {
      // Topic research is done, proceed to script generation
      const scriptResult = await operatorAPI.POST(
        `/operator/dossier/${dossier.id}/execute-stage`,
        {
          stage: "WF-200",
          topic_research_ref: dossierState.packets.pkt_100_ref,
          agent_id: "workflow_orchestrator_001"
        }
      );
      
      logToAuditTrail(dossier.id, {
        action: "wf_200_triggered",
        agent_id: "workflow_orchestrator_001",
        decision_logic: "Topic research complete, script generation required"
      });
      
      stage++;
    }
    
    if (status === "SCRIPT_GENERATION_COMPLETE") {
      // Check if user has voice provider enabled
      const userCapabilities = await operatorAPI.GET(
        `/operator/dossier/${dossier.id}/user-capabilities`
      );
      
      if (userCapabilities.providers.includes("elevenlabs")) {
        // User HAS ElevenLabs, proceed to voice
        const voiceResult = await operatorAPI.POST(
          `/operator/dossier/${dossier.id}/execute-stage`,
          {
            stage: "WF-610",
            script_ref: dossierState.packets.pkt_200_ref,
            provider: "elevenlabs",
            agent_id: "workflow_orchestrator_001"
          }
        );
        
        logToAuditTrail(dossier.id, {
          action: "wf_610_triggered",
          agent_id: "workflow_orchestrator_001",
          decision_logic: "User has ElevenLabs enabled, voice generation requested"
        });
      } else {
        // User does NOT have ElevenLabs, skip voice
        logToAuditTrail(dossier.id, {
          action: "wf_610_skipped",
          agent_id: "workflow_orchestrator_001",
          decision_logic: "User does not have ElevenLabs credential, cannot voice"
        });
      }
      
      status = "READY_FOR_APPROVAL";
    }
  }
  
  // STEP 3: Dossier is ready, return to Chat Hub for founder approval
  return {
    dossier_id: dossier.id,
    status: "READY_FOR_APPROVAL",
    outputs: {
      topic_research: dossierState.packets.pkt_100,
      script: dossierState.packets.pkt_200,
      voice: dossierState.packets.pkt_610  // null if not generated
    },
    agent_note: "Content ready for founder approval. All actions logged to audit trail."
  };
}

// HELPER: Log to audit trail via Operator API (NOT direct file write)
async function logToAuditTrail(dossierId, entry) {
  await operatorAPI.POST(
    `/operator/dossier/${dossierId}/mutate`,
    {
      mutation_type: "audit_trail_append",
      entry: {
        ...entry,
        timestamp: new Date().toISOString(),
        dossier_ref: dossierId
      }
    }
  );
}

// HELPER: Generate correlation ID
function generateUUID() {
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
    var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
    return v.toString(16);
  });
}

// HELPER: Sleep
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
```

### 9.2 Example: Chat Hub Request → Workflow Agent

**User in Chat Hub**:
```
"Create a YouTube script about AI trends"
```

**Request to n8n Workflow Agent**:
```json
{
  "jsonrpc": "2.0",
  "method": "chat_hub/send_task",
  "params": {
    "user_id": "user-001",
    "user_mode": "creator",
    "task": "Create a YouTube script about AI trends",
    "context": {
      "platform": "youtube",
      "format": "long-form",
      "target_duration_minutes": 10,
      "tone": "professional"
    },
    "agent_id": "workflow_orchestrator_001",
    "request_id": "chat-req-20260506-001"
  }
}
```

**Workflow Agent Processing**:
1. Receives task from Chat Hub
2. Calls `orchestrateContentCreation({topic: "AI trends", context: "YouTube long-form", ...})`
3. Creates dossier via Operator API
4. Triggers WF-100 → WF-200 in sequence
5. Monitors progress via polling
6. Returns to Chat Hub when READY_FOR_APPROVAL

**Response to Chat Hub**:
```json
{
  "status": "success",
  "dossier_id": "dossier-20260506-001",
  "message": "YouTube script ready for your approval",
  "outputs": {
    "topic_research": {
      "key_points": ["AI adoption rate", "Top use cases", "Competitive landscape"],
      "sources": 8
    },
    "script": {
      "word_count": 1850,
      "structure": "hook → intro → 3 body sections → cta → outro",
      "estimated_duration_minutes": 9.5
    }
  },
  "action_buttons": ["APPROVE", "REQUEST CHANGES", "REJECT"],
  "agent_note": "All research and writing completed in 3.2 minutes"
}
```

**User in Chat Hub Clicks "APPROVE"**:
```
Chat Hub sends: POST /operator/approve/dossier-20260506-001
Operator API records approval, triggers WF-020
Dossier status → APPROVED_BY_FOUNDER
Agent receives confirmation: "Your content has been approved"
```

---

## PART 10: GLOSSARY OF TERMS

| Term | Definition | Example |
|------|-----------|---------|
| **Routing Law** | All operations must flow: UI → Operator API → n8n → dossier | Agent calls `/operator/new-content-job`, not n8n directly |
| **Dossier Discipline** | All mutations recorded in dossier.audit_trail | Agent action = audit entry + dossier update |
| **Provider Bridge** | Safety boundary preventing real media in PROD-01/02/03 | ElevenLabs calls blocked until PROD-03 release |
| **Credential Vault** | n8n native storage for API keys, OAuth tokens | ElevenLabs API key stored, retrieved by agent at runtime |
| **Cost Gate** | Budget enforcement before provider execution | Agent checks user's $50 budget before calling ElevenLabs |
| **Audit Trail** | Immutable log of all dossier mutations | "agent_orchestrator_001 triggered WF-100 at 2026-05-06T14:32:00Z" |
| **Approval Gate** | Human decision point before publication | Founder approves/rejects/remodifies agent outputs |
| **Dry Run** | Test execution without real provider calls | Agent creates dossier with mock outputs, zero charges |
| **Agent Request ID** | Unique correlation ID per agent request | "chat-req-20260506-001" used to match agent → dossier |
| **Wrapper Workflow** | n8n bridge ensuring Routing Law compliance | WF-940 (Agent Request Handler) validates requests |
| **Dossier Writeback** | Persistence of agent mutations to dossier files | Dossier.audit_trail updated after each agent action |

---

**Status**: 📋 DESIGN_ONLY — Not yet implemented  
**Target Release**: PROD-04 (Q3 2026 estimate, after PROD-02/03 complete)  
**Validation Gate**: All 11 phases must pass before production deployment  
**Founder Authority**: Required for PROD-04 release decision

---

