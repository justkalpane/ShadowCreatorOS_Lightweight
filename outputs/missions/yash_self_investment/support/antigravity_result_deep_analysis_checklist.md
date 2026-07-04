# Antigravity Result Deep Analysis Checklist

mission_id=yash_self_investment
route_id=MEDIA_FACTORY_HANDOFF
mode=ANALYSIS_ONLY_NO_REPO_WRITE

## Objective

Deeply analyze the outputs from the HyperFrames method tests and any proof reruns. Explain where the drift happened, why it happened, and what is truly proven versus only assumed.

## Required Analysis Inputs

- the validation packet used for the test
- all produced raw renders
- all produced composite renders
- all produced final proof artifacts
- all proof JSON files
- registry rows related to the run
- extracted verification frames
- `ffprobe` output for every artifact being evaluated

## Mandatory Analysis Questions

### 1. Input Compliance

- Did the run actually read the packet files named in the prompt?
- Did it honor the `source_background` paths?
- Did it honor the `headline_primary`, `headline_secondary`, `support_line`, and `metric_or_claim` payloads?
- Did it honor `effect_pack_ids` and `border_pack_id`?

### 2. Render Compliance

- Was the raw family render correct?
- Was the composed output correct?
- Did the final proof artifact come from the intended assembled lane or from the wrong intermediate artifact?

### 3. Timing Compliance

- Expected duration?
- Actual raw duration?
- Actual composite duration?
- Actual final duration?
- Did the summary JSON overstate success?

### 4. FX / HUD Compliance

- Which cuts visibly show effect layers?
- Which cuts visibly show border or HUD treatment?
- Which claimed effects are absent?
- Is smoke actually present, or merely referenced in config?

### 5. Payload Compliance

- Which cuts still show generic template copy?
- Which cuts show packet-specific copy correctly?
- Was there any hardcoded fallback to template defaults?

### 6. Assembly Drift

Check for:

- raw panel used instead of composed panel
- stale artifact reused
- wrong output path selected
- wrong clip family concatenated
- clip standardization missing before concat
- alpha lane rendered but not composited
- audio path declared but absent in final output

## Root-Cause Categories

Every failure must be classified into one or more of:

- `PACKET_NOT_HONORED`
- `PAYLOAD_NOT_INJECTED`
- `BACKGROUND_NOT_COMPOSITED`
- `V3_EFFECT_NOT_COMPOSITED`
- `AUDIO_NOT_ASSEMBLED`
- `STALE_ARTIFACT_REUSED`
- `WRONG_FINAL_OUTPUT_SELECTED`
- `DURATION_COLLAPSE`
- `OVERCLAIMED_PASS`
- `CAPABILITY_PRESENT_BUT_UNPROVEN`

## Required Evidence Format

For every important finding:

- `claim=`
- `evidence=`
- `evidence_path=`
- `command_output_or_file_reference=`
- `status=PASS/PARTIAL/BLOCKED/NEEDS_CONFIRMATION`

## Required Comparison Blocks

For every failed or drifting test, provide:

- expected behavior
- actual behavior
- visual proof reference
- metadata proof reference
- likely root cause
- confidence level

## Final Analysis Output

Antigravity must end with:

1. `PROVEN_NOW`
2. `PRESENT_BUT_NOT_PROVEN`
3. `REQUESTED_BUT_MISSED`
4. `OVERCLAIMED`
5. `ROOT_CAUSE_PRIORITY_ORDER`
6. `SAFE_NEXT_ACTIONS`

## Forbidden

- do not convert missing evidence into `PASS`
- do not say “visible” without a frame or clip reference
- do not say “payload injected” without matching text evidence
- do not say “30 seconds” without `ffprobe`
