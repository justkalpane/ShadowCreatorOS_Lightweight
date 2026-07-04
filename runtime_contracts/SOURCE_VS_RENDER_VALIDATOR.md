# Source Vs Render Validator Contract

```text
contract_id=C-SO-006
file_path=runtime_contracts/SOURCE_VS_RENDER_VALIDATOR.md
owner=ShadowCreatorOS_Lightweight
applies_to=visual_qa,source_render_comparison
scope=require_frame_comparison_before_acceptance
status_after_batch_1=DOCUMENTED_ONLY_NOT_ENFORCED
unlocks_nothing=true
```

## Purpose

This contract requires direct comparison between source intent frames and
rendered output frames before a visual pass can be claimed.

## Required Inputs

```text
source_frame
rendered_frame
thresholds
```

## Required Outputs

```text
diff_images
quality_metrics
source_vs_render_report
```

## Forbidden Behaviors

- no comparison at all
- metadata-only QA
- missing thresholds with a PASS claim

## Pass Conditions

- Diff artifacts exist.
- Metrics pass thresholds or a human override is explicitly recorded.

## Fail Conditions

- Comparison artifacts are missing.
- Degradation exceeds thresholds without a recorded override.

## Evidence Required

```text
source_frame_reference
render_frame_reference
diff_artifacts
quality_scorecard
```

## Route Bindings

- `full_video_pipeline`

## Schema Bindings

- `schemas/final_visual_media_generation_draft.schema.json`

## Validator Bindings

- `validators/validate_source_vs_render_packet.py`

## Fixture Bindings

- Gold: `validators/fixtures/gold/source_vs_render_valid.json`
- Bad: `validators/fixtures/bad/source_vs_render_missing_diff.json`

## Proof Artifacts

```text
source_vs_render_report.md
quality_scorecard.json
```
