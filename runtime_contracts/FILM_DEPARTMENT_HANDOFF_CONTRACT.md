# Film Department Handoff Contract

Phase: PHASE_13D_F7

The film preproduction packet must expose department handoff packets for story,
writing, character, direction, cinematography, art, costume, sound, continuity,
production management, validation/audit, and packaging/distribution.

This contract is script-only. It does not trigger downstream media generation,
provider calls, publishing, avatar rendering, or platform packaging execution.

Every department handoff must include:

- department
- required_inputs
- required_outputs
- validation_need
- route_boundary

`FILM_SCREENPLAY_GENERATION` owns cinema craft planning. `MEDIA_FACTORY_HANDOFF`
remains downstream execution only.
