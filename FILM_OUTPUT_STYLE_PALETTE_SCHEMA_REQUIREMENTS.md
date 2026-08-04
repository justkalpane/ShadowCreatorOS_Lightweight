# Film Output Style Palette Schema Requirements

## Objective

The future film output packet needs structured style and palette fields.
This document turns style law into schema requirements.

## Required future schema families

```text
schemas/film/style/film_style_bible.schema.json
schemas/film/style/film_visual_dna.schema.json
schemas/film/style/film_color_palette.schema.json
schemas/film/style/film_lighting_palette.schema.json
schemas/film/style/film_lens_palette.schema.json
schemas/film/style/film_camera_movement_vocabulary.schema.json
schemas/film/style/film_production_design_palette.schema.json
schemas/film/style/film_costume_palette.schema.json
schemas/film/style/film_sound_palette.schema.json
schemas/film/style/film_music_motif_palette.schema.json
schemas/film/style/film_animation_style_bible.schema.json
schemas/film/style/film_ai_prompt_style_dna.schema.json
schemas/film/style/film_continuity_anti_drift.schema.json
```

## Required future packet fields

| Field | Type | Required? | Applies to live action? | Applies to animation? | Validator needed? | Notes |
|---|---|---|---|---|---|---|
| style_bible | object | Yes | Yes | Yes | Yes | Master style authority |
| genre_template | string/object | Yes | Yes | Yes | Yes | Controls genre-specific style |
| visual_dna | object | Yes | Yes | Yes | Yes | Visual identity core |
| aspect_ratio | string | Yes | Yes | Yes | Yes | Framing rule |
| lens_palette | object | Yes | Yes | Yes | Yes | Camera grammar |
| lighting_palette | object | Yes | Yes | Yes | Yes | Light and contrast law |
| color_palette | object | Yes | Yes | Yes | Yes | Color identity |
| color_script | object | Optional/Recommended | Yes | Yes | Yes | Scene-based palette progression |
| production_design_palette | object | Yes | Yes | Yes | Yes | Set/prop/costume coherence |
| costume_palette | object | Recommended | Yes | Yes | Yes | Character visual continuity |
| prop_motif_system | object | Recommended | Yes | Yes | Yes | Symbolic props |
| location_texture_map | object | Recommended | Yes | Yes | Yes | World texture |
| camera_movement_vocabulary | object | Yes | Yes | Yes | Yes | Motion grammar |
| editing_rhythm_template | object | Recommended | Yes | Yes | Yes | Cut rhythm |
| sound_palette | object | Yes | Yes | Yes | Yes | Audio identity |
| music_motif_palette | object | Recommended | Yes | Yes | Yes | Musical recurrence |
| performance_style_guide | object | Yes | Yes | Yes | Yes | Acting direction |
| animation_style_bible | object | Optional/Required for animation | No | Yes | Yes | Animation mode only |
| ai_prompt_style_dna | object | Yes | Yes | Yes | Yes | Prompt language law |
| negative_prompt_rules | object | Yes | Yes | Yes | Yes | Anti-drift restrictions |
| continuity_anti_drift_rules | object | Yes | Yes | Yes | Yes | Prevents shot-scene inconsistency |

## Why these fields matter

The style system is what stops the film route from becoming a generic "cinematic" packet with no usable visual law.
These fields make the output structured enough for validators, downstream media planning, and future route separation.

