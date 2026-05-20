const fs = require('fs');
const path = require('path');
const sqlite3 = require('sqlite3');
const config = require('./config');

function isoToMs(value) {
  const t = Date.parse(value || '');
  return Number.isFinite(t) ? t : null;
}

function toIsoSqlite(value) {
  if (!value) return null;
  return String(value).replace(' ', 'T') + 'Z';
}

function reviveFlatted(refs) {
  if (!Array.isArray(refs) || refs.length === 0) return null;
  const cache = new Map();
  const isRef = (v) => v && typeof v === 'string' && /^\d+$/.test(v);

  function reviveNode(node) {
    if (isRef(node)) return reviveIndex(Number(node));
    if (Array.isArray(node)) return node.map(reviveNode);
    if (node && typeof node === 'object') {
      const out = {};
      for (const [k, v] of Object.entries(node)) out[k] = reviveNode(v);
      return out;
    }
    return node;
  }

  function reviveIndex(index) {
    if (cache.has(index)) return cache.get(index);
    const raw = refs[index];
    if (Array.isArray(raw)) {
      const out = [];
      cache.set(index, out);
      for (const v of raw) out.push(reviveNode(v));
      return out;
    }
    if (raw && typeof raw === 'object') {
      const out = {};
      cache.set(index, out);
      for (const [k, v] of Object.entries(raw)) out[k] = reviveNode(v);
      return out;
    }
    cache.set(index, raw);
    return raw;
  }

  return reviveIndex(0);
}

function iterNodeJsonItems(runData) {
  const out = [];
  if (!runData || typeof runData !== 'object') return out;
  for (const [nodeName, nodeRuns] of Object.entries(runData)) {
    if (!Array.isArray(nodeRuns)) continue;
    for (const run of nodeRuns) {
      const main = run?.data?.main;
      if (!Array.isArray(main)) continue;
      for (const channel of main) {
        if (!Array.isArray(channel)) continue;
        for (const item of channel) {
          if (item?.json && typeof item.json === 'object') {
            out.push({ node_name: nodeName, json: item.json });
          }
        }
      }
    }
  }
  return out;
}

function workflowRef(name) {
  const m = String(name || '').match(/(?:CWF|WF)-\d{3}/);
  return m ? m[0] : null;
}

class N8nExecutionReconciler {
  constructor() {
    const defaultDb = 'C:/ShadowEmpire/n8n_user_restore_01/.n8n/database.sqlite';
    this.dbPath = process.env.SHADOW_N8N_DB_PATH || defaultDb;
    this.repoRoot = (config.repoRoot || 'C:/ShadowEmpire-Git_Restore_01').replace(/\\/g, '/');
  }

  async listDossierExecutions(dossierId) {
    if (!dossierId) return [];
    if (!fs.existsSync(this.dbPath)) return [];

    const like = `%${dossierId}%`;
    const sql = `
      SELECT DISTINCT
        e.id AS execution_id,
        e.status AS execution_status,
        e.startedAt AS started_at,
        e.stoppedAt AS stopped_at,
        w.name AS workflow_name
      FROM execution_data ed
      JOIN execution_entity e ON e.id = ed.executionId
      LEFT JOIN workflow_entity w ON w.id = e.workflowId
      WHERE (ed.workflowData LIKE ? OR ed.data LIKE ?)
      ORDER BY e.id ASC
    `;

    return new Promise((resolve) => {
      const db = new sqlite3.Database(this.dbPath, sqlite3.OPEN_READONLY, (openErr) => {
        if (openErr) return resolve([]);
      });

      db.all(sql, [like, like], (err, rows) => {
        if (err || !Array.isArray(rows)) {
          db.close(() => resolve([]));
          return;
        }

        const out = rows
          .map((r) => ({
            execution_id: r.execution_id,
            workflow_name: r.workflow_name || '',
            workflow_ref: workflowRef(r.workflow_name),
            status: r.execution_status || 'unknown',
            started_at: toIsoSqlite(r.started_at),
            stopped_at: toIsoSqlite(r.stopped_at),
            source: 'n8n_execution_db',
          }))
          .filter((r) => r.workflow_ref && /^(?:CWF|WF)-\d{3}$/.test(r.workflow_ref));

        db.close(() => resolve(out));
      });
    });
  }

  buildExecutionPackets(dossierId, executions = []) {
    return executions.map((e) => ({
      packet_id: `packet-n8n-exec-${e.execution_id}`,
      instance_id: `packet-n8n-exec-${e.execution_id}`,
      dossier_id: dossierId,
      dossier_ref: dossierId,
      artifact_family: 'workflow_execution_event',
      artifact_type: e.workflow_ref,
      status: e.status,
      created_at: e.stopped_at || e.started_at || new Date().toISOString(),
      source: 'n8n_execution_db',
      content: {
        n8n_execution_id: e.execution_id,
        workflow_ref: e.workflow_ref,
        workflow_name: e.workflow_name,
        started_at: e.started_at,
        stopped_at: e.stopped_at,
      },
    }));
  }

  async listDossierRuntimePackets(dossierId) {
    if (!dossierId) return [];
    if (!fs.existsSync(this.dbPath)) return [];

    const like = `%${dossierId}%`;
    const sql = `
      SELECT
        e.id AS execution_id,
        e.status AS execution_status,
        e.startedAt AS started_at,
        e.stoppedAt AS stopped_at,
        w.name AS workflow_name,
        ed.data AS execution_data
      FROM execution_data ed
      JOIN execution_entity e ON e.id = ed.executionId
      LEFT JOIN workflow_entity w ON w.id = e.workflowId
      WHERE (ed.workflowData LIKE ? OR ed.data LIKE ?)
      ORDER BY e.id ASC
    `;

    return new Promise((resolve) => {
      const db = new sqlite3.Database(this.dbPath, sqlite3.OPEN_READONLY, (openErr) => {
        if (openErr) return resolve([]);
      });

      db.all(sql, [like, like], (err, rows) => {
        if (err || !Array.isArray(rows)) {
          db.close(() => resolve([]));
          return;
        }

        const packets = [];
        for (const row of rows) {
          const wfRef = workflowRef(row.workflow_name);
          if (!wfRef) continue;
          try {
            const parsed = JSON.parse(row.execution_data || 'null');
            const revived = reviveFlatted(parsed);
            const items = iterNodeJsonItems(revived?.resultData?.runData);
            for (const item of items) {
              const rp = item?.json?.runtime_packet;
              if (!rp || typeof rp !== 'object') continue;
              const family = String(rp.artifact_family || '').trim();
              if (!family) continue;
              const sourceDossier = rp.dossier_ref || rp.dossier_id || null;
              const dossierRef = (!sourceDossier || sourceDossier === 'DOSSIER-UNSPECIFIED')
                ? dossierId
                : sourceDossier;
              const packetId = rp.packet_id || rp.instance_id || `packet-n8n-runtime-${row.execution_id}-${Date.now()}`;
              packets.push({
                ...rp,
                packet_id: packetId,
                instance_id: rp.instance_id || packetId,
                dossier_ref: dossierRef,
                dossier_id: dossierRef,
                source: 'n8n_execution_data',
                source_workflow: rp.source_workflow || wfRef,
                source_execution_id: row.execution_id,
                source_node: item.node_name || rp.source_node || 'unknown_node',
                created_at: rp.created_at || toIsoSqlite(row.stopped_at) || toIsoSqlite(row.started_at) || new Date().toISOString(),
                status: rp.status || row.execution_status || 'CREATED',
              });
            }
          } catch {
            // best-effort decode
          }
        }

        const dedup = new Map();
        for (const p of packets) {
          const key = p.packet_id || p.instance_id || JSON.stringify(p);
          dedup.set(key, p);
        }
        db.close(() => resolve(Array.from(dedup.values())));
      });
    });
  }

  async listDossierRuntimeErrors(dossierId) {
    if (!dossierId) return [];
    if (!fs.existsSync(this.dbPath)) return [];

    const like = `%${dossierId}%`;
    const sql = `
      SELECT
        e.id AS execution_id,
        e.status AS execution_status,
        e.startedAt AS started_at,
        e.stoppedAt AS stopped_at,
        w.name AS workflow_name,
        ed.data AS execution_data
      FROM execution_data ed
      JOIN execution_entity e ON e.id = ed.executionId
      LEFT JOIN workflow_entity w ON w.id = e.workflowId
      WHERE (ed.workflowData LIKE ? OR ed.data LIKE ?)
      ORDER BY e.id ASC
    `;

    return new Promise((resolve) => {
      const db = new sqlite3.Database(this.dbPath, sqlite3.OPEN_READONLY, (openErr) => {
        if (openErr) return resolve([]);
      });

      db.all(sql, [like, like], (err, rows) => {
        if (err || !Array.isArray(rows)) {
          db.close(() => resolve([]));
          return;
        }

        const errors = [];
        for (const row of rows) {
          const wfRef = workflowRef(row.workflow_name);
          if (!wfRef) continue;

          try {
            const parsed = JSON.parse(row.execution_data || 'null');
            const revived = reviveFlatted(parsed);
            const items = iterNodeJsonItems(revived?.resultData?.runData);
            for (const item of items) {
              const runtime = item?.json?.runtime;
              const hadError = runtime?.had_error === true;
              const message = String(runtime?.error_message || '').trim();
              if (!hadError || !message) continue;

              const safeNode = String(item.node_name || 'unknown_node').replace(/[^a-zA-Z0-9]/g, '_');
              errors.push({
                packet_id: `packet-n8n-runtime-error-${row.execution_id}-${safeNode}`,
                instance_id: `packet-n8n-runtime-error-${row.execution_id}-${safeNode}`,
                dossier_id: dossierId,
                dossier_ref: dossierId,
                artifact_family: 'runtime_error_packet',
                artifact_type: wfRef,
                status: 'ERROR',
                created_at: toIsoSqlite(row.stopped_at) || toIsoSqlite(row.started_at) || new Date().toISOString(),
                source: 'n8n_execution_data',
                source_workflow: wfRef,
                source_execution_id: row.execution_id,
                source_node: item.node_name,
                content: {
                  message,
                  workflow_name: row.workflow_name,
                  execution_status: row.execution_status || 'unknown',
                },
              });
            }
          } catch {
            // Ignore decode failures and keep best-effort reconciliation.
          }
        }

        db.close(() => resolve(errors));
      });
    });
  }

  reconcileOrphanPackets(dossierId, packets = [], executions = []) {
    if (!Array.isArray(packets) || packets.length === 0) return [];
    if (!Array.isArray(executions) || executions.length === 0) return [];

    const executionTimes = executions
      .map((e) => [isoToMs(e.started_at), isoToMs(e.stopped_at)])
      .flat()
      .filter((v) => Number.isFinite(v));
    if (executionTimes.length === 0) return [];

    const minMs = Math.min(...executionTimes) - 60_000;
    const maxMs = Math.max(...executionTimes) + 60_000;

    const orphan = packets.filter((p) => {
      const hasDossier = Boolean(p?.dossier_id || p?.dossier_ref || p?.dossierRef);
      if (hasDossier) return false;
      const packetId = String(p.packet_id || p.instance_id || '');
      const maybeWorkflowPacket = /^WF-\d{3}-COMP-/.test(packetId);
      if (!maybeWorkflowPacket) return false;
      const createdMs = isoToMs(p.created_at);
      if (!Number.isFinite(createdMs)) return false;
      return createdMs >= minMs && createdMs <= maxMs;
    });

    return orphan.map((p) => ({
      ...p,
      dossier_id: dossierId,
      dossier_ref: dossierId,
      source: p.source || 'packet_index_reconciled',
      reconciliation: {
        method: 'time_window_match',
        matched_to: 'n8n_execution_db_window',
      },
    }));
  }
}

module.exports = N8nExecutionReconciler;
