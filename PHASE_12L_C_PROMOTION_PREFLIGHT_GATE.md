# Phase 12L-C Promotion Preflight Gate

## 1. Objective
Define the preflight gate required before any inactive-to-active promotion.

## 2. Required gates

| Gate | Required evidence | Current status | Blocker if missing |
|---|---|---|---|
| Inactive drafts exist | Draft files under `route_drafts/film_screenplay_generation/` | Present | No promotion source exists |
| Inactive drafts parse | YAML/JSON draft files parse cleanly | Present from prior audit chain | Bad drafts must be repaired first |
| Active registry auto-discovery risk acknowledged | Phase 12L-B classification | Present | Promotion without this acknowledgement is unsafe |
| Promotion mechanism selected | A conservative promotion design exists | Present in Phase 12L-C docs | No clear safety model |
| Active target paths known | Registry target paths identified | Present | Promotion target is ambiguous |
| Content route preservation check | `SCRIPT_GENERATION` preservation remains explicit | Present in repo law | Content route could be displaced |
| Route selector remains unchanged | No selector modification yet | Present | Selector changes belong later |
| Selector binding deferred | Binding not allowed in this phase | Present | Would collapse separation of concerns |
| Route collision fixtures available | Phase 12A fixtures and collision review docs | Present | Collision behavior remains untested |
| Schema skeletons available | Phase 12B schema prep | Present | Promotion would outpace schema prep |
| Validator skeletons available | Phase 12C validator prep | Present | Promotion would outpace validation prep |
| Contract prep available | Phase 12D contract prep | Present | Promotion would outpace governance prep |
| No-fake-PASS constraints available | Phase 12I and related docs | Present | False completion risk |
| Rollback plan available | Explicit rollback rules documented | Present | Promotion would be hard to unwind |
| Owner approval phrase supplied | Future approval text recorded | Required later | No owner-governed promotion path |
| No runtime proof claimed | Repo-only design phase | Present | Runtime proof is not part of this phase |

## 3. Required target files for future promotion
`registries/route_manifests/film_screenplay_generation.yaml`
`registries/route_slices/film_screenplay_generation.registry_slice.yaml`

## 4. Future promotion gate verdict values
- `PROMOTION_ALLOWED`
- `PROMOTION_BLOCKED_PENDING_PREFLIGHT`
- `PROMOTION_BLOCKED_PENDING_OWNER_DECISION`
- `PROMOTION_BLOCKED_BY_RUNTIME_DISCOVERY_RISK`

Current verdict: `PROMOTION_BLOCKED_BY_RUNTIME_DISCOVERY_RISK`
