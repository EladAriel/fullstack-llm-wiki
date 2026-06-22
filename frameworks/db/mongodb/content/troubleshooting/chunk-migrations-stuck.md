---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/troubleshooting/chunk-migrations-stuck.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================

# Troubleshoot Stuck Chunk Migrations

Sharded clusters can encounter situations where chunk migrations stall or where one or more chunks become jumbo. When this occurs, the balancer cannot evenly distribute data across shards. This can result in uneven resource utilization and degraded cluster performance.

This page describes common causes of stalled chunk migrations and jumbo chunks, along with steps to diagnose and resolve these conditions. If the issue persists after completing the steps below, contact Technical Support.

## Prerequisite Checks

Verify that your cluster is affected by stalled migrations or jumbo chunks.

### Check Balancer State

From a `mongos` instance, run:

```bash
sh.getBalancerState()
```

If this method returns `true` but data distribution remains uneven, additional investigation is required.

You can also review detailed balancer information:

```bash
db.adminCommand({ balancerStatus: 1 })
```

### Check Chunk Distribution

To review chunk distribution across shards, run:

```bash
sh.status(true)
```

Look for:

- Large differences in the number of chunks per shard
- Chunks marked as `jumbo`
> **Note:** A chunk marked as `jumbo` cannot be migrated by the balancer until
it is split or otherwise reduced in size.

### Check Log Messages

#### Config Server Logs

Review config server logs for entries related to balancing or chunk migration. Look for messages indicating:

- Migration retries
- Aborted migrations
- Chunks marked as jumbo
- Failures during migration commit or delete phases
#### Shard Logs

On shard nodes, review logs for:

- Lock acquisition timeouts
- Replication lag affecting migration
- Disk space errors
- Migration step failures
## Common Issues and Resolutions

### Jumbo Chunks Prevent Migration

A chunk becomes jumbo when it exceeds the configured chunk size and cannot be split automatically.

#### Identify Jumbo Chunks

From `mongos`:

```bash
sh.status(true)
```

Locate chunks labeled as `jumbo`.

#### Resolve Jumbo Chunks

**Divisible chunks** contain multiple unique shard key values and can be split. To resolve a divisible jumbo chunk, manually split it:

```bash
sh.splitAt("database.collection", { shardKeyField: <value> })
```

Then restart the balancer if necessary:

```bash
sh.startBalancer()
```

To learn when manual splitting is appropriate, see `split-chunks-sharded-cluster`.

**Indivisible chunks** represent a single unique shard key value and cannot be split. To resolve an indivisible jumbo chunk:

- Refine the shard key using
:dbcommand:`refineCollectionShardKey` to add a suffix field, making the chunk divisible. See `preferred-method-clear-jumbo`.

- Reshard the collection using a more evenly distributed shard key.
See `sharding-resharding`.

For more details on resolving jumbo chunks, see `clear-jumbo-flag`.

### Ineffective Shard Key Distribution

If the shard key has low cardinality or follows a monotonically increasing pattern, chunks may grow unevenly and resist balancing.

To mitigate:

- Review the shard key pattern used by the collection.
- Determine whether most writes target a narrow shard key range.
If high-frequency shard key values are causing writes to concentrate on a single shard, see `Troubleshooting Shard Keys <shard-hotness>`.

- Consider resharding the collection using a more evenly distributed
shard key.

See `sharding-shard-key-selection` for best practices.

### Balancer Disabled or Paused

If the balancer is disabled, chunk migrations do not occur.

Check balancer state:

```bash
sh.getBalancerState()
```

If disabled, enable it:

```bash
sh.startBalancer()
```

See `sharding-balancing` for additional balancer behavior details.

### Migration Blocked by Ongoing Operations

Long-running operations, index builds, or heavy write workloads may delay or block chunk migrations.

To reduce contention:

- Identify long-running operations:
```bash
  db.currentOp()
```

- Schedule balancing during periods of lower write activity.
- Ensure sufficient disk space is available on all shards.
> **Note:** Chunk migration involves data cloning and a delete phase. Insufficient
disk space or high replication lag can delay these phases.

## Verify Resolution

After resolving the issue:

- Chunk migrations complete successfully.
- No chunks remain marked as `jumbo`.
- Chunk distribution across shards becomes more even.
- The balancer remains active and stable.
Recheck distribution:

```bash
sh.status(true)
```

## Diagnostics to Collect for More Support

If the issue persists, collect the following before contacting Technical Support:

- Output of `sh.status(true)`
- Output of `db.adminCommand({ balancerStatus: 1 })`
- Relevant config server logs
- Relevant shard logs
- Shard key definition for affected collections
- MongoDB version
- Cluster topology description
- Output of `sh.getShardedDataDistribution()` for chunk count
and data size per shard
