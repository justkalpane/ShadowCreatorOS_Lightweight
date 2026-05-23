# Source-Aware Runtime Decision Protocol

This protocol enforces deterministic runtime behavior for freshness-sensitive tasks.

## STEP 1 — Repo Startup

- Read `START_HERE_FOR_AGENTS.md`
- Read `AGENT_READ_ORDER.md`
- Read runtime contracts
- Load registry/director/agent/skill context

## STEP 2 — Task Freshness Classification

Classify task as:

- `EVERGREEN`
- `CURRENT_SENSITIVE`
- `REALTIME_REQUIRED`
- `USER_SOURCE_REQUIRED`
- `HIGH_STAKES_CURRENT`

## STEP 3 — Research Mode Selection

- `EVERGREEN` -> `repo_only` or `repo_plus_static_knowledge`
- `CURRENT_SENSITIVE` -> `web_assisted` preferred
- `REALTIME_REQUIRED` -> `real_time_web` required
- `USER_SOURCE_REQUIRED` -> user links or web required
- `HIGH_STAKES_CURRENT` -> `real_time_web` + citations required

## STEP 4 — Web Access Check

Set:

- `web_access_available=true/false/UNKNOWN`
- `web_access_used=true/false`
- `real_time_sources_used=true/false`

## STEP 5 — Source Decision Gate

If current info is required and web is unavailable or unused:

- `Research Sufficiency Gate = NEEDS_USER_APPROVAL` or `NEEDS_CONFIRMATION`
- Present options:
  - `ENABLE_WEB_RESEARCH`
  - `PROVIDE_SOURCE_LINKS`
  - `APPROVE_REPO_ONLY`
  - `CONTINUE_WITH_LIMITED_CONFIDENCE`
  - `STOP`

## STEP 6 — Tools Connectors Plugins Capability Gate

Before capability claims, assess:

- repo-defined tools
- repo-defined connectors
- repo-defined plugins
- runtime state: active vs planned vs gated

Status set:

- `ACTIVE`
- `AVAILABLE_BY_APPROVAL`
- `PLANNED`
- `NOT_ACTIVE`
- `NEEDS_CONFIRMATION`

## STEP 6B — Native Capability Routing

- Inspect available native agent capabilities.
- Inspect repo-defined tools/connectors/plugins.
- Map task to required capabilities using `registries/native_capability_routing_matrix.yaml`.
- Use `runtime_contracts/NATIVE_AGENT_CAPABILITY_INVENTORY_CONTRACT.md` for capability declaration format.
- Use `runtime_contracts/TOOLS_CONNECTORS_PLUGINS_ASSESSMENT_CONTRACT.md` for mission-layer assessment output.
- Use `registries/agent_runtime_selection_index.yaml` for agent-layer evidence binding when available.
- If a required capability is missing, gate must be `NEEDS_CONFIRMATION` or `NEEDS_USER_APPROVAL`.
- If an optional capability is unavailable, continue with disclosed limitation.
- If provider/n8n/media execution is required, stop and request explicit approval.

## STEP 7 — Output

Output must include:

- Research Sufficiency Gate
- source disclosure fields
- tools/connectors/plugins assessment
- final confidence level
- unsupported claims list

## SOURCE_RESEARCH_LOCK FOR CURRENT PROMPTS

For prompts containing latest, current, this week, new update, today, 2026, or watch this week:

- `SOURCE_RESEARCH_LOCK` is mandatory.
- `sources_used_before_output=true` is required for `PASS`.
- A source list must be present before latest/current claims.
- `unsupported_claims` must be listed.
- If web access is unavailable, ask the user to continue limited mode or provide sources.
- Do not invent latest tools, updates, sources, dates, or claims.
