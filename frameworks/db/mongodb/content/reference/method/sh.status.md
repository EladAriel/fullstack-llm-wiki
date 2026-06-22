---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.status.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# sh.status() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Output Examples

The `sharding-status-version-fields` section displays information on the `config database`:

```javascript
--- Sharding Status ---
  sharding version: {
   "_id" : <num>,
   "minCompatibleVersion" : <num>,
   "currentVersion" : <num>,
   "clusterId" : <ObjectId>
}
```

The `sharding-status-shards-fields` section lists information on the shard(s). For each shard, the section displays the name, host, and the associated tags, if any.

```javascript
  shards:
   { "_id" : <shard name1>, "host" : <string>, "tags" : [ <string> ... ], "state" : <num> }
   { "_id" : <shard name2>, "host" : <string>, "tags" : [ <string> ... ], "state" : <num> }
   ...
```

The `sharding-status-mongoses` section displays, by default, information on the version and count of :binary:`~bin.mongos` instances that have been active within the last 60 seconds:

```javascript
active mongoses:
  <version> : <num>
```

If the method is run with the `verbose` parameter to true, the `sharding-status-mongoses` section displays additional information:

```javascript
active mongoses:
{  "_id" : "<hostname:port>",  "advisoryHostFQDNs" : [ "<name>" ],  "mongoVersion" : <string>,  "ping" : <ISODate>,  "up" : <long>,  "waiting" : <boolean> }
```

The `autosplit-status` displays information on whether autosplit is enabled:

```javascript
autosplit:
  Currently enabled: <yes|no>
```

The `sharding-status-balancer-fields` section lists information about the state of the `balancer`. This provides insight into current balancer operation and can be useful when troubleshooting an unbalanced sharded cluster.

```none
balancer:
      Currently enabled:  yes
      Currently running:  yes
      Collections with active migrations: 
              config.system.sessions started at Fri May 15 2020 17:38:12 GMT-0400 (EDT)
      Failed balancer rounds in last 5 attempts:  0
      Migration Results for the last 24 hours: 
             416 : Success
             1 : Failed with error 'aborted', from shardA to shardB
```

The `sharding-status-databases-fields` section lists information on the database(s). It displays the database name and the `primary shard` for each database.

```javascript
  databases:
   { "_id" : <dbname1>, "primary" : <string>, "version": <document> }
   { "_id" : <dbname2>, "primary" : <string>, "version": <document> }
   ...
```

The `sharding-status-collection-fields` section provides information on the sharding details for sharded collection(s). For each sharded collection, the section displays the shard key, the number of chunks per shard(s), the distribution of chunks across shards [#chunk-details]_, and the tag information, if any, for shard key range(s).

.. include:: /includes/reference/sharded-status-output.rst

The `sharding-status-sharded-data-distribution` section displays data distribution information for each sharded collection:

```javascript
shardedDataDistribution:
[
  {
    "ns" : "<database>.<collection>",
    "shards" : [
      {
        "shardName" : "<shard name>",
        "numOrphanedDocs" : <num>,
        "numOwnedDocuments" : <num>,
        "ownedSizeBytes" : <num>,
        "orphanedSizeBytes" : <num>
      }
    ]
  }
]
```

## Output Fields

### Sharding Version

### Active `mongos` Instances

### Autosplit

> **Note:** .. include:: /includes/extracts/4.2-changes-balancer-autosplit.rst

### Automerge

### Shards

### Balancer

> **Note:** .. include:: /includes/extracts/4.2-changes-balancer-autosplit.rst

### Databases

### Sharded Collection

### Sharded Data Distribution

> **Seealso:** :method:`sh.balancerCollectionStatus()`

displays the chunk information if the total number of chunks is less than 20. To display the information when you have 20 or more chunks, call the :method:`sh.status()` methods with the `verbose` parameter set to `true`, i.e. `sh.status(true)`.
