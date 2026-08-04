# Source Breadth and Rule Evidence Contract

This contract hardens wrapper-required content tasks after MAC-06.1M proved that route locks can execute but rule/source evidence can still be too shallow for full production PASS.

## SOURCE_BREADTH_LOCK

For latest, current, this week, new update, or multi-tool watchlist tasks, output must include:

```text
PER_TOOL_SOURCE_MAP
tool_name=
claim=
source_url=
source_type=official_primary/credible_secondary/user_provided/unknown
source_recency=this_week/recent/stable_reference/outdated/unknown
source_checked_before_output=true/false
claim_allowed=true/false
limitation=
```

Rules:

- If the task asks for latest tools, at least 3 non-identical tool ecosystems must be checked unless the user narrows scope.
- If a named tool is mentioned in final output, it must appear in `PER_TOOL_SOURCE_MAP`.
- If source evidence is missing for a tool claim, set `claim_allowed=false` or classify the output `PARTIAL`.
- If all sources come from one vendor for a broad multi-tool watchlist, `source_breadth_status=FAIL`.
- If a current/latest claim is made without a source map, `SOURCE_BREADTH_LOCK=FAIL`.
- Unsupported tool claims must be listed before final proof classification.
- Source labels without `source_url=` fields are not a source map.
- If web search is claimed for a real-person or biographical script, the output
  must include actual URL-bearing `PER_TOOL_SOURCE_MAP` rows or structured
  `SOURCE_LEDGER` rows. Plain labels such as `Wikipedia - Yash` are not enough.

## RULE_CONSUMPTION_EVIDENCE_LOCK

For each selected director, agent, subagent, skill, and subskill, ledger must include:

```text
RULE_CONSUMPTION_EVIDENCE_LEDGER
component_name=
component_type=director/agent/subagent/skill/subskill
source_file=
exact_rule_id_or_text=
source_section_or_line=
read_before_output=true/false
output_decision_changed=
output_line_or_section_affected=
evidence_depth=EXACT_RULE/SECTION_LEVEL/ROLE_SUMMARY/MISSING
status=USED/PARTIAL/NOT_USED
```

Rules:

- Role-level summaries are not enough for full `PASS`.
- If a component is selected but only described by role, set `evidence_depth=ROLE_SUMMARY` and `status=PARTIAL`.
- If exact rule text or section evidence is missing for critical route components, final status cannot exceed `NEEDS_CONFIRMATION`.
- If ledgers are absent, classify `FAIL`.
- If `LINE_BY_LINE_INFLUENCE_MAP` lacks exact repo rule references, classify `PARTIAL`.

## EXACT_RULE_LINEAGE_MAP

Every production proof must include:

```text
EXACT_RULE_LINEAGE_MAP
output_line_or_section=
component_name=
source_file=
exact_rule_id_or_text=
source_section_or_line=
decision_changed=
```

If all locks pass but source or rule depth is weak, classify
`NEEDS_CONFIRMATION`, not full `PASS`.
