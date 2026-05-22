# Shadow Research Gate

Use this skill for any request involving:

- latest
- current
- trend
- news
- facts
- tools
- models
- pricing
- platform rules
- citations
- real-time
- statistics

## Required Behavior

1. Classify task freshness before answering.
2. Disclose web access status.
3. If web is used, include source list.
4. If web is not used, set `real_time_sources_used=false`.
5. Do not claim realtime or current research without retrieved sources.
6. If current information is required and web access is unavailable, use `NEEDS_USER_APPROVAL` or `NEEDS_CONFIRMATION`.

Allowed gate statuses only:

- `PASS`
- `BLOCKED`
- `NEEDS_USER_APPROVAL`
- `NEEDS_CONFIRMATION`

## Proof Implications

- `PASS`: freshness classification, research mode decision, source disclosure, and valid gate status are present.
- `PARTIAL`: source limitation exists but is disclosed and gated.
- `FAIL`: fake realtime/source claims, missing source list for web research, or invalid gate status.
