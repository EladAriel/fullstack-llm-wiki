---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/serverStatus.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# serverStatus (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand( 
   { 
     serverStatus: 1 
   } 
)
```

The value (that is, `1` above) does not affect the operation of the command. The `db.serverStatus()` command returns a large amount of data. To return a specific object or field from the output append the object or field name to the command.

For example:

```javascript
db.runCommand({ serverStatus: 1}).metrics
db.runCommand({ serverStatus: 1}).metrics.commands
db.runCommand({ serverStatus: 1}).metrics.commands.update
```

:binary:`~bin.mongosh` provides the :method:`db.serverStatus()` wrapper for the :dbcommand:`serverStatus` command.

> **Seealso:** Much of the output of :dbcommand:`serverStatus` is also displayed
dynamically by :binary:`~bin.mongostat`. See the
:binary:`~bin.mongostat` command for more information.

## Behavior

.. include:: /includes/extracts/serverStatus-command-projection.rst

For example, the following operation excludes the `repl`, `metrics` and `locks` information in the output.

```javascript
db.runCommand( { serverStatus: 1, repl: 0, metrics: 0, locks: 0 } )
```

For example, the following operation excludes the embedded `histogram` field in the output.

```javascript
db.runCommand( { serverStatus: 1, metrics: { query: { multiPlanner: { histograms: false } } } } )
```

The following example includes all `server-status-repl` information in the output:

```javascript
db.runCommand( { serverStatus: 1,  repl: 1 } )
```

### Exclude All Optional Fields

.. include:: /includes/fact-serverstatus-excl-fields-w-none.rst

This example uses `none` to initially exclude all optional field from the output, then includes the  `locks` document.

```javascript
db.runCommand({ serverStatus: 1, none: 1, locks: 1 })
```

### Initialization

The statistics reported by :dbcommand:`serverStatus` are reset when the :binary:`~bin.mongod` server is restarted.

This command always returns a value, even on a fresh database. The related command :method:`db.serverStatus()` does not always return a value unless a counter has started to increment for a particular metric.

After you run an update query, `db.serverStatus()` and `db.runCommand({ serverStatus: 1})` both return the same values.

```javascript
{
   arrayFilters : Long("0"),
   failed : Long("0"),
   pipeline : Long("0"),
   total : Long("1")
}
```

### Include `mirroredReads`

By default, the :serverstatus:`mirroredReads` information is not included in the output. To return :serverstatus:`mirroredReads` information, you must explicitly specify the inclusion:

```javascript
db.runCommand( { serverStatus: 1, mirroredReads: 1 } )
```

## Output

> **Note:** The output fields vary depending on the version of MongoDB,
underlying operating system platform, the storage engine, and the
kind of node, including :binary:`~bin.mongos`, :binary:`~bin.mongod` or
`replica set` member.
For the :dbcommand:`serverStatus` output specific to the version of
your MongoDB, refer to the appropriate version of the MongoDB Manual.

### asserts

```javascript
asserts: {
   regular: <num>,
   warning: <num>,
   msg: <num>,
   user: <num>,
   rollovers: <num>
},
```

### bucketCatalog

```javascript
bucketCatalog: {
   numBuckets: <num>,
   numOpenBuckets: <num>,
   numIdleBuckets: <num>,
   memoryUsage: <num>,
   numBucketInserts: <num>,
   numBucketUpdates: <num>,
   numBucketsOpenedDueToMetadata: <num>,
   numBucketsClosedDueToCount: <num>,
   numBucketsClosedDueToSchemaChange: <num>,
   numBucketsClosedDueToSize: <num>,
   numBucketsClosedDueToTimeForward: <num>,
   numBucketsClosedDueToTimeBackward: <num>,
   numBucketsClosedDueToMemoryThreshold: <num>,
   numCommits: <num>,
   numMeasurementsGroupCommitted: <num>,
   numWaits: <num>,
   numMeasurementsCommitted: <num>,
   avgNumMeasurementsPerCommit: <num>,
   numBucketsClosedDueToReopening: <num>,
   numBucketsArchivedDueToMemoryThreshold: <num>,
   numBucketsArchivedDueToTimeBackward: <num>,
   numBucketsReopened: <num>,
   numBucketsKeptOpenDueToLargeMeasurements: <num>,
   numBucketsClosedDueToCachePressure: <num>,
   numBucketsFrozen: <num>,
   numCompressedBucketsConvertedToUnsorted: <num>,
   numBucketsFetched: <num>,
   numBucketsQueried: <num>,
   numBucketFetchesFailed: <num>,
   numBucketQueriesFailed: <num>,
   numBucketReopeningsFailed: <num>,
   numDuplicateBucketsReopened: <num>,
   stateManagement: {
      bucketsManaged: <num>,
      currentEra: <num>,
      erasWithRemainingBuckets: <num>,
      trackedClearOperations: <num>
   }
}
```

.. versionadded:: 5.0

A document that reports metrics related to the `internal storage of time series collections <timeseries-bucket-catalog>`.

The `bucketCatalog` returns the following metrics:

You can also use the :pipeline:`$collStats` aggregation pipeline stage to find time series metrics. To learn more, see `storage-stats-time-series`.

### catalogStats

.. versionadded:: 5.1

```javascript
catalogStats: {
   collections: <num>,
   capped: <num>, 
   views: <num>, 
   timeseries: <num>,
   internalCollections: <num>, 
   internalViews: <num>,
   systemProfile: <num>
}
```

### changeStreamPreImages

.. versionadded:: 5.0

```javascript
changeStreamPreImages : {
   purgingJob : {
      totalPass : <num>,
      docsDeleted : <num>,
      bytesDeleted : <num>,
      scannedCollections : <num>,
      scannedInternalCollections : <num>,
      maxTimestampEligibleForTruncate : <timestamp>,
      maxStartWallTimeMillis : <num>,
      timeElapsedMillis : <num>,
   },
   expireAfterSeconds : <num>
}
```

A document that reports metrics related to `change stream pre-images <change-stream-pre-post-images>`.

### connections

```javascript
connections : {
   current : <num>,
   available : <num>,
   totalCreated : <num>,
   rejected : <num>,  // Added in MongoDB 6.3
   active : <num>,
   threaded : <num>,
   exhaustIsMaster : <num>,
   exhaustHello : <num>,
   awaitingTopologyChanges : <num>,
   loadBalanced : <num>,
   queuedForEstablishment : <num>, // Added in MongoDB 8.2 *(also available in 8.1.1, 8.0.12, and 7.0.23)*
   establishmentRateLimit : { // Added in MongoDB 8.2 *(also available in 8.1.1, 8.0.12, and 7.0.23)*
      rejected: <num>,
      exempted: <num>,
      interruptedDueToClientDisconnect: <num>
   }
}
```

### defaultRWConcern

The `defaultRWConcern` section provides information on the local copy of the global default read or write concern settings. The data may be stale or out of date. See :dbcommand:`getDefaultRWConcern` for more information.

```javascript
defaultRWConcern : {
  defaultReadConcern : {
    level : <string>
  },
  defaultWriteConcern : {
    w : <string> | <int>,
    wtimeout : <int>,
    j : <bool>
  },
  defaultWriteConcernSource: <string>,
  defaultReadConcernSource: <string>,
  updateOpTime : Timestamp,
  updateWallClockTime : Date,
  localUpdateWallClockTime : Date
}
```

### electionMetrics

The `electionMetrics` section provides information on elections called by this :binary:`~bin.mongod` instance in a bid to become the primary:

```javascript
electionMetrics : {
   stepUpCmd : {
      called : Long("<num>"),
      successful : Long("<num>")
   },
   priorityTakeover : {
      called : Long("<num>"),
      successful : Long("<num>")
   },
   catchUpTakeover : {
      called : Long("<num>"),
      successful : Long("<num>")
   },
   electionTimeout : {
      called : Long("<num>"),
      successful : Long("<num>")
   },
   freezeTimeout : {
      called : Long("<num>"),
      successful : Long("<num>")
   },
   numStepDownsCausedByHigherTerm : Long("<num>"),
   numCatchUps : Long("<num>"),
   numCatchUpsSucceeded : Long("<num>"),
   numCatchUpsAlreadyCaughtUp : Long("<num>"),
   numCatchUpsSkipped : Long("<num>"),
   numCatchUpsTimedOut : Long("<num>"),
   numCatchUpsFailedWithError : Long("<num>"),
   numCatchUpsFailedWithNewTerm : Long("<num>"),
   numCatchUpsFailedWithReplSetAbortPrimaryCatchUpCmd : Long("<num>"),
   averageCatchUpOps : <double>
}
```

### extra_info

```javascript
extra_info : {
   note : 'fields vary by platform',
   page_faults : <num>
},
```

### flowControl

```javascript
flowControl : {
   enabled : <boolean>,
   targetRateLimit : <int>,
   timeAcquiringMicros : Long("<num>"),
   locksPerKiloOp : <double>,  
   sustainerRate : <int>,
   isLagged : <boolean>,
   isLaggedCount : <int>,
   isLaggedTimeMicros : Long("<num>")
},
```

### globalLock

```javascript
globalLock : {
   totalTime : Long("<num>"),
   currentQueue : {
      total : <num>,
      readers : <num>,
      writers : <num>
   },
   activeClients : {
      total : <num>,
      readers : <num>,
      writers : <num>
   }
},
```

### ftdcCollectionMetrics

|both|

.. include:: /includes/serverStatus/ftdcCollectionMetrics.rst

### indexBuilds

```javascript
indexBuilds : {
   total : <num>,
   killedDueToInsufficientDiskSpace : <num>,
   failedDueToDataCorruption : <num>
},
```

### indexBulkBuilder

```json
indexBulkBuilder: {
   count: <long>, 
   resumed: <long>, 
   filesOpenedForExternalSort: <long>, 
   filesClosedForExternalSort: <long>, 
   spilledRanges: <long>, 
   bytesSpilledUncompressed: <long>,
   bytesSpilled: <long>,
   numSorted: <long>,
   bytesSorted: <long>,
   memUsage: <long>
}
```

### indexStats

```json
indexStats: {
   count: Long("<num>"), 
   features: {
      '2d': { count: Long("<num>"), accesses: Long("<num>") },
      '2dsphere': { count: Long("<num>"), accesses: Long("<num>") },
      '2dsphere_bucket': { count: Long("<num>"), accesses: Long("<num>") },
      collation: { count: Long("<num>"), accesses: Long("<num>") },
      compound: { count: Long("<num>"), accesses: Long("<num>") },
      hashed: { count: Long("<num>"), accesses: Long("<num>") },
      id: { count: Long("<num>"), accesses: Long("<num>") },
      normal: { count: Long("<num>"), accesses: Long("<num>") },
      partial: { count: Long("<num>"), accesses: Long("<num>") },
      prepareUnique: { count: Long("<num>"), accesses: Long("<num>") }, // Added in 8.1 (and 8.0.4, 7.0.14, and 6.0.20)
      single: { count: Long("<num>"), accesses: Long("<num>") },
      sparse: { count: Long("<num>"), accesses: Long("<num>") },
      text: { count: Long("<num>"), accesses: Long("<num>") },
      ttl: { count: Long("<num>"), accesses: Long("<num>") },
      unique: { count: Long("<num>"), accesses: Long("<num>") },
      wildcard: { count: Long("<num>"), accesses: Long("<num>") }
   }
}
```

### Instance Information

```javascript
host : <string>,
advisoryHostFQDNs : <array>,
version : <string>,
process : <'mongod'|'mongos'>,
pid : Long("<num>"),
uptime : <num>,
uptimeMillis : Long("<num>"),
uptimeEstimate : Long("<num>"),
localTime : ISODate("<Date>"),
```

### locks

```javascript
locks : {
   <type> : {
         acquireCount : {
            <mode> : Long("<num>"),
            ...
         },
         acquireWaitCount : {
            <mode> : Long("<num>"),
            ...
         },
         timeAcquiringMicros : {
            <mode> : Long("<num>"),
            ...
         },
         deadlockCount : {
            <mode> : Long("<num>"),
            ...
         }
   },
   ...
```

### lockContentionMetrics

```javascript
lockContentionMetrics: {
   "<tag>": {
      exclusive: {
         total:       Long("<num>"),
         contentions: Long("<num>"),
         waitCycles:  Long("<num>")
      },
      shared: {
         total:       Long("<num>"),
         contentions: Long("<num>"),
         waitCycles:  Long("<num>")
      },
      // Only present if you specify { lockContentionMetrics: { listAll: 1 } }:
      mutexes: [
         {
            id:         Long("<num>"),
            registered: ISODate("<Date>"),
            exclusive: { total, contentions, waitCycles },
            shared:    { total, contentions, waitCycles }
         },
         ...
      ]
   },
   ...
}
```

### logicalSessionRecordCache

```javascript
logicalSessionRecordCache : {
   activeSessionsCount : <num>,
   sessionsCollectionJobCount : <num>,
   lastSessionsCollectionJobDurationMillis : <num>,
   lastSessionsCollectionJobTimestamp : <Date>,
   lastSessionsCollectionJobEntriesRefreshed : <num>,
   lastSessionsCollectionJobEntriesEnded : <num>,
   lastSessionsCollectionJobCursorsClosed : <num>,
   transactionReaperJobCount : <num>,
   lastTransactionReaperJobDurationMillis : <num>,
   lastTransactionReaperJobTimestamp : <Date>,
   lastTransactionReaperJobEntriesCleanedUp : <num>,
   sessionCatalogSize : <num>  
},
```

### mem

```javascript
mem : {
   bits : <int>,
   resident : <int>,
   virtual : <int>,
   supported : <boolean>
},
```

### metrics

```javascript
metrics : {
   abortExpiredTransactions: {
      passes: <integer>,
      successfulKills: <integer>,
      timedOutKills: <integer>
   },
   apiVersions: {
      <appName1>: <string>, 
      <appName2>: <string>, 
      <appName3>: <string>
   },
   aggStageCounters : {
      <aggregation stage> : Long("<num>")
   },
   changeStreams: {
      largeEventsFailed: Long("<num>"),
      largeEventsSplit: Long("<num>"),
      showExpandedEvents: Long("<num>")
   },
   commands: {
      <command>: {
         failed: Long("<num>"),
         validator: { 
           total: Long("<num>"), 
           failed: Long("<num>"), 
           jsonSchema: Long("<num>")
         }, 
         total: Long("<num>"),
         rejected: Long("<num>")    
      }
   },
   cursor : {
      moreThanOneBatch : Long("<num>"),
      timedOut : Long("<num>"),
      totalOpened : Long("<num>"),
      lifespan : {
         greaterThanOrEqual10Minutes : Long("<num>"),
         lessThan10Minutes : Long("<num>"),
         lessThan15Seconds : Long("<num>"),
         lessThan1Minute : Long("<num>"),
         lessThan1Second : Long("<num>"),
         lessThan30Seconds : Long("<num>"),
         lessThan5Seconds : Long("<num>")
      },
      open : {
         noTimeout : Long("<num>"),
         pinned : Long("<num>"),
         multiTarget : Long("<num>"),
         singleTarget : Long("<num>"),
         total : Long("<num>")
      }
   },
   document : {
      deleted : Long("<num>"),
      inserted : Long("<num>"),
      returned : Long("<num>"),
      updated : Long("<num>")
   },
   dotsAndDollarsFields : {
         inserts : Long("<num>"),
         updates : Long("<num>")
   },
   extension: {
      totalAggStageExecMicros: NumberLong(0),
      apiCallSuccesses: NumberLong(0),
      apiCallFailures: NumberLong(0),
      vectorSearch: {
         legacyVectorSearchUsed: NumberLong(0),
         extensionVectorSearchUsed: NumberLong(0),
         onViewKickbackRetries: NumberLong(0),
         inSubpipelineKickbackRetries: NumberLong(0),
      }
   }
   getLastError : {
      wtime : {
         num : <num>,
         totalMillis : <num>
      },
      wtimeouts : Long("<num>"),
      default : {
         unsatisfiable : Long("<num>"),
         wtimeouts : Long("<num>")
      }
   },
   mongos : {
      cursor : {
         moreThanOneBatch : Long("<num>"),
         totalOpened : Long("<num>")
      }
   },
   network : {  // Added in MongoDB 6.3
      totalEgressConnectionEstablishmentTimeMillis : Long("<num>"),
      totalIngressTLSConnections : Long("<num>"),
      totalIngressTLSHandshakeTimeMillis : Long("<num>"),
      totalTimeForEgressConnectionAcquiredToWireMicros : Long("<num>"),
      totalTimeToFirstNonAuthCommandMillis : Long("<num>")
      "averageTimeToCompletedTLSHandshakeMicros": Long("<num>"), // Added in MongoDB 8.2
      "averageTimeToCompletedHelloMicros": Long("<num>"), // Added in MongoDB 8.2
      "averageTimeToCompletedAuthMicros": Long("<num>") // Added in MongoDB 8.2
   },
   operation : {
      killedDueToClientDisconnect : Long("<num>"),  // Added in MongoDB 7.1
      killedDueToDefaultMaxTimeMSExpired : Long("<num>"),
      killedDueToMaxTimeMSExpired : Long("<num>"),  // Added in MongoDB 7.2
      killedDueToRangeDeletion: Long("<num>"), // Added in MongoDB 8.2 
      numConnectionNetworkTimeouts : Long("<num>"),  // Added in MongoDB 6.3
      scanAndOrder : Long("<num>"),
      totalTimeWaitingBeforeConnectionTimeoutMillis : Long("<num>"),  // Added in MongoDB 6.3
      unsendableCompletedResponses : Long("<num>"),  // Added in MongoDB 7.1
      writeConflicts : Long("<num>")
   },
   operatorCounters : {
      expressions : {
         <command> : Long("<num>")
      },
      match : {
         <command> : Long("<num>")
      }
   },
   query: {
      allowDiskUseFalse: Long("<num>"),
      cbr: {
         choseWinningPlan: Long("<num>"),
         count: Long("<num>"),
         histograms: {
            micros: [
               {
                  lowerBound: Long("<num>"),
                  count: Long("<num>"),
               }
            ]
            numPlans: [
               {
                  lowerBound: Long("<num>"),
                  count: Long("<num>"),
               }
            ]
            samplingMicros: [
               {
                  lowerBound: Long("<num>"),
                  count: Long("<num>"),
               }
            ]
         },
         micros: Long("<num>"),
         numPlans: Long("<num>"),
         numPlansFailedCostEstimation: Long("<num>"),
         numPlansTiedCostEstimation: Long("<num>"),
         samplingMicros: Long("<num>"),
      },
      updateOneOpStyleBroadcastWithExactIDCount: Long("<num>"),
      bucketAuto: {
         spilledBytes: Long("<num>"),
         spilledDataStorageSize: Long("<num>"),
         spilledRecords: Long("<num>"),
         spills: Long("<num>")
      },
      lookup: {
         hashLookup: Long("<num>"),
         hashLookupSpillToDisk: Long("<num>"),
         indexedLoopJoin: Long("<num>"),
         nestedLoopJoin: Long("<num>")
      },
      multiPlanner: {
         classicCount: Long("<num>"),
         classicMicros: Long("<num>"),
         classicWorks: Long("<num>"),
         sbeCount: Long("<num>"),
         sbeMicros: Long("<num>"),
         sbeNumReads: Long("<num>"),
         histograms: {
            classicMicros: [
               { lowerBound: Long("0"), count: Long("<num>") },
               { < Additional histogram groups not shown. > },
               { lowerBound: Long("1073741824"), count: Long("<num>")> }>
            ],
            classicNumPlans: [
               { lowerBound: Long("0"), count: Long("<num>") },
               { < Additional histogram groups not shown. > },
               { lowerBound: Long("32"), count: Long("<num>") }
            ],
            classicWorks: [
               { lowerBound: Long("0"), count: Long("<num>") },
               { < Additional histogram groups not shown. > },
               { lowerBound: Long("32768"), count: Long("<num>") }
            ],
            sbeMicros: [
               { lowerBound: Long("0"), count: Long("<num>") },
               { < Additional histogram groups not shown. > },
               { lowerBound: Long("1073741824"), count: Long("<num>") }
            ],
            sbeNumPlans: [
               { lowerBound: Long("0"), count: Long("<num>") },
               { < Additional histogram groups not shown. > },
               { lowerBound: Long("32"), count: Long("<num>") }
            ],
            sbeNumReads: [
               { lowerBound: Long("0"), count: Long("<num>") },
               { < Additional histogram groups not shown. > },
               { lowerBound: Long("32768"), count: Long("<num>") }
            ]
         }
      },
      planCache: {
         classic: { hits: Long("<num>"), misses: Long("<num>"), replanned: Long("<num>") },
         sbe: { hits: Long("<num>"), misses: Long("<num>"), replanned: Long("<num>") }
      },
      queryFramework: {
         aggregate: {
            classicHybrid: Long("<num>"),
            classicOnly: Long("<num>"),
            cqf: Long("<num>"),
            sbeHybrid: Long("<num>"),
            sbeOnly: Long("<num>")
         },
         find: { classic: Long("<num>"), cqf: Long("<num>"), sbe: Long("<num>") }
      }
   },
   queryExecutor: {
      scanned : Long("<num>"),
      scannedObjects : Long("<num>"),
      collectionScans : {
         nonTailable : Long("<num>"),
         total : Long("<num>")
      },
      profiler : {
         collectionScans : {
            nonTailable : Long("<num>"),
            tailable : Long("<num>"),
            total : Long("<num>")
         }
      }
   },
   record : {
      moves : Long("<num>")
   },
   repl : {
      executor : {
         pool : {
            inProgressCount : <num>
         },
         queues : {
            networkInProgress : <num>,
            sleepers : <num>
         },
         unsignaledEvents : <num>,
         shuttingDown : <boolean>,
         networkInterface : <string>
      },
      apply : {
         attemptsToBecomeSecondary : Long("<num>"),
         batchSize: <num>,
         batches : {
            num : <num>,
            totalMillis : <num>
         },
         ops : Long("<num>")
      },
      write : {
         batchSize: <num>,
         batches : {
            num : <num>,
            totalMillis : <num>
         }
      },
      buffer : {
         write: {
            count : Long("<num>"),
            maxSizeBytes : Long("<num>"),
            sizeBytes : Long("<num>")
         },
         apply: {
            count : Long("<num>"),
            sizeBytes : Long("<num>"),
            maxSizeBytes : Long("<num>"),
            maxCount: Long("<num>")
         },
      },
      initialSync : {
         completed : Long("<num>"),
         failedAttempts : Long("<num>"),
         failures : Long("<num>")
      },
      network : {
         bytes : Long("<num>"),
         getmores : {
            num : <num>,
            totalMillis : <num>
         },
         notPrimaryLegacyUnacknowledgedWrites : Long("<num>"),
         notPrimaryUnacknowledgedWrites : Long("<num>"),
         oplogGetMoresProcessed : {
            num : <num>,
            totalMillis : <num>
         },
         ops : Long("<num>"),
         readersCreated : Long("<num>"),
         replSetUpdatePosition : {
            num : Long("<num>")
         }
      },
      reconfig : {
         numAutoReconfigsForRemovalOfNewlyAddedFields : Long("<num>")
      },
      stateTransition : {
         lastStateTransition : <string>,
         totalOperationsKilled : Long("<num>"),
         totalOperationsRunning : Long("<num>")
      },
      syncSource : {
         numSelections : Long("<num>"),
         numTimesChoseSame : Long("<num>"),
         numTimesChoseDifferent : Long("<num>"),
         numTimesCouldNotFind : Long("<num>")
      },
      waiters : {
         opTime : Long("<num>"),
         replication : Long("<num>"),
         replCoordMutexTotalWaitTimeInOplogServerStatusMillis: Long("<num>")
      }
   },
   storage : {
      freelist : {
         search : {
            bucketExhausted : <num>,
            requests : <num>,
            scanned : <num>
         }
      }
   },
   ttl : {
      deletedDocuments : Long("<num>"),
      passes : Long("<num>"),
      subPasses : Long("<num>")
   }
}
```

### mirroredReads

|mongod-only|

```javascript
"mirroredReads" : {
      "seen" : <num>,
      "sent" : <num>
},
```

### network

```javascript
network : {
   egress : {
      bytesIn : Long("<num>"),
      bytesOut : Long("<num>"),
      physicalBytesIn : Long("<num>"),
      physicalBytesOut : Long("<num>"),
      numRequests : Long("<num>"),
   },
   ingressRequestRateLimiter : { 
      "rejectedAdmissions": Long,
      "successfulAdmissions": Long,
      "exemptedAdmissions": Long,
      "attemptedAdmissions": Long,
      "totalAvailableTokens": Long
   }, // Added in MongoDB 8.0.20
   bytesIn : Long("<num>"),
   bytesOut : Long("<num>"),
   physicalBytesIn : Long("<num>"),
   physicalBytesOut : Long("<num>"),
   numSlowDNSOperations : Long("<num>"),
   numSlowSSLOperations : Long("<num>"),
   numRequests : Long("<num>"),
   tcpFastOpen : {
      kernelSetting : Long("<num>"),
      serverSupported : <bool>,
      clientSupported : <bool>,
      accepted : Long("<num>")
   },
   compression : {
      snappy : {
         compressor : { bytesIn : Long("<num>"), bytesOut : Long("<num>") },
         decompressor : { bytesIn : Long("<num>"), bytesOut : Long("<num>") }
      }, 
      zstd : { 
         compressor : { bytesIn : Long("<num>"), bytesOut : Long("<num>") },
         decompressor : { bytesIn : Long("<num>"), bytesOut : Long("<num>") }
      },
      zlib : {
         compressor : { bytesIn : Long("<num>"), bytesOut : Long("<num>") },
         decompressor : { bytesIn : Long("<num>"), bytesOut : Long("<num>") }
      }
   },
   serviceExecutors : {
      passthrough : {
         threadsRunning : <num>,
         clientsInTotal : <num>,
         clientsRunning : <num>,
         clientsWaitingForData : <num>
      },
      fixed : {
         threadsRunning : <num>,
         clientsInTotal : <num>,
         clientsRunning : <num>,
         clientsWaitingForData : <num>
      }
   },
   listenerProcessingTime : { durationMicros : <num> }  // Added in MongoDB 6.3
}
```

### opLatencies

```javascript
opLatencies : {
   reads : <document>,
   writes : <document>,
   commands : <document>,
   transactions : <document>
},
```

### opWorkingTime

```javascript
opWorkingTime : {
   commands : <document>,
   reads : <document>,
   writes : <document>,
   transactions : <document>
}
```

### opReadConcernCounters

> **Warning:** Starting in version 5.0, :serverstatus:`opReadConcernCounters` is
replaced by :serverstatus:`readConcernCounters`.

Only for mongod instances

```javascript
opReadConcernCounters : {
   available : Long("<num>"),
   linearizable : Long("<num>"),
   local : Long("<num>"),
   majority : Long("<num>"),
   snapshot : Long("<num>"),
   none : Long("<num>")
}
```

### opWriteConcernCounters

Only for mongod instances

```javascript
opWriteConcernCounters : {
   insert : {
      wmajority : Long("<num>"),
      wnum : {
         <num> :  Long("<num>"),
         ...
      },
      wtag : {
         <tag1> :  Long("<num>"),
         ...
      },
      none : Long("<num>"),
      noneInfo : {
         CWWC : {
            wmajority : Long("<num>"),
            wnum : {
               <num> :  Long("<num>"),
               ...
            },
            wtag : {
               <tag1> :  Long("<num>"),
               ...
            }
         },
         implicitDefault : {
            wmajority : Long("<num>")
            wnum : {
               <num> :  Long("<num>"),
               ...
            }
         }
      }
   },
   update : {
      wmajority : Long("<num>"),
      wnum : {
         <num> :  Long("<num>"),
         ...
      },
      wtag : {
         <tag1> :  Long("<num>"),
         ...
      },
      none : Long("<num>"),
      noneInfo : {
         CWWC : {
            wmajority : Long("<num>"),
            wnum : {
               <num> :  Long("<num>"),
               ...
            }
            wtag : {
               <tag1> :  Long("<num>"),
               ...
            }
         },
         implicitDefault : {
            wmajority : Long("<num>")
            wnum : {
               <num> :  Long("<num>"),
               ...
            }
         }
      }
   },
   delete : {
      wmajority :  Long("<num>")
      wnum : {
         <num> :  Long("<num>"),
         ...
      },
      wtag : {
         <tag1> :  Long("<num>"),
         ...
      },
      none : Long("<num>"),
      noneInfo : {
         CWWC : {
            wmajority : Long("<num>"),
            wnum : {
               <num> :  Long("<num>"),
               ...
            },
            wtag : {
               <tag1> :  Long("<num>"),
               ...
            }
         },
         implicitDefault : {
            wmajority : Long("<num>")
            wnum : {
               <num> :  Long("<num>"),
               ...
            }
         }
      }
   }
}
```

### opcounters

```javascript
opcounters : {
   insert : Long("<num>"), 
   query : Long("<num>"),  
   update : Long("<num>"),  
   delete : Long("<num>"),  
   getmore : Long("<num>"), 
   command : Long("<num>"), 
},
```

### opcountersRepl

.. include:: /includes/extracts/4.2-changes-opcountersRepl-type.rst

```javascript
opcountersRepl : {
   insert : Long("<num>"),  
   query : Long("<num>"),   
   update : Long("<num>"), 
   delete : Long("<num>"), 
   getmore : Long("<num>"), 
   command : Long("<num>"), 
},
```

### oplogTruncation

```javascript
oplogTruncation : {
   totalTimeProcessingMicros : Long("<num>"),
   processingMethod : <string>,
   oplogMinRetentionHours : <double>
   totalTimeTruncatingMicros : Long("<num>"),
   truncateCount : Long("<num>")
},
```

### planCache

.. versionadded:: 7.0

```javascript
planCache : {
   totalQueryShapes : Long("<num>"),
   totalSizeEstimateBytes : Long("<num>"),
   classic : { 
      hits : Long("<num>"), 
      misses : Long("<num>"),
      replanned : Long("<num>"),
      replanned_plan_is_cached_plan : Long("<num>"),
      skipped : Long("<num>") 
   },
   sbe : { 
      hits : Long("<num>"), 
      misses: Long("<num>"),
      replanned : Long("<num>"),
      replanned_plan_is_cached_plan : Long("<num>"),
      skipped : Long("<num>")  
   }
}
```

### profiler

```javascript
profiler: {
   totalWrites: <integer>,
   activeWriters: <integer>
}
```

### queryStats

.. versionadded:: 7.1

```javascript
queryStats: {
   numEvicted: Long("<num>"),
   numRateLimitedRequests: Long("<num>"),
   queryStatsStoreSizeEstimateBytes: Long("<num>"),
   numQueryStatsStoreWriteErrors: Long("<num>"),
   numHmacApplicationErrors: Long("<num>")
},
```

### queryAnalyzers

.. versionadded:: 7.0

```javascript
queryAnalyzers: {                                                    
  activeCollections: <integer>,
  totalCollections: <integer>,
  totalSampledReadsCount: <integer>,
  totalSampledWritesCount: <integer>,
  totalSampledReadsBytes: <integer>,
  totalSampledWritesBytes: <integer>
}
```

### queues

As an operation proceeds through its stages, it may enter a queue if the number of concurrent operations at the current stage exceeds a maximum threshold. This prevents excessive resource contention and provides observability into the state of the database.

.. versionadded:: 8.0

```json
queues: {
   execution: {
      admissions: <object>,
      backgroundTasksDeprioritization: <boolean>,
      deprioritizationGate: <boolean>,
      heuristicDeprioritization: <boolean>,
      heuristicDeprioritizationThreshold: Int("<num>"),
      totalDeprioritizations: Long("<num>"),
      usesPrioritization: <boolean>,
      usesThroughputProbing: <boolean>,
      write: <object>,
      read: <object>,
      monitor: {
         timesDecreased: Long("<num>"),
         timesIncreased: Long("<num>"),
         totalAmountDecreased: Long("<num>"),
         totalAmountIncreased: Long("<num>"),
         resizeDurationMicros: Long("<num>"),
         timesProbedStable: Long("<num>"),
         timesProbedUp: Long("<num>"),
         timesProbedDown: Long("<num>")
      },
      nonDeprioritizable: <object>,
      deprioritizable: <object>,
   },
   ingress: {
      out: Long("<num>"),
      available: Long("<num>"),
      totalTickets: Long("<num>"),
      exempt: {
         addedToQueue: Long("<num>"),
         removedFromQueue: Long("<num>"),
         queueLength: Long("<num>"),
         startedProcessing: Long("<num>"),
         processing: Long("<num>"),
         finishedProcessing: Long("<num>"),
         totalTimeProcessingMicros: Long("<num>"),
         canceled: Long("<num>"),
         newAdmissions: Long("<num>"),
         totalTimeQueuedMicros: Long("<num>")
      },
      normalPriority: {
         addedToQueue: Long("<num>"),
         removedFromQueue: Long("<num>"),
         queueLength: Long("<num>"),
         startedProcessing: Long("<num>"),
         processing: Long("<num>"),
         finishedProcessing: Long("<num>"),
         totalTimeProcessingMicros: Long("<num>"),
         canceled: Long("<num>"),
         newAdmissions: Long("<num>"),
         totalTimeQueuedMicros: Long("<num>")
      }
   },
   ingressSessionEstablishment: { // Added in MongoDB 8.2
      "addedToQueue": Long("<num>"),
      "removedFromQueue": Long("<num>"),
      "interruptedInQueue": Long("<num>")
      "rejectedAdmissions": Long("<num>"),
      "exemptedAdmissions": Long("<num>"),
      "successfulAdmissions": Long("<num>"),
      "attemptedAdmissions": Long("<num>"),
      "averageTimeQueuedMicros": Long("<num>"),
      "totalAvailableTokens": Long("<num>")
   }
}
```

### Queue Information

```json
out: Int("<num>"),
available: Int("<num>"),
totalTickets: Int("<num>"),
nonDeprioritizable: <object>,
deprioritizable: <object>,
exempt: {
   addedToQueue: Long("<num>"),
   removedFromQueue: Long("<num>"),
   queueLength: Long("<num>"),
   startedProcessing: Long("<num>"),
   processing: Long("<num>"),
   finishedProcessing: Long("<num>"),
   totalTimeProcessingMicros: Long("<num>"),
   canceled: Long("<num>"),
   totalTimeQueuedMicros: Long("<num>")
},
normalPriority: {
   out: Int("<num>"),
   available: Int("<num>"),
   totalTickets: Int("<num>"),
   addedToQueue: Long("<num>"),
   removedFromQueue: Long("<num>"),
   queueLength: Long("<num>"),
   startedProcessing: Long("<num>"),
   processing: Long("<num>"),
   finishedProcessing: Long("<num>"),
   totalTimeProcessingMicros: Long("<num>"),
   canceled: Long("<num>"),
   newAdmissions: Long("<num>"),
   totalTimeQueuedMicros: Long("<num>"),
   totalDelinquentAcquisitions: Long("<num>"),
   totalAcquisitionDelinquencyMillis: Long("<num>"),
   maxAcquisitionDelinquencyMillis: Long("<num>")
},
lowPriority: {
   out: Int("<num>"),
   available: Int("<num>"),
   totalTickets: Int("<num>"),
   addedToQueue: Long("<num>"),
   removedFromQueue: Long("<num>"),
   queueLength: Long("<num>"),
   startedProcessing: Long("<num>"),
   processing: Long("<num>"),
   finishedProcessing: Long("<num>"),
   totalTimeProcessingMicros: Long("<num>"),
   canceled: Long("<num>"),
   newAdmissions: Long("<num>"),
   totalTimeQueuedMicros: Long("<num>"),
   totalDelinquentAcquisitions: Long("<num>"),
   totalAcquisitionDelinquencyMillis: Long("<num>"),
   maxAcquisitionDelinquencyMillis: Long("<num>")
}
```

### Queue Operation Execution Statistics

.. versionadded:: 8.3

```json
totalElapsedTimeMicros: Long("<num>"),
totalCPUUsageMicros: Long("<num>"),
totalTimeProcessingMicros: Long("<num>"),
totalTimeQueuedMicros: Long("<num>"),
totalAdmissions: Long("<num>"),
totalOpsFinished: Long("<num>"),
totalOpsLoadShed: Long("<num>"),
totalAdmissionsLoadShed: Long("<num>"),
totalCPUUsageLoadShed: Long("<num>"),
totalElapsedTimeMicrosLoadShed: Long("<num>"),
totalQueuedTimeMicrosLoadShed: Long("<num>"),
totalDelinquentAcquisitions: Long("<num>"),
totalAcquisitionDelinquencyMillis: Long("<num>"),
maxAcquisitionDelinquencyMillis: Long("<num>")
```

The total time in microseconds for all operations in this bucket.

The total CPU time in microseconds consumed by operations in the corresponding group (short-running or long-running operations).

The total time in microseconds spent holding tickets across all acquisitions.

The total time in microseconds spent waiting for tickets across all acquisitions.

The total number of ticket acquisitions, including re-acquisitions after yields.

The number of operations that completed in this group.

The number of unique operations that are load-shed due to queue overflow.

The total number of admissions for load-shed operations.

The CPU time in microseconds consumed by operations before being shed.

The elapsed time in microseconds for operations before being shed.

The queue time in microseconds for operations before being shed.

The number of ticket holds that exceeded the delinquency threshold.

The cumulative excess time in milliseconds beyond the threshold for all delinquent holds.

The maximum excess time in milliseconds observed for any single delinquent hold.

### querySettings

.. versionadded:: 8.0

```javascript
querySettings: {
  count: <num>,
  rejectCount: <num>,
  size: <num>
}
```

### readConcernCounters

.. versionadded:: 5.0

```javascript
readConcernCounters : {
   nonTransactionOps : {
      none : Long("<num>"),
      noneInfo : {
         CWRC : {
            local : Long("<num>"),
            available : Long("<num>"),
            majority : Long("<num>")
         },
         implicitDefault : {
            local : Long("<num>"),
            available : Long("<num>")
         }
      },
      local : Long("<num>"),
      available : Long("<num>"),
      majority : Long("<num>"),
      snapshot : {
         withClusterTime : Long("<num>"),
         withoutClusterTime : Long("<num>")
      },
      linearizable : Long("<num>")
   },
   transactionOps : {
      none : Long("<num>"),
      noneInfo : {
         CWRC : {
            local : Long("<num>"),
            available : Long("<num>"),
            majority : Long("<num>")
         },
         implicitDefault : {
            local : Long("<num>"),
            available : Long("<num>")
         }
      },
      local : Long("<num>"),
      majority : Long("<num>"),
      snapshot : {
         withClusterTime : Long("<num>"),
         withoutClusterTime : Long("<num>")
      }
   }
},
```

### readPreferenceCounters

Available starting in MongoDB 7.2 (and 7.0.3, 6.0.11).

|mongod-only|

```javascript
readPreferenceCounters : {
   executedOnPrimary : { 
      primary : {
         internal : Long("<num>"),
         external : Long("<num>") 
      }, 
      primaryPreferred : {
         internal : Long("<num>"),
         external : Long("<num>") 
      }, 
      secondary : {
         internal : Long("<num>"),
         external : Long("<num>") 
      },
      secondaryPreferred : {
         internal : Long("<num>"),
         external : Long("<num>") 
      },
      nearest : {
         internal : Long("<num>"),
         external : Long("<num>") 
      },
      tagged : {
         internal : Long("<num>"),
         external : Long("<num>") 
      }
   },
   executedOnSecondary : { 
      primary : {
         internal : Long("<num>"),
         external : Long("<num>") 
      }, 
      primaryPreferred : {
         internal : Long("<num>"),
         external : Long("<num>") 
      }, 
      secondary : {
         internal : Long("<num>"),
         external : Long("<num>") 
      },
      secondaryPreferred : {
         internal : Long("<num>"),
         external : Long("<num>") 
      },
      nearest : {
         internal : Long("<num>"),
         external : Long("<num>") 
      },
      tagged : {
         internal : Long("<num>"),
         external : Long("<num>") 
      }
   }
}
```

### repl

```javascript
repl : {
   hosts : [
         <string>,
         <string>,
         <string>
   ],
   setName : <string>,
   setVersion : <num>,
   isWritablePrimary : <boolean>,
   secondary : <boolean>,
   primary : <hostname>,
   me : <hostname>,
   electionId : ObjectId(""),
   userWriteBlockReason : <num>,
   userWriteBlockModeCounters: {
      Unspecified: <num>,
      ClusterToClusterMigrationInProgress: <num>,
      DiskUseThresholdExceeded: <num>
   },
   primaryOnlyServices: {
      ReshardingRecipientService: { state: <string>, numInstances: <num> },
      RenameCollectionParticipantService: { state: <string>, numInstances: <num> },
      ShardingDDLCoordinator: { state: <string>, numInstances: <num> },
      ReshardingDonorService: { state: <string>, numInstances: <num> }
   },
   rbid : <num>,
   replicationProgress : [
         {
            rid : <ObjectId>,
            optime : { ts: <timestamp>, term: <num> },
            host : <hostname>,
            memberId : <num>
         },
        ...
   ]
   timestamps : {
      oldestTimestamp: <timestamp>
   }
}
```

### security

```javascript
security : {
   authentication : {
      saslSupportedMechsReceived : <num>,
      mechanisms : {
         MONGODB-X509 : {
            speculativeAuthenticate : {
               received : Long("<num>"),
               successful : Long("<num>")
            },
            authenticate : {
               received : Long("<num>"),
               successful : Long("<num>")
            }
         },
         SCRAM-SHA-1 : {
            speculativeAuthenticate : {
               received : Long("<num>"),
               successful : Long("<num>")
            },
            authenticate : {
               received : Long("<num>"),
               successful : Long("<num>")
            }
         },
         SCRAM-SHA-256 : {
            speculativeAuthenticate : {
               received : Long("<num>"),
               successful : Long("<num>")
            },
            authenticate : {
               received : Long("<num>"),
               successful : Long("<num>")
            }
          }
       }
     },
     SSLServerSubjectName: <string>,
     SSLServerHasCertificateAuthority: <boolean>,
     SSLServerCertificateExpirationDate: <date>
},
```

### sharding

```javascript
{
   configsvrConnectionString : 'csRS/cfg1.example.net:27019,cfg2.example.net:27019,cfg2.example.net:27019',
   lastSeenConfigServerOpTime : {
      ts : <timestamp>,
      t : Long("<num>")
   },
   maxChunkSizeInBytes : Long("<num>")
}
```

### shardingStatistics

### shardedIndexConsistency

```javascript
shardedIndexConsistency : {
   numShardedCollectionsWithInconsistentIndexes : Long("<num>")
},
```

### spillWiredTiger

```javascript
spillWiredTiger: {
  storageSize: <long>,
  uri: <string>,
  version: <string>,
  'block-manager': {
    'blocks read': <num>,
    'blocks written': <num>,
    'bytes read': <num>,
    'bytes written': <num>
  },
  cache: {
    'application thread time evicting (usecs)': <num>,
    'application threads eviction requested with cache fill ratio < 25%': <num>,
    'application threads eviction requested with cache fill ratio >= 75%': <num>,
    'application threads page write from cache to disk count': <num>,
    'application threads page write from cache to disk time (usecs)': <num>,
    'bytes allocated for updates': <num>,
    'bytes currently in the cache': <num>,
    'bytes read into cache': <num>,
    'bytes written from cache': <num>,
    'eviction currently operating in aggressive mode': <num>,
    'eviction empty score': <num>,
    'eviction state': <num>,
    'eviction walk target strategy clean pages': <num>,
    'eviction walk target strategy dirty pages': <num>,
    'eviction walk target strategy pages with updates': <num>,
    'forced eviction - pages evicted that were clean count': <num>,
    'forced eviction - pages evicted that were dirty count': <num>,
    'forced eviction - pages selected count': <num>,
    'forced eviction - pages selected unable to be evicted count': <num>,
    'hazard pointer blocked page eviction': <num>,
    'maximum bytes configured': <num>,
    'maximum page size seen at eviction': <num>,
    'number of times dirty trigger was reached': <num>,
    'number of times eviction trigger was reached': <num>,
    'number of times updates trigger was reached': <num>,
    'page evict attempts by application threads': <num>,
    'page evict failures by application threads': <num>,
    'pages queued for eviction': <num>,
    'pages queued for urgent eviction': <num>,
    'tracked dirty bytes in the cache': <num>
  }
}
```

### storageEngine

```javascript
storageEngine : {
   name : <string>,
   supportsCommittedReads : <boolean>,
   persistent : <boolean>
},
```

### tcmalloc

> **Note:** `tcmalloc` metrics that are only for internal use are omitted from this
page.

```javascript
tcmalloc : {
   usingPerCPUCaches : <boolean>,  // Added in MongoDB 8.0
   maxPerCPUCacheSizeBytes : <integer>, // Added in MongoDB 8.0
   generic : {
      current_allocated_bytes : <integer>, 
      heap_size : <integer>,
      peak_memory_usage : <integer>  // Added in MongoDB 8.0
   },
   tcmalloc : {
      central_cache_free : <integer>, 
      cpu_free : <integer>,  // Added in MongoDB 8.0
      release_rate : <integer>, 
      total_bytes_held : <integer>,  // Added in MongoDB 8.0
      cpuCache : { 
         0 : {
            overflows : <integer>,  // Added in MongoDB 8.0
            underflows : <integer>  // Added in MongoDB 8.0
         },
      }
   },
   tcmalloc_derived : {
      total_free_bytes : <integer>  // Added in MongoDB 8.0
   }
}
```

### transactions

MongoDB creates as many oplog entries as necessary to encapsulate all write operations in a transaction. See `txn-oplog-size-limit` for details.

### transportSecurity

```javascript
transportSecurity : {
   1.0 : Long("<num>"),
   1.1 : Long("<num>"),
   1.2 : Long("<num>"),
   1.3 : Long("<num>"),
   unknown : Long("<num>")
},
```

### watchdog

```javascript
watchdog : {
   checkGeneration : Long("<num>"),
   monitorGeneration : Long("<num>"),
   monitorPeriod : <num>
}
```

> **Note:** The `watchdog` section is only present if the :ref:`Storage Node Watchdog
<storage-node-watchdog>` is enabled.

### wiredTiger

`wiredTiger` information only appears if using the `WiredTiger <storage-wiredtiger>` storage engine. Some of the statistics roll up for the server.

```javascript
{
   uri : 'statistics:',
   version: <string>,
   async : {
      current work queue length : <num>,
      maximum work queue length : <num>,
      number of allocation state races : <num>,
      number of flush calls : <num>,
      number of operation slots viewed for allocation : <num>,
      number of times operation allocation failed : <num>,
      number of times worker found no work : <num>,
      total allocations : <num>,
      total compact calls : <num>,
      total insert calls : <num>,
      total remove calls : <num>,
      total search calls : <num>,
      total update calls : <num>
   },
   block-manager : {
      blocks pre-loaded : <num>,
      blocks read : <num>,
      blocks written : <num>,
      bytes read : <num>,
      bytes written : <num>,
      bytes written for checkpoint : <num>,
      mapped blocks read : <num>,
      mapped bytes read : <num>
   },
   cache : {
      application threads page read from disk to cache count : <num>,
      application threads page read from disk to cache time (usecs) : <num>,
      application threads page write from cache to disk count : <num>,
      application threads page write from cache to disk time (usecs) : <num>,
      bytes belonging to page images in the cache : <num>,
      bytes belonging to the cache overflow table in the cache : <num>,
      bytes currently in the cache : <num>,
      bytes dirty in the cache cumulative : <num>,
      bytes not belonging to page images in the cache : <num>,
      bytes read into cache : <num>,
      bytes written from cache : <num>,
      cache overflow cursor application thread wait time (usecs) : <num>,
      cache overflow cursor internal thread wait time (usecs) : <num>,
      cache overflow score : <num>,
      cache overflow table entries : <num>,
      cache overflow table insert calls : <num>,
      cache overflow table max on-disk size : <num>,
      cache overflow table on-disk size : <num>,
      cache overflow table remove calls : <num>,
      checkpoint blocked page eviction : <num>,
      eviction calls to get a page : <num>,
      eviction calls to get a page found queue empty : <num>,
      eviction calls to get a page found queue empty after locking : <num>,
      eviction currently operating in aggressive mode : <num>,
      eviction empty score : <num>,
      eviction passes of a file : <num>,
      eviction server candidate queue empty when topping up : <num>,
      eviction server candidate queue not empty when topping up : <num>,
      eviction server evicting pages : <num>,
      eviction server slept, because we did not make progress with eviction : <num>,
      eviction server unable to reach eviction goal : <num>,
      eviction server waiting for a leaf page : <num>,
      eviction server waiting for an internal page sleep (usec) : <num>,
      eviction server waiting for an internal page yields : <num>,
      eviction state : <num>,
      eviction walk target pages histogram - 0-9 : <num>,
      eviction walk target pages histogram - 10-31 : <num>,
      eviction walk target pages histogram - 128 and higher : <num>,
      eviction walk target pages histogram - 32-63 : <num>,
      eviction walk target pages histogram - 64-128 : <num>,
      eviction walks abandoned : <num>,
      eviction walks gave up because they restarted their walk twice : <num>,
      eviction walks gave up because they saw too many pages and found no candidates : <num>,
      eviction walks gave up because they saw too many pages and found too few candidates : <num>,
      eviction walks reached end of tree : <num>,
      eviction walks started from root of tree : <num>,
      eviction walks started from saved location in tree : <num>,
      eviction worker thread active : <num>,
      eviction worker thread created : <num>,
      eviction worker thread evicting pages : <num>,
      eviction worker thread removed : <num>,
      eviction worker thread stable number : <num>,
      files with active eviction walks : <num>,
      files with new eviction walks started : <num>,
      force re-tuning of eviction workers once in a while : <num>,
      forced eviction - pages evicted that were clean count : <num>,
      forced eviction - pages evicted that were clean time (usecs) : <num>,
      forced eviction - pages evicted that were dirty count : <num>,
      forced eviction - pages evicted that were dirty time (usecs) : <num>,
      forced eviction - pages selected because of too many deleted items count : <num>,
      forced eviction - pages selected count : <num>,
      forced eviction - pages selected unable to be evicted count : <num>,
      forced eviction - pages selected unable to be evicted time : <num>,
      hazard pointer blocked page eviction : <num>,
      hazard pointer check calls : <num>,
      hazard pointer check entries walked : <num>,
      hazard pointer maximum array length : <num>,
      in-memory page passed criteria to be split : <num>,
      in-memory page splits : <num>,
      internal pages evicted : <num>,
      internal pages split during eviction : <num>,
      leaf pages split during eviction : <num>,
      maximum bytes configured : <num>,
      maximum page size at eviction : <num>,
      modified pages evicted : <num>,
      modified pages evicted by application threads : <num>,
      operations timed out waiting for space in cache : <num>,
      overflow pages read into cache : <num>,
      page split during eviction deepened the tree : <num>,
      page written requiring cache overflow records : <num>,
      pages currently held in the cache : <num>,
      pages evicted by application threads : <num>,
      pages queued for eviction : <num>,
      pages queued for eviction post lru sorting : <num>,
      pages queued for urgent eviction : <num>,
      pages queued for urgent eviction during walk : <num>,
      pages read into cache : <num>,
      pages read into cache after truncate : <num>,
      pages read into cache after truncate in prepare state : <num>,
      pages read into cache requiring cache overflow entries : <num>,
      pages read into cache requiring cache overflow for checkpoint : <num>,
      pages read into cache skipping older cache overflow entries : <num>,
      pages read into cache with skipped cache overflow entries needed later : <num>,
      pages read into cache with skipped cache overflow entries needed later by checkpoint : <num>,
      pages requested from the cache : <num>,
      pages seen by eviction walk : <num>,
      pages selected for eviction unable to be evicted : <num>,
      pages walked for eviction : <num>,
      pages written from cache : <num>,
      pages written requiring in-memory restoration : <num>,
      percentage overhead : <num>,
      tracked bytes belonging to internal pages in the cache : <num>,
      tracked bytes belonging to leaf pages in the cache : <num>,
      tracked dirty bytes in the cache : <num>,
      tracked dirty pages in the cache : <num>,
      unmodified pages evicted : <num>
   },
   capacity : {
      background fsync file handles considered : <num>,
      background fsync file handles synced : <num>,
      background fsync time (msecs) : <num>,
      bytes read : <num>,
      bytes written for checkpoint : <num>,
      bytes written for eviction : <num>,
      bytes written for log : <num>,
      bytes written total : <num>,
      threshold to call fsync : <num>,
      time waiting due to total capacity (usecs) : <num>,
      time waiting during checkpoint (usecs) : <num>,
      time waiting during eviction (usecs) : <num>,
      time waiting during logging (usecs) : <num>,
      time waiting during read (usecs) : <num>
   },
   connection : {
      auto adjusting condition resets : <num>,
      auto adjusting condition wait calls : <num>,
      detected system time went backwards : <num>,
      files currently open : <num>,
      memory allocations : <num>,
      memory frees : <num>,
      memory re-allocations : <num>,
      pthread mutex condition wait calls : <num>,
      pthread mutex shared lock read-lock calls : <num>,
      pthread mutex shared lock write-lock calls : <num>,
      total fsync I/Os : <num>,
      total read I/Os : <num>,
      total write I/Os : <num>
   },
   cursor : {
      cached cursor count : <num>,
      cursor bulk loaded cursor insert calls : <num>,
      cursor close calls that result in cache : <num>,
      cursor create calls : <num>,
      cursor insert calls : <num>,
      cursor insert key and value bytes : <num>,
      cursor modify calls : <num>,
      cursor modify key and value bytes affected : <num>,
      cursor modify value bytes modified : <num>,
      cursor next calls : <num>,
      cursor operation restarted : <num>,
      cursor prev calls : <num>,
      cursor remove calls : <num>,
      cursor remove key bytes removed : <num>,
      cursor reserve calls : <num>,
      cursor reset calls : <num>,
      cursor search calls : <num>,
      cursor search near calls : <num>,
      cursor sweep buckets : <num>,
      cursor sweep cursors closed : <num>,
      cursor sweep cursors examined : <num>,
      cursor sweeps : <num>,
      cursor truncate calls : <num>,
      cursor update calls : <num>,
      cursor update key and value bytes : <num>,
      cursor update value size change : <num>,
      cursors reused from cache : <num>,
      open cursor count : <num>
   },
   data-handle : {
      connection data handle size : <num>,
      connection data handles currently active : <num>,
      connection sweep candidate became referenced : <num>,
      connection sweep dhandles closed : <num>,
      connection sweep dhandles removed from hash list : <num>,
      connection sweep time-of-death sets : <num>,
      connection sweeps : <num>,
      session dhandles swept : <num>,
      session sweep attempts : <num>
   },
   lock : {
      checkpoint lock acquisitions : <num>,
      checkpoint lock application thread wait time (usecs) : <num>,
      checkpoint lock internal thread wait time (usecs) : <num>,
      dhandle lock application thread time waiting (usecs) : <num>,
      dhandle lock internal thread time waiting (usecs) : <num>,
      dhandle read lock acquisitions : <num>,
      dhandle write lock acquisitions : <num>,
      durable timestamp queue lock application thread time waiting (usecs) : <num>,
      durable timestamp queue lock internal thread time waiting (usecs) : <num>,
      durable timestamp queue read lock acquisitions : <num>,
      durable timestamp queue write lock acquisitions : <num>,
      metadata lock acquisitions : <num>,
      metadata lock application thread wait time (usecs) : <num>,
      metadata lock internal thread wait time (usecs) : <num>,
      read timestamp queue lock application thread time waiting (usecs) : <num>,
      read timestamp queue lock internal thread time waiting (usecs) : <num>,
      read timestamp queue read lock acquisitions : <num>,
      read timestamp queue write lock acquisitions : <num>,
      schema lock acquisitions : <num>,
      schema lock application thread wait time (usecs) : <num>,
      schema lock internal thread wait time (usecs) : <num>,
      table lock application thread time waiting for the table lock (usecs) : <num>,
      table lock internal thread time waiting for the table lock (usecs) : <num>,
      table read lock acquisitions : <num>,
      table write lock acquisitions : <num>,
      txn global lock application thread time waiting (usecs) : <num>,
      txn global lock internal thread time waiting (usecs) : <num>,
      txn global read lock acquisitions : <num>,
      txn global write lock acquisitions : <num>
   },
   log : {
      busy returns attempting to switch slots : <num>,
      force archive time sleeping (usecs) : <num>,
      log bytes of payload data : <num>,
      log bytes written : <num>,
      log files manually zero-filled : <num>,
      log flush operations : <num>,
      log force write operations : <num>,
      log force write operations skipped : <num>,
      log records compressed : <num>,
      log records not compressed : <num>,
      log records too small to compress : <num>,
      log release advances write LSN : <num>,
      log scan operations : <num>,
      log scan records requiring two reads : <num>,
      log server thread advances write LSN : <num>,
      log server thread write LSN walk skipped : <num>,
      log sync operations : <num>,
      log sync time duration (usecs) : <num>,
      log sync_dir operations : <num>,
      log sync_dir time duration (usecs) : <num>,
      log write operations : <num>,
      logging bytes consolidated : <num>,
      maximum log file size : <num>,
      number of pre-allocated log files to create : <num>,
      pre-allocated log files not ready and missed : <num>,
      pre-allocated log files prepared : <num>,
      pre-allocated log files used : <num>,
      records processed by log scan : <num>,
      slot close lost race : <num>,
      slot close unbuffered waits : <num>,
      slot closures : <num>,
      slot join atomic update races : <num>,
      slot join calls atomic updates raced : <num>,
      slot join calls did not yield : <num>,
      slot join calls found active slot closed : <num>,
      slot join calls slept : <num>,
      slot join calls yielded : <num>,
      slot join found active slot closed : <num>,
      slot joins yield time (usecs) : <num>,
      slot transitions unable to find free slot : <num>,
      slot unbuffered writes : <num>,
      total in-memory size of compressed records : <num>,
      total log buffer size : <num>,
      total size of compressed records : <num>,
      written slots coalesced : <num>,
      yields waiting for previous log file close : <num>
   },
   perf : {
      file system read latency histogram (bucket 1) - 10-49ms : <num>,
      file system read latency histogram (bucket 2) - 50-99ms : <num>,
      file system read latency histogram (bucket 3) - 100-249ms : <num>,
      file system read latency histogram (bucket 4) - 250-499ms : <num>,
      file system read latency histogram (bucket 5) - 500-999ms : <num>,
      file system read latency histogram (bucket 6) - 1000ms+ : <num>,
      file system write latency histogram (bucket 1) - 10-49ms : <num>,
      file system write latency histogram (bucket 2) - 50-99ms : <num>,
      file system write latency histogram (bucket 3) - 100-249ms : <num>,
      file system write latency histogram (bucket 4) - 250-499ms : <num>,
      file system write latency histogram (bucket 5) - 500-999ms : <num>,
      file system write latency histogram (bucket 6) - 1000ms+ : <num>,
      operation read latency histogram (bucket 1) - 100-249us : <num>,
      operation read latency histogram (bucket 2) - 250-499us : <num>,
      operation read latency histogram (bucket 3) - 500-999us : <num>,
      operation read latency histogram (bucket 4) - 1000-9999us : <num>,
      operation read latency histogram (bucket 5) - 10000us+ : <num>,
      operation write latency histogram (bucket 1) - 100-249us : <num>,
      operation write latency histogram (bucket 2) - 250-499us : <num>,
      operation write latency histogram (bucket 3) - 500-999us : <num>,
      operation write latency histogram (bucket 4) - 1000-9999us : <num>,
      operation write latency histogram (bucket 5) - 10000us+ : <num>
   },
   reconciliation : {
      fast-path pages deleted : <num>,
      page reconciliation calls : <num>,
      page reconciliation calls for eviction : <num>,
      pages deleted : <num>,
      split bytes currently awaiting free : <num>,
      split objects currently awaiting free : <num>
   },
   session : {
      open session count : <num>,
      session query timestamp calls : <num>,
      table alter failed calls : <num>,
      table alter successful calls : <num>,
      table alter unchanged and skipped : <num>,
      table compact failed calls : <num>,
      table compact successful calls : <num>,
      table create failed calls : <num>,
      table create successful calls : <num>,
      table drop failed calls : <num>,
      table drop successful calls : <num>,
      table import failed calls : <num>,
      table import successful calls : <num>,
      table rebalance failed calls : <num>,
      table rebalance successful calls : <num>,
      table rename failed calls : <num>,
      table rename successful calls : <num>,
      table salvage failed calls : <num>,
      table salvage successful calls : <num>,
      table truncate failed calls : <num>,
      table truncate successful calls : <num>,
      table verify failed calls : <num>,
      table verify successful calls : <num>
   },
   thread-state : {
      active filesystem fsync calls : <num>,
      active filesystem read calls : <num>,
      active filesystem write calls : <num>
   },
   thread-yield : {
      application thread time evicting (usecs) : <num>,
      application thread time waiting for cache (usecs) : <num>,
      connection close blocked waiting for transaction state stabilization : <num>,
      connection close yielded for lsm manager shutdown : <num>,
      data handle lock yielded : <num>,
      get reference for page index and slot time sleeping (usecs) : <num>,
      log server sync yielded for log write : <num>,
      page access yielded due to prepare state change : <num>,
      page acquire busy blocked : <num>,
      page acquire eviction blocked : <num>,
      page acquire locked blocked : <num>,
      page acquire read blocked : <num>,
      page acquire time sleeping (usecs) : <num>,
      page delete rollback time sleeping for state change (usecs) : <num>,
      page reconciliation yielded due to child modification : <num>
   },
   transaction : {
      Number of prepared updates : <num>,
      Number of prepared updates added to cache overflow : <num>,
      Number of prepared updates resolved : <num>,
      durable timestamp queue entries walked : <num>,
      durable timestamp queue insert to empty : <num>,
      durable timestamp queue inserts to head : <num>,
      durable timestamp queue inserts total : <num>,
      durable timestamp queue length : <num>,
      number of named snapshots created : <num>,
      number of named snapshots dropped : <num>,
      prepared transactions : <num>,
      prepared transactions committed : <num>,
      prepared transactions currently active : <num>,
      prepared transactions rolled back : <num>,
      query timestamp calls : <num>,
      read timestamp queue entries walked : <num>,
      read timestamp queue insert to empty : <num>,
      read timestamp queue inserts to head : <num>,
      read timestamp queue inserts total : <num>,
      read timestamp queue length : <num>,
      rollback to stable calls : <num>,
      rollback to stable updates aborted : <num>,
      rollback to stable updates removed from cache overflow : <num>,
      set timestamp calls : <num>,
      set timestamp durable calls : <num>,
      set timestamp durable updates : <num>,
      set timestamp oldest calls : <num>,
      set timestamp oldest updates : <num>,
      set timestamp stable calls : <num>,
      set timestamp stable updates : <num>,
      transaction begins : <num>,
      transaction checkpoint currently running : <num>,
      transaction checkpoint generation : <num>,
      transaction checkpoint max time (msecs) : <num>,
      transaction checkpoint min time (msecs) : <num>,
      transaction checkpoint most recent time (msecs) : <num>,
      transaction checkpoint scrub dirty target : <num>,
      transaction checkpoint scrub time (msecs) : <num>,
      transaction checkpoint total time (msecs) : <num>,
      transaction checkpoints : <num>,
      transaction checkpoints skipped because database was clean : <num>,
      transaction failures due to cache overflow : <num>,
      transaction fsync calls for checkpoint after allocating the transaction ID : <num>,
      transaction fsync duration for checkpoint after allocating the transaction ID (usecs) : <num>,
      transaction range of IDs currently pinned : <num>,
      transaction range of IDs currently pinned by a checkpoint : <num>,
      transaction range of IDs currently pinned by named snapshots : <num>,
      transaction range of timestamps currently pinned : <num>,
      transaction range of timestamps pinned by a checkpoint : <num>,
      transaction range of timestamps pinned by the oldest active read timestamp : <num>,
      transaction range of timestamps pinned by the oldest timestamp : <num>,
      transaction read timestamp of the oldest active reader : <num>,
      transaction sync calls : <num>,
      transactions committed : <num>,
      transactions rolled back : <num>,
      update conflicts : <num>
   },
   concurrentTransactions : {
      write : {
         out : <num>,
         available : <num>,
         totalTickets : <num>
      },
      read : {
         out : <num>,
         available : <num>,
         totalTickets : <num>
      },
      monitor : { 
         timesDecreased: <num>, 
         timesIncreased: <num>, 
         totalAmountDecreased: <num>, 
         totalAmountIncreased: <num>
      }
   },
   snapshot-window-settings : {
      total number of SnapshotTooOld errors : <num>,
      max target available snapshots window size in seconds : <num>,
      target available snapshots window size in seconds : <num>,
      current available snapshots window size in seconds : <num>,
      latest majority snapshot timestamp available : <string>,
      oldest majority snapshot timestamp available : <string>
   }
}
```

> **Note:** The following is not an exhaustive list.
