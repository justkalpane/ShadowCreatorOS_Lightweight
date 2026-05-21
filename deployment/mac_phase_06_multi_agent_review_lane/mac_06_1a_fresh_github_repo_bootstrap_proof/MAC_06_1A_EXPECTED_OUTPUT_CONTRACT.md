# MAC-06.1A Expected Output Contract

The returned proof output must include these fields.

```text
repo_loaded=true/false
branch_used=main
start_here_read=true/false
agent_read_order_followed=true/false
shadow_mission_packet_created=true/false
repo_context_loader_summary_present=true/false
registry_first_selection_proven=true/false
director_evidence_paths_present=true/false
agent_evidence_paths_present=true/false
subagent_evidence_paths_present=true/false
skill_evidence_paths_present=true/false
subskill_evidence_paths_present=true/false
tools_connectors_plugins_assessed=true/false
research_brief_created=true/false
script_v1_created=true/false
debate_created=true/false
critique_created=true/false
final_script_created=true/false
context_packet_summary_created=true/false
provider_handoff_boundary_present=true/false
quality_gate_present=true/false
lineage_summary_present=true/false
invented_components_detected=true/false
generic_output_detected=true/false
n8n_used=false
providers_called=false
media_artifacts_claimed=false
```

## MAC-06.1B Governance Addendum

For MAC-06.1A chat proof:

- `repo_files_created=false`
- `approval_gate_blocks_present=true/false`
- `user_approval_required_before_file_creation=true`
- `full_dossier_requested_explicitly=true/false`

Future repo-write proofs must default to one consolidated output file unless full dossier mode is explicitly requested.

## MAC-06.1C Source Intelligence Addendum

Required fields:

```text
research_mode=repo_only/repo_plus_static_knowledge/web_assisted/real_time_web/provider_api_assisted
web_access_available=true/false/UNKNOWN
web_access_used=true/false
real_time_sources_used=true/false
source_list_present=true/false
current_fact_confidence=HIGH/MEDIUM/LOW/LIMITED
research_sufficiency_gate_present=true/false
```

## Proof Status Honesty Law

### `PASS` Requires

- Topic matches user request.
- All required sections are present.
- Directors selected with exact evidence.
- Agents selected with exact evidence, or agent layer explicitly declared optional by active contract.
- Subagents selected with exact evidence.
- Skills selected with exact evidence.
- Subskills selected with exact evidence or marked `NEEDS_CONFIRMATION`.
- Tools/connectors/plugins are honestly assessed.
- Chat gate statuses use only allowed values:
  - `PASS`
  - `BLOCKED`
  - `NEEDS_USER_APPROVAL`
  - `NEEDS_CONFIRMATION`
- If final gate awaits decision, `waiting_for_user_approval=true`.
- Research mode is disclosed:
  - `repo_only`
  - `web_assisted`
  - `real_time_web`
- If web sources are used, source list is included.
- If web sources are not used, `real_time_sources_used=false`.
- Research disclosure fields are present.
- Research Sufficiency Gate is present.
- If task requires current web research and `web_access_used=false`, user explicitly approved repo-only continuation.
- If `real_time_sources_used=true`, `source_list_present=true`.
- No false n8n/provider/media claims.

### `PARTIAL` Is Required If

- Any required evidence layer is `NEEDS_CONFIRMATION`.
- `agents_selected_with_evidence=false` and agent layer is mandatory for this proof mode.
- Gate statuses use non-contract values.
- Lineage lacks exact evidence paths.
- Context packet is summary-only when full packet is required in repo-write/full-dossier mode. In chat-only MAC-06.1A proof, summary is valid.
- Task needs current web evidence but web was not used and repo-only approval is missing.
- `agents_selected_with_evidence=false` unless output explicitly cites active contract section declaring agent layer optional.

### `FAIL` Is Required If

- Invented components are detected.
- Execution claims are false.
- Output is generic and not registry-first.
- Required proof sections are missing.
- `real_time_sources_used=true` but source list is missing.
