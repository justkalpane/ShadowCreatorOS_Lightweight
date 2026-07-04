# Anything Depth Handoff Contract

```text
contract_id=C-SO-016
file_path=runtime_contracts/ANYTHING_DEPTH_HANDOFF_CONTRACT.md
owner=ShadowCreatorOS_Lightweight
applies_to=depth_map_handoff,depth_support_packets
scope=depth_map_support_only
status_after_batch_1=DOCUMENTED_ONLY_NOT_ENFORCED
unlocks_nothing=true
```

## Purpose

This contract keeps Anything Depth in its correct role: depth-map extraction and
normalization support, not image generation or standalone parallax proof.

## Required Inputs

```text
base_image_path
depth_map_path
dimensions
normalization_method
inversion_policy
```

## Required Outputs

```text
depth_validation_report
normalized_depth_map_optional
```

## Forbidden Behaviors

- depth tool claimed as image generation
- missing dimensions
- missing normalization
- depth used as blur proof

## Pass Conditions

- Depth map role is documented as support-only.
- Dimensions and normalization policy are explicit.

## Fail Conditions

- The handoff overstates Anything Depth as a render or imagery engine.

## Evidence Required

```text
base_image_reference
depth_map_reference
validation_report
```

## Route Bindings

- `full_video_pipeline`
- `media_factory_handoff`

## Schema Bindings

- `schemas/depth_map_packet.schema.json`

## Validator Bindings

- `validators/validate_depth_map_packet.py`

## Fixture Bindings

- Gold: `validators/fixtures/gold/depth_map_packet_valid.json`
- Bad: `validators/fixtures/bad/depth_claimed_image_generation.json`

## Proof Artifacts

```text
depth_validation.json
```
