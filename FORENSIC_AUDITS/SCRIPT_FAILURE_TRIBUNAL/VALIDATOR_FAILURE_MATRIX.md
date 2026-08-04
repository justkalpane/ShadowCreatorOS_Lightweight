# Validator Failure Matrix

| evidence location | validator impact | likely pass-fail effect | repair priority |
| --- | --- | --- | --- |
| `validators/validate_script_generation_output.py:2210-2225` and the transcript `:48-85` | Source lock should fail when structured source rows are absent | The output would fail source-proof validation | P0 |
| `validators/validate_script_generation_output.py:2233-2318` and the transcript `:48-85, 117-220` | Real-person source count, source category count, and source-to-script alignment are enforced | The output remains at best partial, not pass | P0 |
| `validators/validate_script_generation_output.py:2320-2493` and the transcript `:129-220` | Beat fields, re-hook rows, and max-gap checks are enforced | The output fails on missing structured rehook rows and can fail on beat structure | P0 |
| `validators/validate_mac06_1a_output.py:647-667, 760-823, 923-953` | Scorecard and quality thresholds are required, not just presence booleans | The output can print false PASS-like markers and still be structurally wrong | P0 |
| `validators/validate_script_generation_output.py:2517-2552` | Final media/influence sync requires scene sync and line-level influence depth | Final-draft acceptance fails when the influence surface is shallow or missing | P1 |

## Validator-layer conclusion

The validator surface is strong enough to catch the failure. The dangerous part
is that the transcript prints success-shaped booleans before the actual proof
objects exist.

