# MAC-00 Baseline Audit

## Objective
Establish Mac host baseline before any migration runtime steps.

## Prerequisites
- Mac machine access.
- Repository copied but not executed.

## Allowed actions
- System info and tool version checks.

## Forbidden actions
- No runtime start, no workflow execution, no provider calls.

## Commands
- sw_vers
- uname -m
- sysctl hw.memsize
- df -h
- xcode-select -p
- rew --version
- git --version
- gh --version
- 
ode -v
- 
pm -v
- python3 --version
- sqlite3 --version
- jq --version
- yq --version
- codex --version
- claude --version
- kimi --version

## Pass criteria
- Baseline audit report captured with all command outputs and gaps marked.

## Stop condition
- Missing critical install prereqs.

## Next gate
- MAC-01 repo transfer integrity.
