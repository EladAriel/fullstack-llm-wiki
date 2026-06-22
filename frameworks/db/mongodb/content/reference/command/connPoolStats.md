---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/connPoolStats.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================

# connPoolStats (database command)

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
     connPoolStats: 1
   }  
)
```

The value of the argument (i.e. `1` ) does not affect the output of the command.

## Behavior

:dbcommand:`connPoolStats` includes aggregated statistics in its output:

- The `connPoolStats.hosts` field displays the information
aggregated by host.

- The `connPoolStats.pools` field displays the information
aggregated by pool.

> **Note:** To avoid interference with any running operations,
:dbcommand:`connPoolStats` does not take any locks. As such, the
counts may change slightly as :dbcommand:`connPoolStats` gathers
information, resulting in slight differences between the
`connPoolStats.hosts` and `connPoolStats.pools`
connection counts.

## Example

The following operation uses the :method:`db.runCommand()` method to run the :dbcommand:`connPoolStats` command on a :binary:`~bin.mongos` of a sharded cluster. The sharded cluster has 2 shards, each a single-member replica set, and a config server replica set. The :binary:`~bin.mongos` runs on a 4-core machine.

```javascript
db.runCommand( { "connPoolStats" : 1 } )
```

The command returns the output of the following form:

> **Note:** The :dbcommand:`connPoolStats` output varies depending on the
deployment and the member against which you run
:dbcommand:`connPoolStats` among other factors.

```javascript
{
   "numClientConnections" : <num>,
   "numAScopedConnections" : <num>,
   "totalInUse" : <num>,
   "totalAvailable" : <num>,
   "totalLeased" : <num>,
   "totalCreated" : <num>,
   "totalRefreshing" : <num>,
   "replicaSetMatchingStrategy" : <string>,
   "acquisitionWaitTimes" : {  // Added in MongoDB 6.3
      "(-inf, 0ms)" : { "count" : <num> },
      "[0ms, 50ms)" : { "count" : <num> },
      "[50ms, 100ms)" : { "count" : <num> },
      "[100ms, 150ms)" : { "count" : <num> },
      "[150ms, 200ms)" : { "count" : <num> },
      "[200ms, 250ms)" : { "count" : <num> },
      "[250ms, 300ms)" : { "count" : <num> },
      "[300ms, 350ms)" : { "count" : <num> },
      "[350ms, 400ms)" : { "count" : <num> },
      "[400ms, 450ms)" : { "count" : <num> },
      "[450ms, 500ms)" : { "count" : <num> },
      "[500ms, 550ms)" : { "count" : <num> },
      "[550ms, 600ms)" : { "count" : <num> },
      "[600ms, 650ms)" : { "count" : <num> },
      "[650ms, 700ms)" : { "count" : <num> },
      "[700ms, 750ms)" : { "count" : <num> },
      "[750ms, 800ms)" : { "count" : <num> },
      "[800ms, 850ms)" : { "count" : <num> },
      "[850ms, 900ms)" : { "count" : <num> },
      "[900ms, 950ms)" : { "count" : <num> },
      "[950ms, 1000ms)" : { "count" : <num> },
      "[1000ms, inf)" : { "count" : <num> },
      "totalCount" : <num>
   },
   "pools" : {
      "NetworkInterfaceTL-TaskExecutorPool-0" : {
         "poolInUse" : <num>,
         "poolAvailable" : <num>,
         "poolLeased" : <num>,
         "poolCreated" : <num>,
         "poolRefreshing" : <num>, 
         "acquisitionWaitTimes" : <document>,  // Added in MongoDB 6.3
         "cfg1.example.net:27019" : {
            "inUse" : <num>,
            "available" : <num>,
            "leased" : <num>,
            "created" : <num>,
            "refreshing" : <num>,
            "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
         },
      },
      "NetworkInterfaceTL-TaskExecutorPool-1" : {
         "poolInUse" : <num>,
         "poolAvailable" : <num>,
         "poolLeased" : <num>,
         "poolCreated" : <num>,
         "poolRefreshing" : <num>,
         "acquisitionWaitTimes" : <document>,  // Added in MongoDB 6.3
         "cfg1.example.net:27019" : {
            "inUse" : <num>,
            "available" : <num>,
            "leased" : <num>,
            "created" : <num>,
            "refreshing" : <num>,
            "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
         }
      },
      "NetworkInterfaceTL-TaskExecutorPool-2" : {
         "poolInUse" : <num>,
         "poolAvailable" : <num>,
         "poolLeased" : <num>,
         "poolCreated" : <num>,
         "poolRefreshing" : <num>, 
         "acquisitionWaitTimes" : <document>,  // Added in MongoDB 6.3
         "cfg1.example.net:27019" : {
            "inUse" : <num>,
            "available" : <num>,
            "leased" : <num>,
            "created" : <num>,
            "refreshing" : <num>,
            "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
         }
      },
      "NetworkInterfaceTL-TaskExecutorPool-3" : {
         "poolInUse" : <num>,
         "poolAvailable" : <num>,
         "poolLeased" : <num>,
         "poolCreated" : <num>,
         "poolRefreshing" : <num>, 
         "acquisitionWaitTimes" : <document>,  // Added in MongoDB 6.3
         "cfg1.example.net:27019" : {
            "inUse" : <num>,
            "available" : <num>,
            "leased" : <num>,
            "created" : <num>,
            "refreshing" : <num>,
            "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
         }
      },
      "NetworkInterfaceTL-ShardRegistry" : {
         "poolInUse" : <num>,
         "poolAvailable" : <num>,
         "poolLeased" : <num>,
         "poolCreated" : <num>,
         "poolRefreshing" : <num>, 
         "acquisitionWaitTimes" : <document>,  // Added in MongoDB 6.3
         "cfg1.example.net:27019" : {
            "inUse" : <num>,
            "available" : <num>,
            "leased" : <num>,
            "created" : <num>,
            "refreshing" : <num>,
            "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
         },
         "cfg2.example.net:27019" : {
            "inUse" : <num>,
            "available" : <num>,
            "leased" : <num>,
            "created" : <num>,
            "refreshing" : <num>,
            "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
         },
         "cfg3.example.net:27019" : {
            "inUse" : <num>,
            "available" : <num>,
            "leased" : <num>,
            "created" : <num>,
            "refreshing" : <num>,
            "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
         },
         "shard1.example.net:27018" : {
            "inUse" : <num>,
            "available" : <num>,
            "leased" : <num>,
            "created" : <num>,
            "refreshing" : <num>,
            "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
         },
         "shard2.example.net:27018" : {
            "inUse" : <num>,
            "available" : <num>,
            "leased" : <num>,
            "created" : <num>,
            "refreshing" : <num>,
            "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
         }
      },
      "global" : {
         "poolInUse" : <num>,
         "poolAvailable" : <num>,
         "poolLeased" : <num>,
         "poolCreated" : <num>,
         "poolRefreshing" : <num>, 
         "acquisitionWaitTimes" : <document>,  // Added in MongoDB 6.3
         "cfg3.example.net:27019" : {
            "inUse" : <num>,
            "available" : <num>,
            "leased" : <num>,
            "created" : <num>,
            "refreshing" : <num>,
            "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
         },
         "cfg1.example.net:27019" : {
            "inUse" : <num>,
            "available" : <num>,
            "leased" : <num>,
            "created" : <num>,
            "refreshing" : <num>,
            "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
         },
         "cfg2.example.net:27019" : {
            "inUse" : <num>,
            "available" : <num>,
            "leased" : <num>,
            "created" : <num>,
            "refreshing" : <num>,
            "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
         },
         "shard2.example.net:27018" : {
            "inUse" : <num>,
            "available" : <num>,
            "leased" : <num>,
            "created" : <num>,
            "refreshing" : <num>,
            "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
         },
         "shard1.example.net:27018" : {
            "inUse" : <num>,
            "available" : <num>,
            "leased" : <num>,
            "created" : <num>,
            "refreshing" : <num>,
            "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
         }
      }
   },
   "hosts" : {
      "cfg3.example.net:27019" : {
         "inUse" : <num>,
         "available" : <num>,
         "leased" : <num>,
         "created" : <num>,
         "refreshing" : <num>,
         "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
      },
      "cfg1.example.net:27019" : {
         "inUse" : <num>,
         "available" : <num>,
         "leased" : <num>,
         "created" : <num>,
         "refreshing" : <num>,
         "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
      },
      "cfg2.example.net:27019" : {
         "inUse" : <num>,
         "available" : <num>,
         "leased" : <num>,
         "created" : <num>,
         "refreshing" : <num>,
         "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
      },
      "shard2.example.net:27018" : {
         "inUse" : <num>,
         "available" : <num>,
         "leased" : <num>,
         "created" : <num>,
         "refreshing" : <num>,
         "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
      },
      "shard1.example.net:27018" : {
         "inUse" : <num>,
         "available" : <num>,
         "leased" : <num>,
         "created" : <num>,
         "refreshing" : <num>,
         "acquisitionWaitTimes" : <document>  // Added in MongoDB 6.3
      }
   },
   "replicaSets" : {
      "csRS" : {
         "hosts" : [
            {
               "addr" : "cfg1.example.net:27019",
               "ok" : <bool>,
               "ismaster" : <bool>,
               "hidden" : <bool>,
               "secondary" : <bool>,
               "pingTimeMillis" : <num>
            },
            {
               "addr" : "cfg2.example.net:27019",
               "ok" : <bool>,
               "ismaster" : <bool>,
               "hidden" : <bool>,
               "secondary" : <bool>,
               "pingTimeMillis" : <num>
            },
            {
               "addr" : "cfg3.example.net:27019",
               "ok" : <bool>,
               "ismaster" : <bool>,
               "hidden" : <bool>,
               "secondary" : <bool>,
               "pingTimeMillis" : <num>
            }
         ]
      },
      "shardB" : {
         "hosts" : [
            {
               "addr" : "shard2.example.net:27018",
               "ok" : <bool>,
               "ismaster" : <bool>,
               "hidden" : <bool>,
               "secondary" : <bool>,
               "pingTimeMillis" : <num>
            }
         ]
      },
      "shardA" : {
         "hosts" : [
            {
               "addr" : "shard1.example.net:27018",
               "ok" : <bool>,
               "ismaster" : <bool>,
               "hidden" : <bool>,
               "secondary" : <bool>,
               "pingTimeMillis" : <num>
            }
         ]
      }
   },
   "ok" : 1,
   "$clusterTime" : {
      "clusterTime" : <timestamp>,
      "signature" : <document>
   },
   "operationTime" : <timestamp>
}
```

## Output

See also `command-response` for details on the `ok` status field, the `operationTime` field and the `$clusterTime` field.

`host <connPoolStats.replicaSets.[replicaSets].hosts>`
