# Phase 13E_3 Next Patch Scope and Acceptance Gate

## 1. Objective

Define the safe next implementation boundary after the Phase 13E_3 coherence audit.

## 2. Recommended Next Phase

```text
Phase 13E_4: remaining director ownership and registry coherence patch
```

Phase 13E_4 should remain bounded. It should not attempt a whole-repo rewrite.

## 3. Proposed Phase 13E_4 File Scope

Primary candidate files:

```text
directors/distribution/saraswati.md
directors/supreme_vision/shakti.md
directors/strategy/narada.md
directors/DIRECTOR_REGISTRY_MANIFEST.yaml
directors/DIRECTORS_COMPLETE_REGISTRY.py
directors/DIRECTORS_05_TO_30_COMPLETE_SPECS.md
```

Recommended scope split if registry consumers are unclear:

```text
Phase 13E_4A: patch Saraswati, Shakti, and Narada ownership blocks only
Phase 13E_4B: director registry active-consumer audit and registry patch
```

## 4. Required Invariants

```text
SCRIPT_GENERATION_boundary_preserved=true
FILM_SCREENPLAY_GENERATION_boundary_preserved=true
downstream_packaging_is_not_cinema_core=true
selector_modified=false
active_route_registry_modified=false
runtime_behavior_changed=false
runtime_proof_claimed=false
pass_claimed=false
unrelated_dirty_files_preserved=true
```

## 5. Acceptance Gate

| Gate | Required evidence | Status now | Required before Phase 13E_4 completion |
| --- | --- | --- | --- |
| All 24 mythology surfaces exist | File inspection under `directors/` | PASS | Keep true. |
| All 24 surfaces have Phase 13E ownership blocks | Marker scan | PARTIAL, 21/24 | Patch Saraswati, Shakti, Narada. |
| Kali represented in registry truth | Registry scan | FAIL | Add or prepare registry mapping after consumer inspection. |
| Registry roles match cinema crafts | Registry content review | FAIL | Replace stale content/distribution role labels with cinema craft roles or mark legacy references. |
| SCRIPT_GENERATION preserved | Boundary statements and tests | PARTIAL | Ensure registry changes do not route content scripts into film core. |
| FILM_SCREENPLAY_GENERATION preserved | Boundary statements and tests | PARTIAL | Ensure film route remains cinema-preproduction focused. |
| Runtime proof boundary | PASS/proof phrase scan | PASS | Continue no runtime proof claim unless governed runtime provides it. |

## 6. Prohibited Changes For Phase 13E_4 Unless Separately Approved

```text
do_not_modify_route_selector=true
do_not_modify_active_route_manifests=true
do_not_modify_active_route_slices=true
do_not_modify_schemas=true
do_not_modify_validators=true
do_not_modify_runtime_contracts=true
do_not_modify_fixtures=true
do_not_push=true
```

## 7. Future Approval Phrase

```text
Approved: proceed with Phase 13E_4 remaining director ownership and registry coherence patch.
```

Do not infer this approval from the existence of this document.

## 8. Phase 13E_3 Verdict

```text
DIRECTOR_REGISTRY_COHERENCE_READY_FOR_BOUNDED_PATCH=true
SAFE_TO_CLAIM_FULL_24_CRAFT_REGISTRY_COHERENCE=false
SAFE_TO_CLAIM_CINEMA_ENGINE_FULLY_IMPLEMENTED=false
NEXT_ACTION=Phase 13E_4 remaining director ownership and registry coherence patch
```
