# Phase 13E_37 Critical Film Validator Enforcement Readiness Gate

## 1. Objective

Phase 13E_37 determines the smallest safe validator-enforcement patch sequence after Phase 13E_36 moved the film proof harness past the route-state schema blocker.

This phase is a readiness gate only. It does not modify validators, schemas, fixtures, selector, active route manifests, active route slices, runtime behavior, directors, agents, subagents, skills, or subskills. It does not execute governed runtime proof, does not generate film output, and does not claim PASS or governed runtime proof.

## 2. Current State

```text
phase=13E_37
base_head=ba3c789414a1166506d73999841bcae899dc2275
phase_13e_36_completed=true
harness_status=FILM_RUNTIME_PROOF_BLOCKED_SKELETON_VALIDATORS
route_state_schema_gap_resolved=true
route_state_schema_compatible=true
critical_film_validators_enforceable=false
film_output_schema_enforceable=false
runtime_execution_performed=false
film_output_generated=false
runtime_behavior_changed=false
selector_modified=false
active_route_manifest_modified=false
active_route_slice_modified=false
schemas_modified=false
validators_modified=false
fixtures_modified=false
tests_modified=false
pass_claimed=false
governed_runtime_proof_claimed=false
worktree_dirty=true
```

The worktree contains broad pre-existing dirty and untracked files. This gate preserves them and stages only this Phase 13E_37 report.

## 3. Evidence Reviewed

| Evidence | Path or command | Finding | Readiness impact |
| --- | --- | --- | --- |
| Phase 13E_36 patch report | `PHASE_13E_36_FILM_ROUTE_STATE_SCHEMA_SUPPORT_PATCH_REPORT.md` | Harness blocker advanced to skeleton validators | Confirms schema gap is resolved |
| Film proof harness | `python3 tools/film_runtime/film_route_runtime_proof_harness.py || true` | `FILM_RUNTIME_PROOF_BLOCKED_SKELETON_VALIDATORS` | Next blocker is validator enforcement |
| Phase 13E_36 test | `python3 tests/test_phase_13e36_film_route_state_schema_support.py` | `phase_13e36_film_route_state_schema_support_ok` | Route-state schema support is covered |
| Phase 13E_34 harness test | `python3 tests/test_phase_13e34_film_route_runtime_proof_harness.py` | `phase_13e34_film_route_runtime_proof_harness_ok` | Harness still blocks honestly |
| Critical route validator | `validators/film/route/validate_film_route_selection.py` | `SKELETON_ONLY`, `passed=false`, `enforced=false` | First safe enforcement target |
| Critical output validator | `validators/film/output_packet/validate_film_screenplay_packet.py` | `SKELETON_ONLY`, `passed=false`, `enforced=false` | Requires stronger packet/schema design before enforcement |
| Critical no-fake-PASS validator | `validators/film/validation/validate_no_fake_film_pass.py` | `SKELETON_ONLY`, `passed=false`, `enforced=false` | Requires explicit proof field contract |
| Critical separation validator | `validators/film/validation/validate_film_content_packet_separation.py` | `SKELETON_ONLY`, `passed=false`, `enforced=false` | Good early target, but safest after route-selection semantics |
| Film output schema | `schemas/film/output_packet/film_screenplay_output_packet.schema.json` | Skeleton-only, zero required fields | Blocks output packet proof |
| Phase 12A fixtures | `tests/fixtures/phase_12a_fixture_manifest.json` | 40 fixtures available | Fixtures support validator enforcement sequence |

## 4. Fixture Coverage Summary

| Fixture family | Count | Should pass later | Should fail later | Coverage use |
| --- | ---: | ---: | ---: | --- |
| `film_route_selection` | 10 | 10 | 0 | Best first validator enforcement target because expected routes are explicit |
| `film_packet_validation` | 10 | 1 | 9 | Supports screenplay packet validator after schema required fields are defined |
| `no_fake_pass` | 7 | 0 | 7 | Supports no-fake-PASS validator after proof field contract is precise |
| `content_preservation` | 6 | 6 | 0 | Supports route-selection and content-vs-film separation preservation |

Route-selection fixture expected-route distribution:

```text
SCRIPT_GENERATION=4
FILM_SCREENPLAY_GENERATION=3
FULL_VIDEO_PIPELINE=1
FILM_RELEASE_PACKAGING=1
FILM_RELEASE_DISTRIBUTION=1
```

This distribution makes `validate_film_route_selection.py` the safest first enforcement target because it can verify explicit route expectations without claiming runtime proof or film output quality.

## 5. Critical Validator Readiness Table

| Validator | Current state | Fixture support | Enforcement readiness | Recommended phase |
| --- | --- | --- | --- | --- |
| `validators/film/route/validate_film_route_selection.py` | Skeleton-only | 10 route-selection fixtures plus 6 content-preservation fixtures | READY_FOR_NARROW_PATCH | Phase 13E_38 |
| `validators/film/validation/validate_film_content_packet_separation.py` | Skeleton-only | Content preservation, no-fake-PASS, and film packet collision fixtures | READY_AFTER_ROUTE_SELECTION | Later patch |
| `validators/film/output_packet/validate_film_screenplay_packet.py` | Skeleton-only | 10 film-packet fixtures | BLOCKED_BY_OUTPUT_SCHEMA_SKELETON | Later patch after output schema required fields |
| `validators/film/validation/validate_no_fake_film_pass.py` | Skeleton-only | 7 no-fake-PASS fixtures | BLOCKED_BY_PROOF_FIELD_CONTRACT | Later patch after proof field contract |

## 6. Proposed Phase 13E_38 Scope

Phase 13E_38 should implement only the route-selection validator.

Allowed files:

```text
validators/film/route/validate_film_route_selection.py
tests/test_phase_13e38_film_route_selection_validator.py
PHASE_13E_38_FILM_ROUTE_SELECTION_VALIDATOR_ENFORCEMENT_PATCH_REPORT.md
```

Allowed behavior:

- Convert `validate_film_route_selection.py` from skeleton-only to enforceable fixture/payload validation.
- Validate explicit `input_prompt`, `expected_route`, and `expected_mode` fields.
- Enforce route-selection expectations from `tests/fixtures/film_route_selection/*.json`.
- Include content-preservation fixtures that must remain `SCRIPT_GENERATION`.
- Preserve `runtime_behavior_changed=false`, `route_selector_modified=false`, `validator_bound_to_runtime=false`, and `governed_runtime_proof_claimed=false`.
- Return PASS only for validator-local payload correctness, not governed runtime proof.
- Keep the Phase 13E_34 harness blocked until all critical validators are enforceable.

Prohibited behavior:

- Do not modify the route selector.
- Do not modify active route manifests or active route slices.
- Do not modify film output schemas.
- Do not modify no-fake-PASS or output-packet validators in Phase 13E_38.
- Do not bind validators to runtime.
- Do not execute runtime proof.
- Do not generate film output.
- Do not claim governed runtime proof.

## 7. Future Patch Sequence After Phase 13E_38

| Sequence | Target | Reason |
| --- | --- | --- |
| 1 | Route-selection validator | Cleanest fixture support and lowest proof-risk |
| 2 | Content-vs-film packet separation validator | Protects `SCRIPT_GENERATION` and prevents content validators from passing film packets |
| 3 | Film output schema required-field patch | Needed before screenplay packet validator can enforce output quality |
| 4 | Film screenplay packet validator | Requires schema-required fields and packet fixtures |
| 5 | No-fake-film-PASS validator | Requires proof-field contract and runtime evidence boundaries |
| 6 | Harness update | Harness should advance only when all critical validators are enforceable |

## 8. Acceptance Matrix For Phase 13E_38

| Gate | Required evidence | Must pass? |
| --- | --- | --- |
| Route-selection validator no longer skeleton-only | Validator returns enforced status for fixture payloads | yes |
| Film route fixtures pass | RS-001, RS-002, RS-003 resolve to `FILM_SCREENPLAY_GENERATION` | yes |
| Content route fixtures pass | RS-004, RS-005, RS-006, RS-010 and CP fixtures preserve `SCRIPT_GENERATION` | yes |
| Downstream route fixtures pass | Trailer, thumbnail/title, and full pipeline fixtures resolve downstream | yes |
| Selector unchanged | `runtime/state/route_chain_mode_selector.yaml` not modified | yes |
| Active registries unchanged | Film and script route manifest/slice files not modified | yes |
| Runtime proof unclaimed | `pass_claimed=false` and `governed_runtime_proof_claimed=false` | yes |
| Harness still blocked | Phase 13E_34 harness remains blocked because other critical validators are skeleton-only | yes |
| Dirty worktree protected | Stage only Phase 13E_38 files | yes |

## 9. Current Gate Verdict

```text
PHASE_13E_37_STATUS=CRITICAL_FILM_VALIDATOR_ENFORCEMENT_READINESS_GATE_COMPLETE
READINESS_GATE_ONLY=true
ROUTE_STATE_SCHEMA_GAP_RESOLVED=true
HARNESS_STATUS=FILM_RUNTIME_PROOF_BLOCKED_SKELETON_VALIDATORS
CRITICAL_FILM_VALIDATORS_SKELETON_ONLY_CONFIRMED=true
ROUTE_SELECTION_VALIDATOR_READY_FOR_NARROW_PATCH=true
CONTENT_PACKET_SEPARATION_VALIDATOR_READY_AFTER_ROUTE_SELECTION=true
FILM_OUTPUT_PACKET_VALIDATOR_BLOCKED_BY_SCHEMA_SKELETON=true
NO_FAKE_FILM_PASS_VALIDATOR_BLOCKED_BY_PROOF_FIELD_CONTRACT=true
PHASE_12A_FIXTURES_AVAILABLE=true
PHASE_12B_SCHEMAS_AVAILABLE_BUT_SKELETON=true
PHASE_12C_VALIDATORS_AVAILABLE_BUT_SKELETON=true
RUNTIME_EXECUTION_PERFORMED=false
FILM_OUTPUT_GENERATED=false
RUNTIME_BEHAVIOR_CHANGED=false
SELECTOR_MODIFIED=false
ACTIVE_ROUTE_MANIFESTS_MODIFIED=false
ACTIVE_ROUTE_SLICES_MODIFIED=false
SCHEMAS_MODIFIED=false
VALIDATORS_MODIFIED=false
FIXTURES_MODIFIED=false
TESTS_MODIFIED=false
PASS_CLAIMED=false
RUNTIME_PROOF_CLAIMED=false
GOVERNED_RUNTIME_PROOF_CLAIMED=false
FINAL_VERDICT=READY_FOR_NARROW_ROUTE_SELECTION_VALIDATOR_ENFORCEMENT_PATCH
```

## 10. Recommended Next Phase

Phase 13E_38: film route selection validator enforcement patch

Phase 13E_38 should implement only `validators/film/route/validate_film_route_selection.py`, its focused tests, and its patch report. It should not modify selector/registry files, should not bind runtime, and should not claim governed runtime proof.
