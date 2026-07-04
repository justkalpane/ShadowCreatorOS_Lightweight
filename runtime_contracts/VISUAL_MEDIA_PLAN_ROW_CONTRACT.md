# Visual Media Plan Row Contract

```text
contract_id=C-SO-012
file_path=runtime_contracts/VISUAL_MEDIA_PLAN_ROW_CONTRACT.md
owner=ShadowCreatorOS_Lightweight
applies_to=visual_media_plan_outputs
scope=row_wise_scene_planning_grammar
status_after_batch_1=DOCUMENTED_ONLY_NOT_ENFORCED
unlocks_nothing=true
```

## Purpose

This contract locks the visual media plan into a row-wise, scene-specific
planning format that cannot collapse into flat generic prose.

## Required Inputs

```text
scene_id
timecode
script_line
scene_intent
visual_role
method
cost_level
provider_lane
proof_requirement
reasoning
```

## Required Outputs

```text
rowwise_visual_plan
```

## Forbidden Behaviors

- flat generic visual plan
- missing reasoning
- no cost level
- no provider or local boundary
- B-roll ratio unproven

## Pass Conditions

- Every scene row carries intent, method, cost, boundary, proof, and reasoning.
- The plan remains planning-only and does not claim asset generation.

## Fail Conditions

- A plan omits scene reasoning or production boundaries.
- A plan presents itself as execution-ready without downstream gates.

## Evidence Required

```text
scene_rows
broll_ratio_breakdown
provider_boundary_notes
```

## Route Bindings

- `visual_media_plan`

## Schema Bindings

- `schemas/visual_media_plan_row.schema.json`

## Validator Bindings

- `validators/validate_visual_template_lock.py`

## Fixture Bindings

- Gold: `validators/fixtures/gold/visual_plan_rowwise_valid.md`
- Bad: `validators/fixtures/bad/visual_plan_flat_generic.md`

## Proof Artifacts

```text
visual_plan_validation_report.json
```
