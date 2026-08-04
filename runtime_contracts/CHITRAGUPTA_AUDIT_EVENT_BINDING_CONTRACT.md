# Chitragupta Audit Event Binding Contract

```text
contract_id=C-SO-AUDIT-8K
file_path=runtime_contracts/CHITRAGUPTA_AUDIT_EVENT_BINDING_CONTRACT.md
owner=ShadowCreatorOS_Lightweight
route_id=MEDIA_FACTORY_HANDOFF
scope=bind_audit_event_to_every_route_state_transition
status=ACTIVE_BOUNDING_CONTRACT
unlocks_nothing=true
```

## Purpose

Chitragupta is the audit authority for route-state truth. Every transition in
the Media Factory handoff chain must be logged as an audit event, and the audit
event must carry the route-state capsule and evidence bundle references that
justify the transition.

## Required Inputs

```text
event_id
event_type
route_id
mission_id
job_id
cut_id
from_state
to_state
route_state_capsule_id
evidence_bundle_id
validator_ledger_hash
decision
blocked_reasons
timestamp
```

## Required Outputs

```text
audit_event_record
audit_event_hash
route_state_transition_link
evidence_bundle_link
```

## Binding Rules

- Every `MEDIA_FACTORY_HANDOFF` route-state transition requires an audit event.
- The audit event must reference the matching route-state capsule.
- The audit event must reference the matching evidence bundle.
- An audit event cannot replace validator proof.
- An audit event cannot replace human review, approval token, or route lock.

## Route Bindings

```text
MEDIA_FACTORY_HANDOFF
```

## Schema / Validator Bindings

```text
schemas/governance/chitragupta_audit_event.schema.json
schemas/runtime_state/route_state_capsule.schema.json
schemas/runtime_state/evidence_bundle.schema.json
validators/validate_chitragupta_audit_event.py
```

## Failure Conditions

- Missing evidence bundle.
- Missing route-state capsule.
- Missing validator ledger reference.
- Missing audit decision.
- Any attempted route advance with no audit event.

