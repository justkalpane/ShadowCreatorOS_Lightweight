# Source Intelligence and Web Research Contract

This contract defines how repo-first work and source freshness work together.

## A. REPO_FIRST_BASELINE

- Agent must read repo doctrine and contracts first.
- Agent must route through registries/directors/skills before deciding web research mode.
- Repo doctrine controls research mode selection.

## B. RESEARCH_MODE_VALUES

- `repo_only`
- `repo_plus_static_knowledge`
- `web_assisted`
- `real_time_web`
- `provider_api_assisted`

## C. WEB_RESEARCH_REQUIRED_WHEN

- current news or current events are requested
- recent platform rules/policies are requested
- current tools/APIs/models behavior is requested
- prices/plans are requested
- product comparisons need current data
- trend analysis requires freshness
- stats may have changed
- user asks for citations
- legal/medical/financial or other high-stakes current claims
- prompt uses latest/current/today/now language

## D. WEB_RESEARCH_NOT_REQUIRED_WHEN

- evergreen conceptual scripts
- style rewrite only
- repo-internal implementation tasks
- historical repo analysis
- fictional/creative outputs without current factual claims

## E. SOURCE_DISCLOSURE_FIELDS

Every output must include:

- `research_mode=`
- `web_access_available=true/false/UNKNOWN`
- `web_access_used=true/false`
- `real_time_sources_used=true/false`
- `source_list=`
- `source_quality=`
- `freshness_date=`
- `current_fact_confidence=HIGH/MEDIUM/LOW/LIMITED`
- `citation_required=true/false`
- `unsupported_claims=`

## F. SOURCE_RULE

- If `real_time_sources_used=true`, `source_list` must not be empty.
- If `source_list` is empty, set `real_time_sources_used=false`.
- If internet is unavailable, do not invent citations.
- If using repo-only reasoning, explicitly disclose repo-only mode.
