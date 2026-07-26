# Phase 12L-M Post Binding Checker Update Plan

## 1. Objective
Plan a checker update for post-promotion and post-selector-binding state without implementing it.

## 2. Problem

```text
existing_checker=pre_promotion_checker
current_result=PROMOTION_GATE_BLOCKED_ACTIVE_FILE_ALREADY_EXISTS
post_binding_state_requires_new_validation_model=true
phase_12L_L_classification=POST_SELECTOR_BINDING_VALIDATION_NEEDS_CHECKER_UPDATE
```

## 3. Required checker split

| Checker | Purpose | Valid before promotion? | Valid after promotion? | Valid after selector binding? |
|---|---|---|---|---|
| Pre-promotion checker | Confirms the route is still unbound and not yet active | Yes | No | No |
| Post-promotion registry checker | Confirms the active manifest/slice pair exists and is parseable | No | Yes | No |
| Post-selector-binding checker | Confirms the selector now points at the active film route | No | No | Yes |
| Runtime-proof checker | Confirms governed runtime evidence, if and only if runtime proof is explicitly requested and available | No | No | Only after runtime proof workflow exists |

## 4. Update recommendation
Create a new checker rather than weakening the existing pre-promotion checker.

Recommended future checker:

```text
validators/film/validate_film_route_post_binding_state.py
```

Do not create it in this phase.
