# Phase 11R Platform-to-Cinema Drift Ledger

This ledger records where platform/content vocabulary still appears across the audit chain and whether that language is valid downstream or risky for cinema-core law.

Most of the findings below are **not bugs**. They are usually either:

- intentional content-mode law
- downstream distribution law
- contrast language used to define film separation

The main risk is not that the terms exist. The risk is that the film core could inherit them without an explicit boundary rule.

| Doc | Line/reference | Term/finding | Current context | Is this valid downstream? | Is this leaking into cinema-core? | Required action | Priority | Notes |
|---|---|---|---|---|---|---|---|---|
| `DEEP_SYNC_SUMMARY_CHART_CINEMATIC_ENGINE_V2.md` | 5, 8, 25, 31 | `SCRIPT_GENERATION`, hook/retention/content-engine core | Historic baseline summary of the content-first engine | Yes | Yes, as a baseline contrast only | `SPLIT_CONTENT_VS_FILM` | High | This is the root reason the film split exists |
| `PHASE_1_DIRECTOR_ROUTE_SPLIT_PLAN.md` | 5, 7, 36 | YouTube/content-first route vs film-first route | Intentional separation language | Yes | No, it is explicitly a separation doc | `NO_ACTION` | Low | Safe contrast language |
| `PHASE_1_DIRECTOR_PLATFORM_DRIFT_LEDGER.md` | 40-55, 69-77 | YouTube, viral, platform, creator, audience, retention | High-authority director drift inventory | Yes, downstream only | Mildly, because it sits at high authority | `ADD_EXPLICIT_ANTI_COLLISION_RULE` | High | Needs durable boundary text so the core does not inherit it |
| `PHASE_2_AGENT_PLATFORM_DRIFT_LEDGER.md` | 56-72 | trend, platform score, recurring hooks, distribution | Agent drift inventory | Yes, downstream only | Mildly, if reused in film-mode routing | `MOVE_TO_DISTRIBUTION_LAYER` | High | The content agent is valid; the film agent must be separate |
| `PHASE_3_SUBAGENT_PLATFORM_DRIFT_LEDGER.md` | hook / retention / open-loop family hits | content micro-behaviors | Content-mode subagent bias | Yes | No, if kept content-only | `KEEP_DOWNSTREAM` | Medium | Good content control, but not film-core law |
| `PHASE_4_SKILL_PLATFORM_DRIFT_LEDGER.md` | retention engineer, re-hook system, platform-fit skills | Content-retention skills | Yes | No, if they stay content-only | `MOVE_TO_DISTRIBUTION_LAYER` | High | These are important, but they are not screenplay canon |
| `PHASE_5_SUBSKILL_PLATFORM_DRIFT_LEDGER.md` | content angle, hook variation, open loop, cliffhanger, retention loop | Micro-behaviors for creator content | Yes | No, if film mirrors are added later | `SPLIT_CONTENT_VS_FILM` | High | These are the clearest content-first micro-laws |
| `PHASE_6_RUNTIME_CONTRACT_PLATFORM_DRIFT_LEDGER.md` | 5-12, 18-24, 28, 31 | `SCRIPT_GENERATION`, recurring hooks, 25-second cadence | Content-first runtime contracts | Yes | Yes, unless explicitly blocked from film core | `BLOCK_FROM_FILM_CORE` | High | Needs a hard anti-collision rule in the implementation plan |
| `PHASE_7_ROUTE_PLATFORM_DRIFT_LEDGER.md` | route manifests / slices for script and media | route split support | Downstream routing and content routing | Yes | No, because the split is the point | `NO_ACTION` | Low | Keep the valid downstream routes intact |
| `PHASE_8_VALIDATOR_PLATFORM_DRIFT_LEDGER.md` | 5-10, 21-26, 44 | hook, retention, cadence, spoken runtime, media checks | Content-style validators | Yes | Yes, if reused for film PASS | `ADD_EXPLICIT_ANTI_COLLISION_RULE` | High | Film validators must not inherit content PASS logic |
| `PHASE_9_SCHEMA_PLATFORM_DRIFT_LEDGER.md` | 5-10, 19, 24, 29-30 | YouTube/TikTok packet shapes, quality scorecard | Content-mode schema spine | Yes, downstream only | Yes, if reused for film packets | `BLOCK_FROM_FILM_CORE` | High | Reusing these schemas raw would blur film-vs-content separation |
| `PHASE_10_TEST_FIXTURE_MATRIX.md` | FP-007, CP-006, NF-007 | film packet completeness vs content preservation | Fixture separation logic | Yes | No, if the fixtures are used as guards | `NO_ACTION` | Low | Good acceptance design |
| `PHASE_11_IMPLEMENTATION_PATCH_PLAN.md` | 5-11, 52-61, 79-145, 184-207 | film schema / contract / validator / route sequence | Implementation staging plan | Yes | No, because it is explicitly additive | `NO_ACTION` | Low | This is the correct construction order |
| `PHASE_11_PATCH_UNIT_LEDGER.md` | 1-30 | schema / contract / validator / route / wiring units | Rollout map | Yes | No | `NO_ACTION` | Low | Good rollout structure; no extra drift |
| `PHASE_11_ACCEPTANCE_ROLLBACK_PLAN.md` | 8-21, 54-73, 86-111 | go/no-go, rollback, no-go, fake PASS blocks | Acceptance and rollback discipline | Yes | No | `NO_ACTION` | Low | Strong safety layer |

## Summary

The platform vocabulary still appears throughout the chain, but most of it is either:

- intentionally retained as downstream distribution logic, or
- intentionally named as the thing to separate from film-core law

The main unresolved drift is the risk that `SCRIPT_GENERATION`, hook cadence, or retention logic could be reused as film truth without an explicit anti-collision boundary.
That boundary should be injected before Phase 12.

