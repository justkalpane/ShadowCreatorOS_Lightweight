# Phase 12G Active Route Registration Prep Plan

## 1. Objective
Phase 12G prepares the future active manifest/slice registration patch without performing registration.

## 2. Baseline verified

| Baseline item | Evidence inspected | Status | Notes |
|---|---|---|---|
| Phase 12F docs | `PHASE_12F_ROUTE_SELECTOR_INTEGRATION_PLAN.md`, `PHASE_12F_ROUTE_SELECTOR_RISK_LEDGER.md`, `PHASE_12F_ROUTE_REGISTRATION_ACCEPTANCE_GATE.md` | Verified | Phase 12F stayed planning-only and preserved `SCRIPT_GENERATION` |
| Route selector | `runtime/state/route_chain_mode_selector.yaml` | Verified | Default mode remains `script_only`; film routing is not active |
| Script generation manifest/slice | `registries/route_manifests/script_generation.yaml`, `registries/route_slices/script_generation.registry_slice.yaml` | Verified | Active content route remains the baseline and still owns content trigger terms |
| Full video pipeline manifest/slice | `registries/route_manifests/full_video_pipeline.yaml`, `registries/route_slices/full_video_pipeline.registry_slice.yaml` | Verified | Downstream production route remains separate from screenplay routing |
| Media factory handoff manifest/slice | `registries/route_manifests/media_factory_handoff.yaml`, `registries/route_slices/media_factory_handoff.registry_slice.yaml` | Verified | Downstream handoff exists for production packaging, not film-core selection |
| Phase 12A fixtures | `tests/fixtures/phase_12a_fixture_manifest.json` | Considered | Route selection, film packet, content preservation, downstream handoff, and no-fake-PASS fixtures already exist |
| Phase 12B schemas | `schemas/film/phase_12b_schema_manifest.json` | Considered | Film schema skeletons already exist and remain prep-only |
| Phase 12C validators | `validators/film/phase_12c_validator_manifest.json` | Considered | Film validator skeletons already exist but are not bound |
| Phase 12D contracts | `runtime_contracts/film/phase_12d_contract_manifest.json` | Considered | Film runtime contract skeletons already exist but are not bound |
| Phase 12E route drafts | `registries/route_drafts/film/phase_12e_route_draft_manifest.json` and draft YAML files | Considered | Film route is still unregistered and draft-only |

## 3. Future registration dependency order
1. Fixtures already exist.
2. Schema skeletons exist.
3. Validator skeletons exist.
4. Contract preparation exists.
5. Draft route manifest/slice preparation exists.
6. Active route manifest/slice registration.
7. Route selector integration.
8. Runtime evaluation.
9. Governed runtime proof only if governed runtime returns it.

## 4. Non-goals
- no active registration
- no selector update
- no runtime behavior change
- no PASS claim
- no governed runtime proof claim

