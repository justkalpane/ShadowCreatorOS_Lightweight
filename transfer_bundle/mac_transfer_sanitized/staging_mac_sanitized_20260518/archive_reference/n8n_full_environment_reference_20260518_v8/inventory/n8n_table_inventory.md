# n8n Table Inventory

| table_name | row_count | purpose_guess | safe_to_export | credential_sensitive | execution_sensitive | needed_for_workflow_diff |
|---|---:|---|---|---|---|---|
| ai_builder_temporary_workflow | 0 | workflow metadata/versioning | true | false | false | true |
| annotation_tag_entity | 0 | general | true | false | false | false |
| auth_identity | 0 | general | true | false | false | false |
| auth_provider_sync_history | 0 | general | true | false | false | false |
| binary_data | 0 | binary payload pointers | no | false | true | false |
| chat_hub_agent_tools | 0 | general | true | false | false | false |
| chat_hub_agents | 0 | general | true | false | false | false |
| chat_hub_messages | 0 | general | true | false | false | false |
| chat_hub_session_tools | 0 | general | true | false | false | false |
| chat_hub_sessions | 0 | general | true | false | false | false |
| chat_hub_tools | 0 | general | true | false | false | false |
| credential_dependency | 0 | credential references and encrypted blobs | redacted_only | true | false | false |
| credentials_entity | 1 | credential references and encrypted blobs | redacted_only | true | false | false |
| data_table | 0 | general | true | false | false | false |
| data_table_column | 0 | general | true | false | false | false |
| deployment_key | 4 | general | true | false | false | false |
| dynamic_credential_entry | 0 | credential references and encrypted blobs | redacted_only | true | false | false |
| dynamic_credential_resolver | 0 | credential references and encrypted blobs | redacted_only | true | false | false |
| dynamic_credential_user_entry | 0 | credential references and encrypted blobs | redacted_only | true | false | false |
| event_destinations | 0 | general | true | false | false | false |
| execution_annotation_tags | 0 | execution history | counts_only | false | true | false |
| execution_annotations | 0 | execution history | counts_only | false | true | false |
| execution_data | 2503 | execution history | counts_only | false | true | false |
| execution_entity | 2503 | execution history | counts_only | false | true | false |
| execution_metadata | 0 | execution history | counts_only | false | true | false |
| folder | 1 | general | true | false | false | false |
| folder_tag | 0 | general | true | false | false | false |
| insights_by_period | 300 | general | true | false | false | false |
| insights_metadata | 5 | general | true | false | false | false |
| insights_raw | 9 | general | true | false | false | false |
| installed_nodes | 0 | general | true | false | false | false |
| installed_packages | 0 | general | true | false | false | false |
| instance_ai_iteration_logs | 0 | general | true | false | false | false |
| instance_ai_messages | 0 | general | true | false | false | false |
| instance_ai_observational_memory | 0 | general | true | false | false | false |
| instance_ai_resources | 0 | general | true | false | false | false |
| instance_ai_run_snapshots | 0 | general | true | false | false | false |
| instance_ai_threads | 0 | general | true | false | false | false |
| instance_ai_workflow_snapshots | 0 | workflow metadata/versioning | true | false | false | true |
| instance_version_history | 1 | general | true | false | false | false |
| invalid_auth_token | 0 | general | true | false | false | false |
| migrations | 159 | general | true | false | false | false |
| oauth_access_tokens | 0 | general | true | false | false | false |
| oauth_authorization_codes | 0 | general | true | false | false | false |
| oauth_clients | 0 | general | true | false | false | false |
| oauth_refresh_tokens | 0 | general | true | false | false | false |
| oauth_user_consents | 0 | general | true | false | false | false |
| processed_data | 0 | general | true | false | false | false |
| project | 1 | general | true | false | false | false |
| project_relation | 1 | general | true | false | false | false |
| project_secrets_provider_access | 0 | general | true | false | false | false |
| role | 15 | general | true | false | false | false |
| role_mapping_rule | 0 | general | true | false | false | false |
| role_mapping_rule_project | 0 | general | true | false | false | false |
| role_scope | 465 | general | true | false | false | false |
| scope | 189 | general | true | false | false | false |
| secrets_provider_connection | 0 | general | true | false | false | false |
| settings | 5 | general | true | false | false | false |
| shared_credentials | 1 | credential references and encrypted blobs | redacted_only | true | false | false |
| shared_workflow | 71 | workflow metadata/versioning | true | false | false | true |
| sqlite_sequence | 5 | general | true | false | false | false |
| tag_entity | 0 | general | true | false | false | false |
| test_case_execution | 0 | execution history | counts_only | false | true | false |
| test_run | 0 | general | true | false | false | false |
| token_exchange_jti | 0 | general | true | false | false | false |
| trusted_key | 0 | general | true | false | false | false |
| trusted_key_source | 0 | general | true | false | false | false |
| user | 1 | general | true | false | false | false |
| user_api_keys | 1 | general | true | false | false | false |
| user_favorites | 1 | general | true | false | false | false |
| variables | 0 | general | true | false | false | false |
| webhook_entity | 6 | general | true | false | false | false |
| workflow_builder_session | 0 | workflow metadata/versioning | true | false | false | true |
| workflow_dependency | 1672 | workflow metadata/versioning | true | false | false | true |
| workflow_entity | 71 | workflow metadata/versioning | true | false | false | true |
| workflow_history | 71 | workflow metadata/versioning | true | false | false | true |
| workflow_publish_history | 495 | workflow metadata/versioning | true | false | false | true |
| workflow_published_version | 0 | workflow metadata/versioning | true | false | false | true |
| workflow_statistics | 53 | workflow metadata/versioning | true | false | false | true |
| workflows_tags | 0 | workflow metadata/versioning | true | false | false | true |