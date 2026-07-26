# Phase 12L-B Active Registry Inertness Audit

## 1. Objective
Determine whether files placed directly under the active route registry directories are inert before any selector binding work begins.

## 2. Blocker recap
Phase 12L blocked because active registry inertness was not proven.

## 3. Surfaces inspected

| Surface | Inspected? | Evidence found | Inertness implication | Notes |
|---|---|---|---|---|
| `runtime/state/active_runtime_truth_map.yaml` | Yes | Declares `registries/route_manifests/*.yaml` and `registries/route_slices/*.registry_slice.yaml` as globbed categories with default access limited to selected-route contexts. | Not inert by default | This is direct evidence that the active registry directories are part of runtime authority classification. |
| `validators/validate_mac06_1a_output.py` | Yes | Builds manifest and slice inventories by scanning `registries/route_manifests/*.yaml` and `registries/route_slices/*.registry_slice.yaml`. | Auto-discovery risk | Presence inside those directories is part of inventory construction. |
| `tests/shadow_runtime/run_batch8k_route_runtime_binding_check.py` | Yes | Hard-codes active route manifest/slice surfaces and their binding contracts in dry-run checks. | Not inert | Shows route files are treated as live binding surfaces in test logic. |
| `runtime/state/route_chain_mode_selector.yaml` | Yes | Defines active modes and allowed route IDs, including `SCRIPT_GENERATION` and `MEDIA_FACTORY_HANDOFF`. | Not inert | Selector behavior remains live and mode-driven. |
| `registries/route_manifests/script_generation.yaml` | Yes | Explicit `route_id: SCRIPT_GENERATION`, trigger terms, required contracts, required locks, and hard fail rules. | Not inert | Active manifest is executable policy, not placeholder content. |
| `registries/route_slices/script_generation.registry_slice.yaml` | Yes | Explicit `route_id: SCRIPT_GENERATION`, source manifest, actors, contracts, validators, and downstream routes. | Not inert | Slice is part of active route scope and dependency resolution. |
| `registries/route_manifests/full_video_pipeline.yaml` | Yes | Explicit `route_id: FULL_VIDEO_PIPELINE`, status `PARTIAL`, and active binding requirements. | Not inert | Downstream route manifest still participates in live policy. |
| `registries/route_slices/full_video_pipeline.registry_slice.yaml` | Yes | Explicit `route_id: FULL_VIDEO_PIPELINE`, runtime packet requirements, and binding gates. | Not inert | Shows active downstream slices are also live configuration. |
| `registries/route_manifests/media_factory_handoff.yaml` | Yes | Explicit trigger aliases, mandatory contracts, required output blocks, and selector-facing route law. | Not inert | Another active route surface with binding semantics. |
| `registries/route_slices/media_factory_handoff.registry_slice.yaml` | Yes | Explicit `route_id: MEDIA_FACTORY_HANDOFF`, runtime packet requirements, validators, and blocked execution unlocks. | Not inert | Active slice logic is rich and binding-aware. |

## 4. Classification
`ACTIVE_REGISTRY_AUTO_DISCOVERY_RISK_CONFIRMED`

## 5. Verdict
Active manifest/slice creation should not be retried yet. The repo shows active registry directories are part of discovery and inventory logic, so file presence alone cannot be assumed inert.
