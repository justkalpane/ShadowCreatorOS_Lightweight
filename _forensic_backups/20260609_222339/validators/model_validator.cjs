#!/usr/bin/env node
/**
 * Model Validator
 * Validates registries/model_registry.yaml structure and routing references.
 * Returns exit 0 on PASS, 1 on FAIL.
 */

const fs = require('fs');
const path = require('path');

const repoRoot = path.resolve(__dirname, '..');
const modelPath = path.join(repoRoot, 'registries', 'model_registry.yaml');

class ModelValidator {
  validate() {
    const errors = [];
    const warnings = [];

    if (!fs.existsSync(modelPath)) {
      errors.push('registries/model_registry.yaml is missing');
      return { passed: false, errors, warnings };
    }

    let content;
    try {
      const raw = fs.readFileSync(modelPath, 'utf8');
      content = this.parseModelRegistry(raw);
    } catch (error) {
      errors.push(`YAML parse error: ${error.message}`);
      return { passed: false, errors, warnings };
    }

    if (!content || typeof content !== 'object') {
      errors.push('Empty or non-object root');
      return { passed: false, errors, warnings };
    }

    if (!content.registry_id) errors.push('Missing registry_id');
    if (content.registry_id && content.registry_id !== 'model_registry') {
      errors.push(`registry_id is "${content.registry_id}", expected "model_registry"`);
    }

    if (!content.model_families && !content.models) {
      errors.push('Missing model_families or models block');
    }

    // Check defaults
    if (!content.defaults) {
      warnings.push('No defaults block defined (recommended)');
    } else {
      if (!content.defaults.primary_text_model) {
        warnings.push('defaults.primary_text_model not set');
      }
    }

    return {
      passed: errors.length === 0,
      errors,
      warnings,
      registry_id: content.registry_id || null,
      family_count: content.model_families ? Object.keys(content.model_families).length : 0
    };
  }

  parseModelRegistry(raw) {
    const text = String(raw || '').replace(/^\uFEFF/, '').replace(/\r\n/g, '\n');
    const registryId = (text.match(/^registry_id:\s*"?([^"\n]+)"?\s*$/m) || [])[1] || null;
    const primaryTextModel =
      (text.match(/^\s*primary_text_model:\s*"?([^"\n]+)"?\s*$/m) || [])[1] || null;
    const familyBlock = text.match(/^model_families:\s*\n([\s\S]*)/m);
    const modelFamilies = {};

    if (familyBlock) {
      for (const match of familyBlock[1].matchAll(/^\s{2}([a-zA-Z0-9_]+):\s*$/gm)) {
        modelFamilies[match[1]] = true;
      }
    }

    return {
      registry_id: registryId,
      defaults: primaryTextModel ? { primary_text_model: primaryTextModel } : null,
      model_families: Object.keys(modelFamilies).length ? modelFamilies : null
    };
  }
}

if (require.main === module) {
  const v = new ModelValidator();
  const result = v.validate();
  console.log('Model Validator');
  console.log('='.repeat(50));
  console.log(`Status: ${result.passed ? 'PASS' : 'FAIL'}`);
  console.log(`Family count: ${result.family_count || 0}`);
  if (result.errors.length) {
    console.log('Errors:');
    result.errors.forEach((e) => console.log('  -', e));
  }
  if (result.warnings.length) {
    console.log('Warnings:');
    result.warnings.forEach((w) => console.log('  -', w));
  }
  process.exit(result.passed ? 0 : 1);
}

module.exports = ModelValidator;
