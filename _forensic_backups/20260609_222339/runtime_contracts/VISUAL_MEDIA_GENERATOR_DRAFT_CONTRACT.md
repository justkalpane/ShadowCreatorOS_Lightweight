# Visual Media Generator Draft Contract

## Purpose

The Visual Media Generator Draft is the execution-facing layer that comes after
the visual media plan and before live provider or local-engine execution.

It is not the same as:

- `SCRIPT_GENERATION`
- `VISUAL_MEDIA_PLAN`
- a generic storyboard
- a shallow prompt list

Its job is to define how the media will actually be generated, saved, handed
off, assembled, and cleaned up.

## Distinction Law

```text
visual_media_plan_requested=true
visual_media_generator_draft_requested=false
=> planning only
```

```text
visual_media_plan_requested=true
visual_media_generator_draft_requested=true
=> generator draft required
```

If generator draft is requested, the output must go beyond scene ideas and must
document execution order, save order, assembly order, mission folder layout,
support files, and per-scene handoff details.

The generator draft may declare the folder and support-file structure in chat.
It must not create folders, `.docx`, `.txt`, `.json`, packet, or media files
unless repo-write or media-generation support has been explicitly approved for
that stage.

## Required Output Blocks

Every Visual Media Generator Draft must include:

```text
SCENE_SYNC_MATRIX
SCENE_BREAKOUT_BLOCKS
SCENE_PROMPT_PACKETS
VIDEO_PROMPT_PACKETS
STORYBOARD_EXPORT_PLAN
PRODUCTION_ORDER_LOCK
ASSET_INVENTORY_LEDGER
ASSET_DEPENDENCY_GRAPH
MISSION_MEDIA_OUTPUT_BUNDLE
VOICE_BATCH_PLAN
A_ROLL_BATCH_PLAN
MUSIC_SFX_BATCH_PLAN
IMAGE_BATCH_PLAN
CINEMATIC_BROLL_BATCH_PLAN
MOTION_GRAPHICS_BATCH_PLAN
ASSEMBLY_SYNC_PLAN
CONTROL_PANEL_EXECUTION_PLAN
DAVINCI_TIMELINE_PACKET
SCENE_EXECUTION_BLOCKS
PRODUCTION_PROOF_GATE
PROVIDER_HONESTY_GATE
```

## Scene Breakout Readability Law

The generator draft must remain readable by operators.

- Every scene must have its own scene breakout block.
- Each scene breakout block must be presented vertically under its own scene
  heading.
- A giant merged storyboard table may exist as a summary, but it cannot be the
  only human-readable scene layout.

Required scene breakout heading format:

```text
SCENE_BREAKOUT_TABLE: <scene_id>
```

Each scene breakout must document:

- scene objective
- narration excerpt
- visual method
- asset classes touched
- generation stage
- save path
- naming convention
- DaVinci handoff target
- proof gate

## Generation Order Law

The generator draft must document the canonical generation order and must not
collapse it into vague summary text.

At minimum it must make clear:

1. what is generated first
2. what depends on what
3. where each asset is saved
4. how each asset is later assembled
5. what proof closes each lane

## Saving Order Law

Every executable lane must declare the save destination before execution:

- voice
- music
- SFX
- reference stills
- storyboard stills
- depth maps
- HyperFrames renders
- A-roll
- cinematic B-roll
- DaVinci project outputs
- proofs

If an output path is missing, the generator draft cannot be `PASS`.

## Batch Orchestration Law

The generator draft must document bulk generation lanes end to end. A draft that
only repeats the storyboard, prompt packets, or visual media plan is shallow.

Required batch blocks:

```text
VOICE_BATCH_PLAN
A_ROLL_BATCH_PLAN
MUSIC_SFX_BATCH_PLAN
IMAGE_BATCH_PLAN
CINEMATIC_BROLL_BATCH_PLAN
MOTION_GRAPHICS_BATCH_PLAN
ASSEMBLY_SYNC_PLAN
```

Each batch block must define:

- batch scope
- generation order
- dependencies
- provider or local tool
- save order
- expected output folder
- proof gate
- approval state
- fallback or block behavior

Minimum lane expectations:

- `VOICE_BATCH_PLAN`: ElevenLabs master narration first, then timestamp
  alignment. The master voice is the default timing anchor.
- `A_ROLL_BATCH_PLAN`: HeyGen A-roll batches grouped by presenter state,
  overlay need, and voice dependency.
- `MUSIC_SFX_BATCH_PLAN`: Suno or licensed-library music beds generated as
  grouped arcs, with SFX saved as timestamped clips.
- `IMAGE_BATCH_PLAN`: reference assets, storyboard stills, stills for depth
  parallax, and thumbnails generated in controlled batches.
- `CINEMATIC_BROLL_BATCH_PLAN`: premium cloud cinematic B-roll generated only
  after scene prompt and video prompt packets are locked.
- `MOTION_GRAPHICS_BATCH_PLAN`: HyperFrames renders, NotebookLM-style panels,
  programmatic slides, WebM overlays, and depth-map/parallax preparation.
- `ASSEMBLY_SYNC_PLAN`: DaVinci V1/V2/V3 and A1-A5 synchronization, including
  voice, music, SFX, A-roll, B-roll, stills, HyperFrames, depth maps, captions,
  QC, export, and proof collection.

## Assembly Order Law

The generator draft must state the DaVinci assembly path clearly enough for an
operator or agent to execute without inventing the workflow:

- which assets go to V1, V2, V3
- which assets go to A1, A2, A3, A4, A5
- whether a scene is base visual, overlay, avatar, depth parallax, or caption
- which proof closes the assembly step

## Mission Folder Law Link

The generator draft must comply with:

- `runtime_contracts/MISSION_MEDIA_OUTPUT_FOLDER_CONTRACT.md`

## Primary Method Lock

Unless a route-specific future proof upgrades another lane, the generator draft
must preserve the approved primary methods:

- voice -> ElevenLabs
- avatar / A-roll -> HeyGen
- music / SFX -> Suno or approved licensed library
- still image generation -> ChatGPT image generation or approved still provider
- cinematic B-roll video -> approved premium cloud provider
- NotebookLM / programmatic slides / HTML-CSS-GSAP visuals -> HyperFrames
- depth parallax -> Depth Anything V2 + DaVinci Fusion
- final assembly -> DaVinci Resolve with FFmpeg support

Local ComfyUI / Wan / AnimateDiff / Flux lanes may exist only as backup or
experimental lanes unless a newer route law explicitly promotes them.
