# Router Failure Matrix

| issue | repo rule | severity | fix needed | repo-gap or model-error |
| --- | --- | --- | --- | --- |
| Canonical route proof surface does not include `VALIDATION_SCORECARD` | `runtime_contracts/MAC_06_SCRIPT_MEDIA_FACTORY_ACCEPTANCE_TESTS.md:64-85` requires `VALIDATION_SCORECARD` | P1 | Add the integrity scorecard to the canonical script route outputs | Repo-gap |
| Canonical route proof surface does not include `script_integrity_lock` | `runtime_contracts/MAC_06_SCRIPT_MEDIA_FACTORY_ACCEPTANCE_TESTS.md:146-159` requires `script_integrity_lock=PASS` for a deeper draft surface | P1 | Elevate integrity proof into the route manifest / slice where production acceptance expects it | Repo-gap |
| `LINE_BY_LINE_INFLUENCE_MAP` is required by acceptance tests but the canonical route surface prefers `EXACT_RULE_LINEAGE_MAP` | `runtime_contracts/MAC_06_SCRIPT_MEDIA_FACTORY_ACCEPTANCE_TESTS.md:64-85` and `registries/task_intent_routing_matrix.yaml:292-307` | P1 | Add the missing influence-map surface to the canonical script route | Repo-gap |
| Route lock was claimed as complete while required proof sections were absent | `TASK_EXECUTION_STATE_MACHINE_CONTRACT.md:8-19, 30-70, 151-198` | P0 | Stop claiming route completion until the required proof blocks are actually emitted | Model-error |

## Router-layer conclusion

The router layer is not the primary failure, but it is under-specified for the
proof depth that acceptance requires.

