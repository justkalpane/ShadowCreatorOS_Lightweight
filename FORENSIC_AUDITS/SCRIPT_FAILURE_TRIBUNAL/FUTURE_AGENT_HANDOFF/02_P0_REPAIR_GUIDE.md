# P0 Repair Guide

## Scope

P0 work must restore the proof surfaces that make production validation
possible.

## Required fixes

- Rebuild the beat map inside the hard `3-20` second range.
- Emit structured `source_row_json`, `fact_map_row_json`, and `rehook_row_json`
  rows.
- Emit a real scorecard before any pass claim.
- Preserve `LINE_BY_LINE_INFLUENCE_MAP` all the way into final output.

