# Film Route Platform Separation Law

## Objective

Preserve the existing content engine while preventing platform-first logic from controlling film-core screenplay generation.

## Core rule

```text
SCRIPT_GENERATION remains for content/platform scripts.
FILM_SCREENPLAY_GENERATION must be added in parallel.
Platform logic stays in content routes or downstream distribution.
Film-core route must not inherit hook/re-hook/retention cadence as core law.
```

## Term classification

| Term/finding | Allowed in content route? | Allowed in film core? | Allowed downstream? | Required action |
|---|---|---|---|---|
| YouTube | Yes | No | Yes | KEEP_DOWNSTREAM |
| Shorts | Yes | No | Yes | KEEP_DOWNSTREAM |
| Instagram | Yes | No | Yes | KEEP_DOWNSTREAM |
| TikTok | Yes | No | Yes | KEEP_DOWNSTREAM |
| reel | Yes | No | Yes | KEEP_DOWNSTREAM |
| social | Yes | No | Yes | KEEP_DOWNSTREAM |
| creator | Yes | No | Yes | KEEP_DOWNSTREAM |
| viral | Yes | No | Yes | KEEP_DOWNSTREAM |
| engagement | Yes | No | Yes | KEEP_DOWNSTREAM |
| retention | Yes | No | Yes | SPLIT_CONTENT_VS_FILM |
| hook | Yes | No | Yes | BLOCK_FROM_FILM_CORE |
| re-hook | Yes | No | Yes | BLOCK_FROM_FILM_CORE |
| recurring hook | Yes | No | Yes | BLOCK_FROM_FILM_CORE |
| open loop | Yes | No | Yes | BLOCK_FROM_FILM_CORE |
| cliffhanger | Yes | Limited | Yes | SPLIT_CONTENT_VS_FILM |
| thumbnail | Yes | No | Yes | MOVE_TO_DISTRIBUTION_LAYER |
| title pack | Yes | No | Yes | MOVE_TO_DISTRIBUTION_LAYER |
| SEO | Yes | No | Yes | MOVE_TO_DISTRIBUTION_LAYER |
| metadata | Yes | No | Yes | MOVE_TO_DISTRIBUTION_LAYER |
| platform analytics | Yes | No | Yes | MOVE_TO_DISTRIBUTION_LAYER |
| voiceover | Yes | Limited | Yes | SPLIT_CONTENT_VS_FILM |
| content engineering | Yes | No | Yes | KEEP_DOWNSTREAM |
| cinematic explainer | Yes | No, unless explicitly requested as film route | Yes | SPLIT_CONTENT_VS_FILM |
| trailer | Yes | No | Yes | MOVE_TO_DISTRIBUTION_LAYER |
| teaser | Yes | No | Yes | MOVE_TO_DISTRIBUTION_LAYER |
| promo cutdown | Yes | No | Yes | MOVE_TO_DISTRIBUTION_LAYER |
| release distribution | Yes | No | Yes | KEEP_DOWNSTREAM |

## Anti-collision examples

- "short film on NEET" -> film route
- "5-minute short film" -> film route
- "YouTube video script on NEET" -> content route
- "cinematic explainer for YouTube" -> content route with cinematic style unless the user explicitly asks for screenplay
- "trailer for NEET film" -> downstream release/adaptation route
- "thumbnail/title for film" -> downstream packaging route

## Prohibited film-core leakage

The following content-mode requirements must not become film-core PASS requirements:

- hook density
- re-hook cadence
- retention loop score
- thumbnail promise
- SEO title score
- viral potential
- platform fit
- creator fit
- Shorts/Reels pacing

## Why the split matters

The content engine remains valid and useful.
The film route simply must not inherit creator-growth law as if it were screenplay law.

