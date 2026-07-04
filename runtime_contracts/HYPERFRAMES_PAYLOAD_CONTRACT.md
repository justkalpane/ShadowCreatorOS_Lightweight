# HyperFrames Payload Contract

```text
contract_id=C-SO-014
file_path=runtime_contracts/HYPERFRAMES_PAYLOAD_CONTRACT.md
owner=ShadowCreatorOS_Lightweight
applies_to=hyperframes_payload_builders,media_factory_handoff
scope=hyperframes_overlay_payload_grammar
status_after_batch_1=DOCUMENTED_ONLY_NOT_ENFORCED
unlocks_nothing=true
```

## Purpose

This contract defines the payload language for HyperFrames overlays so future
wrappers and validators can consume a stable structure.

## Required Inputs

```text
overlay_path
blend_mode
alpha_mode
opacity
z_index
timing
safe_zone
scene_intent
```

## Required Outputs

```text
hyperframes_overlay_packet
```

## Forbidden Behaviors

- missing blend mode
- missing alpha mode
- opacity too high for readability
- random overlay with no scene intent

## Pass Conditions

- Payload is complete, bounded, and scene-relevant.
- Overlay proof outputs are declared.

## Fail Conditions

- Payload omits compositing essentials.
- Payload can obscure subject or act as noise.

## Evidence Required

```text
overlay_reference
payload_dump
scene_alignment_note
```

## Route Bindings

- `media_factory_handoff`
- `full_video_pipeline`

## Schema Bindings

- `schemas/hyperframes_payload.schema.json`

## Validator Bindings

- `validators/validate_hyperframes_payload.py`

## Fixture Bindings

- Gold: `validators/fixtures/gold/hyperframes_payload_valid.json`
- Bad: `validators/fixtures/bad/hyperframes_missing_alpha.json`

## Proof Artifacts

```text
hyperframes_proof.json
```
