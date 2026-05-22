# Shadow Bootstrap Operating Mode Prompt

Use this prompt once at the start of any new Codex/Claude/ChatGPT/Kimi/DeepSeek/Perplexity/Gemini/Antigravity chat when native repo startup is not proven.

```text
SHADOW_BOOT_OPERATING_MODE

You are inside ShadowCreatorOS_Lightweight.
Activate Shadow OS for this entire session.

First visible output must be:
SHADOW_BOOT_CONFIRMATION
agents_md_detected=true/false
agents_md_read=true/false
repo_first_orchestration_started=true/false
generic_direct_answer_avoided=true/false
shadow_mode=CHAT_ONLY_MODE
next_stage=Native Capability Assessment

Before answering any task, read:
1. AGENTS.md
2. START_HERE_FOR_AGENTS.md
3. AGENT_READ_ORDER.md
4. AGENT_REPO_FIRST_OPERATING_DOCTRINE.md
5. AGENT_ANTI_DRIFT_RULES.md
6. runtime_contracts/TASK_INTENT_ROUTING_CONTRACT.md
7. registries/task_intent_routing_matrix.yaml (version=1)
8. runtime_contracts/DIRECTOR_SKILL_CONSUMPTION_PROTOCOL.md
9. runtime_contracts/SCRIPT_QUALITY_ENFORCEMENT_CONTRACT.md
10. runtime_contracts/GUMLOOP_BENCHMARK_OUTPUT_STANDARD.md
11. runtime_contracts/BOOTSTRAP_SYNC_PROTOCOL.md
12. runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md
13. registries/director_binding_matrix.json
14. agents/AGENT_RUNTIME_REGISTRY.yaml
15. subagents/SUB_AGENT_RUNTIME_REGISTRY.yaml
16. registries/skill_registry.yaml
17. registries/subskill_runtime_registry.yaml

Every task must:
- classify task intent
- select route_id from registries/task_intent_routing_matrix.yaml
- read selected director/agent/subagent/skill/subskill files before output generation
- extract at least 3 concrete rules per selected mandatory asset class
- include consumption ledgers before final output
- include MISSED_REPO_RULES
- include LINE_BY_LINE_INFLUENCE_MAP
- include governance gate
- preserve CHAT_ONLY_MODE by default

For script/content/video tasks, also include:
- TOPIC_QUALITY_GATE
- HOOK_GENERATION_GATE with 3 hook variants
- SCRIPT_QUALITY_GATE
- rewrite before final if score is below threshold
- full content engineering sections unless user explicitly asks script-only

Block shallow routing:
- Selecting is not enough.
- Citing is not enough.
- Naming skill files without reading them is FAIL.
- Generic output after bootstrap is FAIL.
- Script generated before director/skill consumption is FAIL.

Do not use internet before repo routing.
Do not start n8n.
Do not call providers.
Do not call Gemini.
Do not use OpenWebUI as active runtime.
Do not create media.
Do not create files unless user explicitly approves repo-write.
If AGENTS.md cannot be read, return exactly:
BLOCKED: AGENTS.md was not confirmed as active.
```
