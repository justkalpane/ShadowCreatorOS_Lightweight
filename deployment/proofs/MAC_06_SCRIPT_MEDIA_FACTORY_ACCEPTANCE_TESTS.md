# MAC-06 Script Media Factory Acceptance Tests

## Purpose

These tests prove that script production cannot pass by filling headings while
language, research, timing, and media synchronization remain shallow.

## T-LANG-001

Prompt: Write a 5-minute YouTube script about Yash and self-investment.

Expected:

- English master script
- explicit language-request check
- translation treated as a downstream stage

Fail:

- Hindi or Hinglish master script without an explicit request

## T-RESEARCH-001

Prompt: Write a script using a real public figure as proof.

Expected:

- web-assisted research
- source ledger
- source limitation notes
- fact-versus-anecdote map
- three sources, two non-encyclopedia sources, and three source categories
  where suitable sources are available

Fail:

- false real-time claim
- single encyclopedia authority
- anecdote treated as verified fact

## T-STORY-001

Prompt: Write a 5-minute self-investment script.

Expected:

- 45-75 second cinematic story
- character, setting, conflict, stakes, turning point, emotional peak, lesson
  bridge, and topic connection
- honest story basis and reconstruction disclosure

Fail:

- generic motivation filler
- invented exact scene passed off as verified fact

## T-BEAT-001

Prompt: Create the timed beat map for a 5-minute script.

Expected:

- dynamic 3-20 second blocks
- duration reason per block
- production dependency fields

Fail:

- unexplained uniform 15-second grid

## T-MEDIA-001

Prompt: Generate the final Media Factory draft.

Expected:

- scene sync matrix
- script, voice, image, video, music/SFX, editing, platform, influence, and
  execution fields aligned per scene

Fail:

- independent shallow context sections

## T-HYBRID-001

Prompt: Generate media handoff for local/cloud/hybrid factory.

Expected:

- execution plan per asset type
- preferred path, fallback, dependency risk, and provider boundary

Fail:

- single-provider assumption or missing fallback

## T-INFLUENCE-001

Prompt: Generate a line-by-line influence map.

Expected:

- why each line exists
- emotion triggered
- retention function
- story/proof role
- topic support
- media dependency

Fail:

- repo lineage only

## T-PROPAGATION-001

Purpose: Prove the laws are not limited to contracts or startup documents.

Expected:

- propagation gate scans active directors, agents, subagents, script skills,
  hook/retention subskills, and executable script nodes
- every relevant actor is patched or explicitly marked not applicable with a
  reason
- validator rejects a missing propagation marker

Fail:

- laws exist only in `runtime_contracts/`
- laws exist only in `AGENTS.md` or `START_HERE_FOR_AGENTS.md`
- laws exist only in the three high-level `.agents` skills
- a selected hook, retention, pacing, or cliffhanger owner lacks propagation

## T-HOOK-DENSITY-002

Prompt: Write a 5-minute YouTube script about Yash and self-investment.

Expected:

- three opening hook variants and one selected opening hook
- at least three internal recurring re-hooks plus a CTA hook
- dynamic 70-90 second default interval with a topic-specific reason
- maximum unexplained gap without a re-hook of 90 seconds
- every re-hook appears in final script, dynamic beat map, editing context,
  and line-by-line influence map
- factual proof re-hooks appear in `FACT_VS_ANECDOTE_MAP`

Fail:

- only one selected opening hook
- re-hooks listed separately but absent from the script
- re-hooks absent from timed beats or creative influence map
- generic motivational filler used as a retention reset

## T-MEDIA-REHOOK-SYNC-001

Prompt: Generate the final Media Factory draft for a 5-minute YouTube script.

Expected:

- every re-hook appears in `SCENE_SYNC_MATRIX`
- re-hook rows contain voice tension, visual pattern interrupt, music/SFX
  accent, editing cue, platform safe-zone cue, and local/cloud/hybrid
  execution path

Fail:

- re-hooks exist only in script text
- scene sync matrix omits re-hook markers or retention-reset goals

## MAC-06.2P1 Validator Reality Negative Fixtures

- `NEG-LANG-001`: Hindi/Hinglish body declared as English must fail.
- `NEG-REHOOK-001`: `RECURRING_REHOOK_MAP` heading without rows must fail.
- `NEG-REHOOK-002`: Re-hook rows absent from final script must fail.
- `NEG-REHOOK-003`: Calculated re-hook gap above 90 seconds without reason must fail.
- `NEG-SOURCE-001`: `SOURCE_LEDGER` heading without rows must fail.
- `NEG-SOURCE-002`: URLs outside `SOURCE_LEDGER` must not satisfy source count.
- `NEG-FACT-001`: `FACT_VS_ANECDOTE_MAP` heading without rows must fail.
- `NEG-FACT-002`: Anecdotal support treated as verified fact must fail.
- `NEG-SCENE-001`: `SCENE_SYNC_MATRIX` heading without rows must fail.
- `NEG-SCENE-002`: Scene row missing nested production context must fail.
- `NEG-STATUS-001`: `final_status=PASS` while a mandatory gate is partial must fail.
- `NEG-PROP-001`: Marker-only runtime actor propagation must fail.
- `NEG-DAG-001`: `M-039` must execute before `S-202` through `rehook_plan_packet`.

## Local Proof Command

```bash
python3 validators/validate_script_generation_output.py --self-test
```
