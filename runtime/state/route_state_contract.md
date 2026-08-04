# Route State Runtime Contract

## Purpose

Route execution must be stateful. A task should run boot stage once, lock one
route, consume the selected route dependencies, enter output phase, and produce
the deliverable. It must not restart boot or rescan unrelated repo areas after
route lock.

## Route State Capsule

Every production route run must maintain a route state capsule with:

```text
route_id=
route_manifest_path=
route_manifest_hash=
task_mode=
route_phase=
files_consumed=
file_hashes=
evidence_bundle_id=
evidence_bundle_schema_path=
validator_ledger=
validator_results=
bridge_job_packet_path=
bridge_job_packet_hash=
patch_transaction_id=
dependencies_complete=true/false
output_phase_started=true/false
last_completed_step=
next_required_step=
compaction_recovery_ready=true/false
historical_files_allowed=true/false
active_runtime_scope=
```

For the `MEDIA_FACTORY_HANDOFF` route family, route-state truth is not just a
snapshot. It is a gated transition record. A route-state capsule claiming
advance must also carry:

```text
required_validators=
required_artifacts=
required_evidence_bundle=
required_audit_event=
required_human_action=
required_token=
blocked_actions=
forbidden_next_states=
error_code_if_blocked=
pilot_prep_allowed=false
pilot_execution_allowed=false
full_render_allowed=false
audio_allowed=false
provider_allowed=false
davinci_allowed=false
no_fake_pass_route_regression_required=true
```

Allowed `route_phase` values:

- `BOOT_CONFIRMED`
- `TASK_CLASSIFIED`
- `ROUTE_LOCKED`
- `DEPENDENCIES_CONSUMED`
- `OUTPUT_PHASE_STARTED`
- `OUTPUT_GENERATED`
- `VALIDATED`
- `BLOCKED`

## Boot Stage Guard

Boot stage is entered once per task. Boot files may be reread after
`ROUTE_LOCKED` when the read ledger proves a real need. Repeated reads are not
blocked by count alone; they are blocked only when unchanged files are reread
without a documented route, validation, audit, hash, or semantic influence
reason.

After `ROUTE_LOCKED`, boot file rereads require one of:

- `file_hash_changed`
- `audit_mode`
- `validator_mode`
- `explicit_user_requested_compare`
- `route_manifest_changed`
- `krishna_directive_dependency_trace`
- `semantic_influence_verification`
- `compaction_recovery_validation`

## Read Ledger With Hashes

Each consumed file must be tracked with:

```text
file_path=
file_hash=
first_read_phase=
last_read_phase=
read_count=
reread_reason=
route_required=true/false
semantic_use_required=true/false
semantic_use_status=USED/NOT_USED/NOT_APPLICABLE/NOT_PROVEN
```

Unchanged file + already consumed + no allowed reread reason = block reread.

Allowed reread reasons:

- `file_hash_changed`
- `audit_mode`
- `validator_mode`
- `explicit_user_requested_compare`
- `route_manifest_changed`
- `krishna_directive_dependency_trace`
- `semantic_influence_verification`
- `compaction_recovery_validation`

## Compaction Recovery

If `compaction_detected=true`:

1. Load the route state capsule.
2. Verify `route_manifest_hash`.
3. Resume from `next_required_step`.
4. Do not restart boot unless `boot_state_invalid=true`.
5. Do not rescan registries, `outputs/missions`, or chat transcripts unless
   the route state explicitly allows audit or continuation mode.

## Output Phase Gate

Once `dependencies_complete=true`, the next phase is:

```text
route_phase=OUTPUT_PHASE_STARTED
output_phase_started=true
```

Additional repo expansion is blocked unless the selected route manifest
explicitly authorizes the downstream branch.

## Semantic Influence Map

File reads are not enough. Each mandatory consumed item must map to output:

```text
component_or_file=
rule_or_contract_used=
output_section=
output_line_or_block=
influence_type=
validator_check=
status=USED/NOT_USED/NOT_APPLICABLE
reason_if_not_used=
```

If a mandatory component is selected and `semantic_use_status=NOT_PROVEN`, the
route cannot declare `PASS`.

## Batch 4 Runtime Binding Surface

For media-factory route families, the route state capsule must also preserve
the runtime binding surface introduced by the governance/schema/validator layer:

```text
required_foundation_validators=
required_domain_validators=
validator_surface_bound=true/false
validator_surface_status=
evidence_bundle_required_for_pass_claims=true/false
bridge_job_packet_required_for_local_handoff=true/false
patch_transaction_required_for_repo_write_claims=true/false
```

If a media-factory route claims local handoff readiness without
`bridge_job_packet_required_for_local_handoff=true`, or claims PASS without an
`evidence_bundle_id`, the route state is incomplete and must be treated as
blocked.

## Media Factory Handshake Binding

The Media Factory handoff route is additionally bound to the Batch 8H / 8I /
8J proof surface and the Chitragupta audit layer.

```text
route_runtime_binding_contract=runtime_contracts/MEDIA_FACTORY_ROUTE_RUNTIME_BINDING_CONTRACT.md
chitragupta_audit_event_binding_contract=runtime_contracts/CHITRAGUPTA_AUDIT_EVENT_BINDING_CONTRACT.md
route_state_transition_audit_required=true
route_state_transition_evidence_required=true
route_state_transition_validation_required=true
route_state_transition_no_fake_pass_required=true
```

Route-state transitions to `PILOT_PREP_ALLOWED`, `PILOT_EXECUTION_ALLOWED`, or
`FULL_RENDER_UNLOCK_APPROVED` are blocked unless the required validator,
evidence bundle, route-state capsule, human review, approval token, and audit
event conditions exist together.
