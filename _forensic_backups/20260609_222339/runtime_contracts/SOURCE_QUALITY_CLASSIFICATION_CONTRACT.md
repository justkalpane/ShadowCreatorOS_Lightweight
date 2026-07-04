# Source Quality Classification Contract

## Purpose

The research layer must validate source sufficiency, not merely source
existence.

## Claim Classes

Every production-sensitive claim must be classified as one of:

- `VERIFIED`
- `CROSS_VERIFIED`
- `ANECDOTAL_SUPPORT`
- `BACKGROUND_CONTEXT`
- `INFERENCE`
- `NEEDS_CONFIRMATION`
- `UNSUPPORTED`

## Source Sufficiency Gate

For a production-grade real-person script:

```text
minimum_total_sources=3
minimum_non_encyclopedia_sources=2
minimum_source_categories=3
fact_vs_anecdote_map_present=true
```

An encyclopedia record may provide background context. It cannot be the sole
final authority. Interview reporting may support an emotional angle. It cannot
be treated as independently verified fact unless cross-verification is
recorded.

## Required Ledger Fields

```text
SOURCE_LEDGER
source_id=
url=
title=
date=
source_type=
claim_supported=
limitation=

FACT_VS_ANECDOTE_MAP
claim=
source=
classification=
script_usage_allowed=
risk_note=
```

Ledger URLs must point to specific pages, articles, interviews, records, or
documents. Root-domain-only entries such as `https://example.com/` or
`https://news-site.com/` do not count as source evidence and cannot pass the
source sufficiency gate.

Source labels without URLs are not evidence. Entries such as `Wikipedia - Yash`,
`Hindustan Times - Yash Interview`, `Search_Web_Results`, or `general
biography` cannot support `SOURCE_RESEARCH_LOCK=PASS` unless they are converted
into structured ledger rows with real URLs and limitations.

If `web_search_conducted=true`, `SOURCE_RESEARCH_LOCK status=PASS`, or
`SOURCE_BREADTH_LOCK status=PASS`, the output must include structured
`source_row_json=` rows and structured `fact_map_row_json=` rows before final
proof.

## Source-To-Script Alignment Law

For real-person proof scripts:

- every fact-like line in `FINAL_SCRIPT` must align to a mapped fact row or
  source row
- a weaker anecdotal source cannot justify a stronger verified-style spoken line
- if a line contains numbers, career milestones, job roles, locations, quotes,
  or biographical events, the line must have an evidence-mapped counterpart

## Absolute Claim Law

Words such as `every`, `always`, `never`, `only`, `all`, `zero shortcuts`, or
equivalent absolutes require explicit source-backed support when attached to a
real person's biography or career arc. Otherwise, downgrade the line to
motivational framing or mark it anecdotal.
