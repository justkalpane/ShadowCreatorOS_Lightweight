# Filmcraft Canon Source Ledger

## Objective

This ledger establishes a source-backed filmcraft canon candidate list before implementation.
It is intentionally conservative: it defines the canon candidates, their relevance to the film route, and what kind of runtime layer should eventually consume them.

## Canon source table

| Canon ID | Book/System/Technique | Author/Origin | Area | Why it matters for film route | Required runtime use | Source status | Repo evidence | External/source notes | Priority |
|---|---|---|---|---|---|---|---|---|---|
| FC-01 | `Poetics` | Aristotle | Dramatic structure | Foundation for reversal, recognition, unity, and catharsis | Route + contract + validator | EXTERNAL_SOURCE_LEDGER_REQUIRED | Not yet directly cited in Phase docs | Needs owner or external canon ledger | High |
| FC-02 | `The Art of Dramatic Writing` | Lajos Egri | Premise / character-driven drama | Premise and character conflict are core screenplay drivers | Contract + schema + validator | REPO_EVIDENCED | Mentioned in Phase 11R canon report | Add explicit premise/character rules later | High |
| FC-03 | `Screenplay` / three-act paradigm | Syd Field | Three-act structure / plot points | Useful structural baseline for film pacing and turning points | Contract + validator + fixture | REPO_EVIDENCED | Mentioned in Phase 6/8/9 docs | Needs film-specific runtime support | High |
| FC-04 | `Story` / scene value turns | Robert McKee | Scene dramaturgy | Scene values, turns, and conflict are central to film craft | Contract + validator | REPO_EVIDENCED | Mentioned in Phase 6/8/9 docs | Needs scene-turn packet fields | High |
| FC-05 | `The Anatomy of Story` | John Truby | 22-step story system | Deeper story-world and moral-argument support | Contract + schema + validator | REPO_EVIDENCED | Mentioned in Phase 8/9 docs | Good candidate for high-depth story layer | High |
| FC-06 | `Save the Cat` | Blake Snyder | Beat sheet | Familiar beat-sheet scaffold for some film routes | Contract + validator + fixture | REPO_EVIDENCED | Mentioned in Phase 1/6/8/9/10 docs | Optional canon, not the only canon | High |
| FC-07 | `The Hero with a Thousand Faces` | Joseph Campbell | Monomyth | Useful mythic journey reference for certain stories | Contract + validator | REPO_EVIDENCED | Mentioned in Phase 8/11R docs | Optional, not mandatory for all films | Medium |
| FC-08 | `The Writer’s Journey` | Christopher Vogler | Mythic screenplay adaptation | Practical bridge from myth to screenplay craft | Contract + validator | REPO_EVIDENCED | Mentioned in Phase 11R docs | Optional canon candidate | Medium |
| FC-09 | Dramatic action / scene objective logic | David Mamet | Scene objective | Keeps scenes action-driven, not explanatory | Contract + validator | EXTERNAL_SOURCE_LEDGER_REQUIRED | Not directly cited in phase docs | Strong supplement candidate | Medium |
| FC-10 | Rewriting / script consulting principles | Linda Seger | Story repair | Useful for rewrite diagnostics and repair loops | Contract + validator | EXTERNAL_SOURCE_LEDGER_REQUIRED | Not directly cited in phase docs | Good second-wave canon item | Medium |
| FC-11 | Hollywood story practice / screenplay craft | William Goldman | Screenplay craft | Practical story and screenplay instincts | Contract + validator | EXTERNAL_SOURCE_LEDGER_REQUIRED | Not directly cited in phase docs | Classic craft reference | Medium |
| FC-12 | Editing logic / cut rhythm | Walter Murch | Editing | Important for cut logic, blink logic, and edit rhythm | Contract + validator + downstream handoff | EXTERNAL_SOURCE_LEDGER_REQUIRED | Not directly cited in phase docs | More relevant downstream but still core canon | Medium |
| FC-13 | Montage theory | Sergei Eisenstein | Editing / montage | Helps define cinematic meaning through cut relationships | Contract + validator | EXTERNAL_SOURCE_LEDGER_REQUIRED | Not directly cited in phase docs | Important if film route expands into montage-heavy work | Medium |
| FC-14 | Kuleshov effect | Kuleshov | Editing / inference | Essential for visual inference and meaning construction | Contract + validator | EXTERNAL_SOURCE_LEDGER_REQUIRED | Not directly cited in phase docs | Strong film literacy item | Medium |
| FC-15 | Visual structure | Bruce Block | Cinematic design | Helps formalize visual hierarchy and visual storytelling | Contract + schema + validator | EXTERNAL_SOURCE_LEDGER_REQUIRED | Not directly cited in phase docs | Strong style/system addition | Medium |
| FC-16 | Shot design / visualizing from script | Steven D. Katz | Shot planning | Useful for translating screenplay to visual language | Schema + validator + downstream handoff | EXTERNAL_SOURCE_LEDGER_REQUIRED | Not directly cited in phase docs | Good production bridge canon | Medium |
| FC-17 | Cinematography grammar | Blain Brown | Camera / lens / light | Supports practical visual language and camera grammar | Schema + contract + validator | EXTERNAL_SOURCE_LEDGER_REQUIRED | Not directly cited in phase docs | Needed for style bible and output schema | High |
| FC-18 | Film form / film art analysis | David Bordwell and Kristin Thompson | Film form | Strong analytical vocabulary for structure and style | Contract + schema | EXTERNAL_SOURCE_LEDGER_REQUIRED | Not directly cited in phase docs | Useful as scholarly support canon | Medium |
| FC-19 | `The Illusion of Life` / Disney 12 principles | Frank Thomas and Ollie Johnston | Animation canon | Required if animation becomes a first-class film mode | Contract + schema + validator | MENTIONED_NO_SOURCE | Animation principles are referenced in Phase 11R gap report | Authors not yet source-led in the repo chain | High |
| FC-20 | Animation craft / timing / movement logic | Richard Williams | Animation | Important for animation motion, timing, and movement craft | Contract + schema + validator | EXTERNAL_SOURCE_LEDGER_REQUIRED | Not directly cited in phase docs | High-value animation canon | High |

## Runtime mapping

| Canon ID | Contract needed | Schema needed | Validator needed | Fixture needed | Skill/subskill needed | Downstream use |
|---|---|---|---|---|---|---|
| FC-01 | film route intent / film structure | film screenplay output packet | film structure / philosophy validator | film structure fixture | story architecture, scene craft | None directly |
| FC-02 | character/premise contract | character arc + premise map | premise and character validator | character arc fixture | premise engine, character engine | None directly |
| FC-03 | three-act / eight-sequence contract | three-act map | three-act validator | structure fixture | screenplay structure skill | None directly |
| FC-04 | scene dramaturgy contract | scene turn map | scene-turn validator | scene conflict fixture | scene dramaturgy skill | None directly |
| FC-05 | story-system contract | story map | story-system validator | story-map fixture | story architecture skill | None directly |
| FC-06 | beat-sheet contract | beat-sheet schema | beat-sheet validator | beat-sheet fixture | beat-mapping skill | Optional downstream adaptation |
| FC-07 | mythic-journey contract | hero-journey schema | optional hero-journey validator | mythic-journey fixture | mythic structure support | Optional |
| FC-08 | mythic-adaptation contract | story-circle schema | story-circle validator | story-circle fixture | mythic adaptation support | Optional |
| FC-09 | scene objective contract | scene objective schema | scene objective validator | scene objective fixture | scene objective skill | None directly |
| FC-10 | rewrite/repair contract | rewrite diagnostics schema | rewrite validator | rewrite-failure fixture | rewrite support skill | Repair loops |
| FC-11 | screenplay craft contract | screenplay packet schema | screenplay craft validator | craft benchmark fixture | screenplay craft skill | None directly |
| FC-12 | edit rhythm contract | edit rhythm schema | cut-rhythm validator | edit rhythm fixture | editing support skill | Downstream editing handoff |
| FC-13 | montage contract | montage schema | montage validator | montage fixture | editing / montage support | Downstream editing handoff |
| FC-14 | inference contract | inference schema | inference validator | inference fixture | editing support skill | Downstream editing handoff |
| FC-15 | visual structure contract | visual structure schema | visual structure validator | visual structure fixture | visual language skill | Downstream visual handoff |
| FC-16 | shot design contract | shot design schema | shot design validator | shot design fixture | shot-planning skill | Downstream shot handoff |
| FC-17 | camera/lens/light contract | camera grammar schema | camera grammar validator | camera grammar fixture | cinematography skill | Downstream production handoff |
| FC-18 | film form contract | film-form schema | film-form validator | film-form fixture | film analysis skill | Research and critique support |
| FC-19 | animation contract | animation style bible schema | animation validator | animation fixture | animation motion skill | Animation downstream handoff |
| FC-20 | animation motion contract | animation motion schema | animation motion validator | animation motion fixture | animation timing skill | Animation downstream handoff |

## Non-goals

This ledger does not enforce all canon systems at once.
It defines candidates, priorities, and the likely runtime layer each canon belongs to.

