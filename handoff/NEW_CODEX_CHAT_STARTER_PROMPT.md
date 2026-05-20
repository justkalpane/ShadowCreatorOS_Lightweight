# New Codex Chat Starter Prompt

You are working only inside:
`C:\ShadowCreatorOS_Lightweight`

Read first:
- `C:\ShadowCreatorOS_Lightweight\handoff\LIGHTWEIGHT_REPO_FIRST_HANDOFF_PRD.md`
- `C:\ShadowCreatorOS_Lightweight\SHADOW_LIGHTWEIGHT_RUNTIME.md`
- `C:\ShadowCreatorOS_Lightweight\AGENT_OPERATING_GUIDE.md`
- `C:\ShadowCreatorOS_Lightweight\runtime_contracts\*`
- `C:\ShadowCreatorOS_Lightweight\COPY_MANIFEST.md`

Do not touch:
- `C:\ShadowEmpire-Git_Restore_01`
- `C:\ShadowEmpire\n8n_user_restore_01`
- n8n
- SQLite
- OpenWebUI
- Operator API runtime
- Gemini
- providers

Mission:
Implement only the first test mission:
Create a YouTube script on AI vs Human using repo-first Shadow OS logic.

Constraints:
- No n8n
- No provider/API
- No OpenWebUI
- Create a full dossier
- Stop after report

## Explicit Non-Execution Rules (Audit Patch)
- No Gemini.
- Do not call Gemini API.
- Do not use Gemini as fallback.
- No provider/API usage.
- No n8n.
- No OpenWebUI.

## Quality Gate (Required Before Final Report)
Quality gate must verify:
- topic preserved
- original request preserved
- selected directors are real or flagged NEEDS_CONFIRMATION
- selected skills are real or flagged NEEDS_CONFIRMATION
- final script is topic-specific
- critique is real
- final script improves from script_v1
- no generic output
- context packet exists and is valid JSON
- provider handoff packet exists and is valid JSON
- no false media generation claim

## Exact Final Report Block
FIRST_TEST_MISSION_STATUS=PASS/FAIL/PARTIAL
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
old_environment_touched=false
generic_output_detected=true/false
final_script_topic_match=true/false
context_packet_valid=true/false
provider_handoff_packet_valid=true/false
