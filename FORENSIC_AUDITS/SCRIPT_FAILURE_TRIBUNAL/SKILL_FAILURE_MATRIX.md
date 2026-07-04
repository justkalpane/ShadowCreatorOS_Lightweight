# Skill Failure Matrix

| failure mode | exact validator string | expected corrected output block | fix owner |
| --- | --- | --- | --- |
| Default re-hook fallback can emit placeholder hooks | `recurring_rehook_map_has_no_structured_rows` or `structured_rehook_rows_below_duration_minimum` | Strict packet mode should force real `rehook_row_json` rows, not placeholder hooks | `S-202-first-draft-generation` / M-039 |
| Final packaging must preserve the re-hook map and line influence map | `line_by_line_influence_map_is_shallow` | `RECURRING_REHOOK_MAP`, `DYNAMIC_TIMED_BEAT_MAP`, `EDITING_CONTEXT`, and `LINE_BY_LINE_INFLUENCE_MAP` must survive to final output | `S-210-final-script-packager` |
| Re-hook density law must stay topic-relevant and dynamic | `max_gap_without_rehook_exceeds_90_without_justification` | A dynamic 70-90 second re-hook plan with a 5-minute minimum of three internal re-hooks plus CTA | `S-203-retention-engineer` / M-039 |

## Skill-layer conclusion

The skill stack is present, but one of its modes can drift into placeholder
output if the stricter packet path is not enforced all the way to the final pack.

