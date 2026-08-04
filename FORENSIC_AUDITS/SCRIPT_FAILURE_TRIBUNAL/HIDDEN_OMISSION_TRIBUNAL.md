# Hidden Omission Tribunal

| omission | required surface | proof | impact | severity |
| --- | --- | --- | --- | --- |
| Missing structured source rows | `SOURCE_LEDGER` / `FACT_VS_ANECDOTE_MAP` JSON rows | `source_row_json=`, `fact_map_row_json=` both count `0` in the transcript | Source claims are not machine-checkable | P0 |
| Missing structured rehook rows | `RECURRING_REHOOK_MAP` JSON rows | `rehook_row_json=` count `0` in the transcript | Re-hook proof cannot be validated | P0 |
| Missing influence-map section | `LINE_BY_LINE_INFLUENCE_MAP` | `LINE_BY_LINE_INFLUENCE_MAP` count `0` in the transcript | Line-level proof cannot be traced | P0 |
| Missing scorecard surface | `VALIDATION_SCORECARD` / score fields | `VALIDATION_SCORECARD` count `0` and `script_pass_threshold` count `0` in the transcript | PASS becomes a self-certification claim | P0 |

