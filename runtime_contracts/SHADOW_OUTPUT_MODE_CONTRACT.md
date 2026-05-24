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

