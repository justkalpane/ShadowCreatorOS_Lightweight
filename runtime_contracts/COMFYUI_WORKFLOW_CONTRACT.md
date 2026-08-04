# ComfyUI Workflow Contract

```text
contract_id=C-SO-015
file_path=runtime_contracts/COMFYUI_WORKFLOW_CONTRACT.md
owner=ShadowCreatorOS_Lightweight
applies_to=comfyui_payloads,local_image_generation
scope=workflow_logging_and_failure_classification
status_after_batch_1=DOCUMENTED_ONLY_NOT_ENFORCED
unlocks_nothing=true
```

## Purpose

This contract defines how ComfyUI workflow payloads, local generation attempts,
and timeout classifications must be represented.

## Required Inputs

```text
workflow_json_path
model
sampler
steps
cfg
seed
width
height
timeout_seconds
```

## Required Outputs

```text
payload_log
node_graph_hash
output_image_path_or_failure_report
```

## Forbidden Behaviors

- unlogged workflow
- native 1920x1080 claim without hires plan
- timeout marked as pass
- missing failure classification

## Pass Conditions

- Workflow is logged and hashed.
- Output or failure is classified explicitly.

## Fail Conditions

- Payload cannot prove what was attempted.
- Timeout or local failure is obscured by a success label.

## Evidence Required

```text
workflow_json_reference
payload_log
failure_or_output_report
```

## Route Bindings

- `media_factory_handoff`

## Schema Bindings

- `schemas/comfyui_workflow_payload.schema.json`

## Validator Bindings

- `validators/validate_comfyui_payload.py`

## Fixture Bindings

- Gold: `validators/fixtures/gold/comfyui_payload_valid.json`
- Bad: `validators/fixtures/bad/comfyui_timeout_marked_pass.json`

## Proof Artifacts

```text
comfyui_run_report.json
```
