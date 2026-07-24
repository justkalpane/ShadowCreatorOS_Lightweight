# Phase 1 Director Platform Drift Ledger

## Scope

This phase inspects only director-level files and director registries.

### Required sources

- `directors/DIRECTOR_REGISTRY_MANIFEST.yaml`
- `directors/DIRECTORS_05_TO_30_COMPLETE_SPECS.md`
- director files under:
  - `directors/supreme_vision/`
  - `directors/strategy/`
  - `directors/production/`
  - `directors/cinematic/`
  - `directors/distribution/`
  - `directors/kernel/`

### Scan note

All director-path files in scope were searched for the following terms:

`YouTube, Shorts, Instagram, TikTok, reel, reels, social, creator, viral, engagement, retention, platform, channel, distribution, publishing, audience, analytics, trend, trend score, platform fit, creator fit, voiceover, content engine, script generation`

The full scan across the director corpus found **3093 total term occurrences** across **69 director-path files**.

## Classification Legend

- `KEEP` = valid downstream distribution / production logic
- `REFACTOR` = wording should become film-mode or route-neutral
- `MOVE` = belongs in downstream distribution, not core screenplay generation
- `REPLACE` = unsafe platform-first language in a universal core role
- `DUPLICATE` = keep old behavior but add film-mode equivalent
- `DELETE` = obsolete or harmful after conversion

## Ledger

| Director | File path | Term/finding | Current context | Classification | Reason | Proposed film-mode wording | Keep downstream? | Risk if ignored |
|---|---|---|---|---|---|---|---|---|
| Krishna | `directors/supreme_vision/krishna.md` | `distribution_vein`, platform signals, audience data, viral scores, YouTube route language, recurring hooks | Core script routing still behaves like a creator/content engine and still names a YouTube route as its default script path | `REPLACE` | This is the highest-authority route family and currently anchors the content-first bias | “Cinema-first screenplay route with dramatic tension, scene arcs, and film intent; platform hooks stay downstream” | Yes, but only for downstream adaptation | Very high |
| Shakti | `directors/supreme_vision/shakti.md` | distribution velocity, engagement amplification, viral acceleration, platform APIs, audience analytics | Heavy audience-force language is useful, but it overweights platform growth logic | `REFACTOR` | Emotional force is useful in cinema, but the current framing is growth/engagement-heavy | “Dramatic-force amplifier, emotional intensity controller, scene pressure multiplier” | Yes, for downstream or support use | High |
| Chanakya | `directors/strategy/chanakya.md` | creator niche, creator skill, viral / monetization / audience_growth / brand_building, creator_fit, platform_fit | Story selection is being judged through creator/platform success terms | `REFACTOR` | These are valid business filters, but not the right core-screenplay objective | “Film opportunity fit, audience resonance, genre-market fit, story commercial viability” | Yes, as a downstream planning lens | High |
| Narada | `directors/strategy/narada.md` | trend analysis, distribution, optimization, platform signals, audience data, YouTube trends, channel logic | Trend and distribution intelligence is strong but too central to route selection | `MOVE` | Trend intelligence should inform research and release strategy, not decide screenplay fundamentals | “Film research signals, source signals, market signals, release signals” | Yes, downstream only | High |
| Vishnu | `directors/supreme_vision/vishnu.md` | cross-platform sync, multi-creator orchestration, platform resilience | Good orchestration layer, but the language assumes platform sync as a primary concern | `DUPLICATE` | Needs a film-mode equivalent for screenplay/scene continuity while preserving current sync behavior | “Film continuity sync, screenplay state sync, production continuity sync” | Yes, preserve current resilience path | Medium |
| Saraswati | `directors/distribution/saraswati.md` | content multiplication, audience expansion, channel optimization, platform compatibility, distribution calendar, YouTube/TikTok/Instagram repurposing | This is clearly downstream distribution and adaptation logic | `KEEP` | It is useful and should remain intact as a release/distribution layer | “Distribution adaptation, format repurposing, platform-ready packaging” | Yes, this is the downstream layer | Low |
| Garuda | `directors/cinematic/garuda.md` | rapid publishing, multi-platform deployment, metadata readiness, platform dispatch | Strong distribution dispatcher, already downstream-oriented | `KEEP` | This should stay as release velocity / dispatch logic | “Premiere dispatch, release packaging, distribution execution” | Yes, downstream only | Low |
| Varuna | `directors/cinematic/varuna.md` | audience segment profiles, platform format constraints, beat retention, continuity score, format variants | Useful for audience/format adaptation, but not core screenplay authority | `KEEP` | It supports adaptation and flow preservation across channels | “Film-format adaptation, release variant logic, continuity-preserving adaptation” | Yes, downstream adapter | Medium |
| Maya | `directors/production/maya.md` | creator visual brand, creator visual profile, style guide | Mostly production-brand alignment and style consistency | `KEEP` | Helpful as a film visual-language support layer | “Director visual language, film visual identity, production style guide” | Yes, production support | Low |
| Vishwakarma | `directors/production/vishwakarma.md` | metadata, creator dashboard, production support fields | Mostly production infrastructure and dashboard support | `KEEP` | Production backbone is reusable for film packets | “Production operations and build support” | Yes | Low |
| Nataraja | `directors/cinematic/nataraja.md` | editing style guide, creator style, ready for distribution, pacing quality, distribution preparation | Good rhythm engine, but still phrased through creator/distribution readiness | `KEEP` | Pacing and editing can serve cinema directly if retargeted later | “Scene rhythm, cut rhythm, beat cadence, editorial motion” | Yes | Medium |
| Tumburu | `directors/production/tumburu.md` | creator audio profile, voiceover direction, sonic branding, creator brand fit | Strong sound-and-voice support layer | `KEEP` | Sound motif and performance texture are useful in film mode too | “Sound motif, performance texture, dialogue sound, cinematic voice direction” | Yes | Low |
| Arjuna | `directors/production/arjuna.md` | reshoot timing, creator dashboard, production_score_fields incl. hook/retention/platform | Production execution is solid, but score fields still include content-route metrics | `KEEP` | The operational layer is reusable even if some scoring terms need later retargeting | “Shoot-plan score, scene readiness, production completion score” | Yes | Medium |
| Agni | `directors/production/agni.md` | trending topic, breaking news, viral moment, creator approval for acceleration | Fast-track logic is useful, but still trend-led | `REFACTOR` | Urgency should become opportunity and schedule pressure, not platform virality | “Opportunity urgency, production acceleration, schedule pressure” | Yes, as an acceleration advisor | Medium |
| Indra | `directors/cinematic/indra.md` | premium distribution, high-value audience conversion | Strong premium-finishing and release-readiness support | `KEEP` | Good downstream finishing logic; not a screenplay core issue | “Premium finish, release polish, audience conversion readiness” | Yes, downstream | Low |
| Durga | `directors/strategy/durga.md` | creator safety, audience safety, content safety, veto scope | Safety and veto control are valuable governance layers | `KEEP` | This is governance, not drift | “Safety governance and boundary enforcement” | Yes | Low |
| Yama | `directors/kernel/yama.md` | content distribution validation, platform policies, creator values, approval for distribution | Policy gate and post-publication compliance support | `KEEP` | This is a valid governance boundary and should remain downstream of core writing | “Governance, policy validation, release compliance” | Yes | Low |

## Classification Counts

- `KEEP`: 11
- `REFACTOR`: 3
- `MOVE`: 1
- `REPLACE`: 1
- `DUPLICATE`: 1
- `DELETE`: 0

## Highest-Risk Drift Findings

1. `Krishna` still uses `SCRIPT_GENERATION` and YouTube cadence as the default top-level route frame.
2. `Krishna` still binds retention/hook law to the route core instead of a downstream content lane.
3. `Shakti` is still defined primarily through engagement and viral velocity.
4. `Chanakya` still scores through `creator_fit` and `platform_fit`.
5. `Narada` still treats trend/platform analytics as a core decision signal.
6. `Vishnu` still frames cross-platform sync as a major orchestration concern without a film-mode sibling.
7. `Agni` still accelerates based on trending opportunity, which can pull the system back toward platform-chasing.
8. `Arjuna` still exposes `platform_score` in a production score field set that should later be retargeted.
9. `Saraswati` is valid downstream, but its channel-optimization language must not leak back into screenplay core.
10. `Garuda` is valid downstream, but it should remain clearly separated from film-authority routing.

## Preservation Notes

The following are valid downstream or production-support layers and should be preserved:

- `Saraswati` distribution and repurposing
- `Garuda` release dispatch
- `Varuna` format adaptation
- `Maya` visual identity support
- `Tumburu` audio / voice support
- `Vishwakarma` production build support
- `Nataraja` rhythm / editing support
- `Arjuna` production execution
- `Indra` premium release polish
- `Durga` and `Yama` governance

## Phase 1 Decision

The repo does **not** yet have a cinema-first director boundary. The current director estate is still biased toward creator/content execution at the highest route layer. That does not make the repo broken; it means the film split must be introduced deliberately and without deleting the valid downstream stack.
