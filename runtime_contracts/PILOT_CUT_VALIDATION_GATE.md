# Pilot Cut Validation Gate

```text
contract_id=C-SO-007
file_path=runtime_contracts/PILOT_CUT_VALIDATION_GATE.md
owner=ShadowCreatorOS_Lightweight
applies_to=pilot_render_unlocks,full_video_pipeline
scope=block_full_render_before_c04a_pilot_pass
status_after_batch_1=DOCUMENTED_ONLY_NOT_ENFORCED
unlocks_nothing=true
route_bindings=[MEDIA_FACTORY_HANDOFF, full_video_pipeline]
```

## Purpose

This contract blocks full render attempts until the chosen pilot cut, currently
`C04a`, has passed QA and human review.

## Required Inputs

```text
pilot_cut_id
pilot_status
qa_status
human_review_status
```

## Required Outputs

```text
pilot_verdict
full_render_unlock_state
```

## Forbidden Behaviors

- full render before pilot
- pilot with no QA plan
- pilot with no human review state

## Pass Conditions

- `pilot_cut_id=C04a`
- Pilot has QA artifacts and a review state.
- Full render remains locked until pilot verdict is positive and approved.

## Fail Conditions

- Full render is allowed from technical output alone.
- Pilot evidence is incomplete.

## Evidence Required

```text
pilot_manifest
contact_sheet
source_vs_render_report
human_review_packet
evidence_bundle
route_state_capsule
chitragupta_audit_event
```

## Route Bindings

- `full_video_pipeline`

## Schema Bindings

- `schemas/final_visual_media_generation_draft.schema.json`

## Validator Bindings

- `validators/validate_pilot_cut_gate.py`

## Fixture Bindings

- Gold: `validators/fixtures/gold/pilot_c04a_valid.json`
- Bad: `validators/fixtures/bad/full_render_before_pilot.json`

## Proof Artifacts

```text
pilot_cut_verdict.md
```
