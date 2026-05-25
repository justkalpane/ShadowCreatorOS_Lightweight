# MAC-06.1O Shadow Output Mode Contract

## Purpose

Shadow OS uses the same internal execution standard across all output modes. Output mode changes what is shown to the user, not what must be executed.

## PROOF_MODE

Use for testing, audit, validation, and onboarding proof.

Must show:

- all locks
- all ledgers
- source maps
- exact rule evidence
- exact rule lineage
- quality gates
- governance gate
- final proof classification

## OPERATOR_MODE

Default for real production usage.

Must show:

- Shadow Boot / Route Summary
- Gate Summary
- Source Summary
- Quality Summary
- Final Output
- Content Engineering Packet
- Provider Boundary
- Compact Final Proof

Do not expose all internal ledger details unless needed. Still execute the full wrapper internally.

## DEBUG_MODE

Use when output quality, routing, rule consumption, source breadth, or validator behavior is suspected.

Must show detailed ledgers and validator-style proof.

## Shared Rules

- The internal execution standard is identical across `PROOF_MODE`, `OPERATOR_MODE`, and `DEBUG_MODE`.
- Output compression must not skip route locks, route manifests, mandatory file reads, source breadth, rule evidence, quality gates, governance, or provider boundary.
- If execution proof is missing internally, output must not claim `PASS`.
- Operator mode can pass only when compact proof confirms all required locks passed internally.

## MAC-06.1P-C Output Enforcement

For Shadow command aliases, the output mode is resolved only after command expansion succeeds.

Required compact proof fields for `OPERATOR_MODE`:

```text
output_mode=OPERATOR_MODE
operator_mode_used=true
operator_mode_compact_proof_present=true
shadow_command_alias_detected=true
raw_user_task_preserved=true
alias_matrix_entry_used=true
route_id_resolved=true
route_manifest_loaded=true
internal_wrapper_applied=true
task_route_lock_status=PASS
route_dependency_expansion_lock_status=PASS
consumption_lock_status=PASS
quality_lock_status=PASS
governance_lock_status=PASS
provider_boundary_present=true
no_n8n_provider_media_execution=true
```

If operator output hides detailed ledgers, it must still include a compact final proof with route, lock, source, rule-evidence, quality, governance, and provider-boundary status. Operator compression is a display choice only; it is not permission to skip internal proof.
