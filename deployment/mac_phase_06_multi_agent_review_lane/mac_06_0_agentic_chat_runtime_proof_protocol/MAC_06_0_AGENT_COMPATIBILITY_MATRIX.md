# MAC-06.0 Agent Compatibility Matrix

| Agent | can_read_github_repo | can_write_local_repo | can_output_to_chat | can_generate_dossier_files | can_generate_chat_packet_only | can_perform_research | can_review_dossier | requires_manual_copy_paste | proof_status |
|---|---|---|---|---|---|---|---|---|---|
| Codex | PROVEN | PROVEN | PROVEN | PROVEN | PROVEN | PROVEN | PLANNED | false | PROVEN for repo-write dossier production |
| Claude | PLANNED | NEEDS_MANUAL_PROOF | PLANNED | NEEDS_MANUAL_PROOF | PLANNED | PLANNED | PLANNED | true unless integrated | NEEDS_MANUAL_PROOF |
| ChatGPT | PLANNED | NEEDS_MANUAL_PROOF | PLANNED | NEEDS_MANUAL_PROOF | PLANNED | PLANNED | PLANNED | true unless integrated | NEEDS_MANUAL_PROOF |
| Kimi | PLANNED | NEEDS_MANUAL_PROOF | PLANNED | NEEDS_MANUAL_PROOF | PLANNED | PLANNED | PLANNED | true unless integrated | NEEDS_MANUAL_PROOF |
| DeepSeek | PLANNED | NEEDS_MANUAL_PROOF | PLANNED | NEEDS_MANUAL_PROOF | PLANNED | PLANNED | PLANNED | true unless integrated | NEEDS_MANUAL_PROOF |
| Perplexity | PLANNED | NOT_AVAILABLE_IN_CURRENT_ENVIRONMENT | PLANNED | NOT_AVAILABLE_IN_CURRENT_ENVIRONMENT | PLANNED | PLANNED | PLANNED | true | NEEDS_MANUAL_PROOF |
| Gemini chat/app | PLANNED | NOT_AVAILABLE_IN_CURRENT_ENVIRONMENT | PLANNED | NOT_AVAILABLE_IN_CURRENT_ENVIRONMENT | PLANNED | PLANNED | PLANNED | true | NEEDS_MANUAL_PROOF |
| Antigravity | PLANNED | NEEDS_MANUAL_PROOF | PLANNED | NEEDS_MANUAL_PROOF | PLANNED | PLANNED | PLANNED | true unless installed | NEEDS_MANUAL_PROOF |
| Generic repo-aware coding agent | PLANNED | NEEDS_MANUAL_PROOF | PLANNED | NEEDS_MANUAL_PROOF | PLANNED | PLANNED | PLANNED | depends on agent | NEEDS_MANUAL_PROOF |

## Interpretation

Codex local repo-write production is proven. Cross-agent chat and reviewer behavior still requires manual or integrated proof before onboarding seal.

## Single-Agent Primary Interpretation

Codex proves one representative repo-aware single-agent path. Other agents do not need to be installed together for basic operation; each can be tested progressively in chat-only or repo-write mode.
