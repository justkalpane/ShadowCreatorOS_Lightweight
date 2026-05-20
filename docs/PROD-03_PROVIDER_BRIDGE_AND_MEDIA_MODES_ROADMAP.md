# Shadow Creator OS - PROD-03 Provider Bridge & Media Modes Roadmap

**Version**: 1.0.0  
**Date**: 2026-05-05  
**Classification**: FUTURE PHASE ARCHITECTURE  
**Purpose**: Define the provider bridge boundary, document all media modes, and map the path to real media generation

---

## CRITICAL PREAMBLE: PROD-01 DOES NOT GENERATE REAL MEDIA

**This Must Be Clear**:

✅ **PROD-01 (Current, May 2026)**:
- Text generation (research, scripts): ✅ REAL (Ollama local)
- Image generation: 🌉 PLANNING PACKETS ONLY (no actual files)
- Video generation: 🌉 PLANNING PACKETS ONLY (no actual files)
- Audio/Voice generation: 🌉 PLANNING PACKETS ONLY (no actual files)
- Avatar generation: 🌉 PLANNING PACKETS ONLY (no actual files)
- Publishing: ❌ NOT AVAILABLE

📦 **What Exists**: JSON metadata and planning instructions for each media type. Zero actual media files generated.

🌉 **What Blocks It**: Provider bridge - the safety boundary that prevents real provider calls without explicit enablement.

⏳ **When Available**: PROD-02 (2-3 months), PROD-03 (4-6 months)

---

## PART 1: PROVIDER BRIDGE ARCHITECTURE

### What is the Provider Bridge?

**Definition**: A safety boundary that separates planning/metadata generation (safe) from real provider execution (requires credentials, costs money, creates real files).

```
┌─────────────────────────────────────────────┐
│         PRODUCER OPERATIONS (Safe)          │
│  ✅ Research generation (text)              │
│  ✅ Script generation (text)                │
│  ✅ Metadata generation (JSON)              │
│  ✅ Planning packets (instructions)         │
│  ✅ Local Ollama only                       │
│  ✅ No credentials needed                   │
│  ✅ Zero cost                               │
└─────────────────────────────────────────────┘
                       ↓
              [PROVIDER BRIDGE]
        (Safety gate - requires enablement)
                       ↓
┌─────────────────────────────────────────────┐
│     PROVIDER EXECUTION (Controlled)         │
│  🌉 Image generation (DALL-E, Midjourney)   │
│  🌉 Video assembly (Runway, HeyGen)         │
│  🌉 Voice generation (ElevenLabs)           │
│  🌉 Music generation (Mubert)               │
│  🌉 Avatar rendering (Synthesia)            │
│  🌉 Publishing (YouTube API)                │
│  🌉 Requires credentials                    │
│  🌉 Incurs costs ($0.10-5 per dossier)     │
│  🌉 Creates actual output files             │
└─────────────────────────────────────────────┘
```

### Where is the Bridge Implemented?

**File**: `engine/api/operator.js` lines 183
```javascript
provider_boundary_note: 'Planning packet generated. Actual provider execution is not enabled yet.'
```

**Also**: Safe Mode setting in mode_registry.yaml (always-on in PROD-01)

**Enforcement**:
- WF-601+ (provider handler workflows) are registered but BLOCKED
- Provider credentials are NOT loaded
- Provider router reports "provider_bridge_required" for all media endpoints
- No actual API calls made to external services

### How to Enable (Future)

**PROD-02 Timeline** (4-6 weeks after PROD-01 go-live):
```powershell
# Step 1: Founder adds provider credentials
curl -X POST http://127.0.0.1:5050/operator/providers/add-credential `
  -Body (@{
    provider="openai"
    api_key="sk-proj-xxxxx"
    org_id="org-xxxxx"
  } | ConvertTo-Json)

# Step 2: Switch runtime from "local" to "hybrid"
curl -X POST http://127.0.0.1:5050/operator/runtime/set `
  -Body (@{runtime_mode="hybrid"} | ConvertTo-Json)

# Step 3: Explicitly enable provider bridge
curl -X POST http://127.0.0.1:5050/operator/modes/provider-bridge/enable `
  -Body (@{provider="openai"; actor_mode="founder"} | ConvertTo-Json)

# Step 4: Verify provider health
curl http://127.0.0.1:5050/operator/providers/openai

# Response should show:
# {
#   "provider": "openai",
#   "status": "healthy",
#   "enabled": true,
#   "quota_used_usd": 0.00,
#   "quota_remaining_usd": 50.00
# }

# Step 5: Create new dossier - will now trigger image generation
# (System routes through WF-610 instead of creating planning packet)
```

---

## PART 2: ALL MEDIA MODES & EXECUTION PATHS

### Media Mode 1: Image/Illustration Generation

**Current Status (PROD-01)**: 🌉 PROVIDER_BRIDGE_REQUIRED

**Planning Packet Structure**:
```json
{
  "packet_id": "PKT-image-plan-001",
  "packet_type": "image_planning_packet",
  "dossier_id": "DOSSIER-xxxxx",
  "generated_at": "2026-05-05T12:35:56Z",
  "images_needed": [
    {
      "sequence": 1,
      "scene_description": "Hook scene: Frustrated creator at computer",
      "prompt": "3D flat design illustration of a tired content creator sitting at desk with multiple tabs open, colorful, modern style, 16:9 aspect ratio",
      "dimensions": "1920x1080",
      "style_reference": "modern, flat design, colorful, professional",
      "estimated_duration_sec": 45
    },
    {
      "sequence": 2,
      "scene_description": "AI tools presentation",
      "prompt": "Modern minimalist dashboard interface showing AI tools logos (ChatGPT, Claude, Midjourney) with green checkmarks",
      "dimensions": "1920x1080",
      "style_reference": "corporate, minimalist, clean"
    }
  ],
  "provider_boundary": "provider_bridge_required",
  "estimated_cost_usd": 0.24,
  "estimated_generation_time_sec": 90,
  "no_actual_images_generated": true,
  "notes": "PROD-01 does not generate actual image files. This packet contains prompts and metadata only."
}
```

**Workflow Path** (When Enabled):

```
WF-400 (Production Planning)
  ↓
  Detects: image_generation needed
  ↓
WF-610 (Image Generation Handler) [BLOCKED in PROD-01]
  ↓
  Loads provider credential (openai/midjourney/stable)
  ↓
  For each image_needed:
    - Call provider API with prompt
    - Download generated image
    - Create PKT-image-001, PKT-image-002, etc.
    - Log cost in dossier audit trail
  ↓
WF-300 (Metadata) [continues]
  ↓
PKT-image-001.json, image_1920x1080_000.png (ACTUAL FILE)
```

**Providers & Costs** (PROD-02+):

| Provider | Cost Per Image | Quality | Speed | Notes |
|----------|---|---------|-------|-------|
| DALL-E 3 (OpenAI) | $0.12-0.20 | Excellent | Fast (60s) | RECOMMENDED for startup |
| Midjourney | $0.04-0.10 | Excellent | Slower (120s) | Queuing required |
| Stable Diffusion 3 | $0.01-0.03 | Good | Fast (30s) | Open source option |
| Leonardo.AI | $0.02-0.08 | Good | Medium | Training custom models |

**Expected Timeline**:
- PROD-02 (May/June): DALL-E 3 support
- PROD-02 (June): Midjourney support
- PROD-03 (July): Stable Diffusion support

---

### Media Mode 2: Voice/Narration Generation

**Current Status (PROD-01)**: 🌉 PROVIDER_BRIDGE_REQUIRED

**Planning Packet Structure**:
```json
{
  "packet_id": "PKT-voice-plan-001",
  "packet_type": "voice_planning_packet",
  "dossier_id": "DOSSIER-xxxxx",
  "generated_at": "2026-05-05T12:36:56Z",
  "narration_segments": [
    {
      "sequence": 1,
      "text": "Did you know that 87% of creators waste time managing repetitive tasks?",
      "duration_estimated_sec": 5,
      "voice_profile": "female_narrator_en_us_calm_professional",
      "pitch": 1.0,
      "speed": 1.0,
      "emotion": "concerned_but_hopeful"
    },
    {
      "sequence": 2,
      "text": "That's where AI tools come in.",
      "duration_estimated_sec": 3,
      "voice_profile": "female_narrator_en_us_calm_professional",
      "pitch": 1.0,
      "speed": 1.0,
      "emotion": "informative"
    }
  ],
  "total_audio_duration_sec": 180,
  "voice_consistency_required": true,
  "provider_boundary": "provider_bridge_required",
  "estimated_cost_usd": 0.27,
  "no_actual_audio_generated": true,
  "notes": "PROD-01 does not generate actual audio files. This packet contains text and voice specifications only."
}
```

**Workflow Path** (When Enabled):

```
WF-400 (Production Planning)
  ↓
  Detects: voice_narration needed
  ↓
WF-620 (Voice Generation Handler) [BLOCKED in PROD-01]
  ↓
  Selects voice provider & voice ID
  ↓
  For each narration_segment:
    - Call provider API with text + voice specs
    - Receive audio MP3
    - Save as narration_segment_001.mp3, etc.
    - Create PKT-voice-001.json
    - Log cost
  ↓
  Combine all segments into single narration.mp3
  ↓
PKT-voice-001.json + narration.mp3 (ACTUAL FILE)
```

**Providers & Costs** (PROD-02+):

| Provider | Cost Per 1K Chars | Quality | Speed | Notes |
|----------|---|---------|-------|-------|
| ElevenLabs | $0.10-0.30 | Excellent | Fast (30s) | RECOMMENDED, zero latency |
| Google Cloud TTS | $0.04-0.16 | Good | Medium | Bulk pricing available |
| AWS Polly | $0.02-0.08 | Good | Fast | Enterprise option |
| Azure Cognitive | $0.06-0.15 | Good | Medium | Enterprise bundling |

**Expected Timeline**:
- PROD-02 (May/June): ElevenLabs support
- PROD-02 (June): Google Cloud TTS
- PROD-03 (July): AWS Polly

---

### Media Mode 3: Background Music/BGM

**Current Status (PROD-01)**: 🌉 PROVIDER_BRIDGE_REQUIRED

**Planning Packet Structure**:
```json
{
  "packet_id": "PKT-music-plan-001",
  "packet_type": "music_planning_packet",
  "dossier_id": "DOSSIER-xxxxx",
  "generated_at": "2026-05-05T12:37:56Z",
  "music_segments": [
    {
      "segment": "intro",
      "duration_sec": 15,
      "mood": "upbeat, energetic, modern",
      "tempo_bpm": 120,
      "genre": "electronic, ambient",
      "instruments": ["synth", "drums"],
      "tags": ["AI", "technology", "productivity"]
    },
    {
      "segment": "body",
      "duration_sec": 150,
      "mood": "professional, informative, engaging",
      "tempo_bpm": 100,
      "genre": "electronic, corporate",
      "instruments": ["piano", "strings", "synth"]
    },
    {
      "segment": "outro",
      "duration_sec": 10,
      "mood": "hopeful, inspiring",
      "tempo_bpm": 120,
      "genre": "electronic"
    }
  ],
  "total_music_duration_sec": 175,
  "provider_boundary": "provider_bridge_required",
  "estimated_cost_usd": 0.15,
  "no_actual_audio_generated": true,
  "notes": "PROD-01 does not generate actual music files. This packet contains specifications only."
}
```

**Workflow Path** (When Enabled):

```
WF-400 (Production Planning)
  ↓
WF-630 (Music Generation Handler) [BLOCKED in PROD-01]
  ↓
  For each segment:
    - Call music generation API with mood/tempo/genre
    - Receive audio MP3 or WAV
    - Save as bgm_intro.mp3, bgm_body.mp3, bgm_outro.mp3
  ↓
  Compose segments into single background_music.mp3
  ↓
PKT-music-001.json + background_music.mp3 (ACTUAL FILE)
```

**Providers & Costs** (PROD-02+):

| Provider | Cost Per Minute | Quality | Speed | Notes |
|----------|---|---------|-------|-------|
| Mubert | $0.01-0.05 | Good | Fast (10s) | RECOMMENDED, AI-native |
| AIVA | $0.02-0.08 | Good | Medium | Custom composition |
| Soundraw | $0.02-0.10 | Good | Fast | Creator-friendly UI |
| Epidemic Sound | $0.10-0.50/mo | Excellent | Instant | Licensing model |

---

### Media Mode 4: Video Assembly & Rendering

**Current Status (PROD-01)**: 🌉 PROVIDER_BRIDGE_REQUIRED

**Planning Packet Structure**:
```json
{
  "packet_id": "PKT-video-plan-001",
  "packet_type": "video_planning_packet",
  "dossier_id": "DOSSIER-xxxxx",
  "generated_at": "2026-05-05T12:38:56Z",
  "video_specification": {
    "format": "MP4 H.264",
    "resolution": "1920x1080",
    "fps": 30,
    "duration_sec": 180,
    "bitrate_mbps": 8
  },
  "timeline": [
    {
      "start_sec": 0,
      "duration_sec": 15,
      "type": "image_sequence",
      "media_reference": "PKT-image-plan-001:sequence_1",
      "fade_in_sec": 0.5,
      "fade_out_sec": 0.5,
      "text_overlay": "AI Tools for Creators"
    },
    {
      "start_sec": 15,
      "duration_sec": 150,
      "type": "image_sequence",
      "media_reference": "PKT-image-plan-001:sequence_2",
      "narration_reference": "PKT-voice-plan-001",
      "background_music_reference": "PKT-music-plan-001:bgm_body",
      "subtitles": true,
      "text_overlays": ["Tool #1", "Tool #2", "Tool #3"]
    },
    {
      "start_sec": 165,
      "duration_sec": 15,
      "type": "image_sequence",
      "media_reference": "PKT-image-plan-001:outro",
      "fade_out_sec": 1,
      "text_overlay": "Subscribe for more AI tips"
    }
  ],
  "color_grading": "bright, vibrant, modern",
  "subtitles_language": "en_US",
  "provider_boundary": "provider_bridge_required",
  "estimated_cost_usd": 2.50,
  "estimated_generation_time_sec": 300,
  "no_actual_video_generated": true,
  "notes": "PROD-01 does not generate actual video files. This packet contains timeline and assembly instructions only."
}
```

**Workflow Path** (When Enabled):

```
WF-400 (Production Planning)
  ↓
  All sub-packets completed:
  ├─ PKT-image-001.json + image files (from WF-610)
  ├─ PKT-voice-001.json + narration.mp3 (from WF-620)
  └─ PKT-music-001.json + bgm.mp3 (from WF-630)
  ↓
WF-640 (Video Assembly Handler) [BLOCKED in PROD-01]
  ↓
  Call video rendering provider:
    - Send timeline specification
    - Send all media files
    - Send color grading, subtitles, overlays
  ↓
  Provider returns:
    - video_1920x1080_30fps.mp4 (180 sec, ~750 MB)
  ↓
PKT-video-001.json + final_video.mp4 (ACTUAL FILE)
```

**Providers & Costs** (PROD-02+):

| Provider | Cost Per Video | Speed | Quality | Notes |
|----------|---|---------|-------|-------|
| Runway ML | $0.50-2.00 | Slow (5-10 min) | Excellent | AI video magic |
| HeyGen | $1.00-3.00 | Medium (2-5 min) | Very Good | Avatar support |
| Synthesia | $1.50-5.00 | Medium (3-8 min) | Excellent | Avatar-focused |
| Descript | $0.50-1.50 | Fast (1-2 min) | Good | Simple assembly |

---

### Media Mode 5: Avatar Generation & Animation

**Current Status (PROD-01)**: 🌉 PROVIDER_BRIDGE_REQUIRED

**Planning Packet Structure**:
```json
{
  "packet_id": "PKT-avatar-plan-001",
  "packet_type": "avatar_planning_packet",
  "dossier_id": "DOSSIER-xxxxx",
  "generated_at": "2026-05-05T12:39:56Z",
  "avatar_specification": {
    "avatar_style": "realistic_business_professional",
    "gender": "female",
    "age_appearance": 28,
    "ethnicity": "diverse",
    "clothing": "professional_blazer_blue",
    "background": "modern_office_clean",
    "speaking_pace": "natural",
    "emotion_variation": true
  },
  "performance": {
    "script_reference": "PKT-script-001",
    "narration_reference": "PKT-voice-plan-001",
    "facial_expressions": "natural",
    "hand_gestures": true,
    "eye_contact": "camera",
    "blinking_frequency": "natural"
  },
  "video_output": {
    "format": "MP4 H.264",
    "resolution": "1920x1080",
    "fps": 30,
    "duration_sec": 180
  },
  "provider_boundary": "provider_bridge_required",
  "estimated_cost_usd": 3.50,
  "estimated_generation_time_sec": 600,
  "no_actual_video_generated": true,
  "notes": "PROD-01 does not generate actual avatar videos. This packet contains avatar specifications and performance directions only."
}
```

**Workflow Path** (When Enabled):

```
WF-400 (Production Planning)
  ↓
WF-650 (Avatar Generation Handler) [BLOCKED in PROD-01]
  ↓
  Call avatar provider:
    - Avatar style specification
    - Script text (or narration audio)
    - Performance directions (emotion, gestures)
  ↓
  Provider generates:
    - avatar_performance_video.mp4 (avatar speaking with script)
  ↓
  [May be used instead of or in addition to image-based video]
  ↓
PKT-avatar-001.json + avatar_video.mp4 (ACTUAL FILE)
```

**Providers & Costs** (PROD-02+):

| Provider | Cost Per Avatar | Quality | Speed | Notes |
|----------|---|---------|-------|-------|
| Synthesia | $1.50-3.00 | Excellent | Medium (3-8 min) | RECOMMENDED, avatar experts |
| D-ID | $0.50-2.00 | Good | Fast (2-5 min) | Facial animation |
| HeyGen | $1.00-3.00 | Very Good | Medium (3-8 min) | Natural speaking |
| Loom | $0.50-1.50 | Good | Fast (1-3 min) | Simple capture |

---

### Media Mode 6: Publishing & Distribution

**Current Status (PROD-01)**: ❌ NOT AVAILABLE

**Planning Packet Structure**:
```json
{
  "packet_id": "PKT-publish-plan-001",
  "packet_type": "publishing_plan_packet",
  "dossier_id": "DOSSIER-xxxxx",
  "generated_at": "2026-05-05T12:40:56Z",
  "publishing_targets": [
    {
      "platform": "youtube",
      "status": "pending_approval",
      "video_reference": "PKT-video-001",
      "metadata": {
        "title": "The 5 Best AI Tools for Content Creators in 2026",
        "description": "...",
        "keywords": ["AI", "content creators", "YouTube 2026"],
        "thumbnail": "PKT-image-001:sequence_1",
        "visibility": "public",
        "license": "creative_commons"
      },
      "scheduling": {
        "publish_date": "2026-05-10",
        "publish_time": "14:00:00Z",
        "premiere": false
      }
    }
  ],
  "provider_boundary": "provider_bridge_required",
  "estimated_cost_usd": 0.00,
  "notes": "Publishing requires YouTube API credentials and founder approval. No actual publishing happens in PROD-01."
}
```

**Workflow Path** (When Enabled):

```
WF-500 (Publishing Preparation)
  ↓
  All video assets ready and approved
  ↓
WF-660 (Publishing Handler) [BLOCKED in PROD-01]
  ↓
  For each publishing_targets:
    - Get platform credentials (YouTube API key)
    - Format video and metadata per platform specs
    - Upload video
    - Schedule publish date/time
    - Set description, keywords, thumbnail
  ↓
  YouTube API returns:
    - video_id: "dQw4w9WgXcQ"
    - url: "https://youtube.com/watch?v=dQw4w9WgXcQ"
  ↓
PKT-publish-001.json (with video_id, live_url, etc.)
```

**Credentials Required** (PROD-02+):
- YouTube Data API key
- Google OAuth consent screen
- Channel access authorization

**Cost**: Free (YouTube doesn't charge for uploading)

---

## PART 3: UNIFIED PROVIDER ENABLEMENT SEQUENCE (PROD-02 Timeline)

**When Provider Bridge Becomes Active** (estimated 4-6 weeks after PROD-01 launch):

### Step 1: Add Provider Credentials

```powershell
# Founder adds OpenAI credentials (first provider)
curl -X POST http://127.0.0.1:5050/operator/providers/add-credential `
  -Headers @{"Content-Type"="application/json"} `
  -Body (@{
    provider="openai"
    api_key="sk-proj-xxxxxxxxxxxxx"
    org_id="org-xxxxxxxxxxxxx"
    quota_monthly_usd=50.00
  } | ConvertTo-Json)

# Response:
# {
#   "status": "success",
#   "provider": "openai",
#   "verified": true,
#   "quota_allocated_usd": 50.00,
#   "quota_used_usd": 0.00,
#   "enabled": true
# }
```

### Step 2: Enable Provider Bridge

```powershell
# Founder explicitly enables provider bridge
curl -X POST http://127.0.0.1:5050/operator/modes/provider-bridge/enable `
  -Headers @{"Content-Type"="application/json"} `
  -Body (@{
    actor_mode="founder"
    providers_enabled=@("openai")
    accept_liability=true
  } | ConvertTo-Json)

# Response:
# {
#   "status": "success",
#   "provider_bridge_active": true,
#   "enabled_providers": ["openai"],
#   "safe_mode_auto_disable": true,  ← Safe Mode becomes optional
#   "cost_tracking_active": true
# }
```

### Step 3: Create New Dossier (Now with Real Media)

```powershell
# Creator creates dossier - system now triggers provider workflows
curl -X POST http://127.0.0.1:5050/operator/new-content-job `
  -Headers @{"Content-Type"="application/json"} `
  -Body (@{
    topic="AI tools for creators"
    context="YouTube video"
    mode="creator"
    include_media=true      # ← NEW: request real media generation
  } | ConvertTo-Json)

# Workflow changes:
# WF-001 → WF-010 → WF-100 → WF-200 → WF-300 → WF-400
#                                               ↓
#                                    ┌─ WF-610 (image gen)
#                                    ├─ WF-620 (voice gen)
#                                    ├─ WF-630 (music gen)
#                                    └─ WF-640 (video assembly)
#                                               ↓
#                                    WF-020 (approval) [locked until complete]

# Cycle time: 3-15 minutes (vs 2-5 minutes in PROD-01)
```

### Step 4: Monitor Provider Costs

```powershell
# Founder monitors provider usage
npm run cost:report

# Output shows:
# Provider       | Month | Used   | Quota  | $/dossier
# ────────────────────────────────────────────────────
# openai         | May   | $12.50 | $50.00 | $2.50
# (future: elevenlabs, midjourney, etc.)
```

### Step 5: Disable Provider (Rollback)

```powershell
# If costs exceed expectations or provider API fails:
curl -X POST http://127.0.0.1:5050/operator/providers/disable `
  -Headers @{"Content-Type"="application/json"} `
  -Body (@{provider="openai"} | ConvertTo-Json)

# Effect:
# - All subsequent dossiers revert to planning packets
# - In-flight dossiers complete with what they have
# - Cost tracking stops
# - Safe Mode becomes mandatory again
```

---

## PART 4: PROVIDER SELECTION GUIDE (PROD-02)

### For Image Generation

**Recommendation**: Start with DALL-E 3 (OpenAI)

**Why**:
- ✅ Excellent quality, consistent style
- ✅ Integrated with OpenAI account (unified billing)
- ✅ Reasonable cost ($0.12-0.20 per image)
- ✅ Good for startup (no additional signup)

**Fallback**: Midjourney (if DALL-E results insufficient)

**Cost Per Dossier**: ~$0.25 (2-3 images)

### For Voice Narration

**Recommendation**: ElevenLabs

**Why**:
- ✅ Highest quality voice synthesis
- ✅ Zero latency (instant, not async)
- ✅ Voice consistency (same voice across project)
- ✅ Reasonable cost (~$0.27 per dossier for 3-5 min audio)

**Setup**:
```powershell
# Add ElevenLabs credential
curl -X POST http://127.0.0.1:5050/operator/providers/add-credential `
  -Body (@{
    provider="elevenlabs"
    api_key="sk_xxxxx"
    voice_id="EXAVITQu4vr4xnSDxMaL"  # Rachel (professional)
  } | ConvertTo-Json)
```

**Cost Per Dossier**: ~$0.25

### For Background Music

**Recommendation**: Mubert (AI-native, fastest)

**Why**:
- ✅ Designed for AI content (understands mood tags)
- ✅ Fast generation (10-30 sec)
- ✅ Cheapest option ($0.01-0.05 per minute)
- ✅ Royalty-free

**Fallback**: Epidemic Sound (if branded music needed)

**Cost Per Dossier**: ~$0.08

### For Video Assembly

**Recommendation**: Runway ML (if budget allows) or Descript (budget option)

**Why (Runway)**:
- ✅ AI-native (understands temporal aspects)
- ✅ Excellent quality (professional color grading, effects)
- ✅ Slower but results worth it

**Why (Descript)** (if cost-conscious):
- ✅ Fastest assembly (1-2 min)
- ✅ Cheapest ($0.50-1.50 per video)
- ✅ Adequate quality for YouTube

**Cost Per Dossier**: $0.50-2.00

### For Avatar (Optional Enhancement)

**Recommendation**: Synthesia (industry standard)

**Why**:
- ✅ Most realistic avatars
- ✅ Natural speaking patterns
- ✅ Professional appearance
- ✅ Supports multiple languages

**Usage**: Instead of image sequences, use avatar as narrator

**Cost Per Dossier**: +$1.50-3.00 (replaces image generation)

### For Publishing

**No Cost**: YouTube (requires API key only)

**Setup**:
```powershell
# Founder creates YouTube Data API key via Google Cloud Console
# Store in environment as YOUTUBE_API_KEY
# System auto-publishes on approval
```

---

## PART 5: COST MODEL (PROD-02+)

### Cost Per Dossier (Full Production)

| Component | Provider | Unit Cost | Cost/Dossier |
|-----------|----------|-----------|--------------|
| Research | (text, local) | — | $0.00 |
| Script | (text, local) | — | $0.00 |
| Metadata | (JSON, local) | — | $0.00 |
| Images | DALL-E 3 | $0.12/image | $0.25 (2-3 images) |
| Voice | ElevenLabs | $0.008/1K chars | $0.25 (500 chars) |
| Music | Mubert | $0.02/minute | $0.10 (5 min) |
| Video | Descript | $0.50-1.50/video | $0.75 |
| **TOTAL** | | | **~$1.35** |

### Cost Optimization

**Recommendation for Startups**:
- Month 1: Text only (research + script) = $0/dossier
- Month 2: Add images = +$0.25/dossier
- Month 3: Add voice = +$0.25/dossier
- Month 4: Add video = +$0.75/dossier
- Month 5+: Full production = $1.35/dossier

**Monthly Cost at Scale**:
- 10 dossiers/day = $40.50/month (10 images only)
- 10 dossiers/day = $200/month (full production)

---

## PART 6: SAFETY & AUDIT DURING PROVIDER PHASE

### Cost Overrun Prevention

```powershell
# Founder sets monthly quota
curl -X POST http://127.0.0.1:5050/operator/providers/set-quota `
  -Body (@{
    provider="openai"
    monthly_budget_usd=100.00
    alert_at_percent=75
  } | ConvertTo-Json)

# System alerts when 75% ($75) is spent
# System BLOCKS new dossiers at 100% to prevent overage
```

### Audit Trail During Provider Execution

**Every Provider Call Logged**:
```json
{
  "audit_entry": {
    "timestamp": "2026-05-05T12:35:00Z",
    "dossier_id": "DOSSIER-xxxxx",
    "workflow": "WF-610",
    "action": "image_generation_called",
    "provider": "openai",
    "prompt": "[image prompt text]",
    "cost_usd": 0.12,
    "result": "success",
    "api_response_time_ms": 45000,
    "image_url": "https://oaidalleapiprodscus.blob.core.windows.net/..."
  }
}
```

### Cost Reversal & Reconciliation

```powershell
# If provider API charged incorrectly:
curl -X POST http://127.0.0.1:5050/operator/audit/cost-reversal `
  -Body (@{
    dossier_id="DOSSIER-xxxxx"
    audit_entry_id="AUDIT-123"
    reason="Provider double-charged"
  } | ConvertTo-Json)

# System:
# 1. Marks cost as disputed
# 2. Creates credit entry
# 3. Logs in audit trail
# 4. Founder must verify manual refund from provider
```

---

## PART 7: MIGRATION PATH: PROD-01 → PROD-02 → PROD-03

### Timeline

```
May 5, 2026 (Today)
  ↓ PROD-01 Live (text only, safe)
  ↓ Operator runs daily; gather feedback
  ↓
May 19, 2026 (2 weeks)
  ↓ Stability check; approve PROD-02 start
  ↓
June 2, 2026 (4 weeks)
  ↓ PROD-02 Launch: Add provider bridge
  ↓ Image generation enabled (DALL-E 3)
  ↓
June 16, 2026 (5 weeks)
  ↓ Voice + Music generation enabled
  ↓
June 30, 2026 (8 weeks)
  ↓ Video assembly enabled
  ↓
July 14, 2026 (10 weeks)
  ↓ PROD-03 Foundation: Avatar + Publishing
  ↓ Multi-platform distribution (YouTube, LinkedIn, TikTok)
  ↓
August 31, 2026 (4 months)
  ↓ PROD-03 Live: Full end-to-end automation
  ↓ Content → YouTube (via publishing API)
  ↓
```

### Data Migration Checklist

When moving from PROD-01 → PROD-02:
```
✅ Backup all dossiers (C:\...\dossiers\)
✅ Export metrics (npm run metrics:weekly)
✅ Document any custom registries or scripts
✅ Test PROD-02 startup sequence
✅ Verify provider credentials are correct
✅ Set conservative cost quotas first
✅ Start with 1-2 dossiers to test providers
✅ Monitor first week closely
```

---

## SUMMARY: What's NOT Available in PROD-01

| Feature | PROD-01 | PROD-02 | PROD-03 |
|---------|---------|---------|---------|
| Text research | ✅ | ✅ | ✅ |
| Script generation | ✅ | ✅ | ✅ |
| Image generation | 📋 Planning | ✅ | ✅ |
| Voice narration | 📋 Planning | ✅ | ✅ |
| Background music | 📋 Planning | ✅ | ✅ |
| Video assembly | 📋 Planning | ✅ | ✅ |
| Avatar rendering | 📋 Planning | ⏳ | ✅ |
| YouTube publishing | ❌ | ⏳ | ✅ |
| Multi-platform publish | ❌ | ❌ | ✅ |
| Cost tracking | ❌ | ✅ | ✅ |
| User auth & RBAC | ❌ | ✅ | ✅ |
| Team collaboration | ❌ | ❌ | ✅ |

---

**Status**: ✅ PROD-03 ROADMAP DEFINED  
**Provider Bridge**: 🌉 DOCUMENTED AND ENFORCED  
**Media Modes**: All 6 planned, specifications complete  
**Timeline**: 4-6 months to full automation  
**Safety**: Audit trail, cost controls, credential management

**Critical Note**: PROD-01 creates ZERO real media files. All media modes are provider_bridge_required until explicitly enabled in PROD-02.

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

## Provider Bridge Execution Must Wait for Runtime Profile Verification

Provider/media execution is blocked until:

- n8n profile is confirmed Restore_01.
- 37 canonical workflows are active.
- WF-000 passes.
- WF-001 -> WF-010 smoke passes.
- provider registry is verified.
- no stale workflow IDs are used.

Do not run image generation, voice generation, avatar generation, video generation, YouTube upload, or analytics pull until core runtime profile is confirmed.
