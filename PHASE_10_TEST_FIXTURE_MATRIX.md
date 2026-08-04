# Phase 10 Test Fixture Matrix

| Fixture ID | Input prompt / packet | Expected route/result | Should PASS later? | Should FAIL later? | Required validator/schema | Purpose | Risk if missing |
|---|---|---|---|---|---|---|---|
| RS-001 | short film on NEET paper issue | `FILM_SCREENPLAY_GENERATION` | yes | no | film route selection validator, film screenplay packet schema | Canonical film intent | Film prompts drift into content route |
| RS-002 | 5-minute short film on NEET issue | `FILM_SCREENPLAY_GENERATION` | yes | no | film route selection validator, film screenplay packet schema | Film duration plus film intent | Duration requests fall back to YouTube-style script mode |
| RS-003 | screenplay about a student after exam leak allegations | `FILM_SCREENPLAY_GENERATION` | yes | no | film route selection validator, film beat-sheet schema | Screenplay-language film request | Screenplay requests get flattened into content scripts |
| RS-004 | YouTube video script about NEET issue | `SCRIPT_GENERATION` | yes | no | content script route validator, content script packet schema | Preserve content route | YouTube requests get misrouted to film core |
| RS-005 | Instagram reel script about NEET issue | `SCRIPT_GENERATION` or social/content route | yes | no | content/social route validator, content script packet schema | Preserve social route | Social intent gets overpromoted into film mode |
| RS-006 | voiceover script about NEET issue | `SCRIPT_GENERATION` | yes | no | content script route validator, voice context schema | Preserve voiceover content routing | Voiceover requests lose content-route behavior |
| RS-007 | trailer for the NEET short film | downstream film release/adaptation route | yes | no | downstream handoff validator, trailer/adaptation schema | Preserve trailer adaptation | Trailer requests are forced back into screenplay mode |
| RS-008 | thumbnail and title for the NEET film | downstream packaging route | yes | no | packaging validator, platform package schema | Preserve packaging behavior | Packaging gets treated like core screenplay work |
| RS-009 | full video pipeline for a film screenplay | downstream production pipeline after film packet | yes | no | full pipeline validator, downstream handoff schema | Preserve downstream production flow | Full pipeline is disconnected from film packet output |
| RS-010 | make a cinematic explainer for YouTube | `SCRIPT_GENERATION` (cinematic-style content route) | yes | no | content route validator, script quality schema | Preserve content route with cinematic style | Ambiguous prompts skip route clarification |
| FP-001 | valid film screenplay packet with logline, theme, beat sheet, character arc, scene turns, dialogue subtext, visual motif, and screenplay body | `FILM_SCREENPLAY_GENERATION` | yes | no | film screenplay packet schema, film validation scorecard | Positive film packet baseline | No canonical pass case for film route |
| FP-002 | film packet missing beat sheet | `FILM_SCREENPLAY_GENERATION` | no | yes | film beat-sheet schema, film scorecard | Mandatory structure failure | Beat-sheet gaps slip through as valid screenplay packets |
| FP-003 | film packet missing character arc | `FILM_SCREENPLAY_GENERATION` | no | yes | film character arc schema | Character transformation failure | Flat characters can still pass film validation |
| FP-004 | film packet missing scene objective / conflict / turn map | `FILM_SCREENPLAY_GENERATION` | no | yes | film scene dramaturgy schema | Scene craft failure | Scene structure collapses without detection |
| FP-005 | film packet missing dialogue subtext pass | `FILM_SCREENPLAY_GENERATION` | no | yes | film dialogue schema | Dialogue craft failure | Literal dialogue can masquerade as cinematic writing |
| FP-006 | film packet missing visual motif system | `FILM_SCREENPLAY_GENERATION` | no | yes | film visual motif schema | Visual storytelling failure | Visual symbolism gaps go unvalidated |
| FP-007 | film packet missing camera / composition language | `FILM_SCREENPLAY_GENERATION` | no | yes | film camera/composition schema | Directorial craft failure | Flat staging gets treated as film-ready |
| FP-008 | film packet missing film validation scorecard | `FILM_SCREENPLAY_GENERATION` | no | yes | film validation scorecard schema | Scorecard completeness failure | Film route can fake a final verdict |
| FP-009 | content-mode script packet pretending to be film packet | `FILM_SCREENPLAY_GENERATION` rejected | no | yes | film-vs-content collision validator | Collision failure | Content scripts impersonate film packets |
| FP-010 | film packet using only hook / re-hook / retention metrics | `FILM_SCREENPLAY_GENERATION` rejected | no | yes | film validation scorecard, film screenplay schema | Content-only metric failure | Content metrics are mistaken for filmcraft |
| CP-001 | YouTube explainer still routes to content script mode | `SCRIPT_GENERATION` | yes | no | content script route validator, script quality schema | Preserve YouTube behavior | Content route gets hijacked by film defaults |
| CP-002 | Shorts script still routes to content/social route | `SCRIPT_GENERATION` or social route | yes | no | content/social route validator, platform packet schema | Preserve Shorts behavior | Shorts lose their short-form routing |
| CP-003 | Reel script still routes to content/social route | `SCRIPT_GENERATION` or social route | yes | no | content/social route validator, platform packet schema | Preserve reel behavior | Reels get incorrectly treated as screenplay output |
| CP-004 | Voiceover script still routes to content route | `SCRIPT_GENERATION` | yes | no | content route validator, voice context schema | Preserve voiceover mode | Voiceover requests lose existing content flow |
| CP-005 | Existing content packet still validates under content validators | `SCRIPT_GENERATION` | yes | no | content validators, quality scorecard schema | Preserve legacy content support | Existing content workflows break during film split |
| CP-006 | Content route does not require Save the Cat / character arc / screenplay format unless explicitly cinematic | `SCRIPT_GENERATION` | yes | no | content route validator, content packet schema | Preserve content-mode scope boundary | Content route inherits film-only requirements by accident |
| DH-001 | film screenplay packet -> visual media plan handoff | downstream visual media plan route | yes | no | visual media plan schema, media handoff validator | Film-to-visual downstream bridge | Film route cannot feed visual planning |
| DH-002 | film screenplay packet -> voice context handoff | downstream voice context route | yes | no | voice context schema, voice handoff validator | Film-to-voice downstream bridge | Film route cannot feed narration/voice context |
| DH-003 | film screenplay packet -> editing packaging handoff | downstream editing route | yes | no | editing packet schema, editing handoff validator | Film-to-editing downstream bridge | Film route cannot feed edit planning |
| DH-004 | film screenplay packet -> media factory handoff | downstream media factory route | yes | no | media factory handoff schema, route-state capsule schema | Film-to-media-factory bridge | Film route cannot enter production handoff cleanly |
| DH-005 | film screenplay packet -> full video pipeline handoff | downstream video pipeline route | yes | no | full pipeline schema, downstream validator | Film-to-full-pipeline bridge | Film output cannot reach broader downstream flow |
| DH-006 | trailer request after film packet | film release/adaptation route | yes | no | trailer/adaptation schema, release validator | Preserve post-film adaptation | Trailer requests get trapped in screenplay mode |
| DH-007 | social cutdown after film packet | downstream platform adaptation route | yes | no | platform package schema, social adaptation validator | Preserve platform repurposing | Social repurposing is lost after film creation |
| NF-001 | film route output cannot pass without film schema | film route rejected | no | yes | film screenplay packet schema, no-fake-PASS validator | Schema gate enforcement | Film packets can pass without film structure |
| NF-002 | film route output cannot pass with content validator only | film route rejected | no | yes | film validator family, collision validator | Validator separation enforcement | Content validators falsely approve film output |
| NF-003 | film route output cannot pass without source ledger when real-world/current topic | film route rejected | no | yes | film source ledger schema, source validation | Source honesty enforcement | Real-world film claims go unverified |
| NF-004 | film route output cannot pass without lineage / consumption ledger | film route rejected | no | yes | lineage schema, route consumption ledger | Proof trace enforcement | Film output lacks auditable lineage |
| NF-005 | film route output cannot pass without filmcraft validation scorecard | film route rejected | no | yes | film validation scorecard schema | Film verdict enforcement | Film output can claim PASS without canon checks |
| NF-006 | runtime artifact names cannot be invented in fixture expected output | fixture rejected | no | yes | fixture parser, governance proof schema | Honest fixture language | Fake artifacts sneak into expected results |
| NF-007 | GitHub direct-read cannot be treated as governed runtime proof | fixture rejected | no | yes | repo-read proof marker, governed runtime proof validator | Boundary enforcement | Repo inspection is mistaken for runtime execution |

## Fixture family counts

* Route selection: 10
* Film packet validation: 10
* Content preservation: 6
* Downstream handoff: 7
* No-fake-PASS: 7

Total proposed fixture cases: 40

## Fixture design rule

The fixture layer should encode the difference between:

* a real film screenplay packet
* a content script packet
* a downstream trailer / teaser / platform package
* a governance proof packet

That distinction is the whole point of Phase 10.

## Non-goals

This phase does not create executable tests yet. It only defines the future fixture matrix and the boundary between film, content, downstream, and governance proof cases.
