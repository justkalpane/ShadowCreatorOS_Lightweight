# Phase 3 Subagent Route Split Plan

## 1. Objective
Phase 3 audits the subagent layer so we can separate cinema-first filmmaking support from the existing YouTube/content-engine subagent stack without breaking current behavior.

The goal is not to remove the existing route families. The goal is to understand which subagents are already safe as downstream support, which ones should be duplicated for film mode, and which ones currently carry platform/content drift that should not be allowed to define the core film screenplay path.

## 2. Relationship to Phase 1 and Phase 2
Phase 1 established that the director layer still has route bias and needs a film-versus-content split.

Phase 2 showed the agent layer is largely generic support infrastructure, with a smaller number of script-oriented agents carrying the strongest content drift.

Phase 3 now checks whether the subagents can support the future cinema routes:

- `FILM_SCREENPLAY_GENERATION`
- `FILM_STORY_DEVELOPMENT`
- `CINEMATIC_DIRECTOR_PLAN`
- `FEATURE_FILM_PRODUCTION_PIPELINE`
- `FILM_RELEASE_DISTRIBUTION`

## 3. Subagent inventory
The repository currently exposes 36 subagent files through `subagents/SUB_AGENT_RUNTIME_REGISTRY.yaml` and `registries/sub_agent_matrix.json`.

| Subagent | File path | Current role | Cinema-core ready? | Platform/content drift? | Recommended mode split | Patch priority | Notes |
|---|---|---|---|---|---|---|---|
| cwf_110 | `subagents/cwf_110/cwf_110_sub_agent.py` | topic discovery | Partial | Low | REFACTOR | Medium | useful upstream research support; should become film-research aware |
| cwf_120 | `subagents/cwf_120/cwf_120_sub_agent.py` | topic qualification | Partial | Low | REFACTOR | Medium | good for premise filtering; wording is topic-led |
| cwf_130 | `subagents/cwf_130/cwf_130_sub_agent.py` | topic scoring | Partial | Low | REFACTOR | Medium | can become film-opportunity scoring |
| cwf_140 | `subagents/cwf_140/cwf_140_sub_agent.py` | research synthesis | Yes, as support | Low | REFACTOR | Medium | already research-oriented; needs film-first framing |
| cwf_210 | `subagents/cwf_210/cwf_210_sub_agent.py` | script generation | No | High | DUPLICATE | High | explicit YouTube opening-hook + recurring re-hook lane |
| cwf_220 | `subagents/cwf_220/cwf_220_sub_agent.py` | script critique | No | High | DUPLICATE | High | critiques cinematic story and hook density, but still content-script framed |
| cwf_230 | `subagents/cwf_230/cwf_230_sub_agent.py` | script refinement | No | High | DUPLICATE | High | repairs flat sections and re-hook placement; should gain film equivalent |
| cwf_240 | `subagents/cwf_240/cwf_240_sub_agent.py` | script packaging | No | High | DUPLICATE | High | preserves recurring re-hook map through final shaping and scene sync |
| cwf_310 | `subagents/cwf_310/cwf_310_sub_agent.py` | context engineering | Partial | Medium | REFACTOR | Medium | useful for film context packets once route-neutral |
| cwf_320 | `subagents/cwf_320/cwf_320_sub_agent.py` | platform packager | No | High | MOVE | High | packaging belongs downstream, not in film-core |
| cwf_330 | `subagents/cwf_330/cwf_330_sub_agent.py` | asset brief generator | Partial | Medium | MOVE | Medium | useful downstream for packaging, not screenplay core |
| cwf_340 | `subagents/cwf_340/cwf_340_sub_agent.py` | lineage validator | Yes, as support | Low | KEEP | Medium | governance support is reusable across both modes |
| cwf_410 | `subagents/cwf_410/cwf_410_sub_agent.py` | avatar/video context | Partial | Medium | MOVE | Medium | media factory support, not film writing core |
| cwf_420 | `subagents/cwf_420/cwf_420_sub_agent.py` | media factory handoff | Partial | Medium | MOVE | Medium | downstream execution handoff support |
| cwf_430 | `subagents/cwf_430/cwf_430_sub_agent.py` | voice context | Partial | Low | REFACTOR | Medium | reusable if recast as cinematic voice/performance context |
| cwf_440 | `subagents/cwf_440/cwf_440_sub_agent.py` | avatar/video context | Partial | Medium | MOVE | Medium | downstream visual support, not screenplay core |
| cwf_510 | `subagents/cwf_510/cwf_510_sub_agent.py` | platform metadata | No | High | KEEP | Low | valid downstream distribution support |
| cwf_520 | `subagents/cwf_520/cwf_520_sub_agent.py` | distribution planner | No | High | KEEP | Low | should remain downstream |
| cwf_530 | `subagents/cwf_530/cwf_530_sub_agent.py` | publish readiness | No | High | KEEP | Low | downstream release gate only |
| cwf_610 | `subagents/cwf_610/cwf_610_sub_agent.py` | performance metrics | No | Low | KEEP | Low | analytics support is downstream and reusable |
| cwf_620 | `subagents/cwf_620/cwf_620_sub_agent.py` | audience feedback | No | Medium | KEEP | Low | useful downstream signal, not film-core |
| cwf_630 | `subagents/cwf_630/cwf_630_sub_agent.py` | growth loop feedback | No | Medium | KEEP | Low | downstream optimization only |
| wf_000 | `subagents/wf_000/wf_000_sub_agent.py` | general support | Yes, as support | Low | KEEP | Low | infrastructure lane |
| wf_001 | `subagents/wf_001/wf_001_sub_agent.py` | general support | Yes, as support | Low | KEEP | Low | infrastructure lane |
| wf_010 | `subagents/wf_010/wf_010_sub_agent.py` | general support | Yes, as support | Low | KEEP | Low | infrastructure lane |
| wf_020 | `subagents/wf_020/wf_020_sub_agent.py` | governance support | Yes, as support | Low | KEEP | Low | governance lane |
| wf_021 | `subagents/wf_021/wf_021_sub_agent.py` | governance support | Yes, as support | Low | KEEP | Low | governance lane |
| wf_022 | `subagents/wf_022/wf_022_sub_agent.py` | governance support | Yes, as support | Low | KEEP | Low | governance lane |
| wf_023 | `subagents/wf_023/wf_023_sub_agent.py` | governance support | Yes, as support | Low | KEEP | Low | governance lane |
| wf_100 | `subagents/wf_100/wf_100_sub_agent.py` | topic pack | Partial | Low | REFACTOR | Medium | upstream discovery support |
| wf_200 | `subagents/wf_200/wf_200_sub_agent.py` | script generation parent | No | High | DUPLICATE | High | current parent for content scripts; must get film twin |
| wf_300 | `subagents/wf_300/wf_300_sub_agent.py` | context pack | Partial | Medium | REFACTOR | Medium | good base for film context mode |
| wf_400 | `subagents/wf_400/wf_400_sub_agent.py` | voice/context/media pack | Partial | Medium | MOVE | Medium | downstream media/context support |
| wf_500 | `subagents/wf_500/wf_500_sub_agent.py` | publishing distribution pack | No | High | KEEP | Low | downstream release lane |
| wf_600 | `subagents/wf_600/wf_600_sub_agent.py` | analytics evolution pack | No | Low | KEEP | Low | downstream analytics lane |
| wf_900 | `subagents/wf_900/wf_900_sub_agent.py` | error handler | Yes, as support | Low | KEEP | Low | cross-cutting system safety lane |

## 4. Film-core subagent requirements
A cinema-first subagent stack should support:

- film research brief subagent
- story premise subagent
- screenplay beat-sheet subagent
- character-web subagent
- scene-dramaturgy subagent
- dialogue-subtext subagent
- visual-motif subagent
- composition/blocking subagent
- shot-design subagent
- sound-motif subagent
- performance-direction subagent
- continuity-check subagent
- film validation subagent
- downstream release-adaptation subagent

## 5. Non-goals
Phase 3 does not:

- patch subagent code
- patch skills or subskills
- patch contracts, validators, schemas, or route manifests
- add `FILM_SCREENPLAY_GENERATION`
- delete the existing YouTube/content path
- claim runtime proof
- claim PASS states

## 6. Proposed next phases

- Phase 4: Skills
- Phase 5: Subskills
- Phase 6: Runtime contracts
- Phase 7: Route manifests and route slices
- Phase 8: Validators
- Phase 9: Output schemas
- Phase 10: NEET short-film test fixture
