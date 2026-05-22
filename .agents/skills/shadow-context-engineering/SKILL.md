# Shadow Context Engineering

Use this skill when:

- script is requested
- video/audio/image/music/media output is implied
- provider handoff is requested
- context packet is requested

## Required Context Engineering Output

For script/video/content tasks, output:

- voice direction
- emotion map
- visual beat map
- facial expression direction
- gesture/body movement direction
- image prompts
- video prompts
- music/SFX cues
- editing plan
- captions/on-screen text
- provider handoff boundary

Do not call media providers. Do not claim generated media. This skill creates context and handoff instructions only.

## Forbidden Behavior

- Do not stop at script-only output unless the user explicitly requests script-only.
- Do not claim voice/image/video/music artifacts were generated.
- Do not omit provider handoff boundary.

## Proof Implications

- `PASS`: all context engineering sections are present with provider boundary.
- `PARTIAL`: script exists but one or more context engineering sections are missing.
- `FAIL`: false media execution claims or provider execution without approval.
