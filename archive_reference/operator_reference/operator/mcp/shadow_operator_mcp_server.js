/**
 * Shadow Operator MCP Server (Stdio-based)
 *
 * Real MCP server supporting JSON-RPC style communication over stdin/stdout.
 * R4B patch: Converted from facade to stdio MCP server (2026-05-03).
 *
 * Protocol: Each line is a JSON-RPC 2.0 request/response.
 * Calls Operator API at http://localhost:5050/operator/* endpoints.
 */

const readline = require('readline');
const http = require('http');

/**
 * Execute HTTP request to Operator API
 */
function callOperatorAPI(method, path, body = null) {
  return new Promise((resolve, reject) => {
    const url = new URL(`http://localhost:5050/operator${path}`);
    const options = {
      hostname: url.hostname,
      port: url.port,
      path: url.pathname + url.search,
      method: method,
      headers: {
        'Content-Type': 'application/json',
      },
    };

    const req = http.request(options, (res) => {
      let data = '';
      res.on('data', (chunk) => {
        data += chunk;
      });
      res.on('end', () => {
        try {
          resolve({
            status: res.statusCode,
            data: JSON.parse(data),
          });
        } catch (e) {
          resolve({
            status: res.statusCode,
            data: { error: 'Invalid JSON response', raw: data },
          });
        }
      });
    });

    req.on('error', (err) => {
      reject({
        error: 'Failed to connect to Operator API',
        details: err.message,
      });
    });

    if (body) {
      req.write(JSON.stringify(body));
    }
    req.end();
  });
}

/**
 * MCP Tool: create_content_job
 * Creates a new content job by calling POST /operator/new-content-job
 */
async function create_content_job(params = {}) {
  try {
    const result = await callOperatorAPI('POST', '/new-content-job', {
      topic: params.topic || params.message || 'new content job',
      context: params.context || 'YouTube video',
      mode: params.mode || 'creator',
      route_id: params.route_id || undefined,
    });
    return {
      status: result.status === 200 ? 'success' : 'failed',
      dossier_id: result.data?.dossier_id,
      execution_id: result.data?.wf001?.execution_id,
      message: result.data?.error_message || 'Job created',
    };
  } catch (err) {
    return { status: 'error', error: err.error, details: err.details };
  }
}

/**
 * MCP Tool: inspect_dossier
 * Inspects a dossier by calling GET /operator/dossier/{dossier_id}
 */
async function inspect_dossier(params = {}) {
  if (!params.dossier_id) {
    return { status: 'error', error: 'dossier_id is required' };
  }
  try {
    const result = await callOperatorAPI('GET', `/dossier/${encodeURIComponent(params.dossier_id)}`);
    return {
      status: result.status === 200 ? 'success' : 'failed',
      dossier: result.data,
    };
  } catch (err) {
    return { status: 'error', error: err.error };
  }
}

/**
 * MCP Tool: list_outputs
 * Lists outputs for a dossier by calling GET /operator/outputs/{dossier_id}
 */
async function list_outputs(params = {}) {
  if (!params.dossier_id) {
    return { status: 'error', error: 'dossier_id is required' };
  }
  try {
    const result = await callOperatorAPI('GET', `/outputs/${encodeURIComponent(params.dossier_id)}`);
    return {
      status: result.status === 200 ? 'success' : 'failed',
      outputs: result.data,
    };
  } catch (err) {
    return { status: 'error', error: err.error };
  }
}

/**
 * MCP Tool: approve_output
 * Approves output by calling POST /operator/approve
 */
async function approve_output(params = {}) {
  if (!params.dossier_id) {
    return { status: 'error', error: 'dossier_id is required' };
  }
  try {
    const result = await callOperatorAPI('POST', '/approve', {
      dossier_id: params.dossier_id,
      reviewer: params.reviewer || 'founder',
      decision: 'approve',
    });
    return {
      status: result.status === 200 ? 'success' : 'failed',
      approval: result.data,
    };
  } catch (err) {
    return { status: 'error', error: err.error };
  }
}

/**
 * MCP Tool: request_changes
 * Requests changes by calling POST /operator/request-changes
 */
async function request_changes(params = {}) {
  if (!params.dossier_id) {
    return { status: 'error', error: 'dossier_id is required' };
  }
  try {
    const result = await callOperatorAPI('POST', '/request-changes', {
      dossier_id: params.dossier_id,
      changes_requested: params.changes || '',
      reviewer: params.reviewer || 'founder',
    });
    return {
      status: result.status === 200 ? 'success' : 'failed',
      result: result.data,
    };
  } catch (err) {
    return { status: 'error', error: err.error };
  }
}

/**
 * MCP Tool: replay_stage
 * Replays a stage by calling POST /operator/replay/:dossier_id/:stage
 */
async function replay_stage(params = {}) {
  if (!params.dossier_id || !params.stage) {
    return { status: 'error', error: 'dossier_id and stage are required' };
  }
  try {
    const result = await callOperatorAPI('POST', `/replay/${encodeURIComponent(params.dossier_id)}/${encodeURIComponent(params.stage)}`, {
      checkpoint: params.checkpoint,
      remodify_instructions: params.remodify_instructions,
    });
    return {
      status: result.status === 200 ? 'success' : 'failed',
      execution: result.data,
    };
  } catch (err) {
    return { status: 'error', error: err.error };
  }
}

/**
 * MCP Tool: check_alerts
 * Checks alerts by calling GET /operator/alerts
 */
async function check_alerts(params = {}) {
  try {
    const result = await callOperatorAPI('GET', '/alerts');
    return {
      status: result.status === 200 ? 'success' : 'failed',
      alerts: result.data,
    };
  } catch (err) {
    return { status: 'error', error: err.error };
  }
}

/**
 * MCP Tool: health_check
 * Checks health by calling GET /operator/health
 */
async function health_check(params = {}) {
  try {
    const result = await callOperatorAPI('GET', '/health');
    return {
      status: result.status === 200 ? 'healthy' : 'unhealthy',
      health: result.data,
    };
  } catch (err) {
    return { status: 'error', error: err.error };
  }
}

/**
 * Tool dispatcher
 */
const tools = {
  create_content_job,
  inspect_dossier,
  list_outputs,
  approve_output,
  request_changes,
  replay_stage,
  check_alerts,
  health_check,
};

/**
 * MCP Protocol Handlers
 */

/**
 * Handler: initialize
 * Implements MCP initialize method per JSON-RPC spec
 */
function handleInitialize(request, id) {
  const serverInfo = {
    name: 'shadow-operator-mcp',
    version: '1.0.0',
  };
  const protocolVersion = '2024-11-05';
  const capabilities = {
    tools: {},
  };

  return {
    jsonrpc: '2.0',
    id,
    result: {
      protocolVersion,
      capabilities,
      serverInfo,
    },
  };
}

/**
 * Handler: tools/list
 * Implements MCP tools/list method per JSON-RPC spec
 */
function handleToolsList(request, id) {
  const toolDefinitions = [
    {
      name: 'health_check',
      description: 'Check operator API health status',
      inputSchema: {
        type: 'object',
        properties: {},
        required: [],
      },
    },
    {
      name: 'create_content_job',
      description: 'Create a new content job with dossier',
      inputSchema: {
        type: 'object',
        properties: {
          topic: { type: 'string', description: 'Content topic' },
          context: { type: 'string', description: 'Content context (e.g., YouTube)' },
          mode: { type: 'string', description: 'User mode (creator, founder, builder, operator)' },
          route_id: { type: 'string', description: 'Optional route ID' },
        },
        required: ['topic'],
      },
    },
    {
      name: 'inspect_dossier',
      description: 'Inspect a dossier by ID',
      inputSchema: {
        type: 'object',
        properties: {
          dossier_id: { type: 'string', description: 'Dossier ID to inspect' },
        },
        required: ['dossier_id'],
      },
    },
    {
      name: 'list_outputs',
      description: 'List outputs for a dossier',
      inputSchema: {
        type: 'object',
        properties: {
          dossier_id: { type: 'string', description: 'Dossier ID' },
        },
        required: ['dossier_id'],
      },
    },
    {
      name: 'approve_output',
      description: 'Approve an output artifact',
      inputSchema: {
        type: 'object',
        properties: {
          dossier_id: { type: 'string', description: 'Dossier ID' },
          reviewer: { type: 'string', description: 'Reviewer role' },
        },
        required: ['dossier_id'],
      },
    },
    {
      name: 'request_changes',
      description: 'Request changes to a dossier output',
      inputSchema: {
        type: 'object',
        properties: {
          dossier_id: { type: 'string', description: 'Dossier ID' },
          changes: { type: 'string', description: 'Change requests' },
          reviewer: { type: 'string', description: 'Reviewer role' },
        },
        required: ['dossier_id'],
      },
    },
    {
      name: 'replay_stage',
      description: 'Replay a workflow stage',
      inputSchema: {
        type: 'object',
        properties: {
          dossier_id: { type: 'string', description: 'Dossier ID' },
          stage: { type: 'string', description: 'Workflow stage to replay' },
          checkpoint: { type: 'string', description: 'Optional checkpoint' },
          remodify_instructions: { type: 'string', description: 'Instructions for remodify' },
        },
        required: ['dossier_id', 'stage'],
      },
    },
    {
      name: 'check_alerts',
      description: 'Check system alerts',
      inputSchema: {
        type: 'object',
        properties: {},
        required: [],
      },
    },
  ];

  return {
    jsonrpc: '2.0',
    id,
    result: {
      tools: toolDefinitions,
    },
  };
}

/**
 * Handler: tools/call
 * Implements MCP tools/call method per JSON-RPC spec
 */
async function handleToolsCall(request, id) {
  const toolName = request.params?.name;
  const toolArgs = request.params?.arguments || {};

  if (!toolName || !tools[toolName]) {
    return {
      jsonrpc: '2.0',
      id,
      error: {
        code: -32601,
        message: `Tool not found: ${toolName}`,
      },
    };
  }

  try {
    const result = await tools[toolName](toolArgs);
    return {
      jsonrpc: '2.0',
      id,
      result,
    };
  } catch (err) {
    return {
      jsonrpc: '2.0',
      id,
      error: {
        code: -32603,
        message: 'Internal error',
        data: err.message,
      },
    };
  }
}

/**
 * Start MCP stdio server
 */
function startMcpServer() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false,
  });

  let messageId = 0;

  rl.on('line', async (line) => {
    try {
      const request = JSON.parse(line);
      const id = request.id || ++messageId;
      const method = request.method;

      let response;

      // Handle MCP protocol methods
      if (method === 'initialize') {
        response = handleInitialize(request, id);
      } else if (method === 'tools/list') {
        response = handleToolsList(request, id);
      } else if (method === 'tools/call') {
        response = await handleToolsCall(request, id);
      } else {
        // Legacy support: direct tool name invocation
        const params = request.params || {};
        if (tools[method]) {
          const result = await tools[method](params);
          response = {
            jsonrpc: '2.0',
            id,
            result,
          };
        } else {
          response = {
            jsonrpc: '2.0',
            id,
            error: {
              code: -32601,
              message: `Method not found: ${method}`,
            },
          };
        }
      }

      process.stdout.write(JSON.stringify(response) + '\n');
    } catch (err) {
      process.stdout.write(
        JSON.stringify({
          jsonrpc: '2.0',
          error: {
            code: -32700,
            message: 'Parse error',
            data: err.message,
          },
        }) + '\n'
      );
    }
  });

  rl.on('close', () => {
    process.exit(0);
  });
}

// Only start if run directly
if (require.main === module) {
  startMcpServer();
}

module.exports = { startMcpServer, tools };

