# No Fake Pass Gate

```text
contract_id=C-SO-008
file_path=runtime_contracts/NO_FAKE_PASS_GATE.md
owner=ShadowCreatorOS_Lightweight
applies_to=all_validation_routes
scope=ban_unsupported_pass_claims
status_after_batch_1=DOCUMENTED_ONLY_NOT_ENFORCED
unlocks_nothing=true
route_bindings=[MEDIA_FACTORY_HANDOFF]
```

## Purpose

This gate bans misleading PASS claims that are not backed by a real evidence
bundle and explicit proof paths.

## Required Inputs

```text
pass_reason
evidence_bundle_id
claim_context
```

## Required Outputs

```text
pass_evidence_matrix
```

## Forbidden Behaviors

- `pass_reason=ffprobe_only`
- `pass_reason=file_exists_only`
- `pass_reason=exit_code_0_only`
- `pass_reason=keyword_hit_only`
- `pass_reason=contract_exists_only`
- `pass_reason=route_state_truth_without_evidence_bundle`
- `pass_reason=route_state_truth_without_audit_event`
- `pass_reason=route_unlock_without_validator_pass`

## Pass Conditions

- PASS points to concrete evidence artifacts.
- Evidence bundle ID is present and traceable.
- Route-state claims include the route-state capsule hash and Chitragupta
  audit event ID.

## Fail Conditions

- PASS is claimed from a forbidden reason.
- No evidence bundle exists.

## Evidence Required

```text
evidence_bundle_id
artifact_paths
validator_status
route_state_capsule_id
audit_event_id
```

## Route Bindings

- `all_routes`
- `MEDIA_FACTORY_HANDOFF`

## Schema Bindings

- `schemas/final_visual_media_generation_draft.schema.json`

## Validator Bindings

- `validators/validate_no_fake_pass_gate.py`

## Fixture Bindings

- Gold: `validators/fixtures/gold/pass_with_evidence_bundle.json`
- Bad: `validators/fixtures/bad/pass_reason_ffprobe_only.json`

## Proof Artifacts

```text
pass_evidence_matrix.txt
route_pass_evidence_matrix.txt
```
