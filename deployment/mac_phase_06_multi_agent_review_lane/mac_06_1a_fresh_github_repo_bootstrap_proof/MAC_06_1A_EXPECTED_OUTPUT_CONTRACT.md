# MAC-06.1A Expected Output Contract

The returned proof output must include these fields.

```text
repo_loaded=true/false
shadow_boot_confirmation_present=true/false
first_visible_output_is_boot_confirmation=true/false
agents_md_detected=true/false
agents_md_read=true/false
repo_first_orchestration_started=true/false
layman_task_trigger_contract_read=true/false
generic_direct_answer_avoided=true/false
environment_trigger_compatibility_checked=true/false
platform_current_classification=NATIVE_AUTO_TRIGGER_COMPATIBLE/BOOTSTRAP_REQUIRED_COMPATIBLE/REPO_VISIBLE_BUT_NOT_BEHAVIOR_ACTIVE/NOT_COMPATIBLE/NEEDS_CONFIRMATION
internet_first_behavior_detected=true/false
web_access_used_before_repo_route=true/false
shadow_mode=CHAT_ONLY_MODE
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
content_engineering_contract_read=true/false
content_mission_brief_present=true/false
research_and_source_status_present=true/false
script_structure_present=true/false
timed_beat_map_present=true/false
voice_generation_context_present=true/false
image_generation_context_present=true/false
video_generation_context_present=true/false
music_sfx_context_present=true/false
editing_context_present=true/false
platform_packaging_present=true/false
provider_handoff_boundary_present=true/false
quality_gate_present=true/false
lineage_summary_present=true/false
native_capability_routing_matrix_cited=true/false
agent_runtime_selection_index_cited=true/false
task_to_capability_routing_present=true/false
chat_only_mode_used=true/false
files_created=false
dossier_artifacts_created=false
invented_components_detected=true/false
generic_output_detected=true/false
n8n_used=false
providers_called=false
media_artifacts_claimed=false
native_auto_trigger_test_result=PASS/PARTIAL/FAIL/NOT_RUN
bootstrap_required_test_result=PASS/PARTIAL/FAIL/NOT_RUN
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
web_fetch_available=true/false
web_access_used=true/false
real_time_sources_used=true/false
source_list_present=true/false
current_fact_confidence=HIGH/MEDIUM/LOW/LIMITED
research_sufficiency_gate_present=true/false
```

Required capability/freshness blocks:

```text
freshness_class=EVERGREEN/CURRENT_SENSITIVE/REALTIME_REQUIRED/USER_SOURCE_REQUIRED/HIGH_STAKES_CURRENT
current_data_required=true/false
freshness_reason=
tools_connectors_plugins_assessment_present=true/false
native_agent_capability_assessment_present=true/false
task_to_capability_routing_present=true/false
capability_matrix_cited=true/false
agent_runtime_selection_index_cited=true/false
agent_layer_status=PROVEN_WITH_ACTIVE_INDEX/PARTIAL_NEEDS_INDEX/NEEDS_CONFIRMATION
chat_only_mode_used=true/false
files_created=false
dossier_artifacts_created=false
layman_task_trigger_verified=true/false
generic_direct_answer_detected=true/false
content_engineering_contract_present=true/false
content_engineering_contract_read=true/false
timed_beat_map_present=true/false
voice_generation_context_present=true/false
image_generation_context_present=true/false
video_generation_context_present=true/false
music_sfx_context_present=true/false
editing_context_present=true/false
platform_packaging_present=true/false
script_only_output_detected=true/false
invalid_gate_status_detected=true/false
media_context_engineering_present=true/false
repo_read=true/false
repo_write=true/false
shell_available=true/false
git_available=true/false
github_remote_available=true/false
file_search_available=true/false
code_execution_available=true/false
package_install_available=true/false
browser_available=true/false
provider_credentials_available=true/false
n8n_runtime_available=true/false
capabilities_requiring_approval_present=true/false
limitations_disclosed=true/false
```

## Proof Status Honesty Law

### `PASS` Requires

- `shadow_boot_confirmation_present=true`.
- `first_visible_output_is_boot_confirmation=true`.
- `agents_md_detected=true` and `agents_md_read=true`.
- `repo_first_orchestration_started=true`.
- `layman_task_trigger_contract_read=true`.
- `generic_direct_answer_avoided=true`.
- `native_capability_routing_matrix_cited=true`.
- `agent_runtime_selection_index_cited=true` when agent layer is mandatory.
- `task_to_capability_routing_present=true`.
- For MAC-06.1A, `chat_only_mode_used=true`, `files_created=false`, and `dossier_artifacts_created=false`.
- For content/script/video tasks, `content_engineering_contract_read=true` and all required content engineering sections are present.
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
- Freshness classification is present.
- Research mode decision is present.
- Tools/connectors/plugins assessment is present.
- Native capability assessment is present.
- Task-to-capability routing is present and references capability matrix.
- `capability_matrix_cited=true`.
- `agent_runtime_selection_index_cited=true` when agent layer is mandatory.
- `chat_only_mode_used=true` and `files_created=false` for MAC-06.1A.
- Output does not follow old dossier-first behavior.
- `AGENTS.md` is detected/read.
- Layman task trigger is verified.
- Content tasks include `CONTENT_ENGINEERING_OUTPUT_CONTRACT` sections unless user explicitly asks script-only.
- For video/script tasks, media context engineering handoff is present.
- Timed beat map is present.
- Voice generation context is present.
- Image generation context is present.
- Video generation context is present.
- Music/SFX context is present.
- Editing context is present.
- Platform packaging is present.
- Final proof status matches weakest required evidence layer.
- No false n8n/provider/media claims.
- PASS is impossible if generic direct answer occurs.
- PASS is impossible if old dossier-first behavior is followed.
- PASS is impossible if any final answer/script/summary/outline/advice appears before `SHADOW_BOOT_CONFIRMATION`.
- PASS is impossible if `SHADOW_BOOT_CONFIRMATION` is missing.
- PASS is impossible if first visible output is not `SHADOW_BOOT_CONFIRMATION`.
- PASS is impossible if `AGENTS.md` is not detected/read.
- PASS is impossible if internet-first behavior occurred before repo routing.
- PASS is impossible if `platform_current_classification=REPO_VISIBLE_BUT_NOT_BEHAVIOR_ACTIVE`.
- Native auto-trigger test and bootstrap-required test are separate proof paths.
- If native auto-trigger fails, do not declare native onboarding.
- If bootstrap-required passes after native auto-trigger fails, classify the platform as `BOOTSTRAP_REQUIRED_COMPATIBLE` only.
- If Test A and Test B fail, classify the platform as `REPO_VISIBLE_BUT_NOT_BEHAVIOR_ACTIVE` or `NOT_COMPATIBLE`.
- n8n execution remains disabled.
- Providers remain disabled.
- Media execution remains disabled.

### `PARTIAL` Is Required If

- Any required evidence layer is `NEEDS_CONFIRMATION`.
- `agents_selected_with_evidence=false` and agent layer is mandatory for this proof mode.
- Gate statuses use non-contract values.
- Lineage lacks exact evidence paths.
- Context packet is summary-only when full packet is required in repo-write/full-dossier mode. In chat-only MAC-06.1A proof, summary is valid.
- Task needs current web evidence but web was not used and repo-only approval is missing.
- `agents_selected_with_evidence=false` unless output explicitly cites active contract section declaring agent layer optional.
- Tool capability claimed without evidence/status.
- Native capability assessment block is missing.
- Task-to-capability routing block is missing.
- Capability matrix or runtime index citation is missing for mandatory layers.
- Generic direct answer appears before repo routing.
- Invalid gate statuses appear.
- Script-only output appears for a video/content task when user did not request script-only.
- Any required content engineering section is missing for a content/script/video task.
- `AGENTS.md` is not detected/read.
- Capability matrix or agent runtime selection index is not cited for mandatory layers.
- `files_created=true` or `dossier_artifacts_created=true` in MAC-06.1A chat-only proof.

### `FAIL` Is Required If

- Invented components are detected.
- Execution claims are false.
- Output is generic and not registry-first.
- `SHADOW_BOOT_CONFIRMATION` is missing.
- Any final answer/script/summary/outline/advice appears before `SHADOW_BOOT_CONFIRMATION`.
- Required proof sections are missing.
- `real_time_sources_used=true` but source list is missing.
- Capability claims are fabricated or contradictory to disclosed environment state.
- Internet-first behavior appears before repo routing.
- `web_access_used_before_repo_route=true`.
