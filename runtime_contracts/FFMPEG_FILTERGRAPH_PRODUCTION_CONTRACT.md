# FFmpeg Filtergraph Production Contract

```text
contract_id=C-SO-017
file_path=runtime_contracts/FFMPEG_FILTERGRAPH_PRODUCTION_CONTRACT.md
owner=ShadowCreatorOS_Lightweight
applies_to=ffmpeg_wrappers,render_packets,full_video_pipeline
scope=filtergraph_proof_and_encode_traceability
status_after_batch_1=DOCUMENTED_ONLY_NOT_ENFORCED
unlocks_nothing=true
```

## Purpose

This contract defines the proof grammar for FFmpeg filtergraphs so future
wrappers, validators, and QA steps can trace exactly what render path was used.

## Required Inputs

```text
filtergraph_text
input_assets
scale_method
encode_profile
color_profile
concat_policy
```

## Required Outputs

```text
filtergraph_packet
command_log
ffmpeg_proof
```

## Forbidden Behaviors

- bilinear scale
- missing `-crf 18`
- missing BT709 flags
- missing filtergraph dump
- hidden transcode chain

## Pass Conditions

- Filtergraph and command log together prove the full render path.
- Required scale, encode, and color locks are explicit.

## Fail Conditions

- Render claims cannot be tied to a concrete filtergraph and command log.

## Evidence Required

```text
filtergraph_dump
command_log
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
- Bad: `validators/fixtures/bad/ffmpeg_missing_lanczos.json`

## Proof Artifacts

```text
ffmpeg_filtergraph.log
encode_proof.txt
```
