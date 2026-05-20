# GIT_STAGING_AUDIT_20260510

## Full Status Classification
| File | Git Status | Classification | Reason | Stage? |
|---|---|---|---|---|
| - | ?? | NEEDS_REVIEW | Manual review required | NO |
| .webui_secret_key | ?? | DO_NOT_STAGE_SECRET | Secret key file | NO |
| all_workflows_temp.json | ?? | NEEDS_REVIEW | Manual review required | NO |
| backups/cutover_20260429_212552/n8n_db/database.sqlite-shm | ?? | DO_NOT_STAGE_DB | Database/WAL/SHM artifact | NO |
| backups/cutover_20260429_212552/n8n_db/database.sqlite-wal | ?? | DO_NOT_STAGE_DB | Database/WAL/SHM artifact | NO |
| config/openwebui_shadow_operator_tools.py | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| config/openwebui_shadow_operator_tools_v2.py | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| config/openwebui_shadow_operator_tools_v3.py | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| data/ollama_direct_runs/ | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| data/se_chat_history.json | M | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| data/se_dossier_index.json | M | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| data/se_error_events.json | M | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| data/se_packet_index.json | M | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| data/se_route_runs.json | M | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| docs/operator/DIRECT_OLLAMA_OPERATOR_METHOD_PRODUCTION_TEST_20260507.md | ?? | SAFE_TO_STAGE_DOCS | Documentation/report content | YES |
| docs/operator/LOCAL_OLLAMA_MODEL_BRAIN_SMOKE_TEST_20260507.md | ?? | SAFE_TO_STAGE_DOCS | Documentation/report content | YES |
| docs/operator/OPEN_WEBUI_INTEGRATION_SETUP.md | M | SAFE_TO_STAGE_DOCS | Documentation/report content | YES |
| docs/operator/OPERATOR_SURFACE_PROOF_STATUS_20260510.md | ?? | SAFE_TO_STAGE_DOCS | Documentation/report content | YES |
| docs/operator/PRODUCTION_OPERATOR_METHODS_SOURCE_OF_TRUTH_20260507.md | ?? | SAFE_TO_STAGE_DOCS | Documentation/report content | YES |
| docs/operator/REALTIME_DEPLOYMENT_OPERATOR_TEST_STATUS_20260507.md | ?? | SAFE_TO_STAGE_DOCS | Documentation/report content | YES |
| docs/recovery/GIT_STAGING_AUDIT_20260510.md | ?? | SAFE_TO_STAGE_DOCS | Documentation/report content | YES |
| docs/recovery/GRAPH_PARITY_AUDIT_20260506_CURRENT/ | ?? | SAFE_TO_STAGE_MIGRATION_REFERENCE | Recovery parity evidence bundle | YES |
| docs/recovery/n8n_webhook_registry.before_r8d_20260504_025213.yaml | ?? | SAFE_TO_STAGE_DOCS | Documentation/report content | YES |
| docs/recovery/OLD_REPO_REQUIREMENT_RECONCILIATION_20260510.md | ?? | SAFE_TO_STAGE_DOCS | Documentation/report content | YES |
| docs/recovery/PHASE_R6B_CANONICAL_IMPORT_FILE_LIST_20260503_235336.txt | ?? | SAFE_TO_STAGE_DOCS | Documentation/report content | YES |
| docs/recovery/PHASE_R6C_EXECUTE_REFERENCE_MAP_20260504_000420.csv | ?? | SAFE_TO_STAGE_DOCS | Documentation/report content | YES |
| docs/recovery/PHASE_R6C_WORKFLOW_ID_MAP_20260504_000420.csv | ?? | SAFE_TO_STAGE_DOCS | Documentation/report content | YES |
| docs/recovery/PHASE_R6C_WORKFLOW_ID_MAP_20260504_000420.json | ?? | SAFE_TO_STAGE_DOCS | Documentation/report content | YES |
| docs/recovery/PHASE_R8_INCIDENT_N8N_FOREGROUND_LOG_20260504_012529.txt | ?? | DO_NOT_STAGE_LOG_TEMP_BACKUP | Backup/log/temp forensic artifact | NO |
| docs/recovery/PHASE_R8_INCIDENT_PRE_FREEZE_GIT_DIFF_20260504_012510.patch | ?? | DO_NOT_STAGE_LOG_TEMP_BACKUP | Backup/log/temp forensic artifact | NO |
| docs/recovery/PHASE_R8B_FIX_PRE_DISCOVERY_GIT_DIFF_20260504_014649.patch | ?? | DO_NOT_STAGE_LOG_TEMP_BACKUP | Backup/log/temp forensic artifact | NO |
| docs/recovery/PHASE_R8D_PRE_REGISTRY_REPAIR_GIT_DIFF_20260504_025207.patch | ?? | DO_NOT_STAGE_LOG_TEMP_BACKUP | Backup/log/temp forensic artifact | NO |
| docs/recovery/PRODUCTION_MIGRATION_MANIFEST_20260510.md | ?? | SAFE_TO_STAGE_DOCS | Documentation/report content | YES |
| docs/recovery/PRODUCTION_PATH_LOCK_POLICY_20260510.md | ?? | SAFE_TO_STAGE_DOCS | Documentation/report content | YES |
| docs/recovery/PRODUCTION_REPO_DRIFT_AUDIT_20260510.md | ?? | SAFE_TO_STAGE_DOCS | Documentation/report content | YES |
| docs/recovery/R6B_FORENSIC_FINDINGS_20260503.txt | ?? | SAFE_TO_STAGE_DOCS | Documentation/report content | YES |
| docs/recovery/R6D_FINAL_REPORT.json | ?? | SAFE_TO_STAGE_DOCS | Documentation/report content | YES |
| docs/recovery/R6D_IMPORT_BATCH_LOG.txt | ?? | SAFE_TO_STAGE_DOCS | Documentation/report content | YES |
| docs/recovery/R6D_IMPORT_BATCH_LOG_20260504_001440.txt | ?? | DO_NOT_STAGE_LOG_TEMP_BACKUP | Backup/log/temp forensic artifact | NO |
| docs/recovery/R6D_IMPORT_RESULTS.json | ?? | SAFE_TO_STAGE_DOCS | Documentation/report content | YES |
| docs/recovery/R6D_STEP5_DATABASE_VERIFICATION.json | ?? | SAFE_TO_STAGE_DOCS | Documentation/report content | YES |
| docs/recovery/R7_FINAL_REPORT.json | ?? | SAFE_TO_STAGE_DOCS | Documentation/report content | YES |
| docs/recovery/R8B_FINAL_REPORT_20260504.txt | ?? | SAFE_TO_STAGE_DOCS | Documentation/report content | YES |
| docs/recovery/R8B_FIX_DISCOVERY_REPORT_20260504.txt | ?? | SAFE_TO_STAGE_DOCS | Documentation/report content | YES |
| docs/recovery/R8E_FIX_N8N_FOREGROUND_LOG_20260504_033137.txt | ?? | DO_NOT_STAGE_LOG_TEMP_BACKUP | Backup/log/temp forensic artifact | NO |
| docs/recovery/R8E_FIX_N8N_STARTUP_1777845818.log | ?? | DO_NOT_STAGE_LOG_TEMP_BACKUP | Backup/log/temp forensic artifact | NO |
| docs/recovery/R9F_BACKUP_20260504_132745/ | ?? | DO_NOT_STAGE_LOG_TEMP_BACKUP | Backup/log/temp forensic artifact | NO |
| docs/recovery/R9F_BACKUP_20260504_143200/ | ?? | DO_NOT_STAGE_LOG_TEMP_BACKUP | Backup/log/temp forensic artifact | NO |
| docs/recovery/R9H_BACKUP_20260504_145100/ | ?? | DO_NOT_STAGE_LOG_TEMP_BACKUP | Backup/log/temp forensic artifact | NO |
| docs/recovery/R9J_D_N8N_START_LOG_20260504_143653.txt | ?? | DO_NOT_STAGE_LOG_TEMP_BACKUP | Backup/log/temp forensic artifact | NO |
| docs/recovery/R9J_N8N_START_LOG_20260504_142313.txt | ?? | DO_NOT_STAGE_LOG_TEMP_BACKUP | Backup/log/temp forensic artifact | NO |
| docs/recovery/R9K_C2_LIVE_DB_EXPORT_20260504/ | ?? | SAFE_TO_STAGE_DOCS | Documentation/report content | YES |
| docs/recovery/R9M_B_POST_REPAIR_LIVE_EXPORT_2026-05-04/ | ?? | SAFE_TO_STAGE_DOCS | Documentation/report content | YES |
| docs/recovery/R9M_D3_SOURCE_VALIDATION_BACKUP_20260504_161237/ | ?? | DO_NOT_STAGE_LOG_TEMP_BACKUP | Backup/log/temp forensic artifact | NO |
| docs/recovery/R9M_LIVE_DB_EXPORT_2026-05-04/ | ?? | SAFE_TO_STAGE_DOCS | Documentation/report content | YES |
| docs/recovery/RUNTIME_PROFILE_CORRECTION_BACKUP_20260506_131135/ | ?? | DO_NOT_STAGE_LOG_TEMP_BACKUP | Backup/log/temp forensic artifact | NO |
| dossiers/DOSSIER-1777885664201-SHI5TFFBQ.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777888167069-EM3AN1LIK.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777888235027-EZ5QL2JNB.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777888253074-0R1JYKJAD.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777888397759-R26NF8QY0.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777888446985-T6FQHE42P.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777888496995-WNNCBN5HT.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777888551134-EIHXBCHAD.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777888560365-SFOPAAOFQ.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777903840634-YBF5WMC55.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777903889647-01BJITOSN.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777904366408-SZKCG9XUN.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777906400329-UIPPWTSVU.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777915049388-5691UYM1A.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777915049913-Y2M8CUBV2.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777918126496-W4AE60QP6.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777919271724-ZCQDT7AO2.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777919729317-VEYNPR0KR.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777931966642-Q7N0H2X2M.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777980298454-HINNBTODN.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777980301671-GI8JKSH82.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777980772703-JVY6XYOIQ.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777981519380-7RKWAIIMU.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777981606350-71XAW4AQ5.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777981799288-B54DCW4YW.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777982430536-1MNDI696G.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777983162669-NZQ7YINWU.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777994083768-O2PYS1PZ2.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777994088570-LBKAA5LX5.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1777999775148-AWM0XS53I.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778058763437-5NP8RLNK8.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778062592871-AUAN261QS.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778062651107-GXJEJG4RX.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778062709391-1QOBJWS9V.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778062736909-D3RN8Q4Q3.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778063202163-HDFBS5S0N.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778063226420-A9W9UTT4X.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778063261257-381NRCTC8.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778063280587-THJ59VCWK.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778064215964-G4SJ9229T.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778064244699-EH8ENMJE8.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778064262103-J2Q6VVI2Z.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778064321906-RP3F2WKYE.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778070197685-78TTI24GW.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778070615264-YE43EVN7J.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/dossier-1778070623418-ofljux1y2.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778070639409-KIUQIX5VO.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/dossier-1778070647577-uab9z7zdz.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778070668277-0LF7J0Q7H.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778070936689-XB57CDIF5.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778072423158-EE2YKVHTO.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778072423758-K3LCLIZZK.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778072624858-P7XCZML9Z.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778072669188-6T359MBUO.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778072686707-VGRT7LBDQ.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778072851330-CQ2EW96BG.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/dossier-1778072859474-mzot5e95w.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778072876800-3GTTDYLQS.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/dossier-1778072884943-1llydzhzm.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778075176436-L6YX7DRPE.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778075275860-Q7EUX78H8.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778075637115-0P8B2T4KN.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/dossier-1778075645236-b5n5cnhjg.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778075659691-VQM6TPMK0.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/dossier-1778075667831-o3r7nzbne.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778075681023-FBREUPSNY.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778075878622-TNIFQBKB5.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/dossier-1778075886760-4hnvypph4.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778076379483-KOJFYIB4Z.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778076380895-7FGV79H2K.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/dossier-1778076387600-18ew049v0.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778076402688-MYJGADZJ3.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/dossier-1778076410809-5ofw7to4t.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778076423334-4MOH61F2H.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/dossier-1778076431479-r6q074266.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778076537427-VQ7NK9PS4.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/dossier-1778076545572-arkj5r89u.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778077477468-YVNZTJ8ZZ.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/dossier-1778077485572-qgbf5wyd5.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778085827118-FPX1OZQPF.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778085830384-65R90A6Z5.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/dossier-1778085835175-602zwqcyn.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778087677309-6YJ61XY0W.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/dossier-1778087685481-7xavom33r.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778087693713-762882HDO.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/dossier-1778087701865-yaagxuxpc.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778087709980-WOX62V0J1.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/dossier-1778087718105-bdfcr3u93.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778087830553-8NB76TFTA.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/dossier-1778087838687-34z5qngc1.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778088758285-OGWMGCLVC.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/dossier-1778088766428-89vvvuwu9.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778131069833-ORCBUNLRR.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778338210762-POK4YT1R0.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778339037237-2T49HGK88.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778339158963-ZSLONPP79.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778346329330-5B9Z7C90C.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778348153821-YRJ2PCLWB.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778361145728-VT77A7GYK.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778361826106-SG5W84828.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778363732663-1F5IDC9LC.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778365771835-HPE3G0MK3.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778408782159-RGM68OA2W.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778409420646-DHRWLHNA8.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778409695497-HSA9L9GDY.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778412313758-2GPA0PMEQ.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778413615265-NQ6GTQ5WQ.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778414777728-5CU9WGJWZ.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778414996783-0NSODRPXU.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-1778415612095-A1DPBL0YY.json | ?? | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| dossiers/DOSSIER-UNSPECIFIED.json | M | DO_NOT_STAGE_RUNTIME_DATA | Runtime-generated dossier/index/output data | NO |
| engine/api/chat.js | M | DO_NOT_STAGE_COMMAND_CENTER | Command Center/chat-layer quarantined | NO |
| engine/api/operator.js | M | SAFE_TO_STAGE_RUNTIME_FIX | Operator runtime/reconciliation boundary | YES |
| engine/chat/chat_orchestration_service.js | M | DO_NOT_STAGE_COMMAND_CENTER | Command Center/chat-layer quarantined | NO |
| engine/chat/n8n_workflow_client.js | M | DO_NOT_STAGE_COMMAND_CENTER | Command Center/chat-layer quarantined | NO |
| n8n/workflows/CWF-110.json | M | SAFE_TO_STAGE_WORKFLOW_FIX | Workflow runtime-boundary fixes | YES |
| n8n/workflows/CWF-120.json | M | SAFE_TO_STAGE_WORKFLOW_FIX | Workflow runtime-boundary fixes | YES |
| n8n/workflows/CWF-130.json | M | SAFE_TO_STAGE_WORKFLOW_FIX | Workflow runtime-boundary fixes | YES |
| n8n/workflows/CWF-140.json | M | SAFE_TO_STAGE_WORKFLOW_FIX | Workflow runtime-boundary fixes | YES |
| n8n/workflows/CWF-210.json | M | SAFE_TO_STAGE_WORKFLOW_FIX | Workflow runtime-boundary fixes | YES |
| n8n/workflows/CWF-220.json | M | SAFE_TO_STAGE_WORKFLOW_FIX | Workflow runtime-boundary fixes | YES |
| n8n/workflows/CWF-230.json | M | SAFE_TO_STAGE_WORKFLOW_FIX | Workflow runtime-boundary fixes | YES |
| n8n/workflows/CWF-240.json | M | SAFE_TO_STAGE_WORKFLOW_FIX | Workflow runtime-boundary fixes | YES |
| n8n/workflows/CWF-310.json | M | SAFE_TO_STAGE_WORKFLOW_FIX | Workflow runtime-boundary fixes | YES |
| n8n/workflows/CWF-320.json | M | SAFE_TO_STAGE_WORKFLOW_FIX | Workflow runtime-boundary fixes | YES |
| n8n/workflows/CWF-330.json | M | SAFE_TO_STAGE_WORKFLOW_FIX | Workflow runtime-boundary fixes | YES |
| n8n/workflows/CWF-340.json | M | SAFE_TO_STAGE_WORKFLOW_FIX | Workflow runtime-boundary fixes | YES |
| n8n/workflows/CWF-410.json | M | SAFE_TO_STAGE_WORKFLOW_FIX | Workflow runtime-boundary fixes | YES |
| n8n/workflows/CWF-420.json | M | SAFE_TO_STAGE_WORKFLOW_FIX | Workflow runtime-boundary fixes | YES |
| n8n/workflows/CWF-430.json | M | SAFE_TO_STAGE_WORKFLOW_FIX | Workflow runtime-boundary fixes | YES |
| n8n/workflows/CWF-440.json | M | SAFE_TO_STAGE_WORKFLOW_FIX | Workflow runtime-boundary fixes | YES |
| n8n/workflows/CWF-510.json | M | SAFE_TO_STAGE_WORKFLOW_FIX | Workflow runtime-boundary fixes | YES |
| n8n/workflows/CWF-520.json | M | SAFE_TO_STAGE_WORKFLOW_FIX | Workflow runtime-boundary fixes | YES |
| n8n/workflows/CWF-530.json | M | SAFE_TO_STAGE_WORKFLOW_FIX | Workflow runtime-boundary fixes | YES |
| n8n/workflows/CWF-610.json | M | SAFE_TO_STAGE_WORKFLOW_FIX | Workflow runtime-boundary fixes | YES |
| n8n/workflows/CWF-620.json | M | SAFE_TO_STAGE_WORKFLOW_FIX | Workflow runtime-boundary fixes | YES |
| n8n/workflows/CWF-630.json | M | SAFE_TO_STAGE_WORKFLOW_FIX | Workflow runtime-boundary fixes | YES |
| operator/config.js | M | SAFE_TO_STAGE_RUNTIME_FIX | Operator runtime/reconciliation boundary | YES |
| operator/mcp/shadow_operator_mcp_server.js | M | SAFE_TO_STAGE_OPERATOR_SURFACE_FIX | Operator surface bridge endpoint/wiring | YES |
| operator/n8n_execution_reconciler.js | ?? | SAFE_TO_STAGE_RUNTIME_FIX | Operator runtime/reconciliation boundary | YES |
| operator/ollama_test_runner.js | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| operator/output_reader.js | M | SAFE_TO_STAGE_RUNTIME_FIX | Operator runtime/reconciliation boundary | YES |
| operator/r9pb2_test.js | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| operator/skill_runtime.js | ?? | SAFE_TO_STAGE_RUNTIME_FIX | Operator runtime/reconciliation boundary | YES |
| r9l_b2_hard_restart.ps1 | ?? | NEEDS_REVIEW | Manual review required | NO |
| r9l_b2_simple_restart.ps1 | ?? | NEEDS_REVIEW | Manual review required | NO |
| restart_n8n.ps1 | ?? | NEEDS_REVIEW | Manual review required | NO |
| scripts/cli/activate_workflows.cjs | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| scripts/cli/query_db_incident.cjs | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| scripts/cli/query_db_webhooks.cjs | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| scripts/cli/query_publish_state.cjs | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| scripts/cli/r8b_check_wf000_definition.cjs | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| scripts/cli/r8b_confirm_wf000.cjs | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| scripts/cli/r8b_fix_analyze_publish.cjs | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| scripts/cli/r8b_fix_webhook_entity_detail.cjs | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| scripts/cli/r8b_post_restart_check.cjs | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| scripts/cli/r8b_save_pre_counts.cjs | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| scripts/cli/r8b_verify_publish.cjs | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| scripts/cli/r8b_webhook_detail.cjs | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| scripts/diagnose_n8n_crash.ps1 | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| scripts/extract_webhook_nodes.js | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| scripts/operator/inspect-output.ps1 | M | SAFE_TO_STAGE_RUNTIME_FIX | Operator runtime/reconciliation boundary | YES |
| scripts/operator/list-outputs.ps1 | M | SAFE_TO_STAGE_RUNTIME_FIX | Operator runtime/reconciliation boundary | YES |
| scripts/r6d_import_batch.ps1 | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| scripts/r6d_restart_n8n.ps1 | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| scripts/r8_start_n8n.ps1 | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| scripts/r8_start_n8n_simple.ps1 | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| scripts/r8b_fix_execute.bat | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| scripts/r8b_fix_execute.ps1 | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| scripts/r8b_fix_execute_v2.bat | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| scripts/restart_n8n_after_ui_publish.ps1 | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| scripts/start_n8n_clean_restart.bat | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| scripts/start_n8n_test.bat | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| scripts/validate_webhook_resolution.js | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| scripts/windows/assert_restore01_path.ps1 | ?? | SAFE_TO_STAGE_STARTUP_GUARD | Path-lock and canonical startup hardening | YES |
| scripts/windows/start_n8n_shadow_phase1.ps1 | M | SAFE_TO_STAGE_STARTUP_GUARD | Path-lock and canonical startup hardening | YES |
| scripts/windows/start_n8n_shadow_phase1.ps1.backup_corrected_20260504_112038 | ?? | NEEDS_REVIEW | Code/config changed outside approved core list | NO |
| scripts/windows/start_openwebui_local_runtime.ps1 | M | SAFE_TO_STAGE_STARTUP_GUARD | Path-lock and canonical startup hardening | YES |
| scripts/windows/start_shadow_operator_api.ps1 | M | SAFE_TO_STAGE_STARTUP_GUARD | Path-lock and canonical startup hardening | YES |
| server.js | M | DO_NOT_STAGE_COMMAND_CENTER | Mixed server/chat-layer risk; quarantined for this staging cycle | NO |
| start_operator.ps1 | ?? | NEEDS_REVIEW | Manual review required | NO |
| temp/ | ?? | DO_NOT_STAGE_LOG_TEMP_BACKUP | Backup/log/temp forensic artifact | NO |
| temp_audit/ | ?? | DO_NOT_STAGE_LOG_TEMP_BACKUP | Backup/log/temp forensic artifact | NO |
| temp_cmd_test.txt | ?? | DO_NOT_STAGE_LOG_TEMP_BACKUP | Backup/log/temp forensic artifact | NO |
| ui/src/screens/Chat.jsx | M | DO_NOT_STAGE_COMMAND_CENTER | Command Center/chat-layer quarantined | NO |
| webhook_nodes_extracted.json | ?? | NEEDS_REVIEW | Manual review required | NO |

## SAFE Candidate Legacy Pattern Scan
| File | Old Path Ref | Old Profile Ref | 5050 Ref | fetch Ref | skill_loader Import | Safe? |
|---|---|---|---|---|---|---|
| docs/operator/DIRECT_OLLAMA_OPERATOR_METHOD_PRODUCTION_TEST_20260507.md | False | False | False | False | False | True |
| docs/operator/LOCAL_OLLAMA_MODEL_BRAIN_SMOKE_TEST_20260507.md | False | False | False | False | False | True |
| docs/operator/OPEN_WEBUI_INTEGRATION_SETUP.md | False | True | False | False | False | False |
| docs/operator/OPERATOR_SURFACE_PROOF_STATUS_20260510.md | False | False | False | False | False | True |
| docs/operator/PRODUCTION_OPERATOR_METHODS_SOURCE_OF_TRUTH_20260507.md | False | False | True | False | False | False |
| docs/operator/REALTIME_DEPLOYMENT_OPERATOR_TEST_STATUS_20260507.md | True | False | False | False | True | False |
| docs/recovery/GIT_STAGING_AUDIT_20260510.md | False | False | False | False | False | True |
| docs/recovery/n8n_webhook_registry.before_r8d_20260504_025213.yaml | False | False | False | False | False | True |
| docs/recovery/OLD_REPO_REQUIREMENT_RECONCILIATION_20260510.md | True | False | False | False | False | False |
| docs/recovery/PHASE_R6B_CANONICAL_IMPORT_FILE_LIST_20260503_235336.txt | False | False | False | False | False | True |
| docs/recovery/PHASE_R6C_EXECUTE_REFERENCE_MAP_20260504_000420.csv | False | False | False | False | False | True |
| docs/recovery/PHASE_R6C_WORKFLOW_ID_MAP_20260504_000420.csv | False | False | False | False | False | True |
| docs/recovery/PHASE_R6C_WORKFLOW_ID_MAP_20260504_000420.json | False | False | False | False | False | True |
| docs/recovery/PRODUCTION_MIGRATION_MANIFEST_20260510.md | True | False | False | True | False | False |
| docs/recovery/PRODUCTION_PATH_LOCK_POLICY_20260510.md | True | False | False | False | False | False |
| docs/recovery/PRODUCTION_REPO_DRIFT_AUDIT_20260510.md | True | True | False | True | False | False |
| docs/recovery/R6B_FORENSIC_FINDINGS_20260503.txt | False | False | False | False | False | True |
| docs/recovery/R6D_FINAL_REPORT.json | False | False | False | False | False | True |
| docs/recovery/R6D_IMPORT_BATCH_LOG.txt | False | False | False | False | False | True |
| docs/recovery/R6D_IMPORT_RESULTS.json | False | False | False | False | False | True |
| docs/recovery/R6D_STEP5_DATABASE_VERIFICATION.json | False | False | False | False | False | True |
| docs/recovery/R7_FINAL_REPORT.json | False | False | False | False | False | True |
| docs/recovery/R8B_FINAL_REPORT_20260504.txt | False | False | False | False | False | True |
| docs/recovery/R8B_FIX_DISCOVERY_REPORT_20260504.txt | False | False | False | False | False | True |
| engine/api/operator.js | False | False | False | False | False | True |
| n8n/workflows/CWF-110.json | False | False | False | False | False | True |
| n8n/workflows/CWF-120.json | False | False | False | False | False | True |
| n8n/workflows/CWF-130.json | False | False | False | False | False | True |
| n8n/workflows/CWF-140.json | False | False | False | False | False | True |
| n8n/workflows/CWF-210.json | False | False | False | False | False | True |
| n8n/workflows/CWF-220.json | False | False | False | False | False | True |
| n8n/workflows/CWF-230.json | False | False | False | False | False | True |
| n8n/workflows/CWF-240.json | False | False | False | False | False | True |
| n8n/workflows/CWF-310.json | False | False | False | False | False | True |
| n8n/workflows/CWF-320.json | False | False | False | False | False | True |
| n8n/workflows/CWF-330.json | False | False | False | False | False | True |
| n8n/workflows/CWF-340.json | False | False | False | False | False | True |
| n8n/workflows/CWF-410.json | False | False | False | False | False | True |
| n8n/workflows/CWF-420.json | False | False | False | False | False | True |
| n8n/workflows/CWF-430.json | False | False | False | False | False | True |
| n8n/workflows/CWF-440.json | False | False | False | False | False | True |
| n8n/workflows/CWF-510.json | False | False | False | False | False | True |
| n8n/workflows/CWF-520.json | False | False | False | False | False | True |
| n8n/workflows/CWF-530.json | False | False | False | False | False | True |
| n8n/workflows/CWF-610.json | False | False | False | False | False | True |
| n8n/workflows/CWF-620.json | False | False | False | False | False | True |
| n8n/workflows/CWF-630.json | False | False | False | False | False | True |
| operator/config.js | False | False | False | False | False | True |
| operator/mcp/shadow_operator_mcp_server.js | False | False | True | False | False | False |
| operator/n8n_execution_reconciler.js | False | False | False | False | False | True |
| operator/output_reader.js | False | False | False | False | False | True |
| operator/skill_runtime.js | False | False | False | False | False | True |
| scripts/operator/inspect-output.ps1 | False | False | False | False | False | True |
| scripts/operator/list-outputs.ps1 | False | False | False | False | False | True |
| scripts/windows/assert_restore01_path.ps1 | False | False | False | False | False | True |
| scripts/windows/start_n8n_shadow_phase1.ps1 | False | False | False | False | False | True |
| scripts/windows/start_openwebui_local_runtime.ps1 | False | False | False | False | False | True |
| scripts/windows/start_shadow_operator_api.ps1 | False | False | False | False | False | True |


## Open WebUI Doc Drift Patch Result
- File: docs/operator/OPEN_WEBUI_INTEGRATION_SETUP.md
- Change: replaced legacy runtime references from localhost:5050 to localhost:5002
- Replacement count: 12

## Proposed Commit Groups (No Staging Yet)
### Commit 9A - Runtime boundary + packet materialization + skill-runtime fixes
- engine/api/operator.js
- operator/skill_runtime.js
- operator/n8n_execution_reconciler.js
- operator/output_reader.js
- operator/config.js
- scripts/operator/inspect-output.ps1
- scripts/operator/list-outputs.ps1

### Commit 9B - n8n workflow/CWF axios + skill-runtime bridge fixes
- n8n/workflows/CWF-110.json
- n8n/workflows/CWF-120.json
- n8n/workflows/CWF-130.json
- n8n/workflows/CWF-140.json
- n8n/workflows/CWF-210.json
- n8n/workflows/CWF-220.json
- n8n/workflows/CWF-230.json
- n8n/workflows/CWF-240.json
- n8n/workflows/CWF-310.json
- n8n/workflows/CWF-320.json
- n8n/workflows/CWF-330.json
- n8n/workflows/CWF-340.json
- n8n/workflows/CWF-410.json
- n8n/workflows/CWF-420.json
- n8n/workflows/CWF-430.json
- n8n/workflows/CWF-440.json
- n8n/workflows/CWF-510.json
- n8n/workflows/CWF-520.json
- n8n/workflows/CWF-530.json
- n8n/workflows/CWF-610.json
- n8n/workflows/CWF-620.json
- n8n/workflows/CWF-630.json

### Commit 9C - Path-lock + startup guard + migration/recovery docs
- scripts/windows/assert_restore01_path.ps1
- scripts/windows/start_shadow_operator_api.ps1
- scripts/windows/start_n8n_shadow_phase1.ps1
- scripts/windows/start_openwebui_local_runtime.ps1
- docs/recovery/OLD_REPO_REQUIREMENT_RECONCILIATION_20260510.md
- docs/recovery/PRODUCTION_MIGRATION_MANIFEST_20260510.md
- docs/recovery/PRODUCTION_PATH_LOCK_POLICY_20260510.md
- docs/recovery/PRODUCTION_REPO_DRIFT_AUDIT_20260510.md
- docs/recovery/GRAPH_PARITY_AUDIT_20260506_CURRENT

### Commit 9D - Operator surface proof docs + Open WebUI doc correction
- docs/operator/OPERATOR_SURFACE_PROOF_STATUS_20260510.md
- docs/operator/REALTIME_DEPLOYMENT_OPERATOR_TEST_STATUS_20260507.md
- docs/operator/OPEN_WEBUI_INTEGRATION_SETUP.md

## Do-Not-Stage List
- data/*
- dossiers/*
- .webui_secret_key
- backups/*
- temp/*
- temp_audit/*
- *.sqlite*
- *.log
- docs/recovery/*BACKUP*
- docs/recovery/*_LOG_*
- docs/recovery/*.patch
- scripts/windows/start_n8n_shadow_phase1.ps1.backup_corrected_20260504_112038

## Needs-Review Files
- operator/mcp/shadow_operator_mcp_server.js
- docs/operator/PRODUCTION_OPERATOR_METHODS_SOURCE_OF_TRUTH_20260507.md
- docs/operator/LOCAL_OLLAMA_MODEL_BRAIN_SMOKE_TEST_20260507.md
- docs/operator/DIRECT_OLLAMA_OPERATOR_METHOD_PRODUCTION_TEST_20260507.md
- engine/api/chat.js
- engine/chat/chat_orchestration_service.js
- engine/chat/n8n_workflow_client.js
- ui/src/screens/Chat.jsx
- server.js
- all_workflows_temp.json
- -

## Proposed git add Commands (Do Not Run Yet)
```powershell
Set-Location C:\ShadowEmpire-Git_Restore_01
git add engine/api/operator.js operator/skill_runtime.js operator/n8n_execution_reconciler.js operator/output_reader.js operator/config.js scripts/operator/inspect-output.ps1 scripts/operator/list-outputs.ps1
git add n8n/workflows/CWF-110.json n8n/workflows/CWF-120.json n8n/workflows/CWF-130.json n8n/workflows/CWF-140.json n8n/workflows/CWF-210.json n8n/workflows/CWF-220.json n8n/workflows/CWF-230.json n8n/workflows/CWF-240.json n8n/workflows/CWF-310.json n8n/workflows/CWF-320.json n8n/workflows/CWF-330.json n8n/workflows/CWF-340.json n8n/workflows/CWF-410.json n8n/workflows/CWF-420.json n8n/workflows/CWF-430.json n8n/workflows/CWF-440.json n8n/workflows/CWF-510.json n8n/workflows/CWF-520.json n8n/workflows/CWF-530.json n8n/workflows/CWF-610.json n8n/workflows/CWF-620.json n8n/workflows/CWF-630.json
git add scripts/windows/assert_restore01_path.ps1 scripts/windows/start_shadow_operator_api.ps1 scripts/windows/start_n8n_shadow_phase1.ps1 scripts/windows/start_openwebui_local_runtime.ps1 docs/recovery/OLD_REPO_REQUIREMENT_RECONCILIATION_20260510.md docs/recovery/PRODUCTION_MIGRATION_MANIFEST_20260510.md docs/recovery/PRODUCTION_PATH_LOCK_POLICY_20260510.md docs/recovery/PRODUCTION_REPO_DRIFT_AUDIT_20260510.md docs/recovery/GRAPH_PARITY_AUDIT_20260506_CURRENT
git add docs/operator/OPERATOR_SURFACE_PROOF_STATUS_20260510.md docs/operator/REALTIME_DEPLOYMENT_OPERATOR_TEST_STATUS_20260507.md docs/operator/OPEN_WEBUI_INTEGRATION_SETUP.md
```

