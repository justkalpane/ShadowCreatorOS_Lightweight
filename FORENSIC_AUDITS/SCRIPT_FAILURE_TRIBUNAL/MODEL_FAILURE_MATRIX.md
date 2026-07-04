# Model Failure Matrix

| failure mode | exact validator string | expected corrected output block | fix owner |
| --- | --- | --- | --- |
| Beat map blocks are too long | `allowed_block_duration_seconds=3-20` / `beat_duration_dynamic=true` | `DYNAMIC_TIMED_BEAT_MAP` with every block between 3 and 20 seconds and a duration reason for each block | Script generation / Vyasa |
| Source proof is not structured | `source_lock_pass_without_structured_source_ledger_rows` and `source_lock_pass_without_structured_fact_map_rows` | `SOURCE_LEDGER` and `FACT_VS_ANECDOTE_MAP` with one JSON row per claim and one JSON row per source | Research / Valmiki |
| Weak inference is stated like fact | `weak_inference_presented_too_strongly` | `FACT_VS_ANECDOTE_MAP` lines that downgrade unsupported absolutes instead of asserting them | Script writer / Valmiki |
| Required influence map is absent | `line_by_line_influence_map_is_shallow` | `LINE_BY_LINE_INFLUENCE_MAP` with exact repo-rule references and line-level influence rows | Final packager / governance |
| Quality pass is claimed without score fields | `quality_gate_without_threshold` and `script_scores_missing` | `TOPIC_QUALITY_GATE`, `HOOK_GENERATION_GATE`, `SCRIPT_QUALITY_GATE`, and `VALIDATION_SCORECARD` with actual scores | Governance / Krishna |

## Model-level conclusion

The model did not merely produce a shorter draft. It produced a draft that
looked complete while omitting the machine-check proof surfaces the repo
requires.

