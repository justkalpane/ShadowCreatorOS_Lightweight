# Cinema Style Bible Requirements

## Objective

The film route needs style law, not generic "cinematic" adjectives.
The style bible is the place where visual, tonal, and motion rules become explicit enough to guide prompts, schemas, and validators.

## Required style bible sections

| Style Section | Required fields | Why it matters | Schema implication | Validator implication | Prompt/output implication |
|---|---|---|---|---|---|
| Genre contract | genre, subgenre, audience promise | Keeps the story promise coherent | genre template field | genre-consistency check | Genre-aware writing style |
| Tone contract | tone, emotional temperature, seriousness, pace | Prevents tonal drift | tone field | tone consistency validator | Tone must remain stable |
| Visual DNA | visual motifs, visual grammar, image logic | Gives the film a recognizable visual identity | visual DNA field | visual drift validator | Style prompts become specific |
| Director style references | named references, stylistic rules | Makes direction reproducible | style reference field | reference consistency check | Style-following prompts |
| Aspect ratio | 16:9, 2.39:1, 4:3, etc. | Framing and composition depend on it | aspect ratio field | aspect-ratio sanity check | Frame layout constraints |
| Lens palette | focal length ranges, lens character, depth feel | Prevents random lens language | lens palette field | lens consistency check | Camera prompt specificity |
| Camera movement vocabulary | static, dolly, handheld, crane, locked, etc. | Controls visual motion grammar | camera movement field | movement drift validator | Shot design language |
| Shot-size grammar | ECU, CU, MCU, MS, WS, etc. | Creates readable shot planning | shot-size field | shot-size coverage check | Shot-level prompts |
| Lighting palette | high-key, low-key, motivated, contrast, color temp | Sets visual mood | lighting palette field | lighting consistency check | Lighting-aware prompts |
| Color palette | dominant colors, contrast, saturation | Prevents palette drift | color palette field | palette drift validator | Color-coded style DNA |
| Color script | scene-by-scene color progression | Supports emotional arc | color script field | color-script coherence check | Scene-aware palette planning |
| Location texture map | architecture, surface, weather, density | Grounds the world | location texture field | location continuity check | World-building detail |
| Production design palette | props, set dressing, materials | Makes the world feel authored | production design field | design consistency check | Set/prop planning prompts |
| Prop motif system | repeated props, symbolic objects | Supports visual storytelling | prop motif field | motif recurrence validator | Visual motif planning |
| Costume palette | wardrobe colors, silhouettes, era markers | Keeps character visual identity coherent | costume palette field | costume continuity check | Wardrobe prompts |
| Makeup/hair style | grooming, transformation, era, texture | Supports continuity and character | makeup/hair field | appearance continuity check | Character prompt clarity |
| Performance style | restraint, theatricality, realism, animation acting | Shapes acting direction | performance style field | performance-style check | Actor-direction prompts |
| Editing rhythm | cuts, pace, transition texture | Links style to pacing | edit rhythm field | rhythm consistency check | Edit-aware output notes |
| Sound palette | ambience, texture, silence, sound effects | Audio identity is part of style | sound palette field | sound continuity check | Audio direction prompts |
| Music/motif palette | thematic motifs, instrumentation, recurring cues | Emotional continuity | music motif field | motif recurrence check | Scoring guidance |
| Title/graphic language | typography, opening titles, lower-thirds | Visual branding and readability | graphic language field | graphic consistency check | Title-card prompts |
| Source-vs-render separation | real-source visuals vs dramatized render | Prevents evidence confusion | source/render flag | evidence-misuse check | Real-incident integrity |
| AI prompt style DNA | prompt phrasing, anti-drift terms, positive style anchors | Keeps generation stable | prompt DNA field | anti-drift validator | Prompt language law |
| Negative prompt / anti-drift rules | forbidden styles, forbidden artifacts, no unwanted genres | Stops style corruption | negative prompt field | style-drift validator | Output constraints |
| Continuity rules across scenes/shots | wardrobe, props, locations, motion, continuity | Prevents inconsistent output | continuity field | continuity validator | Scene-to-scene consistency |

## Genre template system

The style bible should include reusable templates for:

- drama
- thriller
- social realism
- docudrama
- satire
- mythological parallel
- coming-of-age
- courtroom / investigation
- political drama
- sci-fi
- fantasy
- horror
- action
- romance
- animation short
- children/family animation

## Style anti-drift rules

The style bible must explicitly prevent:

- generic cinematic wording with no usable detail
- random lens changes without narrative reason
- random palette changes without story reason
- inconsistent character appearance
- inconsistent locations and set dressing
- factual-real-world visuals pretending to be archival evidence
- platform thumbnail style leaking into film-core frames
- hook/re-hook style language being treated as film style law

## Purpose of the bible

This document is the bridge between the film route, the style schema, the visual output, and the future validators.
Without it, the cinema route would remain "cinematic" in name only.

