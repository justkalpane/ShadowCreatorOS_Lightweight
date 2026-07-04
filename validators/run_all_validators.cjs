#!/usr/bin/env node
/**
 * Aggregate Validator (Substantive)
 * Executes runFullCheck() on all validator classes; aggregates findings; exits non-zero on any error-severity finding.
 *
 * This is NOT a count-only validator. It executes:
 *   - WorkflowValidator.runFullCheck()
 *   - SchemaValidator.runFullCheck()
 *   - RegistryValidator.runFullCheck()
 *   - RuntimeValidator.runFullCheck() (if present)
 *   - ModelValidator.validate()
 *   - ModeValidator.validate()
 *   - Dossier runtime model validation
 *
 * Each result is summarized with overall_valid, finding count, and selected findings.
 */

const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

const repoRoot = path.resolve(__dirname, '..');
const cliArgs = process.argv.slice(2);
const listMode = cliArgs.includes('--list');
const dryRun = cliArgs.includes('--dry-run');
const pythonOnly = cliArgs.includes('--python-only');
const strictMode = cliArgs.includes('--strict');
const helpMode = cliArgs.includes('--help') || cliArgs.includes('-h');

const validators = [
  {
    name: 'WorkflowValidator',
    load: () => require('./workflow_validator.cjs'),
    run: (Cls) => new Cls().runFullCheck()
  },
  {
    name: 'SchemaValidator',
    load: () => require('./schema_validator.cjs'),
    run: (Cls) => new Cls().runFullCheck()
  },
  {
    name: 'RegistryValidator',
    load: () => require('./registry_validator.cjs'),
    run: (Cls) => new Cls().runFullCheck()
  },
  {
    name: 'ModelValidator',
    load: () => require('./model_validator.cjs'),
    run: (Cls) => {
      const r = new Cls().validate();
      return {
        overall_valid: r.passed,
        findings: (r.errors || []).map((m) => ({ severity: 'error', code: 'MODEL_REGISTRY', message: m }))
          .concat((r.warnings || []).map((m) => ({ severity: 'warning', code: 'MODEL_REGISTRY', message: m })))
      };
    }
  },
  {
    name: 'ModeValidator',
    load: () => require('./mode_validator.cjs'),
    run: (Cls) => {
      const r = new Cls().validate();
      return {
        overall_valid: r.passed,
        findings: (r.errors || []).map((m) => ({ severity: 'error', code: 'MODE_REGISTRY', message: m }))
          .concat((r.warnings || []).map((m) => ({ severity: 'warning', code: 'MODE_REGISTRY', message: m })))
      };
    }
  }
];

const pythonValidatorSpecs = [
  {
    name: 'validate_script_generation_output.py',
    relativePath: 'validators/validate_script_generation_output.py',
    args: ['--self-test'],
    fixturePaths: []
  },
  {
    name: 'validate_mac06_1a_output.py',
    relativePath: 'validators/validate_mac06_1a_output.py',
    args: ['validators/fixtures/mac06_1a_pass_minimal_complete.txt'],
    fixturePaths: ['validators/fixtures/mac06_1a_pass_minimal_complete.txt']
  },
  {
    name: 'validate_route_consumption_order.py',
    relativePath: 'validators/validate_route_consumption_order.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/gold/script_generation_consumption_order.yaml',
      'validators/fixtures/gold/visual_media_plan_consumption_order.yaml',
      'validators/fixtures/gold/visual_media_generation_draft_consumption_order.yaml',
      'validators/fixtures/bad/bad_consumption_order.yaml'
    ],
    fixtureProbes: [
      { label: 'gold_script_order', path: 'validators/fixtures/gold/script_generation_consumption_order.yaml', expectedExit: 0 },
      { label: 'gold_visual_plan_order', path: 'validators/fixtures/gold/visual_media_plan_consumption_order.yaml', expectedExit: 0 },
      { label: 'gold_visual_draft_order', path: 'validators/fixtures/gold/visual_media_generation_draft_consumption_order.yaml', expectedExit: 0 },
      { label: 'bad_consumption_order', path: 'validators/fixtures/bad/bad_consumption_order.yaml', expectedExit: 1 }
    ]
  },
  {
    name: 'validate_visual_template_lock.py',
    relativePath: 'validators/validate_visual_template_lock.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/gold/gold_visual_transposed_scene_blocks.md',
      'validators/fixtures/bad/visual_media_generation_draft_bad_flat_template.md',
      'validators/fixtures/bad/visual_media_generation_draft_bad_missing_reasoning.md',
      'validators/fixtures/bad/bad_visual_horizontal_table_only.md',
      'validators/fixtures/bad/bad_visual_missing_transposed_layers.md'
    ],
    fixtureProbes: [
      { label: 'gold_visual_transposed_template', path: 'validators/fixtures/gold/gold_visual_transposed_scene_blocks.md', expectedExit: 0 },
      { label: 'bad_flat_visual_template', path: 'validators/fixtures/bad/visual_media_generation_draft_bad_flat_template.md', expectedExit: 1 },
      { label: 'bad_missing_reasoning', path: 'validators/fixtures/bad/visual_media_generation_draft_bad_missing_reasoning.md', expectedExit: 1 },
      { label: 'bad_horizontal_table_only', path: 'validators/fixtures/bad/bad_visual_horizontal_table_only.md', expectedExit: 1 },
      { label: 'bad_missing_transposed_layers', path: 'validators/fixtures/bad/bad_visual_missing_transposed_layers.md', expectedExit: 1 }
    ]
  },
  {
    name: 'validate_broll_ratio.py',
    relativePath: 'validators/validate_broll_ratio.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/gold/broll_ratio_good_13_1.md',
      'validators/fixtures/bad/broll_ratio_bad_5_2.md'
    ],
    fixtureProbes: [
      { label: 'gold_broll_13_1', path: 'validators/fixtures/gold/broll_ratio_good_13_1.md', expectedExit: 0 },
      { label: 'bad_broll_5_2', path: 'validators/fixtures/bad/broll_ratio_bad_5_2.md', expectedExit: 1 }
    ]
  },
  {
    name: 'validate_evidence_scope_claims.py',
    relativePath: 'validators/validate_evidence_scope_claims.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/gold/evidence_scope_good.md',
      'validators/fixtures/gold/evidence_scope_current_cycle.md',
      'validators/fixtures/bad/evidence_scope_bad_memory_only.md',
      'validators/fixtures/bad/evidence_scope_bad_no_scope.md'
    ],
    fixtureProbes: [
      { label: 'gold_evidence_scope', path: 'validators/fixtures/gold/evidence_scope_good.md', expectedExit: 0 },
      { label: 'gold_current_cycle_scope', path: 'validators/fixtures/gold/evidence_scope_current_cycle.md', expectedExit: 0 },
      { label: 'bad_memory_only_scope', path: 'validators/fixtures/bad/evidence_scope_bad_memory_only.md', expectedExit: 1 },
      { label: 'bad_missing_scope', path: 'validators/fixtures/bad/evidence_scope_bad_no_scope.md', expectedExit: 1 }
    ]
  },
  {
    name: 'validate_route_trigger_collision.py',
    relativePath: 'validators/validate_route_trigger_collision.py',
    args: [],
    fixturePaths: [
      'registries/route_manifests/media_factory_handoff.yaml',
      'registries/route_manifests/avatar_video_context.yaml'
    ]
  },
  {
    name: 'validate_route_claim_evidence_consistency.py',
    relativePath: 'validators/validate_route_claim_evidence_consistency.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/bad/bad_shallow_fake_pass_claims_68_reads.md',
      'validators/fixtures/bad/bad_route_claim_pass_with_fake_slice_path.md',
      'validators/fixtures/bad/bad_route_claim_pass_with_manifest_slice_mismatch.md',
      'validators/fixtures/gold/gold_script_reconstructed.md',
      'validators/fixtures/gold/gold_route_claim_with_verified_slice_lineage.md',
      'validators/fixtures/bad/bad_latest_antigravity_alias_fake_pass.md',
      'validators/fixtures/gold/gold_alias_claims_with_complete_evidence.md'
    ],
    fixtureProbes: [
      { label: 'bad_route_claim_68_reads', path: 'validators/fixtures/bad/bad_shallow_fake_pass_claims_68_reads.md', expectedExit: 1 },
      { label: 'bad_route_claim_fake_slice_path', path: 'validators/fixtures/bad/bad_route_claim_pass_with_fake_slice_path.md', expectedExit: 1 },
      { label: 'bad_route_claim_slice_manifest_mismatch', path: 'validators/fixtures/bad/bad_route_claim_pass_with_manifest_slice_mismatch.md', expectedExit: 1 },
      { label: 'gold_route_claim_script', path: 'validators/fixtures/gold/gold_script_reconstructed.md', expectedExit: 0 },
      { label: 'gold_route_claim_verified_slice_lineage', path: 'validators/fixtures/gold/gold_route_claim_with_verified_slice_lineage.md', expectedExit: 0 },
      { label: 'bad_route_claim_alias_fake_pass', path: 'validators/fixtures/bad/bad_latest_antigravity_alias_fake_pass.md', expectedExit: 1 },
      { label: 'gold_route_claim_alias_complete', path: 'validators/fixtures/gold/gold_alias_claims_with_complete_evidence.md', expectedExit: 0 }
    ]
  },
  {
    name: 'validate_source_freshness_url_ledger.py',
    relativePath: 'validators/validate_source_freshness_url_ledger.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/bad/bad_current_freshness_without_urls.md',
      'validators/fixtures/bad/bad_web_used_without_source_evidence.md',
      'validators/fixtures/gold/gold_current_freshness_with_urls.md',
      'validators/fixtures/bad/bad_latest_antigravity_alias_fake_pass.md',
      'validators/fixtures/gold/gold_alias_claims_with_complete_evidence.md'
    ],
    fixtureProbes: [
      { label: 'bad_current_without_urls', path: 'validators/fixtures/bad/bad_current_freshness_without_urls.md', expectedExit: 1 },
      { label: 'bad_web_without_source', path: 'validators/fixtures/bad/bad_web_used_without_source_evidence.md', expectedExit: 1 },
      { label: 'gold_current_with_urls', path: 'validators/fixtures/gold/gold_current_freshness_with_urls.md', expectedExit: 0 },
      { label: 'bad_source_alias_fake_pass', path: 'validators/fixtures/bad/bad_latest_antigravity_alias_fake_pass.md', expectedExit: 1 },
      { label: 'gold_source_alias_complete', path: 'validators/fixtures/gold/gold_alias_claims_with_complete_evidence.md', expectedExit: 0 }
    ]
  },
  {
    name: 'validate_packet_ready_artifacts.py',
    relativePath: 'validators/validate_packet_ready_artifacts.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/bad/bad_packet_ready_without_artifacts.md',
      'validators/fixtures/gold/gold_packet_ready_with_artifacts.md',
      'validators/fixtures/bad/bad_latest_antigravity_alias_fake_pass.md',
      'validators/fixtures/gold/gold_alias_claims_with_complete_evidence.md'
    ],
    fixtureProbes: [
      { label: 'bad_packet_ready_without_artifacts', path: 'validators/fixtures/bad/bad_packet_ready_without_artifacts.md', expectedExit: 1 },
      { label: 'gold_packet_ready_with_artifacts', path: 'validators/fixtures/gold/gold_packet_ready_with_artifacts.md', expectedExit: 0 },
      { label: 'bad_packet_alias_fake_pass', path: 'validators/fixtures/bad/bad_latest_antigravity_alias_fake_pass.md', expectedExit: 1 },
      { label: 'gold_packet_alias_complete', path: 'validators/fixtures/gold/gold_alias_claims_with_complete_evidence.md', expectedExit: 0 }
    ]
  },
  {
    name: 'validate_visual_generation_depth.py',
    relativePath: 'validators/validate_visual_generation_depth.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/bad/bad_visual_sfx_generic_prose.md',
      'validators/fixtures/bad/bad_davinci_generic_prose.md',
      'validators/fixtures/gold/gold_visual_draft_reconstructed.md'
    ],
    fixtureProbes: [
      { label: 'bad_visual_sfx_generic_prose', path: 'validators/fixtures/bad/bad_visual_sfx_generic_prose.md', expectedExit: 1 },
      { label: 'bad_davinci_generic_prose', path: 'validators/fixtures/bad/bad_davinci_generic_prose.md', expectedExit: 1 },
      { label: 'gold_visual_generation_depth', path: 'validators/fixtures/gold/gold_visual_draft_reconstructed.md', expectedExit: 0 }
    ]
  },
  {
    name: 'validate_route_state_capsule.py',
    relativePath: 'validators/validate_route_state_capsule.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/bad/missing_route_state_capsule.json',
      'validators/fixtures/gold/route_state_capsule_complete.json'
    ],
    fixtureProbes: [
      { label: 'bad_missing_route_state_capsule', path: 'validators/fixtures/bad/missing_route_state_capsule.json', expectedExit: 1 },
      { label: 'gold_route_state_capsule_complete', path: 'validators/fixtures/gold/route_state_capsule_complete.json', expectedExit: 0 }
    ]
  },
  {
    name: 'validate_evidence_bundle.py',
    relativePath: 'validators/validate_evidence_bundle.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/gold/evidence_bundle_complete.json',
      'validators/fixtures/gold/pass_with_evidence_bundle.json',
      'validators/fixtures/bad/missing_evidence_bundle_id.json',
      'validators/fixtures/bad/pass_reason_ffprobe_only.json'
    ],
    fixtureProbes: [
      { label: 'gold_evidence_bundle_complete', path: 'validators/fixtures/gold/evidence_bundle_complete.json', expectedExit: 0 },
      { label: 'bad_missing_evidence_bundle_id', path: 'validators/fixtures/bad/missing_evidence_bundle_id.json', expectedExit: 1 },
      { label: 'bad_pass_reason_ffprobe_only', path: 'validators/fixtures/bad/pass_reason_ffprobe_only.json', expectedExit: 1 }
    ]
  },
  {
    name: 'validate_patch_transaction.py',
    relativePath: 'validators/validate_patch_transaction.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/gold/patch_transaction_clean.json',
      'validators/fixtures/bad/patch_transaction_forbidden_touch.json'
    ],
    fixtureProbes: [
      { label: 'gold_patch_transaction_clean', path: 'validators/fixtures/gold/patch_transaction_clean.json', expectedExit: 0 },
      { label: 'bad_patch_transaction_forbidden_touch', path: 'validators/fixtures/bad/patch_transaction_forbidden_touch.json', expectedExit: 1 }
    ]
  },
  {
    name: 'validate_bridge_job_packet.py',
    relativePath: 'validators/validate_bridge_job_packet.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/gold/bridge_job_packet_c04a.json',
      'validators/fixtures/bad/provider_execution_without_approval.json'
    ],
    fixtureProbes: [
      { label: 'gold_bridge_job_packet_c04a', path: 'validators/fixtures/gold/bridge_job_packet_c04a.json', expectedExit: 0 },
      { label: 'bad_provider_execution_without_approval', path: 'validators/fixtures/bad/provider_execution_without_approval.json', expectedExit: 1 }
    ]
  },
  {
    name: 'validate_visual_media_plan_row.py',
    relativePath: 'validators/validate_visual_media_plan_row.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/gold/visual_media_plan_row_complete.json',
      'validators/fixtures/gold/visual_plan_rowwise_valid.md',
      'validators/fixtures/bad/generic_slideshow_pass.json',
      'validators/fixtures/bad/visual_plan_missing_15_dna_fields.json'
    ],
    fixtureProbes: [
      { label: 'gold_visual_media_plan_row_complete', path: 'validators/fixtures/gold/visual_media_plan_row_complete.json', expectedExit: 0 },
      { label: 'bad_generic_slideshow_pass', path: 'validators/fixtures/bad/generic_slideshow_pass.json', expectedExit: 1 },
      { label: 'bad_visual_plan_missing_15_dna_fields', path: 'validators/fixtures/bad/visual_plan_missing_15_dna_fields.json', expectedExit: 1 }
    ]
  },
  {
    name: 'validate_final_visual_media_generation_draft.py',
    relativePath: 'validators/validate_final_visual_media_generation_draft.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/gold/final_visual_generation_draft_complete.json',
      'validators/fixtures/gold/final_visual_draft_valid.md',
      'validators/fixtures/bad/source_vs_render_required_false.json',
      'validators/fixtures/bad/visual_qa_required_false.json',
      'validators/fixtures/bad/contact_sheet_required_false.json',
      'validators/fixtures/bad/pilot_required_before_batch_false.json'
    ],
    fixtureProbes: [
      { label: 'gold_final_visual_generation_draft_complete', path: 'validators/fixtures/gold/final_visual_generation_draft_complete.json', expectedExit: 0 },
      { label: 'bad_source_vs_render_required_false', path: 'validators/fixtures/bad/source_vs_render_required_false.json', expectedExit: 1 },
      { label: 'bad_visual_qa_required_false', path: 'validators/fixtures/bad/visual_qa_required_false.json', expectedExit: 1 }
    ]
  },
  {
    name: 'validate_depth_map_packet.py',
    relativePath: 'validators/validate_depth_map_packet.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/gold/depth_map_packet_valid.json',
      'validators/fixtures/gold/true_parallax_valid.json',
      'validators/fixtures/bad/depth_method_blur.json',
      'validators/fixtures/bad/depth_method_boxblur.json',
      'validators/fixtures/bad/depth_method_maskedmerge_only.json'
    ],
    fixtureProbes: [
      { label: 'gold_depth_map_packet_valid', path: 'validators/fixtures/gold/depth_map_packet_valid.json', expectedExit: 0 },
      { label: 'bad_depth_method_blur', path: 'validators/fixtures/bad/depth_method_blur.json', expectedExit: 1 },
      { label: 'bad_depth_method_boxblur', path: 'validators/fixtures/bad/depth_method_boxblur.json', expectedExit: 1 }
    ]
  },
  {
    name: 'validate_ffmpeg_filtergraph_packet.py',
    relativePath: 'validators/validate_ffmpeg_filtergraph_packet.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/gold/ffmpeg_filtergraph_packet_valid.json',
      'validators/fixtures/gold/ffmpeg_filtergraph_valid.json',
      'validators/fixtures/bad/ffmpeg_missing_lanczos.json',
      'validators/fixtures/bad/ffmpeg_missing_crf18.json',
      'validators/fixtures/bad/ffmpeg_missing_bt709.json',
      'validators/fixtures/bad/ffmpeg_missing_filtergraph_dump.json',
      'validators/fixtures/bad/hidden_double_encode.json'
    ],
    fixtureProbes: [
      { label: 'gold_ffmpeg_filtergraph_packet_valid', path: 'validators/fixtures/gold/ffmpeg_filtergraph_packet_valid.json', expectedExit: 0 },
      { label: 'bad_ffmpeg_missing_lanczos', path: 'validators/fixtures/bad/ffmpeg_missing_lanczos.json', expectedExit: 1 },
      { label: 'bad_hidden_double_encode', path: 'validators/fixtures/bad/hidden_double_encode.json', expectedExit: 1 }
    ]
  },
  {
    name: 'validate_hyperframes_payload.py',
    relativePath: 'validators/validate_hyperframes_payload.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/gold/hyperframes_payload_valid.json',
      'validators/fixtures/bad/hyperframes_missing_blend_mode.json',
      'validators/fixtures/bad/hyperframes_missing_alpha_mode.json',
      'validators/fixtures/bad/hyperframes_missing_alpha.json',
      'validators/fixtures/bad/hyperframes_subject_occlusion.json',
      'validators/fixtures/bad/hyperframes_random_overlay.json'
    ],
    fixtureProbes: [
      { label: 'gold_hyperframes_payload_valid', path: 'validators/fixtures/gold/hyperframes_payload_valid.json', expectedExit: 0 },
      { label: 'bad_hyperframes_missing_alpha_mode', path: 'validators/fixtures/bad/hyperframes_missing_alpha_mode.json', expectedExit: 1 },
      { label: 'bad_hyperframes_random_overlay', path: 'validators/fixtures/bad/hyperframes_random_overlay.json', expectedExit: 1 }
    ]
  },
  {
    name: 'validate_comfyui_payload.py',
    relativePath: 'validators/validate_comfyui_payload.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/gold/comfyui_payload_with_hires_fix.json',
      'validators/fixtures/gold/comfyui_payload_valid.json',
      'validators/fixtures/bad/comfyui_timeout_marked_pass.json',
      'validators/fixtures/bad/comfyui_missing_workflow_json.json',
      'validators/fixtures/bad/comfyui_missing_node_graph_hash.json',
      'validators/fixtures/bad/comfyui_native_1920_no_hires.json'
    ],
    fixtureProbes: [
      { label: 'gold_comfyui_payload_with_hires_fix', path: 'validators/fixtures/gold/comfyui_payload_with_hires_fix.json', expectedExit: 0 },
      { label: 'bad_comfyui_timeout_marked_pass', path: 'validators/fixtures/bad/comfyui_timeout_marked_pass.json', expectedExit: 1 },
      { label: 'bad_comfyui_native_1920_no_hires', path: 'validators/fixtures/bad/comfyui_native_1920_no_hires.json', expectedExit: 1 }
    ]
  },
  {
    name: 'validate_source_vs_render_packet.py',
    relativePath: 'validators/validate_source_vs_render_packet.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/gold/source_vs_render_valid.json',
      'validators/fixtures/bad/source_vs_render_missing_diff.json',
      'validators/fixtures/bad/source_vs_render_missing_thresholds.json'
    ],
    fixtureProbes: [
      { label: 'gold_source_vs_render_valid', path: 'validators/fixtures/gold/source_vs_render_valid.json', expectedExit: 0 },
      { label: 'bad_source_vs_render_missing_diff', path: 'validators/fixtures/bad/source_vs_render_missing_diff.json', expectedExit: 1 },
      { label: 'bad_source_vs_render_missing_thresholds', path: 'validators/fixtures/bad/source_vs_render_missing_thresholds.json', expectedExit: 1 }
    ]
  },
  {
    name: 'validate_visual_qa_acceptance.py',
    relativePath: 'validators/validate_visual_qa_acceptance.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/gold/visual_qa_acceptance_complete.json',
      'validators/fixtures/gold/visual_qa_valid_full_packet.json',
      'validators/fixtures/bad/visual_qa_missing_contact_sheet.json',
      'validators/fixtures/bad/visual_qa_missing_human_review.json'
    ],
    fixtureProbes: [
      { label: 'gold_visual_qa_acceptance_complete', path: 'validators/fixtures/gold/visual_qa_acceptance_complete.json', expectedExit: 0 },
      { label: 'bad_visual_qa_missing_contact_sheet', path: 'validators/fixtures/bad/visual_qa_missing_contact_sheet.json', expectedExit: 1 },
      { label: 'bad_visual_qa_missing_human_review', path: 'validators/fixtures/bad/visual_qa_missing_human_review.json', expectedExit: 1 }
    ]
  },
  {
    name: 'validate_pilot_cut_validation_packet.py',
    relativePath: 'validators/validate_pilot_cut_validation_packet.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/gold/pilot_cut_c04a_valid.json',
      'validators/fixtures/gold/pilot_c04a_valid.json',
      'validators/fixtures/bad/pilot_wrong_cut_id.json',
      'validators/fixtures/bad/full_render_before_pilot.json'
    ],
    fixtureProbes: [
      { label: 'gold_pilot_cut_c04a_valid', path: 'validators/fixtures/gold/pilot_cut_c04a_valid.json', expectedExit: 0 },
      { label: 'bad_pilot_wrong_cut_id', path: 'validators/fixtures/bad/pilot_wrong_cut_id.json', expectedExit: 1 },
      { label: 'bad_full_render_before_pilot', path: 'validators/fixtures/bad/full_render_before_pilot.json', expectedExit: 1 }
    ]
  },
  {
    name: 'validate_audio_authorization_packet.py',
    relativePath: 'validators/validate_audio_authorization_packet.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/gold/audio_authorization_valid.json',
      'validators/fixtures/gold/audio_authorized_valid.json',
      'validators/fixtures/bad/audio_before_visual_acceptance.json'
    ],
    fixtureProbes: [
      { label: 'gold_audio_authorization_valid', path: 'validators/fixtures/gold/audio_authorization_valid.json', expectedExit: 0 },
      { label: 'bad_audio_before_visual_acceptance', path: 'validators/fixtures/bad/audio_before_visual_acceptance.json', expectedExit: 1 }
    ]
  },
  {
    name: 'validate_davinci_handoff_packet.py',
    relativePath: 'validators/validate_davinci_handoff_packet.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/gold/davinci_handoff_valid.json',
      'validators/fixtures/gold/davinci_handoff_authorized.json',
      'validators/fixtures/bad/davinci_before_visual_audio_package.json',
      'validators/fixtures/bad/davinci_before_acceptance.json'
    ],
    fixtureProbes: [
      { label: 'gold_davinci_handoff_valid', path: 'validators/fixtures/gold/davinci_handoff_valid.json', expectedExit: 0 },
      { label: 'bad_davinci_before_visual_audio_package', path: 'validators/fixtures/bad/davinci_before_visual_audio_package.json', expectedExit: 1 }
    ]
  },
  {
    name: 'validate_no_fake_pass_gate.py',
    relativePath: 'validators/validate_no_fake_pass_gate.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/gold/pass_with_evidence_bundle.json',
      'validators/fixtures/bad/pass_reason_ffprobe_only.json',
      'validators/fixtures/bad/pass_reason_file_exists_only.json',
      'validators/fixtures/bad/pass_reason_exit_code_0_only.json',
      'validators/fixtures/bad/pass_reason_contract_exists_only.json'
    ],
    fixtureProbes: [
      { label: 'gold_pass_with_evidence_bundle', path: 'validators/fixtures/gold/pass_with_evidence_bundle.json', expectedExit: 0 },
      { label: 'bad_pass_reason_ffprobe_only', path: 'validators/fixtures/bad/pass_reason_ffprobe_only.json', expectedExit: 1 },
      { label: 'bad_pass_reason_file_exists_only', path: 'validators/fixtures/bad/pass_reason_file_exists_only.json', expectedExit: 1 },
      { label: 'bad_pass_reason_exit_code_0_only', path: 'validators/fixtures/bad/pass_reason_exit_code_0_only.json', expectedExit: 1 },
      { label: 'bad_pass_reason_contract_exists_only', path: 'validators/fixtures/bad/pass_reason_contract_exists_only.json', expectedExit: 1 }
    ]
  },
  {
    name: 'validate_pilot_cut_gate.py',
    relativePath: 'validators/validate_pilot_cut_gate.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/gold/pilot_c04a_valid.json',
      'validators/fixtures/gold/pilot_cut_c04a_valid.json',
      'validators/fixtures/bad/pilot_wrong_cut_id.json',
      'validators/fixtures/bad/full_render_before_pilot.json'
    ],
    fixtureProbes: [
      { label: 'gold_pilot_c04a_valid', path: 'validators/fixtures/gold/pilot_c04a_valid.json', expectedExit: 0 },
      { label: 'gold_pilot_cut_c04a_valid', path: 'validators/fixtures/gold/pilot_cut_c04a_valid.json', expectedExit: 0 },
      { label: 'bad_pilot_wrong_cut_id', path: 'validators/fixtures/bad/pilot_wrong_cut_id.json', expectedExit: 1 },
      { label: 'bad_full_render_before_pilot', path: 'validators/fixtures/bad/full_render_before_pilot.json', expectedExit: 1 }
    ]
  },
  {
    name: 'validate_audio_authorization_gate.py',
    relativePath: 'validators/validate_audio_authorization_gate.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/gold/audio_authorization_valid.json',
      'validators/fixtures/gold/audio_authorized_valid.json',
      'validators/fixtures/bad/audio_before_visual_acceptance.json'
    ],
    fixtureProbes: [
      { label: 'gold_audio_authorization_valid', path: 'validators/fixtures/gold/audio_authorization_valid.json', expectedExit: 0 },
      { label: 'gold_audio_authorized_valid', path: 'validators/fixtures/gold/audio_authorized_valid.json', expectedExit: 0 },
      { label: 'bad_audio_before_visual_acceptance', path: 'validators/fixtures/bad/audio_before_visual_acceptance.json', expectedExit: 1 }
    ]
  },
  {
    name: 'validate_davinci_handoff_gate.py',
    relativePath: 'validators/validate_davinci_handoff_gate.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/gold/davinci_handoff_valid.json',
      'validators/fixtures/gold/davinci_handoff_authorized.json',
      'validators/fixtures/bad/davinci_before_visual_audio_package.json',
      'validators/fixtures/bad/davinci_before_acceptance.json'
    ],
    fixtureProbes: [
      { label: 'gold_davinci_handoff_valid', path: 'validators/fixtures/gold/davinci_handoff_valid.json', expectedExit: 0 },
      { label: 'gold_davinci_handoff_authorized', path: 'validators/fixtures/gold/davinci_handoff_authorized.json', expectedExit: 0 },
      { label: 'bad_davinci_before_visual_audio_package', path: 'validators/fixtures/bad/davinci_before_visual_audio_package.json', expectedExit: 1 },
      { label: 'bad_davinci_before_acceptance', path: 'validators/fixtures/bad/davinci_before_acceptance.json', expectedExit: 1 }
    ]
  },
  {
    name: 'validate_duplicate_read_guard.py',
    relativePath: 'validators/validate_duplicate_read_guard.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/bad/bad_duplicate_reads_after_manifest_complete.json',
      'validators/fixtures/gold/gold_no_duplicate_reads_route_ledger.json'
    ],
    fixtureProbes: [
      { label: 'bad_duplicate_reads_after_manifest_complete', path: 'validators/fixtures/bad/bad_duplicate_reads_after_manifest_complete.json', expectedExit: 1 },
      { label: 'gold_no_duplicate_reads_route_ledger', path: 'validators/fixtures/gold/gold_no_duplicate_reads_route_ledger.json', expectedExit: 0 }
    ]
  },
  {
    name: 'validate_output_phase_lock.py',
    relativePath: 'validators/validate_output_phase_lock.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/bad/bad_output_phase_not_started_after_completion.json',
      'validators/fixtures/gold/gold_route_state_resume_capsule.json',
      'validators/fixtures/bad/bad_text_output_phase_not_started_after_completion.md',
      'validators/fixtures/gold/gold_text_output_phase_started_after_completion.md'
    ],
    fixtureProbes: [
      { label: 'bad_output_phase_json', path: 'validators/fixtures/bad/bad_output_phase_not_started_after_completion.json', expectedExit: 1 },
      { label: 'gold_output_phase_json', path: 'validators/fixtures/gold/gold_route_state_resume_capsule.json', expectedExit: 0 },
      { label: 'bad_output_phase_text', path: 'validators/fixtures/bad/bad_text_output_phase_not_started_after_completion.md', expectedExit: 1 },
      { label: 'gold_output_phase_text', path: 'validators/fixtures/gold/gold_text_output_phase_started_after_completion.md', expectedExit: 0 }
    ]
  },
  {
    name: 'validate_dominant_failure_classifier.py',
    relativePath: 'validators/validate_dominant_failure_classifier.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/bad/bad_shallow_fake_pass_claims_68_reads.md',
      'validators/fixtures/gold/gold_script_reconstructed.md',
      'validators/fixtures/bad/bad_latest_antigravity_alias_fake_pass.md',
      'validators/fixtures/gold/gold_alias_claims_with_complete_evidence.md'
    ],
    fixtureProbes: [
      { label: 'bad_dominant_68_reads', path: 'validators/fixtures/bad/bad_shallow_fake_pass_claims_68_reads.md', expectedExit: 1 },
      { label: 'gold_dominant_script', path: 'validators/fixtures/gold/gold_script_reconstructed.md', expectedExit: 0 },
      { label: 'bad_dominant_alias_fake_pass', path: 'validators/fixtures/bad/bad_latest_antigravity_alias_fake_pass.md', expectedExit: 1 },
      { label: 'gold_dominant_alias_complete', path: 'validators/fixtures/gold/gold_alias_claims_with_complete_evidence.md', expectedExit: 0 }
    ]
  },
  {
    name: 'validate_tool_ledger_evidence.py',
    relativePath: 'validators/validate_tool_ledger_evidence.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/bad/bad_antigravity_truncated_export_pass_claims.md',
      'validators/fixtures/gold/gold_tool_ledger_with_concrete_file_reads.md'
    ],
    fixtureProbes: [
      { label: 'bad_truncated_export_pass_claims', path: 'validators/fixtures/bad/bad_antigravity_truncated_export_pass_claims.md', expectedExit: 1 },
      { label: 'gold_concrete_tool_ledger', path: 'validators/fixtures/gold/gold_tool_ledger_with_concrete_file_reads.md', expectedExit: 0 }
    ]
  },
  {
    name: 'validate_route_mode_contract.py',
    relativePath: 'validators/validate_route_mode_contract.py',
    args: [],
    fixturePaths: [
      'validators/fixtures/bad/bad_antigravity_standard_script_mode.md',
      'validators/fixtures/bad/bad_visual_generator_alias_unclassified.md',
      'validators/fixtures/bad/bad_route_mode_existing_path_wrong_slice.md',
      'validators/fixtures/gold/gold_script_only_route_mode.md',
      'validators/fixtures/gold/gold_visual_generation_draft_mode_alias_normalized.md'
    ],
    fixtureProbes: [
      { label: 'bad_standard_script_mode', path: 'validators/fixtures/bad/bad_antigravity_standard_script_mode.md', expectedExit: 1 },
      { label: 'bad_visual_generator_alias_unclassified', path: 'validators/fixtures/bad/bad_visual_generator_alias_unclassified.md', expectedExit: 1 },
      { label: 'bad_route_mode_existing_wrong_slice', path: 'validators/fixtures/bad/bad_route_mode_existing_path_wrong_slice.md', expectedExit: 1 },
      { label: 'gold_script_only_mode', path: 'validators/fixtures/gold/gold_script_only_route_mode.md', expectedExit: 0 },
      { label: 'gold_visual_generation_draft_mode', path: 'validators/fixtures/gold/gold_visual_generation_draft_mode_alias_normalized.md', expectedExit: 0 }
    ]
  },
  {
    name: 'validate_route_scope_telemetry_law.py',
    relativePath: 'validators/validate_route_scope_telemetry_law.py',
    args: [],
    fixturePaths: [
      'registries/route_manifests/script_generation.yaml',
      'registries/task_intent_routing_matrix.yaml',
      'validators/fixtures/bad/bad_route_scope_68_pass_authority.yaml',
      'validators/fixtures/gold/gold_route_scope_telemetry_only.yaml'
    ],
    fixtureProbes: [
      { label: 'bad_route_scope_68_pass_authority', path: 'validators/fixtures/bad/bad_route_scope_68_pass_authority.yaml', expectedExit: 1 },
      { label: 'gold_route_scope_telemetry_only', path: 'validators/fixtures/gold/gold_route_scope_telemetry_only.yaml', expectedExit: 0 }
    ]
  },
  {
    name: 'validate_active_skill_contamination.py',
    relativePath: 'validators/validate_active_skill_contamination.py',
    args: [],
    fixturePaths: [
      '.agents/skills',
      'validators/fixtures/bad/bad_active_skill_contaminated_script.md',
      'validators/fixtures/gold/gold_active_skill_clean.md'
    ],
    fixtureProbes: [
      { label: 'bad_active_skill_contaminated_script', path: 'validators/fixtures/bad/bad_active_skill_contaminated_script.md', expectedExit: 1 },
      { label: 'gold_active_skill_clean', path: 'validators/fixtures/gold/gold_active_skill_clean.md', expectedExit: 0 }
    ]
  }
];

function commandForPython(spec) {
  return ['python3', spec.relativePath].concat(spec.args || []);
}

function commandForPythonProbe(spec, probe) {
  return ['python3', spec.relativePath, probe.path];
}

function inspectPythonValidator(spec) {
  const validatorPath = path.join(repoRoot, spec.relativePath);
  const exists = fs.existsSync(validatorPath);
  const missingFixtures = (spec.fixturePaths || []).filter((fixturePath) => !fs.existsSync(path.join(repoRoot, fixturePath)));
  const hasFixtureBinding = exists && (spec.args || []).length > 0 || exists && (spec.fixturePaths || []).length > 0;
  const noFixtureBound = exists && !hasFixtureBinding;
  const ready = exists && !noFixtureBound && missingFixtures.length === 0;
  let status = 'MISSING';
  if (exists && ready) status = 'READY_FOR_EXECUTION';
  if (exists && noFixtureBound) status = 'NO_FIXTURE_BOUND';
  if (exists && missingFixtures.length > 0) status = 'NOT_READY_FOR_EXECUTION';
  return {
    ...spec,
    exists,
    status,
    fileStatus: exists ? 'EXISTS' : 'MISSING',
    bindingStatus: noFixtureBound ? 'NO_FIXTURE_BOUND' : ready ? 'FIXTURE_BOUND' : 'NOT_READY_FOR_EXECUTION',
    executionStatus: ready ? 'READY_FOR_EXECUTION' : 'NOT_READY_FOR_EXECUTION',
    missingFixtures,
    command: commandForPython(spec)
  };
}

function pythonInventory() {
  return pythonValidatorSpecs.map(inspectPythonValidator);
}

function printUsage() {
  console.log('Usage: node validators/run_all_validators.cjs [--list] [--dry-run] [--python-only] [--strict]');
  console.log('');
  console.log('--list         Show Node and Python validator inventory without execution.');
  console.log('--dry-run      Show what would execute without executing validators.');
  console.log('--python-only  Run or inventory Python validators only.');
  console.log('--strict       Treat missing Python validators or fixture bindings as blockers.');
}

function formatCommand(command) {
  return command.join(' ');
}

function printPythonInventory(inventory) {
  console.log('\nPython validator inventory');
  console.log('-'.repeat(70));
  inventory.forEach((item) => {
    console.log(
      `${item.name}: ${item.fileStatus} ${item.bindingStatus} ${item.executionStatus} command="${formatCommand(item.command)}"`
    );
    if (item.missingFixtures.length > 0) {
      console.log(`   missing_fixtures=${item.missingFixtures.join(',')}`);
    }
  });
}

function printNodeInventory() {
  console.log('\nNode validator inventory');
  console.log('-'.repeat(70));
  validators.forEach((spec) => console.log(`${spec.name}: DISCOVERED`));
  console.log('RuntimeValidator: DISCOVERED_OPTIONAL');
  console.log('DossierRuntimeCheck: DISCOVERED');
}

function runPythonValidators(inventory) {
  const results = [];
  inventory.forEach((item, idx) => {
    if (!item.exists) {
      results.push({ name: item.name, status: 'MISSING', executed: false, code: null, errors: 0, warnings: 0 });
      return;
    }
    if (item.executionStatus !== 'READY_FOR_EXECUTION') {
      results.push({ name: item.name, status: 'NO_FIXTURE_BINDING', executed: false, code: null, errors: 0, warnings: 0 });
      return;
    }
    console.log(`\n[PY ${idx + 1}/${inventory.length}] ${item.name}`);
    console.log(`   command=${formatCommand(item.command)}`);
    const run = spawnSync(item.command[0], item.command.slice(1), {
      cwd: repoRoot,
      encoding: 'utf8',
      maxBuffer: 1024 * 1024 * 16
    });
    const stdout = (run.stdout || '').trim();
    const stderr = (run.stderr || '').trim();
    if (stdout) {
      console.log('   stdout:');
      stdout.split('\n').slice(0, 40).forEach((line) => console.log(`      ${line}`));
      if (stdout.split('\n').length > 40) console.log('      ... stdout truncated by runner display');
    }
    if (stderr) {
      console.log('   stderr:');
      stderr.split('\n').slice(0, 40).forEach((line) => console.log(`      ${line}`));
      if (stderr.split('\n').length > 40) console.log('      ... stderr truncated by runner display');
    }
    const code = typeof run.status === 'number' ? run.status : 1;
    const status = code === 0 ? 'EXECUTED_PASS' : 'EXECUTED_FAIL';
    console.log(`   status=${status} exit_code=${code}`);
    let fixtureProbesExecuted = 0;
    let fixtureProbeFailures = 0;
    (item.fixtureProbes || []).forEach((probe) => {
      const probeCommand = commandForPythonProbe(item, probe);
      const probeRun = spawnSync(probeCommand[0], probeCommand.slice(1), {
        cwd: repoRoot,
        encoding: 'utf8',
        maxBuffer: 1024 * 1024 * 16
      });
      const probeCode = typeof probeRun.status === 'number' ? probeRun.status : 1;
      const probePassed = probeCode === probe.expectedExit;
      fixtureProbesExecuted += 1;
      if (!probePassed) fixtureProbeFailures += 1;
      console.log(
        `   fixture_probe=${probe.label} path=${probe.path} expected_exit=${probe.expectedExit} actual_exit=${probeCode} status=${probePassed ? 'PROBE_PASS' : 'PROBE_FAIL'}`
      );
    });
    results.push({
      name: item.name,
      status,
      executed: true,
      code,
      errors: (code === 0 ? 0 : 1) + fixtureProbeFailures,
      warnings: 0,
      fixtureProbesExecuted,
      fixtureProbeFailures
    });
  });
  return results;
}

// Optional runtime validator (uses different shape; treat exceptions as warnings)
function tryRuntimeValidator() {
  try {
    const Cls = require('./runtime_validator.cjs');
    if (typeof Cls === 'function') {
      const inst = new Cls();
      if (typeof inst.runFullCheck === 'function') {
        return inst.runFullCheck();
      }
    }
    return null;
  } catch (error) {
    return { overall_valid: true, findings: [{ severity: 'warning', code: 'RUNTIME_VALIDATOR', message: `optional check skipped: ${error.message}` }] };
  }
}

// Dossier runtime model check
function dossierRuntimeCheck() {
  const dossierDir = path.join(repoRoot, 'dossiers');
  const findings = [];
  if (!fs.existsSync(dossierDir)) {
    return { overall_valid: true, findings: [{ severity: 'warning', code: 'DOSSIER_DIR', message: 'dossiers/ not present' }] };
  }
  const files = fs.readdirSync(dossierDir).filter((f) => f.endsWith('.json'));
  files.forEach((file) => {
    try {
      const d = JSON.parse(fs.readFileSync(path.join(dossierDir, file), 'utf8'));
      if (!d.dossier_id) findings.push({ severity: 'error', code: 'DOSSIER_RUNTIME', message: `${file}: missing dossier_id` });
      if (typeof d._version !== 'number') findings.push({ severity: 'error', code: 'DOSSIER_RUNTIME', message: `${file}: missing/invalid _version` });
      if (!d._created_at) findings.push({ severity: 'error', code: 'DOSSIER_RUNTIME', message: `${file}: missing _created_at` });
      if (!Array.isArray(d._audit_trail)) findings.push({ severity: 'error', code: 'DOSSIER_RUNTIME', message: `${file}: missing _audit_trail array` });
    } catch (error) {
      findings.push({ severity: 'error', code: 'DOSSIER_PARSE', message: `${file}: ${error.message}` });
    }
  });
  const errors = findings.filter((f) => f.severity === 'error');
  return { overall_valid: errors.length === 0, findings };
}

console.log('Shadow Creator OS Phase-1: Substantive Validation');
console.log('='.repeat(70));

const results = [];
const pythonInspect = pythonInventory();

if (helpMode) {
  printUsage();
  process.exit(0);
}

if (listMode || dryRun) {
  if (!pythonOnly) printNodeInventory();
  printPythonInventory(pythonInspect);
}

const shouldExecute = !listMode && !dryRun;
const shouldRunNode = shouldExecute && !pythonOnly;
const shouldRunPython = shouldExecute;
let nodeValidatorsExecuted = 0;
let pythonResults = [];

if (shouldRunNode) {
  validators.forEach((spec, idx) => {
    console.log(`\n[${idx + 1}/${validators.length + 2}] ${spec.name}`);
    try {
      const Cls = spec.load();
      const result = spec.run(Cls);
      const errCount = (result.findings || []).filter((f) => f.severity === 'error').length;
      const warnCount = (result.findings || []).filter((f) => f.severity === 'warning').length;
      results.push({ name: spec.name, valid: !!result.overall_valid, errors: errCount, warnings: warnCount, findings: result.findings || [] });
      nodeValidatorsExecuted += 1;
      console.log(`   overall_valid=${result.overall_valid} errors=${errCount} warnings=${warnCount}`);
    } catch (error) {
      results.push({ name: spec.name, valid: false, errors: 1, warnings: 0, findings: [{ severity: 'error', code: 'VALIDATOR_CRASH', message: error.message }] });
      nodeValidatorsExecuted += 1;
      console.log(`   CRASHED: ${error.message}`);
    }
  });

  console.log(`\n[${validators.length + 1}/${validators.length + 2}] RuntimeValidator (optional)`);
  const runtimeResult = tryRuntimeValidator();
  if (runtimeResult) {
    const errCount = (runtimeResult.findings || []).filter((f) => f.severity === 'error').length;
    const warnCount = (runtimeResult.findings || []).filter((f) => f.severity === 'warning').length;
    results.push({ name: 'RuntimeValidator', valid: !!runtimeResult.overall_valid, errors: errCount, warnings: warnCount, findings: runtimeResult.findings || [] });
    nodeValidatorsExecuted += 1;
    console.log(`   overall_valid=${runtimeResult.overall_valid} errors=${errCount} warnings=${warnCount}`);
  } else {
    console.log('   skipped (no runFullCheck export)');
  }

  console.log(`\n[${validators.length + 2}/${validators.length + 2}] DossierRuntimeCheck`);
  const drc = dossierRuntimeCheck();
  const drcErrCount = drc.findings.filter((f) => f.severity === 'error').length;
  const drcWarnCount = drc.findings.filter((f) => f.severity === 'warning').length;
  results.push({ name: 'DossierRuntimeCheck', valid: drc.overall_valid, errors: drcErrCount, warnings: drcWarnCount, findings: drc.findings });
  nodeValidatorsExecuted += 1;
  console.log(`   overall_valid=${drc.overall_valid} errors=${drcErrCount} warnings=${drcWarnCount}`);
}

if (shouldRunPython) {
  pythonResults = runPythonValidators(pythonInspect);
}

// Final summary
console.log('\n' + '='.repeat(70));
console.log('SUBSTANTIVE VALIDATION SUMMARY');
console.log('='.repeat(70));

let allPassed = true;
let totalErrors = 0;
let totalWarnings = 0;
results.forEach((r) => {
  const tag = r.valid ? 'PASS' : 'FAIL';
  console.log(`[${tag}] ${r.name.padEnd(24)} errors=${r.errors} warnings=${r.warnings}`);
  if (!r.valid) allPassed = false;
  totalErrors += r.errors;
  totalWarnings += r.warnings;
});

const pythonFailures = pythonResults.filter((r) => r.executed && r.errors > 0);
pythonFailures.forEach((r) => {
  allPassed = false;
  totalErrors += r.errors;
  console.log(`[FAIL] ${r.name.padEnd(24)} errors=${r.errors} warnings=0`);
});

// Show first few error findings for context
const errorFindings = results.flatMap((r) => r.findings.filter((f) => f.severity === 'error').map((f) => ({ source: r.name, ...f })));
if (errorFindings.length > 0) {
  console.log('\nTop errors:');
  errorFindings.slice(0, 15).forEach((f) => console.log(`  [${f.source}] ${f.code}: ${f.message}`));
  if (errorFindings.length > 15) {
    console.log(`  ... and ${errorFindings.length - 15} more error findings`);
  }
}

const pythonExisting = pythonInspect.filter((item) => item.exists).length;
const pythonMissing = pythonInspect.filter((item) => !item.exists).length;
const pythonNoFixtureBinding = pythonInspect.filter((item) => item.exists && item.executionStatus !== 'READY_FOR_EXECUTION').length;
const pythonExecuted = pythonResults.filter((item) => item.executed).length;
const pythonFixtureProbesExecuted = pythonResults.reduce((total, item) => total + (item.fixtureProbesExecuted || 0), 0);
const pythonFixtureProbeFailures = pythonResults.reduce((total, item) => total + (item.fixtureProbeFailures || 0), 0);
const strictBlockers = strictMode ? pythonMissing + pythonNoFixtureBinding : 0;
const validationFailures = totalErrors;
const validationBlockers = validationFailures + strictBlockers;
let finalStatus = 'PASS';
if (validationBlockers > 0) {
  finalStatus = 'BLOCKED';
} else if (listMode || dryRun) {
  finalStatus = 'PARTIAL';
}

console.log('='.repeat(70));
console.log(`OVERALL: ${allPassed ? 'PASS' : 'FAIL'} | total_errors=${totalErrors} total_warnings=${totalWarnings}`);
console.log('='.repeat(70));
console.log('VALIDATOR_RUNNER_SUMMARY');
console.log(`node_validators_discovered=${validators.length + 2}`);
console.log(`node_validators_executed=${nodeValidatorsExecuted}`);
console.log(`python_validators_expected=${pythonValidatorSpecs.length}`);
console.log(`python_validators_existing=${pythonExisting}`);
console.log(`python_validators_missing=${pythonMissing}`);
console.log(`python_validators_executed=${pythonExecuted}`);
console.log(`python_validators_no_fixture_binding=${pythonNoFixtureBinding}`);
console.log(`python_fixture_probes_executed=${pythonFixtureProbesExecuted}`);
console.log(`python_fixture_probe_failures=${pythonFixtureProbeFailures}`);
console.log(`strict_mode=${strictMode}`);
console.log(`validation_failures=${validationFailures}`);
console.log(`validation_blockers=${validationBlockers}`);
console.log(`final_status=${finalStatus}`);

if (finalStatus === 'PASS') {
  process.exit(0);
}
if (finalStatus === 'PARTIAL' && (listMode || dryRun)) {
  process.exit(0);
}
process.exit(1);
