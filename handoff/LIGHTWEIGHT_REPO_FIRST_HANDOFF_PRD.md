# Shadow Creator OS - Lightweight Repo-First Runtime Handoff PRD

## 1. Strategic Decision
The legacy Shadow Empire heavy runtime is quarantined as future enterprise infrastructure. The lightweight path uses the repository as the intelligence constitution and AI coding agents (Codex/Claude/ChatGPT/Kimi) as reasoning/runtime operators.

- n8n is not the intelligence backbone.
- OpenWebUI is optional.
- Gemini is not the default brain.
- Provider APIs are not used unless explicitly requested.

## 2. Old Environment Quarantine Rule
Reference-only paths:
- `C:\ShadowEmpire-Git_Restore_01`
- `C:\ShadowEmpire\n8n_user_restore_01`
- `C:\ShadowEmpire_Quarantine\quarantine_20260515_112944`

Rules:
- Do not modify old source repo.
- Do not use old n8n DB as active runtime.
- Do not use old workflow IDs as active truth.
- Do not use old webhook IDs as active truth.
- Do not continue old Gemini/OpenWebUI/n8n sealing track.

## 3. New Runtime Goal
Build a fast repo-first path where AI agents can:
- read repo contracts and registries
- select directors/agents/subagents/skills/subskills (if present)
- generate research, debate, scripts, critique, final script
- generate context engineering packet and provider handoff packet
- write outputs into dossier files

without n8n for intelligence.

## 4. Architecture Doctrine
- Repo = constitution.
- AI coding agents = intelligence runtime.
- Dossiers = state and truth record.
- Runtime contracts = operating law.
- n8n = future external execution bus only.
- Providers = optional future media/action layer.
- `archive_reference` = historical/reference only.

## 5. Strict Non-Goals
- Do not rebuild old n8n-heavy system.
- Do not use n8n for intelligence.
- Do not make OpenWebUI mandatory.
- Do not use Gemini as default.
- Do not call providers.
- Do not fake media generation.
- Do not claim artifact creation without artifacts.
- Do not invent missing subskills or prompts.
- Do not invent missing registry entries.

## 6. Required Files To Read First
- `C:\ShadowCreatorOS_Lightweight\SHADOW_LIGHTWEIGHT_RUNTIME.md`
- `C:\ShadowCreatorOS_Lightweight\AGENT_OPERATING_GUIDE.md`
- `C:\ShadowCreatorOS_Lightweight\COPY_MANIFEST.md`
- `C:\ShadowCreatorOS_Lightweight\runtime_contracts\MISSION_CONTEXT_CONTRACT.md`
- `C:\ShadowCreatorOS_Lightweight\runtime_contracts\DIRECTOR_SELECTION_CONTRACT.md`
- `C:\ShadowCreatorOS_Lightweight\runtime_contracts\SKILL_SELECTION_CONTRACT.md`
- `C:\ShadowCreatorOS_Lightweight\runtime_contracts\DOSSIER_OUTPUT_CONTRACT.md`
- `C:\ShadowCreatorOS_Lightweight\runtime_contracts\QUALITY_GATE_CONTRACT.md`
- `C:\ShadowCreatorOS_Lightweight\runtime_contracts\PROVIDER_HANDOFF_CONTRACT.md`
- `C:\ShadowCreatorOS_Lightweight\runtime_contracts\LINEAGE_CONTRACT.md`
- `C:\ShadowCreatorOS_Lightweight\registries\*`
- `C:\ShadowCreatorOS_Lightweight\directors\*`
- `C:\ShadowCreatorOS_Lightweight\agents\*`
- `C:\ShadowCreatorOS_Lightweight\subagents\*`
- `C:\ShadowCreatorOS_Lightweight\skills\*`
- `C:\ShadowCreatorOS_Lightweight\schemas\*`
- `C:\ShadowCreatorOS_Lightweight\dossiers\DOSSIER_TEMPLATE\*`

Notes:
- `subskills` may be empty.
- `prompts` may be empty.
- Treat missing items as `NEEDS_CONFIRMATION`.

## 7. Runtime Flow
User mission -> create dossier folder -> preserve original user message -> create `mission_context.json` -> load registries -> select directors -> select agents/subagents -> select skills/subskills (if present) -> research -> script_v1 -> debate -> critique -> final_script -> context_engineering_packet -> provider_handoff_packet -> quality gate -> lineage -> final answer summary.

## 8. Dossier Output Contract
Create one new folder per mission under:
`C:\ShadowCreatorOS_Lightweight\dossiers\`

Naming: `DOSSIER_YYYYMMDD_HHMMSS_<short_slug>`

Required files:
- `mission.md`
- `mission_context.json`
- `selected_directors.json`
- `selected_agents.json`
- `selected_subagents.json`
- `selected_skills.json`
- `selected_subskills.json`
- `research_brief.md`
- `script_v1.md`
- `debate.md`
- `critique.md`
- `final_script.md`
- `context_engineering_packet.json`
- `provider_handoff_packet.json`
- `quality_gate_report.md`
- `lineage.json`

## 9. Quality Gates
Must verify:
- topic preserved
- original user request preserved
- selections justified or `NEEDS_CONFIRMATION`
- no generic output
- critique is real
- final script improves from v1
- packet JSON validity
- no false artifact claims
- no n8n usage
- no provider/API usage

## 10. Provider Handoff Rule
For ElevenLabs/HeyGen/Higgsfield/Sora/Seedance/YouTube/analytics:
- generate structured handoff packets only.
- execute only if user explicitly requests and runtime+credentials exist and artifact can be verified.

## 11. Archive Reference Rule
`archive_reference` is historical only. Do not treat old workflow IDs/webhooks/n8n DB/OpenWebUI routes as active runtime truth.

## 12. First Test Mission
Run only this in the fresh Codex chat:

Create a YouTube script on AI vs Human using:
- Narada for research (if present)
- Chanakya for critique (if present)
- Valmiki for story shaping (if present)
- Krishna for final review (if present)

Constraints:
- No n8n
- No Gemini API
- No OpenWebUI
- No provider execution
- Write full dossier

If requested role is missing, mark `NEEDS_CONFIRMATION` and choose nearest registry-backed substitute only if clearly supported.

## 13. Acceptance Criteria
Pass only if:
- dossier created
- all required files written
- selections are real or `NEEDS_CONFIRMATION`
- topic-specific script
- real critique
- improved final script
- valid context/provider JSON packets
- quality gate report exists
- lineage exists
- no n8n/provider/API usage
- old environment untouched
- no generic script

## 14. Implementation Boundary
Fresh Codex chat must implement only the first test mission initially. Do not build framework expansion, n8n/provider/OpenWebUI integrations, or enterprise runtime.

## 15. Expected Final Output (from fresh Codex chat)
Return exactly:
- `FIRST_TEST_MISSION_STATUS=PASS/FAIL/PARTIAL`
- `dossier_path=`
- `files_created=`
- `directors_selected=`
- `skills_selected=`
- `needs_confirmation=`
- `quality_gate_passed=true/false`
- `n8n_used=false`
- `provider_used=false`
- `old_environment_touched=false`
