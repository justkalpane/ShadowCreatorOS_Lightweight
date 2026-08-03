# Clean Film vs Script Route Boundary Contract

Phase: PHASE_13D_F7

`SCRIPT_GENERATION` is the YouTube/content/script/retention/platform packaging
route. It owns hooks, recurring re-hooks, thumbnails, retention loops, CTAs,
creator packaging, and platform-specific content optimization.

`FILM_SCREENPLAY_GENERATION` is the cinema preproduction, screenplay, story,
character, world, visual language, director vision, and craft route. It may
produce script-only cinema artifacts, but it must not import YouTube hook,
thumbnail, retention, shorts, reels, TikTok, or platform packaging logic as
film-core authority.

`MEDIA_FACTORY_HANDOFF` is the downstream visual/audio/avatar/media execution
route. It is not triggered by film preproduction proof runs unless explicitly
authorized by a later downstream phase.

Required preservation:

- `default_mode` remains `script_only`.
- `SCRIPT_GENERATION` remains preserved.
- film-core proof must not call paid APIs.
- film-core proof must not trigger media generation.
- runtime PASS must come only from artifact-bound validators.
