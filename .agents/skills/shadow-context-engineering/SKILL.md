---
name: shadow-context-engineering
description: "Automatically use this skill whenever a script, video, audio, image, music, media, voiceover, provider handoff, or context packet is requested. Requires SHADOW_BOOT_CONFIRMATION, timed beat map, voice context, image prompts, video prompts, music/SFX, editing plan, platform packaging, and provider boundary."
---

# Shadow Context Engineering

Use this skill when:

- script is requested
- video/audio/image/music/media output is implied
- provider handoff is requested
- context packet is requested

## Required Context Engineering Output

For script/video/content tasks, output:

- voice direction
- emotion map
- visual beat map
- facial expression direction
- gesture/body movement direction
- image prompts
- video prompts
- music/SFX cues
- editing plan
- captions/on-screen text
- provider handoff boundary
- cinematic short story block for every 3-10 minute YouTube script
- story visual scenes, emotional peak, and bridge back to the teaching section
- dynamic 3-20 second beat blocks with duration reasons
- scene sync matrix for final Media Factory drafts
- local/cloud/hybrid execution plan with fallback paths
- recurring re-hook scenes marked as synchronized pattern interrupts across
  voice, image, video, music/SFX, editing, platform, influence, and execution

For Media Factory final drafts, additionally output:

- SCENE_PROMPT_PACKETS with all 15 visual DNA fields per scene:
  subject, environment, camera_framing, lens_focal_logic, lighting_setup,
  emotional_tone, color_palette, cinematic_delivery_standard (Rec.709),
  style_lock, movement_intent, negative_prompt, drift_prevention,
  continuity_constraints, brand_persona_consistency, safety_real_person_handling,
  tool_targets, tool_specific_translation_readiness
- VIDEO_PROMPT_PACKETS with camera_movement_type, frame_rate, aspect_ratio,
  animation_style_classification, cinematic_delivery_standard, local_tool_targets,
  controlnet_guidance_types per scene
- STORYBOARD_EXPORT_PLAN with folder path, naming convention, exact filename
  references in pacing metadata JSON
- LOCAL_MEDIA_FACTORY_BRIDGE_STATUS per engine per lane using readiness labels:
  DESIGNED / STUB / PACKET_READY / LOCAL_ENGINE_READY / EXECUTABLE / BLOCKED / NEEDS_CONFIRMATION
- MEDIA_FACTORY_EVIDENCE_GATE with providers_called, n8n_used,
  local_media_generation_engine_used, media_artifacts_claimed declarations
- Load `registries/local_media_factory_bridge.yaml` and
  `runtime_contracts/LOCAL_MEDIA_FACTORY_BRIDGE_CONTRACT.md` before claiming
  local engine paths, control panel command readiness, or Media Factory
  artifact evidence.
- For every claimed artifact: file_path, generation_method, engine_or_provider_used,
  source_prompt_packet_ref, validation_result, human_review_status

Do not call media providers. Do not claim generated media. This skill creates context and handoff instructions only.

## Forbidden Behavior

- Do not stop at script-only output unless the user explicitly requests script-only.
- Do not claim voice/image/video/music artifacts were generated.
- Do not omit provider handoff boundary.
- Do not omit the mandatory cinematic story block for a 3-10 minute YouTube
  script.
- Do not hard-lock a timed beat map to uniform 15-second intervals without
  justification.
- Do not call a Media Factory final draft complete when voice, image, video,
  music/SFX, editing, platform, and influence rows are disconnected.
- Do not omit stronger camera, caption, edit, and music/SFX treatment at
  recurring re-hook moments.

## Proof Implications

- `PASS`: all context engineering sections are present with provider boundary.
- `PARTIAL`: script exists but one or more context engineering sections are missing.
- `FAIL`: false media execution claims or provider execution without approval.
