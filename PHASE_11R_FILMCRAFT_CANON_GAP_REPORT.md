# Phase 11R Filmcraft Canon Gap Report

This report checks whether the Phase 1 through Phase 11 chain contains enough real filmcraft canon to support Phase 12 implementation.

## Canon coverage matrix

| Canon area | Required techniques/books/systems | Present in Phase 1–11 docs? | Depth level | Missing details | Recommended doc update | Evidence/source status |
|---|---|---|---|---|---|---|
| Save the Cat beat sheet | Blake Snyder beat map and beat logic | Yes | USABLE | Needs explicit film validation rules and source-backed canon positioning | Add to film contract / validator supplements | REPO_EVIDENCED |
| Syd Field three-act paradigm / plot points | Three-act structure, Plot Points I/II | Yes | PARTIAL | Needs dedicated structure law and acceptance checks | Add to film contract / validator supplements | REPO_EVIDENCED |
| Robert McKee scene value turns | Value shift, scene turn, conflict shift | Yes | PARTIAL | Needs scene-turn-specific packet fields | Add to film scene dramaturgy supplement | REPO_EVIDENCED |
| Joseph Campbell / Christopher Vogler Hero’s Journey | Monomyth / mythic journey | Yes | PARTIAL | Needs optional canon mapping and validation rules | Add to film canon supplement | REPO_EVIDENCED |
| Dan Harmon Story Circle | Circle structure and story loop | Yes | PARTIAL | Needs explicit equivalence / optional use rule | Add to film canon supplement | REPO_EVIDENCED |
| John Truby 22-step system | 22 steps, moral argument, symbol web | Yes | PARTIAL | Needs much deeper structure coverage | Add to film canon supplement | REPO_EVIDENCED |
| Aristotle dramatic structure | Unity, reversal, recognition, catharsis | No | ABSENT | No dedicated mention or law | New canon supplement required | EXTERNAL_SOURCE_LEDGER_REQUIRED |
| Lajos Egri premise and character-driven drama | Premise, character, conflict, motivation | Yes | MENTION_ONLY | Needs deeper premise / character-law support | Add to film character and premise supplement | REPO_EVIDENCED |
| Linda Seger rewriting and script consulting | Rewrite diagnostics, story repair | No | ABSENT | No dedicated coverage | New canon supplement required | EXTERNAL_SOURCE_LEDGER_REQUIRED |
| Christopher Vogler mythic structure | Mythic adaptation of the hero model | Yes | MENTION_ONLY | Needs explicit mythic-structure mapping | Add to film canon supplement | REPO_EVIDENCED |
| David Mamet dramatic action | Action-driven scene craft | No | ABSENT | No dedicated coverage | New canon supplement required | EXTERNAL_SOURCE_LEDGER_REQUIRED |
| William Goldman screenplay craft | Practical screenplay practice | No | ABSENT | No dedicated coverage | New canon supplement required | EXTERNAL_SOURCE_LEDGER_REQUIRED |
| Walter Murch editing / blink / cut logic | Cutting logic and edit rhythm | No | ABSENT | No dedicated coverage | New editing canon supplement required | EXTERNAL_SOURCE_LEDGER_REQUIRED |
| Kuleshov effect and montage theory | Montage meaning construction | No | ABSENT | No dedicated coverage | New editing canon supplement required | EXTERNAL_SOURCE_LEDGER_REQUIRED |
| Eisenstein montage | Intellectual / metric / tonal montage | No | ABSENT | No dedicated coverage | New editing canon supplement required | EXTERNAL_SOURCE_LEDGER_REQUIRED |
| Bruce Block visual structure | Line, shape, color, depth, movement | No | ABSENT | No dedicated coverage | New visual structure supplement required | EXTERNAL_SOURCE_LEDGER_REQUIRED |
| cinematography grammar | Shot size, angle, lens, movement, depth | Yes | PARTIAL | Needs explicit shot / lens / movement law | Add to visual-language supplement | REPO_EVIDENCED |
| lighting grammar | High-key, low-key, motivated light, contrast | Yes | MENTION_ONLY | Needs dedicated lighting palette law | Add to style / palette supplement | REPO_EVIDENCED |
| color theory / palette / color script | Palette, emotional color logic | No | ABSENT | No dedicated palette system | New style / palette supplement required | EXTERNAL_SOURCE_LEDGER_REQUIRED |
| production design / mise-en-scène / props / costume / set logic | World texture and staging law | Yes | PARTIAL | Needs stronger production-design semantics | Add to production-design supplement | REPO_EVIDENCED |
| sound design | Motif, silence, diegetic / non-diegetic sound | Yes | PARTIAL | Needs sound-language and silence-law detail | Add to sound supplement | REPO_EVIDENCED |
| performance direction | Actor objective, beat, tactic, performance texture | Yes | PARTIAL | Needs explicit performance-beat law | Add to performance supplement | REPO_EVIDENCED |
| dialogue subtext and voice distinction | Subtext, voice, distinct dialogue | Yes | PARTIAL | Needs dialogue-specific validation | Add to dialogue supplement | REPO_EVIDENCED |
| genre grammar and audience contract | Genre promise, expectation management | No | ABSENT | No dedicated genre-law layer | New genre supplement required | EXTERNAL_SOURCE_LEDGER_REQUIRED |
| short film structure | Short-form film story design | Yes | USABLE | Needs validation and edge-case rules | Add to short-film supplement | REPO_EVIDENCED |
| feature film structure | Feature-length design and pacing | Yes | USABLE | Needs pacing / act / sequence detail | Add to feature-film supplement | REPO_EVIDENCED |
| documentary / docudrama ethics | Fact handling, dramatization ethics | No | ABSENT | No dedicated docudrama law | New ethics supplement required | EXTERNAL_SOURCE_LEDGER_REQUIRED |
| Disney 12 principles | Animation principles | Yes | MENTION_ONLY | Needs deeper animation canon | Add animation supplement | REPO_EVIDENCED |
| animation style families | 2D, 3D, anime, stop-motion, hybrid, motion graphics | Yes | PARTIAL | Needs motion-language and style-bible detail | Add animation supplement | REPO_EVIDENCED |
| AI-era visual generation continuity | Character consistency, style consistency, motion continuity | Yes | PARTIAL | Needs explicit continuity and source-vs-render rules | Add visual continuity supplement | REPO_EVIDENCED |

## Canon coverage summary

The audit finds:

- 7 areas at `USABLE` or near-usable level
- 12 areas that are still genuinely missing
- 11 areas that are present only at mention / partial depth and need deeper canon injection

That means the chain is directionally correct, but not canon-complete.

## Animation canon expansion

Animation is still under-covered in the audit chain.
The docs mention animation at a high level, but they do not yet deeply cover:

- squash and stretch
- anticipation
- staging
- pose-to-pose / straight-ahead
- follow-through and overlapping action
- slow in / slow out
- arcs
- secondary action
- timing
- exaggeration
- solid drawing
- appeal
- character rigging logic
- key poses / breakdowns / in-betweens
- acting for animation
- color script for animation
- animation style bible
- smear frames / stretch frames
- animation timing charts
- animation continuity validators

These are all still gap areas for Phase 12 planning.

## Style, palette, template, and design system gaps

The docs do not yet fully define:

- film style bible
- genre templates
- director style references
- visual DNA
- color palette law
- lighting palette
- lens palette
- aspect ratio rules
- camera movement vocabulary
- editing rhythm templates
- sound palette
- musical motif palette
- performance style guide
- production design palette
- costume palette
- location texture map
- prop motif system
- animation style bible
- AI image/video prompt style DNA
- negative prompt / anti-drift rules
- continuity rules across shots and scenes
- source-vs-render separation for real incidents

That is a second major canon gap after story structure.

## Recommended canon injection plan

| Target doc | Missing canon area | Proposed update | Priority | Requires external source ledger? | Notes |
|---|---|---|---|---|---|
| `PHASE_11_IMPLEMENTATION_PATCH_PLAN.md` | Filmcraft canon breadth | Add a minimum viable canon baseline section | High | Yes | The plan should name the canon families before Phase 12 |
| `PHASE_11_PATCH_UNIT_LEDGER.md` | Canon-to-patch mapping | Add a canon patch-unit mapping row set | High | Yes | This makes implementation sequencing concrete |
| `PHASE_11_ACCEPTANCE_ROLLBACK_PLAN.md` | Canon acceptance gates | Add explicit filmcraft coverage gates | High | Yes | The rollback plan needs deeper canon gates |
| `PHASE_1_FILM_ROUTE_PROPOSAL.md` | Film story structure depth | Add style / palette / format law | Medium | Yes | Keep the route proposal film-native |
| `PHASE_6_FILM_CONTRACT_FAMILY_PROPOSAL.md` | Filmcraft canon families | Add animation, palette, and editing canon families | High | Yes | Contract family should not stay only screenplay-centric |
| `PHASE_8_FILM_VALIDATOR_CANON_PROPOSAL.md` | Filmcraft validation breadth | Add animation / style / palette validators | High | Yes | Validators should cover visual and motion canon too |
| `PHASE_9_FILM_OUTPUT_SCHEMA_PROPOSAL.md` | Style and continuity schema depth | Add style bible / palette / animation continuity fields | High | Yes | The schema needs to express visual style law |

## Readiness judgment

The audit chain is good enough to explain the architecture.
It is **not** yet good enough to move to implementation because the canon and style system are still too shallow.

