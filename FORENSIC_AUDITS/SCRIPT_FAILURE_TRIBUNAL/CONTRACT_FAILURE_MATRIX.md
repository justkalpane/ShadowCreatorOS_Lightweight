# Contract Failure Matrix

| issue | repo rule | severity | fix needed | repo-gap or model-error |
| --- | --- | --- | --- | --- |
| Beat blocks exceeded the dynamic timing law | `runtime_contracts/DYNAMIC_TIMED_BEAT_MAP_CONTRACT.md:10-14, 54-56` | P0 | Keep every block between `3-20` seconds and add a duration reason for every block | Model-error |
| Source proof was not serialized in the required rows | `runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md:77-89, 173-181` | P0 | Emit `source_row_json` and `fact_map_row_json` rows before any PASS claim | Model-error |
| Quality pass was claimed without a real scorecard | `runtime_contracts/SCRIPT_QUALITY_ENFORCEMENT_CONTRACT.md:40-53, 154-204` | P0 | Emit actual score fields and a threshold before final proof | Shared failure |
| Canonical route surface under-requires integrity proof | `runtime_contracts/MAC_06_SCRIPT_MEDIA_FACTORY_ACCEPTANCE_TESTS.md:64-85, 146-159` versus `registries/route_slices/script_generation.registry_slice.yaml:63-66` | P1 | Add `VALIDATION_SCORECARD` and `script_integrity_lock` to the canonical script route surface | Repo-gap |

## Contract-layer conclusion

The repo already contains the rules needed to stop the failure. The missing
piece is enforcing them all the way through the route surface and final proof.

