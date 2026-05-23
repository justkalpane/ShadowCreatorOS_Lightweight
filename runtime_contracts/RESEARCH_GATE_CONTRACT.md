# Research Gate Contract

Use this contract to make research sufficiency visible in chat.

## SHADOW_GATE_STATUS — Research Sufficiency Gate

```text
SHADOW_GATE_STATUS
- stage_name=Research Sufficiency Gate
- current_status=PASS/BLOCKED/NEEDS_USER_APPROVAL/NEEDS_CONFIRMATION
- research_mode=
- web_access_available=
- web_access_used=
- real_time_sources_used=
- source_list=
- evidence_used=
- issue_detected=
- recommendation=
- user_options=
- waiting_for_user_approval=true/false
```

## User Options

- `APPROVE_REPO_ONLY`
- `ENABLE_WEB_RESEARCH`
- `PROVIDE_SOURCE_LINKS`
- `REVISE_TOPIC`
- `CONTINUE_WITH_LIMITED_CONFIDENCE`
- `STOP`

## Mandatory Status Rule

If the task requires current web research but web access is unavailable or unused, `Research Sufficiency Gate` must be:

- `NEEDS_USER_APPROVAL`, or
- `NEEDS_CONFIRMATION`

It must not be marked `PASS`.

## SOURCE_RESEARCH_LOCK FOR CURRENT PROMPTS

For prompts containing latest, current, this week, new update, today, 2026, or watch this week:

- `SOURCE_RESEARCH_LOCK` is mandatory.
- `sources_used_before_output=true` is required for `PASS`.
- A source list must be present before latest/current claims.
- `unsupported_claims` must be listed.
- If web access is unavailable, ask the user to continue limited mode or provide sources.
- Do not invent latest tools, updates, sources, dates, or claims.
