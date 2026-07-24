# Phase 9: Schema Route Split Plan

## 1. Objective

Phase 9 audits the schema layer and designs the future data structures for cinema-first route separation. The goal is to keep the current governance, content, and media schemas intact where they are useful, while identifying the missing film-first packet family needed for screenplay-grade output.

## 2. Relationship to Phases 1-8

Phase 1 found director-level drift.
Phase 2 found agent-level drift.
Phase 3 found subagent-level drift.
Phase 4 found skill-layer drift and missing filmcraft skills.
Phase 5 found subskill-layer drift and missing filmcraft subskills.
Phase 6 found missing film contract family.
Phase 7 found missing film route family.
Phase 8 found missing film validator family.
Phase 9 now checks whether the schema layer can actually represent a cinema-first screenplay packet, route-state capsule, validation scorecard, and downstream handoff packet.

## 3. Schema inventory

I directly inspected the following schema files in this phase:

| Schema/File | File path | Current role | Cinema-core ready? | Platform/content drift? | Film-schema gap? | Patch priority | Notes |
|---|---|---|---|---|---|---|---|
| Route state capsule | `schemas/runtime_state/route_state_capsule.schema.json` | Governs Media Factory route state and unlock flags | Partial | Low | Yes | P1 | Strong state capsule, but Media Factory-specific |
| Route state capsule | `runtime/state/route_state.schema.json` | General route state persistence and read ledger | Partial | Low | Yes | P1 | Good route-state spine, not film-specific |
| Empire registry schema | `schemas/registry/empire_registry.schema.json` | Deployment/registry identity schema | Keep | Low | No | P2 | Useful governance registry, not packet output |
| Source evidence packet | `schemas/packets/source_evidence_packet.schema.json` | Source/claim packet with lineage and validation status | Keep | Low | Partial | P1 | Reusable evidence spine |
| Lineage packet | `schemas/packets/lineage_packet.schema.json` | Lineage and decision-log packet | Keep | Low | Partial | P1 | Reusable provenance support |
| Script draft packet | `schemas/packets/script_draft_packet.schema.json` | Draft script packet with hook and section plan | Refactor | Medium | Yes | P0 | Content-script packet, not film screenplay packet |
| Final script packet | `schemas/packets/final_script_packet.schema.json` | Final script payload with CTA | Replace | High | Yes | P0 | Content-mode final script packet |
| Script segment packet | `schemas/packets/script_segment_packet.schema.json` | Script segments and duration | Refactor | Medium | Yes | P1 | Useful but content-oriented |
| Script strategy packet | `schemas/packets/script_strategy_packet.schema.json` | Strategy and duration target | Refactor | Medium | Yes | P1 | Still content-script scoped |
| Context engineering packet | `schemas/packets/context_engineering_packet.schema.json` | Context-engineering output packet | Keep | Low | Partial | P1 | Reusable context spine |
| Context packet | `schemas/packets/context_packet.schema.json` | Context packet for topic/script/runtime/approval | Refactor | Medium | Yes | P1 | Broad, but not cinema-first |
| Research brief packet | `schemas/packets/research_brief_packet.schema.json` | Research brief and evidence refs | Keep | Low | Partial | P1 | Good research support |
| Script refinement packet | `schemas/packets/script_refinement_packet.schema.json` | Critique and refinement packet | Duplicate | Medium | Yes | P1 | Content-mode refinement only today |
| YouTube script packet | `schemas/packets/youtube_script_packet.schema.json` | Platform script packet | Replace | High | Yes | P0 | Explicit platform bias |
| TikTok script packet | `schemas/packets/tiktok_script_packet.schema.json` | Platform script packet | Move | High | Yes | P1 | Downstream platform-only |
| Platform video packet | `schemas/packets/platform_video_packet.schema.json` | Platform video packet | Move | High | Yes | P1 | Downstream platform-only |
| Platform package packet | `schemas/packets/platform_package_packet.schema.json` | Platform packaging packet | Move | High | Yes | P1 | Downstream distribution |
| Publish ready packet | `schemas/packets/publish_ready_packet.schema.json` | Publishing readiness packet | Move | High | Yes | P1 | Downstream release gate |
| Provider handoff packet | `schemas/packets/provider_handoff_packet.schema.json` | Provider execution handoff packet | Move | Medium | Partial | P1 | Downstream execution boundary |
| Voice context packet | `schemas/packets/voice_context_packet.schema.json` | Voice persona / pace / emotion packet | Move | Medium | Partial | P1 | Downstream voice handoff, not film-core schema |
| Scene prompt packet | `schemas/packets/scene_prompt_packet.schema.json` | Scene prompt for visual generation | Move | Medium | Partial | P1 | Downstream visual planning |
| Storyboard export packet | `schemas/packets/storyboard_export_packet.schema.json` | Storyboard export and scene sync packet | Move | Medium | Partial | P1 | Downstream media pipeline |
| Media quality gate packet | `schemas/packets/media_quality_gate_packet.schema.json` | Quality gate for media packets | Keep | Low | Partial | P2 | Generic quality support |
| Quality scorecard | `schemas/quality/quality_scorecard.schema.json` | Numeric script/media/platform scorecard | Keep | Low | Partial | P2 | Generic scorecard, not film canon |
| Visual media plan row | `schemas/media_factory/visual_media_plan_row.schema.json` | Scene-level visual media row | Move | Medium | Partial | P1 | Strong downstream visual planning |
| Final visual media generation draft | `schemas/media_factory/final_visual_media_generation_draft.schema.json` | Planning-stage media factory draft | Move | Medium | Partial | P1 | Downstream production packet |

## 4. Schema family classification

The current schema families group into these buckets:

* Route/state schemas: strong governance spine, but Media Factory and runtime-state oriented
* Registry schemas: useful deployment/identity scaffolding
* Content/script output schemas: strong and explicit, but platform and retention biased
* Source/proof/lineage schemas: reusable governance spine
* Quality scorecard schemas: reusable, but not cinema canon
* Media handoff schemas: strong downstream support
* Visual/voice/editing schemas: useful downstream production support
* Film-specific schema family: missing

There is no dedicated `film/` schema family yet.

## 5. Film-core schema requirements

A cinema-first schema layer needs:

* film route state capsule schema
* film screenplay output packet schema
* film source ledger / fact map schema
* film beat sheet schema
* film character arc map schema
* film character web / opposing force schema
* film scene dramaturgy map schema
* film dialogue subtext schema
* film visual motif / image system schema
* film mise-en-scène / blocking / composition schema
* film camera / lens / framing schema
* film sound motif / silence schema
* film performance direction schema
* film screenplay format status schema
* film downstream handoff schema
* film validation scorecard schema
* no-fake-film-PASS schema
* film-vs-content packet separation schema

## 6. Non-goals

This phase does not patch schemas yet. It only identifies the current content and media packet structure, the reusable governance spine, and the missing film-first packet family.
