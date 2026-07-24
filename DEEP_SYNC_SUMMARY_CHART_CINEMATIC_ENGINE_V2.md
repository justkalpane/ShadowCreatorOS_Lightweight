# Deep Sync Summary Chart - Cinematic Engine V2

| Category | Current System Identity | Intended Future System Identity | What Is Working | What Is Broken | What Is Drifted | What Is Missing | What Is Reusable | What Must Be Refactored | What Must Be Added | What Must Be Preserved | Risk Level | Patch Phase | Evidence Reference |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Core identity | Lightweight Shadow OS content engine with strong media support | Cinema-first filmmaking engine with a downstream distribution layer | Repo-first law, route expansion law, consumption law, media-production stack | No dedicated film screenplay route | `SCRIPT_GENERATION` still means YouTube/content scripting | Film route family, film contracts, film validators, film schemas | Route law, director estate, media factory, voice/editing/distribution lanes | Script-core language, hook-first default framing, platform-first routing in the core | `FILM_SCREENPLAY_GENERATION`, `FILM_STORY_DEVELOPMENT`, film output packet schema | `MEDIA_FACTORY_HANDOFF`, `FULL_VIDEO_PIPELINE`, `VOICE_CONTEXT`, `EDITING_PACKAGING` | High | Phase 1 director and route split | `registries/route_manifests/script_generation.yaml`, `runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md`, `registries/route_manifests/media_factory_handoff.yaml` |
| Governance | Strong repo-law and route-law backbone | Same backbone, extended to film routes | `TASK_INTENT_ROUTING_CONTRACT`, `ROUTE_DEPENDENCY_EXPANSION_PROTOCOL`, `DIRECTOR_SKILL_CONSUMPTION_PROTOCOL` | Live governed runtime bridge still placeholder-based | Runtime proof is separate from repo read | Durable HTTPS Shadow host | Route/consumption/governance contracts | Nothing major; extend rather than replace | Bridge host, runtime deployment proof | Keep no-bypass law and source honesty | High | Bridge/runtime later; repo audit now | `runtime_contracts/TASK_INTENT_ROUTING_CONTRACT.md`, `runtime_contracts/ROUTE_DEPENDENCY_EXPANSION_PROTOCOL.md`, `openapi/custom_gpt_shadow_orchestrator_actions.openapi.yaml` |
| Directorial layer | Mixed cinematic + platform/content language | Film-mode directors plus downstream distribution directors | Cinematic council and production council already exist | Platform-fit language still leaks into high-authority directors | Krishna/Chanakya/Narada/Durga/Saraswati still pull toward platform metrics | Film-mode separation fields and film-specific director wording | Nataraja, Maya, Tumburu, Arjuna, Vishwakarma, Garuda, Varuna, Indra, Brahma | High-authority wording in core decision layers | Cinema mode / distribution mode split, film-scoring terms | Director architecture and council structure | Medium-High | Phase 1 | `directors/DIRECTOR_REGISTRY_MANIFEST.yaml`, `directors/supreme_vision/krishna.md`, `directors/strategy/chanakya.md`, `directors/strategy/narada.md`, `directors/strategy/durga.md`, `directors/distribution/saraswati.md`, `directors/production/maya.md`, `directors/cinematic/nataraja.md` |
| Script generation | Hook, retention, beat-map, content-engine discipline | Screenplay-first, scene-turn-first, filmcraft-aware core | Cinematic story block, source honesty, dynamic beats | Still YouTube-first in trigger terms and cadence law | Opening hook + recurring re-hooks dominate the core route | Save the Cat / three-act / scene dramaturgy / subtext / blocking / composition contracts | Content-engine and beat-map machinery | Content-first quality gates into film-specific gates | Film screenplay route, screenplay validators, screenplay packet schema | Retain content engine as downstream social route | High | Phase 1-2 | `registries/route_manifests/script_generation.yaml`, `runtime_contracts/SCRIPT_QUALITY_ENFORCEMENT_CONTRACT.md`, `runtime_contracts/TASK_EXECUTION_STATE_MACHINE_CONTRACT.md`, `runtime_contracts/DYNAMIC_TIMED_BEAT_MAP_CONTRACT.md` |
| Media production | Strong downstream production and packaging lanes | Same lanes, clearly downstream of film core | Media factory handoff, voice, editing, packaging, full video pipeline | None severe in the downstream layer | None severe; this layer is already appropriate | None urgent; keep and integrate | `MEDIA_FACTORY_HANDOFF`, `FULL_VIDEO_PIPELINE`, `VOICE_CONTEXT`, `EDITING_PACKAGING` | Minimal refactor; mainly scope clarity | Better boundary text and route family mapping | Production councils and bridge contracts | Medium | Preserve and re-label | `registries/route_manifests/media_factory_handoff.yaml`, `registries/route_manifests/full_video_pipeline.yaml`, `registries/route_manifests/voice_context.yaml`, `registries/route_manifests/editing_packaging.yaml` |
| Validation | Many validators exist for content/media | Film-specific validators for screenplay craft | Existing validators for route, evidence, media, and runtime discipline | No screenplay-specific validation suite | Content validation is still the default | Film screenplay validators and contamination checks | Evidence / route / media validators | Add screenplay-specific checks | `validate_film_screenplay_output.py` class and related validators | Keep current validators intact | High | Phase 2 | `validators/validate_mac06_1a_output.py`, `validators/validate_route_claim_evidence_consistency.py`, `validators/validate_source_freshness_url_ledger.py`, `validators/validate_tool_provider_boundary.py` |
| Knowledge/doc handoff | Markdown and DOCX are both present | Synced handoff pair with matching content | Markdown is detailed and DOCX now confirms the same substance | None material in content | None material; only format flattening in DOCX | Optional explicit supersession note if future versions diverge | The handoff itself as a planning reference | No refactor needed yet | None | Preserve this handoff pair as current reference | Medium | Documentation cleanup | `/Users/apple/Downloads/SHADOW_OS_CINEMATIC_ENGINE_CODEX_HANDOFF_UPDATED.md`, `/Users/apple/Downloads/SHADOW_OS_CINEMATIC_ENGINE_CODEX_HANDOFF_UPDATED.docx` |

## Executive Readout

### Working

- Repo-first routing and consumption law.
- Cinematic and production councils.
- Media factory and downstream distribution layers.
- GitHub read-only action surface.

### Broken

- No dedicated film screenplay route.
- Core script generation remains YouTube/content-first.
- Governed Shadow runtime host is still placeholder-based.

### Drifted

- High-authority director language still carries creator, platform, viral, and engagement bias.
- Hook/re-hook cadence dominates the script core.

### Missing

- Film route manifest and slice.
- Film screenplay contracts.
- Film-specific validators.
- Film output packet schema.

### Reusable

- Route law.
- Director registry structure.
- Media production layers.
- Downstream platform distribution.

### Must Be Refactored

- `SCRIPT_GENERATION` core identity.
- Director wording in the high-authority lane.
- Content-engine quality gates that assume YouTube as default.

### Must Be Added

- Cinema-first route family.
- Screenplay craft contracts and validators.
- Film-mode / distribution-mode separation.
- Durable Shadow runtime bridge.

### Must Be Preserved

- Content engine as backup.
- Media factory.
- Full video pipeline.
- Voice, visual, editing, packaging, and distribution lanes.

## Risk Level

High, because the repo is structurally strong but the core route identity is still wrong for film-first work.

## Next Patch Phase

Phase 1: split the director and route identity so film requests stop falling into the content route, while preserving the downstream distribution stack.

