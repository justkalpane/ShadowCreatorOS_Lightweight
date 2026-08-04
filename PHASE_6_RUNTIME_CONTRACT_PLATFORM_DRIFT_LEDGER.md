# Phase 6 Runtime Contract Platform Drift Ledger

| Contract/File | Line or evidence reference | Term/finding | Current context | Classification | Reason | Proposed film-mode equivalent | Keep downstream? | Risk if ignored |
|---|---|---|---|---|---|---|---|---|
| `runtime_contracts/TASK_INTENT_ROUTING_CONTRACT.md` | 59-84 | `SCRIPT_GENERATION` is triggered by YouTube/Shorts/reel/voiceover/script terms and routes through hook generation and content quality gates | Content-first route law | REPLACE | The core trigger language is platform/content oriented | `FILM_SCREENPLAY_GENERATION` route family | No | Film prompts will keep being treated like creator scripts |
| `runtime_contracts/TASK_INTENT_ROUTING_CONTRACT.md` | 104-139 | `CONTEXT_ENGINEERING` and `VOICE_CONTEXT` are downstream route branches, not film-core branches | Content pipeline branch | MOVE | Useful but downstream of film writing | Film context and film voice handoff branches | Yes | Film prompts may be collapsed into narration-only output |
| `runtime_contracts/TASK_INTENT_ROUTING_CONTRACT.md` | 164-196 | `EDITING_PACKAGING` and `FULL_VIDEO_PIPELINE` are downstream media routes | Downstream packaging stack | KEEP | These are valid distribution/post-write layers | Film release-adaptation / packaging layer | Yes | Safe media support may be lost if over-refactored |
| `runtime_contracts/SCRIPT_QUALITY_ENFORCEMENT_CONTRACT.md` | 3-15, 17-58 | Script gate requires script-story, language, research, beat map, media factory draft, and hook quality | Script/content gate | REPLACE | Gate is written around content scripts and recurring hooks | Film screenplay quality gate | No | Film quality will be judged by the wrong rubric |
| `runtime_contracts/SCRIPT_QUALITY_ENFORCEMENT_CONTRACT.md` | 60-98 | Cadence and recurring hook density are central | Retention-centric cadence law | REPLACE | 25-second re-hook cadence is content-first | Film scene escalation / act-turn cadence | No | Cinema scenes could be forced into social retention cadence |
| `runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md` | 3-23, 128-216 | 3-10 minute scripts need a cinematic short story block, hook variants, recurring re-hooks, and platform packaging | Creator-content output contract | REPLACE | Strong content logic, but still creator-first | Film output packet with beat sheet / scene list / screenplay | No | Film prompts stay trapped in YouTube structure |
| `runtime_contracts/DYNAMIC_TIMED_BEAT_MAP_CONTRACT.md` | 6-17, 33-66 | 15-second grids and recurring re-hooks with 25-second cadence | Timed content beat map | MOVE | Useful for content narration, not film core | Film scene / sequence beat map | Yes | Timing becomes false authority for screenwriting |
| `runtime_contracts/SCRIPT_STORY_ENGINE_CONTRACT.md` | 5-16, 22-38 | Mandatory cinematic short story block for 3-10 minute YouTube scripts | YouTube story bridge law | REPLACE | It hard-codes platform context | Cinema story engine for film opening movement | No | Film opening blocks will be content-optimized |
| `runtime_contracts/TASK_EXECUTION_STATE_MACHINE_CONTRACT.md` | 120-168 | `RECURRING_HOOK_DENSITY_LOCK` and `CINEMATIC_STORY_GATE` are coupled to 5-minute script output | Content script state machine | REPLACE | State machine is centered on hook cadence and CTA loops | Film screenplay state machine | No | Wrong state transitions for film core |
| `runtime_contracts/ROUTE_DEPENDENCY_EXPANSION_PROTOCOL.md` | 3-16, 57+ | Requires full route scope and the content-engineering contract for content/video/script tasks | Good generic dependency law, but content contract is hard-wired | REFACTOR | The dependency system is strong, but one dependency family is content-first | Film dependency expansion family | Yes | Film route would inherit the content dependency set by default |
| `runtime_contracts/DIRECTOR_SKILL_CONSUMPTION_PROTOCOL.md` | 79-102 | Requires specific content-route ledgers and exact open/read proof before output | Good consumption law, route-specific scope still content-centric | REFACTOR | The protocol is reusable, but current route bindings are not film aware | Film director/skill consumption set | Yes | Hard to prove film-mode director reading without a new scope |
| `runtime_contracts/LAYMAN_COMMAND_GATEWAY_CONTRACT.md` | 38-42, 70-108 | `Shadow script:` alias maps into `SCRIPT_GENERATION` and content routes | Layman gateway | REPLACE | Alias is wired into content generation, not cinema-first routing | `Shadow film:` or film-aware alias path | No | Layman film commands will misroute |
| `runtime_contracts/ROUTE_STATE_PERSISTENCE_CONTRACT.md` | 11-21 | Route state capsule, dependency tracking, and output-phase tracking | Generic state law | KEEP | Strong generic backbone | Reusable for film route state | Yes | If broken, film and content routes both lose durable proof |
| `runtime_contracts/SOURCE_AWARE_RUNTIME_DECISION_PROTOCOL.md` | 100-154 | Source certainty and research gates | Generic research law | KEEP | Works for factual film development too | Reuse as film research law | Yes | Film research could become source-blind |
| `runtime_contracts/SOURCE_QUALITY_CLASSIFICATION_CONTRACT.md` | 39-109 | Source ledger, claim classes, fact-vs-anecdote map | Generic evidence law | KEEP | Reusable for film research and documentary proof | Reuse as film source law | Yes | Weak evidentiary film writing |
| `runtime_contracts/SHADOW_OUTPUT_MODE_CONTRACT.md` | 7-24, 47-50 | `PROOF_MODE`, `OPERATOR_MODE`, `DEBUG_MODE` and no fake PASS | Generic output law | KEEP | Good reusable output governance | Reuse unchanged | Yes | False completion claims across all routes |
| `runtime_contracts/CONSOLIDATED_OUTPUT_CONTRACT.md` | 21-74 | Consolidated output and evidence visibility | Generic packaging law | KEEP | Useful outer shell for any route | Reuse unchanged | Yes | Output drift and hidden proof gaps |
| `runtime_contracts/NO_FAKE_PASS_GATE.md` | 16-17, 48-84 | False PASS ban and proof bundle law | Generic governance | KEEP | Essential safety rail | Reuse unchanged | Yes | Self-certification risk |
| `runtime_contracts/PRODUCTION_INTENT_ENFORCEMENT_RULE.md` | 1-7, 21-75 | Technical success does not equal production success | Generic downstream safety | KEEP | Helpful for any media route | Reuse unchanged | Yes | Technical-only PASS could bypass real production needs |
| `runtime_contracts/MEDIA_FACTORY_FINAL_DRAFT_CONTRACT.md` | 78-133, 141-279, 425-640 | Visual creation DNA, scene sync, production proof gate | Downstream media production | KEEP | Valuable downstream support, not film screenplay core | Film release-adaptation support | Yes | If moved into core, film writing gets polluted by production packaging |
| `runtime_contracts/VISUAL_MEDIA_GENERATOR_DRAFT_CONTRACT.md` | 5-39, 97-155, 157-220 | Execution-facing visual generation draft with save order and batch orchestration | Downstream visual execution | KEEP | Strong for visual media handoff | Film visual adaptation handoff only | Yes | Do not let visual generation become screenplay authority |
| `runtime_contracts/FINAL_VISUAL_MEDIA_GENERATION_DRAFT_CONTRACT.md` | 3-52, 61-83 | Documentation-only final visual prep packet | Downstream prep artifact | KEEP | Harmless as prep-only | Keep downstream | Yes | None if left downstream |
| `runtime_contracts/media_packets/SCRIPT_SEGMENT_PACKET_CONTRACT.md` | required fields / retention purpose / CTA role | Script segmentation with retention framing | Content micro-packet | REPLACE | Retention purpose and CTA role are content-first | Film scene packet or screenplay beat packet | Yes, downstream only | Film scenes will inherit creator-retention micro-logic |
| `runtime_contracts/media_packets/MEDIA_QUALITY_GATE_PACKET_CONTRACT.md` | media quality fields include hook/retention/platform | Mixed media/content gate | REPLACE | It still grades script/hook/retention/platform behavior | Film production quality packet | Yes | Film quality would be judged like creator content |
| `runtime_contracts/media_packets/VOICE_CONTEXT_PACKET_CONTRACT.md` | voice persona, pace, pause map, emotion per segment | Voice delivery packet | KEEP | Good downstream narration support | Film narration / voiceover support | Yes | None for film screenplay core |
| `runtime_contracts/media_packets/VIDEO_CONTEXT_PACKET_CONTRACT.md` | camera movement, tool targets, aspect ratio, continuity | Video motion packet | KEEP | Useful downstream | Film visual handoff packet | Yes | None if not used as screenplay authority |
| `runtime_contracts/media_packets/VISUAL_CONTEXT_PACKET_CONTRACT.md` | composition, lighting, lens, style bible, visual DNA | Visual prompt packet | KEEP | Good downstream visual support | Film visual handoff packet | Yes | None if not used as screenplay authority |
| `runtime_contracts/media_packets/MUSIC_SFX_PACKET_CONTRACT.md` | music mood / tempo / silence / beat drops | Audio packet | KEEP | Good downstream production support | Film sound motif handoff packet | Yes | None |
| `runtime_contracts/EDITING_TIMELINE_PACKET_CONTRACT.md` | timeline, sync, aspect ratio, b-roll map | Editing packet | KEEP | Downstream only | Film editing-adaptation packet | Yes | None |

## Classification summary
- KEEP: 12
- REFACTOR: 3
- MOVE: 2
- REPLACE: 9
- DUPLICATE: 0
- DELETE: 0
- NEEDS_DESIGN_DECISION: 0
- MISSING_FILM_CONTRACT: 19
- REGISTRY_FILE_MISMATCH: 0 observed in this audit set
- READ_BLOCKED: 0

## High-risk drift pattern
The highest-risk drift is the repeated use of content-cadence laws, hook density laws, recurring re-hook laws, and platform-specific script packaging rules as if they were universal screenplay laws. The generic governance contracts are strong, but the route-specific content contracts still dominate the current script path.

## Film-mode equivalent direction
The film-mode equivalent should not delete the content engine. It should sit beside it, with a dedicated cinema screenplay family that can consume the reusable governance contracts while replacing the content-retention defaults with film structure, scene dramaturgy, dialogue subtext, visual motif, composition, sound motif, and performance direction laws.

