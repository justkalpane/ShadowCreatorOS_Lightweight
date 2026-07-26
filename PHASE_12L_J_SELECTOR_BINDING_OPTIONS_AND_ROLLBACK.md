# Phase 12L-J Selector Binding Options And Rollback

## 1. Objective
Record selector-binding options, constraints, stop conditions, and rollback before any selector edit.

## 2. Binding Risk Ledger

| Risk ID | Risk | Evidence/source | Impact | Mitigation | Stop condition |
|---|---|---|---|---|---|
| R-12LJ-01 | Runtime-affecting selector change | Phase 12L-I readiness review | Selector work can alter live routing behavior | Keep the edit additive and minimal | Stop if the change touches more than selector binding |
| R-12LJ-02 | Accidental removal or weakening of `SCRIPT_GENERATION` | Live selector and content-route law | Existing content scripts may be displaced | Require explicit preservation of `SCRIPT_GENERATION` | Stop if `SCRIPT_GENERATION` is removed or weakened |
| R-12LJ-03 | Selector collision with existing modes | `runtime/state/route_chain_mode_selector.yaml` | Binding could interfere with current mode logic | Add only the film route binding needed | Stop if existing mode semantics change unexpectedly |
| R-12LJ-04 | Film route selected too broadly | Film route readiness docs | Non-film prompts could route incorrectly | Keep trigger logic narrow and reviewable | Stop if routing scope broadens beyond film intent |
| R-12LJ-05 | Missing post-binding validation | Phase 12L-I next phase guidance | Bound selector may not be checked after edit | Require a post-binding validation phase | Stop if validation is not planned |
| R-12LJ-06 | False PASS or governed-proof claim | Prior phase boundaries and checker law | Repo edits could be overstated as runtime completion | Never claim PASS from repo edits alone | Stop if any PASS/proof claim appears |
| R-12LJ-07 | Rollback failure | Selector-binding work | A bad edit could be harder to undo | Write rollback as a separate documented path | Stop if rollback is missing |
| R-12LJ-08 | Dirty worktree staging risk | Current repo state | Unrelated changes could be accidentally staged | Stage only the intended selector-change file(s) | Stop if unrelated files would need staging |

## 3. Non-Negotiable Selector Constraints

```text
selector_binding_must_be_additive=true
SCRIPT_GENERATION_must_remain_available=true
FILM_SCREENPLAY_GENERATION_must_not_replace_SCRIPT_GENERATION=true
selector_change_must_be_minimal=true
post_binding_validation_required=true
runtime_PASS_must_not_be_claimed_from_repo_edit=true
governed_runtime_proof_must_not_be_claimed=true
rollback_plan_required=true
```

## 4. Rollback Plan

Future rollback must:

- revert only the selector-binding change
- leave the active film registry pair intact unless separately approved
- verify `SCRIPT_GENERATION` remains available
- verify `FILM_SCREENPLAY_GENERATION` is no longer selected after rollback
- avoid force push
- avoid runtime PASS or governed proof claims

