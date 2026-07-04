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

Batch 4 runtime binding is required before any PASS-like handoff claim:

- `schemas/runtime_state/evidence_bundle.schema.json`
- `schemas/runtime_state/route_state_capsule.schema.json`
- `schemas/media_factory/bridge_job_packet.schema.json`
- `schemas/media_factory/visual_media_plan_row.schema.json`
- `schemas/media_factory/final_visual_media_generation_draft.schema.json`
- `validators/validate_evidence_bundle.py`
- `validators/validate_route_state_capsule.py`
- `validators/validate_bridge_job_packet.py`
- `validators/validate_visual_media_plan_row.py`
- `validators/validate_final_visual_media_generation_draft.py`

If local-handoff-ready depth is requested, also bind:

- `validators/validate_depth_map_packet.py`
- `validators/validate_ffmpeg_filtergraph_packet.py`
- `validators/validate_hyperframes_payload.py`
- `validators/validate_comfyui_payload.py`
- `validators/validate_source_vs_render_packet.py`
- `validators/validate_visual_qa_acceptance.py`
- `validators/validate_pilot_cut_validation_packet.py`
- `validators/validate_audio_authorization_packet.py`
- `validators/validate_davinci_handoff_packet.py`

Do not treat file existence, route prose, or contract headings as sufficient
handoff proof. Media-factory route claims require `route_state_capsule`,
`evidence_bundle`, and `bridge_job_packet` readiness.

## Required Media Factory Output

Depending on the depth mode requested:

### Mode A: Visual Media Plan (Planning-Only Phase)
If a "Visual Media Plan", "Visual Plan", or "Storyboard Plan" is requested (prior to rendering approval):
- Keep the stage in chat-only planning mode unless repo-write has been
  explicitly approved for this exact stage. Do not create `implementation_plan.md`,
  `task.md`, folders, `.docx`, `.txt`, `.json`, prompt packets, or media files
  during a visual media plan. Any file/folder creation before approval is a
  hard failure.
- Present the detailed, written storyboard layout containing scene-by-scene tables detailing:
  - Media Type & Visual Method (e.g. `A_ROLL_AVATAR`, `A_ROLL_OVERLAY_METHOD`, `NOTEBOOKLM_VISUAL_METHOD`, `PROGRAMMATIC_SLIDE_VISUAL_METHOD`, `HTML_CSS_GSAP_VISUAL_METHOD`, `HYPERFRAME_VISUAL_METHOD`, `IMAGE_MOTION_GRAPHICS_BROLL_METHOD`, or `CINEMATIC_BROLL_VIDEO`)
  - Shot Framing / Setup (Visual description, shot type, environment, safety profile, overlay layouts)
  - Camera Motion / Technique (Ken Burns zoom/pan, dolly, tracking, and **HYPERFRAME_VISUAL_METHOD** detailing 3D parallax layer depth separation via DaVinci Fusion, visual highlights, glow maps, particle layers, lens flares, or depth-of-field blurring based on script lines)
  - Voice (ElevenLabs Settings: stability, similarity, style exaggeration, speaker boost)
  - Music & SFX (Detailed Suno prompts, Suno SFX cues, and **SFX_TIMELINE_METHOD** detailing precision audio timestamps and volume curves synchronized to visuals or speech)
  - Captions (Style, keywords, positioning, kinetic typography)
  - Editing (Nataraja) & Transitions (Cuts, speed shifts, J-cuts and L-cuts with precise offsets in seconds, and **FFMPEG_TRANSITION_METHOD** transition cuts between every photo—whip pans, zoom cuts, glitch wipes)
  - Color Grade (Maya) (Palette, temperature, film grain, continuity)
  - Safe Zone (Platform margins and watch-bar safe coordinates)
- **Image+Motion Graphics Pacing & Hyperframe Rule**: The number of images generated for image-based B-roll segments must scale based on duration and narrative density.
  - Scale image count: 1 image per 2-5 seconds for rapid lists/emphasis, or 1 image with continuous Ken Burns pan.
  - Layer **HYPERFRAME_VISUAL_METHOD** (DaVinci Fusion 2.5D layer animations, DaVinci particle effects, or speed lines) over still images to simulate high-end editing pacing at low cost.
  - Explicitly define the Image Count, the **Transition/Hyperframe FX**, and **Transition Audio** for every image.
- **NOTEBOOKLM_VISUAL_METHOD Rule**:
  - For explanation scenes, note lists, and document summaries, utilize the NotebookLM-style visual method.
  - Define the sources panel on the left and the active note highlights with glowing border overlays on the right.
  - These slides are rendered locally in headless Chrome via HyperFrames CLI at zero cost.
  - **Asset & Render Specification Enforcement (Visual Planning Phase)**:
    - While drafting NotebookLM scenes, the planner MUST explicitly define the asset structure and rendering draft block to prevent engine drift:
      1. *Asset Inventory*: Itemize required files (e.g. `brand_logo.svg`, custom page preview PNGs, or background canvas textures). If no external visual files are needed, explicitly state `assets_needed=NONE (CSS vectors only)`.
      2. *Rendering Draft (HyperFrames Config)*: Specify font family (e.g. Inter/Outfit), background color theme, typing animation velocity, scroll triggers, highlight opacity, and GSAP sync timeline details.
      3. *DaVinci Composite Method*: Detail that the slides are rendered as a clean background MP4, with talking-head HeyGen presenter clips overlaid on track V2 and chromakeyed inside DaVinci Resolve.

- **PROGRAMMATIC_SLIDE_VISUAL_METHOD & HTML_CSS_GSAP_VISUAL_METHOD Rule**:
  - For explanation scenes, listicle blocks, data displays, and learning points, utilize programmatic HTML/CSS templates.
  - Define the layout card style, font colors, kinetic text string, scroll rate, and animation timeline in the shot framing column.
  - These slides are rendered locally in headless Chrome at zero cost.
- **Narrative Transition & Ratio Target Law**:
  - Whenever a backstory, real-person anecdote, or backdrop is introduced (including within segments that would otherwise be talking-head A-roll), the presenter avatar must fade or cut away in favor of `NOTEBOOKLM_VISUAL_METHOD`, `PROGRAMMATIC_SLIDE_VISUAL_METHOD`, `HYPERFRAME_VISUAL_METHOD` overlays, or `CINEMATIC_BROLL_VIDEO`.
  - The plan must target the following cost-efficient production ratios:
    - **A-Roll (HeyGen Presenter / Avatars)**: ~40% of total runtime.
    - **Image+Motion Graphics, Programmatic Slides & NotebookLM Slides (Low Cost)**: ~48% of total runtime.
    - **Cinematic B-Roll Video (Cloud/Premium)**: At least 12% of total runtime (principally allocated to the short story/establishing blocks).
- Provide the **COMPLETE A-ROLL vs B-ROLL vs MOTION GRAPHIC SUMMARY Table** including the `Image Count` column.
- Provide the **Cost Distribution Result** calculating durations and percentages for A-Roll, Motion Graphic Images, and B-Roll Video to verify B-Roll cost minimization and ratio targets.
- Provide readable one-scene-per-table vertical breakout blocks. A giant merged
  table may exist as a summary only; it cannot replace the vertical scene
  breakouts.
- Provide the **PRODUCTION_ORDER_LOCK**, **ASSET_INVENTORY_LEDGER**, **ASSET_DEPENDENCY_GRAPH**, **CONTROL_PANEL_EXECUTION_PLAN**, **DAVINCI_TIMELINE_PACKET**, and **PRODUCTION_PROOF_GATE**. A corrected storyboard without these blocks is a visual plan draft, not a production-ready generation plan.
- Treat the master ElevenLabs voice track as the default timeline anchor. The generation order must be: approved script and scene IDs -> scene sync matrix -> master voice -> timestamp alignment -> music segments -> individual SFX clips -> character/reference assets -> storyboard/still assets -> HyperFrames renders -> Depth Anything V2 maps -> HeyGen A-roll batches -> premium cinematic B-roll -> DaVinci assembly -> QC/export -> proofs/registry update.
- Do not leave the production order as prose only. For production-grade outputs,
  emit one `production_phase_row_json=` row per phase and keep the row order
  identical to the canonical generation chain.
- Separate asset counts by class. Do not report `Still Images Required` as the total visual asset count unless it includes storyboard stills, depth-parallax stills, HyperFrames assets, overlays, thumbnails, and character/reference assets. If only DA-V2 stills are counted, label them `depth_parallax_stills_only`.
- **MEDIA FACTORY TOOL ASSIGNMENT LAW:**
  - `NOTEBOOKLM_VISUAL_METHOD`, `PROGRAMMATIC_SLIDE`, Data Cards, Kinetic Text -> **HyperFrames CLI**
  - WebM Alpha overlays (e.g. promo/CTA particle card) -> **HyperFrames CLI**
  - 2.5D Parallax on Still Images -> **DaVinci Resolve Fusion + Depth Anything V2 (masking)**
  - Ken Burns (Pan/Zoom), particles, glow, lens flares -> **DaVinci Resolve Fusion**
  - Master Final Assembly, J-cut/L-cut audio, color grading -> **DaVinci Resolve**
  - **HYPERFRAME_VISUAL_METHOD** is a naming convention for motion graphics, it does NOT mean "use the HyperFrames tool for everything". Obey the assignment law above.
- Do NOT generate or register executable prompt packets, JSON timeline metadata, or local ComfyUI/AnimateDiff configs. Postpone local media generation tasks until the plan is frozen.

### Depth Anything V2 Operational Lock

- Use DA-V2 only through the local control panel:
  `python3 /Users/apple/ShadowMediaFactory/control_panel/bin/shadow_factory_ctl.py run-depth-anything --input <image_or_dir> --output-dir <depth_output_dir>`
- Installed default: `Depth-Anything-V2-Small`, encoder `vits`, license `Apache-2.0`.
- Base/Large checkpoints are non-commercial lanes and require explicit license approval before use.
- DA-V2 outputs `depth_map_png` artifacts only. It does not generate still images, video clips, cinematic B-roll, camera motion, or DaVinci composites.
- Approved DA-V2 use cases are universal: macro/insert stills, split-screen
  comparison panels, product/object close-ups, document/tabletop shots, and
  other still-image shots where foreground/midground/background parallax adds
  value. Use only for `IMAGE_MOTION_GRAPHICS_BROLL_METHOD` still-image shots.

### Mode B: Media Factory Final Draft (Executable Phase)
For full, executable Media Factory tasks (after plan validation & approval), output:
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
- PRODUCTION_ORDER_LOCK — ordered phases with dependency IDs, approval gates, and proof gates
- ASSET_INVENTORY_LEDGER — separate counts for voice, music, SFX, character references, storyboard stills, depth parallax stills, HyperFrames assets, overlays, cinematic B-roll, A-roll batches, DaVinci assets, and thumbnails
- ASSET_DEPENDENCY_GRAPH — one row per asset with dependencies, lane, tool/provider, expected output path, approval requirement, and proof requirement
- CONTROL_PANEL_EXECUTION_PLAN — control panel CLI, job packet directory, preflight steps, route downgrade handling, proof JSON, registry update requirements, and one `control_panel_phase_row_json=` per executable phase
- DAVINCI_TIMELINE_PACKET — V1/V2/V3 and A1-A5 track placement with scene IDs, source asset IDs, transitions, J/L cuts, color, captions, safe zones, and proof dependencies
- PRODUCTION_PROOF_GATE — no stage is complete until artifacts, proof JSON, registry entry, validation result, and review status are present
- VOICE_BATCH_PLAN, A_ROLL_BATCH_PLAN, MUSIC_SFX_BATCH_PLAN, IMAGE_BATCH_PLAN,
  CINEMATIC_BROLL_BATCH_PLAN, MOTION_GRAPHICS_BATCH_PLAN, and ASSEMBLY_SYNC_PLAN
  when the user asks for the visual media generator draft.
- LOCAL_CLOUD_HYBRID_EXECUTION_PLAN — per-lane options for voice, image, video, music_sfx, editing, packaging
- MEDIA_FACTORY_EVIDENCE_GATE — for any claimed artifact: file_path, generation_method, engine_used,
  source_prompt_packet_ref, validation_result, human_review_status
- CONTROL_PANEL_PREFLIGHT_GATE — for renderable storyboard/B-roll requests:
  requested controls, available controls, route downgrade status,
  output_classification, production_pass_allowed, safe_to_batch_automate
- RULE_CONSUMPTION_EVIDENCE_LEDGER and EXACT_RULE_LINEAGE_MAP — required for
  full production readiness; proxy-only route summaries cap the output below
  production-ready status

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
