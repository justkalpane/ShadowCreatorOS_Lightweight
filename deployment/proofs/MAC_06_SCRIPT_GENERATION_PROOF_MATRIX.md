# MAC-06 Script Generation Proof Matrix

## Purpose

Prove that the script-generation route cannot inflate `PASS` while skipping
source-backed real-world research, the cinematic story engine, or the content
engineering handoff.

## T-SCRIPT-01 - Real-Person Motivational Script

Prompt:

```text
Write a 5-minute YouTube script on "Stop scrolling and invest in yourself"
using Rocking Star Yash as the real-world example.
```

Expected:

- repo-first script route
- `web_required=true`
- web-assisted research when web access is available
- source list with URL, title, date, and access status
- Yash claim-evidence status
- 45-75 second `CINEMATIC_SHORT_STORY_BLOCK`
- character, setting, conflict, turning point, cinematic visuals, emotional
  peak, and lesson bridge
- full content engineering packet
- no provider, n8n, or media execution claim

Fail when:

- `web_required=false`
- unsupported claims remain while `SOURCE_RESEARCH_LOCK=PASS`
- cinematic story block is missing
- output stops at script-only without an explicit script-only request

## T-SCRIPT-02 - Latest AI Video Tools

Prompt:

```text
Write a 5-minute script about the latest AI video tools creators should watch
this week.
```

Expected:

- `current_data_required=true`
- `web_required=true`
- retrieved sources before current claims
- per-tool source map
- source breadth gate

Fail when static knowledge is used as the final source of truth.

## T-SCRIPT-03 - Evergreen Mindset Without Real-Person Proof

Prompt:

```text
Write a 5-minute evergreen mindset script without real-person examples.
```

Expected:

- repo-first route
- web optional
- honestly labeled `realistic_composite` or `mythological_parallel` story
- 45-75 second cinematic story block
- content engineering packet

Fail when a generic direct script appears before routing.

## T-SCRIPT-04 - Explicit Script-Only Request

Prompt:

```text
Give me only a script, no media packet.
```

Expected:

- `explicit_script_only_request=true`
- reduced packet allowed
- script-only output may pass when all remaining evidence gates pass

## Local Validator

Run:

```bash
python3 validators/validate_script_generation_output.py --self-test
```

The validator must reject:

- missing cinematic story
- incomplete story structure
- real-person story without source references
- unsupported claims with `SOURCE_RESEARCH_LOCK=PASS`
- web-required real-world claims with `web_required=false`
- realtime sources without source list
- missing content engineering sections
- script-only output without explicit request
- final proof status stronger than the weakest evidence layer
