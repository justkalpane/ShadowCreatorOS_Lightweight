# Media Factory Final Draft Contract

## Purpose

A script-only response may carry light media hints. A Media Factory final draft
must provide synchronized scene-level production instructions. This contract
defines the complete visual creation DNA, video motion prompt standard,
storyboard export law, evidence requirements, and tool-specific translation
readiness required for every Media Factory handoff.

## Depth Modes

```text
script_only_request=true
media_context_depth=LIGHT_ALLOWED
scene_sync_matrix_required=false
scene_prompt_packets_required=false
storyboard_export_required=false
```

```text
visual_media_plan_requested=true
media_context_depth=PLANNING_ONLY
scene_sync_matrix_required=true
scene_prompt_packets_required=false
storyboard_export_required=false
visual_creation_dna_required=false
video_motion_prompt_required=false
tool_translation_readiness_required=false
local_engine_bridge_status_required=false
```

```text
media_factory_final_draft_requested=true
media_context_depth=DEEP_REQUIRED
scene_sync_matrix_required=true
scene_prompt_packets_required=true
storyboard_export_required=true
visual_creation_dna_required=true
video_motion_prompt_required=true
tool_translation_readiness_required=true
local_engine_bridge_status_required=true
```

## Visual Media Plan vs. Media Factory Final Draft Law

- When a "Visual Media Plan", "Visual Plan", or "Storyboard Plan" is requested (signaled by `visual_media_plan_requested=true`), the output must be a detailed, written, scene-by-scene storyboard layout in Markdown tables.
- The Matrix MUST include the following dimensions:
  - **Media Type & Visual Method**: Declare the exact method: `A_ROLL_AVATAR`, `A_ROLL_OVERLAY_METHOD`, `NOTEBOOKLM_VISUAL_METHOD`, `PROGRAMMATIC_SLIDE_VISUAL_METHOD`, `HTML_CSS_GSAP_VISUAL_METHOD`, `HYPERFRAME_VISUAL_METHOD`, `IMAGE_MOTION_GRAPHICS_BROLL_METHOD`, or `CINEMATIC_BROLL_VIDEO`.
  - **Shot Framing / Setup**: Visual description, shot type, environment, safety profile, and overlay layout (if using `A_ROLL_OVERLAY_METHOD` detailing what floats on top of the presenter).
  - **Camera Motion / Technique**: Ken Burns zoom/pan, dolly, tracking, and **HYPERFRAME_VISUAL_METHOD** (detailing: 3D parallax layer depth separation of foreground vs background, visual highlights, glow maps, particle layers, lens flares, or depth-of-field blurring based on script lines).
  - **Voice (ElevenLabs)**: Script lines, tone, pacing, ElevenLabs Settings (Stability, Similarity, Style Exaggeration, Speaker Boost).
  - **Music & SFX (Suno / Local Library)**: Suno music prompts and **SFX_TIMELINE_METHOD** detailing precision audio timestamps and volume curves (e.g., `[+1.2s] swoop_01.wav at -6dB`, `[+3.5s] coin_ding.wav at -3dB`) synchronized directly to visual transitions or key spoken words.
  - **Captions**: Formatting, kinetic typography, highlights, positioning.
  - **Editing (Nataraja) & Transitions (FFMPEG_TRANSITION_METHOD)**: Cuts, zooms, speed adjustments, J-cuts and L-cuts with precise offsets in seconds (e.g., `J-Cut offset: -0.5s`, `L-Cut offset: +0.8s`), and specific transition cuts (e.g., whip pan, zoom cut, glitch wipe, flash cut) mapped to the visual sequence.
  - **Color Grade (Maya)**: Palette, temperature, film grain, continuity.
  - **Safe Zone**: Safe zone coordinates and platform margins.
- **Image+Motion Graphics Pacing & Hyperframe Rule**: For any image-based B-roll segment:
  - You MUST scale the number of images based on duration and narrative complexity (e.g., 1 image per 2-5 seconds for rapid pacing, or 1 image with continuous Ken Burns motion).
  - Layer **HYPERFRAME_VISUAL_METHOD** overlays (2.5D layer animations, animated kinetic text overlays, digital tracking highlights, particle effects, or speed lines) over still images to simulate high-end editing pacing.
  - Explicitly state the **Image Count** (number of distinct images to be generated) and the **Transition/Hyperframe FX** for each image.
- **NOTEBOOKLM_VISUAL_METHOD Rule**:
  - For sections explaining documents, lessons, note points, and data summaries, utilize the NotebookLM-style presentation.
  - Layout: Left side showcases a vertical document list or note card source block; right side showcases the active selected note with glowing orange/gold bounding highlight boxes that expand over text lines as they are read.
  - Animate document scrolling (vertical scroll) and kinetic citation links popping out from text highlights.
  - These slides are rendered locally in headless Chrome via HyperFrames CLI at zero cost.
  - **Asset & Render Specification Requirements**:
    - During visual planning, the planner must explicitly define the asset structure and rendering parameters for NotebookLM scenes to ensure production quality:
      1. *Asset Inventory*: Explicit list of target file paths (e.g. SVGs, logo files, page preview PNGs). If none are needed, state `assets_needed=NONE (CSS vectors only)`.
      2. *Rendering Draft*: Specify the core rendering variables including font choices, theme styling (light/dark/custom background colors), typing animation speed, scroll offsets, highlight background color/opacity, and GSAP sync timeline parameters.
      3. *DaVinci Overlays Layout*: Explicitly detail the multi-track layering mapping: base slide MP4 on V1 and chromakeyed talking-head avatar video on V2.

- **PROGRAMMATIC_SLIDE_VISUAL_METHOD & HTML_CSS_GSAP_VISUAL_METHOD Rule**:
  - For explanation scenes, listicle blocks, data displays, and learning points, utilize programmatic HTML/CSS templates.
  - Define the layout card style, font colors, kinetic text string, scroll rate, and animation timeline (e.g., card flip, sequential bullet fade-in) in the shot framing column.
  - These slides are rendered locally in headless Chrome at zero cost and offer pixel-perfect layout alignment.
- **Narrative Transition & Ratio Target Law**:
  - Whenever a backstory, real-person anecdote, or backdrop is introduced (including within segments that would otherwise be talking-head A-roll), the presenter avatar must fade or cut away in favor of `NOTEBOOKLM_VISUAL_METHOD`, `PROGRAMMATIC_SLIDE_VISUAL_METHOD`, `HYPERFRAME_VISUAL_METHOD` overlays, or `CINEMATIC_BROLL_VIDEO`.
  - The plan must target the following cost-efficient production ratios:
    - **A-Roll (HeyGen Presenter / Avatars)**: ~40% of total runtime.
    - **Image+Motion Graphics, Programmatic Slides & NotebookLM Slides (Low Cost)**: ~48% of total runtime.
    - **Cinematic B-Roll Video (Cloud/Premium)**: At least 12% of total runtime (principally allocated to the short story/establishing blocks).
- Do NOT generate ComfyUI/AnimateDiff/Flux prompt packets, JSON files, local render configs, or call local rendering engines yet. The goal is to lock the plan before committing to asset rendering.
- Moving to the "Media Factory Final Draft" with full rendering DNA prompts and local engine handoff is only allowed AFTER the user reviews and explicitly approves the written Visual Media Plan.

## Media Factory Tool Assignment Law

Visual method names map to exact tools. Do not substitute tools silently.

```text
NOTEBOOKLM_VISUAL_METHOD -> HyperFrames CLI through SS-116 and SS-118
PROGRAMMATIC_SLIDE_VISUAL_METHOD -> HyperFrames CLI through SS-118
HTML_CSS_GSAP_VISUAL_METHOD -> HyperFrames CLI through SS-118
A_ROLL_OVERLAY_METHOD -> HeyGen chromakey foreground plus HyperFrames MP4/WebM alpha background or overlay, composited in DaVinci Resolve
IMAGE_MOTION_GRAPHICS_BROLL_METHOD -> still image plus Depth Anything V2 mask plus DaVinci Resolve Fusion 2.5D parallax
CINEMATIC_BROLL_VIDEO -> approved cloud/premium cinematic video lane unless a future proof upgrades a local cinematic lane
A_ROLL_AVATAR -> HeyGen or approved avatar provider
FINAL_ASSEMBLY -> DaVinci Resolve, with FFmpeg as assembly/export support
```

HyperFrames is kept for NotebookLM slides, programmatic slides, kinetic text,
data cards, and WebM alpha overlays. HyperFrames does not replace DaVinci
Resolve for 2.5D parallax or final assembly.

Depth Anything V2 is a depth-map masking tool only. It does not generate images
and must not be described as a visual generator.

## Visual Media Plan Required Summary Blocks

Every Visual Media Plan output must conclude with the following two summary sections:
1. **COMPLETE A-ROLL vs B-ROLL vs MOTION GRAPHIC SUMMARY Table**: A markdown table containing columns: `Scene`, `Timecode`, `Type`, `Duration`, `Image Count` (for Image+Motion Graphics scenes), and `Cost Level`.
2. **Cost Distribution Result**: A summary block calculating total durations (in seconds) and percentages for:
   - A-Roll (HeyGen avatar)
   - Motion Graphic Images (Low cost Ken Burns/panning of stills)
   - B-Roll Video (High cost cloud/local video generation)
   This summary must prove that B-Roll video costs have been minimized and target percentages are met.

## Scene Synchronization Law

Every Media Factory scene must align all nine dimensions:

- script line and intent
- voice tone, emotion, pacing, pauses, and pronunciation
- image prompt, composition, lighting, and continuity
- video shot, camera motion, avatar/B-roll need, and duration
- music, SFX, silence, rise, and impact points
- editing cut, caption, transition, and pattern interrupt
- target platform format and safe zone
- line influence reason, emotion, retention function, and topic support
- local, cloud, or hybrid execution mode and fallback

Standalone shallow context sections fail when a final Media Factory draft was
requested.

## Visual Creation DNA Law

Every scene image prompt in a Media Factory final draft must include all fifteen
required DNA fields. A prompt missing any field cannot reach `PASS` status.

Required DNA fields per scene image prompt:

```text
visual_dna:
  subject=
  environment=
  camera_framing=
  lens_focal_logic=
  lighting_setup=
  emotional_tone=
  color_palette=
  cinematic_delivery_standard=Rec.709
  style_lock=
  movement_intent=
  negative_prompt=
  drift_prevention=
  continuity_constraints=
  brand_persona_consistency=
  safety_real_person_handling=
  tool_specific_translation_readiness=
```

- `subject` — who or what is in frame; include persona consistency notes
- `environment` — location, era, weather, time of day, set dressing
- `camera_framing` — shot type: extreme wide | wide | medium | close-up | extreme close-up | POV | two-shot
- `lens_focal_logic` — wide angle for environment / standard for human / telephoto for compression / macro for detail
- `lighting_setup` — key light direction, fill ratio, practical sources, color temperature, shadow depth
- `emotional_tone` — the feeling the frame must evoke in the viewer
- `color_palette` — named palette (teal-orange, amber-shadow, desaturated cool, etc.) + Rec.709 delivery note
- `cinematic_delivery_standard` — always Rec.709 unless explicitly overridden for HDR
- `style_lock` — animation style or photographic style: cinematic realism | stylized | graphic | anime | 3D | photorealistic | illustration
- `movement_intent` — static | slow drift | motivated pan | dolly push | pull-back | handheld
- `negative_prompt` — what to exclude: blurry, watermark, face deformation, split-face, wrong era clothing, etc.
- `drift_prevention` — reference anchor (IP-Adapter ref, previous frame, character sheet, color card)
- `continuity_constraints` — what must match previous or following scene: costume, time of day, set, subject identity
- `brand_persona_consistency` — character or brand identity rules that must be preserved across all scenes
- `safety_real_person_handling` — if a real person is referenced: use_side_profile | use_silhouette | use_shadow | use_animated_inspired | no_face_generation

## Video Motion Prompt Standard

Every scene video prompt in a Media Factory final draft must include:

```text
video_motion_prompt:
  scene_id=
  camera_movement_type=
  lens_focal_logic=
  frame_rate=
  aspect_ratio=
  motion_intensity=
  subject_action=
  background_motion=
  animation_style_classification=
  cinematic_delivery_standard=Rec.709
  local_tool_targets=
  controlnet_guidance_types=
  duration_seconds=
  transition_out=
  sync_point_to_beat_map=
```

Camera movement vocabulary:
- static | pan_left | pan_right | tilt_up | tilt_down | dolly_in | dolly_out
- crane_up | crane_down | handheld | orbit_left | orbit_right | zoom_in | zoom_out
- pull_back | push_in | whip_pan | dutch_tilt

Local tool targets:
- AnimateDiff | Wan | LTX | CogVideoX | ComfyUI_SVD | local_video_model

ControlNet guidance types:
- Canny | OpenPose | Depth | Lineart | SoftEdge | IP-Adapter

## Storyboard Export Law

When a storyboard export is produced, the following structure is mandatory:

```text
storyboard_export:
  export_path=
  naming_convention=shot<N>_<scene_id>_<descriptor>.png
  scene_to_image_map_required=true
  pacing_metadata_coupling_required=true
  json_pacing_metadata_path=
  txt_pacing_metadata_path=
  image_format=PNG
  image_quality=original_generation_quality
  image_to_beat_map_sync=true
```

- Each storyboard image must be named exactly as referenced in the pacing metadata JSON.
- The pacing metadata JSON must contain the `source_image_filename` field for every frame.
- If images are copied to a delivery folder, original file headers must be preserved.

Storyboard folder convention:
- Default: `downloads/b_roll_storyboard/`
- Mission-scoped: `outputs/missions/<mission_id>/storyboard/`

## Scene Prompt Packet Structure

A compliant scene prompt packet must be emitted as:

```text
scene_prompt_packet:
  scene_id=
  timestamp=
  narration_ref=
  emotional_intent=
  visual_objective=
  subject=
  environment=
  camera_framing=
  lens_focal_logic=
  lighting_setup=
  color_palette=
  motion=
  style_lock=
  negative_prompt=
  continuity_rules=
  tool_targets=
  local_execution_readiness=
  provider_handoff_readiness=
  cinematic_delivery_standard=Rec.709
```

Allowed readiness values:
- `DESIGNED` — prompt written, not validated by engine
- `STUB` — placeholder only, fields incomplete
- `PACKET_READY` — all fields present, validated against schema
- `LOCAL_ENGINE_READY` — engine loaded, prompt tested locally
- `PROVIDER_READY` — formatted for cloud provider handoff
- `EXECUTABLE` — execution approved and confirmed
- `BLOCKED` — missing dependency prevents execution
- `NEEDS_CONFIRMATION` — requires user decision before proceeding

## Media Factory Evidence Law

For every claimed media artifact, evidence must include:

```text
media_artifact_evidence:
  file_path=
  artifact_name=
  generation_method=
  source_prompt_packet_ref=
  engine_used=
  render_metadata_path=
  validation_result=
  human_review_status=
  status=PASS/PARTIAL/BLOCKED/NEEDS_CONFIRMATION
```

No evidence block = no `PASS`. Do not convert `NEEDS_CONFIRMATION` into `PASS`.

## Tool-Specific Translation Readiness Law

Every visual scene prompt must be translatable to the following tools without
manual rewriting. Compliance is checked by confirming the prompt contains the
required field mapping:

| Tool | Required Fields |
|------|----------------|
| ComfyUI / SDXL | style_lock, negative_prompt, lighting_setup, color_palette, camera_framing |
| AnimateDiff | camera_movement_type, motion_intensity, frame_rate, duration_seconds |
| Flux-style models | subject, environment, emotional_tone, style_lock, negative_prompt |
| IP-Adapter | drift_prevention (character reference image path) |
| ControlNet | controlnet_guidance_types, source_image_reference |
| FFmpeg assembly | scene_id, duration_seconds, transition_out, sync_point_to_beat_map |
| DaVinci Resolve | scene_id, timestamp, color_palette, cinematic_delivery_standard |

## Re-Hook Synchronization

Every recurring re-hook must be marked in the scene sync matrix. Re-hook scenes
require stronger pattern-interrupt planning across voice tension, image cue,
video camera or B-roll shift, caption treatment, editing cut, music/SFX accent,
platform safe zone, influence reason, and local/cloud/hybrid execution path.

Canonical machine-check output must emit one `scene_row_json=` object per
scene. A heading or completion boolean without schema-valid scene rows is
`FAIL`. Re-hook scenes must include `hook_marker=true`, `rehook_type`, and
`retention_reset_goal`.

## Safety Boundary

```text
n8n_used=false
providers_called=false
media_artifacts_claimed=false
provider_execution_allowed=false
local_media_generation_engine_used=false
```

Override each field only when execution is explicitly approved and evidence is
present. A `PASS` status requires every claimed field to have matching evidence.
