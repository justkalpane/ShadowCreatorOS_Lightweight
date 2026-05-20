# MAC-01 Repo Transfer And Integrity

## Objective
Transfer lightweight package to Mac and verify integrity.

## Prerequisites
- MAC-00 complete.
- Transfer method selected.

## Allowed actions
- Copy repo, compute and compare checksums.

## Forbidden actions
- No runtime start, no n8n import.

## Checks
- File count parity
- SHA256 manifest verification
- Transfer include/exclude policy compliance

## Pass criteria
- Integrity checks pass and excluded artifacts remain excluded.

## Stop condition
- Checksum mismatch or forbidden artifacts found.

## Next gate
- MAC-02 dependency install.
