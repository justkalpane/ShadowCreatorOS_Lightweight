from __future__ import annotations

from lib.batch3_validator_core import (
    err,
    expect_array_min,
    expect_bool,
    expect_const,
    expect_enum,
    expect_number_range,
    expect_pattern,
    get_in,
    is_nonempty,
    require_fields,
)


def validate_evidence_bundle(data, errors, warnings):
    require_fields(data, errors, [
        "evidence_bundle_id", "contract_version", "route_id", "bundle_status",
        "artifact_paths", "validator_statuses", "pass_claims", "human_review_status",
        "proof_bundle_path",
    ])
    if not is_nonempty(data.get("evidence_bundle_id")):
        err(errors, "MISSING_EVIDENCE_BUNDLE")
    expect_pattern(data, errors, "evidence_bundle_id", r"^EVB-[A-Za-z0-9_-]+-[0-9]{8}-[A-Za-z0-9_-]+$")
    expect_enum(data, errors, "bundle_status", ["DRAFT", "COMPLETE", "BLOCKED"])
    expect_array_min(data, errors, "artifact_paths", 1)
    expect_array_min(data, errors, "validator_statuses", 1)
    expect_array_min(data, errors, "pass_claims", 1)
    forbidden = {
        "ffprobe_only": "FAKE_PASS_FFPROBE_ONLY",
        "file_exists_only": "FAKE_PASS_FILE_EXISTS_ONLY",
        "exit_code_0_only": "FAKE_PASS_EXIT_CODE_ONLY",
        "contract_exists_only": "FAKE_PASS_CONTRACT_EXISTS_ONLY",
    }
    for idx, claim in enumerate(data.get("pass_claims", [])):
        reason = claim.get("pass_reason")
        if reason in forbidden:
            err(errors, forbidden[reason], f"pass_claims[{idx}]")
        if reason == "keyword_hit_only":
            err(errors, "forbidden_pass_reason", f"pass_claims[{idx}]")
        if claim.get("status") == "PASS" and claim.get("validator_status") != "PASS":
            err(errors, "pass_without_validator_pass", f"pass_claims[{idx}]")
        if not claim.get("artifact_paths"):
            err(errors, "missing_claim_artifacts", f"pass_claims[{idx}]")


def validate_no_fake_pass_gate(data, errors, warnings):
    validate_evidence_bundle(data, errors, warnings)
    require_fields(data, errors, [
        "pass_reason", "claim_context", "route_state_capsule_id", "audit_event_id",
    ])
    top_level_reason = data.get("pass_reason")
    if not is_nonempty(top_level_reason):
        err(errors, "missing_required_field", "pass_reason")
    claim_reasons = [
        claim.get("pass_reason")
        for claim in data.get("pass_claims", [])
        if is_nonempty(claim.get("pass_reason"))
    ]
    if claim_reasons and top_level_reason != claim_reasons[0]:
        err(errors, "const_mismatch", f"pass_reason expected={claim_reasons[0]!r} actual={top_level_reason!r}")
    forbidden = {
        "ffprobe_only": "FAKE_PASS_FFPROBE_ONLY",
        "file_exists_only": "FAKE_PASS_FILE_EXISTS_ONLY",
        "exit_code_0_only": "FAKE_PASS_EXIT_CODE_ONLY",
        "contract_exists_only": "FAKE_PASS_CONTRACT_EXISTS_ONLY",
        "keyword_hit_only": "forbidden_pass_reason",
        "route_state_truth_without_evidence_bundle": "FAKE_PASS_ROUTE_STATE_TRUTH_WITHOUT_EVIDENCE_BUNDLE",
        "route_state_truth_without_audit_event": "FAKE_PASS_ROUTE_STATE_TRUTH_WITHOUT_AUDIT_EVENT",
        "route_unlock_without_validator_pass": "FAKE_PASS_ROUTE_UNLOCK_WITHOUT_VALIDATOR_PASS",
    }
    if top_level_reason in forbidden:
        err(errors, forbidden[top_level_reason], "pass_reason")
    for idx, claim in enumerate(data.get("pass_claims", [])):
        reason = claim.get("pass_reason")
        if reason in forbidden:
            err(errors, forbidden[reason], f"pass_claims[{idx}]")


def validate_pilot_cut_gate(data, errors, warnings):
    validate_pilot_cut_validation_packet(data, errors, warnings)


def validate_audio_authorization_gate(data, errors, warnings):
    validate_audio_authorization_packet(data, errors, warnings)


def validate_davinci_handoff_gate(data, errors, warnings):
    validate_davinci_handoff_packet(data, errors, warnings)


def validate_route_state_capsule(data, errors, warnings):
    require_fields(data, errors, [
        "route_state_capsule_id", "route_id", "route_manifest_path", "route_manifest_hash",
        "task_intent", "task_mode", "output_mode", "phase", "last_completed_lock",
        "next_required_lock", "evidence_scope", "files_read", "file_hashes",
        "selected_directors", "selected_agents", "selected_subagents", "selected_skills",
        "selected_subskills", "dependencies_complete", "output_phase_started",
        "read_ledger", "consumed_files_ledger", "validator_status_ledger",
        "pass_fail_ledger", "blocked_state", "unlocked_state", "evidence_bundle_id",
        "proof_bundle_path", "human_review_status",
    ])
    if not is_nonempty(data.get("route_state_capsule_id")):
        err(errors, "MISSING_ROUTE_STATE_CAPSULE")
    expect_pattern(data, errors, "route_state_capsule_id", r"^RSC-[A-Za-z0-9_-]+$")
    expect_pattern(data, errors, "route_manifest_hash", r"^sha256:[a-f0-9]{64}$")
    expect_enum(data, errors, "evidence_scope", ["current_cycle", "previous_cycle_with_step_reference", "persisted_route_state_with_hash"])
    expect_array_min(data, errors, "files_read", 1)
    expect_array_min(data, errors, "read_ledger", 1)
    expect_array_min(data, errors, "consumed_files_ledger", 1)
    expect_array_min(data, errors, "validator_status_ledger", 1)
    expect_array_min(data, errors, "pass_fail_ledger", 1)
    if data.get("compaction_detected") and data.get("evidence_scope") != "persisted_route_state_with_hash":
        err(errors, "compaction_requires_persisted_scope")
    if data.get("final_output_allowed") and not data.get("dependencies_complete"):
        err(errors, "final_output_without_dependencies_complete")
    if data.get("final_output_allowed") and not data.get("output_phase_started"):
        err(errors, "final_output_without_output_phase")
    if data.get("unlocked_state") == "full_render" and data.get("blocked_state") != "ready_for_patch":
        err(errors, "full_render_unlock_without_ready_for_patch")
    file_hashes = data.get("file_hashes", {})
    for item in data.get("files_read", []):
        if item not in file_hashes:
            err(errors, "missing_file_hash", item)
    for idx, row in enumerate(data.get("read_ledger", [])):
        if row.get("semantic_use_status") not in {"USED", "NOT_USED", "NOT_APPLICABLE", "NOT_PROVEN"}:
            err(errors, "invalid_semantic_use_status", f"read_ledger[{idx}]")


def validate_patch_transaction(data, errors, warnings):
    require_fields(data, errors, [
        "batch_id", "repo", "repo_type", "precheck_status", "backup_status",
        "files_created", "files_modified", "forbidden_touched", "tests_run",
        "proof_bundle_path", "next_batch_allowed"
    ])
    expect_enum(data, errors, "repo_type", ["git_repo", "non_git_repo"])
    expect_enum(data, errors, "precheck_status", ["PASS", "FAIL"])
    expect_enum(data, errors, "backup_status", ["PASS", "FAIL", "NOT_REQUIRED"])
    expect_bool(data, errors, "forbidden_touched")
    expect_bool(data, errors, "next_batch_allowed")
    expect_array_min(data, errors, "tests_run", 1)
    if data.get("forbidden_touched") is True and data.get("next_batch_allowed") is not False:
        err(errors, "forbidden_touch_must_block_next_batch")
    if data.get("repo_type") == "non_git_repo" and data.get("backup_status") != "PASS":
        err(errors, "non_git_repo_requires_backup_pass")


def validate_bridge_job_packet(data, errors, warnings):
    require_fields(data, errors, [
        "job_id", "route_id", "route_state_capsule_id", "media_task_type",
        "allowed_execution", "blocked_execution", "required_inputs", "required_proofs",
        "provider_execution_allowed", "return_contract"
    ])
    expect_const(data, errors, "route_id", "MEDIA_FACTORY_HANDOFF")
    if data.get("provider_execution_allowed") is not False:
        err(errors, "PROVIDER_WITHOUT_APPROVAL")
    expect_const(data, errors, "provider_execution_allowed", False)
    expect_array_min(data, errors, "allowed_execution", 1)
    expect_array_min(data, errors, "blocked_execution", 4)
    blocked = set(data.get("blocked_execution", []))
    for item in ["full_127s", "audio", "provider", "davinci"]:
        if item not in blocked:
            err(errors, "missing_blocked_execution", item)
    if data.get("media_task_type") == "pilot_cut" and data.get("cut_id") != "C04a":
        err(errors, "pilot_cut_requires_c04a")
    return_contract = data.get("return_contract", {})
    if return_contract.get("production_pass_allowed") is not False:
        err(errors, "production_pass_allowed_must_be_false")


def validate_visual_media_plan_row(data, errors, warnings):
    require_fields(data, errors, [
        "scene_id", "timecode", "script_line", "scene_intent", "visual_role", "method",
        "cost_level", "provider_lane", "proof_requirement", "reasoning", "visual_dna_fields_present",
        "visual_dna_fields", "camera_motion_type", "depth_requirement", "lineart_requirement",
        "ipadapter_requirement", "openpose_requirement", "child_shot_max_seconds", "child_microshot_grid",
        "true_camera_motion_required",
        "beat_timing_dynamic", "generic_slideshow_prevented", "provider_execution_claimed",
        "local_engine_output_claimed", "storyboard_not_cinematic_broll"
    ])
    expect_const(data, errors, "visual_dna_fields_present", True)
    expect_const(data, errors, "beat_timing_dynamic", True)
    expect_const(data, errors, "generic_slideshow_prevented", True)
    expect_const(data, errors, "provider_execution_claimed", False)
    expect_const(data, errors, "local_engine_output_claimed", False)
    expect_number_range(data, errors, "child_shot_max_seconds", 0, 4)
    dna = data.get("visual_dna_fields", {})
    for field in [
        "subject", "environment", "camera_framing", "lens_focal_logic", "lighting_setup",
        "emotional_tone", "color_palette", "cinematic_delivery_standard", "style_lock",
        "movement_intent", "negative_prompt", "drift_prevention", "continuity_constraints",
        "brand_persona_consistency", "safety_real_person_handling", "tool_targets",
        "tool_specific_translation_readiness"
    ]:
        if not is_nonempty(dna.get(field)):
            err(errors, "missing_visual_dna_field", field)
    if dna.get("cinematic_delivery_standard") != "Rec.709":
        err(errors, "cinematic_delivery_standard_must_be_rec709")
    if data.get("method") != "CINEMATIC_BROLL_VIDEO" and data.get("storyboard_not_cinematic_broll") is not True:
        err(errors, "non_cinematic_storyboard_flag_required")
    grid = data.get("child_microshot_grid")
    if not isinstance(grid, list) or not grid:
        err(errors, "child_microshot_grid_missing")
    else:
        parent_duration = get_in(data, "timecode.duration_seconds")
        if isinstance(parent_duration, (int, float)) and parent_duration > 12 and len(grid) < 3:
            err(errors, "child_microshot_grid_too_sparse_for_long_scene")
        for idx, child in enumerate(grid):
            if not isinstance(child, dict):
                err(errors, "child_microshot_grid_row_invalid", f"child_microshot_grid[{idx}]")
                continue
            if not is_nonempty(child.get("child_shot_id")) or not is_nonempty(child.get("child_shot_method")):
                err(errors, "child_microshot_grid_row_missing", f"child_microshot_grid[{idx}]")
            if child.get("status") not in {"PASS", "NEEDS_CONFIRMATION", "NEEDS_USER_APPROVAL"}:
                err(errors, "child_microshot_grid_row_status_invalid", f"child_microshot_grid[{idx}]")
            if not isinstance(child.get("child_shot_duration_seconds"), (int, float)) or child.get("child_shot_duration_seconds") > 4:
                err(errors, "child_microshot_child_over_4_seconds", f"child_microshot_grid[{idx}]")


def validate_final_visual_media_generation_draft(data, errors, warnings):
    require_fields(data, errors, [
        "packet_id", "route_id", "route_state_capsule_id", "evidence_bundle_id",
        "bridge_job_packet_id", "execution_lane", "visual_rows", "scene_sync_required",
        "asset_inventory_required", "source_vs_render_required", "visual_qa_required",
        "contact_sheet_required", "pilot_required_before_batch", "tools_connectors_plugins_assessment",
        "provider_execution_allowed", "audio_allowed", "davinci_allowed"
    ])
    if not is_nonempty(data.get("evidence_bundle_id")):
        err(errors, "MISSING_EVIDENCE_BUNDLE")
    expect_const(data, errors, "route_id", "MEDIA_FACTORY_HANDOFF")
    expect_const(data, errors, "scene_sync_required", True)
    expect_const(data, errors, "asset_inventory_required", True)
    expect_const(data, errors, "source_vs_render_required", True)
    expect_const(data, errors, "visual_qa_required", True)
    expect_const(data, errors, "contact_sheet_required", True)
    expect_const(data, errors, "pilot_required_before_batch", True)
    if data.get("provider_execution_allowed") is not False:
        err(errors, "PROVIDER_WITHOUT_APPROVAL")
    if data.get("audio_allowed") is not False:
        err(errors, "AUDIO_BEFORE_VISUAL_ACCEPTANCE")
    if data.get("davinci_allowed") is not False:
        err(errors, "DAVINCI_BEFORE_ACCEPTANCE")
    assessment = data.get("tools_connectors_plugins_assessment")
    if not isinstance(assessment, dict):
        err(errors, "MISSING_TOOLS_CONNECTORS_PLUGINS_ASSESSMENT")
    else:
        if assessment.get("item_name") != "HyperFrames CLI (Local)":
            err(errors, "HYPERFRAMES_CONNECTOR_ITEM_NAME_MISMATCH")
        if assessment.get("item_type") != "provider":
            err(errors, "HYPERFRAMES_CONNECTOR_ITEM_TYPE_MISMATCH")
        if assessment.get("source_path") != "registries/provider_registry.yaml#provider_id=hyperframes_cli_local":
            err(errors, "HYPERFRAMES_CONNECTOR_SOURCE_PATH_MISMATCH")
        if assessment.get("runtime_status") != "ACTIVE":
            err(errors, "HYPERFRAMES_CONNECTOR_RUNTIME_STATUS_MISMATCH")
        if assessment.get("required_for_task") is not True:
            err(errors, "HYPERFRAMES_CONNECTOR_REQUIRED_FOR_TASK_FALSE")
        if assessment.get("approval_required") is not False:
            err(errors, "HYPERFRAMES_CONNECTOR_APPROVAL_REQUIRED_TRUE")
        if assessment.get("execution_allowed_now") is not True:
            err(errors, "HYPERFRAMES_CONNECTOR_EXECUTION_ALLOWED_NOW_FALSE")
        if not is_nonempty(assessment.get("notes")):
            err(errors, "HYPERFRAMES_CONNECTOR_NOTES_MISSING")
    expect_const(data, errors, "provider_execution_allowed", False)
    expect_const(data, errors, "audio_allowed", False)
    expect_const(data, errors, "davinci_allowed", False)
    expect_array_min(data, errors, "visual_rows", 1)


def validate_depth_map_packet(data, errors, warnings):
    require_fields(data, errors, [
        "scene_id", "base_image_path", "base_image_sha256", "depth_map_path",
        "depth_map_sha256", "dimensions", "dimension_match_required",
        "depth_normalization_method", "depth_normalization_range", "depth_inversion_policy",
        "depth_visual_preview_path", "depth_method", "support_only",
        "parallax_proof_required_downstream", "depth_not_used_as_blur_proof",
        "render_unlock_allowed"
    ])
    expect_const(data, errors, "dimension_match_required", True)
    expect_const(data, errors, "support_only", True)
    expect_const(data, errors, "parallax_proof_required_downstream", True)
    expect_const(data, errors, "depth_not_used_as_blur_proof", True)
    expect_const(data, errors, "render_unlock_allowed", False)
    method = data.get("depth_method")
    if method == "blur":
        err(errors, "DEPTH_METHOD_BLUR_FORBIDDEN")
    elif method == "boxblur":
        err(errors, "DEPTH_METHOD_BOXBLUR_FORBIDDEN")
    elif method == "maskedmerge_only":
        err(errors, "DEPTH_METHOD_MASKEDMERGE_ONLY_FORBIDDEN")
    expect_enum(data, errors, "depth_method", ["displace", "layered_parallax"])
    dims = data.get("dimensions", {})
    if dims.get("base_width") != dims.get("depth_width") or dims.get("base_height") != dims.get("depth_height"):
        err(errors, "dimension_mismatch")


def validate_ffmpeg_filtergraph_packet(data, errors, warnings):
    require_fields(data, errors, [
        "input_assets", "filtergraph_chain", "scale_method", "color_profile",
        "encode_profile", "concat_policy", "double_encode_detected",
        "filtergraph_dump_path", "command_log_path"
    ])
    if data.get("scale_method") != "lanczos":
        err(errors, "FFMPEG_MISSING_LANCZOS")
    if data.get("color_profile") != "bt709":
        err(errors, "FFMPEG_MISSING_BT709")
    if data.get("encode_profile") != "crf18_bt709_lanczos":
        err(errors, "FFMPEG_MISSING_CRF18")
    if not is_nonempty(data.get("filtergraph_dump_path")):
        err(errors, "FFMPEG_MISSING_FILTERGRAPH_DUMP")
    expect_const(data, errors, "scale_method", "lanczos")
    expect_const(data, errors, "color_profile", "bt709")
    expect_const(data, errors, "encode_profile", "crf18_bt709_lanczos")
    expect_const(data, errors, "concat_policy", "no_double_encode_concat")
    expect_const(data, errors, "double_encode_detected", False)
    expect_array_min(data, errors, "input_assets", 1)
    chain = data.get("filtergraph_chain", {})
    for field in ["depth_stage", "overlay_stage", "scale_stage", "color_stage", "encode_stage", "concat_stage"]:
        if field not in chain:
            err(errors, "missing_filtergraph_stage", field)
    if get_in(data, "filtergraph_chain.depth_stage.depth_proxy_method") not in {"none", "displace", "layered_parallax"}:
        err(errors, "invalid_depth_proxy_method")


def validate_hyperframes_payload(data, errors, warnings):
    require_fields(data, errors, [
        "overlay_path", "overlay_category", "overlay_purpose", "scene_relevance",
        "blend_mode", "alpha_mode", "opacity", "z_index", "timing",
        "safe_zone_coordinates", "subject_occlusion_limit", "visual_noise_limit",
        "scene_intent", "proof_frame_reference", "contact_sheet_frame_required",
        "random_overlay_prevented"
    ])
    if not is_nonempty(data.get("blend_mode")):
        err(errors, "HYPERFRAMES_MISSING_BLEND")
    if not is_nonempty(data.get("alpha_mode")):
        err(errors, "HYPERFRAMES_MISSING_ALPHA")
    expect_const(data, errors, "contact_sheet_frame_required", True)
    expect_const(data, errors, "random_overlay_prevented", True)
    expect_number_range(data, errors, "opacity", 0, 0.72)
    expect_number_range(data, errors, "subject_occlusion_limit", 0, 0.25)
    expect_number_range(data, errors, "visual_noise_limit", 0, 0.4)
    expect_enum(data, errors, "blend_mode", ["screen", "add", "normal"])
    expect_enum(data, errors, "alpha_mode", ["premultiplied", "straight"])


def validate_comfyui_workflow_payload(data, errors, warnings):
    require_fields(data, errors, [
        "workflow_id", "workflow_json_path", "node_graph_hash", "model_family", "model",
        "prompt", "negative_prompt", "sampler", "steps", "cfg", "seed", "width", "height",
        "timeout_seconds", "retry_policy", "downgrade_policy", "fallback_provider_policy",
        "failure_classification", "provider_execution_allowed"
    ])
    expect_const(data, errors, "provider_execution_allowed", False)
    expect_enum(data, errors, "failure_classification", [
        "none", "COMFY_TIMEOUT_300S", "COMFY_NO_OUTPUT_IMAGE", "COMFY_MISSING_WORKFLOW_JSON",
        "COMFY_HIRES_FIX_MISSING", "COMFY_OOM_OR_RESOURCE_LIMIT"
    ])
    if data.get("failure_classification") == "COMFY_TIMEOUT_300S" and is_nonempty(data.get("output_image_path")):
        err(errors, "COMFYUI_TIMEOUT_MARKED_PASS")
    if data.get("width") == 1920 and data.get("height") == 1080:
        if not get_in(data, "hires_fix.enabled"):
            err(errors, "native_1920_requires_hires_fix")
    if data.get("failure_classification") == "none" and not is_nonempty(data.get("output_image_path")):
        err(errors, "missing_output_image_path")
    if data.get("failure_classification") != "none" and is_nonempty(data.get("output_image_path")):
        err(errors, "failure_classification_cannot_coexist_with_output_image")


def validate_source_vs_render_packet(data, errors, warnings):
    if data.get("artifact_type") == "source_vs_render_support_ledger":
        require_fields(data, errors, [
            "job_id", "artifact_type", "created_from_existing_local_evidence_only",
            "providers_used", "renders_created", "n8n_used", "davinci_used",
            "approval_token_issued", "production_pass_allowed", "ready_for_pilot_execution",
            "source_artifacts", "render_artifacts", "comparison_artifacts",
            "contact_sheet_candidate", "contact_sheet_png_path", "render_anchor",
            "hashes", "pairs", "comparison_status", "validation_status",
            "stable_proof_bundle_paths", "notes",
        ])
        expect_const(data, errors, "artifact_type", "source_vs_render_support_ledger")
        expect_const(data, errors, "created_from_existing_local_evidence_only", True)
        expect_const(data, errors, "providers_used", False)
        expect_const(data, errors, "renders_created", False)
        expect_const(data, errors, "n8n_used", False)
        expect_const(data, errors, "davinci_used", False)
        expect_const(data, errors, "approval_token_issued", False)
        expect_const(data, errors, "production_pass_allowed", False)
        expect_const(data, errors, "ready_for_pilot_execution", False)
        expect_array_min(data, errors, "source_artifacts", 1)
        expect_array_min(data, errors, "render_artifacts", 1)
        expect_array_min(data, errors, "pairs", 1)
        expect_enum(data, errors, "comparison_status", ["COMPLETE", "PARTIAL", "BLOCKED"])
        if not is_nonempty(data.get("contact_sheet_candidate")):
            err(errors, "SOURCE_VS_RENDER_MISSING_ARTIFACTS", "contact_sheet_candidate")
        if not is_nonempty(data.get("contact_sheet_png_path")):
            err(errors, "SOURCE_VS_RENDER_MISSING_ARTIFACTS", "contact_sheet_png_path")
        if not is_nonempty(data.get("render_anchor")):
            err(errors, "SOURCE_VS_RENDER_MISSING_ARTIFACTS", "render_anchor")
        if not is_nonempty(data.get("validation_status")):
            err(errors, "missing_required_field", "validation_status")
        hashes = data.get("hashes", {})
        if not isinstance(hashes, dict) or len(hashes) == 0:
            err(errors, "SOURCE_VS_RENDER_MISSING_ARTIFACTS", "hashes")
        for path_key, hash_value in hashes.items():
            if not is_nonempty(path_key):
                err(errors, "missing_required_field", "hashes.<path>")
            if not isinstance(hash_value, str) or len(hash_value) != 64:
                err(errors, "missing_required_field", f"hashes[{path_key}]")
        stable_paths = data.get("stable_proof_bundle_paths", {})
        for field in ["source_vs_render_json", "contact_sheet_png", "source_render_report_md"]:
            if not is_nonempty(stable_paths.get(field)):
                err(errors, "missing_required_field", f"stable_proof_bundle_paths.{field}")
        for idx, pair in enumerate(data.get("pairs", [])):
            if not isinstance(pair, dict):
                err(errors, "missing_required_field", f"pairs[{idx}]")
                continue
            for field in ["pair_id", "source_path", "render_path", "source_sha256", "render_sha256", "status", "proof_reference"]:
                if not is_nonempty(pair.get(field)):
                    err(errors, "missing_required_field", f"pairs[{idx}].{field}")
            if pair.get("status") not in {"VERIFIED", "DUPLICATE_CONFIRMED", "DUPLICATE_RISK", "REJECTED"}:
                err(errors, "invalid_enum", f"pairs[{idx}].status")
        return
    require_fields(data, errors, [
        "source_frame", "rendered_frame", "diff_images", "quality_metrics", "thresholds",
        "human_review_required", "human_override_status", "auto_status",
        "source_vs_render_report_path"
    ])
    expect_const(data, errors, "human_review_required", True)
    if not data.get("diff_images"):
        err(errors, "SOURCE_VS_RENDER_MISSING_ARTIFACTS")
    expect_array_min(data, errors, "diff_images", 1)
    metrics = data.get("quality_metrics", {})
    for field in [
        "sharpness_delta", "edge_density_delta", "color_delta", "contrast_delta",
        "compression_artifact_flag", "blur_detection_score", "overlay_occlusion_flag",
        "parallax_visibility_flag", "subject_readability_score"
    ]:
        if field not in metrics:
            err(errors, "missing_quality_metric", field)
    thresholds = data.get("thresholds", {})
    for field in [
        "sharpness_delta_threshold", "edge_density_delta_threshold", "color_delta_threshold",
        "contrast_delta_threshold", "blur_detection_threshold", "minimum_subject_readability_score"
    ]:
        if field not in thresholds:
            err(errors, "missing_threshold", field)
    if data.get("human_override_status") == "approved":
        override = data.get("human_override") or {}
        if override.get("used") is not True or not all(is_nonempty(override.get(k)) for k in ["reviewer", "reason", "timestamp"]):
            err(errors, "approved_override_requires_full_override_payload")


def validate_visual_qa_acceptance_packet(data, errors, warnings):
    require_fields(data, errors, [
        "evidence_bundle_id", "contact_sheet_path", "source_vs_render_packet_path",
        "human_review_packet", "qa_status", "visual_qa_required", "contact_sheet_required",
        "source_vs_render_required", "human_review_required", "production_pass_allowed"
    ])
    if not is_nonempty(data.get("contact_sheet_path")):
        err(errors, "VISUAL_QA_MISSING_CONTACT_SHEET")
    human_review = data.get("human_review_packet") or {}
    if not is_nonempty(human_review):
        err(errors, "HUMAN_REVIEW_NOT_APPROVED")
    if data.get("qa_status") == "approved" and human_review.get("review_status") != "APPROVED":
        err(errors, "HUMAN_REVIEW_NOT_APPROVED")
    expect_const(data, errors, "visual_qa_required", True)
    expect_const(data, errors, "contact_sheet_required", True)
    expect_const(data, errors, "source_vs_render_required", True)
    expect_const(data, errors, "human_review_required", True)
    expect_const(data, errors, "production_pass_allowed", False)
    if data.get("qa_status") == "approved" and get_in(data, "human_review_packet.review_status") != "APPROVED":
        err(errors, "approved_qa_requires_approved_human_review")


def validate_pilot_cut_validation_packet(data, errors, warnings):
    require_fields(data, errors, [
        "pilot_cut_id", "reason_selected", "script_line", "visual_intent", "base_image_path",
        "base_image_sha256", "depth_map_path", "depth_map_sha256", "hyperframes_overlay_path",
        "hyperframes_overlay_sha256", "motion_profile", "depth_method",
        "ffmpeg_filtergraph_packet_path", "encode_profile", "contact_sheet_plan",
        "source_vs_render_frame_points", "human_review_packet", "full_render_unlock_allowed"
    ])
    if data.get("pilot_cut_id") != "C04a":
        err(errors, "PILOT_WRONG_CUT_ID")
    if data.get("full_render_unlock_allowed") is not False:
        err(errors, "FULL_RENDER_BEFORE_PILOT")
    expect_const(data, errors, "pilot_cut_id", "C04a")
    expect_const(data, errors, "encode_profile", "crf18_bt709_lanczos")
    expect_const(data, errors, "full_render_unlock_allowed", False)
    expect_array_min(data, errors, "source_vs_render_frame_points", 1)


def validate_audio_authorization_packet(data, errors, warnings):
    require_fields(data, errors, ["visual_acceptance_token", "audio_authorization_token"])
    if get_in(data, "visual_acceptance_token.status") != "active":
        err(errors, "AUDIO_BEFORE_VISUAL_ACCEPTANCE")
    expect_const(data, errors, "visual_acceptance_token.status", "active")
    expect_const(data, errors, "audio_authorization_token.status", "active")
    expect_enum(data, errors, "visual_acceptance_token.scope", ["visual_acceptance"])
    expect_enum(data, errors, "audio_authorization_token.scope", ["audio_sync", "audio_export"])


def validate_davinci_handoff_packet(data, errors, warnings):
    require_fields(data, errors, [
        "visual_acceptance_token", "davinci_handoff_token", "asset_registry_path",
        "visual_audio_package_status"
    ])
    if get_in(data, "visual_acceptance_token.status") != "active" or data.get("visual_audio_package_status") != "ready":
        err(errors, "DAVINCI_BEFORE_ACCEPTANCE")
    expect_const(data, errors, "visual_acceptance_token.status", "active")
    expect_const(data, errors, "davinci_handoff_token.status", "active")
    expect_const(data, errors, "visual_audio_package_status", "ready")
    expect_enum(data, errors, "davinci_handoff_token.scope", ["davinci_handoff"])


CONFIGS = {
    "evidence_bundle": {
        "banner": "EVIDENCE_BUNDLE",
        "validate": validate_evidence_bundle,
        "gold_fixtures": [("gold_evidence_bundle_complete", "validators/fixtures/gold/evidence_bundle_complete.json")],
        "bad_fixtures": [
            ("bad_missing_evidence_bundle_id", "validators/fixtures/bad/missing_evidence_bundle_id.json"),
            ("bad_pass_reason_ffprobe_only", "validators/fixtures/bad/pass_reason_ffprobe_only.json"),
            ("bad_pass_reason_file_exists_only", "validators/fixtures/bad/pass_reason_file_exists_only.json"),
            ("bad_pass_reason_exit_code_0_only", "validators/fixtures/bad/pass_reason_exit_code_0_only.json"),
            ("bad_pass_reason_contract_exists_only", "validators/fixtures/bad/pass_reason_contract_exists_only.json"),
        ],
    },
    "route_state_capsule": {
        "banner": "ROUTE_STATE_CAPSULE",
        "validate": validate_route_state_capsule,
        "gold_fixtures": [("gold_route_state_capsule_complete", "validators/fixtures/gold/route_state_capsule_complete.json")],
        "bad_fixtures": [("bad_missing_route_state_capsule", "validators/fixtures/bad/missing_route_state_capsule.json")],
    },
    "patch_transaction": {
        "banner": "PATCH_TRANSACTION",
        "validate": validate_patch_transaction,
        "gold_fixtures": [("gold_patch_transaction_clean", "validators/fixtures/gold/patch_transaction_clean.json")],
        "bad_fixtures": [("bad_patch_transaction_forbidden_touch", "validators/fixtures/bad/patch_transaction_forbidden_touch.json")],
    },
    "bridge_job_packet": {
        "banner": "BRIDGE_JOB_PACKET",
        "validate": validate_bridge_job_packet,
        "gold_fixtures": [("gold_bridge_job_packet_c04a", "validators/fixtures/gold/bridge_job_packet_c04a.json")],
        "bad_fixtures": [("bad_provider_execution_without_approval", "validators/fixtures/bad/provider_execution_without_approval.json")],
    },
    "visual_media_plan_row": {
        "banner": "VISUAL_MEDIA_PLAN_ROW",
        "validate": validate_visual_media_plan_row,
        "gold_fixtures": [("gold_visual_media_plan_row_complete", "validators/fixtures/gold/visual_media_plan_row_complete.json")],
        "bad_fixtures": [
            ("bad_generic_slideshow_pass", "validators/fixtures/bad/generic_slideshow_pass.json"),
            ("bad_visual_plan_missing_15_dna_fields", "validators/fixtures/bad/visual_plan_missing_15_dna_fields.json"),
            ("bad_visual_plan_child_shot_over_4_seconds", "validators/fixtures/bad/visual_plan_child_shot_over_4_seconds.json"),
        ],
    },
    "final_visual_media_generation_draft": {
        "banner": "FINAL_VISUAL_MEDIA_GENERATION_DRAFT",
        "validate": validate_final_visual_media_generation_draft,
        "gold_fixtures": [("gold_final_visual_generation_draft_complete", "validators/fixtures/gold/final_visual_generation_draft_complete.json")],
        "bad_fixtures": [
            ("bad_source_vs_render_required_false", "validators/fixtures/bad/source_vs_render_required_false.json"),
            ("bad_visual_qa_required_false", "validators/fixtures/bad/visual_qa_required_false.json"),
            ("bad_contact_sheet_required_false", "validators/fixtures/bad/contact_sheet_required_false.json"),
            ("bad_pilot_required_before_batch_false", "validators/fixtures/bad/pilot_required_before_batch_false.json"),
            ("bad_connector_assessment_missing", "validators/fixtures/bad/final_visual_generation_draft_missing_connector_assessment.json"),
        ],
    },
    "depth_map_packet": {
        "banner": "DEPTH_MAP_PACKET",
        "validate": validate_depth_map_packet,
        "gold_fixtures": [("gold_depth_map_packet_valid", "validators/fixtures/gold/depth_map_packet_valid.json")],
        "bad_fixtures": [
            ("bad_depth_method_blur", "validators/fixtures/bad/depth_method_blur.json"),
            ("bad_depth_method_boxblur", "validators/fixtures/bad/depth_method_boxblur.json"),
            ("bad_depth_method_maskedmerge_only", "validators/fixtures/bad/depth_method_maskedmerge_only.json"),
            ("bad_depth_map_exists_only_pass", "validators/fixtures/bad/depth_map_exists_only_pass.json"),
        ],
    },
    "ffmpeg_filtergraph_packet": {
        "banner": "FFMPEG_FILTERGRAPH_PACKET",
        "validate": validate_ffmpeg_filtergraph_packet,
        "gold_fixtures": [("gold_ffmpeg_filtergraph_packet_valid", "validators/fixtures/gold/ffmpeg_filtergraph_packet_valid.json")],
        "bad_fixtures": [
            ("bad_ffmpeg_missing_lanczos", "validators/fixtures/bad/ffmpeg_missing_lanczos.json"),
            ("bad_ffmpeg_missing_crf18", "validators/fixtures/bad/ffmpeg_missing_crf18.json"),
            ("bad_ffmpeg_missing_bt709", "validators/fixtures/bad/ffmpeg_missing_bt709.json"),
            ("bad_ffmpeg_missing_filtergraph_dump", "validators/fixtures/bad/ffmpeg_missing_filtergraph_dump.json"),
            ("bad_hidden_double_encode", "validators/fixtures/bad/hidden_double_encode.json"),
        ],
    },
    "hyperframes_payload": {
        "banner": "HYPERFRAMES_PAYLOAD",
        "validate": validate_hyperframes_payload,
        "gold_fixtures": [("gold_hyperframes_payload_valid", "validators/fixtures/gold/hyperframes_payload_valid.json")],
        "bad_fixtures": [
            ("bad_hyperframes_missing_blend_mode", "validators/fixtures/bad/hyperframes_missing_blend_mode.json"),
            ("bad_hyperframes_missing_alpha_mode", "validators/fixtures/bad/hyperframes_missing_alpha_mode.json"),
            ("bad_hyperframes_subject_occlusion", "validators/fixtures/bad/hyperframes_subject_occlusion.json"),
            ("bad_hyperframes_random_overlay", "validators/fixtures/bad/hyperframes_random_overlay.json"),
        ],
    },
    "comfyui_payload": {
        "banner": "COMFYUI_PAYLOAD",
        "validate": validate_comfyui_workflow_payload,
        "gold_fixtures": [("gold_comfyui_payload_with_hires_fix", "validators/fixtures/gold/comfyui_payload_with_hires_fix.json")],
        "bad_fixtures": [
            ("bad_comfyui_timeout_marked_pass", "validators/fixtures/bad/comfyui_timeout_marked_pass.json"),
            ("bad_comfyui_missing_workflow_json", "validators/fixtures/bad/comfyui_missing_workflow_json.json"),
            ("bad_comfyui_missing_node_graph_hash", "validators/fixtures/bad/comfyui_missing_node_graph_hash.json"),
            ("bad_comfyui_native_1920_no_hires", "validators/fixtures/bad/comfyui_native_1920_no_hires.json"),
        ],
    },
    "source_vs_render_packet": {
        "banner": "SOURCE_VS_RENDER_PACKET",
        "validate": validate_source_vs_render_packet,
        "gold_fixtures": [("gold_source_vs_render_valid", "validators/fixtures/gold/source_vs_render_valid.json")],
        "bad_fixtures": [
            ("bad_source_vs_render_missing_diff", "validators/fixtures/bad/source_vs_render_missing_diff.json"),
            ("bad_source_vs_render_missing_thresholds", "validators/fixtures/bad/source_vs_render_missing_thresholds.json"),
        ],
    },
    "visual_qa_acceptance": {
        "banner": "VISUAL_QA_ACCEPTANCE",
        "validate": validate_visual_qa_acceptance_packet,
        "gold_fixtures": [("gold_visual_qa_acceptance_complete", "validators/fixtures/gold/visual_qa_acceptance_complete.json")],
        "bad_fixtures": [
            ("bad_visual_qa_missing_contact_sheet", "validators/fixtures/bad/visual_qa_missing_contact_sheet.json"),
            ("bad_visual_qa_missing_human_review", "validators/fixtures/bad/visual_qa_missing_human_review.json"),
        ],
    },
    "pilot_cut_validation_packet": {
        "banner": "PILOT_CUT_VALIDATION_PACKET",
        "validate": validate_pilot_cut_validation_packet,
        "gold_fixtures": [("gold_pilot_cut_c04a_valid", "validators/fixtures/gold/pilot_cut_c04a_valid.json")],
        "bad_fixtures": [
            ("bad_pilot_wrong_cut_id", "validators/fixtures/bad/pilot_wrong_cut_id.json"),
            ("bad_full_render_before_pilot", "validators/fixtures/bad/full_render_before_pilot.json"),
        ],
    },
    "audio_authorization_packet": {
        "banner": "AUDIO_AUTHORIZATION_PACKET",
        "validate": validate_audio_authorization_packet,
        "gold_fixtures": [("gold_audio_authorization_valid", "validators/fixtures/gold/audio_authorization_valid.json")],
        "bad_fixtures": [("bad_audio_before_visual_acceptance", "validators/fixtures/bad/audio_before_visual_acceptance.json")],
    },
    "davinci_handoff_packet": {
        "banner": "DAVINCI_HANDOFF_PACKET",
        "validate": validate_davinci_handoff_packet,
        "gold_fixtures": [("gold_davinci_handoff_valid", "validators/fixtures/gold/davinci_handoff_valid.json")],
        "bad_fixtures": [("bad_davinci_before_visual_audio_package", "validators/fixtures/bad/davinci_before_visual_audio_package.json")],
    },
    "no_fake_pass_gate": {
        "banner": "NO_FAKE_PASS_GATE",
        "validate": validate_no_fake_pass_gate,
        "gold_fixtures": [("gold_pass_with_evidence_bundle", "validators/fixtures/gold/pass_with_evidence_bundle.json")],
        "bad_fixtures": [
            ("bad_pass_reason_ffprobe_only", "validators/fixtures/bad/pass_reason_ffprobe_only.json"),
            ("bad_pass_reason_file_exists_only", "validators/fixtures/bad/pass_reason_file_exists_only.json"),
            ("bad_pass_reason_exit_code_0_only", "validators/fixtures/bad/pass_reason_exit_code_0_only.json"),
            ("bad_pass_reason_contract_exists_only", "validators/fixtures/bad/pass_reason_contract_exists_only.json"),
        ],
    },
    "pilot_cut_gate": {
        "banner": "PILOT_CUT_GATE",
        "validate": validate_pilot_cut_gate,
        "gold_fixtures": [("gold_pilot_c04a_valid", "validators/fixtures/gold/pilot_c04a_valid.json")],
        "bad_fixtures": [
            ("bad_pilot_wrong_cut_id", "validators/fixtures/bad/pilot_wrong_cut_id.json"),
            ("bad_full_render_before_pilot", "validators/fixtures/bad/full_render_before_pilot.json"),
        ],
    },
    "audio_authorization_gate": {
        "banner": "AUDIO_AUTHORIZATION_GATE",
        "validate": validate_audio_authorization_gate,
        "gold_fixtures": [
            ("gold_audio_authorization_valid", "validators/fixtures/gold/audio_authorization_valid.json"),
            ("gold_audio_authorized_valid", "validators/fixtures/gold/audio_authorized_valid.json"),
        ],
        "bad_fixtures": [
            ("bad_audio_before_visual_acceptance", "validators/fixtures/bad/audio_before_visual_acceptance.json"),
        ],
    },
    "davinci_handoff_gate": {
        "banner": "DAVINCI_HANDOFF_GATE",
        "validate": validate_davinci_handoff_gate,
        "gold_fixtures": [
            ("gold_davinci_handoff_valid", "validators/fixtures/gold/davinci_handoff_valid.json"),
            ("gold_davinci_handoff_authorized", "validators/fixtures/gold/davinci_handoff_authorized.json"),
        ],
        "bad_fixtures": [
            ("bad_davinci_before_visual_audio_package", "validators/fixtures/bad/davinci_before_visual_audio_package.json"),
            ("bad_davinci_before_acceptance", "validators/fixtures/bad/davinci_before_acceptance.json"),
        ],
    },
}
