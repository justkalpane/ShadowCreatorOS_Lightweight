# Blur Masking Prohibition

```text
contract_id=C-SO-002
file_path=runtime_contracts/BLUR_MASKING_PROHIBITION.md
owner=ShadowCreatorOS_Lightweight
applies_to=depth_map_validation,ffmpeg_filtergraph_validation
scope=ban_blur_as_depth_or_parallax_proof
status_after_batch_1=DOCUMENTED_ONLY_NOT_ENFORCED
unlocks_nothing=true
```

## Purpose

This contract prevents blur filters from being credited as depth or parallax
proof. Aesthetic blur may exist as style, but it cannot satisfy spatial motion
requirements.

## Required Inputs

```text
filtergraph_text
depth_intent
pass_reason
```

## Required Outputs

```text
forbidden_filter_scan_report
```

## Forbidden Behaviors

- boxblur used as depth proof
- gblur used as depth proof
- maskedmerge-only depth pass
- aesthetic blur mislabeled as parallax

## Pass Conditions

- Blur is tagged as non-depth style when present.
- No blur-only stage is cited as parallax evidence.

## Fail Conditions

- Any blur-only filter is used to justify true depth motion.
- The pass reason cites blur or mask merging instead of depth-driven movement.

## Evidence Required

```text
filtergraph_dump
pass_reason_record
rejection_or_clearance_report
```

## Route Bindings

- `full_video_pipeline`

## Schema Bindings

- `schemas/depth_map_packet.schema.json`
- `schemas/ffmpeg_filtergraph_packet.schema.json`

## Validator Bindings

- `validators/validate_depth_map_packet.py`

## Fixture Bindings

- Gold: `validators/fixtures/gold/depth_map_packet_valid.json`
- Bad: `validators/fixtures/bad/depth_method_maskedmerge_only.json`

## Proof Artifacts

```text
blur_ban_scan.txt
```
