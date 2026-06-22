---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/sharded-cluster-requirements.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
