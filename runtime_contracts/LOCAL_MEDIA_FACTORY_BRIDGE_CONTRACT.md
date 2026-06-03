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
-> FFmpeg assembly / packaging
-> HyperFrames / DaVinci handoff when applicable
-> proof JSON
-> asset registry update
-> export artifact
```

## Required Handoff Flow

For Media Factory work, agents must use this sequence:

1. Select `MEDIA_FACTORY_HANDOFF`.
2. Load `registries/route_manifests/media_factory_handoff.yaml`.
3. Load `registries/local_media_factory_bridge.yaml`.
4. Load this contract.
5. Produce or locate a media-aware scene contract and prompt packet.
6. Place or reference handoff files under:

```text
/Users/apple/ShadowMediaFactory/control_panel/jobs/<job_id>/01_timeline/
```

7. Run Media Factory status/doctor/preflight only when local checks are needed.
8. Run render commands only after explicit user approval.
9. Read proof JSON and registry JSONL before claiming any media artifact.

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
