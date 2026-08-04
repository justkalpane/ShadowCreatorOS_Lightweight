# Media Factory FFmpeg Encode Standard

```text
contract_id=C-SO-003
file_path=runtime_contracts/MEDIA_FACTORY_FFMPEG_ENCODE_STANDARD.md
owner=ShadowCreatorOS_Lightweight
applies_to=ffmpeg_render_packets,media_factory_templates
scope=production_encode_quality_locks
status_after_batch_1=DOCUMENTED_ONLY_NOT_ENFORCED
unlocks_nothing=true
```

## Purpose

This contract locks minimum FFmpeg quality requirements for production-bound
video outputs and blocks silent fallback to weak scale, color, or encode
defaults.

## Required Inputs

```text
filtergraph_text
scale_method
encode_profile
color_profile
concat_policy
```

## Required Outputs

```text
ffmpeg_command_log
encode_profile_proof
ffprobe_report
```

## Forbidden Behaviors

- `scale_method=bilinear`
- missing `-crf 18`
- missing BT709 flags
- hidden repeated lossy transcodes
- default VBR pass without proof

## Pass Conditions

- Lanczos scaling is explicit when scaling occurs.
- `-crf 18` and BT709 flags are present.
- Concat policy proves no hidden double lossy chain.

## Fail Conditions

- Required scale, CRF, or color flags are absent.
- FFmpeg logs cannot prove the encode profile actually used.

## Evidence Required

```text
ffmpeg_command_log
filtergraph_dump
ffprobe_report
```

## Route Bindings

- `full_video_pipeline`

## Schema Bindings

- `schemas/ffmpeg_filtergraph_packet.schema.json`

## Validator Bindings

- `validators/validate_ffmpeg_filtergraph_packet.py`

## Fixture Bindings

- Gold: `validators/fixtures/gold/ffmpeg_filtergraph_valid.json`
- Bad: `validators/fixtures/bad/ffmpeg_missing_crf18.json`

## Proof Artifacts

```text
ffmpeg_encode_proof.txt
ffprobe_report.json
```
