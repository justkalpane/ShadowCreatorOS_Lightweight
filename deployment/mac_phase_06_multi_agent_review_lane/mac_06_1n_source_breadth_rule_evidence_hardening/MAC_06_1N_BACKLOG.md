# MAC-06.1N Source Breadth + Exact Rule Consumption Evidence Hardening Backlog

MAC_06_1N_BACKLOG_STATUS=OPEN

## Purpose

MAC-06.1M proved that Codex Cloud wrapper-required mode can enforce the route-lock structure for chat-only content tasks. The next hardening layer is source breadth and exact rule-consumption evidence depth.

## Required Future Hardening

1. For latest/current research tasks, require per-tool source mapping:
   - `tool_name=`
   - `claim=`
   - `source_url=`
   - `source_type=official/credible_secondary`
   - `recency_class=this_week/recent/stable_reference`
   - `claim_allowed=true/false`

2. For director, agent, skill, and subskill ledgers, require:
   - `exact_rule_id_or_text=`
   - `source_file=`
   - `line_or_section=`
   - `output_decision_changed=`
   - `output_line_or_section_affected=`

3. If rule evidence is only role-level summary, classify `PARTIAL`, not full `PASS`.

4. If source breadth is too narrow for a multi-tool watchlist, classify `PARTIAL`.

5. If all locks pass but source/rule depth is weak, classify `PASS_WITH_NOTICE`.

## Safety Boundary

n8n_started=false
providers_called=false
media_artifacts_created=false
dossier_4_started=false

safe_to_declare_lightweight_os_onboarded=false
safe_to_start_n8n_execution_bus=false
