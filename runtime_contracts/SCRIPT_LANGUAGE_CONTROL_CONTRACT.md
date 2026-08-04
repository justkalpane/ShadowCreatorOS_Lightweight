# Script Language Control Contract

## Purpose

Every script route must produce a deterministic English master draft unless the
user explicitly requests another language or asks for translation/localization.

## Master Language Law

```text
default_master_script_language=English
translation_stage_required=true
translation_stage_separate_from_master_draft=true
language_inference_from_topic=false
language_inference_from_celebrity=false
language_inference_from_location=false
language_inference_from_culture=false
language_inference_from_mythology=false
language_inference_from_source_language=false
```

Hindi, Kannada, Telugu, Tamil, and other Indian languages are supported only
when the user explicitly requests that language or during a separate
translation/localization stage.

## Required Output

```text
SCRIPT_LANGUAGE_DECLARATION
master_script_language=
translation_stage_required=
non_english_generation_allowed=
language_inference_blocked=

USER_LANGUAGE_REQUEST_CHECK
explicit_language_requested=
requested_language=
output_language_decision=
```

## Failure Rules

- A first draft in Hindi, Hinglish, Kannada, Telugu, Tamil, or another
  non-English language fails when no explicit language request exists.
- A celebrity, geography, cultural reference, mythology reference, source
  language, typo, or previous output must never silently change the master
  script language.
- Translation is a downstream localization task. It does not overwrite the
  approved English master draft.

