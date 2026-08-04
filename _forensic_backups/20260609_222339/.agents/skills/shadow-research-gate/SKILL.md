---
name: shadow-research-gate
description: "Automatically use this skill whenever the task involves latest, current, trend, news, facts, tools, models, pricing, platform rules, citations, real-time claims, statistics, or source-backed output. Requires SHADOW_BOOT_CONFIRMATION, freshness classification, web access disclosure, source list if web used, and no fake realtime claims."
---

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
- real people or celebrities
- real incidents
- biographical or career claims
- brands, companies, platforms, or case studies used as proof

## Required Behavior

1. Classify task freshness before answering.
2. Disclose web access status.
3. If web is used, include source list.
4. If web is not used, set `real_time_sources_used=false`.
5. Do not claim realtime or current research without retrieved sources.
6. If current information is required and web access is unavailable, use `NEEDS_USER_APPROVAL` or `NEEDS_CONFIRMATION`.
7. If a real person, real incident, brand, company, factual case study, or
   biographical/career claim is used as proof, require web-assisted research
   when web access is available.
8. A named public figure or known real-world identity cannot be silently
   relabeled as a composite to avoid the source gate.
9. If the user names a public figure, known real-world identity, brand,
   company, or real incident, treat that anchor as real-person/real-world proof
   unless the user explicitly requests a fictionalized retelling.
10. If `unsupported_claims` is non-empty, `SOURCE_RESEARCH_LOCK` cannot be
   `PASS`.
11. If `real_time_sources_used=true`, require `source_list_present=true`.
12. If `web_access_used=true` but `real_time_sources_used=false`, classify the
    research as `WEB_ASSISTED_STATIC_REFERENCE` or
    `WEB_ASSISTED_LIMITED_REFERENCE`, never real-time research.
13. For real-person proof scripts, require source sufficiency: three sources,
    two non-encyclopedia sources, and three source categories where suitable
    sources are available.
14. Treat encyclopedia records as background context and interview reporting
    as anecdotal support unless independently verified.
15. Require `FACT_VS_ANECDOTE_MAP` for real-world proof claims.
16. When a recurring re-hook uses a person, incident, factual, or current
    proof claim, include it in `SOURCE_LEDGER` and `FACT_VS_ANECDOTE_MAP`.
17. For real-person proof scripts, check the spoken script line by line:
    numbers, milestones, jobs, locations, quotes, and biographical events must
    map back to a fact row or source row.
18. Do not let a single sourced anecdote mutate into a stronger universal or
    absolute script line.
19. Block off-topic current promo, teaser, or release-marketing lines unless
    the user explicitly requested that tie-in.

Allowed gate statuses only:

- `PASS`
- `BLOCKED`
- `NEEDS_USER_APPROVAL`
- `NEEDS_CONFIRMATION`

## Proof Implications

- `PASS`: freshness classification, research mode decision, source disclosure, and valid gate status are present.
- `PARTIAL`: source limitation exists but is disclosed and gated.
- `FAIL`: fake realtime/source claims, missing source list for web research, or invalid gate status.


MAC-06.2O ROUTE FAMILY PROPAGATION
route_families: [full_video_pipeline]
route_family_resolved: [full_video_pipeline]
