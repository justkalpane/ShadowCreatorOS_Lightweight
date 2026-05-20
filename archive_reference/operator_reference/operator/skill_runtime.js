const SkillLoader = require('../engine/skill_loader/skill_loader.js');
const ProviderRouter = require('./provider_router');
const { readJsonSafe, writeJsonSafe, nowIso } = require('./_shared');

function mapWorkflowToFamily(workflowId) {
  const wf = String(workflowId || '').toUpperCase();
  const map = {
    'CWF-110': 'research_packet',
    'CWF-120': 'research_packet',
    'CWF-130': 'debate_packet',
    'CWF-140': 'research_packet',
    'CWF-210': 'script_packet',
    'CWF-220': 'debate_packet',
    'CWF-230': 'refined_script_packet',
    'CWF-240': 'refined_script_packet',
    'CWF-310': 'context_packet',
    'CWF-320': 'context_packet',
    'CWF-330': 'context_packet',
    'CWF-340': 'context_packet',
    'CWF-410': 'thumbnail_packet',
    'CWF-420': 'thumbnail_packet',
    'CWF-430': 'metadata_packet',
    'CWF-440': 'metadata_packet',
    'CWF-510': 'metadata_packet',
    'CWF-520': 'metadata_packet',
    'CWF-530': 'metadata_packet',
    'CWF-610': 'metadata_packet',
    'CWF-620': 'metadata_packet',
    'CWF-630': 'metadata_packet',
  };
  return map[wf] || 'runtime_packet';
}

function mapFamilyToType(family) {
  switch (family) {
    case 'research_packet':
      return 'research';
    case 'script_packet':
      return 'script_draft';
    case 'debate_packet':
      return 'debate_critique';
    case 'refined_script_packet':
      return 'refined_script';
    case 'context_packet':
      return 'context_engineering';
    case 'thumbnail_packet':
      return 'thumbnail_plan';
    case 'metadata_packet':
      return 'metadata_plan';
    default:
      return 'runtime_output';
  }
}

function cleanTopic(input = {}) {
  const mc = (input.mission_context && typeof input.mission_context === 'object') ? input.mission_context : {};
  const raw = String(
    input.topic ||
    input.task ||
    input.message ||
    input.user_message ||
    mc.normalized_topic ||
    mc.original_user_message ||
    (input.context && (input.context.topic || input.context.user_message)) ||
    ''
  ).trim();
  const normalized = raw.replace(/\s+/g, ' ').slice(0, 240);
  return normalized || 'MISSION_CONTEXT_MISSING';
}

function inferProviderMetadata(input = {}) {
  const explicitProvider = String(input.provider_used || input.provider || '').trim();
  const explicitModel = String(input.model_used || input.model || '').trim();
  return {
    provider_used: explicitProvider || 'local_deterministic_template',
    model_used: explicitModel || 'template_v1',
    realtime_used: false,
    fallback_chain: ['local_deterministic_template'],
    provider_skip_reason: null,
    citations: [],
    cloud_provider_used: false,
  };
}

function materializeContent(family, input = {}) {
  const topic = cleanTopic(input);
  const topicShort = topic.length > 90 ? `${topic.slice(0, 87)}...` : topic;

  switch (family) {
    case 'research_packet':
      return {
        summary: `This topic explores ${topicShort} with a creator-first lens: explain the conflict clearly, ground claims in practical examples, and frame audience stakes early.`,
        angles: [
          `Myth vs reality in ${topicShort}`,
          'Human judgment vs machine speed',
          'What viewers can do next'
        ],
        claims: [
          'AI improves scale, but human framing determines trust.',
          'Audiences retain stories with conflict + consequence.',
          'Credibility increases when tradeoffs are explicit.'
        ],
        risks: [
          'Overclaiming without sources can reduce trust.',
          'One-sided framing can hurt audience retention.'
        ],
        audience_hooks: [
          `What if ${topicShort} changes your role sooner than expected?`,
          'Would you trust AI with a decision that affects your family?'
        ]
      };
    case 'script_packet':
      return {
        hook: `AI can write faster than us. But can it decide better than us?`,
        intro: `Today we test ${topicShort} with real tradeoffs, not hype.`,
        body: [
          'Part 1: Where AI clearly wins (speed, scale, pattern detection).',
          'Part 2: Where humans still win (context, ethics, accountability).',
          'Part 3: A practical hybrid workflow creators can adopt this week.'
        ],
        payoff: 'The winner is not AI or human alone. The winner is smart orchestration.',
        cta: 'Comment with one task you would delegate to AI and one you would keep human.'
      };
    case 'debate_packet':
      return {
        strengths: [
          'Strong contrast between machine efficiency and human judgment.',
          'High relevance for creator and career-focused audiences.'
        ],
        weaknesses: [
          'Can become abstract without concrete examples.',
          'Risk of sounding binary instead of hybrid.'
        ],
        critique: 'Add one real scenario where AI failure had human consequences and one scenario where AI saved time meaningfully.',
        improvement_notes: [
          'Insert measurable outcomes (time saved, errors reduced).',
          'Balance optimism with governance safeguards.'
        ]
      };
    case 'refined_script_packet':
      return {
        final_script: [
          'Hook: AI can outpace us in seconds. But can it outthink us when stakes are real?',
          `Intro: In this video, we break down ${topicShort} without hype.`,
          'Research Summary: AI dominates repetition and prediction, while humans dominate context, ethics, and accountability.',
          'Debate: If AI makes decisions faster, do we gain efficiency or lose responsibility?',
          'Refined Take: Use AI for drafting, ranking, and simulation; keep humans for judgment, narrative, and final approval.',
          'CTA: If you had to choose one decision AI should never make alone, what would it be?'
        ].join('\n'),
        scene_beats: [
          'Cold open question',
          'Fast evidence montage',
          'Two-column AI vs Human comparison',
          'Hybrid framework reveal',
          'Call to action'
        ],
        voiceover_text: `AI is your accelerator. Human judgment is your steering wheel. ${topicShort} only works when both are in sync.`
      };
    case 'context_packet':
      return {
        audience: 'YouTube viewers interested in AI, productivity, and career impact.',
        tone: 'Confident, practical, balanced, high-retention.',
        structure: ['Hook', 'Context', 'Evidence', 'Debate', 'Resolution', 'CTA'],
        visual_direction: 'Kinetic text overlays, split-screen AI vs Human, fast cutaways to examples.',
        context_json: {
          platform: 'YouTube',
          format: 'short-form explainer',
          target_retention_style: 'pattern interrupts every 8-12 seconds'
        }
      };
    case 'thumbnail_packet':
      return {
        thumbnail_ideas: [
          'Half-face split: robotic eye vs human eye, text: "WHO DECIDES?"',
          'Bold text: "AI vs HUMAN" with red/green verdict markers',
          'Creator pointing at two buttons: "AUTOMATE" vs "JUDGMENT"'
        ],
        text_overlay_options: ['AI vs HUMAN', 'WHO SHOULD DECIDE?', 'SPEED vs JUDGMENT'],
        composition_notes: 'High contrast subject cutout, 3-word max text, strong facial emotion, single focal hierarchy.'
      };
    case 'metadata_packet':
      return {
        title_options: [
          'AI vs Human: Who Should Make the Final Decision?',
          'AI Is Fast. Humans Are Responsible. Here’s the Difference.',
          'The Real AI vs Human Debate (No Hype)'
        ],
        description: `AI vs Human is not about replacement. It is about role clarity. This video breaks down where AI wins, where humans win, and how to build a better hybrid workflow.`,
        hashtags: ['#AI', '#HumanVsAI', '#CreatorEconomy', '#FutureOfWork', '#YouTubeStrategy'],
        pinned_comment: 'Where do you draw the line: what should AI never decide alone?'
      };
    default:
      return {
        summary: `Materialized fallback content for ${topicShort}.`
      };
  }
}

class SkillRuntime {
  constructor() {
    this.loader = new SkillLoader();
    this.providerRouter = new ProviderRouter();
    this.initialized = false;
    this.bundleCache = new Map();
  }

  mapFamilyToTaskType(family) {
    switch (family) {
      case 'research_packet':
        return 'real_time_research';
      case 'script_packet':
        return 'script_generation';
      case 'debate_packet':
        return 'debate_generation';
      case 'refined_script_packet':
        return 'script_refinement';
      case 'context_packet':
        return 'context_engineering';
      case 'thumbnail_packet':
        return 'thumbnail_planning';
      case 'metadata_packet':
        return 'metadata_generation';
      default:
        return 'generic_generation';
    }
  }

  async ensureInitialized() {
    if (this.initialized) return;
    const init = await this.loader.initialize();
    if (init?.status !== 'initialized') {
      throw new Error(`skill_loader_init_failed: ${JSON.stringify(init)}`);
    }
    this.initialized = true;
  }

  normalizePacket(packet, input, providerMetaOverride = null, contentOverride = null) {
    const dossierId = input.dossier_id || input.dossier_ref || 'DOSSIER-UNSPECIFIED';
    const workflowId = String(input.workflow_id || input.workflow_ref || 'CWF-UNKNOWN').toUpperCase();
    const family = mapWorkflowToFamily(workflowId);
    const createdAt = nowIso();
    const instanceId = packet?.instance_id || `PKT-${workflowId}-${Date.now()}`;
    const providerMeta = providerMetaOverride || inferProviderMetadata(input);
    const content = contentOverride || materializeContent(family, input);

    const missionContext =
      input.mission_context && typeof input.mission_context === 'object'
        ? input.mission_context
        : {};

    return {
      ...packet,
      instance_id: instanceId,
      packet_id: instanceId,
      artifact_family: family,
      artifact_type: mapFamilyToType(family),
      producer_workflow: workflowId,
      source_workflow: workflowId,
      source_skill: input.skill_id || packet?.skill_id || 'M-001',
      source_subskill: input.subskill_id || null,
      source_node: input.source_node || 'Skill Execution Node',
      dossier_ref: dossierId,
      dossier_id: dossierId,
      created_at: packet?.created_at || createdAt,
      status: packet?.status || 'CREATED',
      materialization_source: 'operator_skill_runtime',
      provider_used: providerMeta.provider_used,
      model_used: providerMeta.model_used,
      realtime_used: providerMeta.realtime_used,
      fallback_chain: providerMeta.fallback_chain,
      provider_skip_reason: providerMeta.provider_skip_reason || null,
      citations: Array.isArray(providerMeta.citations) ? providerMeta.citations : [],
      cloud_provider_used: Boolean(providerMeta.cloud_provider_used),
      generated_at: createdAt,
      producer_workflow_id: workflowId,
      producer_workflow_name: workflowId,
      producer_cwf_id: workflowId,
      producer_skill_id: input.skill_id || packet?.skill_id || 'M-001',
      producer_skill_name: input.skill_name || null,
      producer_director_id: missionContext.director_requested || input.director_requested || null,
      producer_director_name: missionContext.director_requested || input.director_requested || null,
      producer_agent_id: input.agent_id || null,
      producer_subagent_id: input.subagent_id || null,
      producer_subskill_id: input.subskill_id || null,
      intent_id: missionContext.intent_id || input.intent_id || null,
      mission_hash: missionContext.mission_hash || null,
      reference_dossier_id: missionContext.reference_dossier_id || input.reference_dossier_id || null,
      content,
    };
  }

  appendPacketIndex(packet) {
    const doc = readJsonSafe('data/se_packet_index.json', { entries: [] });
    const entries = Array.isArray(doc.entries)
      ? doc.entries
      : (Array.isArray(doc.packets) ? doc.packets : []);

    const key = packet.packet_id || packet.instance_id;
    const exists = entries.some((e) => (e.packet_id || e.instance_id) === key);
    if (!exists) entries.push(packet);

    writeJsonSafe('data/se_packet_index.json', {
      ...doc,
      entries,
      total_entries: entries.length,
      last_updated: nowIso(),
    });
  }

  async execute(input = {}) {
    await this.ensureInitialized();

    const missionContext =
      input.mission_context && typeof input.mission_context === 'object'
        ? input.mission_context
        : {};
    const resolvedTopic = cleanTopic(input);
    if (resolvedTopic === 'MISSION_CONTEXT_MISSING') {
      return {
        status: 'FAILED',
        error: 'MISSION_CONTEXT_MISSING',
      };
    }

    const dossierId = input.dossier_id || input.dossier_ref || 'DOSSIER-UNSPECIFIED';
    const skillId = input.skill_id || 'M-001';
    const contextPacket = {
      dossier_id: dossierId,
      workflow_id: input.workflow_id || input.workflow_ref || null,
      route_id: input.route_id || null,
      user_message: input.task || input.message || null,
      mission_context: missionContext,
      ...(typeof input.context === 'object' && input.context ? input.context : {}),
    };
    const dossierState = typeof input.dossier === 'object' && input.dossier ? input.dossier : {};

    let result = await this.loader.executeSkill(skillId, contextPacket, dossierState);
    if ((result?.status !== 'SUCCESS' || !result?.output) && skillId !== 'M-001') {
      const err = String(result?.error || '');
      if (/not found/i.test(err)) {
        result = await this.loader.executeSkill('M-001', contextPacket, dossierState);
      }
    }
    if (result?.status !== 'SUCCESS' || !result?.output) {
      return {
        status: 'FAILED',
        error: String(result?.error || 'skill_execution_failed'),
      };
    }

    const family = mapWorkflowToFamily(input.workflow_id || input.workflow_ref || 'CWF-UNKNOWN');
    const taskType = this.mapFamilyToTaskType(family);
    const preferredProvider = String(
      input.provider_preference ||
      input.preferred_provider ||
      (input.context && input.context.provider_preference) ||
      process.env.SHADOW_DEFAULT_PROVIDER ||
      'gemini'
    ).trim();
    const cloudRequired = input.cloud_llm_required !== false;
    const routeMode = String(input.route_mode || 'production').toLowerCase();

    let providerMeta = inferProviderMetadata(input);
    let contentOverride = null;
    try {
      const creativeFamilies = new Set([
        'research_packet',
        'script_packet',
        'debate_packet',
        'refined_script_packet',
        'context_packet',
        'thumbnail_packet',
        'metadata_packet',
      ]);

      let routed;
      if (cloudRequired && creativeFamilies.has(family)) {
        const cacheKey = `${dossierId}::${preferredProvider || 'gemini'}::creative_bundle`;
        if (!this.bundleCache.has(cacheKey)) {
          const p = this.providerRouter.generate({
            task_type: 'creative_bundle',
            preferred_provider: preferredProvider,
            cloud_llm_required: true,
            route_mode: routeMode,
            topic: input.topic || input.task || input.message || '',
            prompt: input.task || input.message || '',
            context: input.context || {},
          });
          this.bundleCache.set(cacheKey, p);
        }
        routed = await this.bundleCache.get(cacheKey);
      } else {
        routed = await this.providerRouter.generate({
          task_type: taskType,
          preferred_provider: cloudRequired ? preferredProvider : '',
          cloud_llm_required: cloudRequired,
          route_mode: routeMode,
          topic: resolvedTopic,
          prompt: input.task || input.message || resolvedTopic,
          context: input.context || {},
        });
      }

      if (cloudRequired && routeMode === 'production' && routed?.status !== 'SUCCESS') {
        return {
          status: 'FAILED',
          error: String(routed?.provider_skip_reason || routed?.status || 'CLOUD_PROVIDER_FAILED'),
        };
      }

      if (routed && typeof routed === 'object') {
        providerMeta = {
          provider_used: routed.provider_used || providerMeta.provider_used,
          model_used: routed.model_used || providerMeta.model_used,
          realtime_used: Boolean(routed.realtime_used),
          fallback_chain: Array.isArray(routed.fallback_chain) ? routed.fallback_chain : providerMeta.fallback_chain,
          provider_skip_reason: routed.provider_skip_reason || null,
          citations: Array.isArray(routed.citations) ? routed.citations : [],
          cloud_provider_used: Boolean(routed.cloud_provider_used),
        };

        const bundle = routed?.content?.creative_bundle;
        if (bundle && typeof bundle === 'object') {
          contentOverride = bundle[family] || null;
          if (cloudRequired && routeMode === 'production' && !contentOverride) {
            return {
              status: 'FAILED',
              error: `CLOUD_BUNDLE_MISSING_${family.toUpperCase()}`,
            };
          }
        }
      }
    } catch (_) {
      if (cloudRequired && routeMode === 'production') {
        return {
          status: 'FAILED',
          error: 'CLOUD_PROVIDER_RUNTIME_EXCEPTION',
        };
      }
    }

    const packet = this.normalizePacket(result.output, input, providerMeta, contentOverride);

    // Quality gate: prevent generic stale output in production when topic was explicit.
    if (
      cloudRequired &&
      routeMode === 'production' &&
      packet?.artifact_family === 'refined_script_packet' &&
      missionContext?.normalized_topic &&
      /content generation/i.test(String(packet?.content?.final_script || '')) &&
      !/content generation/i.test(String(missionContext.normalized_topic || ''))
    ) {
      return {
        status: 'FAILED',
        error: 'GENERIC_OUTPUT_REJECTED',
      };
    }

    this.appendPacketIndex(packet);

    return {
      status: 'SUCCESS',
      runtime_packet: packet,
      skill_execution_result: result,
    };
  }
}

module.exports = SkillRuntime;
