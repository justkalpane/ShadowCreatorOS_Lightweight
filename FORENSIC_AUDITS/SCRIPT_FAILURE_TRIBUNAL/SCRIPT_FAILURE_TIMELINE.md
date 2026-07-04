# Script Failure Timeline

## Sequence

1. Boot and route selection succeeded.
   - The transcript shows `SHADOW_BOOT_CONFIRMATION` and `route_id=SCRIPT_GENERATION`.

2. Source claims were introduced.
   - Two URL-backed claims were written, but only two sources were used and both were the same source type.

3. Opening hook variants were generated.
   - Three hooks exist, so the opening-hook gate is not the first failure.

4. The beat map was built with illegal durations.
   - The transcript contains `50`, `60`, `65`, `50`, and `30` second blocks, which violates the hard `3-20` second contract.

5. The script body was written.
   - The spoken script itself is long enough for 5 minutes, so the failure is not a short-body failure.

6. Proof serialization remained shallow.
   - No `source_row_json`, `fact_map_row_json`, `rehook_row_json`, or `LINE_BY_LINE_INFLUENCE_MAP` rows are present in the inspected transcript.

7. The output self-certified quality.
   - The transcript prints `script_quality_gate_present=true` without the score fields required by the quality gate.

8. Acceptance-test mismatch remains.
   - The canonical route slice does not require `VALIDATION_SCORECARD`, although the acceptance test does.

## First drift point

`DYNAMIC_TIMED_BEAT_MAP`

## Where production quality collapsed

The collapse happened when the output stopped being a machine-checkable proof
packet and became a self-certified narrative packet.

