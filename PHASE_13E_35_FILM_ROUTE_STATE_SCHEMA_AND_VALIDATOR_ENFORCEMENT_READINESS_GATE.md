# Phase 13E_35 Film Route State Schema and Validator Enforcement Readiness Gate

## 1. Objective

Phase 13E_35 decides the smallest safe path to unblock the Phase 13E_34 read-only film route proof harness.

This phase is a readiness gate only. It does not modify `runtime/state/route_state.schema.json`, does not modify film schemas, does not modify validators, does not bind validators to runtime, does not execute governed runtime proof, does not generate film output, does not modify selector or registries, and does not claim PASS or governed runtime proof.

## 2. Current State

```text
phase=13E_35
base_head=cc6076c9da409edc16d91c947d4ead3e9db5b608
phase_13e_34_completed=true
harness_implemented=true
harness_read_only=true
harness_status=FILM_RUNTIME_PROOF_BLOCKED_ROUTE_STATE_SCHEMA_GAP
runtime_execution_performed=false
film_output_generated=false
runtime_behavior_changed=false
selector_modified=false
active_route_manifest_modified=false
active_route_slice_modified=false
schemas_modified=false
validators_modified=false
tests_modified=false
pass_claimed=false
governed_runtime_proof_claimed=false
worktree_dirty=true
```

The worktree contains broad pre-existing dirty and untracked files. This gate preserves them and stages only this Phase 13E_35 report.

## 3. Evidence Reviewed

| Evidence | Path or command | Finding | Readiness impact |
| --- | --- | --- | --- |
| Phase 13E_34 report | `PHASE_13E_34_GOVERNED_FILM_ROUTE_RUNTIME_PROOF_HARNESS_IMPLEMENTATION_REPORT.md` | Harness implemented; status is `FILM_RUNTIME_PROOF_BLOCKED_ROUTE_STATE_SCHEMA_GAP` | Confirms the first blocker |
| Harness CLI | `python3 tools/film_runtime/film_route_runtime_proof_harness.py || true` | Reports blocked proof, no output, no PASS, no governed proof | Harness is honest and non-writing |
| Harness test | `python3 tests/test_phase_13e34_film_route_runtime_proof_harness.py` | `phase_13e34_film_route_runtime_proof_harness_ok` | Test expects the blocked status |
| Runtime route state schema | `runtime/state/route_state.schema.json` | `task_mode` enum lacks `film_screenplay_generation` | First blocker must be repaired before capsule schema compatibility |
| Film route state schema | `schemas/film/route/film_route_state_capsule.schema.json` | Skeleton-only, no required fields, not bound | Cannot replace runtime route state schema yet |
| Film screenplay output schema | `schemas/film/output_packet/film_screenplay_output_packet.schema.json` | Skeleton-only, no required fields, not bound | Cannot prove output quality yet |
| Phase 12B schema manifest | `schemas/film/phase_12b_schema_manifest.json` | 39 film schemas, all skeleton-only and unbound | Schema enforcement remains future work |
| Phase 12C validator manifest | `validators/film/phase_12c_validator_manifest.json` | 36 film validators, all skeleton-only and unbound | Validator enforcement remains future work |
| Phase 12A fixture manifest | `tests/fixtures/phase_12a_fixture_manifest.json` | 40 fixture examples across route selection, packet validation, content preservation, downstream handoff, and no-fake-PASS | Fixtures exist as test targets for future validator enforcement |
| Post-binding checker | `python3 validators/film/validate_film_route_post_binding_state.py` | `POST_BINDING_FILM_ROUTE_STATE_READY` | Static selector/route metadata remains coherent |

## 4. Blocker Stack

| Blocker ID | Blocker | Responsible path | Current evidence | Must be resolved before |
| --- | --- | --- | --- | --- |
| B-001 | Runtime route state schema does not accept `film_screenplay_generation` task mode | `runtime/state/route_state.schema.json` | Harness reports `route_state_schema_compatible=false` | Any schema-compatible film route state capsule |
| B-002 | Film route state capsule schema is skeleton-only | `schemas/film/route/film_route_state_capsule.schema.json` | No required fields; `x_schema_enforcement_bound=false` | Strong film-specific capsule validation |
| B-003 | Film screenplay output packet schema is skeleton-only | `schemas/film/output_packet/film_screenplay_output_packet.schema.json` | No required fields; `x_schema_enforcement_bound=false` | Film output schema validation |
| B-004 | Critical film validators are skeleton-only | `validators/film/output_packet/validate_film_screenplay_packet.py`, `validators/film/validation/validate_no_fake_film_pass.py`, `validators/film/validation/validate_film_content_packet_separation.py`, `validators/film/route/validate_film_route_selection.py` | Each returns `SKELETON_ONLY`, `passed=false`, `enforced=false` | Any proof claim |
| B-005 | Full 36-validator film set remains unbound | `validators/film/phase_12c_validator_manifest.json` | `validators_bound=false` | Full cinema validation closure |
| B-006 | Runtime proof invocation remains undefined | No governed film runtime command exists yet | Phase 13E_32/13E_33 recorded `governed_runtime_invocation_identified=false` | Runtime proof execution |

## 5. Readiness Decision

The next implementation must be split. A single broad patch that changes schemas, validators, runtime proof behavior, and route execution together would be too risky.

Recommended order:

1. Add route-state schema support for `film_screenplay_generation` only.
2. Re-run the Phase 13E_34 harness and confirm the first blocker advances from `FILM_RUNTIME_PROOF_BLOCKED_ROUTE_STATE_SCHEMA_GAP` to the validator/schema enforcement blocker.
3. Convert only the critical validator subset into enforceable validators in a later bounded patch.
4. Strengthen the film output packet schema only after the critical validator contract is clear.
5. Only after enforceable validators and schema requirements exist, design a governed runtime invocation.
6. Only after that, attempt runtime proof with explicit owner approval.

## 6. Proposed Phase 13E_36 Scope

Phase 13E_36 should be a narrow route-state schema compatibility patch.

Allowed files:

```text
runtime/state/route_state.schema.json
tests/test_phase_13e36_film_route_state_schema_support.py
PHASE_13E_36_FILM_ROUTE_STATE_SCHEMA_SUPPORT_PATCH_REPORT.md
```

Allowed behavior:

- Add `film_screenplay_generation` to the `task_mode` enum.
- Add a focused test proving a minimal Phase 13E_34 route-state capsule template is schema-compatible.
- Re-run the Phase 13E_34 harness and confirm it no longer stops at `FILM_RUNTIME_PROOF_BLOCKED_ROUTE_STATE_SCHEMA_GAP`.
- Preserve `script_only` and all existing task modes.
- Preserve selector and active registry files.
- Preserve no PASS and no governed runtime proof.

Prohibited behavior:

- Do not modify validators in Phase 13E_36.
- Do not modify film output schemas in Phase 13E_36.
- Do not execute runtime proof.
- Do not generate film output.
- Do not bind validators to runtime.
- Do not modify selector or active route registry files.

Expected post-13E_36 harness status:

```text
FILM_RUNTIME_PROOF_BLOCKED_SKELETON_VALIDATORS
```

or, if validator order reveals the output schema first:

```text
FILM_RUNTIME_PROOF_BLOCKED_OUTPUT_SCHEMA_SKELETON
```

Either result is acceptable if `FILM_RUNTIME_PROOF_BLOCKED_ROUTE_STATE_SCHEMA_GAP` is resolved and no runtime proof is claimed.

## 7. Future Validator Enforcement Scope

After route-state schema support, a later phase should make only the critical subset enforceable first:

| Validator | Minimum enforceable responsibility | Fixture support |
| --- | --- | --- |
| `validators/film/route/validate_film_route_selection.py` | Enforce film-vs-content route selection expectations | `tests/fixtures/film_route_selection/*.json` |
| `validators/film/output_packet/validate_film_screenplay_packet.py` | Require core film packet fields and reject content-only packets | `tests/fixtures/film_packet_validation/*.json` |
| `validators/film/validation/validate_no_fake_film_pass.py` | Reject proof/PASS claims without schema, lineage, scorecard, source, and runtime evidence | `tests/fixtures/no_fake_pass/*.json` |
| `validators/film/validation/validate_film_content_packet_separation.py` | Reject content packets pretending to be film packets and content validators passing film output | `tests/fixtures/content_preservation/*.json`, `tests/fixtures/no_fake_pass/*.json` |

This should be its own patch after Phase 13E_36. It should not be merged into the route-state schema enum patch.

## 8. Acceptance Matrix For Phase 13E_36

| Gate | Required evidence | Must pass? |
| --- | --- | --- |
| Schema parses | `python3 -m json.tool runtime/state/route_state.schema.json` | yes |
| Existing task modes preserved | Test verifies all previous enum values remain | yes |
| Film task mode added | Test verifies `film_screenplay_generation` is accepted | yes |
| Harness rerun | `python3 tools/film_runtime/film_route_runtime_proof_harness.py || true` | yes |
| Harness blocker advances | Status is no longer `FILM_RUNTIME_PROOF_BLOCKED_ROUTE_STATE_SCHEMA_GAP` | yes |
| No runtime proof | Harness still reports `runtime_execution_performed=false`, `film_output_generated=false`, `pass_claimed=false`, `governed_runtime_proof_claimed=false` | yes |
| Static route checker preserved | `python3 validators/film/validate_film_route_post_binding_state.py` | yes |
| Phase 13E_34 harness tests | `python3 tests/test_phase_13e34_film_route_runtime_proof_harness.py` updated only if expected status changes | yes |
| Script/default mode preserved | Selector remains `default_mode=script_only` | yes |
| Dirty worktree protected | Stage only Phase 13E_36 files | yes |

## 9. Current Gate Verdict

```text
PHASE_13E_35_STATUS=FILM_ROUTE_STATE_SCHEMA_AND_VALIDATOR_ENFORCEMENT_READINESS_GATE_COMPLETE
READINESS_GATE_ONLY=true
ROUTE_STATE_SCHEMA_GAP_CONFIRMED=true
CRITICAL_FILM_VALIDATORS_SKELETON_ONLY_CONFIRMED=true
FILM_OUTPUT_SCHEMA_SKELETON_ONLY_CONFIRMED=true
PHASE_12A_FIXTURES_AVAILABLE=true
PHASE_12B_SCHEMAS_AVAILABLE_BUT_UNBOUND=true
PHASE_12C_VALIDATORS_AVAILABLE_BUT_UNBOUND=true
POST_BINDING_CHECKER_READY_STATUS_CONFIRMED=true
HARNESS_IMPLEMENTED=true
HARNESS_RUNTIME_PROOF_BLOCKED=true
RUNTIME_EXECUTION_PERFORMED=false
FILM_OUTPUT_GENERATED=false
RUNTIME_BEHAVIOR_CHANGED=false
SELECTOR_MODIFIED=false
ACTIVE_ROUTE_MANIFESTS_MODIFIED=false
ACTIVE_ROUTE_SLICES_MODIFIED=false
SCHEMAS_MODIFIED=false
VALIDATORS_MODIFIED=false
TESTS_MODIFIED=false
PASS_CLAIMED=false
RUNTIME_PROOF_CLAIMED=false
GOVERNED_RUNTIME_PROOF_CLAIMED=false
FINAL_VERDICT=READY_FOR_NARROW_ROUTE_STATE_SCHEMA_SUPPORT_PATCH
```

## 10. Recommended Next Phase

Phase 13E_36: film route state schema support patch

Phase 13E_36 should add only `film_screenplay_generation` route-state schema support and the focused regression test/report needed to prove the Phase 13E_34 harness advances to the next blocker without claiming runtime proof.
