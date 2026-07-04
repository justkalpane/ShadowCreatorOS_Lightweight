# Local Media Factory Bridge Contract

## Purpose

This contract permanently wires ShadowCreatorOS_Lightweight to the deployed
local ShadowMediaFactory engine on the current Mac.

ShadowCreatorOS_Lightweight remains the brain. ShadowMediaFactory remains the
local media worker. Agents must not blur those responsibilities.

## Canonical Bridge Registry

Agents must load:

```text
registries/local_media_factory_bridge.yaml
```

before any Media Factory handoff, storyboard render request, local visual
generation request, or local/cloud media route decision.

The bridge registry stores the current local Mac paths for:

```text
LOCAL_MEDIA_FACTORY_ROOT=/Users/apple/ShadowMediaFactory
MEDIA_FACTORY_CONTROL_PANEL=/Users/apple/ShadowMediaFactory/control_panel
MEDIA_FACTORY_CLI=/Users/apple/ShadowMediaFactory/control_panel/bin/shadow_factory_ctl.py
MEDIA_FACTORY_PROOFS=/Users/apple/ShadowMediaFactory/control_panel/proofs
MEDIA_FACTORY_REGISTRY=/Users/apple/ShadowMediaFactory/control_panel/registry
MEDIA_FACTORY_JOBS=/Users/apple/ShadowMediaFactory/control_panel/jobs
MEDIA_FACTORY_OUTPUTS=/Users/apple/ShadowMediaFactory/08_EXPORTS
COMFYUI_ROOT=/Users/apple/ShadowMediaFactory/apps/ComfyUI
```

Absolute paths are local Mac references. They are active for this workstation
but must not be treated as portable startup law.

## Responsibility Split

```text
ShadowCreatorOS_Lightweight
-> research
-> script
-> scene plan
-> visual media draft
-> scene contract
-> prompt packet
-> route decision
-> Media Factory handoff packet

ShadowMediaFactory
-> status / doctor / preflight
-> ComfyUI local generation when approved
-> AnimateDiff / Wan lane execution when approved
-> Depth map generation via DA-V2 (ViT-S Small default / MPS)
-> HyperFrames HTML deterministic renders (NotebookLM slides, kinetic titles)
-> FFmpeg assembly / packaging
-> DaVinci handoff for 2.5D Parallax, manual compositing, and final polish
-> proof JSON
-> asset registry update
-> export artifact
```

## Locked Local Pipelines

Depth Anything V2 is authorized only as a local depth-map generator for still
images. The production 2.5D parallax path is:

```text
source_still_image
-> Depth Anything V2 depth_map_png
-> DaVinci Resolve Fusion layer separation / Luma Keyer mask
-> foreground/midground/background transform animation
-> DaVinci timeline render or MP4 export
```

NotebookLM-style and programmatic slide rendering is authorized through
HyperFrames CLI. The NotebookLM slide path is:

```text
notebook_dual_panel_html_css_gsap_project
-> HyperFrames CLI / headless Chrome render
-> MP4 panel output or MOV alpha output
-> HyperFrames proof JSON
-> registry/assets.jsonl hyperframes_rendered event
-> DaVinci Resolve V1 slide background
-> optional HeyGen chromakey presenter on V2
-> final DaVinci assembly
```

HyperFrames does not replace DaVinci Resolve for 2.5D parallax or final
assembly. Depth Anything V2 does not generate images or video.

The first approved non-cinematic B-roll foundation lane is:

```text
approved still images or background video
-> FFmpeg local image/music/SFX B-roll proof where needed
-> HyperFrames dashboard / NotebookLM / evidence wall / kinetic card render
-> MP4 panel output or MOV alpha overlay output
-> proof JSON plus registry event
-> DaVinci or FFmpeg assembly
```

HyperFrames output cannot be claimed as generated media unless the control
panel emits a proof JSON and an `assets.jsonl` registry event containing
`proof_path`, `template_family`, `visual_pattern`, and `asset_path`.

HyperFrames output also cannot be claimed unless the mission output includes a
`TOOLS_CONNECTORS_PLUGINS_ASSESSMENT` row for `hyperframes_cli_local` plus the
official SS-118 skill proof and the upstream HyperFrames skill paths.

For alpha-overlay scenes, current production truth on this workstation is:

```text
alpha_required=true
-> approved output extension=.mov
-> proof pix_fmt must contain yuva
-> compatibility family name may remain webm_alpha_overlay
```

If the requested alpha overlay path is `.webm`, the local worker must block or
route-downgrade. It must not claim production-safe alpha delivery on the
current runtime.

If the repo-side packet, Antigravity test, or operator plan requests a
HyperFrames family, the local worker must either:

```text
1. execute the requested HyperFrames family and return proof JSON + registry event
```

or:

```text
2. declare ROUTE_DOWNGRADED=true with fallback_reason, requested_hyperframes_family,
   replacement_method, and production_pass_allowed=false
```

Silent downgrade to generic FFmpeg Ken Burns motion is forbidden when the task
claims HyperFrames-first non-cinematic B-roll coverage.

The installed production default is Depth-Anything-V2-Small (`vits`) because
the official upstream repository lists the Small checkpoint under Apache-2.0.
Base and Large checkpoints are non-commercial (`CC-BY-NC-4.0`) lanes and cannot
be used for monetized/commercial production without explicit license approval.

## Required Handoff Flow

For Media Factory work, agents must use this sequence:

1. Select `MEDIA_FACTORY_HANDOFF`.
2. Load `registries/route_manifests/media_factory_handoff.yaml`.
3. Load `registries/local_media_factory_bridge.yaml`.
4. Load this contract.
5. Load `runtime_contracts/HYPERFRAMES_CONNECTOR_INTEGRATION_CONTRACT.md`
   whenever HyperFrames is part of the route.
6. Produce or locate a media-aware scene contract and prompt packet.
7. Place or reference handoff files under:

```text
/Users/apple/ShadowMediaFactory/control_panel/jobs/<job_id>/01_timeline/
```

8. Run Media Factory status/doctor/preflight only when local checks are needed.
9. Run render commands only after explicit user approval.
10. Read proof JSON and registry JSONL before claiming any media artifact.

## Batch 4 Shadow OS Runtime Binding

Before any local-handoff-ready claim, ShadowCreatorOS_Lightweight must bind the
handoff to the governed packet surface introduced by the Batch 1-3 law stack:

```text
route_state_capsule.schema.json
evidence_bundle.schema.json
bridge_job_packet.schema.json
patch_transaction.schema.json (repo-write claims only)
final_visual_media_generation_draft.schema.json
depth_map_packet.schema.json
ffmpeg_filtergraph_packet.schema.json
hyperframes_payload.schema.json
comfyui_workflow_payload.schema.json
source_vs_render_packet.schema.json
visual_qa_acceptance_packet.schema.json
pilot_cut_validation_packet.schema.json
audio_authorization_packet.schema.json
davinci_handoff_packet.schema.json
```

Required validator surface before any unlock claim:

```text
validators/validate_evidence_bundle.py
validators/validate_route_state_capsule.py
validators/validate_bridge_job_packet.py
validators/validate_final_visual_media_generation_draft.py
validators/validate_depth_map_packet.py
validators/validate_ffmpeg_filtergraph_packet.py
validators/validate_hyperframes_payload.py
validators/validate_comfyui_payload.py
validators/validate_source_vs_render_packet.py
validators/validate_visual_qa_acceptance.py
validators/validate_pilot_cut_validation_packet.py
validators/validate_audio_authorization_packet.py
validators/validate_davinci_handoff_packet.py
```

Bridge readiness is therefore not a prose claim. It is a bound state requiring:

```text
bridge_job_packet_present=true
evidence_bundle_present=true
route_state_capsule_present=true
validator_surface_bound=true
production_pass_allowed=false until validator + approval gates are satisfied
```

## Required Preflight Honesty Gate

Before rendering storyboard or B-roll requests, the control panel preflight must
compare:

```text
requested controls
available controls
wired controls
route capability
audio requirements
camera motion requirements
visual quality target
```

If the request asks for OpenPose, Depth, Lineart, IPAdapter, true camera
movement, realistic human action, or production cinematic output, and the
current local route cannot execute those requirements, the result must be:

```text
ROUTE_DOWNGRADED=true
OUTPUT_CLASSIFICATION=animated_storyboard
PRODUCTION_PASS_ALLOWED=false
SAFE_TO_BATCH_AUTOMATE=false
```

No agent may call an SD1.5 + Canny + AnimateDiff result "production cinematic
B-roll" unless a future proof explicitly upgrades that lane.

## Current Lane Truth

The current local capability truth is read from:

```text
/Users/apple/ShadowMediaFactory/control_panel/config/capability_map.json
```

Current summary:

```text
LOCAL_ANIMATIC_LANE=LOCAL_ENGINE_READY
LOCAL_ANIMATIC_ENGINE=SD1.5 + Canny ControlNet + AnimateDiff
LOCAL_ANIMATIC_OUTPUT_CLASSIFICATION=animated_storyboard

WAN_LANE=LOCAL_ENGINE_READY
WAN_TECHNICAL_PASS=true
WAN_PRODUCTION_QUALITY_PASS=false
WAN_ROLE=experimental

HYPERFRAMES_LANE=LOCAL_ENGINE_READY
HYPERFRAMES_ROLE=html_css_deterministic_render

DEPTH_ANYTHING_V2_LANE=LOCAL_ENGINE_READY
DEPTH_ANYTHING_V2_DEFAULT_ENCODER=vits
DEPTH_ANYTHING_V2_DEFAULT_MODEL=Depth-Anything-V2-Small
DEPTH_ANYTHING_V2_DEFAULT_LICENSE=Apache-2.0
DEPTH_ANYTHING_V2_ROLE=depth_map_generation

FFMPEG_ASSEMBLY_LANE=LOCAL_ENGINE_READY
DAVINCI_LANE=LOCAL_ENGINE_READY_FOR_MANUAL_FINISHING_QC
LOCAL_CINEMATIC_BROLL_LANE_PROVEN=false
SAFE_TO_BATCH_AUTOMATE_CINEMATIC_BROLL=false
```

## Proof Requirement

Any claimed output must include:

```text
artifact_path=
proof_json_path=
registry_path=
engine_used=
route_used=
providers_called=false/true
n8n_used=false/true
output_classification=
production_pass_allowed=false/true
```

If proof is missing, the claim status is `NEEDS_CONFIRMATION`, not `PASS`.

## Drift Sync Protocol

The permanent bridge is not allowed to drift from the local Media Factory.
Whenever the Media Factory control panel, capability map, proofs, registry, or
runtime lanes change, agents must run:

```text
python3 tools/shadow_runtime/media_factory_bridge_sync.py --runtime-check
```

This command audits:

```text
/Users/apple/ShadowMediaFactory/control_panel/config/capability_map.json
/Users/apple/ShadowMediaFactory/control_panel/bin/shadow_factory_ctl.py
/Users/apple/ShadowMediaFactory/control_panel/proofs/
/Users/apple/ShadowMediaFactory/control_panel/registry/
```

and compares them against:

```text
registries/local_media_factory_bridge.yaml
```

If repo-write is approved, agents may synchronize the bridge state with:

```text
python3 tools/shadow_runtime/media_factory_bridge_sync.py --runtime-check --apply
```

The apply mode may update only the auto-generated `sync_state` block inside the
bridge registry. It must not install tools, render media, call providers, use
n8n, or modify the Media Factory runtime.

Required drift fields:

```text
BRIDGE_IN_SYNC=true/false
MEDIA_FACTORY_CHANGED=true/false
REPO_BRIDGE_UPDATE_REQUIRED=true/false
SYNC_STATE_WRITTEN=true/false
```

## Provider Boundary

Core paid/provider exceptions remain:

```text
HeyGen
ElevenLabs
```

No other paid/cloud provider may be added to the core or called without user
approval.

## Forbidden

- Do not claim local cinematic B-roll is proven when preflight classifies the
  lane as `animated_storyboard`.
- Do not silently downgrade requested controls.
- Do not call providers or n8n by default.
- Do not render unless local engine execution is explicitly approved.
- Do not modify the Shadow repo from Media Factory execution unless repo-write
  is explicitly approved.
- Do not let Media Factory runtime changes remain unsynced; run the drift sync
  audit and report `REPO_BRIDGE_UPDATE_REQUIRED` honestly.
