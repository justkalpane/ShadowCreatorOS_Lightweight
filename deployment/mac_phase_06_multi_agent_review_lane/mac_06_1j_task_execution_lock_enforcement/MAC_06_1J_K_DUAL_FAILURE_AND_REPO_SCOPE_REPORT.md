# MAC-06.1J/K Dual Failure and Repo Scope Report

TEST_1_BOOTSTRAP_BUT_GENERIC_OUTPUT=FAIL

- bootstrap_confirmed=true
- task_intent_classified=false
- route_id_missing=true
- route_selected_before_script=false
- routing_matrix_read_before_output=false
- director_ledger_missing=true
- agent_ledger_missing=true
- subagent_ledger_missing=true
- skill_files_not_read=true
- subskill_ledger_missing=true
- source_gate_missing=true
- script_generated_before_consumption_complete=true
- final_verdict=GENERIC_OUTPUT_AFTER_BOOTSTRAP

TEST_2_MANUAL_RERUN_STRUCTURED_BUT_PARTIAL=PARTIAL

- mission_packet_present=true
- research_status_present=true
- sources_present=true
- content_engineering_sections_present=true
- provider_boundary_present=true
- route_id_missing=true
- task_route_lock_missing=true
- route_dependency_expansion_lock_missing=true
- consumption_lock_missing=true
- director_ledger_missing=true
- subskill_ledger_missing=true
- quality_scorecard_missing=true
- governance_approval_missing=true
- line_by_line_repo_rule_influence_missing=true

ROOT_CAUSE:
Bootstrap activation is not enough.
Manual "read/apply repo" instruction is not enough.
The repo must enforce route dependency expansion and complete required repo consumption per task.

## Boundary

No Test A or Test B rerun was performed.
No n8n, provider, Gemini, OpenWebUI, media, or Dossier #4 action was performed.
