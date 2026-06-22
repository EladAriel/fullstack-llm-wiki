---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/sharding-consolidate-collection-data.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================

# Consolidate Collection Data

Prior to MongoDB v8.0, sharding a collection was an irreversible action. Starting in v8.0, you can unshard a collection to the shard of your choice.

## When to Unshard a Collection

The following scenarios benefit from moving unsharded collections across shards.

### Correcting unintentional sharding of a collection

If you discover that sharding was unnecessary or causing performance issues, you can use the`unshardCollection` command to rewrite the entire collection as an unsharded collection.

### Simplifying zone-based isolation

If you use `zones <zone-sharding>` to keep a sharded collection on a single shard, you can now unshard the collection to reduce the complexity in your cluster.

### Consolidating previously sharded small collections

If you sharded small collections to efficiently utilize resources on multiple shards, you can unshard and move the collections to a shard of your choice. Doing so reduces the complexity of a deployment while maintaining appropriate resource allocation.

## Command Syntax

```javascript
sh.unshardCollection("database.collection", "shardName")
```

The following example unshards the `riders` collection in the `taxi` database and moves the collection to `shard1`.

```javascript
db.adminCommand({unshardCollection:"taxi.riders", toShard: "shard1"})
```

.. figure:: /images/sharding-unshard-collection.bakedsvg.svg

## Learn More

- `unshard-collection-task`
