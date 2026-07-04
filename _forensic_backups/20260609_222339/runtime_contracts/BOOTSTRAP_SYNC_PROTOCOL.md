# Bootstrap Sync Protocol

Whenever active startup docs, routing contracts, registries, proof docs, or validators change, update `handoff/agent_bootstrap/SHADOW_BOOTSTRAP_OPERATING_MODE_PROMPT.md`.

## Sync Rules

- Bootstrap prompt must include current routing matrix version.
- Bootstrap prompt must include current required contracts.
- Bootstrap prompt must include current output laws.
- Bootstrap prompt must include task routing and consumption enforcement.
- Bootstrap prompt must mention current validator expectations when proof docs change.
- Patch is incomplete if bootstrap is stale.
- Bootstrap prompt must mention route-state recovery, read ledger, boot-once
  guard, route-scoped registry slices, active runtime truth map, and output
  phase gate when repo-consumption recovery files change.

## Required Checklist

```text
bootstrap_updated_after_repo_change=true/false
bootstrap_mentions_current_contracts=true/false
bootstrap_mentions_current_routing_matrix=true/false
bootstrap_mentions_current_consumption_protocol=true/false
bootstrap_mentions_route_state_contract=true/false
bootstrap_mentions_read_ledger=true/false
bootstrap_mentions_output_phase_gate=true/false
```
