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
