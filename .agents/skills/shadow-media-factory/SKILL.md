---
name: shadow-media-factory
description: "Automatically use this skill whenever a storyboard, B-roll plan, scene prompt, visual plan, image prompt packet, video prompt packet, pacing metadata, local engine handoff, local media generation, or Media Factory output is requested. Requires SHADOW_BOOT_CONFIRMATION, MEDIA_FACTORY_HANDOFF route lock, visual DNA fields, scene sync matrix, scene prompt packets, video motion prompts, storyboard export plan, local engine bridge status, and provider honesty gate."
---

# Shadow Media Factory

Use this skill when:

- storyboard is requested
- B-roll planning or scene prompt packets are requested
- image prompt packets or video motion prompts are requested
- pacing metadata or frame-by-frame breakdown is requested
- local engine handoff (ComfyUI, AnimateDiff, FFmpeg, DaVinci Resolve) is requested
- visual plan, cinematic plan, or shot list with prompts is requested
- Media Factory final draft is requested
- local render packet or render metadata is requested

## Required Route

Classify task as `MEDIA_FACTORY_HANDOFF` before output.
Load `registries/route_manifests/media_factory_handoff.yaml` before generating any output.
Load `registries/local_media_factory_bridge.yaml` and
`runtime_contracts/LOCAL_MEDIA_FACTORY_BRIDGE_CONTRACT.md` before local engine
handoff, control panel routing, storyboard render planning, or artifact claims.
Consume mandatory directors: Maya, Vishwakarma, Nataraja, Brahma, Varuna.
Apply `MEDIA_FACTORY_SYNC_LOCK` before scene output.

## Required Media Factory Output

For every Media Factory task, output:

- SCENE_SYNC_MATRIX — one scene_row_json per scene with all nine alignment dimensions
- SCENE_PROMPT_PACKETS — per-scene image prompt with all 15 visual DNA fields:
  - subject, environment, camera_framing, lens_focal_logic, lighting_setup
  - emotional_tone, color_palette, cinematic_delivery_standard (Rec.709)
  - style_lock, movement_intent, negative_prompt, drift_prevention
  - continuity_constraints, brand_persona_consistency, safety_real_person_handling
  - tool_targets, tool_specific_translation_readiness
- VIDEO_PROMPT_PACKETS — per-scene video prompt with camera_movement_type, frame_rate, aspect_ratio,
  animation_style_classification, cinematic_delivery_standard (Rec.709),
  local_tool_targets, controlnet_guidance_types
- STORYBOARD_EXPORT_PLAN — folder path, naming convention (shot<N>_<scene_id>_<descriptor>.png),
  pacing metadata JSON path, exact filename references
- LOCAL_MEDIA_FACTORY_BRIDGE_STATUS — readiness status per engine per lane
  (DESIGNED / STUB / PACKET_READY / LOCAL_ENGINE_READY / EXECUTABLE / BLOCKED / NEEDS_CONFIRMATION)
  and the active bridge registry path when local execution is relevant
- PROVIDER_HONESTY_GATE — explicit status for providers_called, n8n_used,
  local_media_generation_engine_used, media_artifacts_claimed, provider_execution_allowed
- LOCAL_CLOUD_HYBRID_EXECUTION_PLAN — per-lane options for voice, image, video, music_sfx, editing, packaging
- MEDIA_FACTORY_EVIDENCE_GATE — for any claimed artifact: file_path, generation_method, engine_used,
  source_prompt_packet_ref, validation_result, human_review_status
- CONTROL_PANEL_PREFLIGHT_GATE — for renderable storyboard/B-roll requests:
  requested controls, available controls, route downgrade status,
  output_classification, production_pass_allowed, safe_to_batch_automate

## Visual DNA Compliance

Every image prompt must include all 15 visual DNA fields as defined in:
`runtime_contracts/MEDIA_FACTORY_FINAL_DRAFT_CONTRACT.md`

A prompt missing any DNA field cannot reach PASS status.

## Tool Translation Readiness

Every prompt must be translatable to:
- ComfyUI / SDXL / Flux — requires style_lock, negative_prompt, lighting_setup, color_palette, camera_framing
- AnimateDiff — requires movement_intent, camera_movement_type, motion_intensity, frame_rate
- FFmpeg assembly — requires scene_id, duration_seconds, transition_out, sync_point_to_beat_map
- DaVinci Resolve — requires scene_id, timestamp, color_palette, cinematic_delivery_standard

## Cinematic Delivery Standard

Default delivery standard for all visual and video prompts is Rec.709 unless
the user explicitly requests HDR or an alternate color space.

## Real-Person Safety

When a real person is referenced in any visual scene:

- Do not generate photorealistic face prompts
- Use one of: use_side_profile | use_silhouette | use_shadow | use_animated_inspired
- Set safety_real_person_handling in every scene prompt that depicts the person

## Storyboard Export Standard

- Naming: `shot<N>_<scene_id>_<descriptor>.png`
- Default local Mac path: `/Users/apple/Downloads/b_roll_storyboard/`
- Mission path: `outputs/missions/<mission_id>/storyboard/`
- JSON pacing metadata must contain exact image filenames
- TXT notepad must mirror the JSON for human readability

## Permanent Local Bridge

Active local Media Factory root:

```text
/Users/apple/ShadowMediaFactory
```

Active control panel CLI:

```text
python3 /Users/apple/ShadowMediaFactory/control_panel/bin/shadow_factory_ctl.py
```

The repo-side source of truth is:

```text
registries/local_media_factory_bridge.yaml
runtime_contracts/LOCAL_MEDIA_FACTORY_BRIDGE_CONTRACT.md
```

Current lane truth:

- SD1.5 + Canny + AnimateDiff is an `animated_storyboard` / animatic lane.
- Wan2.2 5B is technical/experimental until visual quality proof upgrades it.
- FFmpeg is assembly/export.
- DaVinci Resolve is manual finishing/QC.
- Production cinematic B-roll is not locally proven until proof says otherwise.

## Forbidden Behavior

- Do not output scene prompts without the 15 visual DNA fields.
- Do not claim media artifacts were generated without file_path and evidence.
- Do not call an `animated_storyboard` lane production cinematic B-roll.
- Do not silently downgrade requested OpenPose, Depth, Lineart, IPAdapter, true camera motion, or audio requirements.
- Do not set providers_called=true unless a provider was actually called.
- Do not set local_media_generation_engine_used=true unless local engine produced output.
- Do not hard-lock beat timing to a uniform 15-second grid.
- Do not omit LOCAL_MEDIA_FACTORY_BRIDGE_STATUS when local engine execution is planned.
- Do not omit PROVIDER_HONESTY_GATE from any Media Factory output.
- Do not use real-person photorealistic face generation.
- Do not call a storyboard complete if exact filenames are not in the pacing metadata JSON.

## Proof Implications

```text
PASS: all visual DNA fields present per scene, SCENE_SYNC_MATRIX emits scene_row_json per scene,
LOCAL_MEDIA_FACTORY_BRIDGE_STATUS declared per lane, PROVIDER_HONESTY_GATE explicit and honest.

PARTIAL: prompt packets present but one or more DNA fields missing, or storyboard plan present
but images not yet generated, or local engine readiness is DESIGNED/STUB but disclosed.

BLOCKED: media artifact claimed without evidence block, or provider/local engine execution claimed
without approval and render metadata.

FAIL: fake provider execution claims, fake PASS on incomplete evidence, real-person face generation.
```
