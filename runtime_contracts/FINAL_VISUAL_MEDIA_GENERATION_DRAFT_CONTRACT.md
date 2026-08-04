# Final Visual Media Generation Draft Contract

```text
contract_id=C-SO-013
file_path=runtime_contracts/FINAL_VISUAL_MEDIA_GENERATION_DRAFT_CONTRACT.md
owner=ShadowCreatorOS_Lightweight
applies_to=visual_media_generation_draft_outputs
scope=packet_preparation_only_until_route_gates_pass
status_after_batch_1=DOCUMENTED_ONLY_NOT_ENFORCED
unlocks_nothing=true
```

## Purpose

This contract defines the final visual generation draft as a packetized
preparation artifact, not an execution authorization.

## Required Inputs

```text
locked_script_id
locked_visual_plan_id
scene_packets
asset_generation_order
broll_ratio_proof
blocked_execution_state
```

## Required Outputs

```text
draft_packet
asset_generation_order
proof_requirements
```

## Forbidden Behaviors

- execution authorized by draft alone
- missing scene reasoning
- missing B-roll ratio proof
- missing provider or local boundary

## Pass Conditions

- The draft prepares packets, order, and proof expectations.
- The draft keeps execution blocked until route gates pass.

## Fail Conditions

- The draft claims production readiness or execution authority by itself.

## Evidence Required

```text
locked_script_reference
locked_visual_plan_reference
scene_packet_references
```

## Route Bindings

- `visual_media_generation_draft`
- `media_factory_handoff`

## Schema Bindings

- `schemas/final_visual_media_generation_draft.schema.json`

## Validator Bindings

- `validators/validate_visual_generation_depth.py`

## Fixture Bindings

- Gold: `validators/fixtures/gold/final_visual_draft_valid.md`
- Bad: `validators/fixtures/bad/final_visual_draft_authorizes_execution.md`

## Proof Artifacts

```text
draft_validation_report.json
```
