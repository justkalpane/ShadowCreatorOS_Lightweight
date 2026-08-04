# Visual QA Acceptance Gate

```text
contract_id=C-SO-005
file_path=runtime_contracts/VISUAL_QA_ACCEPTANCE_GATE.md
owner=ShadowCreatorOS_Lightweight
applies_to=pilot_render_review,final_visual_acceptance
scope=block_production_pass_without_visual_qa
status_after_batch_1=DOCUMENTED_ONLY_NOT_ENFORCED
unlocks_nothing=true
route_bindings=[MEDIA_FACTORY_HANDOFF, full_video_pipeline, editing_packaging]
```

## Purpose

This gate blocks production acceptance until visual QA artifacts exist and a
human review state is recorded.

## Required Inputs

```text
final_mp4_path
ffprobe_report
contact_sheet
source_vs_render_report
human_review_status
```

## Required Outputs

```text
visual_qa_verdict
acceptance_packet
```

## Forbidden Behaviors

- `pass_reason=ffprobe_only`
- `pass_reason=file_exists_only`
- `pass_reason=exit_code_0_only`
- missing contact sheet
- missing source-vs-render report
- no human review state

## Pass Conditions

- QA artifacts exist together.
- Human review is explicitly recorded as pass, fail, or pending-blocking.

## Fail Conditions

- Any required QA artifact is missing.
- Automation alone claims production acceptance.

## Evidence Required

```text
ffprobe_report
contact_sheet
source_vs_render_report
human_review_packet
evidence_bundle
route_state_capsule
chitragupta_audit_event
```

## Route Bindings

- `full_video_pipeline`
- `editing_packaging`

## Schema Bindings

- `schemas/final_visual_media_generation_draft.schema.json`

## Validator Bindings

- `validators/validate_visual_qa_acceptance.py`

## Fixture Bindings

- Gold: `validators/fixtures/gold/visual_qa_valid_full_packet.json`
- Bad: `validators/fixtures/bad/visual_qa_missing_contact_sheet.json`

## Proof Artifacts

```text
visual_qa_acceptance_packet.json
```
