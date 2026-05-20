# Shadow Creator OS — PROD-02 Through PROD-07 Roadmap

**Document Type**: Strategic Phase Roadmap + Implementation Plan  
**Coverage**: PROD-02 through PROD-07 (24+ months of planned development)  
**Status**: DESIGN_ONLY — No work started on PROD-02+  
**Last Updated**: 2026-05-06  
**Audience**: Founder (go/no-go decisions), Builder (long-term planning), Operator (deployment timeline)

---

## EXECUTIVE SUMMARY

Shadow Creator OS is designed as a **7-phase release roadmap**:

| Phase | Name | Focus | Timeline | Status |
|-------|------|-------|----------|--------|
| **PROD-01** | **Local LLM Foundation** | Ollama, Operator API, dossier system | 0-4 weeks | ✅ ACTIVE |
| **PROD-02** | **Cloud Model Speed Layer** | GPT-4, Claude, Gemini alternatives | Weeks 4-10 | 🔴 DEFERRED |
| **PROD-03** | **Provider Bridge Execution** | Voice, avatar, images, video composition | Weeks 10-20 | 🔴 DEFERRED |
| **PROD-04** | **n8n Native Agent Surface** | Personal/Workflow agents, Chat Hub | Weeks 20-28 | 🔴 DEFERRED |
| **PROD-05** | **Multi-Channel Publishing** | YouTube, Instagram, TikTok, LinkedIn, Blog, Podcast | Weeks 28-40 | 🔴 DEFERRED |
| **PROD-06** | **Custom GUI + Scheduler** | Dashboard, channel calendar, automation rules | Weeks 40-52 | 🔴 DEFERRED |
| **PROD-07** | **Scaling & Storage** | PostgreSQL, Redis, Qdrant, multi-user, backup automation | Weeks 52-78 | 🔴 FUTURE |

**Total Roadmap**: ~18 months from PROD-01 to PROD-07 fully deployed

This document defines for **each phase**:
1. **Goal**: What problem this phase solves
2. **What Becomes Live**: Features users see/use
3. **What Remains Deferred**: Blocked features
4. **Prerequisites**: What must be done first
5. **Files to Create/Modify**: Code changes needed
6. **n8n Workflows**: Which WF-XXX workflows to add
7. **Credentials Required**: API keys to set up
8. **Validation Gate**: How to prove phase is working
9. **Rollback Plan**: How to revert if issues occur
10. **Success Criteria**: Definition of "done"

---

## PHASE PROD-01: LOCAL LLM FOUNDATION (✅ Active, Weeks 0-4)

### 1.1 Phase Goal

Establish working dossier system with local Ollama LLM, proving core architecture is sound.

**Actual Status**: ✅ COMPLETE
- Ollama running locally (Llama 3.2)
- Operator API functional
- Open WebUI integrated
- n8n workflows WF-001, WF-100, WF-200 working
- Dossier creation end-to-end tested
- Audit trail logging functional

### 1.2 What Becomes Live (PROD-01)

✅ **Operating Modes**:
- Creator mode (default)
- Founder mode (approval authority)
- Builder mode (debugging)
- Operator mode (monitoring)

✅ **Dossier System**:
- JSON-based dossier storage
- Packet lineage tracking
- Audit trail immutable logging
- Cost tracking (zero cost for Ollama)

✅ **User Interfaces**:
- Open WebUI chat (primary)
- Operator API via curl/PowerShell
- n8n UI (for technical users)

✅ **Core Workflows**:
- WF-001: Dossier creation
- WF-010: Router (decides which lane)
- WF-100: Topic intelligence (Ollama research)
- WF-200: Script generation (Ollama writing)
- WF-020: Approval handler
- WF-021: Replay/remodify handler

✅ **Content Modes** (Stubs Only):
- Photo generation (WF-610 stub, PROVIDER_BRIDGE_REQUIRED)
- Script generation (WF-200 working)
- Debate mode (stub)
- Video creation (stub)
- Avatar creation (stub)
- Music generation (stub)
- Songs generation (stub)
- Poetry generation (stub)

### 1.3 What Remains Deferred (PROD-01)

🔴 **Blocked Until PROD-02**:
- Cloud LLMs (GPT-4, Claude, Gemini)
- Speed optimization via parallel execution
- Model selection (user choice of LLM)

🔴 **Blocked Until PROD-03**:
- Real media generation (voice, avatar, images, video)
- Provider bridge execution
- Provider credentials storage

🔴 **Blocked Until PROD-04**:
- n8n native agents
- Chat Hub agent interface
- Agent orchestration

🔴 **Blocked Until PROD-05**:
- Multi-channel publishing
- YouTube/Instagram/TikTok upload
- Scheduler automation

🔴 **Blocked Until PROD-06**:
- Custom GUI dashboard
- Channel calendar
- Analytics aggregation

### 1.4 Prerequisites for PROD-01

✅ All completed:
- Ollama installed locally
- n8n running
- PostgreSQL/SQLite for state
- Node.js environment
- npm packages installed

### 1.5 Files Created/Modified (PROD-01)

**Core Operator API** (engine/operator.js):
- POST /operator/new-content-job (create dossier)
- GET /operator/dossier/:id (read dossier)
- POST /operator/approve/:id (approval)
- POST /operator/remodify/:id (feedback loop)
- POST /operator/replay/:id (retry)
- GET /operator/health (system health)
- POST /operator/modes/set (mode switching)

**n8n Workflows** (workflows/n8n/):
- WF-001_Dossier_Create.json
- WF-010_Parent_Router.json
- WF-100_Topic_Intelligence.json
- WF-200_Script_Generation.json
- WF-020_Approval_Handler.json
- WF-021_Replay_Remodify.json

**Registries** (registries/):
- provider_registry.yaml (Ollama: ACTIVE)
- model_registry.yaml (Llama 3.2: ACTIVE)
- workflow_registry.yaml (WF-001/010/100/200/020/021: ready)
- mode_registry.yaml (4 operating modes defined)
- operational_modes.yaml (8 operational modes: stub)

**Documentation** (docs/):
- PROD-01_STARTUP_CHECKLIST.md (✅ Created)
- PROD-01_USER_OPERATING_GUIDE.md (✅ Created)
- PROD-01_CAPABILITY_LIST.md (✅ Created)
- PROD-01_COMMAND_ATLAS.md (✅ Created)
- PROD-01_DECISION_AND_REFERENCE_MATRICES.md (✅ Created)
- PROD-01_MODES_MODULES_TASKS_RUNBOOK.md (✅ Created)
- PROD-01_TROUBLESHOOTING_AND_RECOVERY.md (✅ Created)
- PROD-01_DIRECTOR_AGENT_SKILL_OPERATIONS.md (✅ Created)
- PROD-03_PROVIDER_BRIDGE_AND_MEDIA_MODES_ROADMAP.md (✅ Created)
- PROD-04_PENDING_MODULES_MASTER_LEDGER.md (✅ Created)

### 1.6 Validation Gate (PROD-01)

✅ **Proven Working**:
```powershell
npm run health:check
# Output: status: healthy, All services: ✅

npm run operator:test
# Output: All acceptance tests passed (37/37)

# Dossier creation via Open WebUI
POST http://localhost:3000 → "Create YouTube script about AI"
# Response: dossier_id = "DOSSIER-001", status = "CREATED"

# Monitor workflow
GET /operator/dossier/DOSSIER-001
# Shows: WF-100 running, topic research 45% complete

# Approval workflow
POST /operator/approve/DOSSIER-001
# Response: status = "APPROVED_BY_FOUNDER"

# All audit trail entries visible in dossier.json
```

### 1.7 Success Criteria (PROD-01) ✅ MET

✅ Founder can create dossier via Open WebUI  
✅ Dossier flows through WF-100 → WF-200  
✅ Founder can approve outputs  
✅ Audit trail complete  
✅ Cost tracking shows $0.00  
✅ System handles errors gracefully  
✅ All npm scripts verified working  
✅ All API endpoints verified working  

---

## PHASE PROD-02: CLOUD MODEL SPEED LAYER (Weeks 4-10, ~6 weeks)

### 2.1 Phase Goal

Add optional cloud LLM integration to speed up script generation (GPT-4, Claude, Gemini, etc.).

**Key Benefit**: WF-200 (script generation) drops from 30-120 sec (Ollama) to 5-10 sec (GPT-4)

### 2.2 What Becomes Live (PROD-02)

✅ **Multiple LLM Options**:
- Ollama (local, free, default)
- OpenAI GPT-4 ($0.15 per dossier)
- Claude Anthropic ($0.05 per dossier, premium quality)
- Gemini ($0.10 per dossier)
- OpenRouter (multi-model gateway)
- Groq (ultra-fast inference)
- Mistral (cost-optimized)
- Perplexity (research-focused)
- DeepSeek (very cheap)

✅ **Speed Improvements**:
- WF-100 with GPT-4: 5-10 sec (vs 45 sec with Ollama)
- WF-200 with Claude: 5-10 sec (vs 60 sec with Ollama)
- Total cycle time: ~1 minute (vs 2-5 minutes PROD-01)

✅ **Cost Options**:
- Free tier (Ollama only, default)
- Budget tier ($5-10/dossier, use Mistral/OpenRouter)
- Premium tier ($10-20/dossier, use GPT-4/Claude)

✅ **User Control**:
- Open WebUI tool menu shows "Model" selector
- User can choose: Ollama, GPT-4, Claude, etc.
- Cost estimate shown before execution
- Budget still enforced (never exceed daily limit)

### 2.3 What Remains Deferred (PROD-02)

🔴 **Not in PROD-02**:
- Real media generation (voice, avatar, images) — PROD-03
- Provider bridge execution — PROD-03
- Multi-channel publishing — PROD-05
- Custom GUI — PROD-06

### 2.4 Prerequisites for PROD-02

✅ **Required**:
- PROD-01 fully functional
- OpenAI API account (for GPT-4 access)
- Anthropic API account (for Claude access)
- Gemini API account (optional)
- OpenRouter account (optional)

⚠️ **Risk**: API rate limits, cost overages if not careful

### 2.5 Files to Create/Modify (PROD-02)

**Operator API** (engine/operator.js):
- Add: `POST /operator/modes/set-model` (choose which LLM)
- Modify: `POST /operator/new-content-job` (accept model parameter)
- Add: `GET /operator/models/available` (list models + pricing)

**n8n Workflows** (workflows/n8n/):
- Modify: WF-100_Topic_Intelligence.json
  - Add parallel execution: Ollama route + GPT-4 route
  - User selects preferred route
- Modify: WF-200_Script_Generation.json
  - Add router: If model=GPT-4, call OpenAI API
  - If model=Ollama, call Ollama locally
  - Fallback to Ollama if GPT-4 unavailable

**n8n Credential Nodes**:
- Create: OpenAI API credential node
- Create: Anthropic API credential node
- Create: Gemini API credential node
- Create: OpenRouter credential node

**Registries** (registries/):
- Modify: model_registry.yaml
  - Add: openai_gpt4 (ACTIVE_PROD-02)
  - Add: anthropic_claude (ACTIVE_PROD-02)
  - Add: gemini (ACTIVE_PROD-02)
  - Add: openrouter (ACTIVE_PROD-02)
  - Add: groq (DEFERRED_PROD-03)

**Open WebUI** (ui/src/):
- Add: Model selector dropdown in Open WebUI chat interface
- Show: Cost estimate for selected model
- Add: "Use Ollama" fallback warning if cloud model offline

### 2.6 n8n Workflows to Add/Modify (PROD-02)

**New Workflows**:
- (None — just modify existing WF-100, WF-200)

**Modified Workflows**:
- WF-100 (Topic Intelligence):
  - Add node: Decision (model == GPT-4 or Ollama?)
  - Path 1: Call GPT-4 API (5 sec expected)
  - Path 2: Call Ollama (45 sec expected)
  - Merge results before output

- WF-200 (Script Generation):
  - Add node: Decision (model == Claude or Ollama?)
  - Path 1: Call Claude API (8 sec expected)
  - Path 2: Call Ollama (90 sec expected)
  - Merge results, output to dossier

### 2.7 Credentials Required (PROD-02)

| Provider | Credential | Obtain From | Cost | For What |
|----------|-----------|---|---|---|
| OpenAI | API Key | https://platform.openai.com | $0 setup, pay-as-you-go | GPT-4 model |
| Anthropic | API Key | https://console.anthropic.com | $0 setup, pay-as-you-go | Claude model |
| Gemini | API Key | https://ai.google.dev | $0 setup, free tier available | Gemini model |
| OpenRouter | API Key | https://openrouter.ai | $0 setup, pay-as-you-go | Multi-model gateway |
| Groq | API Key | https://console.groq.com | $0 setup, free tier | Fast inference |

### 2.8 Validation Gate (PROD-02)

```powershell
# Test: Create dossier with GPT-4
POST /operator/new-content-job
{
  "topic": "AI trends",
  "model": "gpt-4"
}

# Expected: Script generated in ~10 sec (vs 90+ sec with Ollama)
# Expected: Cost shows $0.15 (GPT-4 cost)
# Expected: Audit trail shows: "Used GPT-4 model for script generation"

# Test: Cost gate enforced
POST /operator/new-content-job
{
  "topic": "AI trends",
  "model": "gpt-4",
  "user_budget": $2.00
}
# Expected: Error if dossier cost > budget
# Expected: Founder approval required for overage

# Test: Fallback to Ollama
If OpenAI API offline:
  POST /operator/new-content-job
  {
    "topic": "AI trends",
    "model": "gpt-4"
  }
  # Expected: Auto-fallback to Ollama
  # Expected: Audit trail shows: "GPT-4 unavailable, using Ollama fallback"

# Verification
npm run validate:all
# Expected: All workflows still functional, no regressions
```

### 2.9 Rollback Plan (PROD-02)

If cloud LLM integration causes issues:

```powershell
# 1. Disable cloud models in registries
npm run registry:disable-model --model=gpt-4

# 2. Revert n8n workflows to PROD-01 version
npm run n8n:rollback --workflow=WF-100 --version=prod-01

# 3. Verify Ollama still works
npm run health:check

# 4. Clear any failed dossiers
npm run dossier:revert --status=error --since-date=today

# 5. Re-enable once fixes applied
npm run registry:enable-model --model=gpt-4
```

### 2.10 Success Criteria (PROD-02)

✅ Script generation time reduced to <10 sec with GPT-4 (vs 60+ sec with Ollama)  
✅ User can select model via Open WebUI dropdown  
✅ Cost estimates accurate (actual cost ±10%)  
✅ Daily budget enforced (no overage possible)  
✅ Fallback to Ollama if cloud model unavailable  
✅ All PROD-01 features still working (backward compatible)  
✅ Zero unauthorized API calls (audit trail shows all usage)  
✅ Founder sign-off: "PROD-02 ready for production"  

---

## PHASE PROD-03: PROVIDER BRIDGE EXECUTION (Weeks 10-20, ~10 weeks)

### 3.1 Phase Goal

Enable real media generation: voice (ElevenLabs), avatars (HeyGen), images (DALL-E), video composition (FFmpeg).

**Key Benefit**: User can now generate full multimedia content (script + voice + avatar + images).

### 3.2 What Becomes Live (PROD-03)

✅ **Media Providers** (All with cost gates):
- **ElevenLabs** (voice synthesis): $0.15/dossier
- **HeyGen** (avatar video): $2.00/dossier
- **DALL-E 3** (images): $0.12/image
- **Wav2Lip** (lipsync): $0.00 (open-source, local)
- **FFmpeg** (video composition): $0.00 (open-source, local)

✅ **Content Lanes** (All functional):
- WF-610: Image generation (DALL-E)
- WF-620: Image curation (stock images, Google Images)
- WF-630: Music generation (stub, or licensed music)
- WF-640: Video assembly (FFmpeg)
- WF-650: Avatar generation (HeyGen)
- WF-660: Publishing (YouTube upload)

✅ **Cost Tracking**:
- Per-dossier cost: $0.27 (voice + image) to $2.27 (voice + avatar + image)
- Daily budget: $50.00 (default, Founder adjustable)
- Weekly budget: $350.00
- Monthly projection: $1,050.00

✅ **Quality** (Post-approval only):
- Voice synthesis quality acceptable (no artifacts)
- Avatar lipsync quality good (smooth movements)
- Image generation quality matches prompt
- Video composition has no corruption

### 3.3 What Remains Deferred (PROD-03)

🔴 **Not in PROD-03**:
- n8n native agents — PROD-04
- Multi-channel publishing automation — PROD-05
- Custom GUI dashboard — PROD-06
- Scaling (Postgres, Redis) — PROD-07

### 3.4 Prerequisites for PROD-03

✅ **Required**:
- PROD-01 fully functional
- PROD-02 fully functional (cloud models optional)
- ElevenLabs API account + API key
- HeyGen API account + API key
- OpenAI API account (DALL-E access)
- Ollama, n8n, Operator API running

⚠️ **Risk**: Significant cost exposure if budgets not enforced

### 3.5 Files to Create/Modify (PROD-03)

**Operator API** (engine/operator.js):
- Add: `POST /operator/dossier/:id/execute-stage` (run specific WF)
- Add: `POST /operator/providers/:name/validate` (test provider credentials)
- Modify: `/operator/new-content-job` (add media provider selection)

**n8n Workflows** (workflows/n8n/):
- Create: WF-610_Image_Generation.json (DALL-E)
- Create: WF-620_Image_Curation.json (stock images)
- Create: WF-630_Music_Generation.json (stub or licensed)
- Create: WF-640_Video_Assembly.json (FFmpeg)
- Create: WF-650_Avatar_Generation.json (HeyGen)
- Create: WF-660_YouTube_Publishing.json (upload videos)
- Modify: WF-300, WF-400, WF-500 (replace stubs with working code)

**n8n Credential Nodes**:
- Create: ElevenLabs API credential
- Create: HeyGen API credential
- Create: OpenAI API (already done PROD-02)
- Create: YouTube OAuth credential
- Create: YouTube Analytics credential

**Registries** (registries/):
- Modify: provider_registry.yaml
  - Change: elevenlabs_api from DEFERRED to ACTIVE_PROD-03
  - Change: heygen_api from DEFERRED to ACTIVE_PROD-03
  - Change: dalle3_api from DEFERRED to ACTIVE_PROD-03
  - Add: wav2lip (ACTIVE_PROD-03, free)
  - Add: ffmpeg (ACTIVE_PROD-03, free)

**Cost Gate Policy** (registries/):
- Create: cost_gate_policy.yaml
  - Define: Per-provider spend limits
  - Define: Per-user daily budget
  - Define: Approval thresholds ($1+ requires approval)

**Documentation** (docs/):
- PROD-05_PROVIDER_BRIDGE_IMPLEMENTATION_BACKLOG.md (✅ Already created)

### 3.6 n8n Workflows to Add/Modify (PROD-03)

**New Workflows** (all must follow async pattern for HeyGen):

- **WF-610**: Image Generation (DALL-E)
  - Input: description from pkt_200 (script)
  - Call: DALL-E API
  - Output: image_file_path, cost, metadata
  - Async: Synchronous (fast, 10-20 sec)

- **WF-620**: Image Curation (optional)
  - Input: description from pkt_200
  - Search: Google Images or Unsplash API
  - Output: 3-5 curated images
  - Cost: $0.00 (free APIs)

- **WF-630**: Music Generation (stub)
  - Input: mood/tone from metadata
  - Options: 
    - A) Stub output (silent, no music)
    - B) Licensed music API (Epidemic Sound, Artlist)
    - C) AI music gen (MusicGen, Runway)
  - For PROD-03: Stub implementation

- **WF-640**: Video Assembly (FFmpeg)
  - Input: avatar_video (from WF-650), voice_audio (from WF-610), background_music (WF-630)
  - Process: FFmpeg command to compose streams
  - Output: final_video_file, duration, size
  - Async: Asynchronous (~1-2 min per video)

- **WF-650**: Avatar Generation (HeyGen)
  - Input: script (from pkt_200), voice (from pkt_610 if available)
  - Call: HeyGen API (asynchronous, returns job_id)
  - Poll: Check status every 30 sec until complete
  - Output: video_file_path, duration, cost
  - Async: Asynchronous (2-3 min per video)
  - ⚠️ **Critical**: Must implement polling mechanism

- **WF-660**: YouTube Publishing
  - Input: final_video (from WF-640), title (from pkt_300), description, tags
  - Call: YouTube Data API (OAuth)
  - Output: youtube_video_id, watch_url
  - Async: Asynchronous (upload can take 5-10 min for large files)

**Modified Workflows**:

- **WF-300**: Metadata Planning
  - Replace: Stub with actual metadata generation
  - Input: topic (pkt_100), script (pkt_200)
  - Output: Title, description, tags, category
  - Cost: $0.00 (Ollama)

- **WF-400**: Production Planning
  - Replace: Stub with production planning logic
  - Input: metadata (pkt_300), user preferences
  - Output: Which media providers to use, timeline estimates
  - Cost: $0.00 (logic only)

- **WF-500**: Publishing Prep
  - Replace: Stub with pre-publishing checklist
  - Input: all packets (research, script, images, voice, video)
  - Output: Publishing readiness (pass/fail), required actions
  - Cost: $0.00

### 3.7 Credentials Required (PROD-03)

| Provider | Credential | Cost | Type |
|----------|-----------|------|------|
| ElevenLabs | API Key | $0 setup + usage | Sync |
| HeyGen | API Key | $0 setup + usage | Async (polling) |
| DALL-E | API Key (OpenAI) | $0 setup + usage | Sync |
| YouTube Data API | OAuth 2.0 Refresh Token | $0 | Async |
| YouTube Analytics | OAuth 2.0 Refresh Token | $0 | Async |
| Wav2Lip | None (local, open-source) | $0 | Local executable |
| FFmpeg | None (local, open-source) | $0 | Local executable |

### 3.8 Validation Gate (PROD-03)

**Test 1: Single Real Run (Voice Only)**
```powershell
# Create dossier with voice synthesis enabled
POST /operator/new-content-job
{
  "topic": "AI trends",
  "providers_enabled": ["elevenlabs"]
}

# Expected:
# - WF-100: Topic research complete (Ollama)
# - WF-200: Script generated (Ollama or GPT-4)
# - WF-610: Voice synthesized (ElevenLabs), cost $0.15
# - Dossier shows: 2 packets (research, script, voice)
# - Audit trail: All actions logged with timestamps
# - Cost tracking: $0.15 deducted from budget
```

**Test 2: Single Real Run (Voice + Avatar)**
```powershell
POST /operator/new-content-job
{
  "topic": "AI trends",
  "providers_enabled": ["elevenlabs", "heygen"]
}

# Expected:
# - WF-100: Topic research (45 sec, Ollama)
# - WF-200: Script generation (60 sec, Ollama)
# - WF-610: Voice synthesis (15 sec, ElevenLabs)
# - WF-650: Avatar video (2-3 min, HeyGen polling)
#   ├─ Job submitted: Returns job_id
#   ├─ Poll every 30 sec: "processing" → "completed"
#   ├─ Download video from CDN
#   └─ Save to dossier
# - Total time: ~4-5 minutes
# - Cost: Voice $0.15 + Avatar $2.00 = $2.15
# - Audit trail: All steps + polling attempts logged
```

**Test 3: Multi-Media (Voice + Avatar + Images)**
```powershell
POST /operator/new-content-job
{
  "topic": "AI trends",
  "providers_enabled": ["elevenlabs", "heygen", "dalle3"]
}

# Expected:
# - All workflows execute in optimal order (WF-610 and WF-650 in parallel)
# - Total cost: $0.15 + $2.00 + $0.12 = $2.27
# - Founder can approve/reject outputs
# - All media files accessible for download
```

**Test 4: Cost Gate Enforcement**
```powershell
# Set user budget to $2.00
POST /operator/new-content-job
{
  "topic": "AI trends",
  "providers_enabled": ["elevenlabs", "heygen"],  # Would cost $2.15
  "user_budget": $2.00
}

# Expected: Error returned
# "Budget insufficient: Required $2.15, Available $2.00"
# "Escalate to Founder for approval?"
```

**Test 5: Verification Commands**
```powershell
npm run validate:all
# Expected: All workflows functional, no regressions

npm run health:check
# Expected: status=healthy, all services running

npm run metrics:daily
# Expected: Cost breakdown shows ElevenLabs + HeyGen usage

# Check dossier
Get-Content dossiers/DOSSIER-001/dossier.json | ConvertFrom-Json | Select-Object packets
# Expected: packets contains pkt_100, pkt_200, pkt_610 (voice), pkt_650 (avatar)
```

### 3.9 Rollback Plan (PROD-03)

```powershell
# If provider integration breaks:

# 1. Disable problematic provider
npm run registry:disable-provider --provider=elevenlabs

# 2. Revert n8n workflows
npm run n8n:rollback --workflow=WF-610 --version=stub

# 3. Clear failed dossiers
npm run dossier:revert --status=error --provider=elevenlabs

# 4. Verify PROD-02 still works (cloud LLMs)
npm run health:check

# 5. Apply fix (credential, workflow bug, etc.)
# ... fix ...

# 6. Re-enable provider
npm run registry:enable-provider --provider=elevenlabs

# 7. Test single dossier
POST /operator/new-content-job (as per validation gate above)
```

### 3.10 Success Criteria (PROD-03)

✅ ElevenLabs voice synthesis working, cost accurate  
✅ HeyGen avatar generation working with polling  
✅ DALL-E image generation working  
✅ FFmpeg video composition working  
✅ Cost gates prevent budget overages  
✅ Full multimedia dossier (research + script + voice + avatar + images) functional  
✅ Founder can approve/reject outputs  
✅ Multi-channel publishing prep (WF-500) working  
✅ All PROD-01/02 features still working  
✅ Audit trail complete for all provider calls  
✅ Founder sign-off: "PROD-03 ready for production"  

---

## PHASE PROD-04: N8N NATIVE AGENT SURFACE (Weeks 20-28, ~8 weeks)

### 4.1 Phase Goal

Enable n8n Personal/Workflow agents + Chat Hub UI for autonomous task orchestration.

**Key Benefit**: Users can type natural language tasks ("Create YouTube video about AI") and agents autonomously execute without manual workflow stage triggering.

### 4.2 What Becomes Live (PROD-04)

✅ **Agent Types**:
- Personal Agents (read dossier state, make routing decisions)
- Workflow Agents (orchestrate multi-stage workflows)
- Chat Hub (natural language interface to agents)

✅ **Agent Capabilities**:
- Read dossier state via Operator API
- Decide which workflow to run next
- Monitor workflow execution
- Retry failed stages
- Escalate to Founder if needed
- Log all decisions to audit trail

✅ **Chat Hub UI**:
- User types: "Create 10-minute YouTube video about renewable energy"
- Agent receives task
- Agent creates dossier
- Agent orchestrates WF-100 → WF-200 → WF-610 → WF-650 → WF-660
- Agent returns: "Content ready, [APPROVE] [REJECT] [MODIFY]"

### 4.3 Prerequisites for PROD-04

✅ **Required**:
- PROD-01, 02, 03 fully functional
- n8n v1.x with agent capabilities
- All provider credentials from PROD-03 in place

### 4.4 Files to Create/Modify (PROD-04)

**Operator API** (engine/operator.js):
- Modify: `/operator/dossier/:id` (add support for agent mutations)
- Add: `POST /operator/dossier/:id/mutate` (for agents to update audit trail)

**n8n Workflows** (workflows/n8n/):
- Create: WF-931_Personal_Agent_Demo.json
- Create: WF-932_Workflow_Agent_Main.json
- Create: WF-940_Agent_Request_Handler.json
- Create: WF-941_Agent_Authorization_Check.json
- Create: WF-942_Agent_Cost_Gate.json
- Create: WF-943_Agent_Audit_Logger.json

**Registries** (registries/):
- Create: agent_registry.yaml (list agents, capabilities, constraints)

**Documentation** (docs/):
- PROD-04_N8N_NATIVE_AGENTS_AND_CREDENTIALS_PLAN.md (✅ Already created)

### 4.5 n8n Workflows to Add (PROD-04)

- **WF-931**: Personal Agent Demo
  - Read-only agent that observes dossier state
  - Makes simple routing decisions (quality score > 0.8? Continue : Retry)
  - Does NOT execute workflows, just provides suggestions

- **WF-932**: Workflow Agent (Main)
  - Accepts natural language task from Chat Hub
  - Creates dossier with task description
  - Orchestrates workflow stages (WF-100 → WF-200 → media providers)
  - Monitors execution, handles retries
  - Returns results to Chat Hub for approval

- **WF-940**: Agent Request Handler (Bridge)
  - Validates agent request came from authorized agent
  - Checks cost gates (budget sufficient?)
  - Routes to appropriate workflow
  - Returns response to agent

- **WF-941**: Agent Authorization Check
  - Verify agent has permission for requested action
  - Check role (Founder > Operator > Creator)
  - Prevent unauthorized operations

- **WF-942**: Agent Cost Gate
  - Check user budget before executing expensive operations
  - Escalate to Founder if cost > threshold
  - Block operation if budget insufficient

- **WF-943**: Agent Audit Logger
  - Log all agent decisions to dossier.audit_trail
  - Format: {"actor": "agent_id", "action": "...", "decision_logic": "..."}
  - Ensure immutability (no editing after log)

### 4.6 Validation Gate (PROD-04)

**Test 1: Chat Hub Request**
```
User: "Create a 10-minute YouTube video about renewable energy"

Expected:
1. Chat Hub receives message
2. Routes to WF-932 (Workflow Agent)
3. Agent creates dossier-xxx
4. Agent orchestrates:
   - WF-100 (topic research) → 45 sec
   - WF-200 (script generation) → 60 sec
   - WF-610 (voice) → 15 sec
   - WF-650 (avatar) → 2 min
   - WF-640 (video composition) → 1 min
5. Agent returns: "Ready for approval"
6. Chat Hub shows: [APPROVE] [REQUEST CHANGES] [REJECT]
7. Audit trail: All agent actions logged

Total time: ~5 minutes
Cost: ~$2.15 (voice + avatar)
```

**Test 2: Cost Gate Enforcement (Agent)**
```
Agent attempts: Execute WF-650 (avatar, $2.00)
User budget remaining: $1.00

Expected:
- WF-942 (Cost Gate) returns error
- Agent escalates to Founder: "Budget insufficient, approve?"
- Founder approves (increases budget)
- Agent re-attempts, succeeds
- Audit trail: "Agent escalated, Founder approved overage"
```

**Test 3: Audit Trail Completeness**
```
Read: dossier-xxx/audit_trail.json

Expected entries:
- "actor": "workflow_agent_001"
- "action": "dossier_created_by_agent"
- "action": "wf_100_triggered"
- "action": "wf_200_triggered"
- "action": "wf_610_triggered"
- ... (all steps logged)
- No missing entries
- All timestamps in order
```

**Test 4: Verify Routing Law**
```
Grep agent code for direct provider calls:

Expected:
- Zero "elevenlabs" API calls directly
- Zero "heygen" API calls directly
- All calls via: Agent → Operator API → n8n → Provider

If violations found:
- Fail test
- Fix agent code
- Re-test
```

### 4.7 Success Criteria (PROD-04)

✅ Chat Hub accepts natural language task descriptions  
✅ Workflow Agent orchestrates multi-stage workflows  
✅ Agent cost gates enforced (never overage without approval)  
✅ All agent actions logged to audit trail  
✅ Agent respects Routing Law (never direct provider calls)  
✅ Founder can review/approve/reject agent outputs  
✅ Agent retries work correctly on failure  
✅ All PROD-01/02/03 features still working  
✅ Zero credential leaks in agent code or logs  
✅ Founder sign-off: "PROD-04 agents ready for production"  

---

## PHASE PROD-05: MULTI-CHANNEL PUBLISHING + SCHEDULER (Weeks 28-40, ~12 weeks)

### 5.1 Phase Goal

Enable automated publishing to multiple channels (YouTube, Instagram, TikTok, LinkedIn, Blog, Newsletter, Podcast).

**Key Benefit**: Single dossier → 10 channel versions auto-generated → Scheduled publishing → Analytics aggregation.

### 5.2 What Becomes Live (PROD-05)

✅ **Channel Calendar** (Screen 7):
- Visual calendar showing which content publishes when
- Drag-drop dossiers to calendar dates
- Auto-format conversion (YouTube long-form → Shorts, Reels, TikTok, Blog, Podcast, Newsletter)

✅ **Multi-Channel Format Conversion**:
- YouTube Long-Form (15 min) → 1,850-word script
- YouTube Shorts (60 sec) → 150-word key point
- Instagram Reel (60 sec) → 100-word hook + trendy
- TikTok (60 sec) → 60-word snappy
- LinkedIn (article) → 800-word professional
- Blog (article) → 1,850-word SEO-optimized
- Podcast (audio) → 10-15 min monologue
- Newsletter (email) → 300-word summary + CTA
- X/Twitter (thread) → 8 tweets with images

✅ **Automated Scheduler**:
- Daily topic hunt (discover trending topics)
- Weekly content calendar (plan 5 dossiers)
- Recurring channel publish (Mon/Wed/Fri @ 9 AM YouTube, etc.)
- Analytics sync (pull metrics from all platforms)

✅ **Publishing Automation**:
- YouTube: API upload + schedule publish
- Instagram: Manual or API upload
- TikTok: Manual upload (limited API)
- LinkedIn: API post articles
- Blog: API post to WordPress/Medium
- Newsletter: Email API (Mailchimp, Substack)
- Podcast: Podcast hosting API

### 5.3 Prerequisites for PROD-05

✅ **Required**:
- PROD-01, 02, 03, 04 fully functional
- YouTube OAuth credentials
- Instagram credentials (optional)
- LinkedIn credentials (optional)
- WordPress/Medium API (for blog)
- Email service API (Mailchimp, Substack)
- Podcast hosting service API

### 5.4 Files to Create/Modify (PROD-05)

**Operator API** (engine/operator.js):
- Add: `POST /operator/channel/publish` (publish to single channel)
- Add: `GET /operator/channels/analytics` (aggregate analytics)
- Add: `POST /operator/scheduler/add` (add automation rule)

**n8n Workflows** (workflows/n8n/):
- Modify: WF-660_YouTube_Publishing.json (enhance)
- Create: WF-661_Instagram_Publishing.json
- Create: WF-662_TikTok_Publishing.json
- Create: WF-663_LinkedIn_Publishing.json
- Create: WF-664_Blog_Publishing.json
- Create: WF-665_Newsletter_Publishing.json
- Create: WF-666_Podcast_Publishing.json
- Create: WF-667_Twitter_Publishing.json
- Create: WF-901_Channel_Analytics_Aggregator.json
- Create: WF-902_Scheduler_Topic_Hunt.json
- Create: WF-903_Scheduler_Calendar_Planning.json
- Create: WF-920_Analytics_Aggregator.json

**Registries** (registries/):
- Create: channel_registry.yaml (list all channels + metadata)
- Create: format_conversion_rules.yaml (YouTube → Instagram rules, etc.)
- Create: publishing_schedule.yaml (recurring publish times)

**Documentation** (docs/):
- PROD-06_FUTURE_GUI_MULTI_CHANNEL_SCHEDULER_ROADMAP.md (✅ Already created)

### 5.5 Validation Gate (PROD-05)

**Test 1: Multi-Channel Format Conversion**
```
Input: Dossier-001 (YouTube script, 1,850 words)

Expected Output:
- YouTube Long-Form: Full 1,850-word script
- YouTube Shorts: 150-word version
- Instagram Reel: 100-word version (emoji-heavy)
- TikTok: 60-word version (trendy slang)
- LinkedIn: 800-word professional version
- Blog: 1,850-word + SEO metadata
- Podcast: 10-min monologue version
- Newsletter: 300-word summary
- X/Twitter: 8-tweet thread

All variants maintain core message, adapted for platform tone/format
```

**Test 2: Scheduled Publishing**
```
# Publish dossier to multiple channels on schedule

POST /operator/channel/publish
{
  "dossier_id": "DOSSIER-001",
  "channels": {
    "youtube": {"publish_at": "2026-05-05T09:00:00Z", "format": "long-form"},
    "instagram": {"publish_at": "2026-05-05T19:00:00Z", "format": "reel"},
    "linkedin": {"publish_at": "2026-05-06T09:00:00Z", "format": "article"},
    "blog": {"publish_at": "2026-05-05T10:00:00Z", "format": "article"}
  }
}

Expected:
- All 4 formats auto-converted
- Scheduled for correct times
- At publish time: Auto-upload to each platform
- Analytics collected post-publishing
- Audit trail: All publishing actions logged
```

**Test 3: Scheduler Automation**
```
# Enable daily topic hunt scheduler

POST /operator/scheduler/add
{
  "mode": "daily_topic_hunt",
  "frequency": "0 8 * * *",  # 8 AM daily
  "auto_execute": ["WF-100"],
  "create_dossiers": 3
}

Expected:
- Every day @ 8 AM: 3 new dossiers created
- WF-100 (topic research) auto-runs
- Creator notified: "3 new dossiers ready for approval"
```

### 5.6 Success Criteria (PROD-05)

✅ Single dossier auto-converts to 10 channel-specific formats  
✅ Multi-channel calendar UI functional  
✅ Scheduled publishing to YouTube, Instagram, LinkedIn, Blog, Podcast  
✅ Analytics aggregation from all platforms  
✅ Scheduler automation (daily hunt, weekly plan, recurring publishes)  
✅ Cost tracking per channel (YouTube free, Instagram free, etc.)  
✅ All PROD-01/02/03/04 features still working  
✅ Founder sign-off: "PROD-05 multi-channel ready"  

---

## PHASE PROD-06: CUSTOM GUI + SCHEDULER CONSOLE (Weeks 40-52, ~12 weeks)

### 6.1 Phase Goal

Replace Open WebUI + curl with custom 17-screen GUI dashboard for full visual control.

**Key Benefit**: Non-technical creators can now use Shadow Creator without CLI/API knowledge.

### 6.2 What Becomes Live (PROD-06)

✅ **17 GUI Screens**:
1. Dashboard (overview)
2. Task Builder (create content)
3. Mode Launcher (operating modes)
4. Dossier Browser (list all projects)
5. Packet Viewer (inspect generated packets)
6. Output Viewer (preview media)
7. Channel Calendar (publishing schedule)
8. Approval Screen (founder reviews)
9. Remodify Screen (request changes)
10. Replay Control (retry failed stages)
11. Workflow Progress Tree (DAG visualization)
12. Alert Center (error monitoring)
13. Provider Bridge Monitor (API call tracking)
14. Cost/Budget Monitor (spending control)
15. Weekly Briefing View (analytics summary)
16. Scheduler Console (automation rules)
17. Analytics Dashboard (multi-channel metrics)

✅ **Tech Stack**:
- Frontend: React.js + Tailwind CSS
- Backend: Node.js/Express (Operator API, already exists)
- Database: SQLite (PROD-06), PostgreSQL (PROD-07)
- Real-time updates: WebSocket or polling

### 6.3 Prerequisites for PROD-06

✅ **Required**:
- PROD-01, 02, 03, 04, 05 fully functional
- Operator API stable (no breaking changes)
- React.js development environment

### 6.4 Files to Create (PROD-06)

**Frontend** (ui/src/):
```
ui/src/screens/
  ├─ Dashboard.jsx
  ├─ TaskBuilder.jsx
  ├─ ModeLauncher.jsx
  ├─ DossierBrowser.jsx
  ├─ PacketViewer.jsx
  ├─ OutputViewer.jsx
  ├─ ChannelCalendar.jsx
  ├─ ApprovalScreen.jsx
  ├─ RemodifyScreen.jsx
  ├─ ReplayControl.jsx
  ├─ WorkflowProgressTree.jsx
  ├─ AlertCenter.jsx
  ├─ ProviderBridgeMonitor.jsx
  ├─ CostBudgetMonitor.jsx
  ├─ WeeklyBriefing.jsx
  ├─ SchedulerConsole.jsx
  └─ AnalyticsDashboard.jsx

ui/src/components/
  ├─ Sidebar.jsx
  ├─ TopBar.jsx
  ├─ StatCard.jsx
  ├─ DataTable.jsx
  ├─ AlertPanel.jsx
  └─ ...

ui/src/hooks/
  ├─ useAppStore.js
  ├─ useDossierData.js
  ├─ useOperatorAPI.js
  └─ ...

ui/public/
  └─ index.html (SPA entry point)
```

**Backend Enhancement** (engine/):
- Modify: operator.js (ensure all API endpoints support real-time updates)
- Add: WebSocket support (for live dossier monitoring)
- Add: Rate limiting (prevent GUI from spamming API)

### 6.5 Validation Gate (PROD-06)

**Test 1: All 17 Screens Load**
```
Access: http://localhost:3000/gui

Expected:
- Dashboard loads (shows real-time metrics)
- Click "Create" → Task Builder screen
- Click "Manage" → Dossier Browser screen
- ... (test all 17 screens navigate correctly)
- All screens show real data (no stubs)
```

**Test 2: Create Content via GUI**
```
1. Open Task Builder
2. Fill form: Topic="AI trends", Platform="YouTube long-form"
3. Click "Create Task"

Expected:
- POST /operator/new-content-job sent
- Dossier created
- Redirect to Dashboard
- Real-time progress updates as WF runs
```

**Test 3: Approval Workflow via GUI**
```
1. Click "Approvals" → shows 2 pending
2. Click dossier-001
3. View content (script, voice preview, images)
4. Click "APPROVE"

Expected:
- POST /operator/approve/dossier-001 sent
- Status changes to APPROVED_BY_FOUNDER
- Audit trail logged
- Dossier moves to "Ready for Publishing"
```

### 6.6 Success Criteria (PROD-06)

✅ All 17 GUI screens functional  
✅ Real-time data updates (5-sec refresh)  
✅ Non-technical creator can use GUI without CLI  
✅ All PROD-01/02/03/04/05 features accessible via GUI  
✅ Mobile-responsive design (works on tablet)  
✅ Zero "Open WebUI needed" — everything in custom GUI  
✅ Founder sign-off: "PROD-06 GUI complete"  

---

## PHASE PROD-07: SCALING & STORAGE (Weeks 52-78, ~26 weeks)

### 7.1 Phase Goal

Scale system for multi-user, production reliability, enterprise features.

**Key Improvements**:
- PostgreSQL (from SQLite)
- Redis queue (async job processing)
- Qdrant vector DB (semantic search)
- Multi-user authentication
- Automated backups
- High availability
- Advanced analytics

### 7.2 What Becomes Live (PROD-07)

✅ **Database Upgrade**:
- PostgreSQL: Replaces SQLite (multi-user, concurrent access)
- Redis: Job queue for async workflows (n8n execution)
- Qdrant: Vector embeddings (semantic search of old dossiers)

✅ **Multi-User Features**:
- User authentication (username/password or OAuth)
- Role-based access control (Founder, Creator, Operator, Builder)
- Shared team workspaces
- User-specific budgets
- Per-user API keys

✅ **Reliability**:
- Automated backups (daily, weekly, monthly)
- Backup verification (restore test monthly)
- Disaster recovery playbook
- 99.9% uptime SLA
- Health monitoring + alerts

✅ **Analytics** (Advanced):
- Long-term trend analysis
- ROI calculations (cost per view/engagement)
- Machine learning recommendations
- Cohort analysis (which content types best for which creators?)

### 7.3 Prerequisites for PROD-07

✅ **Required**:
- PROD-01 through 06 fully functional
- PostgreSQL database (managed or self-hosted)
- Redis instance
- Qdrant instance (can be single-node)
- AWS/GCP/Azure account (for backups, CDN)

### 7.4 Files to Create/Modify (PROD-07)

**Database** (db/):
```
db/migrations/
  ├─ 001_sqlite_to_postgres.sql
  ├─ 002_add_user_table.sql
  ├─ 003_add_role_based_access.sql
  ├─ 004_add_backup_tracking.sql
  └─ ...

db/schema/
  ├─ users.sql
  ├─ dossiers.sql (modified)
  ├─ packets.sql (modified)
  ├─ audit_trail.sql (modified)
  ├─ backup_inventory.sql
  └─ ...
```

**Backend** (engine/):
- Modify: operator.js (add user auth, role checks)
- Add: auth/middleware.js (JWT validation)
- Add: db/connection.js (PostgreSQL pool)
- Add: queue/producer.js (Redis job queue)
- Add: backup/scheduler.js (automated backups)
- Add: analytics/engine.js (advanced analytics)

**Documentation** (docs/):
- PROD-07_SCALING_ARCHITECTURE_AND_OPERATIONS.md (new, ~3,000 lines)

### 7.5 Migration Plan (SQLite → PostgreSQL)

```powershell
# Phase 1: Setup (1 week)
- Provision PostgreSQL (AWS RDS or Heroku)
- Run schema migration scripts
- Load SQLite data into Postgres
- Verify data integrity

# Phase 2: Testing (1 week)
- Run all tests against Postgres
- Performance testing (load testing)
- Backup/restore testing

# Phase 3: Switchover (Downtime: ~1 hour)
- Stop n8n and Operator API
- Final SQLite → Postgres sync
- Update connection strings
- Restart services
- Verify health check passes

# Phase 4: Monitoring (1 week)
- Monitor error logs
- Watch query performance
- User feedback collection
```

### 7.6 Validation Gate (PROD-07)

**Test 1: Multi-User Isolation**
```
User A: Create dossier-A (budget $50)
User B: Create dossier-B (budget $50)

Expected:
- User A cannot see dossier-B
- User B cannot see dossier-A
- Budgets tracked separately
- Cost for dossier-A only charges User A
```

**Test 2: Automated Backups**
```
# Configure backup schedule
POST /operator/backup/schedule
{
  "frequency": "daily",
  "time": "02:00 UTC",
  "retention_days": 30
}

Expected:
- Every day @ 2 AM: Full backup to S3
- Backup contains: All dossiers, packets, audit trail, user data
- Verification: Restore test monthly
- Restore time target: <30 min
```

**Test 3: Redis Queue**
```
# Submit 10 dossiers simultaneously
POST /operator/batch/create
{
  "count": 10,
  "topic_pattern": "AI topic {1..10}"
}

Expected:
- All 10 jobs queued to Redis
- n8n processes queue sequentially (or in parallel by config)
- No job lost
- No API timeout (async processing)
- All complete within SLA
```

### 7.7 Success Criteria (PROD-07)

✅ PostgreSQL operational (no more SQLite)  
✅ Multi-user support (separate budgets, isolation)  
✅ Automated daily backups with verification  
✅ Redis queue for async job processing  
✅ Qdrant for semantic search of past content  
✅ 99.9% uptime demonstrated (30-day history)  
✅ Advanced analytics (ROI, trend analysis)  
✅ Team workspace support  
✅ All PROD-01-06 features still working  
✅ Founder sign-off: "PROD-07 enterprise-ready"  

---

## IMPLEMENTATION ROADMAP SUMMARY

| Phase | Goal | Effort | Timeline | Dependencies | Key Milestones |
|-------|------|--------|----------|---|---|
| **PROD-01** ✅ | Local LLM foundation | 4 weeks | Weeks 0-4 | None (greenfield) | Health check passes |
| **PROD-02** | Cloud LLM speed layer | 6 weeks | Weeks 4-10 | PROD-01 done | Script gen < 10 sec with GPT-4 |
| **PROD-03** | Provider bridge execution | 10 weeks | Weeks 10-20 | PROD-02 done | Full multimedia dossier works |
| **PROD-04** | n8n agents + Chat Hub | 8 weeks | Weeks 20-28 | PROD-03 done | Chat Hub accepts natural language |
| **PROD-05** | Multi-channel publishing | 12 weeks | Weeks 28-40 | PROD-04 done | Publish to 8+ channels simultaneously |
| **PROD-06** | Custom GUI + scheduler | 12 weeks | Weeks 40-52 | PROD-05 done | 17 screens functional, non-tech creator ready |
| **PROD-07** | Scaling + storage | 26 weeks | Weeks 52-78 | PROD-06 done | Multi-user, Postgres, 99.9% SLA |
| **TOTAL** | | 78 weeks | ~18 months | | Enterprise-grade platform |

---

## CRITICAL DECISION POINTS (Founder Authority Required)

### Go/No-Go Gates

1. **After PROD-01 (Week 4)**: "Should we proceed to PROD-02 cloud models?"
   - Go-to criteria: Health check passes, dossier system proven, no critical bugs
   - No-go criteria: Systematic crashes, audit trail gaps, cost tracking errors

2. **After PROD-02 (Week 10)**: "Should we enable real media generation (PROD-03)?"
   - Go-to criteria: Cloud LLMs working, cost gates proven effective
   - No-go criteria: API instability, cost overages, high error rates

3. **After PROD-03 (Week 20)**: "Should we release n8n agents (PROD-04)?"
   - Go-to criteria: All media providers working, full dossier end-to-end tested
   - No-go criteria: Provider integration brittle, audit trail incomplete

4. **After PROD-04 (Week 28)**: "Should we launch multi-channel publishing (PROD-05)?"
   - Go-to criteria: Agents autonomous and safe, cost governance proven
   - No-go criteria: Agent bypassing approval gates, cost tracking unreliable

5. **After PROD-05 (Week 40)**: "Should we replace Open WebUI with custom GUI (PROD-06)?"
   - Go-to criteria: Multi-channel publishing working, scheduler reliable
   - No-go criteria: Analytics incomplete, publishing failures, user confusion

6. **After PROD-06 (Week 52)**: "Should we scale to PostgreSQL + multi-user (PROD-07)?"
   - Go-to criteria: GUI complete, scheduler proven over 4 weeks
   - No-go criteria: GUI instability, scheduler missing automation modes

---

**Status**: 📋 DESIGN_ONLY — PROD-02+ not yet started  
**Target Release**: PROD-06 by Q4 2026, PROD-07 by Q2 2027  
**Founder Authority**: Required for all go/no-go decisions  

---

