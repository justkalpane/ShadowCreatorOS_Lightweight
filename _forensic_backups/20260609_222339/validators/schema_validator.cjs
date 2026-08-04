/**
 * Schema Validator
 * Validates packet schemas, schema registry closure, and mutation payload contracts.
 */

const fs = require('fs');
const path = require('path');
const PacketValidator = require('../engine/packets/packet_validator');

class SchemaValidator {
  constructor(config = {}) {
    this.config = {
      schema_registry_path: config.schema_registry_path || './registries/schema_registry.yaml',
      skill_registry_path: config.skill_registry_path || './registries/skill_registry.yaml'
    };

    this.packet_validator = new PacketValidator({
      schema_registry_path: this.config.schema_registry_path
    });
    this.validation_log = [];
    this.allowed_mutation_types = new Set([
      'append_to_array',
      'create_new_packet',
      'create_new_index_row',
      'append_audit_entry'
    ]);
  }

  validatePacket(packet) {
    return this.packet_validator.validatePacket(packet);
  }

  validatePacketBatch(packets) {
    const results = packets.map((packet) => this.validatePacket(packet));
    return {
      total: packets.length,
      valid: results.filter((row) => row.valid).length,
      invalid: results.filter((row) => !row.valid).length,
      results
    };
  }

  validateDossier(dossier) {
    const errors = [];
    const warnings = [];

    if (!dossier || typeof dossier !== 'object' || Array.isArray(dossier)) {
      return { valid: false, errors: ['Dossier is not a valid object'], warnings: [] };
    }

    if (!dossier.dossier_id) {
      errors.push('Missing dossier_id');
    }

    if (dossier._version === undefined) {
      warnings.push('Missing _version field');
    }
    if (!dossier._created_at) {
      warnings.push('Missing _created_at field');
    }

    if (!Array.isArray(dossier._audit_trail)) {
      errors.push('Missing or invalid _audit_trail. Expected array.');
    } else {
      dossier._audit_trail.forEach((entry, index) => {
        this.validateAuditEntry(entry, `audit_trail[${index}]`, errors);
      });
    }

    const allowed_namespaces = new Set([
      'system',
      'intake',
      'discovery',
      'research',
      'script',
      'context',
      'approval',
      'runtime',
      'script_vein',
      'research_vein',
      'media_vein'
    ]);

    Object.keys(dossier)
      .filter((key) => !key.startsWith('_') && key !== 'dossier_id')
      .forEach((namespace) => {
        if (!allowed_namespaces.has(namespace)) {
          warnings.push(`Unknown namespace "${namespace}" in dossier payload`);
        }
      });

    return {
      valid: errors.length === 0,
      dossier_id: dossier.dossier_id || 'UNKNOWN',
      version: dossier._version,
      errors,
      warnings
    };
  }

  validateDelta(delta) {
    const errors = [];

    const required = [
      'namespace',
      'mutation_type',
      'target',
      'value',
      'timestamp',
      'writer_id',
      'skill_id',
      'instance_id',
      'schema_version',
      'lineage_reference',
      'audit_entry'
    ];

    for (const field of required) {
      if (!(field in (delta || {}))) {
        errors.push(`Delta missing required field: ${field}`);
      }
    }

    if (delta?.mutation_type && !this.allowed_mutation_types.has(delta.mutation_type)) {
      errors.push(
        `Invalid mutation_type "${delta.mutation_type}". Allowed: ${Array.from(this.allowed_mutation_types).join(', ')}`
      );
    }

    if (delta?.audit_entry && (typeof delta.audit_entry !== 'object' || Array.isArray(delta.audit_entry))) {
      errors.push('audit_entry must be an object');
    } else if (delta?.audit_entry) {
      if (!delta.audit_entry.workflow_id) {
        errors.push('audit_entry missing workflow_id');
      }
      if (!delta.audit_entry.operation) {
        errors.push('audit_entry missing operation');
      }
    }

    return {
      valid: errors.length === 0,
      errors
    };
  }

  validateSchemaRegistry() {
    const findings = [];
    const registryPath = path.resolve(this.config.schema_registry_path);
    if (!fs.existsSync(registryPath)) {
      findings.push({
        code: 'MISSING_SCHEMA_REGISTRY',
        severity: 'error',
        message: `Missing schema registry: ${registryPath}`
      });
      return { valid: false, schemas: [], findings };
    }

    const schemas = this.parseSchemaRegistry(fs.readFileSync(registryPath, 'utf8'));
    const seenFamilies = new Set();

    for (const schema of schemas) {
      if (!schema.artifact_family) {
        findings.push({
          code: 'SCHEMA_REGISTRY_MISSING_ARTIFACT_FAMILY',
          severity: 'error',
          message: 'Schema registry row missing artifact_family'
        });
      }
      if (!schema.schema_path) {
        findings.push({
          code: 'SCHEMA_REGISTRY_MISSING_SCHEMA_PATH',
          severity: 'error',
          message: `${schema.artifact_family || 'UNKNOWN'} missing schema_path`
        });
      }

      if (schema.artifact_family) {
        if (seenFamilies.has(schema.artifact_family)) {
          findings.push({
            code: 'SCHEMA_REGISTRY_DUPLICATE_ARTIFACT_FAMILY',
            severity: 'error',
            message: `Duplicate artifact_family in schema registry: ${schema.artifact_family}`
          });
        }
        seenFamilies.add(schema.artifact_family);
      }

      if (schema.schema_path) {
        const schemaPath = path.resolve(schema.schema_path);
        if (!fs.existsSync(schemaPath)) {
          findings.push({
            code: 'MISSING_SCHEMA_FILE',
            severity: 'error',
            message: `${schema.artifact_family || 'UNKNOWN'} schema file missing: ${schema.schema_path}`
          });
        } else {
          try {
            JSON.parse(this.stripBom(fs.readFileSync(schemaPath, 'utf8')));
          } catch (error) {
            findings.push({
              code: 'INVALID_SCHEMA_JSON',
              severity: 'error',
              message: `${schema.artifact_family || 'UNKNOWN'} schema parse failed: ${error.message}`
            });
          }
        }
      }
    }

    return {
      valid: !findings.some((row) => row.severity === 'error'),
      schemas,
      findings
    };
  }

  validateSkillSchemaBindings() {
    const findings = [];
    const schemaMap = new Map();
    const schemaCheck = this.validateSchemaRegistry();

    for (const row of schemaCheck.schemas) {
      if (row.artifact_family) {
        schemaMap.set(row.artifact_family, row);
      }
    }

    const skillRegistryPath = path.resolve(this.config.skill_registry_path);
    if (!fs.existsSync(skillRegistryPath)) {
      findings.push({
        code: 'MISSING_SKILL_REGISTRY',
        severity: 'error',
        message: `Missing skill registry: ${skillRegistryPath}`
      });
      return {
        valid: false,
        findings
      };
    }

    const skills = this.parseSkillSchemaBindings(fs.readFileSync(skillRegistryPath, 'utf8'));
    for (const skill of skills) {
      if (!skill.schema_ref) {
        findings.push({
          code: 'SKILL_MISSING_SCHEMA_REF',
          severity: 'error',
          message: `${skill.skill_id} missing schema_ref`
        });
        continue;
      }

      const schemaRefPath = path.resolve(skill.schema_ref);
      if (!fs.existsSync(schemaRefPath)) {
        findings.push({
          code: 'SKILL_SCHEMA_REF_MISSING_FILE',
          severity: 'error',
          message: `${skill.skill_id} schema_ref file missing: ${skill.schema_ref}`
        });
      }

      if (!skill.output_packet_family) {
        findings.push({
          code: 'SKILL_MISSING_OUTPUT_PACKET_FAMILY',
          severity: 'error',
          message: `${skill.skill_id} missing output_packet_family`
        });
      } else if (!schemaMap.has(skill.output_packet_family)) {
        findings.push({
          code: 'SKILL_PACKET_FAMILY_NOT_IN_SCHEMA_REGISTRY',
          severity: 'error',
          message: `${skill.skill_id} output_packet_family ${skill.output_packet_family} not found in schema_registry`
        });
      }
    }

    return {
      valid: schemaCheck.valid && !findings.some((row) => row.severity === 'error'),
      findings
    };
  }

  runFullCheck() {
    const schemaCheck = this.validateSchemaRegistry();
    const bindingCheck = this.validateSkillSchemaBindings();
    const mediaFactoryPacketCheck = this.validateMediaFactoryBenchmarkPacket();

    return {
      overall_valid: schemaCheck.valid && bindingCheck.valid && mediaFactoryPacketCheck.valid,
      schema_registry_check: schemaCheck,
      binding_check: bindingCheck,
      media_factory_packet_check: mediaFactoryPacketCheck,
      findings: [...schemaCheck.findings, ...bindingCheck.findings, ...mediaFactoryPacketCheck.findings],
      timestamp: new Date().toISOString()
    };
  }

  validateMediaFactoryBenchmarkPacket() {
    const packetPath = path.resolve('outputs/missions/yash_self_investment/packets/media_factory_packet.json');
    const findings = [];
    const parseClockSeconds = (value) => {
      if (typeof value === 'number' && Number.isFinite(value)) {
        return value;
      }
      if (typeof value !== 'string') {
        return null;
      }
      const trimmed = value.trim();
      const match = trimmed.match(/^(\d{1,2}):(\d{2})$/);
      if (!match) {
        return null;
      }
      return (Number(match[1]) * 60) + Number(match[2]);
    };

    if (!fs.existsSync(packetPath)) {
      return {
        valid: true,
        findings: [
          {
            code: 'MEDIA_FACTORY_BENCHMARK_PACKET_MISSING',
            severity: 'warning',
            message: 'Yash benchmark media_factory_packet.json not present; structural benchmark validation skipped'
          }
        ]
      };
    }

    let packet;
    try {
      packet = JSON.parse(this.stripBom(fs.readFileSync(packetPath, 'utf8')));
    } catch (error) {
      return {
        valid: false,
        findings: [
          {
            code: 'MEDIA_FACTORY_BENCHMARK_PACKET_PARSE_ERROR',
            severity: 'error',
            message: `media_factory_packet.json parse failed: ${error.message}`,
            filepath: packetPath
          }
        ]
      };
    }

    const phases = packet?.production_order_lock?.phases || [];
    const controlPhases = packet?.control_panel_execution_plan?.phases || [];
    const timelineRows = packet?.davinci_timeline_packet?.timeline_rows || [];
    const assetRows = packet?.asset_dependency_graph || [];
    const evidenceRows = packet?.evidence || [];
    const expectedPhaseIds = Array.from({ length: 17 }, (_, index) => `P${String(index + 1).padStart(2, '0')}`);
    const phaseRequired = [
      'phase_id',
      'phase_order',
      'phase_name',
      'depends_on_phase_ids',
      'blocking_prerequisites',
      'output_asset_classes',
      'execution_mode',
      'approval_gate',
      'proof_gate',
      'status'
    ];
    const controlRequired = [
      'phase_id',
      'plan_state',
      'control_panel_entrypoint',
      'preflight_dependency',
      'downgrade_on_failure',
      'proof_artifacts',
      'status'
    ];

    if (packet.packet_id !== 'media_factory_packet' || packet.route_id !== 'MEDIA_FACTORY_HANDOFF') {
      findings.push({
        code: 'MEDIA_FACTORY_BENCHMARK_ID_MISMATCH',
        severity: 'error',
        message: 'Benchmark packet must use packet_id=media_factory_packet and route_id=MEDIA_FACTORY_HANDOFF',
        filepath: packetPath
      });
    }

    if (phases.length !== 17) {
      findings.push({
        code: 'MEDIA_FACTORY_PRODUCTION_PHASE_COUNT',
        severity: 'error',
        message: `production_order_lock.phases must contain exactly 17 canonical phases; found ${phases.length}`,
        filepath: packetPath
      });
    }

    phases.forEach((row, index) => {
      const expectedId = expectedPhaseIds[index];
      if (row.phase_id !== expectedId || row.phase_order !== index + 1) {
        findings.push({
          code: 'MEDIA_FACTORY_PRODUCTION_PHASE_ORDER',
          severity: 'error',
          message: `production phase index ${index} must be ${expectedId} with phase_order=${index + 1}`,
          filepath: packetPath
        });
      }
      for (const field of phaseRequired) {
        if (!(field in row)) {
          findings.push({
            code: 'MEDIA_FACTORY_PRODUCTION_PHASE_FIELD',
            severity: 'error',
            message: `${row.phase_id || `phase_${index + 1}`} missing canonical field ${field}`,
            filepath: packetPath
          });
        }
      }
      for (const legacyField of ['sequence', 'action', 'depends_on', 'approval_required', 'proof_required']) {
        if (legacyField in row) {
          findings.push({
            code: 'MEDIA_FACTORY_LEGACY_PHASE_FIELD',
            severity: 'error',
            message: `${row.phase_id || `phase_${index + 1}`} still contains legacy field ${legacyField}`,
            filepath: packetPath
          });
        }
      }
    });

    if (controlPhases.length !== 17) {
      findings.push({
        code: 'MEDIA_FACTORY_CONTROL_PHASE_COUNT',
        severity: 'error',
        message: `control_panel_execution_plan.phases must contain exactly 17 per-phase rows; found ${controlPhases.length}`,
        filepath: packetPath
      });
    }

    controlPhases.forEach((row, index) => {
      const expectedId = expectedPhaseIds[index];
      if (row.phase_id !== expectedId) {
        findings.push({
          code: 'MEDIA_FACTORY_CONTROL_PHASE_ORDER',
          severity: 'error',
          message: `control panel phase index ${index} must be ${expectedId}`,
          filepath: packetPath
        });
      }
      for (const field of controlRequired) {
        if (!(field in row)) {
          findings.push({
            code: 'MEDIA_FACTORY_CONTROL_PHASE_FIELD',
            severity: 'error',
            message: `${row.phase_id || `control_phase_${index + 1}`} missing canonical field ${field}`,
            filepath: packetPath
          });
        }
      }
      if ('control_panel_action' in row) {
        findings.push({
          code: 'MEDIA_FACTORY_LEGACY_CONTROL_FIELD',
          severity: 'error',
          message: `${row.phase_id || `control_phase_${index + 1}`} still contains legacy field control_panel_action`,
          filepath: packetPath
        });
      }
    });

    if (Number.isInteger(packet.scene_count) && timelineRows.length < packet.scene_count) {
      findings.push({
        code: 'MEDIA_FACTORY_DAVINCI_TIMELINE_INCOMPLETE',
        severity: 'error',
        message: `davinci_timeline_packet.timeline_rows must cover every scene (${packet.scene_count}); found ${timelineRows.length}`,
        filepath: packetPath
      });
    }

    if (assetRows.length < 10) {
      findings.push({
        code: 'MEDIA_FACTORY_ASSET_DEPENDENCY_GRAPH_SHALLOW',
        severity: 'error',
        message: `asset_dependency_graph must map production asset classes, not only summary lanes; found ${assetRows.length}`,
        filepath: packetPath
      });
    }

    if (evidenceRows.length < 3) {
      findings.push({
        code: 'MEDIA_FACTORY_EVIDENCE_LEDGER_SHALLOW',
        severity: 'error',
        message: `evidence ledger must include packet, scene sync, and production-control evidence; found ${evidenceRows.length}`,
        filepath: packetPath
      });
    }

    if (packet?.provider_boundary?.providers_called !== false || packet?.provider_boundary?.provider_execution_allowed !== false) {
      findings.push({
        code: 'MEDIA_FACTORY_PROVIDER_BOUNDARY_WEAK',
        severity: 'error',
        message: 'provider_boundary must keep providers_called=false and provider_execution_allowed=false in planning packet',
        filepath: packetPath
      });
    }

    const voiceCount = packet?.asset_inventory_ledger?.voice_assets?.count;
    const musicCount = packet?.asset_inventory_ledger?.music_segments?.count;
    const sfxCount = packet?.asset_inventory_ledger?.sfx_clips?.count;
    const storyboardCount = packet?.asset_inventory_ledger?.storyboard_stills?.count;
    const depthStillCount = packet?.asset_inventory_ledger?.depth_parallax_stills?.count;
    if (voiceCount !== 1) {
      findings.push({
        code: 'MEDIA_FACTORY_MASTER_VOICE_REQUIRED',
        severity: 'error',
        message: `voice_assets.count must be exactly 1 master voice anchor; found ${voiceCount}`,
        filepath: packetPath
      });
    }
    if (!(typeof musicCount === 'number' && musicCount >= 3)) {
      findings.push({
        code: 'MEDIA_FACTORY_MUSIC_SEGMENTS_TOO_SHALLOW',
        severity: 'error',
        message: `music_segments.count must be at least 3 for arc-based scoring; found ${musicCount}`,
        filepath: packetPath
      });
    }
    if (!(typeof sfxCount === 'number' && sfxCount >= 10)) {
      findings.push({
        code: 'MEDIA_FACTORY_SFX_SEGMENTS_TOO_SHALLOW',
        severity: 'error',
        message: `sfx_clips.count must be at least 10 for generator-grade sync; found ${sfxCount}`,
        filepath: packetPath
      });
    }
    if (
      typeof storyboardCount === 'number'
      && typeof depthStillCount === 'number'
      && storyboardCount <= depthStillCount
    ) {
      findings.push({
        code: 'MEDIA_FACTORY_STORYBOARD_SCOPE_TOO_SHALLOW',
        severity: 'error',
        message: `storyboard_stills.count must exceed depth_parallax_stills.count; found storyboard=${storyboardCount}, depth=${depthStillCount}`,
        filepath: packetPath
      });
    }

    const toolTargets = {
      voice: String(packet?.voice_plan?.tool_target || '').toLowerCase(),
      aRoll: String(packet?.a_roll_plan?.tool_target || '').toLowerCase(),
      music: String(packet?.music_sfx_plan?.tool_target || '').toLowerCase(),
      bRoll: String(packet?.b_roll_plan?.primary_tool_target || '').toLowerCase()
    };
    if (!toolTargets.voice.includes('elevenlabs')) {
      findings.push({
        code: 'MEDIA_FACTORY_PRIMARY_VOICE_METHOD_DRIFT',
        severity: 'error',
        message: 'voice_plan.tool_target must remain ElevenLabs-first for the benchmark packet',
        filepath: packetPath
      });
    }
    if (!toolTargets.aRoll.includes('heygen')) {
      findings.push({
        code: 'MEDIA_FACTORY_PRIMARY_AROLL_METHOD_DRIFT',
        severity: 'error',
        message: 'a_roll_plan.tool_target must remain HeyGen-first for the benchmark packet',
        filepath: packetPath
      });
    }
    if (!toolTargets.music.includes('suno')) {
      findings.push({
        code: 'MEDIA_FACTORY_PRIMARY_MUSIC_METHOD_DRIFT',
        severity: 'error',
        message: 'music_sfx_plan.tool_target must keep Suno in the approved primary lane',
        filepath: packetPath
      });
    }
    if (!toolTargets.bRoll.includes('runway') && !toolTargets.bRoll.includes('kling')) {
      findings.push({
        code: 'MEDIA_FACTORY_PRIMARY_BROLL_METHOD_DRIFT',
        severity: 'error',
        message: 'b_roll_plan.primary_tool_target must keep premium cloud cinematic providers as the primary lane',
        filepath: packetPath
      });
    }
    if (['wan_local', 'comfyui', 'animatediff', 'flux'].some((marker) => toolTargets.bRoll.includes(marker))) {
      findings.push({
        code: 'MEDIA_FACTORY_EXPERIMENTAL_LOCAL_BROLL_PRIMARY',
        severity: 'error',
        message: 'experimental local video engines may not appear as the primary cinematic B-roll lane in the benchmark packet',
        filepath: packetPath
      });
    }

    const assetMap = new Map(assetRows.map((row) => [row.asset_id, row]));
    const voiceAsset = assetMap.get('master_voice_5m05s');
    const aRollAsset = assetMap.get('heygen_batch_pack');
    const bRollAsset = assetMap.get('cinematic_broll_pack');
    const storyboardAsset = assetMap.get('storyboard_stills_pack');
    if (voiceAsset) {
      if (!String(voiceAsset.tool_or_provider || '').toLowerCase().includes('elevenlabs')) {
        findings.push({
          code: 'MEDIA_FACTORY_VOICE_ASSET_PROVIDER_DRIFT',
          severity: 'error',
          message: 'master_voice_5m05s must remain on the ElevenLabs lane',
          filepath: packetPath
        });
      }
      if (!String(voiceAsset.generation_lane || '').toLowerCase().includes('cloud')) {
        findings.push({
          code: 'MEDIA_FACTORY_VOICE_ASSET_LANE_DRIFT',
          severity: 'error',
          message: 'master_voice_5m05s must remain a cloud_voice lane asset',
          filepath: packetPath
        });
      }
    }
    if (aRollAsset) {
      if (!String(aRollAsset.tool_or_provider || '').toLowerCase().includes('heygen')) {
        findings.push({
          code: 'MEDIA_FACTORY_AROLL_ASSET_PROVIDER_DRIFT',
          severity: 'error',
          message: 'heygen_batch_pack must remain on the HeyGen lane',
          filepath: packetPath
        });
      }
      if (!String(aRollAsset.generation_lane || '').toLowerCase().includes('cloud')) {
        findings.push({
          code: 'MEDIA_FACTORY_AROLL_ASSET_LANE_DRIFT',
          severity: 'error',
          message: 'heygen_batch_pack must remain a cloud_avatar lane asset',
          filepath: packetPath
        });
      }
    }
    if (bRollAsset) {
      const provider = String(bRollAsset.tool_or_provider || '').toLowerCase();
      const lane = String(bRollAsset.generation_lane || '').toLowerCase();
      if (!provider.includes('runway') && !provider.includes('kling')) {
        findings.push({
          code: 'MEDIA_FACTORY_BROLL_ASSET_PROVIDER_DRIFT',
          severity: 'error',
          message: 'cinematic_broll_pack must remain on Runway/Kling-class premium cloud providers',
          filepath: packetPath
        });
      }
      if (!lane.includes('cloud')) {
        findings.push({
          code: 'MEDIA_FACTORY_BROLL_ASSET_LANE_DRIFT',
          severity: 'error',
          message: 'cinematic_broll_pack must remain a cloud_video lane asset',
          filepath: packetPath
        });
      }
      if (['wan', 'comfyui', 'animatediff', 'flux'].some((marker) => provider.includes(marker))) {
        findings.push({
          code: 'MEDIA_FACTORY_BROLL_ASSET_EXPERIMENTAL_PRIMARY',
          severity: 'error',
          message: 'cinematic_broll_pack may not use local experimental engines as its primary provider',
          filepath: packetPath
        });
      }
    }
    if (storyboardAsset) {
      const provider = String(storyboardAsset.tool_or_provider || '').toLowerCase();
      if (!provider.includes('chatgpt') && !provider.includes('approved still provider')) {
        findings.push({
          code: 'MEDIA_FACTORY_STORYBOARD_STILL_METHOD_DRIFT',
          severity: 'error',
          message: 'storyboard_stills_pack must remain on the approved cloud still-image lane',
          filepath: packetPath
        });
      }
    }

    if (packet?.pacing_metadata?.scene_count !== packet.scene_count) {
      findings.push({
        code: 'MEDIA_FACTORY_SCENE_COUNT_MISMATCH',
        severity: 'error',
        message: `pacing_metadata.scene_count must match packet.scene_count (${packet.scene_count}); found ${packet?.pacing_metadata?.scene_count}`,
        filepath: packetPath
      });
    }
    const totalTimelineDuration = timelineRows.reduce((sum, row) => {
      const start = parseClockSeconds(row.start_time);
      const end = parseClockSeconds(row.end_time);
      if (start === null || end === null || end < start) {
        return sum;
      }
      return sum + (end - start);
    }, 0);
    if (
      typeof packet?.pacing_metadata?.total_duration_seconds === 'number'
      && totalTimelineDuration !== packet.pacing_metadata.total_duration_seconds
    ) {
      findings.push({
        code: 'MEDIA_FACTORY_DURATION_RECONCILIATION_FAILED',
        severity: 'error',
        message: `davinci_timeline_packet duration (${totalTimelineDuration}s) must match pacing_metadata.total_duration_seconds (${packet.pacing_metadata.total_duration_seconds}s)`,
        filepath: packetPath
      });
    }

    return {
      valid: !findings.some((row) => row.severity === 'error'),
      findings
    };
  }

  stripBom(text) {
    return String(text || '').replace(/^\uFEFF/, '');
  }

  validateAuditEntry(entry, location, errors) {
    const required = ['mutation_id', 'workflow_id', 'namespace', 'timestamp'];
    for (const field of required) {
      if (!entry[field]) {
        errors.push(`${location} missing ${field}`);
      }
    }
  }

  parseSchemaRegistry(text) {
    const lines = text.replace(/\r\n/g, '\n').split('\n');
    const entries = [];
    let current = null;

    const flush = () => {
      if (current) {
        entries.push(current);
      }
      current = null;
    };

    for (const line of lines) {
      const start = line.match(/^\s*-\s*artifact_family:\s*([a-zA-Z0-9_-]+)\s*$/);
      if (start) {
        flush();
        current = {
          artifact_family: start[1],
          schema_path: null
        };
        continue;
      }

      if (!current) {
        continue;
      }

      const schemaPath = line.match(/^\s*schema_path:\s*(.+?)\s*$/);
      if (schemaPath) {
        current.schema_path = schemaPath[1].trim();
      }
    }

    flush();
    return entries;
  }

  parseSkillSchemaBindings(text) {
    const lines = text.replace(/\r\n/g, '\n').split('\n');
    const skills = [];
    let current = null;

    const flush = () => {
      if (current) {
        skills.push(current);
      }
      current = null;
    };

    for (const line of lines) {
      const start = line.match(/^\s*-\s*skill_id:\s*(M-\d{3})\s*$/);
      if (start) {
        flush();
        current = {
          skill_id: start[1],
          schema_ref: null,
          output_packet_family: null
        };
        continue;
      }

      if (!current) {
        continue;
      }

      const schemaRef = line.match(/^\s*schema_ref:\s*(.+?)\s*$/);
      if (schemaRef) {
        current.schema_ref = schemaRef[1].trim();
        continue;
      }

      const packetFamily = line.match(/^\s*output_packet_family:\s*([a-zA-Z0-9_-]+)\s*$/);
      if (packetFamily) {
        current.output_packet_family = packetFamily[1].trim();
      }
    }

    flush();
    return skills;
  }

  getValidationLog() {
    return this.validation_log;
  }
}

module.exports = SchemaValidator;
