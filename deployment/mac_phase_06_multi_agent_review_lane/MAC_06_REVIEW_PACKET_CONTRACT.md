# MAC-06 Review Packet Contract

Every reviewer must return one structured packet per dossier review.

## Required Fields

- `review_agent`
- `reviewed_dossier_id`
- `reviewed_files`
- `score_summary`
- `topic_adherence_score` (0-10)
- `script_quality_score` (0-10)
- `generic_output_risk` (`low`/`medium`/`high`)
- `director_grounding_check` (`pass`/`fail`)
- `skill_grounding_check` (`pass`/`fail`)
- `lineage_check` (`pass`/`fail`)
- `context_packet_check` (`pass`/`fail`)
- `provider_handoff_check` (`pass`/`fail`)
- `recommended_changes`
- `must_fix_items`
- `optional_improvements`
- `approval_recommendation` (`approve`/`approve_with_changes`/`reject`)

## Format Rule

Return as Markdown with:

1. Short summary
2. Score table
3. Must-fix list
4. Optional improvements
5. Approval recommendation

## Grounding Rule

Claims must reference dossier files or repo doctrine/contract paths. No generic critique without artifact evidence.

## Safety Rule

No provider execution claims. No n8n execution claims. No media artifact generation claims unless actually generated in an approved execution phase.

