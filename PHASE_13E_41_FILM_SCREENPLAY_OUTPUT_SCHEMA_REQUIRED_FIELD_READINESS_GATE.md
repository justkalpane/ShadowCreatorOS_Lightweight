# Phase 13E_41 Film Screenplay Output Schema Required-Field Readiness Gate

## 1. Objective

Phase 13E_41 defines the smallest safe schema support patch needed before `validators/film/output_packet/validate_film_screenplay_packet.py` can become locally enforceable.

This phase is a readiness gate only. It does not modify schemas, validators, fixtures, selectors, active route manifests, active route slices, runtime behavior, directors, agents, subagents, skills, or subskills. It does not bind schemas or validators to runtime, does not generate film output, and does not claim PASS or governed runtime proof.

## 2. Current State

```text
phase=13E_41
base_head=15ecffd46d49d31f66f08ad89cc9fe240e52803a
phase_13e_40_completed=true
route_selection_validator_local_enforcement=true
content_packet_separation_validator_local_enforcement=true
film_screenplay_output_schema_path=schemas/film/output_packet/film_screenplay_output_packet.schema.json
film_screenplay_output_schema_status=SKELETON_ONLY
film_screenplay_output_schema_property_count=28
film_screenplay_output_schema_required_field_count=0
film_screenplay_packet_validator_status=SKELETON_ONLY
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

The worktree contains broad pre-existing dirty and untracked files. This readiness gate preserves them and stages only this Phase 13E_41 report.

## 3. Evidence Reviewed

| Evidence | Path or command | Finding | Readiness impact |
| --- | --- | --- | --- |
| Phase 13E_40 patch report | `PHASE_13E_40_FILM_CONTENT_PACKET_SEPARATION_VALIDATOR_PATCH_REPORT.md` | Content-vs-film packet separation is locally enforceable; runtime proof still blocked | Confirms the next blocker is output schema/packet validation |
| Output schema | `schemas/film/output_packet/film_screenplay_output_packet.schema.json` | 28 properties, zero required fields | Cannot enforce screenplay packet quality until required fields are declared |
| Output validator | `validators/film/output_packet/validate_film_screenplay_packet.py` | Phase 12C skeleton, `passed=false`, `enforced=false` | Must remain blocked until schema support exists |
| Film packet fixtures | `tests/fixtures/film_packet_validation/*.json` | One positive baseline and nine future failure fixtures | Defines required-field support target |
| Runtime proof harness | `python3 tools/film_runtime/film_route_runtime_proof_harness.py || true` | `FILM_RUNTIME_PROOF_BLOCKED_SKELETON_VALIDATORS`; `film_output_schema_required_field_count=0` | Confirms no runtime proof or output schema enforceability |
| Phase 13E_40 test | `python3 tests/test_phase_13e40_film_content_packet_separation_validator.py` | `phase_13e40_film_content_packet_separation_validator_ok` | Regression support for content/film separation |
| Phase 13E_38 test | `python3 tests/test_phase_13e38_film_route_selection_validator.py` | `phase_13e38_film_route_selection_validator_ok` | Regression support for route boundary |
| JSON parse check | `python3 -m json.tool ...` | `phase_13e41_json_inputs_parse_ok` | Current schema and manifests parse |

## 4. Current Schema Inventory

```text
schema_property_count=28
schema_required_count=0
schema_properties=route_state_capsule,film_intent_lock,source_research_status,source_ledger,fact_vs_anecdote_map,logline,theme,premise,genre,tone,cinematic_world,protagonist_want,protagonist_need,protagonist_flaw,protagonist_arc,opposing_force,character_web,beat_sheet,three_act_map,eight_sequence_map,scene_dramaturgy_map,dialogue_subtext_pass,visual_motif_system,style_bible,screenplay_body,film_validation_scorecard,no_fake_pass_gate,downstream_handoff_recommendations
```

The schema already has a useful property surface, but it remains a skeleton because no property is required and `x_schema_enforcement_bound=false`.

## 5. Film Packet Fixture Coverage

| Fixture family | Count | Should pass later | Should fail later | Schema readiness use |
| --- | ---: | ---: | ---: | --- |
| `film_packet_validation` | 10 | 1 | 9 | Defines minimum required-field coverage for film packet schema support |

Missing-required-field evidence from fixtures:

```text
film_packet_shape=1
beat_sheet=2
character_arc=2
scene_dramaturgy=1
dialogue_subtext=2
camera_language=1
composition_notes=1
scene_objective=1
scene_conflict=1
scene_turn=1
validation_scorecard=1
visual_motif_system=1
```

Positive baseline fixture:

```text
tests/fixtures/film_packet_validation/valid_minimal_film_packet.json
```

## 6. Fixture-To-Schema Field Translation

Some fixture terms intentionally describe cinema craft responsibility while the schema uses more formal packet property names. Phase 13E_42 should document this translation in its patch report and tests.

| Fixture field or concept | Existing schema property | Readiness status |
| --- | --- | --- |
| `film_packet_shape` | Multiple core packet fields: `film_intent_lock`, `logline`, `premise`, `screenplay_body` | Needs explicit required-field group |
| `beat_sheet` | `beat_sheet` | Direct match |
| `character_arc` | `protagonist_arc` plus `protagonist_want`, `protagonist_need`, `protagonist_flaw` | Needs translation |
| `scene_dramaturgy` | `scene_dramaturgy_map` | Direct semantic match |
| `scene_objective`, `scene_conflict`, `scene_turn` | `scene_dramaturgy_map` | Needs nested or semantic validator later |
| `dialogue_subtext` | `dialogue_subtext_pass` | Direct semantic match |
| `visual_motif_system` | `visual_motif_system` | Direct match |
| `camera_language`, `composition_notes` | No exact current required property; nearest existing support is `style_bible` plus downstream craft validators | Needs conservative handling |
| `validation_scorecard` | `film_validation_scorecard` | Direct semantic match |

## 7. Proposed Phase 13E_42 Scope

Phase 13E_42 should implement only a schema required-field support patch.

Allowed files:

```text
schemas/film/output_packet/film_screenplay_output_packet.schema.json
tests/test_phase_13e42_film_screenplay_output_schema_required_fields.py
PHASE_13E_42_FILM_SCREENPLAY_OUTPUT_SCHEMA_REQUIRED_FIELD_PATCH_REPORT.md
```

Allowed behavior:

- Add a conservative `required` list to `film_screenplay_output_packet.schema.json`.
- Preserve existing schema metadata boundaries:
  - `x_runtime_behavior_changed=false`
  - `x_route_selector_modified=false`
  - `x_validator_bound=false`
  - `x_governed_runtime_proof_claimed=false`
- Preserve all existing property names unless a direct typo or JSON validity issue is found.
- Add no runtime binding.
- Add no route selector or active registry changes.
- Add a focused test that proves required fields are present and fixture-derived core fields are represented.
- Keep the output packet validator skeleton-only until a later validator enforcement phase.

Recommended conservative required fields for Phase 13E_42:

```text
route_state_capsule
film_intent_lock
logline
theme
premise
genre
tone
protagonist_want
protagonist_need
protagonist_flaw
protagonist_arc
opposing_force
beat_sheet
scene_dramaturgy_map
dialogue_subtext_pass
visual_motif_system
style_bible
screenplay_body
film_validation_scorecard
no_fake_pass_gate
```

This list is intentionally narrower than the full 28-property schema surface. It covers the Phase 12A positive film packet baseline and the current missing-field fixture families while avoiding premature source/docudrama/downstream requirements that should be enforced by later specialized validators.

## 8. Prohibited Phase 13E_42 Behavior

- Do not modify `validators/film/output_packet/validate_film_screenplay_packet.py`.
- Do not modify `validators/film/validation/validate_no_fake_film_pass.py`.
- Do not modify `validators/film/validation/validate_film_content_packet_separation.py`.
- Do not modify route selector, active route manifests, or active route slices.
- Do not modify fixtures.
- Do not bind schema enforcement to runtime.
- Do not claim film packet validator PASS.
- Do not claim governed runtime proof.
- Do not generate film output.

## 9. Acceptance Matrix For Phase 13E_42

| Gate | Required evidence | Must pass? |
| --- | --- | --- |
| Schema remains valid JSON | `python3 -m json.tool schemas/film/output_packet/film_screenplay_output_packet.schema.json` | yes |
| Required list becomes non-empty | `len(required) > 0` | yes |
| Required fields exist in properties | Every required field is a key in `properties` | yes |
| Fixture-derived craft fields represented | Beat sheet, character arc, scene dramaturgy, dialogue subtext, visual motif, screenplay body, validation scorecard represented | yes |
| Schema metadata boundaries preserved | Runtime, selector, validator binding, proof flags remain false | yes |
| Validators unchanged | No validator files modified | yes |
| Selector/registries unchanged | No route selector or active registry files modified | yes |
| Runtime proof unclaimed | Harness still blocks until validators are enforceable | yes |
| Dirty worktree protected | Stage only Phase 13E_42 scoped files | yes |

## 10. Current Gate Verdict

```text
PHASE_13E_41_STATUS=FILM_SCREENPLAY_OUTPUT_SCHEMA_REQUIRED_FIELD_READINESS_GATE_COMPLETE
READINESS_GATE_ONLY=true
PHASE_13E_40_CONTENT_PACKET_SEPARATION_CONFIRMED=true
FILM_SCREENPLAY_OUTPUT_SCHEMA_EXISTS=true
FILM_SCREENPLAY_OUTPUT_SCHEMA_PROPERTY_COUNT=28
FILM_SCREENPLAY_OUTPUT_SCHEMA_REQUIRED_FIELD_COUNT=0
FILM_SCREENPLAY_OUTPUT_SCHEMA_REQUIRED_FIELD_GAP_CONFIRMED=true
FILM_PACKET_FIXTURES_AVAILABLE=true
FILM_PACKET_POSITIVE_BASELINE_AVAILABLE=true
FIXTURE_TO_SCHEMA_TRANSLATION_REQUIRED=true
OUTPUT_PACKET_VALIDATOR_STILL_SKELETON_ONLY=true
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
FINAL_VERDICT=READY_FOR_NARROW_FILM_SCREENPLAY_OUTPUT_SCHEMA_REQUIRED_FIELD_PATCH
```

## 11. Recommended Next Phase

Phase 13E_42: film screenplay output schema required-field support patch

Phase 13E_42 should modify only `schemas/film/output_packet/film_screenplay_output_packet.schema.json`, one focused schema test, and one patch report. It should not modify validators, selector, active registries, fixtures, runtime harness, or runtime behavior.
