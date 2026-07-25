---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/sharded-cluster-requirements.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

============================================

# Operational Restrictions in Sharded Clusters

with other nodes.

## Sharding Operational Restrictions

### Operations Unavailable in Sharded Environments

.. include:: /includes/limits-sharding-unavailable-operations.rst

### Single Document Modification Operations in Sharded Collections

and :method:`~db.collection.deleteOne()`

.. include:: /includes/fact-single-modification-in-sharded-collections.rst

To use :method:`~db.collection.findOneAndUpdate()` with a sharded collection, your query filter must include an equality condition on the `shard key` to compare the key and value in either of these formats:

```javascript
{ key: value }
{ key: { $eq: value } }
```

### Unique Indexes in Sharded Collections

.. include:: /includes/limits-sharding-unique-indexes.rst

### Consistent Indexes

MongoDB does not guarantee consistent indexes across shards.  Index creation during :dbcommand:`addShard` operations or chunk migrations may not propagate to new shards.

To check a sharded cluster for consistent indexes, use the :dbcommand:`checkMetadataConsistency` command:

```javascript
db.runCommand( {
   checkMetadataConsistency: 1,
   checkIndexes: true
} )
```

### Write Concern for DDL Operations

.. include:: /includes/ddl-ops-write-concern-sharded-clusters.rst
