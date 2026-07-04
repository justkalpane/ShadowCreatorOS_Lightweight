---
name: shadow-content-orchestration
description: "Automatically use this skill whenever content, script, YouTube, Shorts, social repurposing, visual media planning, storyboard, Media Factory context, or provider handoff planning is requested. Requires repo-first routing, content engineering gates, source honesty, recurring hook density, and explicit provider boundaries."
---

# Shadow Content Orchestration

Use this skill when:

- a script, YouTube script, Short, Reel, TikTok, LinkedIn, Instagram, or X content request is made
- the task asks for content strategy, script strategy, hook writing, story shaping, retention planning, or line-by-line influence
- a content output needs voice, image, video, music/SFX, editing, platform packaging, or Media Factory handoff context
- the task transitions from approved script to visual media plan or storyboard

## Required Routing

Before output, classify through:

- `runtime_contracts/TASK_INTENT_ROUTING_CONTRACT.md`
- `registries/task_intent_routing_matrix.yaml`

For script/content tasks, load the selected route manifest and consume:

- `runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md`
- `runtime_contracts/SCRIPT_QUALITY_ENFORCEMENT_CONTRACT.md`
- `runtime_contracts/SOURCE_AWARE_RUNTIME_DECISION_PROTOCOL.md`
- `runtime_contracts/SCRIPT_LANGUAGE_CONTROL_CONTRACT.md`
- `runtime_contracts/REAL_TIME_RESEARCH_ENFORCEMENT_CONTRACT.md`
- `runtime_contracts/SOURCE_QUALITY_CLASSIFICATION_CONTRACT.md`
- `runtime_contracts/SCRIPT_STORY_ENGINE_CONTRACT.md`
- `runtime_contracts/DYNAMIC_TIMED_BEAT_MAP_CONTRACT.md`

For a plain script request, default `task_mode=script_only` and generate the
script before any visual/media route expansion. Do not load Media Factory
contracts, old mission outputs, or chat transcripts before `FINAL_SCRIPT`
unless the user explicitly asks for visual media planning, a generator draft,
a Media Factory handoff, continuation of a previous mission, or drift audit.

For visual media planning, generator drafts, or full content packets, also
consume:

- `runtime_contracts/MEDIA_FACTORY_FINAL_DRAFT_CONTRACT.md`
- `runtime_contracts/LOCAL_CLOUD_HYBRID_MEDIA_EXECUTION_CONTRACT.md`

If the task requests storyboard, B-roll, visual plan, scene prompts, local engine handoff, or Media Factory output, also activate:

- `.agents/skills/shadow-media-factory/SKILL.md`
- `registries/route_manifests/media_factory_handoff.yaml`
- `registries/local_media_factory_bridge.yaml`
- `runtime_contracts/LOCAL_MEDIA_FACTORY_BRIDGE_CONTRACT.md`

## Mandatory Script Behavior Laws

- The first master script must be English unless the user explicitly requests another language or translation/localization.
- Translation/localization is a separate downstream stage.
- Real-person, real-incident, brand, company, factual case study, career claim, or biographical proof requires source-quality classification and a fact-versus-anecdote map.
- Named public figures or known real-world identities default to real-person
  proof. Do not silently downgrade them to a composite or mythology anchor
  unless the user explicitly requests fictionalization.
- In real-person scripts, every fact-like spoken line must align to
  `SOURCE_LEDGER` or `FACT_VS_ANECDOTE_MAP`. Do not let a nearby source justify
  a stronger rewritten claim.
- Unsupported biographical absolutes such as `every`, `always`, `never`,
  `only`, or `zero shortcuts` must be downgraded to safer language unless the
  exact strength is source-backed.
- Do not claim real-time research unless sources were actually used and listed.
- Every 3-10 minute YouTube script requires a 45-75 second cinematic short story unless the user explicitly disables it.
- `HOOK_VARIANTS` chooses the opening hook only.
- Every 3-10 minute YouTube script requires recurring re-hooks by default every 70-90 seconds, dynamically adjusted with a reason.
- A 5-minute script requires at least three internal re-hooks plus a CTA hook unless a format-specific exception is justified.
- Timed beat maps are dynamic; do not hard-lock to uniform 15-second blocks without production reason.
- Script-only output is `PARTIAL` unless the user explicitly asked for script-only.
- Final proof status must match the weakest gate.
- Manifest proxy binding is not enough for mandatory script-generation
  directors, agents, subagents, skills, or subskills. Mandatory route actors
  must be individually opened before output.
- In `CHAT_ONLY_MODE`, keep the spoken script central. Present `FINAL_SCRIPT`
  before downstream media-context blocks unless the user explicitly requests a
  deep operator or dossier format.
- Do not insert off-topic teaser, promo, or cross-sell lines into the spoken
  script unless the user explicitly requested them.
- If `cinematic_reconstruction=true` for a real person, disclose which details
  are verified and which are dramatized for continuity.

## Media Factory Delegation

When content becomes a visual media plan or Media Factory draft, delegate tool-specific behavior to the registered Media Factory stack:

- `SS-101` ElevenLabs voice generation optimizer: voice settings, delivery tone, pauses, emotion, pronunciation notes.
- `SS-102` HeyGen avatar render orchestrator: A-roll batches, avatar framing, chromakey/overlay constraints.
- `SS-112` FFmpeg render assembly guard: assembly checks, audio/video sync, render guardrails.
- `SS-116` NotebookLM Visual Style Orchestrator: NotebookLM-style dual-panel source shelf and active note scenes rendered through HyperFrames.
- `SS-117` Depth Anything V2 Depth Map Generator: depth-mask-only local engine for DaVinci Fusion 2.5D parallax.
- `SS-118` HyperFrames HTML Renderer: deterministic HTML/CSS/GSAP slides, kinetic text, data cards, and WebM alpha overlays.

Do not create a new tool subskill when an existing subskill covers the tool role. Add a new subskill only when no existing active subskill can own the behavior.

## Visual Method Assignment Law

For Media Factory outputs, use exact method-to-tool assignment:

- `NOTEBOOKLM_VISUAL_METHOD` -> HyperFrames CLI through SS-116/SS-118.
- `PROGRAMMATIC_SLIDE_VISUAL_METHOD` -> HyperFrames CLI through SS-118.
- `HTML_CSS_GSAP_VISUAL_METHOD` -> HyperFrames CLI through SS-118.
- `A_ROLL_OVERLAY_METHOD` -> HeyGen chromakey foreground + HyperFrames WebM alpha or MP4 background + DaVinci Resolve composite.
- `IMAGE_MOTION_GRAPHICS_BROLL_METHOD` -> still image + Depth Anything V2 mask + DaVinci Resolve Fusion parallax.
- `CINEMATIC_BROLL_VIDEO` -> cloud/premium video provider or future proven cinematic local lane; local animatic lanes must not be called production cinematic B-roll.
- `A_ROLL_AVATAR` -> HeyGen or approved avatar provider.
- Final assembly, color grade, J/L cuts, and manual finishing -> DaVinci Resolve; FFmpeg is assembly/export support, not a creative replacement.

HyperFrames is kept. Depth Anything V2 is a masking tool only. Neither replaces DaVinci final assembly.

## Visual Media Plan Minimums

For a 3-10 minute visual media plan:

- Cinematic B-roll Video must be at least 12% of total runtime.
- Every storyboard scene must use the locked multi-arc table format with 10 production columns plus the Reasoning column.
- Every scene must include ElevenLabs settings when voice is present: Stability, Similarity, Style, Speaker Boost.
- Every scene must include `SFX_TIMELINE_METHOD` with exact relative timestamps and dB levels.
- Every scene must include Color Grade and Safe Zone entries.
- Re-hooks must appear in the script, dynamic beat map, editing context, line-by-line influence map, and scene sync matrix when final Media Factory draft is requested.
- If the output claims production-ready Media Factory context instead of light
  media hints, escalate to `SCENE_SYNC_MATRIX` and synchronized packet-level
  planning.

## Required Output Blocks

For content/script tasks:

- `SHADOW_BOOT_CONFIRMATION`
- `TASK_ROUTE_LOCK`
- `CONSUMPTION_LOCK`
- `SCRIPT_LANGUAGE_DECLARATION`
- `RESEARCH_AND_SOURCE_STATUS`
- `SOURCE_LEDGER`
- `FACT_VS_ANECDOTE_MAP`
- `HOOK_VARIANTS`
- `SELECTED_OPENING_HOOK`
- `RECURRING_REHOOK_MAP`
- `CINEMATIC_SHORT_STORY_BLOCK`
- `FINAL_SCRIPT_IN_ENGLISH`
- `DYNAMIC_TIMED_BEAT_MAP`
- `VOICE_GENERATION_CONTEXT`
- `IMAGE_GENERATION_CONTEXT`
- `VIDEO_GENERATION_CONTEXT`
- `MUSIC_AND_SFX_CONTEXT`
- `EDITING_CONTEXT`
- `PLATFORM_PACKAGING`
- `LINE_BY_LINE_INFLUENCE_MAP`
- `LOCAL_CLOUD_HYBRID_EXECUTION_PLAN`
- `PROVIDER_HANDOFF_BOUNDARY`
- `FINAL_PROOF_CLASSIFICATION`

For Media Factory plans, use the output contract in `.agents/skills/shadow-media-factory/SKILL.md`.

## Provider Boundary

Default behavior is planning-only.

- `n8n_used=false`
- `providers_called=false`
- `media_artifacts_claimed=false`
- `provider_execution_allowed=false`
- `local_media_generation_engine_used=false` unless a local engine actually ran and proof files exist

Do not claim generated media or local execution without artifact paths and proof JSON.

## PASS / PARTIAL / BLOCKED

```text
PASS: route selected, required contracts consumed, source/status gates honest, story/re-hook/timing/media context complete, and final proof matches weakest gate.

PARTIAL: script-only output without explicit script-only request, missing source sufficiency, light media context for a production draft, bridge sync stale, or route actor propagation incomplete.

BLOCKED: provider/media execution requested without approval, missing AGENTS boot confirmation, missing route manifest, or media artifact claimed without proof.
```


MAC-06.2O ROUTE FAMILY PROPAGATION
route_families: [full_video_pipeline]
route_family_resolved: [full_video_pipeline]
