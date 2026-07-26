# Phase 12L-C Inactive-To-Active Promotion Design

## 1. Objective
Design a safe mechanism for promoting inactive route drafts into active route registry files later, without performing the promotion in Phase 12L-C.

## 2. Blocker inherited from Phase 12L-B
`ACTIVE_REGISTRY_AUTO_DISCOVERY_RISK_CONFIRMED`

Phase 12L-B showed that active registry paths participate in discovery and inventory logic, so file presence alone cannot be assumed inert.

## 3. Promotion model options

| Option | Mechanism | Runtime risk | Requires code? | Reversible? | Recommendation |
|---|---|---|---|---|---|
| Option A | Manual copy from `route_drafts/` to active registry paths | High | No | Yes, but error-prone | Not recommended |
| Option B | Script-assisted promotion with preflight checks | Medium | Yes | Yes | Better than copy-only, but still too open-ended without a guardrail |
| Option C | Validator-gated promotion | Low | Yes | Yes | Recommended |
| Option D | Keep route drafts only and defer active files | Lowest | No | Yes | Safe fallback if approval stalls |
| Option E | Selector-first activation | Highest | Yes | No, not safely | Not recommended |

## 4. Recommended promotion model
`Option C — validator-gated promotion`

That is the safest practical model because it can enforce path checks, parse checks, collision checks, and selector-readiness checks before anything lands in `registries/route_manifests/` or `registries/route_slices/`.

## 5. Promotion boundary
- Active registry files remain blocked until the promotion gate passes.
- Selector binding remains a separate later phase.
- Route registration remains separate from runtime proof.
- No PASS or governed proof can be claimed by file creation alone.
