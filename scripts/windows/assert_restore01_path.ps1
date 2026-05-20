$ErrorActionPreference = "Stop"

$expectedGitRoot = "C:/ShadowEmpire-Git_Restore_01"
$expectedFsRoot = "C:\ShadowEmpire-Git_Restore_01"

$cwd = (Get-Location).Path
if (-not $cwd.StartsWith($expectedFsRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
  throw "ABORT: current path is not under $expectedFsRoot. Current: $cwd"
}

$gitCmd = Get-Command git -ErrorAction SilentlyContinue
if (-not $gitCmd) {
  throw "ABORT: git not found on PATH."
}

$gitRoot = (& git rev-parse --show-toplevel 2>$null).Trim()
if (-not $gitRoot) {
  throw "ABORT: unable to detect git root from current path."
}

if ($gitRoot -ne $expectedGitRoot) {
  throw "ABORT: wrong repo root: $gitRoot (expected $expectedGitRoot)"
}

Write-Output "PATH LOCK PASS: $gitRoot"
