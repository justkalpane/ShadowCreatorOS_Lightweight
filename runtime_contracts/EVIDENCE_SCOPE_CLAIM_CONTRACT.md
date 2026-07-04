# Evidence Scope Claim Contract

## Purpose

Production-sensitive claims must prove what cycle or persisted route state they
come from. Memory-only claims cannot pass.

## Required Fields

```text
claim=
evidence=
evidence_scope=
evidence_path=
command_output_or_file_reference=
status=PASS/PARTIAL/BLOCKED/NEEDS_CONFIRMATION
route_state_capsule_id=
route_state_capsule_hash=
audit_event_id=
```

## Allowed Evidence Scopes

- `current_cycle`
- `previous_cycle_with_step_reference`
- `persisted_route_state_with_hash`

## Blocked Evidence Scopes

- `memory_only`

## Rules

- `memory_only` cannot PASS.
- A production claim without an explicit evidence scope cannot exceed
  `NEEDS_CONFIRMATION`.
- Persisted route-state claims must cite a route-state hash or file path.
- Route-state transition claims must also cite the Chitragupta audit event
  that recorded the transition.
- `memory_only` cannot justify a route advancement, route unlock, or evidence
  bundle PASS claim.
