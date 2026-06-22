---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/remove-shards-from-cluster.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================

# Remove Shards from a Sharded Cluster

To remove a `shard` you must ensure the shard's data is migrated to the remaining shards in the cluster. This procedure describes how to safely migrate data and remove a shard.

## About this Task

- .. include:: /includes/fact-draining-procedure-interruptions.rst
- .. include:: /includes/fact-do-not-migrate-cluster-hardware.rst
- .. include:: /includes/fact-remove-shard-balance-order.rst
- .. include:: /includes/extracts/changestream-remove-shard-with-link.rst
- You can safely restart a cluster during a shard removal process. If
you restart a cluster during an ongoing `draining` process, draining continues automatically after the cluster components restart. MongoDB records the shard draining status in the `config.shards` collection.

## Before you Begin

1. This procedure uses the :method:`sh.moveCollection()` method to move
collections off of the removed shard. Before you begin this procedure, review the `moveCollection` `considerations <moveCollection-method-considerations>` and `requirements <moveCollection-method-reqs>` to understand the command behavior.

#. To remove a shard, first connect to one of the cluster's :binary:`~bin.mongos` instances using :binary:`~bin.mongosh`.

> **Note:** When removing multiple shards, remove them simultaneously rather
than one at a time. Removing one shard at a time causes the balancer
to drain data into other remaining shards. A shard can only participate
in one chunk migration at a time, so removing one shard limits the
throughput of data migration.

## Steps

## Learn More

- `sharding-procedure-add-member-to-shard`
- `back-up-sharded-cluster-metadata`
- `sharding-data-partitioning`
