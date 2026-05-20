const express = require('express');
const ModeManager = require('../../operator/mode_manager');
const RouteManager = require('../../operator/route_manager');
const TaskRouter = require('../../operator/task_router');
const OperatorN8nClient = require('../../operator/n8n_client');
const OutputReader = require('../../operator/output_reader');
const ReviewManager = require('../../operator/review_manager');
const AlertManager = require('../../operator/alert_manager');
const TroubleshootManager = require('../../operator/troubleshoot_manager');
const EventStream = require('../../operator/event_stream');
const ProviderRouter = require('../../operator/provider_router');
const OllamaToolRunner = require('../../operator/ollama_tool_runner');
const SkillRuntime = require('../../operator/skill_runtime');
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const operatorConfig = require('../../operator/config');


function getDataRoot() {
  const root = (operatorConfig.repoRoot || 'C:/ShadowEmpire-Git_Restore_01').replace(/\\/g, '/');
  return path.join(root, 'data');
}

function readJsonSafeFile(filePath, fallback) {
  try {
    if (!fs.existsSync(filePath)) return fallback;
    return JSON.parse(fs.readFileSync(filePath, 'utf8'));
  } catch {
    return fallback;
  }
}

function writeJsonSafeFile(filePath, payload) {
  const dir = path.dirname(filePath);
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(filePath, JSON.stringify(payload, null, 2), 'utf8');
}

function appendRouteRunSnapshot(dossierId, wf001, wf010, routeId) {
  const dataRoot = getDataRoot();
  const file = path.join(dataRoot, 'se_route_runs.json');
  const now = new Date().toISOString();
  const doc = readJsonSafeFile(file, {
    table: 'se_route_runs',
    description: 'Workflow execution runs.',
    records: [],
    created_at: now,
    last_updated: now,
  });
  const records = Array.isArray(doc.records) ? doc.records : [];

  const mk = (wf, label) => ({
    route_run_id: `RR-OP-${Date.now()}-${Math.random().toString(36).slice(2, 8).toUpperCase()}`,
    execution_id: wf?.execution_id || null,
    workflow_id: label,
    workflow_ref: wf?.workflow_id || null,
    status: wf?.status || 'accepted',
    started_at: now,
    stopped_at: null,
    dossier_id: dossierId,
    dossier_ref: dossierId,
    route_id: routeId || null,
    source: 'operator_api_snapshot',
    persisted_at: now,
  });

  records.push(mk(wf001, 'WF-001 Dossier Create Canonical'));
  records.push(mk(wf010, 'WF-010 Parent Orchestrator Canonical'));
  doc.records = records;
  doc.last_updated = now;
  writeJsonSafeFile(file, doc);
}

function appendPacketSnapshot(dossierId, routeId, intentId) {
  const dataRoot = getDataRoot();
  const file = path.join(dataRoot, 'se_packet_index.json');
  const now = new Date().toISOString();
  const doc = readJsonSafeFile(file, { entries: [] });
  const entries = Array.isArray(doc.entries) ? doc.entries : [];
  entries.push({
    packet_id: `packet-op-${Date.now()}`,
    dossier_ref: dossierId,
    dossier_id: dossierId,
    artifact_family: 'orchestration_status_packet',
    artifact_type: 'operator_new_content_job',
    status: 'accepted',
    created_at: now,
    source: 'operator_api_snapshot',
    content: {
      route_id: routeId || null,
      intent_id: intentId || 'new_content_job',
      note: 'Planning packet generated. Actual provider execution is not enabled yet.',
    },
  });
  doc.entries = entries;
  doc.last_updated = now;
  writeJsonSafeFile(file, doc);
}

function appendErrorEvent(event) {
  const dataRoot = getDataRoot();
  const file = path.join(dataRoot, 'se_error_events.json');
  const now = new Date().toISOString();
  const doc = readJsonSafeFile(file, {
    table: 'se_error_events',
    description: 'Error events captured by WF-900.',
    records: [],
    created_at: now,
  });
  const records = Array.isArray(doc.records) ? doc.records : [];
  records.push({
    error_id: `ERR-OP-${Date.now()}-${Math.random().toString(36).slice(2, 7).toUpperCase()}`,
    created_at: now,
    source: 'operator_api',
    ...event,
  });
  doc.records = records;
  doc.last_updated = now;
  writeJsonSafeFile(file, doc);
}

function esc(value) {
  return String(value ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function createOperatorRouter() {
  const router = express.Router();
  const modes = new ModeManager();
  const routes = new RouteManager();
  const taskRouter = new TaskRouter();
  const n8n = new OperatorN8nClient();
  const outputs = new OutputReader();
  const review = new ReviewManager(n8n);
  const alerts = new AlertManager(n8n);
  const troubleshoot = new TroubleshootManager();
  const events = new EventStream();
  const providers = new ProviderRouter();
  const ollamaRunner = new OllamaToolRunner(modes, n8n);
  const skillRuntime = new SkillRuntime();

  function deriveProviderFailure({ wf010 = null, preferredProvider = 'gemini' } = {}) {
    const responseText = JSON.stringify(wf010?.response_body || wf010?.error_details || wf010 || {});
    const gemini503 =
      /GEMINI_HTTP_503/i.test(responseText) ||
      /503/i.test(String(wf010?.http_status || '')) ||
      /GEMINI_HTTP_503/i.test(String(wf010?.error || ''));

    if (gemini503) {
      return {
        error_code: 'CLOUD_PROVIDER_UNAVAILABLE',
        error_class: 'GEMINI_HTTP_503',
        provider_used: preferredProvider,
        model_used: process.env.GEMINI_MODEL || 'gemini-2.5-flash',
        cloud_provider_used: false,
      };
    }

    return {
      error_code: 'WORKFLOW_EXECUTION_FAILED',
      error_class: String(wf010?.error_details?.code || wf010?.error || 'WF010_TRIGGER_FAILED'),
      provider_used: preferredProvider,
      model_used: process.env.GEMINI_MODEL || 'gemini-2.5-flash',
      cloud_provider_used: false,
    };
  }

  function controlledFailureResponse({
    dossierId = null,
    providerPreference = 'gemini',
    wf001 = null,
    wf010 = null,
    n8nRouteReached = false,
    wf010Reached = false,
    errorCode = 'OPERATOR_ROUTE_FAILED',
    errorClass = 'OPERATOR_ROUTE_FAILED',
    message = 'Shadow OS route reached but request could not be completed.',
    routeReached = true,
    requestId = null,
    route = null,
  } = {}) {
    return {
      status: 'FAILED_CONTROLLED',
      error_code: errorCode,
      error_class: errorClass,
      route_reached: routeReached,
      operator_route_reached: routeReached,
      n8n_route_reached: n8nRouteReached,
      wf001_dossier_created: Boolean(dossierId),
      wf010_reached: wf010Reached,
      dossier_id: dossierId || null,
      provider_used: providerPreference || 'gemini',
      model_used: process.env.GEMINI_MODEL || 'gemini-2.5-flash',
      cloud_provider_used: false,
      content_generation_executed: false,
      controlled_failure: true,
      runtime_error_packet_count: 1,
      message,
      route_used: route || null,
      operator_ingress_endpoint: '/operator/new-content-job',
      request_id: requestId || null,
      wf001,
      wf010,
    };
  }

  function getChatContextMapPath() {
    return path.join(getDataRoot(), 'se_openwebui_chat_context_map.json');
  }

  function readChatContextMap() {
    return readJsonSafeFile(getChatContextMapPath(), { chats: {}, last_updated: new Date().toISOString() });
  }

  function writeChatContextMap(doc) {
    writeJsonSafeFile(getChatContextMapPath(), { chats: doc.chats || {}, last_updated: new Date().toISOString() });
  }

  function resolveReferenceDossierId({ explicit, message, channelId }) {
    if (explicit) return explicit;
    const text = String(message || '');
    const match = text.match(/DOSSIER-[A-Z0-9-]+/i);
    if (match) return String(match[0]).toUpperCase();
    const asksForPrevious = /\b(above|latest|previous|that script|this script)\b/i.test(text);
    if (!asksForPrevious || !channelId) return null;
    const map = readChatContextMap();
    return map?.chats?.[String(channelId)]?.last_dossier_id || null;
  }

  function updateChatContext({ channelId, dossierId, missionContext }) {
    if (!channelId || !dossierId) return;
    const map = readChatContextMap();
    map.chats = map.chats || {};
    map.chats[String(channelId)] = {
      channel_id: String(channelId),
      last_dossier_id: dossierId,
      last_mission_hash: missionContext?.mission_hash || null,
      last_topic: missionContext?.normalized_topic || null,
      updated_at: new Date().toISOString(),
    };
    writeChatContextMap(map);
  }

  router.get('/health', async (req, res) => {
    const n8nHealth = await n8n.health();
    res.status(n8nHealth.healthy ? 200 : 503).json({
      status: n8nHealth.healthy ? 'healthy' : 'degraded',
      mode_default: modes.getDefaultMode(),
      runtime_default: modes.getDefaultRuntimeMode(),
      n8n: n8nHealth,
    });
  });

  router.get('/modes', (req, res) => {
    res.json({
      default_mode: modes.getDefaultMode(),
      default_runtime_mode: modes.getDefaultRuntimeMode(),
      operating_modes: modes.listOperatingModes(),
      operational_modes: modes.listOperationalModes(),
      runtime_modes: modes.getRuntimeModes(),
    });
  });

  router.get('/mode/state', (req, res) => {
    res.json({
      status: 'ok',
      state: modes.getState(),
      generated_at: new Date().toISOString(),
    });
  });

  router.post('/modes/set', (req, res) => {
    const mode = req.body?.mode;
    if (!mode) return res.status(400).json({ status: 'failed', reason: 'mode is required' });
    const out = modes.setMode(mode);
    res.status(out.status === 'success' ? 200 : 400).json(out);
  });

  router.post('/runtime/set', (req, res) => {
    const runtime_mode = req.body?.runtime_mode;
    if (!runtime_mode) return res.status(400).json({ status: 'failed', reason: 'runtime_mode is required' });
    const out = modes.setRuntimeMode(runtime_mode);
    res.status(out.status === 'success' ? 200 : 400).json(out);
  });

  router.post('/modes/operational/:mode_id/enable', (req, res) => {
    const actorMode = req.body?.actor_mode || modes.getDefaultMode();
    const out = modes.enableOperationalMode(req.params.mode_id, { actor_mode: actorMode });
    res.status(out.status === 'success' ? 200 : 400).json(out);
  });

  router.post('/modes/operational/:mode_id/disable', (req, res) => {
    const out = modes.disableOperationalMode(req.params.mode_id);
    res.status(out.status === 'success' ? 200 : 400).json(out);
  });

  router.post('/modes/permission-check', (req, res) => {
    const mode = req.body?.mode || modes.getDefaultMode();
    const task = req.body?.task || '';
    const out = modes.checkPermission(mode, task);
    res.status(out.allowed ? 200 : 403).json({ mode, task, ...out });
  });

  router.get('/routes', (req, res) => {
    const mode = req.query.mode || modes.getDefaultMode();
    res.json({
      mode,
      legal_routes: modes.getLegalRoutes(mode),
      default_route: modes.getDefaultRoute(mode),
      routes: routes.listRoutes(),
    });
  });

  router.post('/new-content-job', async (req, res) => {
    let dossierId = req.body?.dossier_id || null;
    let wf001 = null;
    let wf010 = null;
    let route = null;
    let requestId = req.body?.request_id || null;
    let providerPreference = req.body?.provider_preference || 'gemini';
    try {
      const message =
        req.body?.mission_text ||
        req.body?.user_message ||
        req.body?.message ||
        req.body?.topic ||
        'new content job';
      const mode = req.body?.mode || modes.getDefaultMode();
      requestId = requestId || `REQ-${Date.now()}-${Math.random().toString(36).substring(7)}`;
      const creatorId = req.body?.creator_id || req.body?.user_id || 'creator-unknown';
      const channelId = req.body?.channel_id || null;
      const routeMode = req.body?.route_mode || 'production';
      providerPreference = providerPreference || 'gemini';
      const cloudLlmRequired = req.body?.cloud_llm_required !== false;
      const sourceSurface = req.body?.source_surface || 'operator_api';
      const resolved = taskRouter.resolveTaskFromMessage(message);
      const referenceDossierId = resolveReferenceDossierId({
        explicit: req.body?.reference_dossier_id || req.body?.mission_context?.reference_dossier_id || null,
        message,
        channelId,
      });
      const missionContext = {
        original_user_message: String(message || '').trim(),
        normalized_topic: String(req.body?.topic || message || '').trim(),
        intent_id: resolved.intent_id,
        intent_family: resolved.intent_family || (String(resolved.intent_id || '').startsWith('director_') ? 'director_command' : 'content_command'),
        director_requested: resolved.director_requested || null,
        reference_dossier_id: referenceDossierId,
        openwebui_chat_id: channelId || null,
        mission_hash: crypto.createHash('sha256').update(String(message || '')).digest('hex').slice(0, 16),
        materialization_source: sourceSurface,
        created_at: new Date().toISOString(),
      };
      if (!missionContext.normalized_topic) {
        missionContext.normalized_topic = missionContext.original_user_message;
      }

      if (!missionContext.original_user_message) {
        return res.status(200).json(
          controlledFailureResponse({
            dossierId,
            providerPreference,
            wf001,
            wf010,
            n8nRouteReached: false,
            wf010Reached: false,
            errorCode: 'MISSION_CONTEXT_MISSING',
            errorClass: 'MISSION_CONTEXT_MISSING',
            message: 'Mission context is missing from request payload.',
            routeReached: true,
            requestId,
            route,
          })
        );
      }

      if (resolved.requires_reference_context && !missionContext.reference_dossier_id) {
        return res.status(200).json(
          controlledFailureResponse({
            dossierId,
            providerPreference,
            wf001,
            wf010,
            n8nRouteReached: false,
            wf010Reached: false,
            errorCode: 'REFERENCE_DOSSIER_NOT_FOUND',
            errorClass: 'REFERENCE_DOSSIER_NOT_FOUND',
            message: 'Director command requires a prior dossier context, but none could be resolved.',
            routeReached: true,
            requestId,
            route,
          })
        );
      }
      const modeCheck = modes.validateModeForTask(mode, {
        id: resolved.intent_id,
        allowed_modes: resolved.task_contract?.allowed_modes || [],
      });
      route = req.body?.route_id || modes.getDefaultRoute(mode);
      const routeCheck = modes.validateRoute(mode, route);

      if (!modeCheck.allowed || !routeCheck.allowed) {
        return res.status(200).json(
          controlledFailureResponse({
            dossierId,
            providerPreference,
            wf001,
            wf010,
            n8nRouteReached: false,
            wf010Reached: false,
            errorCode: 'MODE_OR_ROUTE_BLOCKED',
            errorClass: 'MODE_OR_ROUTE_BLOCKED',
            message: modeCheck.reason || routeCheck.reason || 'Mode/route validation blocked this request.',
            routeReached: true,
            requestId,
            route,
          })
        );
      }

      // Deterministic correlation id carried through WF-001/WF-010
      const operatorRequestId = requestId;
      const requestStartTime = Date.now();
      const requestStartTimeISO = new Date(requestStartTime).toISOString();

      wf001 = await n8n.trigger('WF-001', {
        topic: req.body?.topic || missionContext.normalized_topic || message,
        context: req.body?.context || 'YouTube video',
        mode,
        route_id: route,
        operator_request_id: operatorRequestId,
        request_timestamp: requestStartTimeISO,
        creator_id: creatorId,
        channel_id: channelId,
        route_mode: routeMode,
        provider_preference: providerPreference,
        cloud_llm_required: cloudLlmRequired,
        source_surface: sourceSurface,
        intent_id: resolved.intent_id,
        director_requested: resolved.director_requested || null,
        reference_dossier_id: missionContext.reference_dossier_id,
        mission_context: missionContext,
      });

      if (wf001?.status === 'failed') {
        appendErrorEvent({
          dossier_id: dossierId,
          workflow_id: 'WF-001',
          error_code: 'WF001_TRIGGER_FAILED',
          message: 'WF-001 trigger failed from operator/new-content-job',
          details: wf001,
        });
        return res.status(200).json(
          controlledFailureResponse({
            dossierId,
            providerPreference,
            wf001,
            wf010,
            n8nRouteReached: true,
            wf010Reached: false,
            errorCode: 'WF001_TRIGGER_FAILED',
            errorClass: String(wf001?.error_details?.code || wf001?.error || 'WF001_TRIGGER_FAILED'),
            message: 'Shadow OS route reached but dossier creation failed in WF-001.',
            routeReached: true,
            requestId,
            route,
          })
        );
      }

      if (!dossierId) {
        dossierId = await waitForNewDossier(missionContext.normalized_topic, 30000, requestStartTime, route, operatorRequestId);
      }

      if (!dossierId) {
        appendErrorEvent({
          dossier_id: null,
          workflow_id: 'WF-001',
          error_code: 'DOSSIER_CREATION_TIMEOUT',
          message: 'WF-001 completed but dossier correlation timed out',
          details: { wf001, request_id: requestId, route },
        });
        return res.status(200).json(
          controlledFailureResponse({
            dossierId: null,
            providerPreference,
            wf001,
            wf010,
            n8nRouteReached: true,
            wf010Reached: false,
            errorCode: 'DOSSIER_CREATION_TIMEOUT',
            errorClass: 'DOSSIER_CREATION_TIMEOUT',
            message: 'Shadow OS route reached, but dossier_id correlation timed out.',
            routeReached: true,
            requestId,
            route,
          })
        );
      }

      wf010 = await n8n.trigger('WF-010', {
        dossier_id: dossierId,
        route_id: route,
        user_mode: mode,
        intent_id: resolved.intent_id,
        topic: missionContext.normalized_topic,
        user_message: message,
        request_id: requestId,
        creator_id: creatorId,
        channel_id: channelId,
        route_mode: routeMode,
        provider_preference: providerPreference,
        cloud_llm_required: cloudLlmRequired,
        source_surface: sourceSurface,
        director_requested: resolved.director_requested || null,
        reference_dossier_id: missionContext.reference_dossier_id,
        mission_context: missionContext,
      });

      if (wf010?.status !== 'failed') {
        updateChatContext({ channelId, dossierId, missionContext });
        appendRouteRunSnapshot(dossierId, wf001, wf010, route);
        appendPacketSnapshot(dossierId, route, resolved.intent_id);
        return res.status(200).json({
          status: 'accepted',
          dossier_id: dossierId,
          route_used: route,
          operator_ingress_endpoint: '/operator/new-content-job',
          request_id: requestId,
          intent: resolved,
          mission_context: missionContext,
          wf001,
          wf010,
          provider_boundary_note: 'Provider execution depends on runtime provider_router and workflow routing.',
        });
      }

      appendErrorEvent({
        dossier_id: dossierId,
        workflow_id: 'WF-010',
        error_code: 'WF010_TRIGGER_FAILED',
        message: 'WF-010 trigger failed from operator/new-content-job',
        details: wf010,
      });

      const providerFailure = deriveProviderFailure({ wf010, preferredProvider: providerPreference });
      return res.status(200).json(
        controlledFailureResponse({
          dossierId,
          providerPreference: providerFailure.provider_used,
          wf001,
          wf010,
          n8nRouteReached: true,
          wf010Reached: true,
          errorCode: providerFailure.error_code,
          errorClass: providerFailure.error_class,
          message:
            providerFailure.error_code === 'CLOUD_PROVIDER_UNAVAILABLE'
              ? 'Shadow OS route reached, but Gemini is temporarily unavailable. Production content generation is blocked until provider recovers.'
              : 'Shadow OS route reached, but WF-010 failed before content generation could complete.',
          routeReached: true,
          requestId,
          route,
        })
      );
    } catch (error) {
      const errorClass = String(error?.code || error?.name || 'OPERATOR_ROUTE_EXCEPTION');
      appendErrorEvent({
        dossier_id: dossierId,
        workflow_id: 'WF-010',
        error_code: 'OPERATOR_ROUTE_EXCEPTION',
        message: 'Unhandled exception in /operator/new-content-job',
        details: {
          error_class: errorClass,
          error_message: String(error?.message || error),
          request_id: requestId,
          route,
        },
      });
      return res.status(200).json(
        controlledFailureResponse({
          dossierId,
          providerPreference,
          wf001,
          wf010,
          n8nRouteReached: Boolean(wf001 || wf010),
          wf010Reached: Boolean(wf010),
          errorCode: 'OPERATOR_API_UNAVAILABLE',
          errorClass,
          message:
            'Shadow OS route reached, but Operator API encountered a runtime exception. Retry once service stabilizes.',
          routeReached: true,
          requestId,
          route,
        })
      );
    }
  });

  // Helper function to wait for new dossier to appear
  // operatorRequestId is the unique per-request identifier for deterministic correlation
  async function waitForNewDossier(topicHint, maxWaitMs = 30000, requestStartTime = null, routeId = null, operatorRequestId = null) {
    const timeoutAt = Date.now() + maxWaitMs;
    const fs = require('fs');
    const path = require('path');
    const config = require('../../operator/config');

    // Use absolute paths from config (normalize to use forward slashes for consistency)
    const repoRoot = (config.repoRoot || 'C:/ShadowEmpire-Git_Restore_01').replace(/\\/g, '/');
    const dossiersDir = `${repoRoot}/dossiers`;
    const dataDir = `${repoRoot}/data`;

    // Correlation criteria: dossier must be created after request start time
    // Primary: Match by operatorRequestId if available
    // Secondary: Match by request timestamp
    const minCreatedTime = requestStartTime ? new Date(requestStartTime).toISOString() : null;
    const requestId = operatorRequestId;

    let indexFound = false;
    let fallbackUsed = false;
    let correlatedDossier = null;

    while (Date.now() < timeoutAt) {
      // PRIMARY: Check se_dossier_index.json first (authoritative source)
      try {
        const indexPath = path.join(dataDir, 'se_dossier_index.json');
        if (fs.existsSync(indexPath)) {
          indexFound = true;
          const data = JSON.parse(fs.readFileSync(indexPath, 'utf8'));
          const dossiers = data.records || data.dossiers || [];
          if (dossiers.length > 0) {
            // Filter dossiers created after request start time and pass basic validation
            const validDossiers = dossiers.filter(d => {
              if (!minCreatedTime) return true; // If no start time, accept any
              const dosCreated = d.created_at || '';
              // Only accept dossiers created at or after request start time
              return dosCreated >= minCreatedTime;
            });

            // PRIORITY 1: Look for exact operatorRequestId match (deterministic correlation)
            if (requestId) {
              const requestIdMatch = validDossiers.find(d => {
                const meta = d.operator_request_id || d.metadata?.operator_request_id || '';
                return meta === requestId;
              });
              if (requestIdMatch?.dossier_id) {
                console.log(`[Operator] Dossier correlated via requestId: ${requestIdMatch.dossier_id} (requestId=${requestId})`);
                return requestIdMatch.dossier_id;
              }
            }

            // PRIORITY 2: Look for topic match within valid dossiers
            if (validDossiers.length > 0) {
              let bestMatch = null;

              // Search for exact topic match
              for (let i = validDossiers.length - 1; i >= 0; i--) {
                const dos = validDossiers[i];
                if (topicHint && dos.dossier_id && dos.topic) {
                  // Normalize both for comparison (lowercase, trim)
                  const normalizedDosTopicstart = dos.topic.toLowerCase().substring(0, 50);
                  const normalizedHint = topicHint.toLowerCase().substring(0, 50);
                  if (normalizedDosTopicstart.includes(normalizedHint.substring(0, 20)) ||
                      normalizedHint.includes(normalizedDosTopicstart.substring(0, 20))) {
                    bestMatch = dos;
                    break;
                  }
                }
              }

              // PRIORITY 3: Fall back to newest valid dossier
              if (!bestMatch && validDossiers.length > 0) {
                bestMatch = validDossiers[validDossiers.length - 1];
              }

              if (bestMatch?.dossier_id) {
                correlatedDossier = bestMatch.dossier_id;
                console.log(`[Operator] Dossier correlated via index: ${bestMatch.dossier_id} (created=${bestMatch.created_at}, min_time=${minCreatedTime}, requestId_match=false)`);
                return correlatedDossier;
              }
            }
          }
        }
      } catch (err) {
        console.log(`[Operator] Index check error: ${err.message}`);
        // Index check failed, will fall through to secondary fallback
      }

      // SECONDARY: Fallback to file scan only if index was missing or failed
      try {
        if (fs.existsSync(dossiersDir)) {
          const files = fs.readdirSync(dossiersDir)
            .filter(f => f.startsWith('DOSSIER-') && f.endsWith('.json'))
            .sort();

          if (files.length > 0) {
            // Process files in reverse order (newest first) and filter by creation time
            for (let i = files.length - 1; i >= 0; i--) {
              const newest = files[i];
              const dossierId = newest.replace('.json', '');
              const filePath = `${dossiersDir}/${newest}`;

              try {
                const fileContent = JSON.parse(fs.readFileSync(filePath, 'utf8'));
                const dosCreated = fileContent?._created_at || fileContent?.created_at || '';

                // STRICT TIME FILTERING: Only accept dossiers created at or after request start time
                if (minCreatedTime && dosCreated < minCreatedTime) {
                  console.log(`[Operator] Skipping stale dossier: ${dossierId} (created=${dosCreated} < min=${minCreatedTime})`);
                  continue; // Skip stale dossiers
                }

                // CHECK 1: Exact requestId match (if searching with requestId)
                if (requestId) {
                  const meta = fileContent?.operator_request_id || fileContent?.metadata?.operator_request_id || '';
                  if (meta === requestId && fileContent?.dossier_id && fileContent?.namespaces?.intake?.topic) {
                    fallbackUsed = true;
                    console.log(`[Operator] Dossier correlated via file scan (requestId): ${dossierId} (requestId=${requestId})`);
                    return dossierId;
                  }
                }

                // CHECK 2: Topic match in file
                if (fileContent?.dossier_id && fileContent?.namespaces?.intake?.topic) {
                  fallbackUsed = true;
                  console.log(`[Operator] Dossier correlated via file scan: ${dossierId} (created=${dosCreated}, min_time=${minCreatedTime})`);
                  return dossierId;
                }
              } catch (e) {
                // File scan parsing failed, continue polling
              }
            }
          }
        }
      } catch (err) {
        console.log(`[Operator] File scan error: ${err.message}`);
        // File scan error, continue polling
      }

      await new Promise((resolve) => setTimeout(resolve, 500));
    }
    console.log(`[Operator] Dossier detection timeout after ${maxWaitMs}ms (index_found=${indexFound}, fallback_used=${fallbackUsed}, min_created_time=${minCreatedTime}, request_id=${requestId})`);
    return null;
  }

  router.post('/run', async (req, res) => {
    const out = await ollamaRunner.run(req.body?.message || '', {
      mode: req.body?.mode,
      topic_context: req.body?.context,
      dossier_id: req.body?.dossier_id,
    });
    res.status(out.status === 'failed' ? 502 : (out.status === 'blocked' ? 403 : 200)).json(out);
  });

  router.get('/dossier/:id', (req, res) => {
    res.json(outputs.getDossier(req.params.id));
  });

  router.get('/outputs/:id', async (req, res) => {
    const out = await outputs.getDossierOutputs(req.params.id);
    res.json(out);
  });

  router.post('/skill-runtime', async (req, res) => {
    try {
      const out = await skillRuntime.execute(req.body || {});
      if (out.status !== 'SUCCESS') {
        // Return controlled failure JSON so callers can surface root cause
        // instead of a generic HTTP error wrapper.
        return res.status(200).json({
          status: 'FAILED',
          error: out.error || 'skill_runtime_failed',
        });
      }
      return res.status(200).json({
        status: 'SUCCESS',
        runtime_packet: out.runtime_packet,
        skill_execution_result: out.skill_execution_result,
      });
    } catch (error) {
      return res.status(500).json({
        status: 'FAILED',
        error: String(error?.message || error),
      });
    }
  });

  router.get('/library', (req, res) => {
    res.json(outputs.getLibrary());
  });

  router.post('/approve/:id', async (req, res) => {
    const out = await review.approveOutput(req.params.id, req.body?.reviewer || 'founder');
    res.status(out.status === 'failed' ? 502 : 200).json(out);
  });

  router.post('/remodify/:id', async (req, res) => {
    const out = await review.requestChanges(req.params.id, req.body?.instructions, req.body?.reviewer || 'founder');
    res.status(out.status === 'failed' ? 502 : 200).json(out);
  });

  router.post('/replay/:id', async (req, res) => {
    const dossier = outputs.getDossier(req.params.id);
    const exists = Boolean(dossier?.dossier || dossier?.index_record);

    if (!exists) {
      appendErrorEvent({
        dossier_id: req.params.id,
        workflow_id: 'WF-021',
        error_code: 'INVALID_DOSSIER_ID',
        message: 'Replay requested for missing dossier',
        details: {
          stage: req.body?.stage || 'script',
          checkpoint: req.body?.checkpoint || 'latest',
        },
      });
      return res.status(404).json({
        status: 'failed',
        reason: 'dossier_not_found',
        dossier_id: req.params.id,
      });
    }

    const out = await review.replayStage(
      req.params.id,
      req.body?.stage || 'script',
      req.body?.checkpoint || 'latest',
      req.body?.instructions || null
    );

    if (out.status === 'failed') {
      appendErrorEvent({
        dossier_id: req.params.id,
        workflow_id: 'WF-021',
        error_code: 'WF021_TRIGGER_FAILED',
        message: 'Replay trigger failed',
        details: out,
      });
    }

    res.status(out.status === 'failed' ? 502 : 200).json(out);
  });

  router.get('/alerts', async (req, res) => {
    res.json(await alerts.listAlerts());
  });

  router.post('/alerts/:alert_id/acknowledge', (req, res) => {
    const out = alerts.acknowledgeAlert(req.params.alert_id);
    res.json(out);
  });

  router.post('/alerts/:alert_id/escalate', (req, res) => {
    const out = alerts.escalateAlert(req.params.alert_id, req.body?.note || null);
    res.json(out);
  });

  router.get('/events', (req, res) => {
    res.json(events.getEvents(Number(req.query.limit || 50)));
  });

  router.get('/runs/:run_id/status', (req, res) => {
    const out = outputs.getRunStatus(req.params.run_id);
    res.status(out.status === 'not_found' ? 404 : 200).json(out);
  });

  router.get('/troubleshoot/dossier/:id', (req, res) => {
    res.json(troubleshoot.traceDossier(req.params.id));
  });

  router.get('/troubleshoot/packet/:id', (req, res) => {
    res.json(troubleshoot.tracePacket(req.params.id));
  });

  router.get('/providers', (req, res) => {
    res.json(providers.listProviders());
  });

  router.get('/providers/:id', (req, res) => {
    const status = providers.getProviderStatus(req.params.id);
    res.status(status.status === 'not_found' ? 404 : 200).json(status);
  });

  router.get('/tasks', (req, res) => {
    res.json({
      tasks: taskRouter.listTaskContracts(),
      registered_workflows: n8n.getRegisteredWorkflows(),
    });
  });

  router.get('/dossier/:id/timeline', async (req, res) => {
    const timeline = await outputs.getDossierTimeline(req.params.id);
    res.json(timeline);
  });

  router.get('/job/:dossier_id', async (req, res) => {
    const dossier = outputs.getDossier(req.params.dossier_id);
    const out = await outputs.getDossierOutputs(req.params.dossier_id);
    const grouped = out.grouped_by_type || {};
    const rows = Object.entries(grouped)
      .map(([k, v]) => `<tr><td>${esc(k)}</td><td>${esc(Array.isArray(v) ? v.length : 0)}</td></tr>`)
      .join('');
    const reviewable = out.packets_count > 0;

    const html = `<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Operator Job Review - ${esc(req.params.dossier_id)}</title>
  <style>
    body { font-family: Segoe UI, Arial, sans-serif; margin: 24px; background: #f8fafc; color: #0f172a; }
    .card { background: #fff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px; margin-bottom: 16px; }
    h1 { margin: 0 0 12px 0; font-size: 22px; }
    h2 { margin: 0 0 10px 0; font-size: 18px; }
    table { width: 100%; border-collapse: collapse; }
    th, td { border: 1px solid #e2e8f0; padding: 8px; text-align: left; }
    .muted { color: #475569; font-size: 13px; }
    .badge { display: inline-block; padding: 4px 8px; border-radius: 999px; background: #e2e8f0; font-size: 12px; }
    .btn { display: inline-block; margin-right: 8px; padding: 8px 10px; border-radius: 8px; border: 1px solid #cbd5e1; background: #fff; text-decoration: none; color: #0f172a; }
  </style>
</head>
<body>
  <div class="card">
    <h1>Shadow Operator Review Console</h1>
    <div class="muted">Dossier ID: <b>${esc(req.params.dossier_id)}</b></div>
    <div class="muted">Provider boundary: Planning packet generated. Actual provider execution is not enabled yet.</div>
  </div>
  <div class="card">
    <h2>Dossier Summary</h2>
    <div>Status: <span class="badge">${esc(dossier.index_record?.status || dossier.dossier?.status || 'unknown')}</span></div>
    <div>Current Stage: <span class="badge">${esc(dossier.index_record?.current_stage || dossier.index_record?.workflow_stage || 'unknown')}</span></div>
    <div>Topic: ${esc(dossier.index_record?.topic || dossier.dossier?.topic || 'n/a')}</div>
  </div>
  <div class="card">
    <h2>Generated Output Groups</h2>
    <table>
      <thead><tr><th>Output Type</th><th>Count</th></tr></thead>
      <tbody>${rows || '<tr><td colspan="2">No outputs yet.</td></tr>'}</tbody>
    </table>
  </div>
  <div class="card">
    <h2>Review Actions</h2>
    <div class="muted">Reviewable outputs available: <b>${reviewable ? 'YES' : 'NO'}</b></div>
    <div style="margin-top:10px">
      <a class="btn" href="/operator/outputs/${esc(req.params.dossier_id)}">View Raw Outputs JSON</a>
      <a class="btn" href="/operator/dossier/${esc(req.params.dossier_id)}/timeline">View Timeline JSON</a>
    </div>
  </div>
</body>
</html>`;

    res.setHeader('Content-Type', 'text/html; charset=utf-8');
    res.send(html);
  });

  return router;
}

module.exports = createOperatorRouter;

