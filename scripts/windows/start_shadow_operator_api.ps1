$ErrorActionPreference = "Stop"

Set-Location "C:\ShadowEmpire-Git_Restore_01"
& ".\scripts\windows\assert_restore01_path.ps1"

Write-Host "Starting Shadow Operator API (canonical) on localhost:5002..."
Write-Host "n8n expected at localhost:5678"

node server.js
