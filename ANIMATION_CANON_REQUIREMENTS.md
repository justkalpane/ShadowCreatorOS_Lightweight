# Animation Canon Requirements

## Objective

Animation film mode must support animation-specific principles, styles, and validation.
Animation is not a side note; it is a first-class cinema mode with its own motion grammar.

## Disney 12 principles coverage

| Principle | Required interpretation | Schema field? | Validator needed? | Prompt/style implication | Fixture needed? |
|---|---|---|---|---|---|
| Squash and stretch | Flexibility, weight, elasticity | Yes | Yes | Motion should feel alive | Yes |
| Anticipation | Preparation before action | Yes | Yes | Build readable motion cues | Yes |
| Staging | Clear presentation of the idea | Yes | Yes | Keep the shot readable | Yes |
| Straight ahead and pose-to-pose | Two animation planning methods | Yes | Yes | Choose motion method explicitly | Yes |
| Follow-through and overlapping action | Delayed motion after main action | Yes | Yes | Keep motion believable | Yes |
| Slow in and slow out | Natural acceleration curves | Yes | Yes | Smooth motion timing | Yes |
| Arcs | Natural motion paths | Yes | Yes | Avoid robotic movement | Yes |
| Secondary action | Supporting motion | Yes | Yes | Add life without confusion | Yes |
| Timing | Frame count and rhythm | Yes | Yes | Pace motion intentionally | Yes |
| Exaggeration | Emotional emphasis | Yes | Yes | Intensify key beats without breaking style | Yes |
| Solid drawing | Structure and form | Yes | Yes | Preserve form and volume | Yes |
| Appeal | Readability and charm | Yes | Yes | Make designs compelling | Yes |

## Animation style families

The film route should support at least these styles:

- 2D hand-drawn
- 3D CGI
- stop-motion
- claymation
- anime
- cutout animation
- motion graphics
- stylized toon
- realistic animation
- hybrid live action + animation
- rotoscope
- puppet animation
- children/family animation
- adult animation
- educational explainer animation
- mythological animation
- graphic novel / comic animation

## Animation production fields

Required future packet fields:

- animation style bible
- character design sheet
- turnaround sheet
- expression sheet
- key poses
- extremes
- breakdowns
- in-betweens
- timing chart
- motion arcs
- smear/stretch frame notes
- rigging assumptions
- layout/background style
- color script
- animation acting notes
- continuity notes
- frame economy notes

## Animation validators

Recommended future validators:

- `validate_animation_style_bible.py`
- `validate_disney_12_principles_map.py`
- `validate_character_design_consistency.py`
- `validate_key_pose_timing_chart.py`
- `validate_animation_motion_continuity.py`
- `validate_animation_color_script.py`
- `validate_animation_prompt_anti_drift.py`

## Why this matters

If animation is not modeled explicitly, the cinema route will accidentally default to live-action assumptions.
That would leave a major gap for shorts, motion graphics, anime, and stylized animated storytelling.

