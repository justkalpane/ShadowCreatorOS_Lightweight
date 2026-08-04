# Bootstrap Sync Protocol

Whenever active startup docs, routing contracts, registries, proof docs, or validators change, update `handoff/agent_bootstrap/SHADOW_BOOTSTRAP_OPERATING_MODE_PROMPT.md`.

## Sync Rules

- Bootstrap prompt must include current routing matrix version.
- Bootstrap prompt must include current required contracts.
- Bootstrap prompt must include current output laws.
- Bootstrap prompt must include task routing and consumption enforcement.
- Bootstrap prompt must mention current validator expectations when proof docs change.
- Patch is incomplete if bootstrap is stale.

## Required Checklist

```text
bootstrap_updated_after_repo_change=true/false
bootstrap_mentions_current_contracts=true/false
bootstrap_mentions_current_routing_matrix=true/false
bootstrap_mentions_current_consumption_protocol=true/false
```
