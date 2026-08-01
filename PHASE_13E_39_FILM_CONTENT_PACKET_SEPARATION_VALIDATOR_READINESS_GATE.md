# Phase 13E_39 Film Content Packet Separation Validator Enforcement Readiness Gate

## 1. Objective

Phase 13E_39 defines the smallest safe enforcement patch for `validators/film/validation/validate_film_content_packet_separation.py` after Phase 13E_38 made film route-selection validation locally enforceable.

This phase is a readiness gate only. It does not modify validators, schemas, fixtures, selectors, active route manifests, active route slices, runtime behavior, directors, agents, subagents, skills, or subskills. It does not bind validators to runtime, does not generate film output, and does not claim PASS or governed runtime proof.

## 2. Current State

```text
phase=13E_39
base_head=5659490802f514d20e40b35d7868fed387844ac8
phase_13e_38_completed=true
route_selection_validator_local_enforcement=true
content_packet_separation_validator_status=SKELETON_ONLY
content_packet_separation_schema_status=SKELETON_ONLY
content_packet_separation_schema_required_field_count=0
film_output_schema_required_field_count=0
runtime_harness_status=FILM_RUNTIME_PROOF_BLOCKED_SKELETON_VALIDATORS
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

The worktree contains broad pre-existing dirty and untracked files. This readiness gate preserves them and stages only this Phase 13E_39 report.

## 3. Evidence Reviewed

| Evidence | Path or command | Finding | Readiness impact |
| --- | --- | --- | --- |
| Phase 13E_38 patch report | `PHASE_13E_38_FILM_ROUTE_SELECTION_VALIDATOR_ENFORCEMENT_PATCH_REPORT.md` | Route-selection validator is locally enforceable; runtime proof still blocked | Confirms next critical validator target |
| Route-selection validator test | `python3 tests/test_phase_13e38_film_route_selection_validator.py` | `phase_13e38_film_route_selection_validator_ok` | Confirms content route preservation can be consumed as fixture evidence |
| Runtime proof harness test | `python3 tests/test_phase_13e34_film_route_runtime_proof_harness.py` | Harness still reports skeleton validator blocker | Confirms no runtime proof claimed |
| Runtime proof harness | `python3 tools/film_runtime/film_route_runtime_proof_harness.py || true` | `FILM_RUNTIME_PROOF_BLOCKED_SKELETON_VALIDATORS` | Remaining validators block runtime proof |
| Target validator | `validators/film/validation/validate_film_content_packet_separation.py` | Phase 12C skeleton, `passed=false`, `enforced=false` | Needs bounded enforcement patch |
| Separation schema | `schemas/film/validation/film_content_packet_separation.schema.json` | Skeleton schema, zero required fields | Validator should not depend on schema enforcement yet |
| Film output schema | `schemas/film/output_packet/film_screenplay_output_packet.schema.json` | Skeleton schema, zero required fields | Film output packet validator remains blocked |
| No-fake-PASS schema | `schemas/film/validation/no_fake_film_pass.schema.json` | Skeleton schema, zero required fields | No-fake-PASS validator remains blocked |
| Content-preservation fixtures | `tests/fixtures/content_preservation/*.json` | Six positive `SCRIPT_GENERATION` preservation fixtures | Positive content boundary evidence |
| Film-packet fixtures | `tests/fixtures/film_packet_validation/*.json` | One positive film baseline and nine failure cases | Separation patch can use collision cases without claiming full film packet proof |
| No-fake-PASS fixtures | `tests/fixtures/no_fake_pass/*.json` | Seven future failure fixtures | Includes direct content-validator-for-film-packet blocker |

## 4. Fixture Coverage Summary

| Fixture family | Count | Should pass later | Should fail later | Readiness use for next patch |
| --- | ---: | ---: | ---: | --- |
| `content_preservation` | 6 | 6 | 0 | Positive content-route preservation cases |
| `film_packet_validation` | 10 | 1 | 9 | Film packet baseline plus content-packet and content-metric collision failures |
| `no_fake_pass` | 7 | 0 | 7 | Prohibits content validators passing film packets and fake runtime proof |
| `film_route_selection` | 10 | 10 | 0 | Already covered by Phase 13E_38; useful as boundary regression support only |

Relevant fixture facts:

```text
content_preservation_expected_route=SCRIPT_GENERATION
content_preservation_count=6
film_packet_validation_expected_route=FILM_SCREENPLAY_GENERATION
film_packet_validation_pass_later_count=1
film_packet_validation_fail_later_count=9
no_fake_pass_fail_later_count=7
direct_collision_fixture=tests/fixtures/no_fake_pass/content_validator_cannot_pass_film_packet.json
film_collision_fixture=tests/fixtures/film_packet_validation/content_packet_pretending_film_should_fail.json
content_metric_collision_fixture=tests/fixtures/film_packet_validation/hook_retention_only_packet_should_fail.json
```

## 5. Proposed Phase 13E_40 Scope

Phase 13E_40 should implement only local content-vs-film packet separation enforcement.

Allowed files:

```text
validators/film/validation/validate_film_content_packet_separation.py
tests/test_phase_13e40_film_content_packet_separation_validator.py
PHASE_13E_40_FILM_CONTENT_PACKET_SEPARATION_VALIDATOR_PATCH_REPORT.md
```

Allowed behavior:

- Convert `validate_film_content_packet_separation.py` from skeleton-only to local fixture/payload enforcement.
- Accept content-preservation payloads where `expected_route=SCRIPT_GENERATION`.
- Accept the positive minimal film packet fixture as film-route evidence without claiming full film packet schema validation.
- Reject content packets pretending to be film packets.
- Reject film packets that rely only on content hooks, re-hooks, retention, platform packaging, or content-validator claims.
- Preserve `runtime_behavior_changed=false`, `route_selector_modified=false`, `validator_bound_to_runtime=false`, `pass_claimed=false`, and `governed_runtime_proof_claimed=false`.
- Keep empty-payload calls non-proof-producing so the runtime proof harness remains blocked until governed validator inputs are designed.

Prohibited behavior:

- Do not modify the route selector.
- Do not modify active route manifests or active route slices.
- Do not modify `validators/film/route/validate_film_route_selection.py`.
- Do not modify output-packet or no-fake-PASS validators.
- Do not modify film schemas or fixtures.
- Do not bind validators to runtime.
- Do not update the runtime proof harness.
- Do not claim film packet schema PASS.
- Do not claim governed runtime proof.

## 6. Proposed Local Payload Rules

| Payload class | Expected validator behavior |
| --- | --- |
| `fixture_family=content_preservation`, `expected_route=SCRIPT_GENERATION` | Pass local separation if the payload remains content-mode and does not claim film-core authority |
| `fixture_family=film_packet_validation`, positive film baseline | Pass separation only for route boundary, not full screenplay packet quality |
| Content packet pretending film | Fail local separation |
| Hook/retention-only film packet | Fail local separation |
| No-fake-PASS content-validator-for-film-packet fixture | Fail local separation |
| Runtime artifact or governed proof claims | Fail or remain blocked; do not validate as runtime proof |

## 7. Acceptance Matrix For Phase 13E_40

| Gate | Required evidence | Must pass? |
| --- | --- | --- |
| Separation validator no longer skeleton-only for payloads | Payload calls return local enforced statuses | yes |
| Content preservation fixtures pass | Six `content_preservation` fixtures preserve `SCRIPT_GENERATION` | yes |
| Positive film baseline passes route-boundary separation only | `valid_minimal_film_packet.json` accepted as film route shape boundary | yes |
| Content packet pretending film fails | `content_packet_pretending_film_should_fail.json` rejected | yes |
| Hook/retention-only packet fails | `hook_retention_only_packet_should_fail.json` rejected | yes |
| Content validator cannot pass film packet | `content_validator_cannot_pass_film_packet.json` rejected | yes |
| Route-selection validator regression passes | `python3 tests/test_phase_13e38_film_route_selection_validator.py` | yes |
| Runtime harness still blocks honestly | Harness remains blocked until all critical validators and schemas are enforceable | yes |
| Selector unchanged | `runtime/state/route_chain_mode_selector.yaml` not modified | yes |
| Active registries unchanged | Active film/script route manifest/slice files not modified | yes |
| Dirty worktree protected | Stage only Phase 13E_40 scoped files | yes |

## 8. Current Gate Verdict

```text
PHASE_13E_39_STATUS=FILM_CONTENT_PACKET_SEPARATION_VALIDATOR_READINESS_GATE_COMPLETE
READINESS_GATE_ONLY=true
PHASE_13E_38_ROUTE_SELECTION_VALIDATOR_CONFIRMED=true
CONTENT_PACKET_SEPARATION_VALIDATOR_SKELETON_ONLY_CONFIRMED=true
CONTENT_PACKET_SEPARATION_SCHEMA_SKELETON_ONLY_CONFIRMED=true
CONTENT_PRESERVATION_FIXTURES_AVAILABLE=true
FILM_PACKET_COLLISION_FIXTURES_AVAILABLE=true
NO_FAKE_PASS_COLLISION_FIXTURES_AVAILABLE=true
CONTENT_PACKET_SEPARATION_READY_FOR_NARROW_PATCH=true
FILM_OUTPUT_PACKET_VALIDATOR_STILL_BLOCKED_BY_SCHEMA_SKELETON=true
NO_FAKE_FILM_PASS_VALIDATOR_STILL_BLOCKED_BY_PROOF_FIELD_CONTRACT=true
RUNTIME_HARNESS_STATUS=FILM_RUNTIME_PROOF_BLOCKED_SKELETON_VALIDATORS
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
FINAL_VERDICT=READY_FOR_NARROW_CONTENT_PACKET_SEPARATION_VALIDATOR_PATCH
```

## 9. Recommended Next Phase

Phase 13E_40: film content packet separation validator enforcement patch

Phase 13E_40 should implement only `validators/film/validation/validate_film_content_packet_separation.py`, one focused test file, and one patch report. It should not modify selector, active registries, schemas, fixtures, the runtime harness, or unrelated validators.
