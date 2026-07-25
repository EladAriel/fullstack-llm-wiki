---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=================

# Database Commands

All command documentation outlined below describes a command and its available parameters and provides a document template or prototype for each command. Some command documentation also includes the relevant :binary:`~bin.mongosh` helpers.

To run a command against the current database, use :method:`db.runCommand()`:

```javascript
db.runCommand( { <command> } )
```

To run an administrative command against the `admin` database, use :method:`db.adminCommand()`:

```javascript
db.adminCommand( { <command> } )
```

.. include:: /includes/extracts/commands-toc-explanation.rst

## Command Syntax

When you run a database command, you specify the command as a document to :method:`db.runCommand()`. The document's key is the command to run, and the value is typically supplied as `1`. The value does not affect the output of the command for example:

```javascript
db.runCommand( { hello: 1 } )
```

## User Commands

### Aggregation Commands

### Query and Write Operation Commands

### Query Plan Cache Commands

## Contents

- planCacheClear </reference/command/planCacheClear>
- planCacheClearFilters </reference/command/planCacheClearFilters>
- planCacheListFilters </reference/command/planCacheListFilters>
- planCacheSetFilter </reference/command/planCacheSetFilter>

## Database Operations

### Authentication Commands

## Contents

- authenticate </reference/command/authenticate>
- logout </reference/command/logout>

### User Management Commands

## Contents

- createUser </reference/command/createUser>
- dropAllUsersFromDatabase </reference/command/dropAllUsersFromDatabase>
- dropUser </reference/command/dropUser>
- grantRolesToUser </reference/command/grantRolesToUser>
- revokeRolesFromUser </reference/command/revokeRolesFromUser>
- updateUser </reference/command/updateUser>
- usersInfo </reference/command/usersInfo>

### Role Management Commands

## Contents

- createRole </reference/command/createRole>
- dropAllRolesFromDatabase </reference/command/dropAllRolesFromDatabase>
- dropRole </reference/command/dropRole>
- grantPrivilegesToRole </reference/command/grantPrivilegesToRole>
- grantRolesToRole </reference/command/grantRolesToRole>
- invalidateUserCache </reference/command/invalidateUserCache>
- revokePrivilegesFromRole </reference/command/revokePrivilegesFromRole>
- revokeRolesFromRole </reference/command/revokeRolesFromRole>
- rolesInfo </reference/command/rolesInfo>
- updateRole </reference/command/updateRole>

### Replication Commands

## Contents

- appendOplogNote </reference/command/appendOplogNote>
- applyOps </reference/command/applyOps>
- hello </reference/command/hello>
- replSetAbortPrimaryCatchUp </reference/command/replSetAbortPrimaryCatchUp>
- replSetFreeze </reference/command/replSetFreeze>
- replSetGetConfig </reference/command/replSetGetConfig>
- replSetGetStatus </reference/command/replSetGetStatus>
- replSetInitiate </reference/command/replSetInitiate>
- replSetMaintenance </reference/command/replSetMaintenance>
- replSetReconfig </reference/command/replSetReconfig>
- replSetResizeOplog </reference/command/replSetResizeOplog>
- replSetStepDown </reference/command/replSetStepDown>
- replSetSyncFrom </reference/command/replSetSyncFrom>

> **Seealso:** `/replication` for more information regarding
replication.

### Sharding Commands

## Contents

- abortMoveCollection </reference/command/abortMoveCollection>
- abortReshardCollection </reference/command/abortReshardCollection>
- abortRewriteCollection </reference/command/abortRewriteCollection>
- abortUnshardCollection </reference/command/abortUnshardCollection>
- addShard </reference/command/addShard>
- addShardToZone </reference/command/addShardToZone>
- analyzeShardKey </reference/command/analyzeShardKey>
- balancerCollectionStatus </reference/command/balancerCollectionStatus>
- balancerStart </reference/command/balancerStart>
- balancerStatus </reference/command/balancerStatus>
- balancerStop </reference/command/balancerStop>
- checkMetadataConsistency </reference/command/checkMetadataConsistency>
- clearJumboFlag </reference/command/clearJumboFlag>
- cleanupOrphaned </reference/command/cleanupOrphaned>
- cleanupReshardCollection </reference/command/cleanupReshardCollection>
- commitReshardCollection </reference/command/commitReshardCollection>
- commitShardRemoval </reference/command/commitShardRemoval>
- commitTransitionToDedicatedConfigServer </reference/command/commitTransitionToDedicatedConfigServer>
- configureCollectionBalancing </reference/command/configureCollectionBalancing>
- configureQueryAnalyzer </reference/command/configureQueryAnalyzer>
- enableSharding </reference/command/enableSharding>
- flushRouterConfig </reference/command/flushRouterConfig>
- getShardMap </reference/command/getShardMap>
- getTransitionToDedicatedConfigServerStatus </reference/command/getTransitionToDedicatedConfigServerStatus>
- isdbgrid </reference/command/isdbgrid>
- listShards </reference/command/listShards>
- mergeAllChunksOnShard </reference/command/mergeAllChunksOnShard>
- mergeChunks </reference/command/mergeChunks>
- moveChunk </reference/command/moveChunk>
- moveCollection </reference/command/moveCollection>
- movePrimary </reference/command/movePrimary>
- moveRange </reference/command/moveRange>
- refineCollectionShardKey </reference/command/refineCollectionShardKey>
- removeShard </reference/command/removeShard>
- removeShardFromZone </reference/command/removeShardFromZone>
- reshardCollection </reference/command/reshardCollection>
- rewriteCollection </reference/command/rewriteCollection>
- setAllowMigrations </reference/command/setAllowMigrations>
- shardCollection </reference/command/shardCollection>
- shardDrainingStatus </reference/command/shardDrainingStatus>
- shardingState </reference/command/shardingState>
- split </reference/command/split>
- startShardDraining </reference/command/startShardDraining>
- startTransitionToDedicatedConfigServer </reference/command/startTransitionToDedicatedConfigServer>
- stopShardDraining </reference/command/stopShardDraining>
- stopTransitionToDedicatedConfigServer </reference/command/stopTransitionToDedicatedConfigServer>
- transitionFromDedicatedConfigServer </reference/command/transitionFromDedicatedConfigServer>
- transitionToDedicatedConfigServer </reference/command/transitionToDedicatedConfigServer>
- unsetSharding </reference/command/unsetSharding>
- unshardCollection </reference/command/unshardCollection>
- updateZoneKeyRange </reference/command/updateZoneKeyRange>

> **Seealso:** `/sharding` for more information about MongoDB's
sharding functionality.

### Session Commands

.. include:: /includes/table-sessions-commands.rst

## Contents

- abortTransaction </reference/command/abortTransaction>
- commitTransaction </reference/command/commitTransaction>
- endSessions </reference/command/endSessions>
- killAllSessions </reference/command/killAllSessions>
- killAllSessionsByPattern </reference/command/killAllSessionsByPattern>
- killSessions </reference/command/killSessions>
- refreshSessions </reference/command/refreshSessions>
- startSession </reference/command/startSession>

### Administration Commands

## Contents

- autoCompact </reference/command/autoCompact>
- cloneCollectionAsCapped </reference/command/cloneCollectionAsCapped>
- collMod </reference/command/collMod>
- compact </reference/command/compact>
- compactStructuredEncryptionData </reference/command/compactStructuredEncryptionData>
- convertToCapped </reference/command/convertToCapped>
- create </reference/command/create>
- createIndexes </reference/command/createIndexes>
- currentOp </reference/command/currentOp>
- drop </reference/command/drop>
- dropDatabase </reference/command/dropDatabase>
- dropConnections </reference/command/dropConnections>
- dropIndexes </reference/command/dropIndexes>
- filemd5 </reference/command/filemd5>
- fsync </reference/command/fsync>
- fsyncUnlock </reference/command/fsyncUnlock>
- getAuditConfig </reference/command/getAuditConfig>
- getClusterParameter </reference/command/getClusterParameter>
- getDefaultRWConcern </reference/command/getDefaultRWConcern>
- getParameter </reference/command/getParameter>
- killCursors </reference/command/killCursors>
- killOp </reference/command/killOp>
- listCollections </reference/command/listCollections>
- listDatabases </reference/command/listDatabases>
- listIndexes </reference/command/listIndexes>
- logRotate </reference/command/logRotate>
- reIndex </reference/command/reIndex>
- removeQuerySettings </reference/command/removeQuerySettings>
- renameCollection </reference/command/renameCollection>
- rotateCertificates </reference/command/rotateCertificates>
- setAuditConfig </reference/command/setAuditConfig>
- setClusterParameter </reference/command/setClusterParameter>
- setDefaultRWConcern </reference/command/setDefaultRWConcern>
- setFeatureCompatibilityVersion </reference/command/setFeatureCompatibilityVersion>
- setIndexCommitQuorum </reference/command/setIndexCommitQuorum>
- setParameter </reference/command/setParameter>
- setQuerySettings </reference/command/setQuerySettings>
- setUserWriteBlockMode </reference/command/setUserWriteBlockMode>
- shutdown </reference/command/shutdown>

### Diagnostic Commands

## Contents

- buildInfo </reference/command/buildInfo>
- collStats </reference/command/collStats>
- connPoolStats </reference/command/connPoolStats>
- connectionStatus </reference/command/connectionStatus>
- dataSize </reference/command/dataSize>
- dbHash </reference/command/dbHash>
- dbStats </reference/command/dbStats>
- explain </reference/command/explain>
- getCmdLineOpts </reference/command/getCmdLineOpts>
- getLog </reference/command/getLog>
- hostInfo </reference/command/hostInfo>
- listCommands </reference/command/listCommands>
- lockInfo </reference/command/lockInfo>
- ping </reference/command/ping>
- profile </reference/command/profile>
- serverStatus </reference/command/serverStatus>
- shardConnPoolStats </reference/command/shardConnPoolStats>
- top </reference/command/top>
- validate </reference/command/validate>
- validateDBMetadata </reference/command/validateDBMetadata>
- whatsmyuri </reference/command/whatsmyuri>

### Auditing Commands

## Contents

- logApplicationMessage </reference/command/logApplicationMessage>

## Atlas Search

.. versionadded:: 7.0 (Also available starting in 6.0.7)

.. include:: /includes/atlas-search-commands/atlas-search-command-table.rst

## Contents

- createSearchIndexes </reference/command/createSearchIndexes>
- dropSearchIndex </reference/command/dropSearchIndex>
- updateSearchIndex </reference/command/updateSearchIndex>
