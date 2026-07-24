# Phase 6 Runtime Contract Route Split Plan

## 1. Objective
Phase 6 audits the runtime contract layer so we can decide what must stay as generic Shadow governance and what must be split out for a future cinema-first route family. The goal is not to patch the contracts yet. The goal is to identify which contracts are still safe and reusable, which are content-first and should stay in `SCRIPT_GENERATION`, which belong downstream in media/distribution, and which film-specific contracts are still missing.

## 2. Relationship to Phases 1-5
Phase 1 found director-level platform drift.
Phase 2 found agent-level content and platform drift.
Phase 3 found subagent-level hook, trend, and retention drift.
Phase 4 found skill-level content-hook and retention drift plus missing filmcraft skills.
Phase 5 found subskill-level micro-behavior drift plus missing filmcraft subskills.
Phase 6 now checks whether the runtime contract layer itself legally forces the old behavior or can support cinema mode without breaking the existing content engine.

## 3. Contract inventory

| Contract | File path | Current role | Cinema-core ready? | Platform/content drift? | Recommended mode split | Patch priority | Notes |
|---|---|---:|---:|---:|---|---:|---|
| Task intent routing | `runtime_contracts/TASK_INTENT_ROUTING_CONTRACT.md` | Primary route classifier and fallback gate | Partial | Yes | Keep generic routing, add film route family | P0 | `SCRIPT_GENERATION` is explicitly YouTube/Shorts/reel oriented |
| Route dependency expansion | `runtime_contracts/ROUTE_DEPENDENCY_EXPANSION_PROTOCOL.md` | Forces complete required repo scope before output | Yes | No | Keep as-is | P0 | Strong generic governance spine |
| Director/skill consumption | `runtime_contracts/DIRECTOR_SKILL_CONSUMPTION_PROTOCOL.md` | Requires direct consumption of the selected route scope | Yes | No | Keep as-is | P0 | Excellent no-shallow-read law |
| Script quality enforcement | `runtime_contracts/SCRIPT_QUALITY_ENFORCEMENT_CONTRACT.md` | Script quality gate for content/script output | Partial | Yes | Refactor content gate, add film twin | P0 | Recurring hooks and content cadence remain dominant |
| Content engineering output | `runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md` | Output contract for scripts, visuals, voice, platform packaging | Partial | Yes | Split content vs film output families | P0 | Strong downstream stack, but content-first core |
| Dynamic timed beat map | `runtime_contracts/DYNAMIC_TIMED_BEAT_MAP_CONTRACT.md` | Time-slice beat map for scripts | Partial | Yes | Duplicate into film beat system | P1 | 25-second recurring hook cadence is content-first |
| Script story engine | `runtime_contracts/SCRIPT_STORY_ENGINE_CONTRACT.md` | Requires cinematic story block in 3-10 minute YouTube scripts | Partial | Yes | Keep content mode, mirror for film mode | P1 | Film story needs its own engine |
| Source-aware runtime decision | `runtime_contracts/SOURCE_AWARE_RUNTIME_DECISION_PROTOCOL.md` | Source honesty and proof requirement | Yes | No | Keep as-is | P0 | Reusable for film research and factual claims |
| Source quality classification | `runtime_contracts/SOURCE_QUALITY_CLASSIFICATION_CONTRACT.md` | Source ledger and fact-vs-anecdote law | Yes | No | Keep as-is | P0 | Strong reusable evidence law |
| Route state persistence | `runtime_contracts/ROUTE_STATE_PERSISTENCE_CONTRACT.md` | Durable route state capsule | Yes | No | Keep as-is | P0 | Good foundation for any future route family |
| Task execution state machine | `runtime_contracts/TASK_EXECUTION_STATE_MACHINE_CONTRACT.md` | Execution lifecycle, recurring hook gates, validation states | Partial | Yes | Refactor into content and film state machines | P0 | Currently assumes content-style script production |
| Shadow output mode | `runtime_contracts/SHADOW_OUTPUT_MODE_CONTRACT.md` | Output modes and proof-display law | Yes | No | Keep as-is | P1 | Good global mode law |
| Layman command gateway | `runtime_contracts/LAYMAN_COMMAND_GATEWAY_CONTRACT.md` | Alias-to-route gateway for layman commands | Partial | Yes | Keep gateway, split route payloads | P1 | `Shadow script:` maps into content-centric route logic |
| Consolidated output | `runtime_contracts/CONSOLIDATED_OUTPUT_CONTRACT.md` | Output packaging and proof visibility law | Yes | No | Keep as-is | P1 | Reusable shell for film outputs |
| No fake pass gate | `runtime_contracts/NO_FAKE_PASS_GATE.md` | Prevents false PASS claims | Yes | No | Keep as-is | P0 | Critical evidence law |
| Production intent enforcement | `runtime_contracts/PRODUCTION_INTENT_ENFORCEMENT_RULE.md` | Prevents technical success from being mistaken for production readiness | Yes | No | Keep as-is | P1 | Helpful for film/media pipelines |
| Media factory final draft | `runtime_contracts/MEDIA_FACTORY_FINAL_DRAFT_CONTRACT.md` | Downstream media creation handoff | Yes, downstream only | No | Keep downstream | P1 | Strong reusable media support, not screenplay core |
| Visual media generator draft | `runtime_contracts/VISUAL_MEDIA_GENERATOR_DRAFT_CONTRACT.md` | Execution-facing visual draft layer | Yes, downstream only | No | Keep downstream | P1 | Good for visual adaptation, not core film writing |
| Final visual media generation draft | `runtime_contracts/FINAL_VISUAL_MEDIA_GENERATION_DRAFT_CONTRACT.md` | Final visual prep contract | Yes, downstream only | No | Keep downstream | P2 | Documentation-only prep artifact |
| Editing timeline packet | `runtime_contracts/media_packets/EDITING_TIMELINE_PACKET_CONTRACT.md` | Editing packet | Yes, downstream only | No | Keep downstream | P2 | Strong post-script support |
| Script segment packet | `runtime_contracts/media_packets/SCRIPT_SEGMENT_PACKET_CONTRACT.md` | Script segment packet | Partial | Yes | Duplicate for film segmentation | P1 | Narration and retention framing remain content-first |
| Voice context packet | `runtime_contracts/media_packets/VOICE_CONTEXT_PACKET_CONTRACT.md` | Voice delivery packet | Yes, downstream only | No | Keep downstream | P2 | Useful for narration, not screenplay core |
| Visual context packet | `runtime_contracts/media_packets/VISUAL_CONTEXT_PACKET_CONTRACT.md` | Visual prompt packet | Yes, downstream only | No | Keep downstream | P2 | Downstream visual craft support |
| Video context packet | `runtime_contracts/media_packets/VIDEO_CONTEXT_PACKET_CONTRACT.md` | Video motion/context packet | Yes, downstream only | No | Keep downstream | P2 | Downstream production bridge |
| Music/SFX packet | `runtime_contracts/media_packets/MUSIC_SFX_PACKET_CONTRACT.md` | Audio cue packet | Yes, downstream only | No | Keep downstream | P2 | Useful for film delivery, not route intent |
| Provider handoff packet | `runtime_contracts/media_packets/PROVIDER_HANDOFF_PACKET_CONTRACT.md` | Provider boundary packet | Yes | No | Keep as-is | P1 | Good boundary law |
| Media quality gate packet | `runtime_contracts/media_packets/MEDIA_QUALITY_GATE_PACKET_CONTRACT.md` | Multi-layer quality gate | Partial | Yes | Split content and film quality families | P1 | Still written for script/retention/platform checks |
| Lineage approval packet | `runtime_contracts/media_packets/LINEAGE_APPROVAL_PACKET_CONTRACT.md` | Approval evidence packet | Yes | No | Keep as-is | P1 | Helpful for governance |

## 4. Contract family classification

### Core film compatible
- `ROUTE_DEPENDENCY_EXPANSION_PROTOCOL`
- `DIRECTOR_SKILL_CONSUMPTION_PROTOCOL`
- `SOURCE_AWARE_RUNTIME_DECISION_PROTOCOL`
- `SOURCE_QUALITY_CLASSIFICATION_CONTRACT`
- `ROUTE_STATE_PERSISTENCE_CONTRACT`
- `SHADOW_OUTPUT_MODE_CONTRACT`
- `CONSOLIDATED_OUTPUT_CONTRACT`
- `NO_FAKE_PASS_GATE`
- `PRODUCTION_INTENT_ENFORCEMENT_RULE`
- `PROVIDER_HANDOFF_PACKET_CONTRACT`
- `LINEAGE_APPROVAL_PACKET_CONTRACT`

### Content-route only
- `TASK_INTENT_ROUTING_CONTRACT`
- `SCRIPT_QUALITY_ENFORCEMENT_CONTRACT`
- `CONTENT_ENGINEERING_OUTPUT_CONTRACT`
- `DYNAMIC_TIMED_BEAT_MAP_CONTRACT`
- `SCRIPT_STORY_ENGINE_CONTRACT`
- `TASK_EXECUTION_STATE_MACHINE_CONTRACT`
- `LAYMAN_COMMAND_GATEWAY_CONTRACT`
- `MEDIA_QUALITY_GATE_PACKET_CONTRACT`
- `SCRIPT_SEGMENT_PACKET_CONTRACT`

### Downstream distribution only
- `MEDIA_FACTORY_FINAL_DRAFT_CONTRACT`
- `VISUAL_MEDIA_GENERATOR_DRAFT_CONTRACT`
- `FINAL_VISUAL_MEDIA_GENERATION_DRAFT_CONTRACT`
- `EDITING_TIMELINE_PACKET_CONTRACT`
- `VOICE_CONTEXT_PACKET_CONTRACT`
- `VISUAL_CONTEXT_PACKET_CONTRACT`
- `VIDEO_CONTEXT_PACKET_CONTRACT`
- `MUSIC_SFX_PACKET_CONTRACT`

### Needs film mirror
- `SCRIPT_QUALITY_ENFORCEMENT_CONTRACT`
- `CONTENT_ENGINEERING_OUTPUT_CONTRACT`
- `DYNAMIC_TIMED_BEAT_MAP_CONTRACT`
- `SCRIPT_STORY_ENGINE_CONTRACT`
- `TASK_EXECUTION_STATE_MACHINE_CONTRACT`
- `MEDIA_QUALITY_GATE_PACKET_CONTRACT`
- `SCRIPT_SEGMENT_PACKET_CONTRACT`

## 5. Film-core contract requirements
The current contract layer does not yet contain dedicated film-route legal spine documents for:
- film route intent
- screenplay structure
- Save the Cat beat sheet
- three-act / eight-sequence map
- character arc and desire
- character web / opposing force
- scene dramaturgy
- dialogue subtext
- visual motif / image system
- mise-en-scène / blocking / composition
- camera language
- sound motif
- performance direction
- screenplay format
- film continuity
- film output packet
- short film validation
- feature film validation
- content-vs-film route separation

## 6. Non-goals
Phase 6 does not patch contracts yet. It only records what is reusable, what must stay content-first, what belongs downstream, and what is still missing for cinema mode.

