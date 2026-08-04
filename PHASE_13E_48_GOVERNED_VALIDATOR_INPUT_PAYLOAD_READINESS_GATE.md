# Phase 13E_48 Governed Validator Input Payload Readiness Gate

## 1. Objective

Phase 13E_48 defines the exact governed input payload shapes needed for the film validator stack to move from local enforcement to a future governed runtime proof attempt.

This phase is readiness-only. It does not modify validators, schemas, fixtures, tests, selectors, active route manifests, active route slices, runtime contracts, directors, agents, subagents, skills, or subskills. It does not bind validators to runtime, does not execute governed runtime output, does not claim PASS, and does not claim governed runtime proof.

## 2. Current State

```text
phase=13E_48
base_head=09f087661b8b81b455f2c8cc1c721b1fccc49a61
phase_13e_38_route_selection_validator_local_enforcement=true
phase_13e_40_content_packet_separation_validator_local_enforcement=true
phase_13e_44_output_packet_validator_local_enforcement=true
phase_13e_46_no_fake_pass_validator_local_enforcement=true
runtime_harness_status=FILM_RUNTIME_PROOF_BLOCKED_SKELETON_VALIDATORS
runtime_harness_blocker_reclassified=GOVERNED_VALIDATOR_INPUT_PAYLOADS_MISSING
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

The worktree contains broad pre-existing dirty and untracked files. This readiness gate preserves them and stages only this Phase 13E_48 report.

## 3. Evidence Reviewed

| Evidence | Path or command | Finding | Readiness impact |
| --- | --- | --- | --- |
| Phase 13E_47 audit | `PHASE_13E_47_FILM_VALIDATOR_STACK_POST_ENFORCEMENT_COHERENCE_AUDIT.md` | Confirms local validator enforcement exists but governed runtime proof inputs are still missing | Establishes the bridge point for this gate |
| Route-selection validator | `validators/film/route/validate_film_route_selection.py` | Locally enforced for explicit payloads; empty payload remains `SKELETON_ONLY` | Needs governed non-empty payloads |
| Content-separation validator | `validators/film/validation/validate_film_content_packet_separation.py` | Locally enforced for explicit payloads; empty payload remains `SKELETON_ONLY` | Needs governed non-empty payloads |
| Output packet validator | `validators/film/output_packet/validate_film_screenplay_packet.py` | Locally enforced for explicit payloads; empty payload remains `SKELETON_ONLY` | Needs governed non-empty payloads |
| No-fake PASS validator | `validators/film/validation/validate_no_fake_film_pass.py` | Locally enforced for explicit payloads; empty payload remains `SKELETON_ONLY` | Needs governed non-empty payloads |
| Runtime proof harness | `python3 tools/film_runtime/film_route_runtime_proof_harness.py \|\| true` | Still blocks because it sees empty-payload skeleton results | Identifies the exact next readiness gap |

## 4. Governed Input Payload Matrix

The future harness should not call the four validators with empty payloads. It should pass governed, non-empty payloads that are explicit about the intended route and proof boundary.

| Validator | Governed payload kind | Required governing keys | Positive-control shape | Failure-control shape | Expected local status |
| --- | --- | --- | --- | --- | --- |
| `validate_film_route_selection.py` | Route-selection governed fixture payload | `fixture_family`, `input_prompt` or `input_packet_summary`, `expected_route`, `expected_mode`, `should_pass_later`, `should_fail_later` | `fixture_family=route_selection`, `expected_route=FILM_SCREENPLAY_GENERATION`, `expected_mode=film_core`, `should_pass_later=true`, `should_fail_later=false` | Content prompt routed to film core, explicit screenplay prompt routed to content route, or downstream trigger routed to film core | `VALIDATION_PASSED` for the positive control |
| `validate_film_content_packet_separation.py` | Film/content separation governed fixture payload | `fixture_family`, `input_prompt` or `input_packet_summary` or `input_summary`, `expected_route`, `expected_result`, `should_pass_later`, `should_fail_later` | `fixture_family=film_packet_validation`, `expected_route=FILM_SCREENPLAY_GENERATION`, `expected_result=FAIL_LATER`, `should_pass_later=false`, `should_fail_later=true` for collision cases that should fail | Content packet pretending to be film, hook/retention-only packet, or content validator claiming film approval | `VALIDATION_FAILED` for collision cases |
| `validate_film_screenplay_packet.py` | Film screenplay output packet governed payload | All 20 schema required fields plus `route_state_capsule`, `film_intent_lock`, `no_fake_pass_gate` | Complete screenplay packet with the Phase 13E_42 required fields and no content/platform drift markers | Missing `beat_sheet`, missing `dialogue_subtext_pass`, content packet masquerading as film, or hook/retention-only packet | `VALIDATION_PASSED` for the complete packet |
| `validate_no_fake_film_pass.py` | No-fake PASS governed payload | Explicit claims/evidence fields such as `claims_film_schema_valid`, `film_schema_evidence`, `claims_source_backed`, `source_ledger`, `claims_route_lineage_complete`, `route_lineage_ledger`, `claims_filmcraft_scorecard_complete`, `filmcraft_scorecard`, `claims_governed_runtime_proof_from_repo_read`, `runtime_artifact_claims` | Clean positive control with evidence present and all pass/proof claims false | Any fake PASS claim, invented runtime artifact claim, repo-read masquerading as runtime proof, or missing evidence for a claimed property | `VALIDATION_PASSED` for the clean positive control |

## 5. Harness Integration Plan

The runtime harness currently invokes the validators with `{}` and therefore sees `SKELETON_ONLY` by design. The next implementation step should replace those empty calls with governed payload builders that are explicit about:

1. The intended route family.
2. The expected outcome.
3. The evidence keys required to justify the assertion.
4. The difference between local enforcement and governed runtime proof.

The harness should not silently infer proof from repository reads. It should call the locally enforced validators with real payloads only when those payloads are designed to be governed inputs.

## 6. Why the Harness Is Still Blocked

```text
local_validator_enforcement_exists=true
governed_validator_input_payloads_missing=true
runtime_harness_empty_payload_detection_still_blocks=true
runtime_proof_not_claimed=true
```

The current blocker is no longer “the validators do nothing.” The blocker is “the harness still has no governed payloads to exercise the validators as proof-bearing inputs.”

## 7. Boundary Preservation

```text
runtime_behavior_changed=false
route_selector_modified=false
active_route_manifest_modified=false
active_route_slice_modified=false
schemas_modified=false
validators_modified=false
fixtures_modified=false
tests_modified=false
runtime_contracts_modified=false
directors_modified=false
agents_modified=false
subagents_modified=false
skills_modified=false
subskills_modified=false
pass_claimed=false
governed_runtime_proof_claimed=false
```

This gate modified no implementation files.

## 8. Remaining Implementation Gap

| Gap | Current status | Why it matters | Next required action |
| --- | --- | --- | --- |
| Harness still uses empty validator payloads | Blocking | Empty payloads intentionally return `SKELETON_ONLY` | Patch the harness to use governed payload builders |
| No governed input schema for proof-bearing validation | Blocking | Without an explicit input contract, proof attempts remain ambiguous | Define a narrow governed payload contract for the four critical validators |
| Runtime proof still not claimed | Correct | Repo inspection is not runtime proof | Keep proof claims blocked until governed inputs exist |
| Full cinema engine still broader than validator stack | Partial | Directors/agents/skills still need later cohesion work | Continue bounded implementation phases after input payload design |

## 9. Current Gate Verdict

```text
PHASE_13E_48_STATUS=GOVERNED_VALIDATOR_INPUT_PAYLOAD_READINESS_GATE_COMPLETE
READINESS_GATE_ONLY=true
GOVERNED_VALIDATOR_INPUT_PAYLOADS_DEFINED=true
ROUTE_SELECTION_GOVERNED_PAYLOAD_DEFINED=true
CONTENT_SEPARATION_GOVERNED_PAYLOAD_DEFINED=true
OUTPUT_PACKET_GOVERNED_PAYLOAD_DEFINED=true
NO_FAKE_PASS_GOVERNED_PAYLOAD_DEFINED=true
RUNTIME_HARNESS_EMPTY_PAYLOADS_BLOCK_RUNTIME_PROOF=true
LOCAL_VALIDATOR_ENFORCEMENT_EXISTS=true
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
FINAL_VERDICT=READY_FOR_GOVERNED_VALIDATOR_INPUT_PAYLOAD_IMPLEMENTATION
```

## 10. Recommended Next Phase

Phase 13E_49: governed validator input payload implementation patch

Phase 13E_49 should implement only the governed payload builders or harness inputs needed to call the four locally enforced validators with explicit non-empty payloads. It should not modify selector, active registries, schemas, fixtures, output validators, or runtime behavior beyond the narrow harness input path approved by the readiness gate.
