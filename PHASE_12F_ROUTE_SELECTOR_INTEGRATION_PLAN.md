# Phase 12F Route Selector Integration Plan

## 1. Objective
Plan a later route-selector integration for `FILM_SCREENPLAY_GENERATION` without implementing it in Phase 12F.

## 2. Current selector/route surfaces inspected

| File | Exists? | Role | Film integration implication | Safe later action |
|---|---|---|---|---|
| `runtime/state/route_chain_mode_selector.yaml` | Yes | Top-level route-chain mode selector | Currently defaults to `script_only` and keeps `SCRIPT_GENERATION` as the active baseline | Add a dedicated film mode branch only after preparation gates pass |
| `registries/route_manifests/script_generation.yaml` | Yes | Active content/script route manifest | Canonical `SCRIPT_GENERATION` remains preserved and already owns the content-first trigger vocabulary | Leave intact; use as the regression baseline |
| `registries/route_slices/script_generation.registry_slice.yaml` | Yes | Active content/script route slice | This slice anchors the current content route dependency set | Do not alter in Phase 12F; preserve as the comparison slice |
| `registries/route_manifests/full_video_pipeline.yaml` | Yes | Downstream full video production route manifest | It already expresses a downstream, provider-gated production path | Reuse later only for downstream handoff, not as film-core routing law |
| `registries/route_slices/full_video_pipeline.registry_slice.yaml` | Yes | Downstream full video pipeline slice | It shows a larger production path that is still separate from film screenplay intent | Keep downstream and distinct from film screenplay generation |
| `registries/route_manifests/media_factory_handoff.yaml` | Yes | Media Factory handoff manifest | It confirms the repo already has a downstream production route family | Use later for handoff mapping, not selector substitution |
| `registries/route_slices/media_factory_handoff.registry_slice.yaml` | Yes | Media Factory handoff slice | It is a downstream slice with route-state and provider boundaries | Keep as a downstream target after screenplay approval |

## 3. Future integration sequence
1. Register the active film route manifest only after the supporting docs and proofs are complete.
2. Register the active film route slice only after the manifest exists and the slice dependencies are explicit.
3. Add selector branching only after fixtures, schemas, validators, and contracts are ready for enforcement.
4. Add route collision checks before any runtime routing is enabled.
5. Add content-preservation regression checks before film routing is allowed to affect `SCRIPT_GENERATION`.
6. Add a no-fake-PASS guard before any film result can be treated as approved.
7. Add downstream handoff mapping for visual, voice, editing, and media-factory paths.
8. Run a dry-run validation path before any runtime binding.
9. Only then allow runtime binding.

## 4. Route intent rules
- `write a 5-minute short film on NEET` -> future `FILM_SCREENPLAY_GENERATION`
- `write a screenplay about exam leak impact` -> future `FILM_SCREENPLAY_GENERATION`
- `YouTube script about NEET` -> preserve `SCRIPT_GENERATION`
- `Instagram reel about NEET` -> preserve content/social route
- `trailer for a film` -> downstream handoff, not film-core screenplay generation
- `thumbnail/title for a film` -> downstream packaging, not film-core route
- `cinematic explainer for YouTube` -> content route with cinematic style, not screenplay route unless explicitly requested

## 5. Required future dependencies
- Phase 12A fixtures
- Phase 12B schemas
- Phase 12C validators
- Phase 12D contracts
- Phase 12E unregistered route drafts

## 6. Explicit non-actions in Phase 12F
- route selector not modified
- active route manifests not modified
- active route slices not modified
- runtime behavior not changed
- routes not registered
- validators not bound
- schemas not bound
- contracts not bound
- PASS not claimed
- governed runtime proof not claimed

## 7. Recommended next implementation phase
`Phase 12G: active route manifest/slice registration preparation only`

Do not recommend direct selector modification unless the risk ledger supports it.
