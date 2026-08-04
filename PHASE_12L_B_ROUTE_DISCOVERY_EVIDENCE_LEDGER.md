# Phase 12L-B Route Discovery Evidence Ledger

## 1. Objective
Record exact evidence about route discovery and registry loading before any active registry file creation.

## 2. Evidence table

| Evidence ID | File/path | Line/reference | Finding | Supports inertness? | Supports auto-discovery risk? | Notes |
|---|---|---|---|---|---|---|
| E-12LB-01 | `runtime/state/active_runtime_truth_map.yaml` | 18-31 | Declares `registries/route_manifests/*.yaml` and `registries/route_slices/*.registry_slice.yaml` as globbed file categories. | No | Yes | This is the strongest evidence that active registry directories are discovery surfaces, not inert storage. |
| E-12LB-02 | `runtime/state/active_runtime_truth_map.yaml` | 41-58 | Classifies contracts, skills, subskills, validators, and tests by runtime authority; validators and tests are mode-limited but still inventory-driven. | No | Yes | Shows the repository uses file-category authority rules rather than treating all files as passive. |
| E-12LB-03 | `validators/validate_mac06_1a_output.py` | 634-684 | `route_manifest_inventory()` scans `registries/route_manifests/*.yaml`, parses `route_id`, and builds a manifest inventory map. | No | Yes | Presence under `registries/route_manifests/` directly feeds runtime inventory. |
| E-12LB-04 | `validators/validate_mac06_1a_output.py` | 693-723 | `route_slice_inventory()` scans `registries/route_slices/*.registry_slice.yaml`, parses `route_id`, and builds a slice inventory map. | No | Yes | Presence under `registries/route_slices/` directly feeds runtime inventory. |
| E-12LB-05 | `tests/shadow_runtime/run_batch8k_route_runtime_binding_check.py` | 18-76 | Route/runtime binding checker asserts specific route-manifest and route-slice contract references. | No | Yes | Confirms registry files are consumed as binding artifacts in route validation. |
| E-12LB-06 | `runtime/state/route_chain_mode_selector.yaml` | 1-24 | `script_only` mode allows only `SCRIPT_GENERATION` and blocks media factory routes by default. | No | Yes | Selector remains active and route-gating remains live. |
| E-12LB-07 | `registries/route_manifests/script_generation.yaml` | 1-25, 34-66, 112-120 | Explicit active manifest with `SCRIPT_GENERATION`, trigger terms, mandatory contracts, mandatory registries, and required locks. | No | Yes | Not a placeholder; it is live route law. |
| E-12LB-08 | `registries/route_slices/script_generation.registry_slice.yaml` | 1-4, 45-66, 75-89 | Explicit active slice with `SCRIPT_GENERATION`, contracts, validators, and downstream route references. | No | Yes | Active slice participates in dependency resolution. |
| E-12LB-09 | `registries/route_manifests/full_video_pipeline.yaml` | 1-10, 15-20 | Explicit `FULL_VIDEO_PIPELINE` route policy, status `PARTIAL`, and live route dependencies. | No | Yes | Demonstrates downstream route manifests are also live policy surfaces. |
| E-12LB-10 | `registries/route_slices/full_video_pipeline.registry_slice.yaml` | 1-16, 72-91 | Explicit `FULL_VIDEO_PIPELINE` slice with route/runtime requirements and binding rules. | No | Yes | Downstream slice is active configuration. |
| E-12LB-11 | `registries/route_manifests/media_factory_handoff.yaml` | 1-16, 22-28, 33-66 | Explicit `MEDIA_FACTORY_HANDOFF` route law with mandatory contracts, skills, validators, and locks. | No | Yes | Shows active routes are governed by manifest content. |
| E-12LB-12 | `registries/route_slices/media_factory_handoff.registry_slice.yaml` | 1-15, 21-55, 72-93 | Explicit `MEDIA_FACTORY_HANDOFF` slice with validators, runtime packets, blocked unlocks, and laws. | No | Yes | Confirms slice files are active route governance artifacts. |

## 3. Missing evidence
No evidence was found proving that files created directly under `registries/route_manifests/` or `registries/route_slices/` are inert by mere presence alone.

What is still missing before active registry file creation:
- A selector or loader proof that ignores newly added files until explicit registration.
- A documented inactive-to-active promotion mechanism for registry files.
- A repo rule stating that active registry directory presence does not affect inventories, tests, or runtime selection.
- A binding simulation or dry-run proof showing new registry files remain unreachable until a later selector patch.
