# Agent App Compatibility Model

| Agent/App | can_attach_github_repo | can_read_repo_docs | can_write_files | can_output_chat_only | can_execute_terminal | can_perform_web_research | best_operating_mode | proof_required | current_status |
|---|---|---|---|---|---|---|---|---|---|
| Codex | PROVEN | PROVEN | PROVEN | PROVEN | PROVEN | READY_TO_TEST | repo-write dossier operation | representative repo-aware single-agent proof | PROVEN |
| Claude Code | READY_TO_TEST | READY_TO_TEST | READY_TO_TEST | READY_TO_TEST | NEEDS_MANUAL_PROOF | READY_TO_TEST | repo-aware review or dossier operation | manual install/auth proof | READY_TO_TEST |
| Claude web/app | NEEDS_MANUAL_PROOF | NEEDS_MANUAL_PROOF | NOT_AVAILABLE_IN_CURRENT_ENVIRONMENT | READY_TO_TEST | NOT_AVAILABLE_IN_CURRENT_ENVIRONMENT | READY_TO_TEST | chat-only packet/review | manual proof | NEEDS_MANUAL_PROOF |
| ChatGPT web/app/project/custom GPT | NEEDS_MANUAL_PROOF | NEEDS_MANUAL_PROOF | NOT_AVAILABLE_IN_CURRENT_ENVIRONMENT | READY_TO_TEST | NOT_AVAILABLE_IN_CURRENT_ENVIRONMENT | READY_TO_TEST | chat-only packet/review | manual proof | NEEDS_MANUAL_PROOF |
| Kimi / Kimi K2 | NEEDS_MANUAL_PROOF | NEEDS_MANUAL_PROOF | NEEDS_MANUAL_PROOF | READY_TO_TEST | NEEDS_MANUAL_PROOF | READY_TO_TEST | chat-only or repo-aware review | manual proof | NEEDS_MANUAL_PROOF |
| DeepSeek | NEEDS_MANUAL_PROOF | NEEDS_MANUAL_PROOF | NEEDS_MANUAL_PROOF | READY_TO_TEST | NEEDS_MANUAL_PROOF | READY_TO_TEST | schema/logic review | manual proof | NEEDS_MANUAL_PROOF |
| Gemini web/app | NEEDS_MANUAL_PROOF | NEEDS_MANUAL_PROOF | NOT_AVAILABLE_IN_CURRENT_ENVIRONMENT | READY_TO_TEST | NOT_AVAILABLE_IN_CURRENT_ENVIRONMENT | READY_TO_TEST | chat-only packet/review | manual proof; no Gemini API call by default | NEEDS_MANUAL_PROOF |
| Perplexity | NEEDS_MANUAL_PROOF | NEEDS_MANUAL_PROOF | NOT_AVAILABLE_IN_CURRENT_ENVIRONMENT | READY_TO_TEST | NOT_AVAILABLE_IN_CURRENT_ENVIRONMENT | READY_TO_TEST | research/source validation | manual proof | NEEDS_MANUAL_PROOF |
| Antigravity | NEEDS_MANUAL_PROOF | NEEDS_MANUAL_PROOF | NEEDS_MANUAL_PROOF | READY_TO_TEST | NEEDS_MANUAL_PROOF | READY_TO_TEST | repo-aware coding/review | manual install/access proof | NEEDS_MANUAL_PROOF |
| local LLM apps | NEEDS_MANUAL_PROOF | NEEDS_MANUAL_PROOF | NEEDS_MANUAL_PROOF | READY_TO_TEST | NEEDS_MANUAL_PROOF | NEEDS_MANUAL_PROOF | local chat or local repo-aware operation | manual proof | NEEDS_MANUAL_PROOF |
| generic future repo-aware coding agents | NEEDS_MANUAL_PROOF | NEEDS_MANUAL_PROOF | NEEDS_MANUAL_PROOF | READY_TO_TEST | NEEDS_MANUAL_PROOF | NEEDS_MANUAL_PROOF | depends on agent | manual proof | NEEDS_MANUAL_PROOF |

## Rule

Do not claim a web/app agent can read, write, or execute against the repo unless proven in that environment.

