#!/usr/bin/env node
/**
 * R9P-A Test Runner for Ollama Tool Runner
 * Tests the patched OllamaToolRunner with dossier creation
 */

const OllamaToolRunner = require('./ollama_tool_runner');
const ModeManager = require('./mode_manager');
const OperatorN8nClient = require('./n8n_client');

async function runTest() {
  const testMessage = 'Create a YouTube script outline about AI tools for creators using the Shadow Creator OS local operator';
  
  console.log('='.repeat(70));
  console.log('R9P-A: Ollama Tool Runner Test');
  console.log('='.repeat(70));
  console.log('');
  console.log('Test Message:', testMessage);
  console.log('');
  console.log('Initializing components...');

  const modes = new ModeManager();
  const n8n = new OperatorN8nClient();
  const ollama = new OllamaToolRunner(modes, n8n);

  console.log('Running OllamaToolRunner.run()...');
  console.log('');

  const result = await ollama.run(testMessage, {
    mode: 'creator',
    topic_context: 'YouTube video creation',
  });

  console.log('Result:');
  console.log(JSON.stringify(result, null, 2));
  console.log('');
  console.log('='.repeat(70));
  
  if (result.status === 'accepted' && result.dossier_id) {
    console.log('✓ TEST PASSED - Dossier created: ' + result.dossier_id);
    console.log('  WF-001 status:', result.wf001?.status);
    console.log('  WF-010 status:', result.wf010?.status);
  } else if (result.status === 'failed') {
    console.log('✗ TEST FAILED - ' + (result.error || 'Unknown error'));
  } else if (result.status === 'blocked') {
    console.log('✗ TEST BLOCKED - ' + result.reason);
  } else {
    console.log('? TEST INCOMPLETE - Unexpected status: ' + result.status);
  }
  console.log('='.repeat(70));
}

runTest().catch(err => {
  console.error('Test runner error:', err);
  process.exit(1);
});
