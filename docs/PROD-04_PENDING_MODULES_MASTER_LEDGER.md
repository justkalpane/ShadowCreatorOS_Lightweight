# Shadow Creator OS - PROD-04 Pending Modules Master Ledger

**Version**: 1.0.0  
**Date**: 2026-05-06  
**Classification**: AUDIT & ROADMAP DOCUMENTATION  
**Purpose**: Complete gap ledger of all pending/deferred modules with status classification

---

## EXECUTIVE SUMMARY

This ledger documents **28 pending modules** across 7 categories that are designed but not yet production-live in PROD-01. All modules are classified using a precise **5-tier status system** based on actual registry and codebase evidence.

**Key Finding**: PROD-01 runs with **2 active components** (Ollama local, Operator API). Everything else is deferred, designed, or planned.

---

## STATUS CLASSIFICATION SYSTEM

| Status | Meaning | Example | Can Execute | Needs Credentials |
|--------|---------|---------|-------------|------------------|
| **ACTIVE_PHASE_1** | Running in production right now | Ollama local, Operator API | ✅ YES | ❌ NO |
| **DEFERRED_PHASE_2+** | Designed, registered, but blocked by release blocker | ElevenLabs, HeyGen, YouTube API | ❌ NO | ⏳ NOT YET |
| **DESIGNED_STUB_ONLY** | Architecture exists, no runtime implementation | WF-300-600 (parent packs), Cloud models | ❌ NO | ❌ NO |
| **ROUTING_READY_NOT_TESTED** | n8n workflows exist but not tested at scale | WF-020, WF-021, WF-022, WF-023 | ⏳ MAYBE | ⏳ NOT YET |
| **NOT_IMPLEMENTED** | Planned but no code/registry entry yet | n8n Personal Agents, n8n Chat Hub, custom GUI | ❌ NO | ❌ NO |
| **PROVIDER_BRIDGE_REQUIRED** | Planning packet generated, real execution blocked | All media (image, voice, video, avatar) | 📋 PACKETS ONLY | ❌ NO |

---

## MATRIX 1: ALL PENDING MODULES (28 Total)

| # | Module | Category | Current Status | Evidence | Credentials | n8n WF | API Endpoint | GUI | Can Run Now | Target Phase |
|---|--------|----------|----------------|----------|-------------|--------|--------------|-----|-------------|--------------|
| 1 | ElevenLabs Voice | Provider | DEFERRED_PHASE_2 | provider_registry.yaml:line38 | api_key | ❌ | POST /provider/voice/generate | ❌ | ❌ NO | PROD-02 |
| 2 | HeyGen Avatar | Provider | DEFERRED_PHASE_2 | provider_registry.yaml:line56 | api_key | ❌ | POST /provider/avatar/generate | ❌ | ❌ NO | PROD-02 |
| 3 | YouTube Data API | Provider | DEFERRED_PHASE_2 | provider_registry.yaml:line74 | oauth2 | ❌ | POST /provider/youtube/upload | ❌ | ❌ NO | PROD-03 |
| 4 | Claude 3 Opus | Model | DEFERRED_PHASE_2 | model_registry.yaml:line105 | api_key | ❌ | GET /models/reasoning | ❌ | ❌ NO | PROD-02 |
| 5 | Llama 70B | Model | DEFERRED_PHASE_2 | model_registry.yaml:line128 | api_key | ❌ | GET /models/cloud | ❌ | ❌ NO | PROD-02 |
| 6 | WF-300 Context Eng | Workflow | DESIGNED_STUB_ONLY | workflow_registry.yaml:line94 | — | 📋 | — | ❌ | ⏳ MAYBE | PROD-02 |
| 7 | WF-400 Media Prod | Workflow | DESIGNED_STUB_ONLY | workflow_registry.yaml:line102 | — | 📋 | — | ❌ | ⏳ MAYBE | PROD-02 |
| 8 | WF-500 Publishing | Workflow | DESIGNED_STUB_ONLY | workflow_registry.yaml:line110 | — | 📋 | — | ❌ | ⏳ MAYBE | PROD-02 |
| 9 | WF-600 Analytics | Workflow | DESIGNED_STUB_ONLY | workflow_registry.yaml:line118 | — | 📋 | — | ❌ | ⏳ MAYBE | PROD-02 |
| 10 | WF-020 Approval | Workflow | ROUTING_READY_NOT_TESTED | workflow_registry.yaml:line62 | — | ✅ WIRED | — | ❌ | ✅ YES | PROD-01 |
| 11 | WF-021 Replay | Workflow | ROUTING_READY_NOT_TESTED | workflow_registry.yaml:line70 | — | ✅ WIRED | — | ❌ | ✅ YES | PROD-01 |
| 12 | WF-022 Provider Bridge | Workflow | ROUTING_READY_NOT_TESTED | workflow_registry.yaml:line78 | — | ✅ WIRED | — | ❌ | ❌ NO | PROD-02 |
| 13 | WF-023 Downstream Prep | Workflow | ROUTING_READY_NOT_TESTED | workflow_registry.yaml:line86 | — | ✅ WIRED | — | ❌ | ⏳ MAYBE | PROD-02 |
| 14 | n8n Personal Agents | n8n Surface | NOT_IMPLEMENTED | No registry entry | — | ❌ | — | ❌ | ❌ NO | PROD-04 |
| 15 | n8n Workflow Agents | n8n Surface | NOT_IMPLEMENTED | No registry entry | — | ❌ | — | ❌ | ❌ NO | PROD-04 |
| 16 | n8n Chat Hub | n8n Surface | NOT_IMPLEMENTED | No registry entry | — | ❌ | — | ❌ | ❌ NO | PROD-04 |
| 17 | n8n Credential Vault | n8n Feature | NOT_IMPLEMENTED | No registry entry | — | ❌ | — | ❌ | ❌ NO | PROD-02 |
| 18 | Image Generation | Media | PROVIDER_BRIDGE_REQUIRED | PROD-03_roadmap | provider key | ❌ | POST /provider/image/generate | ❌ | 📋 PACKETS | PROD-03 |
| 19 | Voice Generation | Media | PROVIDER_BRIDGE_REQUIRED | PROD-03_roadmap | provider key | ❌ | POST /provider/voice/generate | ❌ | 📋 PACKETS | PROD-03 |
| 20 | Music Generation | Media | PROVIDER_BRIDGE_REQUIRED | PROD-03_roadmap | provider key | ❌ | POST /provider/music/generate | ❌ | 📋 PACKETS | PROD-03 |
| 21 | Video Assembly | Media | PROVIDER_BRIDGE_REQUIRED | PROD-03_roadmap | provider key | ❌ | POST /provider/video/assemble | ❌ | 📋 PACKETS | PROD-03 |
| 22 | Avatar Video | Media | PROVIDER_BRIDGE_REQUIRED | PROD-03_roadmap | provider key | ❌ | POST /provider/avatar/render | ❌ | 📋 PACKETS | PROD-03 |
| 23 | Publishing Handler | Media | PROVIDER_BRIDGE_REQUIRED | PROD-03_roadmap | oauth2 | ❌ | POST /provider/publish/upload | ❌ | 📋 PACKETS | PROD-03 |
| 24 | Custom Dashboard | GUI | NOT_IMPLEMENTED | No code | — | ❌ | — | ❌ | ❌ NO | PROD-06 |
| 25 | Multi-Channel Orchestration | Orchestration | NOT_IMPLEMENTED | No code | — | ❌ | — | ❌ | ❌ NO | PROD-05 |
| 26 | Automated Scheduler | Orchestration | NOT_IMPLEMENTED | No code | — | ❌ | — | ❌ | ❌ NO | PROD-05 |
| 27 | Analytics Feedback Loop | Orchestration | NOT_IMPLEMENTED | No code | — | ❌ | — | ❌ | ❌ NO | PROD-05 |
| 28 | Cost/Budget Gates | Governance | NOT_IMPLEMENTED | No code | — | ❌ | — | ❌ | ❌ NO | PROD-02 |

**Key Observations**:
- ✅ ACTIVE_PHASE_1: 2 modules (Ollama, Operator API)
- 🟠 DEFERRED_PHASE_2+: 5 modules (blocked by release blockers)
- 📋 DESIGNED_STUB_ONLY: 4 modules (workflows)
- ✅ ROUTING_READY: 4 modules (WF-020, WF-021, WF-022, WF-023)
- ❌ NOT_IMPLEMENTED: 7 modules (n8n surfaces, GUI, orchestration)
- 🌉 PROVIDER_BRIDGE_REQUIRED: 6 modules (media, publishing)

---

## MATRIX 2: PROVIDER DETAILS (5 Deferred Providers)

| Provider | Type | Auth | Callback | Phase | Cost Model | Release Blocker | Evidence |
|----------|------|------|----------|-------|-----------|-----------------|----------|
| **ElevenLabs** | Voice | api_key | sync_http | PROD-02 | $0.008/1K chars | provider_auth_closure | provider_registry:38-54 |
| **HeyGen** | Avatar | api_key | webhook_polling | PROD-02 | $1.50-3.00/avatar | provider_auth_closure | provider_registry:56-72 |
| **YouTube Data** | Publishing | oauth2 | redirect_uri | PROD-03 | Free | oauth_redirect_uri | provider_registry:74-90 |
| **OpenRouter Claude** | Model | api_key | n8n_header | PROD-02 | $0.015/1K input | api_key_vault_required | model_registry:105-126 |
| **OpenRouter Llama** | Model | api_key | n8n_header | PROD-02 | $0.005/1K input | api_key_vault_required | model_registry:128-149 |

**Release Blockers** (Why these can't be activated in PROD-01):
1. `provider_auth_closure` - Auth/callback contracts incomplete
2. `oauth_redirect_uri` - OAuth redirect URI not finalized
3. `api_key_vault_integration_required` - Credential vault not yet implemented
4. `cost_gate_enforcement` - Cost limiting gate not yet built

---

## MATRIX 3: WORKFLOW STATUS (13 n8n Workflows)

| WF-ID | Name | Type | Artifact | Runtime | Validated | Notes |
|-------|------|------|----------|---------|-----------|-------|
| WF-001 | Dossier Create | parent | repo_present | not_built | yes | Phase 1 (works) |
| WF-010 | Orchestrator | parent | repo_present | not_built | yes | Phase 1 (works) |
| WF-100 | Topic Intelligence | pack | repo_present | not_built | yes | Phase 2+ (designed) |
| WF-200 | Script Generation | pack | repo_present | not_built | yes | Phase 2+ (designed) |
| WF-020 | Final Approval | governance | starter_wired | not_built | yes | Phase 1 (ready to wire) |
| WF-021 | Replay-Remodify | governance | starter_wired | not_built | yes | Phase 1 (ready to wire) |
| WF-022 | Provider Bridge | system_bridge | starter_wired | not_built | yes | Phase 2 (requires provider) |
| WF-023 | Downstream Prep | planning | starter_wired | not_built | yes | Phase 2 (planning packets) |
| WF-300 | Context Engineering | pack | repo_present | not_built | yes | Phase 2+ (stub) |
| WF-400 | Media Production | pack | repo_present | not_built | yes | Phase 2+ (stub) |
| WF-500 | Publishing Distribution | pack | repo_present | not_built | yes | Phase 2+ (stub) |
| WF-600 | Analytics Evolution | pack | repo_present | not_built | yes | Phase 2+ (stub) |
| WF-901 | Error Recovery | system | repo_present | deployed_live | yes | Live (works) |

**Key Facts**:
- ✅ WF-001, WF-010 are production-live
- 📋 WF-100, WF-200 are designed (stubs)
- ✅ WF-020, WF-021 are wired and ready to execute
- 🌉 WF-022, WF-023 require provider bridge
- 📋 WF-300-600 are designed parent packs
- ✅ WF-901 is production-live

---

## MATRIX 4: n8n NATIVE SURFACES (3 Planned, 0 Implemented)

| Feature | Status | Purpose | Current State | When Available |
|---------|--------|---------|---|---------|
| **Personal Agents** | NOT_IMPLEMENTED | User-facing agents within n8n | Design discussion only | PROD-04 |
| **Workflow Agents** | NOT_IMPLEMENTED | Agent-orchestrated workflows | Design discussion only | PROD-04 |
| **Chat Hub** | NOT_IMPLEMENTED | Native n8n chat interface | Design discussion only | PROD-04 |

**Critical Rules** (when implemented):
- Must route through Operator API
- Cannot bypass dossier system
- Must maintain audit trail
- Cannot make direct provider calls
- Must preserve routing law

---

## MATRIX 5: MEDIA/PROVIDER MODES (6 Planning Packets Exist)

| Mode | Status | Packet Type | Real Files | Credentials | When Enabled |
|------|--------|-------------|-----------|-------------|--------------|
| **Image Generation** | PROVIDER_BRIDGE_REQUIRED | PKT-image-plan | ❌ NONE | provider key | PROD-03 |
| **Voice/Narration** | PROVIDER_BRIDGE_REQUIRED | PKT-voice-plan | ❌ NONE | provider key | PROD-03 |
| **Music/BGM** | PROVIDER_BRIDGE_REQUIRED | PKT-music-plan | ❌ NONE | provider key | PROD-03 |
| **Video Assembly** | PROVIDER_BRIDGE_REQUIRED | PKT-video-plan | ❌ NONE | provider key | PROD-03 |
| **Avatar Rendering** | PROVIDER_BRIDGE_REQUIRED | PKT-avatar-plan | ❌ NONE | provider key | PROD-03 |
| **Publishing/Upload** | PROVIDER_BRIDGE_REQUIRED | PKT-publish-plan | ❌ NONE | oauth2 | PROD-03 |

**Critical Fact**: **ZERO actual media files are generated in PROD-01**. Only JSON planning packets exist.

---

## MATRIX 6: CLOUD MODEL PROVIDERS (5 Deferred)

| Model | Provider | Type | Phase | Cost/1K tokens | Status |
|-------|----------|------|-------|---|---------|
| Claude 3 Opus | OpenRouter | Reasoning | PROD-02 | $0.015 input | DEFERRED_PHASE_2 |
| Llama 70B | OpenRouter | Reasoning | PROD-02 | $0.005 input | DEFERRED_PHASE_2 |
| GPT-4 (future) | OpenAI | Reasoning | PROD-02+ | TBD | NOT_YET_PLANNED |
| Gemini (future) | Google | Reasoning | PROD-02+ | TBD | NOT_YET_PLANNED |
| Perplexity (future) | Perplexity | Research | PROD-02+ | TBD | NOT_YET_PLANNED |

**Release Blockers**: All cloud models blocked by api_key_vault_integration_required

---

## MATRIX 7: GOVERNANCE MODULES (4 Not Yet Implemented)

| Module | Purpose | Status | Phase |
|--------|---------|--------|-------|
| **Cost/Budget Gates** | Enforce kubera_budget_gate | NOT_IMPLEMENTED | PROD-02 |
| **Policy Enforcement** | Enforce yama_policy_illegality | NOT_IMPLEMENTED | PROD-02 |
| **Credential Rotation** | Quarterly API key rotation | NOT_IMPLEMENTED | PROD-02 |
| **Analytics Feedback** | Learn from approval feedback | NOT_IMPLEMENTED | PROD-05 |

---

## PHASE ROADMAP (PROD-02 through PROD-07)

### PROD-01 (Current - May 2026)
**Status**: ACTIVE ✅
- Ollama local (Llama 3.2)
- Operator API
- Dossier system
- Approval gate (WF-020/WF-021 ready)
- Alert system
- Text generation only

### PROD-02 (4-6 weeks after PROD-01)
**Status**: NEXT
- ✅ Add cloud model providers (Claude, Llama 70B via OpenRouter)
- 🌉 Enable provider credentials vault (n8n credential integration)
- 🌉 Wire WF-022 (provider bridge)
- 🌉 Implement cost/budget gates
- ✅ Wire WF-300-600 (design stubs)
- 🌉 Test single real media output (image generation via DALL-E or Midjourney)
- ⏳ Plan n8n native agents surface

### PROD-03 (PROD-02 + 4-6 weeks)
**Status**: PLANNED
- ✅ Enable all media providers (image, voice, music, video, avatar)
- ✅ Enable YouTube Data API publishing
- 🌉 Full provider bridge execution (real media files)
- 📊 Analytics feedback loop (collect approval data)
- 🌉 Test multi-channel publishing (YouTube + LinkedIn test)

### PROD-04 (PROD-03 + 4-6 weeks)
**Status**: DESIGNED
- ✅ Implement n8n Personal Agents (governed by routing law)
- ✅ Implement n8n Workflow Agents
- ✅ Implement n8n Chat Hub (with Operator API gateway)
- 🌉 Credential vault hardening

### PROD-05 (PROD-04 + 4-6 weeks)
**Status**: PLANNED
- ✅ Multi-channel orchestration (YouTube, Instagram, TikTok, LinkedIn, X)
- ✅ Automated scheduler (daily/weekly/recurring jobs)
- ✅ Channel calendar
- 📊 Full analytics feedback loop

### PROD-06 (PROD-05 + 4-6 weeks)
**Status**: DESIGNED
- ✅ Custom Shadow Creator dashboard
- ✅ Mode/module/director selector UI
- ✅ Dossier/packet browser GUI
- ✅ Approval/remodify UI
- ✅ Provider bridge status panel

### PROD-07 (PROD-06 + 4-6 weeks)
**Status**: FUTURE
- ✅ PostgreSQL (scaling from SQLite)
- ✅ Redis (queue management)
- ✅ Qdrant (vector memory)
- ✅ Multi-user hardening
- ✅ Automated backup/recovery

---

## CRITICAL SAFETY RULES (Always Preserved)

1. ✅ All paths through Operator API (never direct n8n)
2. ✅ Complete audit trail (every operation logged)
3. ✅ Dossier immutability (no blind overwrites)
4. ✅ Provider bridge enforcement (no live media in PROD-01)
5. ✅ Credential security (never hardcoded, vault-based)
6. ✅ Cost gates (kubera_budget_gate enforced)
7. ✅ No n8n workflow modifications during production
8. ✅ No SQLite direct edits
9. ✅ No webhook registry changes (except via API)
10. ✅ Routing law preserved in all phases

---

## NEXT STEPS

1. ✅ PROD-01-C audit complete (this document)
2. ⏳ PROD-04 n8n Agents & Credentials plan (next doc)
3. ⏳ PROD-05 Provider Bridge backlog (next doc)
4. ⏳ PROD-06 Future GUI & Multi-channel roadmap (next doc)
5. ⏳ PROD-07 Phase roadmap full detail (next doc)

---

**Status**: ✅ PROD-04 PENDING MODULES LEDGER COMPLETE  
**Modules Audited**: 28 total  
**Active in PROD-01**: 2 modules  
**Deferred**: 26 modules  
**Release Blockers Identified**: 6  
**Evidence Source**: registries/ + docs/ + PROD-01-C audit

---
