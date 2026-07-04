# Real-Time Research Enforcement Contract

## Purpose

Source presence is not the same as real-time research. Research claims must
describe the evidence actually retrieved.

## Required Semantics

```text
web_access_used=true
real_time_sources_used=false
research_mode=WEB_ASSISTED_STATIC_REFERENCE or WEB_ASSISTED_LIMITED_REFERENCE
```

The state above must never be described as real-time research.

## Real-Person Anchor Rule

Production scripts using a real person, career arc, incident, case study, or
real-world proof require:

- web-assisted research when web access is available
- at least three sources when suitable sources are available
- at least two non-encyclopedia sources
- at least three source categories where available
- a `SOURCE_LEDGER`
- `SOURCE_LIMITATION_NOTES`
- a `FACT_VS_ANECDOTE_MAP`

## Source Classes

- `official_source`
- `credible_news_article`
- `interview_reporting`
- `historical_record`
- `biography_reference`
- `encyclopedia_background`
- `video_reference`
- `secondary_commentary`

## Pass Blockers

- `real_time_sources_used=false` while real-time research is claimed
- a single encyclopedia record used as final authority
- interview reporting used as verified fact without independent support
- missing source ledger
- missing fact-versus-anecdote map
- non-empty unsupported claims with a passing source lock
- current-film promo, teaser, or release-marketing lines inserted into the
  spoken script without explicit user request or source-backed relevance
