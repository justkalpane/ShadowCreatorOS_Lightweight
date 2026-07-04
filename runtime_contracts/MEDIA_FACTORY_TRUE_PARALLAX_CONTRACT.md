# Media Factory True Parallax Contract

```text
contract_id=C-SO-001
file_path=runtime_contracts/MEDIA_FACTORY_TRUE_PARALLAX_CONTRACT.md
owner=ShadowCreatorOS_Lightweight
applies_to=visual_media_generation_draft,media_factory_handoff,full_video_pipeline
scope=depth_driven_spatial_motion_only
status_after_batch_1=DOCUMENTED_ONLY_NOT_ENFORCED
unlocks_nothing=true
```

## Purpose

This contract requires true parallax proof when a scene claims depth-driven
motion. Depth maps may support spatial motion, but blur masks and flat zooms
cannot be labeled as parallax.

## Required Inputs

```text
base_image_path
depth_map_path
depth_method
parallax_strength
motion_axis
scene_intent
```

## Required Outputs

```text
parallax_filtergraph_packet
depth_usage_log
pilot_parallax_proof
```

## Forbidden Behaviors

- `depth_method=blur`
- `depth_method=boxblur`
- `depth_method=maskedmerge_only`
- `pass_reason=ffprobe_only`
- `pass_reason=file_exists_only`
- claiming parallax without source/depth/render proof

## Pass Conditions

- Filtergraph uses approved displace or layered parallax behavior.
- Depth method is logged explicitly.
- Evidence maps source image, depth map, and rendered result together.

## Fail Conditions

- Blur or masked-merge is treated as true depth motion.
- No proof bundle ties the depth map to the render result.
- Spatial motion is claimed from a flat zoom or generic camera move.

## Evidence Required

```text
source_image_reference
depth_map_reference
filtergraph_dump
rendered_frame_reference
```

## Route Bindings

- `media_factory_handoff`
- `full_video_pipeline`

## Schema Bindings

- `schemas/depth_map_packet.schema.json`
- `schemas/ffmpeg_filtergraph_packet.schema.json`

## Validator Bindings

- `validators/validate_depth_map_packet.py`
- `validators/validate_ffmpeg_filtergraph_packet.py`

## Fixture Bindings

- Gold: `validators/fixtures/gold/true_parallax_valid.json`
- Bad: `validators/fixtures/bad/depth_method_boxblur.json`

## Proof Artifacts

```text
parallax_proof.json
ffmpeg_filtergraph.txt
contact_sheet.jpg
```
