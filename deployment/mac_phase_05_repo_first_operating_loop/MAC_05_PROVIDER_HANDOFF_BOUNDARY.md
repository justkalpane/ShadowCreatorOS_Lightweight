# MAC-05 Provider Handoff Boundary

## Boundary Rule

MAC-05 planning does not execute providers.

## Allowed

- Create `provider_handoff_packet.json`
- Define provider preferences, constraints, cost gates, and approval requirements
- Prepare artifact routing paths

## Not Allowed

- Provider API calls
- Credential creation/use
- Paid media generation execution
- Publishing execution

## Contract Position

- Topic-to-context engineering remains repo-first.
- Provider handoff packet is downstream execution input only.
- Execution requires separate approval gate.

