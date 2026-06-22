---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================

# `mongosh` Methods

## Introduction

This page contains :binary:`~bin.mongosh` methods.

.. include:: /includes/extracts/admonition-js-prevalence-methods.rst

## Native Methods

The methods listed in this section are :binary:`mongosh` functional replacements for the native methods that were available in the legacy `mongo` shell. These methods are not exact replacements: output formats and some functionality may differ from the corresponding legacy methods.

In addition to these methods, the [mongocompat snippet](https://github.com/mongodb-labs/mongosh-snippets/blob/main/snippets/mongocompat/index.js)_ provides access to legacy :binary:`mongo` shell APIs.

> **Note:** In the following table `<path>` and `<filename>` are strings and
should be in quotes.
.. code-block:: javascript
   :copyable: false
   // process.chdir( <path> )
   process.chdir( "./data/incoming" )

.. include:: /includes/method/native-methods.rst

## Atlas Search Index

.. versionadded:: 7.0 (Also available starting in 6.0.7)

.. include:: /includes/atlas-search-commands/mongosh-method-intro.rst

.. include:: /includes/atlas-search-commands/mongosh-method-table.rst

## Atlas Stream Processing

:atlas:`Atlas Stream Processors </atlas-sp/overview/#mongodb-expression-exp.Stream-Processor>` let you perform aggregation operations against streams of continuous data using the same data model and query API that you use with at-rest data.

Use the following methods to manage Stream Processors:

> **Important:** The following methods can only be run on deployments hosted on
:atlas:`MongoDB Atlas </>`.

## Collections

## Cursors

These methods modify the way that the underlying query is executed.

## Databases

## Query Plan Caches

The PlanCache methods are only accessible from a collection's plan cache object. To retrieve the plan cache object, use the :method:`db.collection.getPlanCache()` method.

## Bulk Operations

.. include:: /includes/fact-bulkwrite.rst

## User Management

## Role Management

## Replication

## Sharding

.. include:: /includes/mongosh-sharding-methods.rst

## Object Constructors

## Connections

## In-Use Encryption

MongoDB supports two approaches to `In-Use Encryption <about-qe-csfle>`, {+csfle+} (CSFLE) and {+qe+} (QE). `ClientEncryption` is an abstraction used across drivers and :binary:`~bin.mongosh` that encapsulates operations for both CSFLE and QE. However, some methods are specific to one feature.

> **Note:** .. include:: /includes/extracts/csfle-requires-enabling-encryption.rst

.. include:: /includes/table-clientencryption-methods.rst

## Contents

- connect </reference/method/connect>
- Mongo </reference/method/Mongo>
- Mongo.getDB </reference/method/Mongo.getDB>
- Mongo.getDBNames </reference/method/Mongo.getDBNames>
- Mongo.getDBs </reference/method/Mongo.getDBs>
- Mongo.getReadPrefMode </reference/method/Mongo.getReadPrefMode>
- Mongo.getReadPrefTagSet </reference/method/Mongo.getReadPrefTagSet>
- Mongo.getURI </reference/method/Mongo.getURI>
- Mongo.getWriteConcern </reference/method/Mongo.getWriteConcern>
- Mongo.setCausalConsistency </reference/method/Mongo.setCausalConsistency>
- Mongo.setReadPref </reference/method/Mongo.setReadPref>
- Mongo.startSession </reference/method/Mongo.startSession>
- Mongo.setWriteConcern </reference/method/Mongo.setWriteConcern>
- Mongo.watch </reference/method/Mongo.watch>
- Session </reference/method/Session>
- SessionOptions </reference/method/SessionOptions>
- ClientEncryption.createEncryptedCollection </reference/method/ClientEncryption.createEncryptedCollection>
- ClientEncryption.encrypt </reference/method/ClientEncryption.encrypt>
- ClientEncryption.encryptExpression </reference/method/ClientEncryption.encryptExpression>
- ClientEncryption.decrypt </reference/method/ClientEncryption.decrypt>
- getClientEncryption </reference/method/getClientEncryption>
- getKeyVault </reference/method/getKeyVault>
- KeyVault.addKeyName </reference/method/KeyVault.addKeyName>
- KeyVault.addKeyAlternateName </reference/method/KeyVault.addKeyAlternateName>
- KeyVault.createDataKey </reference/method/KeyVault.createDataKey>
- KeyVault.createKey </reference/method/KeyVault.createKey>
- KeyVault.deleteKey </reference/method/KeyVault.deleteKey>
- KeyVault.getKey </reference/method/KeyVault.getKey>
- KeyVault.getKeys </reference/method/KeyVault.getKeys>
- KeyVault.getKeyByAltName </reference/method/KeyVault.getKeyByAltName>
- KeyVault.removeKeyAlternateName </reference/method/KeyVault.removeKeyAlternateName>
- KeyVault.removeKeyAltName </reference/method/KeyVault.removeKeyAltName>
- KeyVault.rewrapManyDataKey </reference/method/KeyVault.rewrapManyDataKey>
- rs.add </reference/method/rs.add>
- rs.addArb </reference/method/rs.addArb>
- rs.conf </reference/method/rs.conf>
- rs.freeze </reference/method/rs.freeze>
- rs.help </reference/method/rs.help>
- rs.initiate </reference/method/rs.initiate>
- rs.printReplicationInfo </reference/method/rs.printReplicationInfo>
- rs.printSecondaryReplicationInfo </reference/method/rs.printSecondaryReplicationInfo>
- rs.reconfig </reference/method/rs.reconfig>
- rs.reconfigForPSASet </reference/method/rs.reconfigForPSASet>
- rs.remove </reference/method/rs.remove>
- rs.status </reference/method/rs.status>
- rs.stepDown </reference/method/rs.stepDown>
- rs.syncFrom </reference/method/rs.syncFrom>
- convertShardKeyToHashed </reference/method/convertShardKeyToHashed>
- db.checkMetadataConsistency </reference/method/db.checkMetadataConsistency>
- db.collection.checkMetadataConsistency </reference/method/db.collection.checkMetadataConsistency>
- db.collection.getShardLocation <reference/method/db.collection.getShardLocation>
- sh.abortMoveCollection </reference/method/sh.abortMoveCollection>
- sh.abortReshardCollection </reference/method/sh.abortReshardCollection>
- sh.abortUnshardCollection </reference/method/sh.abortUnshardCollection>
- sh.addShard </reference/method/sh.addShard>
- sh.addShardTag </reference/method/sh.addShardTag>
- sh.addShardToZone </reference/method/sh.addShardToZone>
- sh.addTagRange </reference/method/sh.addTagRange>
- sh.balancerCollectionStatus </reference/method/sh.balancerCollectionStatus>
- sh.checkMetadataConsistency </reference/method/sh.checkMetadataConsistency>
- sh.commitReshardCollection </reference/method/sh.commitReshardCollection>
- sh.disableAutoMerger </reference/method/sh.disableAutoMerger>
- sh.disableAutoSplit </reference/method/sh.disableAutoSplit>
- sh.disableBalancing </reference/method/sh.disableBalancing>
- sh.disableMigrations </reference/method/sh.disableMigrations>
- sh.enableAutoMerger </reference/method/sh.enableAutoMerger>
- sh.enableBalancing </reference/method/sh.enableBalancing>
- sh.enableAutoSplit </reference/method/sh.enableAutoSplit>
- sh.enableMigrations </reference/method/sh.enableMigrations>
- sh.enableSharding </reference/method/sh.enableSharding>
- sh.getBalancerState </reference/method/sh.getBalancerState>
- sh.getShardedDataDistribution </reference/method/sh.getShardedDataDistribution>
- sh.help </reference/method/sh.help>
- sh.isBalancerRunning </reference/method/sh.isBalancerRunning>
- sh.isConfigShardEnabled </reference/method/sh.isConfigShardEnabled>
- sh.listShards </reference/method/sh.listShards>
- sh.moveChunk </reference/method/sh.moveChunk>
- sh.moveCollection </reference/method/sh.moveCollection>
- sh.moveRange </reference/method/sh.moveRange>
- sh.removeRangeFromZone </reference/method/sh.removeRangeFromZone>
- sh.removeShardTag </reference/method/sh.removeShardTag>
- sh.removeShardFromZone </reference/method/sh.removeShardFromZone>
- sh.removeTagRange </reference/method/sh.removeTagRange>
- sh.reshardCollection </reference/method/sh.reshardCollection>
- sh.setBalancerState </reference/method/sh.setBalancerState>
- sh.shardAndDistributeCollection </reference/method/sh.shardAndDistributeCollection>
- sh.shardCollection </reference/method/sh.shardCollection>
- sh.splitAt </reference/method/sh.splitAt>
- sh.splitFind </reference/method/sh.splitFind>
- sh.startAutoMerger </reference/method/sh.startAutoMerger>
- sh.startBalancer </reference/method/sh.startBalancer>
- sh.status </reference/method/sh.status>
- sh.stopAutoMerger </reference/method/sh.stopAutoMerger>
- sh.stopBalancer </reference/method/sh.stopBalancer>
- sh.unshardCollection </reference/method/sh.unshardCollection>
- sh.updateZoneKeyRange </reference/method/sh.updateZoneKeyRange>
- sh.waitForBalancer </reference/method/sh.waitForBalancer>
- sh.waitForBalancerOff </reference/method/sh.waitForBalancerOff>
- sh.waitForPingChange </reference/method/sh.waitForPingChange>
- db.createRole </reference/method/db.createRole>
- db.dropRole </reference/method/db.dropRole>
- db.dropAllRoles </reference/method/db.dropAllRoles>
- db.getRole </reference/method/db.getRole>
- db.getRoles </reference/method/db.getRoles>
- db.grantPrivilegesToRole </reference/method/db.grantPrivilegesToRole>
- db.revokePrivilegesFromRole </reference/method/db.revokePrivilegesFromRole>
- db.grantRolesToRole </reference/method/db.grantRolesToRole>
- db.revokeRolesFromRole </reference/method/db.revokeRolesFromRole>
- db.updateRole </reference/method/db.updateRole>
- db.auth </reference/method/db.auth>
- db.changeUserPassword </reference/method/db.changeUserPassword>
- db.createUser </reference/method/db.createUser>
- db.dropUser </reference/method/db.dropUser>
- db.dropAllUsers </reference/method/db.dropAllUsers>
- db.getUser </reference/method/db.getUser>
- db.getUsers </reference/method/db.getUsers>
- db.grantRolesToUser </reference/method/db.grantRolesToUser>
- db.removeUser </reference/method/db.removeUser>
- db.revokeRolesFromUser </reference/method/db.revokeRolesFromUser>
- db.createEncryptedCollection </reference/method/db.createEncryptedCollection>
- db.updateUser </reference/method/db.updateUser>
- passwordPrompt </reference/method/passwordPrompt>
- db.collection.initializeOrderedBulkOp </reference/method/db.collection.initializeOrderedBulkOp>
- db.collection.initializeUnorderedBulkOp </reference/method/db.collection.initializeUnorderedBulkOp>
- Mongo.bulkWrite </reference/method/Mongo.bulkWrite>
- Bulk </reference/method/Bulk>
- Bulk.execute </reference/method/Bulk.execute>
- Bulk.find </reference/method/Bulk.find>
- Bulk.find.arrayFilters </reference/method/Bulk.find.arrayFilters>
- Bulk.find.collation </reference/method/Bulk.find.collation>
- Bulk.find.delete </reference/method/Bulk.find.delete>
- Bulk.find.deleteOne </reference/method/Bulk.find.deleteOne>
- Bulk.find.hint </reference/method/Bulk.find.hint>
- Bulk.find.remove </reference/method/Bulk.find.remove>
- Bulk.find.removeOne </reference/method/Bulk.find.removeOne>
- Bulk.find.replaceOne </reference/method/Bulk.find.replaceOne>
- Bulk.find.updateOne </reference/method/Bulk.find.updateOne>
- Bulk.find.update </reference/method/Bulk.find.update>
- Bulk.find.upsert </reference/method/Bulk.find.upsert>
- Bulk.getOperations </reference/method/Bulk.getOperations>
- Bulk.insert </reference/method/Bulk.insert>
- Bulk.tojson </reference/method/Bulk.tojson>
- Bulk.toString </reference/method/Bulk.toString>
- db.collection.getPlanCache </reference/method/db.collection.getPlanCache>
- PlanCache.clear </reference/method/PlanCache.clear>
- PlanCache.clearPlansByQuery </reference/method/PlanCache.clearPlansByQuery>
- PlanCache.help </reference/method/PlanCache.help>
- PlanCache.list </reference/method/PlanCache.list>
- db.adminCommand </reference/method/db.adminCommand>
- db.aggregate </reference/method/db.aggregate>
- db.commandHelp </reference/method/db.commandHelp>
- db.createCollection </reference/method/db.createCollection>
- db.createView </reference/method/db.createView>
- db.currentOp </reference/method/db.currentOp>
- db.dropDatabase </reference/method/db.dropDatabase>
- db.fsyncLock </reference/method/db.fsyncLock>
- db.fsyncUnlock </reference/method/db.fsyncUnlock>
- db.getCollection </reference/method/db.getCollection>
- db.getCollectionInfos </reference/method/db.getCollectionInfos>
- db.getCollectionNames </reference/method/db.getCollectionNames>
- db.getLogComponents </reference/method/db.getLogComponents>
- db.getMongo </reference/method/db.getMongo>
- db.getName </reference/method/db.getName>
- db.getProfilingStatus </reference/method/db.getProfilingStatus>
- db.getReplicationInfo </reference/method/db.getReplicationInfo>
- db.getSiblingDB </reference/method/db.getSiblingDB>
- db.hello </reference/method/db.hello>
- db.help </reference/method/db.help>
- db.hostInfo </reference/method/db.hostInfo>
- db.killOp </reference/method/db.killOp>
- db.listCommands </reference/method/db.listCommands>
- db.logout </reference/method/db.logout>
- db.printCollectionStats </reference/method/db.printCollectionStats>
- db.printReplicationInfo </reference/method/db.printReplicationInfo>
- db.printSecondaryReplicationInfo </reference/method/db.printSecondaryReplicationInfo>
- db.printShardingStatus </reference/method/db.printShardingStatus>
- db.rotateCertificates </reference/method/db.rotateCertificates>
- db.runCommand </reference/method/db.runCommand>
- db.serverBuildInfo </reference/method/db.serverBuildInfo>
- db.serverCmdLineOpts </reference/method/db.serverCmdLineOpts>
- db.serverStatus </reference/method/db.serverStatus>
- db.setLogLevel </reference/method/db.setLogLevel>
- db.setProfilingLevel </reference/method/db.setProfilingLevel>
- db.shutdownServer </reference/method/db.shutdownServer>
- db.stats </reference/method/db.stats>
- db.version </reference/method/db.version>
- db.watch </reference/method/db.watch>
- cursor.addOption </reference/method/cursor.addOption>
- cursor.allowDiskUse </reference/method/cursor.allowDiskUse>
- cursor.batchSize </reference/method/cursor.batchSize>
- cursor.close </reference/method/cursor.close>
- cursor.isClosed </reference/method/cursor.isClosed>
- cursor.collation </reference/method/cursor.collation>
- cursor.comment </reference/method/cursor.comment>
- cursor.count </reference/method/cursor.count>
- cursor.disableBlockWarnings </reference/method/cursor.disableBlockWarnings>
- cursor.explain </reference/method/cursor.explain>
- cursor.forEach </reference/method/cursor.forEach>
- cursor.hasNext </reference/method/cursor.hasNext>
- cursor.hint </reference/method/cursor.hint>
- cursor.isExhausted </reference/method/cursor.isExhausted>
- cursor.itcount </reference/method/cursor.itcount>
- cursor.limit </reference/method/cursor.limit>
- cursor.map </reference/method/cursor.map>
- cursor.max </reference/method/cursor.max>
- cursor.maxAwaitTimeMS </reference/method/cursor.maxAwaitTimeMS>
- cursor.maxTimeMS </reference/method/cursor.maxTimeMS>
- cursor.min </reference/method/cursor.min>
- cursor.next </reference/method/cursor.next>
- cursor.noCursorTimeout </reference/method/cursor.noCursorTimeout>
- cursor.objsLeftInBatch </reference/method/cursor.objsLeftInBatch>
- cursor.pretty </reference/method/cursor.pretty>
- cursor.readConcern </reference/method/cursor.readConcern>
- cursor.readPref </reference/method/cursor.readPref>
- cursor.returnKey </reference/method/cursor.returnKey>
- cursor.showRecordId </reference/method/cursor.showRecordId>
- cursor.size </reference/method/cursor.size>
- cursor.skip </reference/method/cursor.skip>
- cursor.sort </reference/method/cursor.sort>
- cursor.tailable </reference/method/cursor.tailable>
- cursor.toArray </reference/method/cursor.toArray>
- cursor.tryNext </reference/method/cursor.tryNext>
- db.collection.aggregate </reference/method/db.collection.aggregate>
- db.collection.analyzeShardKey </reference/method/db.collection.analyzeShardKey>
- db.collection.bulkWrite </reference/method/db.collection.bulkWrite>
- db.collection.compactStructuredEncryptionData </reference/method/db.collection.compactStructuredEncryptionData>
- db.collection.configureQueryAnalyzer </reference/method/db.collection.configureQueryAnalyzer>
- db.collection.count </reference/method/db.collection.count>
- db.collection.countDocuments </reference/method/db.collection.countDocuments>
- db.collection.createIndex </reference/method/db.collection.createIndex>
- db.collection.createIndexes </reference/method/db.collection.createIndexes>
- db.collection.dataSize </reference/method/db.collection.dataSize>
- db.collection.deleteMany </reference/method/db.collection.deleteMany>
- db.collection.deleteOne </reference/method/db.collection.deleteOne>
- db.collection.distinct </reference/method/db.collection.distinct>
- db.collection.drop </reference/method/db.collection.drop>
- db.collection.dropIndex </reference/method/db.collection.dropIndex>
- db.collection.dropIndexes </reference/method/db.collection.dropIndexes>
- db.collection.estimatedDocumentCount  </reference/method/db.collection.estimatedDocumentCount>
- db.collection.explain </reference/method/db.collection.explain>
- db.collection.find </reference/method/db.collection.find>
- db.collection.findAndModify </reference/method/db.collection.findAndModify>
- db.collection.findOne </reference/method/db.collection.findOne>
- db.collection.findOneAndDelete </reference/method/db.collection.findOneAndDelete>
- db.collection.findOneAndReplace </reference/method/db.collection.findOneAndReplace>
- db.collection.findOneAndUpdate </reference/method/db.collection.findOneAndUpdate>
- db.collection.getIndexes </reference/method/db.collection.getIndexes>
- db.collection.getShardDistribution </reference/method/db.collection.getShardDistribution>
- db.collection.getShardVersion </reference/method/db.collection.getShardVersion>
- db.collection.hideIndex </reference/method/db.collection.hideIndex>
- db.collection.insert </reference/method/db.collection.insert>
- db.collection.insertMany </reference/method/db.collection.insertMany>
- db.collection.insertOne </reference/method/db.collection.insertOne>
- db.collection.isCapped </reference/method/db.collection.isCapped>
- db.collection.latencyStats </reference/method/db.collection.latencyStats>
- db.collection.mapReduce </reference/method/db.collection.mapReduce>
- db.collection.reIndex </reference/method/db.collection.reIndex>
- db.collection.remove </reference/method/db.collection.remove>
- db.collection.renameCollection </reference/method/db.collection.renameCollection>
- db.collection.replaceOne </reference/method/db.collection.replaceOne>
- db.collection.stats </reference/method/db.collection.stats>
- db.collection.storageSize </reference/method/db.collection.storageSize>
- db.collection.totalIndexSize </reference/method/db.collection.totalIndexSize>
- db.collection.totalSize </reference/method/db.collection.totalSize>
- db.collection.unhideIndex </reference/method/db.collection.unhideIndex>
- db.collection.update </reference/method/db.collection.update>
- db.collection.updateMany </reference/method/db.collection.updateMany>
- db.collection.updateOne </reference/method/db.collection.updateOne>
- db.collection.validate </reference/method/db.collection.validate>
- db.collection.watch </reference/method/db.collection.watch>
- db.collection.createSearchIndex </reference/method/db.collection.createSearchIndex>
- db.collection.dropSearchIndex </reference/method/db.collection.dropSearchIndex>
- db.collection.getSearchIndexes </reference/method/db.collection.getSearchIndexes>
- db.collection.updateSearchIndex </reference/method/db.collection.updateSearchIndex>
- sp.createStreamProcessor </reference/method/sp.createStreamProcessor>
- sp.listConnections </reference/method/sp.listConnections>
- sp.listStreamProcessors </reference/method/sp.listStreamProcessors>
- sp.listWorkspaceDefaults </reference/method/sp.listWorkspaceDefaults>
- sp.process </reference/method/sp.process>
- sp.processor.drop </reference/method/sp.processor.drop>
- sp.processor.sample </reference/method/sp.processor.sample>
- sp.processor.start </reference/method/sp.processor.start>
- sp.processor.stats </reference/method/sp.processor.stats>
- sp.processor.stop </reference/method/sp.processor.stop>
- Binary.createFromBase64 </reference/method/Binary.createFromBase64>
- Binary.createFromHexString </reference/method/Binary.createFromHexString>
- BinData </reference/method/BinData>
- BSONRegExp </reference/method/BSONRegExp>
- BulkWriteResult </reference/method/BulkWriteResult>
- Date </reference/method/Date>
- HexData </reference/method/HexData>
- ObjectId </reference/method/ObjectId>
- ObjectId.createFromBase64 </reference/method/ObjectId.createFromBase64>
- ObjectId.createFromHexString </reference/method/ObjectId.createFromHexString>
- ObjectId.getTimestamp </reference/method/ObjectId.getTimestamp>
- ObjectId.toString </reference/method/ObjectId.toString>
- UUID </reference/method/UUID>
- WriteResult </reference/method/WriteResult>
