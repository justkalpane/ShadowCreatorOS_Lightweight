# Phase 12L-F Promotion Options And Risk Ledger

## 1. Objective
Record promotion risks and constraints before any active registry file is created.

This packet preserves the Phase 12L-B classification token `ACTIVE_REGISTRY_AUTO_DISCOVERY_RISK_CONFIRMED` so the owner decision is grounded in the confirmed discovery risk.

## 2. Risk Ledger

| Risk ID | Risk | Evidence/source | Impact | Mitigation | Residual risk |
|---|---|---|---|---|---|
| R-12LF-01 | Active registry auto-discovery risk | Phase 12L-B / Phase 12L-C audit chain | New files could be discovered as live surfaces sooner than intended | Keep promotion validator-gated and separate from selector binding | Medium until an explicit promotion mechanism exists |
| R-12LF-02 | Route inventory visibility risk | `validators/validate_mac06_1a_output.py` and route inventory scans | A newly created registry file may appear in inventories | Require preflight checks before promotion | Medium |
| R-12LF-03 | Accidental selector binding risk | Live selector and route-chain law | Promotion could collapse into activation too early | Keep selector work in a later phase | Medium |
| R-12LF-04 | Content route collision risk | `SCRIPT_GENERATION` active route law | Film route could displace or blur the content route boundary | Preserve `SCRIPT_GENERATION` as content-only law | Medium |
| R-12LF-05 | False PASS/runtime-proof risk | Phase chain guardrails and checker boundary | Would misstate repo readiness as governed execution | Never treat repo file presence as runtime proof | Low if boundaries are honored |
| R-12LF-06 | Rollback risk | Active registry promotion path | Harder to unwind if active files are created carelessly | Define a delete-only rollback for promoted files | Medium |
| R-12LF-07 | Dirty worktree risk | Current repo state and many unrelated changes | Unrelated files might be staged or conflated with promotion work | Stage only the intended files | High in a dirty worktree |
| R-12LF-08 | Draft-to-active drift risk | Draft route history and promotion sequence | Draft semantics could be lost when copied to active locations | Keep a checker and explicit promotion gate between draft and active states | Medium |

## 3. Non-Negotiable Constraints

```text
route_selector_must_remain_unchanged=true
film_route_must_not_be_selector_bound=true
content_route_must_be_preserved=true
no_runtime_pass_claim=true
no_governed_runtime_proof_claim=true
rollback_plan_required=true
```

## 4. Rollback Requirement

Future promotion rollback must delete only:

```text
registries/route_manifests/film_screenplay_generation.yaml
registries/route_slices/film_screenplay_generation.registry_slice.yaml
```

And must verify:

```text
runtime/state/route_chain_mode_selector.yaml unchanged
SCRIPT_GENERATION preserved
FILM_SCREENPLAY_GENERATION not selector-bound
```
