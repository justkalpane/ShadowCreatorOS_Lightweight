# First Mac Repo-First Proof Prompt

Use this prompt in Mac Codex exactly.

`
Working directory: ~/ShadowCreatorOS_Lightweight

Read-first files:
- 00_READ_ME_FIRST_FOR_MAC_MIGRATION.md
- handoff/MAC_MIGRATION_MASTER_INDEX.md
- deployment/mac_phase_04_first_repo_proof/MAC_04_FIRST_REPO_FIRST_DOSSIER_PROOF.md

Mission:
Create exactly one dossier for topic: AI vs Human.

Hard constraints:
- no n8n
- no Gemini
- no provider API
- no OpenWebUI
- no old Windows runtime usage

Role rule:
Use Narada/Chanakya/Valmiki/Krishna only if present in repo.
If any are missing, mark NEEDS_CONFIRMATION and do not invent.

Required dossier outputs:
- final_script.md
- context_engineering_packet.json
- provider_handoff_packet.json
- lineage.json

Quality gate:
- topic must remain AI vs Human throughout
- reject generic script drift
- include explicit comparison, tension, and synthesis

Final report block:
FIRST_MAC_REPO_FIRST_TEST_STATUS=PASS/FAIL/PARTIAL
working_directory=
dossier_path=
files_created=
directors_selected=
agents_selected=
subagents_selected=
skills_selected=
subskills_selected=
needs_confirmation=
quality_gate_passed=true/false
n8n_used=false
provider_used=false
gemini_used=false
openwebui_used=false
old_windows_environment_used=false
generic_output_detected=true/false
final_script_topic_match=true/false
context_packet_valid=true/false
provider_handoff_packet_valid=true/false
lineage_written=true/false
safe_to_continue_mac_build=true/false
`
"@

# 8) Future n8n execution bus design
Write-Doc "C:\ShadowCreatorOS_Lightweight\deployment\mac_phase_05_future_n8n_bus\FUTURE_N8N_EXECUTION_BUS_DESIGN.md" @"
# Future n8n Execution Bus Design

## Contract
- Repo-first stage outputs provider_handoff_packet.json.
- n8n consumes handoff packet only after approval gates.

## Workflow categories
- voice
- image
- thumbnail
- avatar
- video
- publish
- analytics
- callback/polling
- retry/DLQ
- cost gate
- artifact lineage
- imported template reuse lane

## Per-category contract template
- input packet
- output artifact
- provider/tool
- credential rule
- cost gate
- retry rule
- dossier update path
- failure mode

## Source pool
Use C:\ShadowCreatorOS_Lightweight\archive_reference\n8n_full_environment_reference_20260518_v8 (71 workflows) as template reference pool.

## Warning
Imports require manual review first. Old IDs/webhooks are not active truth.
