# n8n Database Schema Snapshot

- source_db: `C:\ShadowEmpire\n8n_user_restore_01\.n8n\database.sqlite`
- snapshot_db: `C:\ShadowCreatorOS_Lightweight\archive_reference\n8n_full_environment_reference_20260518_v8\PRIVATE_DB_SNAPSHOT_DO_NOT_USE_AS_RUNTIME\database.sqlite.copy`

## ai_builder_temporary_workflow
- row_count: 0
- workflowId | varchar(36) | notnull=1 | pk=1
- threadId | varchar | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## annotation_tag_entity
- row_count: 0
- id | varchar(16) | notnull=1 | pk=1
- name | varchar(24) | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## auth_identity
- row_count: 0
- userId | VARCHAR(36) | notnull=0 | pk=0
- providerId | VARCHAR(64) | notnull=1 | pk=1
- providerType | VARCHAR(32) | notnull=1 | pk=2
- createdAt | timestamp | notnull=1 | pk=0
- updatedAt | timestamp | notnull=1 | pk=0

## auth_provider_sync_history
- row_count: 0
- id | INTEGER | notnull=0 | pk=1
- providerType | VARCHAR(32) | notnull=1 | pk=0
- runMode | TEXT | notnull=1 | pk=0
- status | TEXT | notnull=1 | pk=0
- startedAt | DATETIME | notnull=1 | pk=0
- endedAt | DATETIME | notnull=1 | pk=0
- scanned | INTEGER | notnull=1 | pk=0
- created | INTEGER | notnull=1 | pk=0
- updated | INTEGER | notnull=1 | pk=0
- disabled | INTEGER | notnull=1 | pk=0
- error | TEXT | notnull=0 | pk=0

## binary_data
- row_count: 0
- fileId | varchar | notnull=1 | pk=1
- sourceType | varchar(50) | notnull=1 | pk=0
- sourceId | varchar(255) | notnull=1 | pk=0
- data | BLOB | notnull=1 | pk=0
- mimeType | varchar(255) | notnull=0 | pk=0
- fileName | varchar(255) | notnull=0 | pk=0
- fileSize | INTEGER | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## chat_hub_agent_tools
- row_count: 0
- agentId | varchar | notnull=1 | pk=1
- toolId | varchar | notnull=1 | pk=2

## chat_hub_agents
- row_count: 0
- id | varchar | notnull=1 | pk=1
- name | varchar(256) | notnull=1 | pk=0
- description | varchar(512) | notnull=0 | pk=0
- systemPrompt | TEXT | notnull=1 | pk=0
- ownerId | varchar | notnull=1 | pk=0
- credentialId | varchar(36) | notnull=0 | pk=0
- provider | varchar(16) | notnull=1 | pk=0
- model | varchar(64) | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0
- icon | TEXT | notnull=0 | pk=0
- files | TEXT | notnull=1 | pk=0
- suggestedPrompts | TEXT | notnull=1 | pk=0

## chat_hub_messages
- row_count: 0
- id | varchar | notnull=1 | pk=1
- sessionId | varchar | notnull=1 | pk=0
- previousMessageId | varchar | notnull=0 | pk=0
- revisionOfMessageId | varchar | notnull=0 | pk=0
- retryOfMessageId | varchar | notnull=0 | pk=0
- type | varchar(16) | notnull=1 | pk=0
- name | varchar(128) | notnull=1 | pk=0
- content | TEXT | notnull=1 | pk=0
- provider | varchar(16) | notnull=0 | pk=0
- workflowId | varchar(36) | notnull=0 | pk=0
- executionId | INTEGER | notnull=0 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0
- agentId | varchar(36) | notnull=0 | pk=0
- status | varchar(16) | notnull=1 | pk=0
- attachments | TEXT | notnull=0 | pk=0
- model | VARCHAR(256) | notnull=0 | pk=0

## chat_hub_session_tools
- row_count: 0
- sessionId | varchar | notnull=1 | pk=1
- toolId | varchar | notnull=1 | pk=2

## chat_hub_sessions
- row_count: 0
- id | varchar | notnull=1 | pk=1
- title | varchar(256) | notnull=1 | pk=0
- ownerId | varchar | notnull=1 | pk=0
- lastMessageAt | datetime(3) | notnull=1 | pk=0
- credentialId | varchar(36) | notnull=0 | pk=0
- provider | varchar(16) | notnull=0 | pk=0
- model | varchar(64) | notnull=0 | pk=0
- workflowId | varchar(36) | notnull=0 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0
- agentId | varchar(36) | notnull=0 | pk=0
- agentName | varchar(128) | notnull=0 | pk=0
- type | varchar(16) | notnull=1 | pk=0

## chat_hub_tools
- row_count: 0
- id | varchar | notnull=1 | pk=1
- name | varchar(255) | notnull=1 | pk=0
- type | varchar(255) | notnull=1 | pk=0
- typeVersion | REAL | notnull=1 | pk=0
- ownerId | varchar | notnull=1 | pk=0
- definition | TEXT | notnull=1 | pk=0
- enabled | boolean | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## credential_dependency
- row_count: 0
- id | INTEGER | notnull=1 | pk=1
- credentialId | varchar(36) | notnull=1 | pk=0
- dependencyType | varchar(64) | notnull=1 | pk=0
- dependencyId | varchar(255) | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0

## credentials_entity
- row_count: 1
- id | varchar(36) | notnull=1 | pk=1
- name | varchar(128) | notnull=1 | pk=0
- data | TEXT | notnull=1 | pk=0
- type | varchar(32) | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0
- isManaged | boolean | notnull=1 | pk=0
- isGlobal | boolean | notnull=1 | pk=0
- isResolvable | boolean | notnull=1 | pk=0
- resolvableAllowFallback | boolean | notnull=1 | pk=0
- resolverId | varchar(16) | notnull=0 | pk=0

## data_table
- row_count: 0
- id | varchar(36) | notnull=1 | pk=1
- name | varchar(128) | notnull=1 | pk=0
- projectId | varchar(36) | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## data_table_column
- row_count: 0
- id | varchar(36) | notnull=1 | pk=1
- name | varchar(128) | notnull=1 | pk=0
- type | varchar(32) | notnull=1 | pk=0
- index | INTEGER | notnull=1 | pk=0
- dataTableId | varchar(36) | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## deployment_key
- row_count: 4
- id | varchar(36) | notnull=1 | pk=1
- type | varchar(64) | notnull=1 | pk=0
- value | TEXT | notnull=1 | pk=0
- algorithm | varchar(20) | notnull=0 | pk=0
- status | varchar(20) | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## dynamic_credential_entry
- row_count: 0
- credential_id | varchar(16) | notnull=1 | pk=1
- subject_id | varchar(2048) | notnull=1 | pk=2
- resolver_id | varchar(16) | notnull=1 | pk=3
- data | TEXT | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## dynamic_credential_resolver
- row_count: 0
- id | varchar(16) | notnull=1 | pk=1
- name | varchar(128) | notnull=1 | pk=0
- type | varchar(128) | notnull=1 | pk=0
- config | TEXT | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## dynamic_credential_user_entry
- row_count: 0
- credentialId | varchar(16) | notnull=1 | pk=1
- userId | varchar | notnull=1 | pk=2
- resolverId | varchar(16) | notnull=1 | pk=3
- data | TEXT | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## event_destinations
- row_count: 0
- id | varchar(36) | notnull=1 | pk=1
- destination | TEXT | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## execution_annotation_tags
- row_count: 0
- annotationId | INTEGER | notnull=1 | pk=1
- tagId | varchar(24) | notnull=1 | pk=2

## execution_annotations
- row_count: 0
- id | INTEGER | notnull=1 | pk=1
- executionId | INTEGER | notnull=1 | pk=0
- vote | varchar(6) | notnull=0 | pk=0
- note | TEXT | notnull=0 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## execution_data
- row_count: 2503
- executionId | INT | notnull=1 | pk=1
- workflowData | TEXT | notnull=1 | pk=0
- data | TEXT | notnull=1 | pk=0
- workflowVersionId | VARCHAR(36) | notnull=0 | pk=0

## execution_entity
- row_count: 2503
- id | INTEGER | notnull=1 | pk=1
- workflowId | varchar(36) | notnull=1 | pk=0
- finished | boolean | notnull=1 | pk=0
- mode | varchar | notnull=1 | pk=0
- retryOf | varchar | notnull=0 | pk=0
- retrySuccessId | varchar | notnull=0 | pk=0
- startedAt | datetime | notnull=0 | pk=0
- stoppedAt | datetime | notnull=0 | pk=0
- waitTill | datetime | notnull=0 | pk=0
- status | varchar | notnull=1 | pk=0
- deletedAt | datetime(3) | notnull=0 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- storedAt | VARCHAR(2) | notnull=1 | pk=0

## execution_metadata
- row_count: 0
- id | INTEGER | notnull=1 | pk=1
- executionId | INTEGER | notnull=1 | pk=0
- key | varchar(255) | notnull=1 | pk=0
- value | TEXT | notnull=1 | pk=0

## folder
- row_count: 1
- id | varchar(36) | notnull=1 | pk=1
- name | varchar(128) | notnull=1 | pk=0
- parentFolderId | varchar(36) | notnull=0 | pk=0
- projectId | varchar(36) | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## folder_tag
- row_count: 0
- folderId | varchar(36) | notnull=1 | pk=1
- tagId | varchar(36) | notnull=1 | pk=2

## insights_by_period
- row_count: 300
- id | INTEGER | notnull=1 | pk=1
- metaId | INTEGER | notnull=1 | pk=0
- type | INTEGER | notnull=1 | pk=0
- value | bigint | notnull=1 | pk=0
- periodUnit | INTEGER | notnull=1 | pk=0
- periodStart | datetime(0) | notnull=0 | pk=0

## insights_metadata
- row_count: 5
- metaId | INTEGER | notnull=1 | pk=1
- workflowId | varchar(16) | notnull=0 | pk=0
- projectId | varchar(36) | notnull=0 | pk=0
- workflowName | varchar(128) | notnull=1 | pk=0
- projectName | varchar(255) | notnull=1 | pk=0

## insights_raw
- row_count: 9
- id | INTEGER | notnull=1 | pk=1
- metaId | INTEGER | notnull=1 | pk=0
- type | INTEGER | notnull=1 | pk=0
- value | bigint | notnull=1 | pk=0
- timestamp | datetime(0) | notnull=1 | pk=0

## installed_nodes
- row_count: 0
- name | char(200) | notnull=1 | pk=1
- type | char(200) | notnull=1 | pk=0
- latestVersion | INTEGER | notnull=0 | pk=0
- package | char(214) | notnull=1 | pk=0

## installed_packages
- row_count: 0
- packageName | char(214) | notnull=1 | pk=1
- installedVersion | char(50) | notnull=1 | pk=0
- authorName | char(70) | notnull=0 | pk=0
- authorEmail | char(70) | notnull=0 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## instance_ai_iteration_logs
- row_count: 0
- id | varchar(36) | notnull=1 | pk=1
- threadId | varchar | notnull=1 | pk=0
- taskKey | varchar | notnull=1 | pk=0
- entry | TEXT | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## instance_ai_messages
- row_count: 0
- id | varchar(36) | notnull=1 | pk=1
- threadId | varchar | notnull=1 | pk=0
- content | TEXT | notnull=1 | pk=0
- role | varchar(16) | notnull=1 | pk=0
- type | varchar(32) | notnull=0 | pk=0
- resourceId | varchar(255) | notnull=0 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## instance_ai_observational_memory
- row_count: 0
- id | varchar(36) | notnull=1 | pk=1
- lookupKey | varchar(255) | notnull=1 | pk=0
- scope | varchar(16) | notnull=1 | pk=0
- threadId | varchar | notnull=0 | pk=0
- resourceId | varchar(255) | notnull=1 | pk=0
- activeObservations | TEXT | notnull=1 | pk=0
- originType | varchar(32) | notnull=1 | pk=0
- config | TEXT | notnull=1 | pk=0
- generationCount | INTEGER | notnull=1 | pk=0
- lastObservedAt | datetime(3) | notnull=0 | pk=0
- pendingMessageTokens | INTEGER | notnull=1 | pk=0
- totalTokensObserved | INTEGER | notnull=1 | pk=0
- observationTokenCount | INTEGER | notnull=1 | pk=0
- isObserving | boolean | notnull=1 | pk=0
- isReflecting | boolean | notnull=1 | pk=0
- observedMessageIds | TEXT | notnull=0 | pk=0
- observedTimezone | varchar | notnull=0 | pk=0
- bufferedObservations | TEXT | notnull=0 | pk=0
- bufferedObservationTokens | INTEGER | notnull=0 | pk=0
- bufferedMessageIds | TEXT | notnull=0 | pk=0
- bufferedReflection | TEXT | notnull=0 | pk=0
- bufferedReflectionTokens | INTEGER | notnull=0 | pk=0
- bufferedReflectionInputTokens | INTEGER | notnull=0 | pk=0
- reflectedObservationLineCount | INTEGER | notnull=0 | pk=0
- bufferedObservationChunks | TEXT | notnull=0 | pk=0
- isBufferingObservation | boolean | notnull=1 | pk=0
- isBufferingReflection | boolean | notnull=1 | pk=0
- lastBufferedAtTokens | INTEGER | notnull=1 | pk=0
- lastBufferedAtTime | datetime(3) | notnull=0 | pk=0
- metadata | TEXT | notnull=0 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## instance_ai_resources
- row_count: 0
- id | varchar(255) | notnull=1 | pk=1
- workingMemory | TEXT | notnull=0 | pk=0
- metadata | TEXT | notnull=0 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## instance_ai_run_snapshots
- row_count: 0
- threadId | varchar | notnull=1 | pk=1
- runId | varchar(36) | notnull=1 | pk=2
- messageGroupId | varchar(36) | notnull=0 | pk=0
- runIds | TEXT | notnull=0 | pk=0
- tree | TEXT | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## instance_ai_threads
- row_count: 0
- id | varchar | notnull=1 | pk=1
- resourceId | varchar(255) | notnull=1 | pk=0
- title | TEXT | notnull=1 | pk=0
- metadata | TEXT | notnull=0 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## instance_ai_workflow_snapshots
- row_count: 0
- runId | varchar(36) | notnull=1 | pk=1
- workflowName | varchar(255) | notnull=1 | pk=2
- resourceId | varchar(255) | notnull=0 | pk=0
- status | varchar | notnull=0 | pk=0
- snapshot | TEXT | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## instance_version_history
- row_count: 1
- id | INTEGER | notnull=1 | pk=1
- major | INTEGER | notnull=1 | pk=0
- minor | INTEGER | notnull=1 | pk=0
- patch | INTEGER | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0

## invalid_auth_token
- row_count: 0
- token | varchar(512) | notnull=1 | pk=1
- expiresAt | datetime(3) | notnull=1 | pk=0

## migrations
- row_count: 159
- id | INTEGER | notnull=1 | pk=1
- timestamp | bigint | notnull=1 | pk=0
- name | varchar | notnull=1 | pk=0

## oauth_access_tokens
- row_count: 0
- token | varchar | notnull=1 | pk=1
- clientId | varchar | notnull=1 | pk=0
- userId | varchar | notnull=1 | pk=0

## oauth_authorization_codes
- row_count: 0
- code | varchar(255) | notnull=1 | pk=1
- clientId | varchar | notnull=1 | pk=0
- userId | varchar | notnull=1 | pk=0
- redirectUri | varchar | notnull=1 | pk=0
- codeChallenge | varchar | notnull=1 | pk=0
- codeChallengeMethod | varchar(255) | notnull=1 | pk=0
- expiresAt | bigint | notnull=1 | pk=0
- state | varchar | notnull=0 | pk=0
- used | boolean | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## oauth_clients
- row_count: 0
- id | varchar | notnull=1 | pk=1
- name | varchar(255) | notnull=1 | pk=0
- redirectUris | TEXT | notnull=1 | pk=0
- grantTypes | TEXT | notnull=1 | pk=0
- clientSecret | varchar(255) | notnull=0 | pk=0
- clientSecretExpiresAt | bigint | notnull=0 | pk=0
- tokenEndpointAuthMethod | varchar(255) | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## oauth_refresh_tokens
- row_count: 0
- token | varchar(255) | notnull=1 | pk=1
- clientId | varchar | notnull=1 | pk=0
- userId | varchar | notnull=1 | pk=0
- expiresAt | bigint | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## oauth_user_consents
- row_count: 0
- id | INTEGER | notnull=1 | pk=1
- userId | varchar | notnull=1 | pk=0
- clientId | varchar | notnull=1 | pk=0
- grantedAt | bigint | notnull=1 | pk=0

## processed_data
- row_count: 0
- workflowId | varchar(36) | notnull=1 | pk=1
- context | varchar(255) | notnull=1 | pk=2
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0
- value | TEXT | notnull=1 | pk=0

## project
- row_count: 1
- id | varchar(36) | notnull=1 | pk=1
- name | varchar(255) | notnull=1 | pk=0
- type | varchar(36) | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0
- icon | TEXT | notnull=0 | pk=0
- description | varchar(512) | notnull=0 | pk=0
- creatorId | varchar | notnull=0 | pk=0

## project_relation
- row_count: 1
- projectId | varchar(36) | notnull=1 | pk=1
- userId | varchar | notnull=1 | pk=2
- role | varchar | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## project_secrets_provider_access
- row_count: 0
- secretsProviderConnectionId | INTEGER | notnull=1 | pk=1
- projectId | varchar(36) | notnull=1 | pk=2
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0
- role | varchar(128) | notnull=1 | pk=0

## role
- row_count: 15
- slug | varchar(128) | notnull=1 | pk=1
- displayName | TEXT | notnull=0 | pk=0
- description | TEXT | notnull=0 | pk=0
- roleType | TEXT | notnull=0 | pk=0
- systemRole | boolean | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## role_mapping_rule
- row_count: 0
- id | varchar(16) | notnull=1 | pk=1
- expression | TEXT | notnull=1 | pk=0
- role | varchar(128) | notnull=1 | pk=0
- type | varchar(64) | notnull=1 | pk=0
- order | INTEGER | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## role_mapping_rule_project
- row_count: 0
- roleMappingRuleId | varchar(16) | notnull=1 | pk=1
- projectId | varchar(36) | notnull=1 | pk=2

## role_scope
- row_count: 465
- roleSlug | VARCHAR(128) | notnull=1 | pk=1
- scopeSlug | VARCHAR(128) | notnull=1 | pk=2

## scope
- row_count: 189
- slug | varchar(128) | notnull=1 | pk=1
- displayName | TEXT | notnull=0 | pk=0
- description | TEXT | notnull=0 | pk=0

## secrets_provider_connection
- row_count: 0
- id | INTEGER | notnull=1 | pk=1
- providerKey | varchar(128) | notnull=1 | pk=0
- type | varchar(36) | notnull=1 | pk=0
- encryptedSettings | TEXT | notnull=1 | pk=0
- isEnabled | boolean | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## settings
- row_count: 5
- key | TEXT | notnull=1 | pk=1
- value | TEXT | notnull=1 | pk=0
- loadOnStartup | boolean | notnull=1 | pk=0

## shared_credentials
- row_count: 1
- credentialsId | varchar(36) | notnull=1 | pk=1
- projectId | varchar(36) | notnull=1 | pk=2
- role | TEXT | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## shared_workflow
- row_count: 71
- workflowId | varchar(36) | notnull=1 | pk=1
- projectId | varchar(36) | notnull=1 | pk=2
- role | TEXT | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## sqlite_sequence
- row_count: 5
- name |  | notnull=0 | pk=0
- seq |  | notnull=0 | pk=0

## tag_entity
- row_count: 0
- id | varchar(36) | notnull=1 | pk=1
- name | varchar(24) | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## test_case_execution
- row_count: 0
- id | varchar(36) | notnull=1 | pk=1
- testRunId | varchar(36) | notnull=1 | pk=0
- pastExecutionId | INTEGER | notnull=0 | pk=0
- executionId | INTEGER | notnull=0 | pk=0
- evaluationExecutionId | INTEGER | notnull=0 | pk=0
- status | varchar | notnull=1 | pk=0
- runAt | datetime(3) | notnull=0 | pk=0
- completedAt | datetime(3) | notnull=0 | pk=0
- errorCode | varchar | notnull=0 | pk=0
- errorDetails | TEXT | notnull=0 | pk=0
- metrics | TEXT | notnull=0 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0
- inputs | TEXT | notnull=0 | pk=0
- outputs | TEXT | notnull=0 | pk=0

## test_run
- row_count: 0
- id | varchar(36) | notnull=1 | pk=1
- workflowId | varchar(36) | notnull=1 | pk=0
- status | varchar | notnull=1 | pk=0
- errorCode | varchar | notnull=0 | pk=0
- errorDetails | TEXT | notnull=0 | pk=0
- runAt | datetime(3) | notnull=0 | pk=0
- completedAt | datetime(3) | notnull=0 | pk=0
- metrics | TEXT | notnull=0 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0
- runningInstanceId | VARCHAR(255) | notnull=0 | pk=0
- cancelRequested | BOOLEAN | notnull=1 | pk=0

## token_exchange_jti
- row_count: 0
- jti | varchar(255) | notnull=1 | pk=1
- expiresAt | datetime(3) | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0

## trusted_key
- row_count: 0
- sourceId | varchar(36) | notnull=1 | pk=1
- kid | varchar(255) | notnull=1 | pk=2
- data | TEXT | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0

## trusted_key_source
- row_count: 0
- id | varchar(36) | notnull=1 | pk=1
- type | varchar(32) | notnull=1 | pk=0
- config | TEXT | notnull=1 | pk=0
- status | varchar(32) | notnull=1 | pk=0
- lastError | TEXT | notnull=0 | pk=0
- lastRefreshedAt | datetime(3) | notnull=0 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## user
- row_count: 1
- id | varchar | notnull=0 | pk=1
- email | varchar(255) | notnull=0 | pk=0
- firstName | varchar(32) | notnull=0 | pk=0
- lastName | varchar(32) | notnull=0 | pk=0
- password | varchar | notnull=0 | pk=0
- personalizationAnswers | TEXT | notnull=0 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0
- settings | TEXT | notnull=0 | pk=0
- disabled | boolean | notnull=1 | pk=0
- mfaEnabled | boolean | notnull=1 | pk=0
- mfaSecret | TEXT | notnull=0 | pk=0
- mfaRecoveryCodes | TEXT | notnull=0 | pk=0
- lastActiveAt | date | notnull=0 | pk=0
- roleSlug | varchar(128) | notnull=1 | pk=0

## user_api_keys
- row_count: 1
- id | varchar(36) | notnull=1 | pk=1
- userId | varchar | notnull=1 | pk=0
- label | varchar(100) | notnull=1 | pk=0
- apiKey | varchar | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0
- scopes | TEXT | notnull=0 | pk=0
- audience | varchar | notnull=1 | pk=0

## user_favorites
- row_count: 1
- id | INTEGER | notnull=1 | pk=1
- userId | varchar | notnull=1 | pk=0
- resourceId | varchar(255) | notnull=1 | pk=0
- resourceType | varchar(64) | notnull=1 | pk=0

## variables
- row_count: 0
- id | varchar(36) | notnull=1 | pk=1
- key | TEXT | notnull=1 | pk=0
- type | TEXT | notnull=1 | pk=0
- value | TEXT | notnull=0 | pk=0
- projectId | varchar(36) | notnull=0 | pk=0

## webhook_entity
- row_count: 6
- workflowId | varchar(36) | notnull=1 | pk=0
- webhookPath | varchar | notnull=1 | pk=1
- method | varchar | notnull=1 | pk=2
- node | varchar | notnull=1 | pk=0
- webhookId | varchar | notnull=0 | pk=0
- pathLength | INTEGER | notnull=0 | pk=0

## workflow_builder_session
- row_count: 0
- id | varchar | notnull=1 | pk=1
- workflowId | varchar(36) | notnull=1 | pk=0
- userId | varchar | notnull=1 | pk=0
- messages | TEXT | notnull=1 | pk=0
- previousSummary | TEXT | notnull=0 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0
- activeVersionCardId | varchar(255) | notnull=0 | pk=0
- resumeAfterRestoreMessageId | varchar(255) | notnull=0 | pk=0

## workflow_dependency
- row_count: 1672
- id | INTEGER | notnull=1 | pk=1
- workflowId | varchar(36) | notnull=1 | pk=0
- workflowVersionId | INTEGER | notnull=1 | pk=0
- dependencyType | varchar(32) | notnull=1 | pk=0
- dependencyKey | varchar(255) | notnull=1 | pk=0
- indexVersionId | smallint | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- dependencyInfo | TEXT | notnull=0 | pk=0
- publishedVersionId | varchar(36) | notnull=0 | pk=0

## workflow_entity
- row_count: 71
- id | varchar(36) | notnull=1 | pk=1
- name | varchar(128) | notnull=1 | pk=0
- active | boolean | notnull=1 | pk=0
- nodes | TEXT | notnull=0 | pk=0
- connections | TEXT | notnull=0 | pk=0
- settings | TEXT | notnull=0 | pk=0
- staticData | TEXT | notnull=0 | pk=0
- pinData | TEXT | notnull=0 | pk=0
- versionId | varchar(36) | notnull=1 | pk=0
- triggerCount | INTEGER | notnull=0 | pk=0
- meta | TEXT | notnull=0 | pk=0
- parentFolderId | varchar(36) | notnull=0 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0
- isArchived | boolean | notnull=1 | pk=0
- versionCounter | INTEGER | notnull=1 | pk=0
- description | TEXT | notnull=0 | pk=0
- activeVersionId | varchar(36) | notnull=0 | pk=0

## workflow_history
- row_count: 71
- versionId | varchar(36) | notnull=1 | pk=1
- workflowId | varchar(36) | notnull=1 | pk=0
- authors | varchar(255) | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0
- nodes | TEXT | notnull=1 | pk=0
- connections | TEXT | notnull=1 | pk=0
- name | varchar(128) | notnull=0 | pk=0
- autosaved | boolean | notnull=1 | pk=0
- description | TEXT | notnull=0 | pk=0

## workflow_publish_history
- row_count: 495
- id | INTEGER | notnull=1 | pk=1
- workflowId | varchar(36) | notnull=1 | pk=0
- versionId | varchar(36) | notnull=0 | pk=0
- event | varchar(36) | notnull=1 | pk=0
- userId | varchar | notnull=0 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0

## workflow_published_version
- row_count: 0
- workflowId | varchar(36) | notnull=1 | pk=1
- publishedVersionId | varchar(36) | notnull=1 | pk=0
- createdAt | datetime(3) | notnull=1 | pk=0
- updatedAt | datetime(3) | notnull=1 | pk=0

## workflow_statistics
- row_count: 53
- id | INTEGER | notnull=0 | pk=1
- count | INTEGER | notnull=0 | pk=0
- latestEvent | DATETIME | notnull=0 | pk=0
- name | VARCHAR(128) | notnull=1 | pk=0
- workflowId | VARCHAR(36) | notnull=1 | pk=0
- workflowName | VARCHAR(128) | notnull=0 | pk=0
- rootCount | INTEGER | notnull=0 | pk=0

## workflows_tags
- row_count: 0
- workflowId | varchar(36) | notnull=1 | pk=1
- tagId | INTEGER | notnull=1 | pk=2
