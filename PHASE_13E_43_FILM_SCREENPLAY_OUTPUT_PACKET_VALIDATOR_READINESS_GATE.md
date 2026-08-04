# Phase 13E_43 Film Screenplay Output Packet Validator Enforcement Readiness Gate

## 1. Objective

Phase 13E_43 defines the smallest safe enforcement patch for `validators/film/output_packet/validate_film_screenplay_packet.py` after Phase 13E_42 added required-field support to the film screenplay output schema.

This phase is a readiness gate only. It does not modify schemas, validators, fixtures, selectors, active route manifests, active route slices, runtime behavior, directors, agents, subagents, skills, or subskills. It does not bind validators to runtime, does not generate film output, and does not claim PASS or governed runtime proof.

## 2. Current State

```text
phase=13E_43
base_head=64968b119554effd2e1a40def97f6d8e8037fe26
phase_13e_42_completed=true
film_screenplay_output_schema_required_field_support=true
film_screenplay_output_schema_required_field_count=20
film_screenplay_output_schema_enforceable_for_required_fields=true
film_screenplay_packet_validator_status=SKELETON_ONLY
route_selection_validator_local_enforcement=true
content_packet_separation_validator_local_enforcement=true
no_fake_film_pass_validator_status=SKELETON_ONLY
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

The worktree contains broad pre-existing dirty and untracked files. This readiness gate preserves them and stages only this Phase 13E_43 report.

## 3. Evidence Reviewed

| Evidence | Path or command | Finding | Readiness impact |
| --- | --- | --- | --- |
| Phase 13E_42 patch report | `PHASE_13E_42_FILM_SCREENPLAY_OUTPUT_SCHEMA_REQUIRED_FIELD_PATCH_REPORT.md` | Output schema now has 20 required fields; runtime proof still blocked | Confirms schema prerequisite exists |
| Output schema | `schemas/film/output_packet/film_screenplay_output_packet.schema.json` | Required field count is 20; schema metadata remains unbound | Ready for local validator consumption |
| Output validator | `validators/film/output_packet/validate_film_screenplay_packet.py` | Phase 12C skeleton, `passed=false`, `enforced=false` | Target for next narrow patch |
| Film packet fixtures | `tests/fixtures/film_packet_validation/*.json` | One positive baseline and nine future failure fixtures | Defines validator pass/fail behavior |
| Runtime proof harness | `python3 tools/film_runtime/film_route_runtime_proof_harness.py || true` | `FILM_RUNTIME_PROOF_BLOCKED_SKELETON_VALIDATORS`; `film_output_schema_enforceable=true`; `film_output_schema_required_field_count=20` | Confirms schema blocker is resolved but validator blocker remains |
| Phase 13E_42 test | `python3 tests/test_phase_13e42_film_screenplay_output_schema_required_fields.py` | `phase_13e42_film_screenplay_output_schema_required_fields_ok` | Confirms schema required-field support |
| Phase 13E_40 test | `python3 tests/test_phase_13e40_film_content_packet_separation_validator.py` | `phase_13e40_film_content_packet_separation_validator_ok` | Confirms content/film separation regression |
| Phase 13E_38 test | `python3 tests/test_phase_13e38_film_route_selection_validator.py` | `phase_13e38_film_route_selection_validator_ok` | Confirms route-selection regression |

## 4. Schema Readiness Summary

```text
schema_required_count=20
schema_required=route_state_capsule,film_intent_lock,logline,theme,premise,genre,tone,protagonist_want,protagonist_need,protagonist_flaw,protagonist_arc,opposing_force,beat_sheet,scene_dramaturgy_map,dialogue_subtext_pass,visual_motif_system,style_bible,screenplay_body,film_validation_scorecard,no_fake_pass_gate
schema_runtime_behavior_changed=false
schema_route_selector_modified=false
schema_enforcement_bound=false
schema_validator_bound=false
schema_governed_runtime_proof_claimed=false
```

The schema can now support local required-field validation, but remains unbound to runtime.

## 5. Film Packet Fixture Coverage

| Fixture | Expected result | Should pass later | Should fail later | Validator readiness use |
| --- | --- | ---: | ---: | --- |
| `valid_minimal_film_packet.json` | `PASS_LATER` | true | false | Positive output packet baseline |
| `missing_beat_sheet_should_fail.json` | `FAIL_LATER` | false | true | Missing direct required field |
| `missing_character_arc_should_fail.json` | `FAIL_LATER` | false | true | Missing translated character arc fields |
| `missing_scene_turns_should_fail.json` | `FAIL_LATER` | false | true | Missing scene dramaturgy map content |
| `missing_dialogue_subtext_should_fail.json` | `FAIL_LATER` | false | true | Missing dialogue subtext pass |
| `missing_visual_motif_should_fail.json` | `FAIL_LATER` | false | true | Missing visual motif system |
| `missing_camera_composition_should_fail.json` | `FAIL_LATER` | false | true | Camera/composition remains delegated to style/craft validators |
| `missing_validation_scorecard_should_fail.json` | `FAIL_LATER` | false | true | Missing film validation scorecard |
| `content_packet_pretending_film_should_fail.json` | `FAIL_LATER` | false | true | Collision already covered by separation validator, but output validator should reject too |
| `hook_retention_only_packet_should_fail.json` | `FAIL_LATER` | false | true | Reject content-metric-only packet as non-film packet |

## 6. Proposed Phase 13E_44 Scope

Phase 13E_44 should implement only local film screenplay output packet enforcement.

Allowed files:

```text
validators/film/output_packet/validate_film_screenplay_packet.py
tests/test_phase_13e44_film_screenplay_output_packet_validator.py
PHASE_13E_44_FILM_SCREENPLAY_OUTPUT_PACKET_VALIDATOR_PATCH_REPORT.md
```

Allowed behavior:

- Convert `validate_film_screenplay_packet.py` from skeleton-only to local fixture/payload enforcement.
- Load and consume `schemas/film/output_packet/film_screenplay_output_packet.schema.json`.
- Require all schema `required` fields for actual packet payloads.
- Accept the positive minimal fixture only when represented as a validator-local synthetic packet containing required schema fields.
- Reject fixture payloads that declare missing required fields.
- Reject content packets pretending to be film packets.
- Reject hook/re-hook/retention-only packets as non-film output packets.
- Preserve `runtime_behavior_changed=false`, `route_selector_modified=false`, `validator_bound_to_runtime=false`, `pass_claimed=false`, and `governed_runtime_proof_claimed=false`.
- Keep empty-payload calls non-proof-producing so the runtime proof harness remains blocked until governed validator inputs are designed.

Prohibited behavior:

- Do not modify the route selector.
- Do not modify active route manifests or active route slices.
- Do not modify output schema required fields in Phase 13E_44.
- Do not modify `validators/film/validation/validate_no_fake_film_pass.py`.
- Do not modify route-selection or content-separation validators.
- Do not modify fixtures.
- Do not bind validators to runtime.
- Do not update the runtime proof harness.
- Do not claim film runtime proof.
- Do not generate film output.

## 7. Fixture-To-Packet Test Strategy For Phase 13E_44

Because Phase 12A fixtures are summary fixtures rather than complete screenplay packets, Phase 13E_44 tests should use two layers:

| Test layer | Purpose |
| --- | --- |
| Fixture classification tests | Ensure all `FAIL_LATER` fixtures fail for the intended missing/collision reason and the `PASS_LATER` fixture maps to a complete synthetic packet |
| Synthetic packet tests | Build one minimal packet with every schema-required field and confirm local validation passes without runtime proof |

This avoids pretending that summary fixtures are full runtime output packets.

## 8. Acceptance Matrix For Phase 13E_44

| Gate | Required evidence | Must pass? |
| --- | --- | --- |
| Output validator no longer skeleton-only for payloads | Payload calls return local enforced statuses | yes |
| Empty payload remains non-proof-producing | Empty payload returns non-proof status for harness compatibility | yes |
| Schema consumed locally | Validator loads schema and checks required fields | yes |
| Complete synthetic film packet passes | One packet containing all 20 required fields passes local validation | yes |
| Missing required fields fail | Missing-field cases fail with clear field ledger | yes |
| Content packet pretending film fails | Collision fixture fails | yes |
| Hook/retention-only packet fails | Content-metric-only fixture fails | yes |
| Existing route-selection regression passes | Phase 13E_38 test passes | yes |
| Existing content-separation regression passes | Phase 13E_40 test passes | yes |
| Runtime harness still blocks honestly | Harness remains blocked until no-fake-PASS validator and governed inputs are ready | yes |
| Selector/registries unchanged | No route selector or active registry files modified | yes |
| Dirty worktree protected | Stage only Phase 13E_44 scoped files | yes |

## 9. Remaining Blockers After Phase 13E_44

Even after the next patch, runtime proof should remain blocked because:

- `validators/film/validation/validate_no_fake_film_pass.py` will still be skeleton-only.
- The runtime proof harness still calls validators with empty payloads.
- Governed runtime invocation inputs have not been designed or executed.
- No film output has been generated.
- No runtime artifact IDs or completion certificates can be invented.

## 10. Current Gate Verdict

```text
PHASE_13E_43_STATUS=FILM_SCREENPLAY_OUTPUT_PACKET_VALIDATOR_READINESS_GATE_COMPLETE
READINESS_GATE_ONLY=true
PHASE_13E_42_OUTPUT_SCHEMA_REQUIRED_FIELDS_CONFIRMED=true
FILM_SCREENPLAY_OUTPUT_SCHEMA_REQUIRED_FIELD_COUNT=20
FILM_SCREENPLAY_OUTPUT_SCHEMA_ENFORCEABLE_FOR_REQUIRED_FIELDS=true
FILM_SCREENPLAY_PACKET_VALIDATOR_SKELETON_ONLY_CONFIRMED=true
FILM_PACKET_FIXTURES_AVAILABLE=true
FILM_PACKET_POSITIVE_BASELINE_AVAILABLE=true
SYNTHETIC_PACKET_TEST_STRATEGY_REQUIRED=true
CONTENT_DRIFT_FAILURE_FIXTURES_AVAILABLE=true
NO_FAKE_FILM_PASS_VALIDATOR_STILL_SKELETON_ONLY=true
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
FINAL_VERDICT=READY_FOR_NARROW_FILM_SCREENPLAY_OUTPUT_PACKET_VALIDATOR_PATCH
```

## 11. Recommended Next Phase

Phase 13E_44: film screenplay output packet validator enforcement patch

Phase 13E_44 should implement only `validators/film/output_packet/validate_film_screenplay_packet.py`, one focused test file, and one patch report. It should not modify selector, active registries, schemas, fixtures, no-fake-PASS validator, runtime harness, or runtime behavior.
