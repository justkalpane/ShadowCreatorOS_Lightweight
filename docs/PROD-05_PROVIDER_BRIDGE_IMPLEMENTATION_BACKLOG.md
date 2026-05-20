# PROD-05: Provider Bridge Implementation Backlog

**Document Type**: Technical Implementation Backlog  
**Phase**: PROD-03 through PROD-07 (Provider activation and scaling)  
**Status**: DESIGN_ONLY — Provider Bridge NOT active in PROD-01  
**Last Updated**: 2026-05-06  
**Audience**: Builder (implementation), Operator (integration testing), Founder (approval gates)

---

## EXECUTIVE SUMMARY

This document defines the **complete backlog for enabling real media generation** in Shadow Creator OS. Each provider is listed with:
- **Purpose**: What it does (voice synthesis, image generation, video assembly, etc.)
- **Current Status**: Where it is in PROD-01/02/03 roadmap
- **Implementation Checklist**: 12 concrete steps to activate this provider
- **Failure Modes**: What can go wrong and recovery procedures
- **Phase Target**: When this provider becomes production-ready

**Key Principle**: Providers activate sequentially, not simultaneously, to maintain audit trail integrity and cost control.

---

## PART 1: PROVIDER PRIORITY ORDER & PHASES

### 1.1 Phase Rollout Timeline

```
PROD-01 (Active Today)
  └─ Ollama Local (Llama 3.2) — ZERO-COST, PRODUCTION READY
  
PROD-02 (Cloud Models, ~6 weeks after PROD-01)
  ├─ OpenRouter (multi-model gateway) — COST_GATED
  ├─ OpenAI (GPT-4) — COST_GATED
  ├─ Gemini (Google) — COST_GATED
  ├─ Claude (Anthropic via API) — COST_GATED
  ├─ Perplexity (research LLM) — COST_GATED
  ├─ Groq (fast inference) — COST_GATED
  ├─ DeepSeek (research models) — COST_GATED
  ├─ Mistral (open models) — COST_GATED
  ├─ Kimi/K2 (Chinese LLM) — COST_GATED
  └─ Nano Banana (serverless GPU) — COST_GATED
  
PROD-03 (Media Providers, ~10 weeks after PROD-02)
  ├─ ElevenLabs (voice synthesis) — COST_GATED, APPROVAL_REQUIRED
  ├─ HeyGen (avatar video) — COST_GATED, APPROVAL_REQUIRED
  ├─ Wav2Lip (lipsync video) — COST_GATED, OPEN_SOURCE
  ├─ FFmpeg (video composition) — ZERO_COST, OPEN_SOURCE
  ├─ DALL-E 3 (image generation) — COST_GATED, APPROVAL_REQUIRED
  ├─ YouTube Data API (publishing) — OAUTH_REQUIRED, APPROVAL_REQUIRED
  └─ YouTube Analytics API (feedback loop) — OAUTH_REQUIRED, APPROVAL_REQUIRED
  
PROD-04 (n8n Agents, ~4 weeks after PROD-03)
  └─ All above providers accessible via n8n agent orchestration
  
PROD-05/06/07 (Scaling & Optimization)
  └─ Additional providers, custom integrations, cost optimization
```

### 1.2 Why Sequential Activation?

Each provider activation requires:
1. **Credential management** (store API key safely)
2. **Cost gate configuration** (set budget limits)
3. **Packet schema definition** (define output structure)
4. **Workflow integration** (add to n8n)
5. **Dry run testing** (non-production)
6. **Single real run** (production dossier)
7. **Founder approval** (release decision)

Doing this sequentially ensures no surprises and builds confidence in the system.

---

## PART 2: PROVIDER BACKLOG (Detailed)

---

### PROVIDER 1: OLLAMA_LOCAL (Llama 3.2)

**Status**: ✅ ACTIVE_PROD-01

**Purpose**: Local LLM inference (research, script generation, metadata)  
**Model**: Llama 3.2 (7B or larger)  
**Cost**: $0.00 (runs locally on user's machine)  
**Estimated Tokens/Dossier**: 1,000-2,000 tokens  
**Typical Latency**: 5-30 sec per request  

**Current Status in PROD-01**:
- ✅ Installed and running (verified: `curl http://localhost:11434/api/tags`)
- ✅ Integrated into WF-100 (topic intelligence)
- ✅ Integrated into WF-200 (script generation)
- ✅ Being used daily for test dossiers
- ✅ Audit trail shows all usage
- ✅ Cost tracking ($0.00) accurate

**Implementation Checklist** (ALREADY DONE):
- [x] 1. Install Ollama: `ollama pull llama2`
- [x] 2. Start Ollama: `ollama serve`
- [x] 3. Create n8n node: "Ollama LLM Call"
- [x] 4. Define prompts for WF-100 and WF-200
- [x] 5. Test non-production: dry run with dummy dossier
- [x] 6. Test production: real dossier via Open WebUI
- [x] 7. Configure cost tracking: $0.00
- [x] 8. Add monitoring: token count, latency
- [x] 9. Document: registries/provider_registry.yaml
- [x] 10. Test failure mode: Ollama timeout recovery
- [x] 11. Enable approval gate: No gate needed (cost = $0)
- [x] 12. Sign-off: Founder approves as ready

**Output Packet Schema**:
```yaml
packet_type: llm_output
workflow: WF-100 or WF-200
provider: ollama_local

content:
  prompt: "string (max 2000 chars)"
  response: "string (model output)"
  tokens_used: "integer"
  generation_time_ms: "integer"
  model_version: "llama3.2-7b"
  
metadata:
  provider_response_time_ms: "integer"
  confidence_score: "float 0-1"
  input_tokens: "integer"
  output_tokens: "integer"
```

**Failure Modes & Recovery**:

| Failure | Detection | Recovery |
|---------|-----------|----------|
| Ollama timeout (>30 sec) | Operator detects no response | Retry WF-100: `npm run operator:replay dossier-xyz --stage WF-100 --max-attempts 3` |
| Ollama out of memory | CUDA/GPU error in logs | Restart Ollama: `killall ollama && ollama serve` |
| Model hallucination (bad output) | Founder reviews, quality score < 0.5 | Request remodify: `POST /operator/remodify/dossier-xyz --instructions "Fix hallucination"` |
| Network disconnect | Operator API cannot reach Ollama | Check: `curl http://localhost:11434/api/tags` |

**Operational Notes**:
- Ollama must be running at all times (add to startup scripts)
- Monitor token usage for cost forecasting (useful for PROD-02+)
- Latency acceptable for this provider (5-30 sec is normal)

---

### PROVIDER 2: ELEVENLABS (Voice Synthesis)

**Status**: 🔴 DEFERRED_PROD-03 (Blocked by PROVIDER_BRIDGE_REQUIRED)

**Purpose**: Convert script to natural-sounding voice (audio files)  
**API Endpoint**: `https://api.elevenlabs.io/v1/text-to-speech/{voice_id}`  
**Cost**: $0.008 per 1,000 characters (~$0.15 per 1,500-word script)  
**Estimated Tokens**: 0 (uses character count, not tokens)  
**Typical Latency**: 5-15 sec per voice synthesis call  
**Available Voices**: 29 (alloy, breeze, cinnamon, etc.)  

**Current Status in PROD-01**:
- ❌ Credential NOT installed (no API key stored)
- ❌ n8n workflow NOT created (WF-610 is stub)
- ❌ Cost gate NOT configured
- ❌ Packet schema NOT defined
- ❌ Approval gate NOT implemented
- ❌ NO dossiers with voice outputs (PROVIDER_BRIDGE blocks execution)

**Phase Target**: PROD-03 (Week 10-12 after PROD-01)

**Implementation Checklist** (For PROD-03):

1. **Obtain API Credentials**:
   - [ ] User creates ElevenLabs account: https://elevenlabs.io
   - [ ] User generates API key from dashboard
   - [ ] Operator stores API key in n8n credential vault (encrypted)
   - [ ] Test: `curl https://api.elevenlabs.io/v1/voices -H "xi-api-key: $API_KEY"`

2. **Create n8n Credential**:
   - [ ] Create in n8n: Credentials → New → ElevenLabs API
   - [ ] Store: xi-api-key, voice_id (default: alloy), model_id (default: eleven_monolingual_v1)
   - [ ] Test: n8n credential validates against API

3. **Define Packet Schema**:
   - [ ] Create: registries/packet_schema_WF-610_voice.yaml
   - [ ] Fields: input_text, voice_id, output_file_path, duration_seconds, cost_usd
   - [ ] Validate: Schema matches ElevenLabs response format

4. **Create n8n Workflow (WF-610)**:
   - [ ] n8n node: "ElevenLabs API Call"
   - [ ] Input: script_text from pkt_200, voice_id, model_id
   - [ ] Output: audio file path, duration, cost
   - [ ] Error handling: Retry on rate limit (max 3 attempts)
   - [ ] Logging: All calls to dossier.audit_trail

5. **Configure Cost Gate**:
   - [ ] Policy: $0.20 max per dossier (safety buffer)
   - [ ] Check: user's budget_remaining >= $0.20 before WF-610 runs
   - [ ] If insufficient: Escalate to Founder for approval
   - [ ] Track: Actual cost deducted from budget_remaining

6. **Dry Run Testing**:
   - [ ] Create dossier with mode=dry_run
   - [ ] Call WF-610 with mock ElevenLabs response (no actual call)
   - [ ] Verify: audit_trail recorded, cost_tracking = $0.00, packet created
   - [ ] Verify: zero API charges to ElevenLabs

7. **Single Real Run**:
   - [ ] Create production dossier (mode=production, provider_enabled=elevenlabs)
   - [ ] Limit to 1 voice synthesis call (no looping)
   - [ ] Monitor: Cost should be ~$0.15
   - [ ] Verify: Audio file created locally at `/dossiers/dossier-xyz/audio_elevenlabs_001.mp3`
   - [ ] Verify: audit_trail shows voice synthesis, cost tracking shows $0.15
   - [ ] Listen: Audio quality acceptable (no truncation, natural voice)

8. **Dossier Writeback Verification**:
   - [ ] Read dossier.packets.pkt_610_voice
   - [ ] Confirm: input_text, voice_id, output_file_path, duration_seconds, cost_usd
   - [ ] Confirm: audit_trail entry: "elevenlabs_voice_synthesis_complete"
   - [ ] Confirm: budget_remaining decreased by $0.15

9. **Output File Validation**:
   - [ ] File path exists: `/dossiers/dossier-xyz/audio_elevenlabs_001.mp3`
   - [ ] File size > 100KB (not truncated)
   - [ ] Audio playable (no corruption)
   - [ ] Duration matches expected (±2 sec tolerance)

10. **Approval Gate Testing**:
    - [ ] Founder can approve dossier with ElevenLabs output
    - [ ] Status transitions: VOICE_SYNTHESIS_COMPLETE → READY_FOR_APPROVAL → APPROVED_BY_FOUNDER
    - [ ] Next workflow (WF-620 or WF-660) receives input correctly

11. **Failure Mode Testing**:
    - [ ] Rate limit (429): Retry mechanism activates, succeeds on retry 2
    - [ ] Invalid API key: Error caught, escalated to Founder
    - [ ] Offline: Connection timeout after 5 sec, retry offered
    - [ ] Truncated audio: Detected by validation (size check), regenerated

12. **Sign-off & Release**:
    - [ ] Builder confirms all 11 above checks passed
    - [ ] Operator confirms zero credential leaks in logs
    - [ ] Founder reviews: cost gates work, approval flow functional
    - [ ] Founder sign-off: "WF-610 ready for PROD-03"

**Output Packet Example**:
```json
{
  "pkt_610_voice": {
    "artifact_type": "voice_synthesis",
    "workflow": "WF-610",
    "provider": "elevenlabs",
    "input": {
      "script_text": "Hello, welcome to our podcast...",
      "script_word_count": 450,
      "voice_id": "alloy",
      "model_id": "eleven_monolingual_v1"
    },
    "output": {
      "audio_file_path": "/dossiers/dossier-20260515-001/audio_elevenlabs_001.mp3",
      "file_size_bytes": 240000,
      "duration_seconds": 125,
      "bit_rate_kbps": 128,
      "sample_rate_hz": 44100
    },
    "cost": {
      "characters_processed": 3456,
      "cost_per_1k_chars_usd": 0.008,
      "total_cost_usd": 0.0276,
      "currency": "USD",
      "provider": "elevenlabs"
    },
    "metadata": {
      "agent_id": "workflow_orchestrator_001",
      "credential_ref": "user-001_elevenlabs_001",
      "provider_response_time_ms": 8500,
      "timestamp": "2026-05-15T14:32:00Z"
    }
  }
}
```

**Failure Mode: Rate Limit**:
```yaml
Scenario: User creates 5 dossiers simultaneously, all call ElevenLabs
  
ElevenLabs API response (429):
  {
    "error": "Rate limit exceeded",
    "retry_after": 60
  }

Detection:
  n8n node receives 429 status

Recovery:
  1. Log to audit_trail: "elevenlabs_rate_limit_detected"
  2. Wait: Sleep for 60 seconds
  3. Retry: WF-610 triggers again
  4. If retry succeeds: Continue normally, log success
  5. If retry fails: Escalate to Founder, dossier marked ELEVENLABS_RATE_LIMIT_ERROR

Founder Action:
  Founder can:
  - REMODIFY: Request same script regenerated (will retry later)
  - ESCALATE: Report issue to ElevenLabs support
  - ACCEPT: Use fallback (Ollama text output without voice)
```

**Rollback Plan** (If ElevenLabs integration breaks):
```powershell
# 1. Disable WF-610 temporarily
npm run operator:modes:set -- --disable-workflow=WF-610

# 2. Notify users: ElevenLabs unavailable
npm run operator:alerts:send -- --message="Voice synthesis temporarily unavailable"

# 3. Fix API key or configuration
# ... debug steps ...

# 4. Re-enable WF-610
npm run operator:modes:set -- --enable-workflow=WF-610

# 5. Rerun failed dossiers
npm run operator:replay dossier-xyz --stage WF-610 --force
```

---

### PROVIDER 3: HEYGEN (Avatar Video)

**Status**: 🔴 DEFERRED_PROD-03

**Purpose**: Generate avatar video with lip-sync (video files)  
**API Endpoint**: `https://api.heygen.com/v1/video_requests`  
**Cost**: $2.00 per 1-minute avatar video  
**Estimated Time**: 2-3 minutes per video (asynchronous generation)  
**Available Avatars**: 30+ professional avatars  

**Current Status in PROD-01**:
- ❌ Credential NOT installed
- ❌ n8n workflow NOT created (WF-650 is stub)
- ❌ Cost gate NOT configured
- ❌ Async polling NOT implemented (HeyGen takes 2-3 min to generate)
- ❌ No dossiers with avatar outputs (PROVIDER_BRIDGE blocks execution)

**Phase Target**: PROD-03 (Week 10-12 after PROD-01)

**Key Challenge**: Asynchronous Execution
- User submits video generation request to HeyGen
- HeyGen returns job_id and says "check back in 2-3 minutes"
- n8n must implement polling mechanism: check every 30 sec until video_ready
- When ready, download video and store in dossier

**Implementation Checklist** (For PROD-03):

1. **Obtain API Credentials**:
   - [ ] User creates HeyGen account: https://heygen.com
   - [ ] User generates API token from dashboard
   - [ ] Operator stores in n8n credential vault
   - [ ] Test: `curl https://api.heygen.com/v1/voices -H "Authorization: Bearer $TOKEN"`

2. **Create n8n Credential**:
   - [ ] Create in n8n: Credentials → New → HeyGen API
   - [ ] Store: api_token, user_id, avatar_id (default: professional_avatar_001)
   - [ ] Test: Credential validates against API

3. **Define Packet Schema**:
   - [ ] Create: registries/packet_schema_WF-650_avatar.yaml
   - [ ] Fields: input_script, avatar_id, voice_id, output_video_path, duration_seconds, cost_usd, generation_time_ms
   - [ ] Validate: Schema matches HeyGen response + video metadata

4. **Create n8n Workflow (WF-650)** with Polling:
   - [ ] n8n node: "HeyGen Submit Video Request"
     - Input: script from pkt_200, avatar_id, voice from pkt_610 (if available)
     - Output: job_id, submitted_at
   - [ ] n8n loop node: "HeyGen Poll for Completion"
     - Query: `/api/v1/video_requests/{job_id}` every 30 sec
     - Exit condition: status == "completed" OR timeout 5 minutes
     - Log attempts to audit_trail
   - [ ] n8n node: "Download & Store Video"
     - Download video from HeyGen CDN URL
     - Save to: `/dossiers/dossier-xyz/video_heygen_001.mp4`
   - [ ] Error handling: Handle timeout (>5 min), API errors, network issues

5. **Configure Cost Gate**:
   - [ ] Policy: $5.00 max per dossier (for 1-2 minutes of video)
   - [ ] Check: user's budget_remaining >= $5.00 before WF-650 starts
   - [ ] If insufficient: Escalate to Founder
   - [ ] Track: Actual cost (~$2.00 per minute) deducted

6. **Dry Run Testing**:
   - [ ] Create dossier with mode=dry_run, provider_enabled=heygen
   - [ ] Call WF-650 with MOCK response:
     - Mock submit: return job_id="mock_job_123"
     - Mock poll: immediately return status="completed"
     - Mock download: copy placeholder video from /templates/heygen_sample.mp4
   - [ ] Verify: audit_trail recorded, cost_tracking = $0.00, no real HeyGen calls
   - [ ] Duration: dry run completes in <10 sec (no actual 2-3 min wait)

7. **Single Real Run**:
   - [ ] Create production dossier with provider_enabled=heygen
   - [ ] Generate ONE avatar video (script 30-60 sec, avatar_id="avatar_001")
   - [ ] Monitor polling: "Waiting for HeyGen... 30 sec, 60 sec, 90 sec..."
   - [ ] Expected total time: 2-3 minutes (1 min script + 2 min HeyGen generation)
   - [ ] Verify: Video file created at `/dossiers/dossier-xyz/video_heygen_001.mp4`
   - [ ] Verify: audit_trail shows job_id, polling attempts (4-6 checks), completion
   - [ ] Verify: cost_tracking shows ~$2.00
   - [ ] Watch video: 30-60 sec of avatar speaking, lip-sync quality acceptable

8. **Dossier Writeback Verification**:
   - [ ] Read dossier.packets.pkt_650_avatar
   - [ ] Confirm: input_script, avatar_id, output_video_path, duration_seconds, cost_usd
   - [ ] Confirm: audit_trail shows job_submission, all polling attempts, completion
   - [ ] Confirm: budget_remaining decreased by ~$2.00
   - [ ] Confirm: dossier state machine transitioned correctly

9. **Output File Validation**:
   - [ ] File exists: `/dossiers/dossier-xyz/video_heygen_001.mp4`
   - [ ] File size > 5 MB (minimum for quality video)
   - [ ] Video duration matches expected (±5 sec tolerance)
   - [ ] Video codec: H.264 or similar (playable in browsers)
   - [ ] Video quality: 1080p or 720p minimum

10. **Approval Gate Testing**:
    - [ ] Founder can view/download avatar video from approval screen
    - [ ] Founder can approve/reject video
    - [ ] Status transitions: AVATAR_GENERATION_RUNNING → AVATAR_GENERATION_COMPLETE → READY_FOR_APPROVAL → APPROVED_BY_FOUNDER

11. **Failure Mode Testing**:
    - [ ] Timeout (>5 min): HeyGen is slow, n8n stops polling, escalates to Founder with "Avatar generation timeout"
    - [ ] Invalid avatar_id: HeyGen returns 400 error, caught and logged
    - [ ] Download failure: Video generated but CDN unreachable, retry offered
    - [ ] Truncated video: File size < 5 MB, detected, flagged as error

12. **Sign-off & Release**:
    - [ ] Builder confirms all 11 checks passed
    - [ ] Operator confirms zero API tokens in logs
    - [ ] Founder approves: "WF-650 ready for PROD-03, cost gates effective"

**Failure Mode: Generation Timeout**:
```yaml
Scenario: HeyGen takes >5 minutes (API down or overloaded)

Detection:
  n8n polling loop reaches 5-minute timeout
  Status still "processing" (not "completed")

Recovery:
  1. Stop polling, log to audit_trail: "heygen_generation_timeout"
  2. Save job_id to dossier for manual recovery: dossier.pending_jobs.heygen_job_001
  3. Escalate to Founder: "Avatar generation timeout. Retry or use fallback (Ollama voice)?"
  
Founder Options:
  - REMODIFY: Request shorter script, try again (faster generation)
  - ESCALATE: Report to HeyGen support
  - ACCEPT: Use fallback (script-only output, no video)
  
Manual Recovery (if job eventually completes):
  npm run operator:heygen:poll-pending-job -- --dossier-id=dossier-xyz --job-id=heygen_job_001
```

**Async Execution Pattern** (Key for HeyGen and similar providers):
```json
{
  "dossier_state": {
    "status": "AVATAR_GENERATION_RUNNING",
    "pending_operations": [
      {
        "operation_type": "heygen_avatar_generation",
        "job_id": "hg_job_20260515_001",
        "submitted_at": "2026-05-15T14:32:00Z",
        "polling_since": "2026-05-15T14:32:30Z",
        "polling_count": 6,
        "next_poll_at": "2026-05-15T14:35:00Z",
        "timeout_at": "2026-05-15T14:37:00Z"
      }
    ]
  }
}
```

---

### PROVIDER 4: DALL-E 3 (Image Generation)

**Status**: 🔴 DEFERRED_PROD-03

**Purpose**: Generate images from text descriptions  
**API Endpoint**: `https://api.openai.com/v1/images/generations`  
**Cost**: $0.12-0.20 per image (varies by size/quality)  
**Typical Latency**: 10-30 sec per image  
**Available Sizes**: 1024x1024, 1792x1024, 1024x1792  

**Current Status in PROD-01**:
- ❌ Credential NOT installed (requires OpenAI API key)
- ❌ n8n workflow NOT created (WF-620 is stub)
- ❌ Cost gate NOT configured
- ❌ No dossiers with image outputs (PROVIDER_BRIDGE blocks execution)

**Phase Target**: PROD-03 (concurrent with voice/avatar)

**Implementation Checklist** (For PROD-03):

1. **Obtain API Credentials**:
   - [ ] User creates OpenAI account: https://platform.openai.com
   - [ ] User generates API key with "images" permission
   - [ ] Operator stores in n8n credential vault (encrypted)
   - [ ] Test: `curl https://api.openai.com/v1/models -H "Authorization: Bearer $KEY"`

2. **Create n8n Credential**:
   - [ ] Create: Credentials → New → OpenAI API (for images)
   - [ ] Store: api_key, model="dall-e-3", size="1024x1024" (default)
   - [ ] Test: Credential validates against API

3. **Define Packet Schema**:
   - [ ] Create: registries/packet_schema_WF-620_image.yaml
   - [ ] Fields: prompt, size, style, output_image_path, cost_usd, model_version
   - [ ] Validate: Schema matches DALL-E response format

4. **Create n8n Workflow (WF-620)**:
   - [ ] n8n node: "DALL-E 3 Image Generation"
     - Input: description (from topic research or script), style (default: "photorealistic"), size (1024x1024)
     - Output: image_url, revised_prompt, created_at
   - [ ] n8n node: "Download & Store Image"
     - Download from OpenAI URL
     - Save to: `/dossiers/dossier-xyz/image_dalle3_001.png`
   - [ ] Error handling: API errors, rate limits (429), offline

5. **Configure Cost Gate**:
   - [ ] Policy: $0.50 max per dossier (5 images max at $0.12 each)
   - [ ] Check: user's budget_remaining >= $0.50 before WF-620
   - [ ] If insufficient: Escalate to Founder
   - [ ] Track: Actual cost deducted

6. **Dry Run Testing**:
   - [ ] mode=dry_run, return mock image (placeholder PNG)
   - [ ] Verify: cost_tracking = $0.00, zero OpenAI calls

7. **Single Real Run**:
   - [ ] Generate ONE image for YouTube script
   - [ ] Image topic: Related to script content (e.g., "AI trends" script → image of AI robots)
   - [ ] Expected cost: ~$0.12
   - [ ] Verify: Image file created, 1024x1024, readable format
   - [ ] Verify: audit_trail shows image generation, cost tracking shows $0.12

8. **Dossier Writeback Verification**:
   - [ ] dossier.packets.pkt_620_image contains image metadata
   - [ ] audit_trail shows image generation, prompt, cost

9. **Output File Validation**:
   - [ ] File exists: `/dossiers/dossier-xyz/image_dalle3_001.png`
   - [ ] File size > 100KB (quality image)
   - [ ] Image dimensions: 1024x1024

10. **Approval Gate Testing**:
    - [ ] Founder can view image in approval screen
    - [ ] Approve/reject workflows function correctly

11. **Failure Mode Testing**:
    - [ ] Rate limit: Retry mechanism (max 3 attempts with backoff)
    - [ ] Bad prompt: DALL-E rejects, error caught
    - [ ] Offline: Timeout after 30 sec

12. **Sign-off & Release**:
    - [ ] All checks passed
    - [ ] Founder approves WF-620

---

### PROVIDER 5: YOUTUBE_DATA_API (Publishing)

**Status**: 🔴 DEFERRED_PROD-05

**Purpose**: Upload videos to YouTube, manage metadata, analytics  
**API Endpoint**: `https://www.googleapis.com/youtube/v3/videos`  
**Auth**: OAuth 2.0 (user grants permission, refresh tokens)  
**Cost**: $0.00 (YouTube Data API is free tier)  
**Typical Latency**: 10-30 sec per upload (for small videos)  

**Current Status in PROD-01**:
- ❌ Credential NOT installed (requires OAuth)
- ❌ n8n workflow NOT created (WF-660 is stub)
- ❌ OAuth redirect URI NOT configured
- ❌ No dossiers published to YouTube (PROVIDER_BRIDGE blocks execution)

**Phase Target**: PROD-05 (after PROD-03, requires multi-channel architecture)

**Key Challenge**: OAuth Flow
- User must grant Shadow Creator permission to upload videos
- YouTube returns refresh token (valid for ~50 days)
- Must implement token refresh logic

**Implementation Checklist** (For PROD-05):

1. **Setup Google Cloud Project**:
   - [ ] Create GCP project: https://console.cloud.google.com
   - [ ] Enable YouTube Data API v3
   - [ ] Create OAuth 2.0 credentials (type: Web application)
   - [ ] Set redirect URI: `http://localhost:5050/oauth/google/callback`

2. **Create n8n Credential** (OAuth):
   - [ ] Create: Credentials → New → Google OAuth
   - [ ] Configure: client_id, client_secret, redirect_uri
   - [ ] User clicks "Authorize" button in UI
   - [ ] Browser redirects to Google login
   - [ ] User grants "Upload videos to YouTube" permission
   - [ ] Google redirects back with auth_code
   - [ ] n8n exchanges auth_code for access_token + refresh_token
   - [ ] Store refresh_token in credential vault (encrypted)

3. **Define Packet Schema**:
   - [ ] Create: registries/packet_schema_WF-660_publishing.yaml
   - [ ] Fields: video_file_path, title, description, tags, privacy_status (private/unlisted/public), channel_id, youtube_video_id, upload_status, cost_usd (always 0)

4. **Create n8n Workflow (WF-660)**:
   - [ ] n8n node: "YouTube OAuth Token Refresh"
     - Input: refresh_token from credential vault
     - Check: token_expiry < now + 1 hour
     - If expired: call Google API to refresh
     - Output: valid access_token
   - [ ] n8n node: "YouTube Upload Video"
     - Input: video_file_path (from pkt_640), title, description, tags, privacy_status
     - Call: POST /youtube/v3/videos with multipart upload
     - Output: youtube_video_id, watch_url
   - [ ] n8n node: "YouTube Set Metadata"
     - Set: thumbnail, category, language, caption hint, etc.
   - [ ] Error handling: Upload timeout (>10 min), token expired, permission denied

5. **Configure "Cost Gate"** (Free, but quota-limited):
   - [ ] Policy: User can upload max 2 videos per day (YouTube API quota)
   - [ ] Track: Daily upload count
   - [ ] If limit exceeded: Escalate to Founder (quota increase request)
   - [ ] Cost: $0.00 always (free tier)

6. **Dry Run Testing**:
   - [ ] mode=dry_run
   - [ ] Mock YouTube API responses
   - [ ] Verify: audit_trail recorded, zero actual uploads to YouTube

7. **Single Real Run** (REQUIRES USER'S ACTUAL YOUTUBE ACCOUNT):
   - [ ] User authorizes Shadow Creator to upload videos
   - [ ] User receives YouTube permission prompt
   - [ ] User clicks "Allow"
   - [ ] Shadow Creator receives refresh_token
   - [ ] Generate ONE test video
   - [ ] Upload to YouTube with privacy_status="unlisted" (only accessible via link)
   - [ ] Verify: Video appears on YouTube
   - [ ] Verify: Title, description, tags correct
   - [ ] Watch URL example: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`

8. **Dossier Writeback Verification**:
   - [ ] dossier.packets.pkt_660_publishing contains youtube_video_id
   - [ ] audit_trail shows upload timestamp, watch_url
   - [ ] budget_remaining unchanged ($0.00 cost)

9. **Output File Validation**:
   - [ ] YouTube video accessible at returned watch_url
   - [ ] Title, description, tags visible on YouTube
   - [ ] Video playable (no corruption)

10. **Approval Gate Testing**:
    - [ ] Founder can see YouTube link in approval screen
    - [ ] Founder can click to preview video on YouTube before approving
    - [ ] Approve workflow publishes to public (changes privacy_status to "public")

11. **Failure Mode Testing**:
    - [ ] Token expired: Token refresh triggers, new access_token obtained
    - [ ] Permission revoked: User removes Shadow Creator from Google account, error caught
    - [ ] Upload timeout: File too large or network slow, retry offered
    - [ ] Quota exceeded: Daily upload limit reached, escalate to Founder

12. **Sign-off & Release**:
    - [ ] All checks passed
    - [ ] Founder approves WF-660

**Token Refresh Pattern** (OAuth):
```json
{
  "credential": {
    "type": "google_oauth",
    "client_id": "...",
    "client_secret": "...",
    "refresh_token": "...",
    "access_token": "...",
    "access_token_expiry": "2026-05-06T15:32:00Z"  // auto-refresh before expiry
  }
}
```

---

### PROVIDER 6: WAV2LIP (Lipsync Video)

**Status**: 🔴 DEFERRED_PROD-03

**Purpose**: Sync lip movements to voice (takes avatar video + audio, creates lip-synced video)  
**Type**: Open-source (runs locally via Python)  
**Cost**: $0.00 (open-source, runs locally)  
**Typical Latency**: 2-5 minutes per video (CPU-intensive)  

**Current Status in PROD-01**:
- ❌ Not installed (requires Python + GPU/CUDA)
- ❌ n8n workflow NOT created
- ❌ No dossiers with lip-sync (PROVIDER_BRIDGE blocks execution)

**Phase Target**: PROD-03 (depends on avatar provider being ready first)

**Implementation Checklist** (For PROD-03):

1. **Install Wav2Lip Locally**:
   - [ ] Clone repo: `git clone https://github.com/Rudrabha/Wav2Lip`
   - [ ] Install dependencies: `pip install -r requirements.txt`
   - [ ] Download pre-trained model: `python download_model.py face seg`
   - [ ] Test: Run demo on sample video

2. **Create n8n Workflow** (or PowerShell script wrapper):
   - [ ] Option A: Call local Python script from n8n
     - n8n node: "PowerShell / Execute"
     - Command: `python wav2lip_batch.py --video avatar.mp4 --audio voice.wav --output lip_sync.mp4`
   - [ ] Option B: Create n8n nodes for each Wav2Lip step (frame extraction, lipsync, reassembly)

3. **Define Packet Schema**:
   - [ ] Fields: input_video_path (avatar), input_audio_path (voice), output_video_path (lip-synced), processing_time_ms, cost_usd (0)

4. **Dry Run Testing**:
   - [ ] Create mock Wav2Lip output (dummy MP4 file)
   - [ ] Verify: cost_tracking = $0.00, no actual GPU processing

5. **Single Real Run**:
   - [ ] Input: avatar video (30-60 sec, from HeyGen) + voice audio (from ElevenLabs)
   - [ ] Process: Wav2Lip creates lip-synced video
   - [ ] Expected time: 2-5 minutes (CPU-intensive)
   - [ ] Output: `/dossiers/dossier-xyz/video_lip_sync_001.mp4`
   - [ ] Verify: Avatar's lips move with audio (quality acceptable)

6. **Dossier Writeback Verification**:
   - [ ] dossier.packets.pkt_645_lip_sync contains output path and processing time

7. **Approval Gate Testing**:
    - [ ] Founder can watch lip-synced video before approval

8. **Failure Mode Testing**:
    - [ ] Timeout (>10 min): GPU memory issue, error caught
    - [ ] Bad input (wrong audio length): Wav2Lip fails gracefully, logged

9. **Sign-off & Release**:
    - [ ] Builder confirms zero GPU OOM errors during testing
    - [ ] Founder approves

---

### PROVIDER 7: FFMPEG (Video Composition)

**Status**: 🔴 DEFERRED_PROD-03

**Purpose**: Compose multiple video/audio/image streams into final output (add overlays, transitions, effects)  
**Type**: Open-source command-line tool  
**Cost**: $0.00 (open-source, runs locally)  
**Typical Latency**: 1-3 minutes per video (depends on output resolution/codec)  

**Current Status in PROD-01**:
- ❌ Not installed
- ❌ n8n workflow NOT created
- ❌ No dossiers with composed videos (PROVIDER_BRIDGE blocks execution)

**Phase Target**: PROD-03 (concurrent with other video tools)

**Implementation Checklist** (For PROD-03):

1. **Install FFmpeg**:
   - [ ] Windows: `choco install ffmpeg` or download from ffmpeg.org
   - [ ] Linux: `apt-get install ffmpeg`
   - [ ] Test: `ffmpeg -version` should return version info

2. **Create n8n Workflow** (FFmpeg command wrapper):
   - [ ] n8n node: "FFmpeg Compose Video"
     - Inputs: lip-synced video, background music, overlay images, intro/outro clips
     - Command: `ffmpeg -i lip_sync.mp4 -i music.mp3 -i overlay.png ... -c:v libx264 -c:a aac output.mp4`
     - Output: final_video.mp4

3. **Define Packet Schema**:
   - [ ] Fields: input_video_path, input_audio_paths (array), overlay_image_paths, output_video_path, processing_time_ms, cost_usd (0)

4. **Dry Run Testing**:
   - [ ] Mock FFmpeg output (dummy MP4)
   - [ ] cost_tracking = $0.00

5. **Single Real Run**:
   - [ ] Compose 60-second final video from:
     - Lip-synced avatar video (45 sec)
     - Background music (60 sec)
     - Intro/outro clips (15 sec total)
     - Text overlays (titles, subtitles)
   - [ ] Expected output: 1080p H.264, file size ~100-200 MB

6. **Approval Gate Testing**:
    - [ ] Founder can download final video before approval
    - [ ] Video quality acceptable

7. **Sign-off & Release**:
    - [ ] FFmpeg correctly installed and tested
    - [ ] Founder approves

---

### PROVIDER 8: OPENAI (GPT-4) — Cloud LLM Alternative

**Status**: 🔴 DEFERRED_PROD-02

**Purpose**: Cloud LLM option for faster, higher-quality scripts (alternative to Ollama)  
**Cost**: $0.03 per 1K input tokens, $0.06 per 1K output tokens (~$0.15 per dossier)  
**Model**: gpt-4, gpt-4-turbo, gpt-4o (latest)  

**Phase Target**: PROD-02 (early, provides speed boost to Ollama)

**Implementation Checklist** (Abbreviated, similar to ElevenLabs):

1. **Obtain API Credentials**: OpenAI API key
2. **Create n8n Credential**: OpenAI API
3. **Define Packet Schema**: prompt, response, tokens_used, cost
4. **Create n8n Workflow (WF-200-alt)**: Call GPT-4 for script generation
5. **Configure Cost Gate**: $1.00 max per dossier (safety limit)
6. **Dry Run Testing**: Mock response, cost = $0
7. **Single Real Run**: Generate ONE script with GPT-4, cost ~$0.15
8. **Dossier Writeback**: Audit trail, cost tracking
9. **Approval Gate**: Founder can select which model was used (Ollama vs GPT-4)
10. **Failure Mode**: Rate limit, API error handling
11. **Speed Benefit**: WF-200 with GPT-4 completes in 5-10 sec (vs 30-120 sec with Ollama)
12. **Sign-off**: Founder approves speed-benefit trade-off

---

### PROVIDER 9: GEMINI (Google) — Cloud LLM

**Status**: 🔴 DEFERRED_PROD-02

**Purpose**: Alternative cloud LLM (Google's offering)  
**Cost**: $0.075 per 1M input tokens (~$0.10 per dossier)  
**Model**: gemini-pro, gemini-vision  

**Phase Target**: PROD-02 (concurrent with OpenAI)

**Implementation**: Similar to OpenAI provider (abbreviated for space)

---

### PROVIDER 10: CLAUDE_ANTHROPIC (Anthropic API) — Cloud LLM

**Status**: 🔴 DEFERRED_PROD-02

**Purpose**: Claude 3.5 Sonnet via API (high-quality, multimodal)  
**Cost**: $0.003 per 1K input tokens (~$0.05 per dossier)  
**Model**: claude-3-5-sonnet, claude-opus  

**Phase Target**: PROD-02 (premium option for best quality)

**Note**: This is different from using Claude in Open WebUI chat interface. This is direct API access for agents.

---

### PROVIDER 11: PERPLEXITY (Research LLM) — Cloud LLM

**Status**: 🔴 DEFERRED_PROD-02

**Purpose**: Research-optimized LLM (real-time web search included)  
**Cost**: Similar to OpenAI (~$0.15 per dossier)  
**Advantage**: Built-in web search for WF-100 (topic intelligence)  

**Phase Target**: PROD-02 (optional, replaces WF-100 web search step)

---

### PROVIDER 12: GROQ (Fast Inference) — Cloud LLM

**Status**: 🔴 DEFERRED_PROD-03

**Purpose**: Ultra-fast LLM inference (serverless)  
**Cost**: Similar to OpenAI (~$0.10 per dossier)  
**Advantage**: Very fast response times (good for agent orchestration)  

**Phase Target**: PROD-03

---

### PROVIDER 13: DEEPSEEK (Research Models) — Cloud LLM

**Status**: 🔴 DEFERRED_PROD-03

**Purpose**: Research-grade LLM (Chinese alternative to OpenAI)  
**Cost**: $0.14 per 1M input tokens (very cheap, ~$0.05 per dossier)  
**Model**: deepseek-chat, deepseek-coder  

**Phase Target**: PROD-03

---

### PROVIDER 14: MISTRAL (Open LLM) — Cloud LLM

**Status**: 🔴 DEFERRED_PROD-02

**Purpose**: Open LLM via API (Mistral's cloud service)  
**Cost**: $0.14 per 1M input tokens (~$0.08 per dossier)  
**Model**: mistral-medium, mistral-large  

**Phase Target**: PROD-02 (cost-optimized alternative)

---

### PROVIDER 15: KIMI_K2 (Chinese LLM) — Cloud LLM

**Status**: 🔴 DEFERRED_PROD-03

**Purpose**: Chinese LLM for multilingual content  
**Cost**: Pricing TBD  
**Advantage**: Optimized for Chinese language scripts  

**Phase Target**: PROD-03 (if multilingual support required)

---

### PROVIDER 16: NANO_BANANA (Serverless GPU) — Compute Provider

**Status**: 🔴 DEFERRED_PROD-04

**Purpose**: Serverless GPU compute (for custom model inference, local LLM acceleration)  
**Cost**: $0.0004 per GPU-second (~$0.20 per dossier if used for acceleration)  
**Use Case**: Run larger local models (Llama 70B) in cloud instead of local Ollama  

**Phase Target**: PROD-04 (optimization layer)

---

### PROVIDER 17: HIGGSFIELD (Custom Models) — Compute Provider

**Status**: 🔴 DEFERRED_PROD-04

**Purpose**: Deploy custom fine-tuned models (Higgsfield platform)  
**Cost**: Usage-based  
**Use Case**: Train custom Shadow Creator script-generation model  

**Phase Target**: PROD-04/05 (advanced optimization)

---

### PROVIDER 18: BROWSER_AUTOMATION (Fallback) — Web Scraping

**Status**: 🔴 DEFERRED_PROD-05

**Purpose**: Fallback for providers without API (manual browser automation)  
**Type**: Selenium/Playwright automation  
**Cost**: $0.00 (open-source tools)  
**Use Case**: If YouTube API fails, use browser to upload video manually  

**Phase Target**: PROD-05 (safety fallback)

---

## PART 3: PROVIDER ACTIVATION TIMELINE SUMMARY

| Provider | Type | Cost | Phase | Est. Weeks | Status |
|----------|------|------|-------|------------|--------|
| Ollama Local | LLM | $0 | PROD-01 ✅ | 0 | ACTIVE |
| OpenRouter | Multi-Gateway | $$$ | PROD-02 | 4-6 | DEFERRED |
| OpenAI (GPT-4) | LLM | $$$ | PROD-02 | 4-6 | DEFERRED |
| Gemini | LLM | $ | PROD-02 | 4-6 | DEFERRED |
| Claude API | LLM | $ | PROD-02 | 4-6 | DEFERRED |
| Perplexity | LLM | $$ | PROD-02 | 4-6 | DEFERRED |
| Groq | LLM | $$ | PROD-03 | 8-10 | DEFERRED |
| DeepSeek | LLM | $ | PROD-03 | 8-10 | DEFERRED |
| Mistral | LLM | $ | PROD-02 | 4-6 | DEFERRED |
| Kimi/K2 | LLM | $$ | PROD-03 | 8-10 | DEFERRED |
| **ElevenLabs** | **Voice** | **$$** | **PROD-03** | **8-10** | **DEFERRED** |
| **HeyGen** | **Avatar** | **$$$** | **PROD-03** | **8-10** | **DEFERRED** |
| **DALL-E 3** | **Image** | **$$** | **PROD-03** | **8-10** | **DEFERRED** |
| **Wav2Lip** | **Lipsync** | **$0** | **PROD-03** | **8-10** | **DEFERRED** |
| **FFmpeg** | **Compose** | **$0** | **PROD-03** | **8-10** | **DEFERRED** |
| **YouTube Data API** | **Publishing** | **$0** | **PROD-05** | **16-18** | **DEFERRED** |
| YouTube Analytics | Analytics | $0 | PROD-05 | 16-18 | DEFERRED |
| Nano Banana | GPU Compute | $ | PROD-04 | 12-14 | DEFERRED |
| Higgsfield | Custom Models | $$ | PROD-04 | 12-14 | DEFERRED |
| Browser Automation | Fallback | $0 | PROD-05 | 16-18 | DEFERRED |

---

## PART 4: COST PROJECTION PER DOSSIER

### Current Costs (PROD-01)
```
Ollama topic research: $0.00
Ollama script generation: $0.00
─────────────────────────────
Total per dossier: $0.00
```

### Future Costs by Phase

**PROD-02** (with optional cloud LLMs):
```
Option A (Budget): 
  Mistral LLM: $0.08
  Total: $0.08

Option B (Premium):
  OpenAI GPT-4: $0.15
  Total: $0.15

Option C (Hybrid - Default):
  Ollama (local): $0.00
  Total: $0.00
```

**PROD-03** (with voice + avatar):
```
Ollama research: $0.00
Ollama script: $0.00
ElevenLabs voice: $0.15
HeyGen avatar: $2.00
FFmpeg composition: $0.00
────────────────────────
Total: $2.15
```

**PROD-03** (with voice + image, no avatar):
```
Ollama research: $0.00
Ollama script: $0.00
ElevenLabs voice: $0.15
DALL-E image: $0.12
────────────────────────
Total: $0.27
```

**PROD-05** (with publishing):
```
PROD-03 content: $2.15
YouTube upload: $0.00 (free API)
────────────────────────
Total: $2.15
```

---

## PART 5: CREDENTIAL ROTATION & EXPIRY

### PROD-04+ Requirement: Credential Lifecycle

**Credential Expiry Policies** (to implement in PROD-04/05):

| Credential Type | Expiry | Rotation Interval | Action on Expiry |
|---|---|---|---|
| API_KEY (OpenAI, ElevenLabs, etc.) | Never (unless rotated) | 90 days recommended | Escalate to user for renewal |
| OAuth Token (YouTube, Google) | 1 hour | Auto-refresh | Silent refresh if refresh_token valid |
| OAuth Refresh Token | 50 days (Google) | N/A | Request user re-auth if expired |
| Service Account Key | 90 days | 90 days | Escalate for renewal |

**Expiry Monitoring**:
```powershell
npm run credentials:check-expiry
# Output: 
# ElevenLabs API key expires in 45 days (warning)
# YouTube OAuth refresh token expires in 7 days (alert)
```

---

## PART 6: COST GOVERNANCE & BUDGETS

### Budget Enforcement (All Providers)

**Founder Sets Budgets**:
```yaml
budget_policy:
  per_user_monthly: $100  # Max spend per creator per month
  per_dossier: $5.00      # Max spend per single dossier
  per_provider:           # Max spend per provider per month
    elevenlabs: $30
    heygen: $50
    openai: $40
    other: $20
  approval_gate:
    if_spend > $1.00: Founder approval required
    if_spend > $5.00: Immediate escalation + halt
```

**Cost Tracking** (Real-time):
```json
{
  "dossier_cost_tracking": {
    "ollama_research": 0.00,
    "elevenlabs_voice": 0.15,
    "heygen_avatar": 2.00,
    "dalle_image": 0.12,
    ──────────────────────
    "total": 2.27,
    "budget_remaining_user": 97.73,
    "budget_remaining_dossier": 2.73
  }
}
```

---

## PART 7: ROLLBACK PROCEDURES FOR EACH PROVIDER

**Generic Rollback** (all providers):

1. **Disable Provider Immediately**:
   ```powershell
   npm run operator:providers:disable -- --provider=elevenlabs
   # All WF-610 calls now return "Provider disabled" error
   ```

2. **Notify Active Users**:
   ```powershell
   npm run operator:alerts:send -- --message="ElevenLabs service temporarily unavailable"
   ```

3. **Revert Dossiers in Progress**:
   ```powershell
   npm run operator:dossier:revert -- --stage=WF-610 --affected-dossiers=3
   # Rollback 3 dossiers from VOICE_GENERATION_RUNNING to SCRIPT_GENERATION_COMPLETE
   ```

4. **Refund Charges** (if provider failed):
   ```powershell
   npm run billing:refund -- --dossier-id=xyz --reason="provider_failure"
   # Credit user's budget_remaining with $0.15
   ```

5. **Fix & Re-enable**:
   ```powershell
   # Fix: Update API key, fix workflow bug, etc.
   npm run operator:providers:enable -- --provider=elevenlabs
   ```

6. **Replay Failed Dossiers**:
   ```powershell
   npm run operator:replay dossier-xyz --stage WF-610 --force
   # Re-run WF-610 on failed dossier, should now succeed
   ```

---

## PART 8: VALIDATION CHECKLIST FOR ALL PROVIDERS

### Pre-Release Validation (Before Any Provider Goes Live)

For **EACH provider**, before Founder approval:

- [ ] **Credential Security**: No API keys in logs, environment variables, or dossier files
- [ ] **Cost Accuracy**: Actual cost matches estimated cost (±10%)
- [ ] **Audit Trail**: All calls logged to dossier.audit_trail with timestamp, actor, result
- [ ] **Error Handling**: All failure modes tested and handled gracefully
- [ ] **Dry Run**: Non-production dossier executes without charges
- [ ] **Real Run**: Production dossier executes with accurate cost tracking
- [ ] **Rollback**: Provider can be disabled and dossiers reverted without data loss
- [ ] **Rate Limiting**: Retry logic works if provider rate-limits
- [ ] **Timeout Handling**: Async providers implement polling correctly (HeyGen, etc.)
- [ ] **Output Validation**: Generated files exist, are readable, meet quality standards
- [ ] **Approval Gate**: Founder can review and approve/reject outputs
- [ ] **Zero Breach**: No unauthorized provider calls, no cost overages, no credential leaks

---

**Status**: 📋 DESIGN_ONLY — No providers active except Ollama  
**Target Release**: Phased from PROD-02 through PROD-07  
**Validation Gate**: Each provider requires Founder sign-off before activation  
**Founder Authority**: Required for credential storage, budget policy, cost approval  

---

