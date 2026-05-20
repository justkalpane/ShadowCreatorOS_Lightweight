# Mac Transfer Bundle Plan

## Transfer-safe baseline
Use sanitized assets and governance docs only.

## Methods
- Private GitHub
- External SSD
- ZIP + SHA256 checksum
- rsync/scp equivalent after Mac baseline readiness

## Checksum plan
- Use SHA256SUMS_SANITIZED_REFERENCE.txt from n8n full export.
- Create transfer-time checksum manifest for copied bundle.

## Safety
- Do not auto-transfer raw private forensic exports.
