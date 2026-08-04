# Local Cloud Hybrid Media Execution Contract

## Purpose

Media handoff planning must remain portable and provider-safe. Every Media
Factory task must declare its execution lane per asset type, disclose the local
engine readiness status, and never claim execution that has not occurred.

## Required Output

```text
LOCAL_CLOUD_HYBRID_EXECUTION_PLAN
voice:
  local_options:
  cloud_options:
  hybrid_strategy:
  fallback:
image:
  local_options:
  cloud_options:
  hybrid_strategy:
  fallback:
video:
  local_options:
  cloud_options:
  hybrid_strategy:
  fallback:
music_sfx:
  local_options:
  cloud_options:
  hybrid_strategy:
  fallback:
editing:
  local_options:
  cloud_options:
  hybrid_strategy:
  fallback:
packaging:
  local_options:
  cloud_options:
  hybrid_strategy:
  fallback:
```

Each asset lane must disclose preferred path, fallback path, dependency risk,
and provider boundary. Planning must not assume one provider.

## Local Media Factory Bridge Readiness Law

The repo is designed to connect to a locally hosted Media Factory engine using
local open-source tools. The following engines are recognized. Each must declare
its readiness status when referenced in a Media Factory handoff.

The active local Mac bridge is registered in:

```text
registries/local_media_factory_bridge.yaml
```

For Media Factory tasks, agents must load that registry and
`runtime_contracts/LOCAL_MEDIA_FACTORY_BRIDGE_CONTRACT.md` before declaring
local engine readiness, command paths, proof paths, or execution safety.

### Recognized Local Engines

```text
local_engine_registry:

  engine_id: comfyui_local
  engine_class: image_and_video_generation
  input_format: JSON workflow + text prompt
  output_format: PNG / JPEG / MP4
  supported_models: SDXL | Flux | SD1.5 | AnimateDiff | SVD
  currently_wired_controlnet_support: Canny
  requested_but_not_wired: OpenPose | Depth | Lineart | IP-Adapter | true_camera_motion
  hardware_requirement: GPU recommended (CPU fallback available)
  readiness_status: LOCAL_ENGINE_READY
  current_role: animated_storyboard / animatic_preview

  engine_id: ffmpeg_local
  engine_class: video_assembly_and_rendering
  input_format: image sequence | audio | subtitle files
  output_format: MP4 | MOV | WebM
  hardware_requirement: CPU
  readiness_status: LOCAL_ENGINE_READY

  engine_id: animatediff_local
  engine_class: video_motion_generation
  input_format: text prompt + reference image
  output_format: GIF | MP4
  hardware_requirement: Apple Silicon MPS / local ComfyUI route
  readiness_status: LOCAL_ENGINE_READY
  current_role: animated_storyboard / animatic_preview

  engine_id: wan_local
  engine_class: open_source_video_model
  input_format: text prompt + optional image
  output_format: MP4
  hardware_requirement: Apple Silicon Mac-safe preset with cpu-vae
  readiness_status: LOCAL_ENGINE_READY
  current_role: experimental
  production_quality_pass: false

  engine_id: ltx_local
  engine_class: open_source_video_model
  input_format: text prompt + optional image
  output_format: MP4
  hardware_requirement: GPU required
  readiness_status: STUB

  engine_id: davinci_resolve_local
  engine_class: editing_and_color_grading
  input_format: video clips | audio | project file
  output_format: MP4 | ProRes | DCP
  hardware_requirement: CPU + GPU
  readiness_status: LOCAL_ENGINE_READY
  current_role: manual finishing and QC
```

## Permanent Local Bridge Commands

The active local bridge commands are:

```text
MEDIA_FACTORY_STATUS=python3 /Users/apple/ShadowMediaFactory/control_panel/bin/shadow_factory_ctl.py status
MEDIA_FACTORY_DOCTOR=python3 /Users/apple/ShadowMediaFactory/control_panel/bin/shadow_factory_ctl.py doctor
MEDIA_FACTORY_PREFLIGHT_STORYBOARD=python3 /Users/apple/ShadowMediaFactory/control_panel/bin/shadow_factory_ctl.py preflight-storyboard --metadata <metadata_json>
```

Rendering commands require explicit user approval. Planning and preflight do not
prove media creation.

## Local Capability Honesty Rule

If a scene packet requests controls or motion that the current local lane cannot
execute, the handoff must report:

```text
ROUTE_DOWNGRADED=true
OUTPUT_CLASSIFICATION=animated_storyboard
PRODUCTION_PASS_ALLOWED=false
SAFE_TO_BATCH_AUTOMATE=false
```

Current limitations from the bridge capability map:

```text
OpenPose=false
Depth=false
Lineart=false
IPAdapter=false
true_camera_motion=false
Wan2.2_production_quality_pass=false
```

Agents may still use the local lane for animatics and proof-of-routing, but not
as a proven cinematic B-roll lane until a later proof upgrades the capability.

## Readiness Status Labels

Every local engine reference must use one of these status values:

```text
DESIGNED       — architecture and prompt packets planned, engine not yet connected
STUB           — placeholder reference only, fields incomplete
PACKET_READY   — prompt packets validated, engine connection not yet confirmed
LOCAL_ENGINE_READY — engine installed, tested, and accepting prompt packets
PROVIDER_READY — prompt packet formatted for cloud provider handoff
EXECUTABLE     — execution explicitly approved and engine confirmed operational
BLOCKED        — missing dependency or hardware prevents execution
NEEDS_CONFIRMATION — requires user decision before proceeding
```

## Local Render Metadata Standard

When a local engine produces output, the following metadata must be recorded:

```text
local_render_metadata:
  render_id=
  source_prompt_packet_ref=
  engine_used=
  engine_readiness_at_render_time=
  render_resolution=
  render_duration_seconds=
  output_path=
  output_format=
  quality_score=
  human_review_status=
  validation_result=PASS/PARTIAL/BLOCKED/NEEDS_CONFIRMATION
```

## Storyboard Folder Convention

When storyboard images are exported for local engine ingestion:

```text
storyboard_delivery:
  default_path=/Users/apple/Downloads/b_roll_storyboard/
  mission_scoped_path=outputs/missions/<mission_id>/storyboard/
  naming_convention=shot<N>_<scene_id>_<descriptor>.png
  json_pacing_metadata_path=<folder>/video_pacing_metadata.json
  txt_pacing_metadata_path=<folder>/video_pacing_metadata_notepad.txt
  image_quality=original_generation_quality
  file_headers_preserved=true
  exact_filenames_in_json=true
```

The pacing metadata JSON must reference exact image filenames so local engine
ingestion has full context without manual filename mapping.

## Asset Lane Guidance

```text
voice:
  local_options: Coqui TTS | Piper | local Ollama with audio extension
  cloud_options: ElevenLabs (deferred, requires approval)
  hybrid_strategy: generate script and SSML locally, send to ElevenLabs when approved
  fallback: use system TTS for timing reference only

image:
  local_options: ComfyUI + SDXL/Flux (LOCAL_ENGINE_READY when confirmed)
  cloud_options: NanoBanana | Midjourney | DALL-E (requires approval)
  hybrid_strategy: generate prompt packets locally, execute in ComfyUI or cloud when approved
  fallback: provide detailed text storyboard with full DNA fields

video:
  local_options: AnimateDiff | Wan | LTX via ComfyUI (DESIGNED to STUB range)
  cloud_options: Sora | Seedance | Higgsfield | Kling (requires approval)
  hybrid_strategy: use local stills + FFmpeg assembly while video model approval pending
  fallback: image sequence + pacing metadata for manual assembly in DaVinci Resolve

music_sfx:
  local_options: Suno (local API if available) | pre-licensed local library
  cloud_options: Suno API | Udio (requires approval)
  hybrid_strategy: specify mood, tempo, intensity locally; execute in Suno when approved
  fallback: provide music direction brief with scene sync timestamps

editing:
  local_options: FFmpeg (assembly) | DaVinci Resolve (color + cut)
  cloud_options: not required; editing is always local-first
  hybrid_strategy: FFmpeg handles rough assembly; DaVinci Resolve handles color and final export
  fallback: provide detailed editing timeline with frame-level instructions

packaging:
  local_options: FFmpeg for platform transcoding | local metadata generator
  cloud_options: YouTube Data API (deferred, requires approval)
  hybrid_strategy: transcode locally, upload manually or via approved API
  fallback: provide platform-ready file specs and manual upload checklist
```

## Safety Boundary

```text
n8n_used=false
providers_called=false
media_artifacts_claimed=false
provider_execution_allowed=false
local_media_generation_engine_used=false
```

Override each field only when execution is explicitly approved and evidence is
present. Planning declarations alone cannot set any field to `true`.
