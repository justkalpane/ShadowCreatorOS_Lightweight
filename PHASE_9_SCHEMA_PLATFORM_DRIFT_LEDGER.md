# Phase 9 Schema Platform Drift Ledger

| Schema/File | Line or evidence reference | Term/finding | Current context | Classification | Reason | Proposed film-mode equivalent | Keep downstream? | Risk if ignored |
|---|---|---|---|---|---|---|---|---|
| `schemas/packets/youtube_script_packet.schema.json` | `1-60` | `youtube_script_packet` | Explicit platform script packet | REPLACE | This is platform-first, not cinema-first | `film_screenplay_output_packet.schema.json` | No | Film outputs can be shaped like YouTube drafts |
| `schemas/packets/tiktok_script_packet.schema.json` | `1-60` | `tiktok_script_packet` | Explicit platform script packet | MOVE | Useful downstream, not film-core | downstream platform packet | Yes | Keep in distribution layer only |
| `schemas/packets/platform_video_packet.schema.json` | `1-60` | `platform_video_packet` | Platform video packet | MOVE | Downstream packaging/release artifact | downstream platform packet | Yes | Good downstream, wrong core |
| `schemas/packets/platform_package_packet.schema.json` | `1-63` | `platform_package_packet` | Platform packaging packet | MOVE | Distribution/release packet | downstream platform package | Yes | Keep downstream |
| `schemas/packets/publish_ready_packet.schema.json` | `1-64` | publish readiness | Publishing readiness packet | MOVE | Release gate, not screenplay canon | downstream release packet | Yes | Safe downstream only |
| `schemas/packets/script_draft_packet.schema.json` | `1-39` | `hook`, `section_plan` | Draft packet is hook/section-plan driven | REFACTOR | Useful but content-draft language dominates | `film_screenplay_output_packet.schema.json` | Yes | Wrong default semantics for film |
| `schemas/packets/final_script_packet.schema.json` | `1-45` | `final_script_text`, `cta` | Final content script with CTA | REPLACE | CTA-centric final script, not film screenplay | film screenplay packet | No | False equivalence between script and screenplay |
| `schemas/packets/script_refinement_packet.schema.json` | `1-43` | `critique_log`, `refined_hook`, `refined_sections` | Content refinement packet | DUPLICATE | Keep for content mode, add film-mode equivalent later | film refinement packet | Yes | Useful, but not film-core |
| `schemas/packets/context_packet.schema.json` | `1-102` | `context_type` includes `script` / `runtime` / `resource_prep` | Broad context engineering packet | REFACTOR | Reusable, but too generic for film packet semantics | film context packet | Yes | Could dilute cinema-specific context |
| `schemas/packets/source_evidence_packet.schema.json` | `1-50` | sources, claims, lineage | Source/evidence packet | KEEP | Reusable proof spine | film source ledger / fact map | Yes | Safe governance support |
| `schemas/packets/lineage_packet.schema.json` | `1-47` | lineage, decision_log | Lineage packet | KEEP | Reusable provenance support | film lineage packet | Yes | Good governance support |
| `schemas/runtime_state/route_state_capsule.schema.json` | `1-220` | route-state capsule for Media Factory | Route-state capsule | REFACTOR | Strong state capsule, but Media Factory-specific | film route-state capsule | Yes | Could be repurposed later |
| `runtime/state/route_state.schema.json` | `1-116` | route_phase, task_mode, read_ledger | Route state persistence | REFACTOR | Good route-state schema, but content modes dominate | film route-state schema | Yes | Needs film route mode expansion |
| `schemas/registry/empire_registry.schema.json` | `1-60` | registry identity | Registry schema | KEEP | Governance/identity scaffolding | none immediate | Yes | Reusable infrastructure |
| `schemas/quality/quality_scorecard.schema.json` | `1-63` | script/hook/retention/platform scores | Content scorecard | REFACTOR | Scoring language is content-mode biased | film validation scorecard | Yes | Could be mistaken for film canon |
| `schemas/packets/media_quality_gate_packet.schema.json` | `1-45` | media QA scores | Media QA packet | MOVE | Downstream media support | downstream media quality packet | Yes | Useful only downstream |
| `schemas/packets/voice_context_packet.schema.json` | `1-67` | voice persona, pace, emotion_map | Voice handoff packet | MOVE | Good downstream voice packet, not screenplay packet | film dialogue/performance packet | Yes | Preserve downstream |
| `schemas/packets/scene_prompt_packet.schema.json` | `1-38` | visual_method, visual_dna, prompt | Scene prompt packet | MOVE | Downstream visual planning | film scene-design packet | Yes | Good media support |
| `schemas/packets/storyboard_export_packet.schema.json` | `1-36` | scene_count, pacing_metadata_path | Storyboard export packet | MOVE | Downstream media factory support | film storyboard handoff packet | Yes | Preserve downstream |
| `schemas/media_factory/visual_media_plan_row.schema.json` | `1-34` | visual DNA, camera motion, beat timing | Visual planning row | MOVE | Strong downstream visual planning, not screenplay canon | film scene visual plan packet | Yes | Downstream support only |
| `schemas/media_factory/final_visual_media_generation_draft.schema.json` | `1-120` | visual rows, scene sync, QA, contact sheet | Media factory draft packet | MOVE | Downstream production draft | film downstream handoff packet | Yes | Preserve downstream |
| `schemas/packets/research_brief_packet.schema.json` | `1-48` | brief, source_evidence_refs | Research brief | KEEP | Reusable research support | film research brief packet | Yes | Good generic support |
| `schemas/packets/script_segment_packet.schema.json` | `1-48` | segments, duration | Script segmentation | REFACTOR | Useful, but still content-script oriented | film scene segmentation packet | Yes | Could be repurposed later |
| `schemas/packets/script_strategy_packet.schema.json` | `1-45` | strategy, duration_target_sec | Strategy packet | REFACTOR | Content planning, not film screenplay canon | film story strategy packet | Yes | Not enough for film core |
| `runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md` | `1-220` | YouTube / Shorts / reel / rehook / story block | Content contract shapes packet expectations | REPLACE | It hard-codes content-style output laws into schema-linked expectations | film output contract | No | Directly drags schema validation toward content mode |
| `runtime_contracts/SCRIPT_QUALITY_ENFORCEMENT_CONTRACT.md` | `1-220` | hook, retention, cadence, article-like risk | Content quality contract | REPLACE | Validates spoken content, not film screenplay canon | film quality contract | No | Film route could pass content-only quality gates |
| `runtime_contracts/ROUTE_STATE_PERSISTENCE_CONTRACT.md` | `1-65` | route state, selected manifest/slice, validator results | Generic route-state contract | KEEP | Reusable governance spine | film route-state persistence contract | Yes | Safe to reuse |
| `runtime_contracts/MEDIA_FACTORY_ROUTE_RUNTIME_BINDING_CONTRACT.md` | `1-153` | Media Factory route runtime binding | Media/production runtime binding | MOVE | Important downstream binding, not film-core schema | film downstream binding if needed later | Yes | Keep downstream |

### Schema collision risk

The biggest collision risk is reusing the content-script packet family as if it were a film screenplay packet family. The packet shapes today are good for YouTube/content engineering, but they do not encode beat-sheet canon, character transformation, or scene dramaturgy.

## 3. What the current schemas can already express

The repo already supports:

* route-state capsules
* lineage and source evidence
* generic context packets
* content/script drafts
* final content script bodies
* platform/video packages
* visual media plans and storyboards
* voice context and media handoff
* scorecards and quality gates

What it does not yet support is a dedicated film screenplay packet with filmcraft structure fields.
