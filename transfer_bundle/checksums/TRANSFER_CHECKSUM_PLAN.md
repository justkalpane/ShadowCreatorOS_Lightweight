# Transfer Checksum Plan

Do not zip yet. Use this plan when packaging is explicitly approved.

## Windows checksum command
certutil -hashfile <zip_or_tar_file> SHA256

## Mac checksum command
shasum -a 256 <zip_or_tar_file>

## File-count verification strategy
1. Capture file and directory counts on Windows before transfer.
2. Capture file and directory counts on Mac after transfer.
3. Compare counts and investigate any mismatch.
4. Verify n8n sanitized export count equals 71.
5. Verify checksum manifest file is present and unchanged.
