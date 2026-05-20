# PRODUCTION_PATH_LOCK_POLICY_20260510

## Production Law
- Production repo: `C:\ShadowEmpire-Git_Restore_01`
- Old repo quarantine: `C:\ShadowEmpire-Git`
- Production n8n profile: `C:\ShadowEmpire\n8n_user_restore_01`

## Mandatory Preflight
```powershell
Set-Location C:\ShadowEmpire-Git_Restore_01
.\scripts\windows\assert_restore01_path.ps1
```

If path-lock fails, abort immediately.

## Never-Run Rule
Do not run production startup scripts, patch scripts, or operator tests from `C:\ShadowEmpire-Git`.

## Startup Scripts Covered
- `scripts/windows/start_shadow_operator_api.ps1`
- `scripts/windows/start_n8n_shadow_phase1.ps1`
- `scripts/windows/start_openwebui_local_runtime.ps1`

## Migration Checklist (Future PC)
1. Restore repo to `C:\ShadowEmpire-Git_Restore_01`
2. Restore profile to `C:\ShadowEmpire\n8n_user_restore_01`
3. Run path-lock preflight
4. Start services in canonical order
5. Run health + creative-chain validation
