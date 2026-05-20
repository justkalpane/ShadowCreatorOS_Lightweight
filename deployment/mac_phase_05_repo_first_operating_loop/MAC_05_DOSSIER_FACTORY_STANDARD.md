# MAC-05 Dossier Factory Standard

## Naming Convention

- Folder pattern:
  - `dossiers/DOSSIER_MAC04_YYYYMMDD_HHMMSS_<TOPIC_SLUG>/` for MAC-04 style proofs
  - For future phases, preserve `DOSSIER_<PHASE>_<TIMESTAMP>_<TOPIC_SLUG>`

## Required File Set

1. `mission.md`
2. `mission_context.json`
3. `selected_directors.json`
4. `selected_agents.json`
5. `selected_subagents.json`
6. `selected_skills.json`
7. `selected_subskills.json`
8. `research_brief.md`
9. `script_v1.md`
10. `debate.md`
11. `critique.md`
12. `final_script.md`
13. `context_engineering_packet.json`
14. `provider_handoff_packet.json`
15. `quality_gate_report.md`
16. `lineage.json`
17. `DOSSIER_README.md`

## JSON Validation Rules

- Validate with `jq` before commit:
  - `mission_context.json`
  - all `selected_*.json`
  - `context_engineering_packet.json`
  - `provider_handoff_packet.json`
  - `lineage.json`
- Any invalid JSON is a hard stop.

## Lineage Required Fields

- `dossier_id`
- `created_at`
- `repo_path`
- `git_baseline_commit`
- `files_created`
- `directors_selected`
- `agents_selected`
- `subagents_selected`
- `skills_selected`
- `subskills_selected`
- `needs_confirmation`
- runtime truth flags (`n8n_used`, `gemini_used`, `providers_used`, `openwebui_used`, `old_windows_runtime_used`)

## Quality Gate Required Fields

- `topic_adherence_pass`
- `generic_output_detected`
- `director_selection_grounded`
- `skill_selection_grounded`
- `final_script_quality_pass`
- `json_packets_valid`
- `lineage_written`
- `overall_quality_gate_pass`

## Provider Handoff Requirements

- Include execution metadata and constraints
- `execution_mode` must be reference-only until explicit execution approval
- `approval_required=true`

## Safety Rules

- No false claim of generated media/audio/video/image artifacts
- No API/provider call claim unless actually executed in an approved phase

