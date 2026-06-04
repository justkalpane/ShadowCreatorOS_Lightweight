const fs = require('fs');
const path = require('path');

class PacketValidator {
  constructor(config = {}) {
    this.schemaRegistryPath = config.schema_registry_path || './registries/schema_registry.yaml';
  }

  validatePacket(packet) {
    const errors = [];
    if (!packet || typeof packet !== 'object' || Array.isArray(packet)) {
      return { valid: false, artifact_family: null, errors: ['Packet is not an object'] };
    }

    const artifactFamily = packet.packet_id || packet.packet_type || packet.artifact_family || null;
    if (!artifactFamily) {
      errors.push('Missing packet_id, packet_type, or artifact_family');
    }

    const schemaPath = artifactFamily ? this.resolveSchemaPath(artifactFamily) : null;
    if (!schemaPath) {
      return {
        valid: errors.length === 0,
        artifact_family: artifactFamily,
        schema_path: null,
        errors,
        warnings: ['No schema registered for packet family; base validation only']
      };
    }

    let schema;
    try {
      schema = JSON.parse(this.stripBom(fs.readFileSync(schemaPath, 'utf8')));
    } catch (error) {
      errors.push(`Cannot read schema ${schemaPath}: ${error.message}`);
      return { valid: false, artifact_family: artifactFamily, schema_path: schemaPath, errors };
    }

    const required = Array.isArray(schema.required) ? schema.required : [];
    for (const field of required) {
      if (!(field in packet)) {
        errors.push(`Missing required field: ${field}`);
      }
    }

    return {
      valid: errors.length === 0,
      artifact_family: artifactFamily,
      schema_path: schemaPath,
      errors,
      warnings: []
    };
  }

  resolveSchemaPath(artifactFamily) {
    const registryPath = path.resolve(this.schemaRegistryPath);
    if (fs.existsSync(registryPath)) {
      const text = fs.readFileSync(registryPath, 'utf8');
      const lines = text.replace(/\r\n/g, '\n').split('\n');
      let current = null;
      for (const line of lines) {
        const start = line.match(/^\s*-\s*artifact_family:\s*([a-zA-Z0-9_-]+)\s*$/);
        if (start) {
          current = start[1];
          continue;
        }
        if (current === artifactFamily) {
          const schemaPath = line.match(/^\s*schema_path:\s*(.+?)\s*$/);
          if (schemaPath) {
            return path.resolve(schemaPath[1].trim());
          }
        }
      }
    }

    const fallback = path.resolve('schemas', 'packets', `${artifactFamily}.schema.json`);
    return fs.existsSync(fallback) ? fallback : null;
  }

  stripBom(text) {
    return String(text || '').replace(/^\uFEFF/, '');
  }
}

module.exports = PacketValidator;
