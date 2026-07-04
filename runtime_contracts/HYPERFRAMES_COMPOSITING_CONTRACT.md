# HyperFrames Compositing Contract

```text
contract_id=C-SO-004
file_path=runtime_contracts/HYPERFRAMES_COMPOSITING_CONTRACT.md
owner=ShadowCreatorOS_Lightweight
applies_to=hyperframes_payloads,overlay_compositing,visual_qa
scope=overlay_visibility_and_scene_relevance
status_after_batch_1=DOCUMENTED_ONLY_NOT_ENFORCED
unlocks_nothing=true
```

## Purpose

This contract governs how HyperFrames overlays behave so they support the scene
instead of obscuring the subject or adding random noise.

## Required Inputs

```text
overlay_path
base_image_path
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
overlay_composite_log
overlay_contact_sheet
hierarchy_map
```

## Forbidden Behaviors

- raw overlay with no alpha or blend configuration
- opacity outside approved range
- overlay obstructs subject readability
- overlay dominates with no scene relevance

## Pass Conditions

- Overlay is visible, bounded, and non-destructive.
- Blend and alpha handling are explicit.
- Overlay supports scene intent and respects safe zones.

## Fail Conditions

- Overlay hides the base subject.
- No proof shows the overlay position, opacity, and blend mode used.

## Evidence Required

```text
overlay_probe
contact_sheet
hierarchy_validation
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
overlay_visibility_report.md
hierarchy_validation.json
```
