# MAC-07 Readiness Seal Plan

## Objective

Issue a strict readiness seal only after multi-agent review flow is proven and repo-first controls remain intact.

## Required Evidence Checklist

1. GitHub `main` is active lightweight source of truth.
2. Agent doctrine docs are present and current.
3. Historical source index exists and is reconciled.
4. Dossier #2 and #3 are committed and pushed.
5. MAC-06.1A fresh GitHub repo bootstrap proof completed.
6. MAC-06.1B output consolidation and chat approval gate completed.
7. MAC-06.1C source intelligence and research mode gate completed.
8. MAC-06.1 reviewer proof completed if user keeps external review inside onboarding seal.
9. MAC-06.2 Codex finalization proof completed if MAC-06.1 is included in seal.
10. Final git state is clean at seal time.
11. No n8n/provider/Gemini/OpenWebUI/old-runtime drift occurred during readiness proofs.
12. MAC-06.0B single-agent doctrine confirms basic operation does not require multiple installed agents.
13. MAC-06.1C native capability inventory and task-routing matrix are referenced by active runtime docs.
14. MAC-06.1A rerun includes freshness classification, research gate output, and tools/connectors/plugins + native capability assessment.
15. MAC-06.1A rerun must not execute until capability-routing artifacts exist (`native_capability_routing_matrix.yaml`, `agent_runtime_selection_index.yaml`) and are referenced by active contracts.

## Seal Outcome Options

- `PASS`: onboarding-ready for repo-first + multi-agent review production.
- `PARTIAL`: minor non-critical gaps remain; onboarding declaration blocked.
- `FAIL`: critical gates missing or drift detected.

## Explicit Boundary

A MAC-07 PASS does not authorize n8n/provider execution bus phases. Those begin only in MAC-09+ with explicit approval.

## Single-Agent Seal Interpretation

MAC-07 readiness may validate repo-first onboarding through one representative single-agent repo-aware path. Multi-agent review remains preserved for stronger quality review, not as a forced dependency for normal use.

MAC-06.1A is the primary portability proof for the lightweight OS. External reviewer proof remains valuable and preserved, but it is not required for basic single-agent operation unless the user explicitly adds it to the seal.

MAC-06.1B is the output-governance proof for lightweight product behavior. It ensures no default file sprawl and ensures user-facing chat approval control.
