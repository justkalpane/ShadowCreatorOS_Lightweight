# Production Intent Enforcement Rule

```text
contract_id=C-SO-009
file_path=runtime_contracts/PRODUCTION_INTENT_ENFORCEMENT_RULE.md
owner=ShadowCreatorOS_Lightweight
applies_to=script_to_visual_plan,visual_draft,render_qa
scope=separate_technical_success_from_creative_success
status_after_batch_1=DOCUMENTED_ONLY_NOT_ENFORCED
unlocks_nothing=true
```

## Purpose

This rule prevents technically valid but creatively flat outputs from being
treated as production-ready.

## Required Inputs

```text
scene_intent
visual_metaphor
motion_intent
acceptance_criteria
```

## Required Outputs

```text
intent_alignment_report
```

## Forbidden Behaviors

- generic slideshow
- random effect stack
- render ignores scene intent
- technical success labeled production success

## Pass Conditions

- Scene intent maps to visual proof.
- Motion and overlays support the intended emotional or narrative beat.

## Fail Conditions

- No intent mapping exists.
- Output is generic while claiming cinematic or story-specific execution.

## Evidence Required

```text
scene_intent_matrix
visual_alignment_notes
render_frame_examples
```

## Route Bindings

- `visual_media_plan`
- `media_factory_handoff`
- `full_video_pipeline`

## Schema Bindings

- `schemas/visual_media_plan_row.schema.json`
- `schemas/final_visual_media_generation_draft.schema.json`

## Validator Bindings

- `validators/validate_visual_qa_acceptance.py`

## Fixture Bindings

- Gold: `validators/fixtures/gold/scene_intent_mapped.json`
- Bad: `validators/fixtures/bad/generic_slideshow_pass.json`

## Proof Artifacts

```text
intent_alignment_report.md
```
