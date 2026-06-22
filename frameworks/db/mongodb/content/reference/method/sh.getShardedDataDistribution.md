---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.getShardedDataDistribution.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================================

# sh.getShardedDataDistribution() (mongosh method)

## Definition

.. versionadded:: 6.0.3

.. include:: /includes/sharding/getShardedDataDistribution-shell-helper-method-summary.rst

You can only run the method from a :binary:`~bin.mongosh` session connected to a :binary:`~bin.mongos` instance.

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The method has the following syntax:

```javascript
sh.getShardedDataDistribution()
```

## Example

The following example runs the method:

```javascript
sh.getShardedDataDistribution()
```

The method returns an array of documents for each sharded collection. For example:

```javascript
[
   {
      ns: 'config.system.sessions',
      shards: [
         {
            shardName: 'shard1',
            numOrphanedDocs: 0,
            numOwnedDocuments: 18,
            ownedSizeBytes: 1782,
            orphanedSizeBytes: 0
         }
      ]
   },
   {
      ns: 'records.people',
      shards: [
         {
            shardName: 'shard1',
            numOrphanedDocs: 0,
            numOwnedDocuments: 21,
            ownedSizeBytes: 134,
            orphanedSizeBytes: 0
         }
      ]
   }
]
```

The following table describes the output fields:

.. include:: /includes/sharding/shardedDataDistribution-output.rst

## Learn More

- :pipeline:`$shardedDataDistribution`
- :method:`sh.enableSharding()`
- :method:`sh.addShard()`
- :method:`sh.shardCollection()`
- :method:`sh.reshardCollection()`
