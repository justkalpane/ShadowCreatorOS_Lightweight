# Shadow Creator OS - Agent Startup Law

You are operating inside ShadowCreatorOS_Lightweight.

For every user task, including simple layman requests, you MUST run repo-first Shadow orchestration before answering.

Never answer directly as a generic chatbot unless the user explicitly says:

- `bypass Shadow OS`
- `answer normally without repo`

## Default Behavior

1. Read `START_HERE_FOR_AGENTS.md`.
2. Read `AGENT_READ_ORDER.md`.
3. Read `AGENT_REPO_FIRST_OPERATING_DOCTRINE.md`.
4. Run Native Agent Capability Assessment.
5. Run Task Freshness Classification.
6. Run Research Mode Decision.
7. Run registry-first routing.
8. Select directors / agents / subagents / skills / subskills with evidence.
9. Assess tools / connectors / plugins.
10. If the task is content/script/video/media related, run the Shadow Content Engineering Output Standard.
11. Output to chat by default.

## Mandatory Mode

- `CHAT_ONLY_MODE` is default.
- No files are created by default.
- Repo-write requires explicit user approval.
- Full dossier requires explicit user request.
- n8n/providers/media execution require explicit approval.

## Forbidden

- Do not produce generic LLM output before repo routing.
- Do not skip registry-first selection.
- Do not claim realtime web research unless sources were actually used.
- Do not use invalid gate statuses.
- Do not create files unless approved.
- Do not claim n8n/provider/media execution unless actually executed with approval.

Allowed gate statuses only:

- `PASS`
- `BLOCKED`
- `NEEDS_USER_APPROVAL`
- `NEEDS_CONFIRMATION`
