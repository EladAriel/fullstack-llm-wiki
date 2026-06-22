---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/migrate-chunks-in-sharded-cluster.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================

# Migrate Ranges in a Sharded Cluster

In most circumstances, you should let the automatic `balancer` migrate `ranges <range>` between `shards <shard>`. However, you may want to migrate ranges manually in a few cases:

- When `pre-splitting` an empty collection, migrate ranges
manually to distribute them evenly across the shards. Use pre-splitting in limited situations to support bulk data ingestion.

- If the balancer in an active cluster cannot distribute ranges within
the `balancing window <sharding-schedule-balancing-window>`, then you will have to migrate ranges manually.

To manually migrate ranges, use the :dbcommand:`moveChunk` or :dbcommand:`moveRange` command.

For more information on how the automatic balancer moves ranges between shards, see `sharding-balancing-internals` and `sharding-range-migration`.

See `create-ranges-in-a-sharded-cluster` for an introduction to pre-splitting.

- Use the :dbcommand:`moveChunk command with the secondaryThrottle`
and `writeConcern` fields to determine when the balancer proceeds with the next document in the migrating range.

- Use the :dbcommand:`moveRange` command with the `secondaryThrottle`
and `writeConcern` fields to determine when the balancer proceeds with the next document in the migrating range.

See :dbcommand:`moveChunk` and :dbcommand:`moveRange` for details.

## Change Streams and Orphan Documents

.. include:: /includes/change-streams-and-orphans.rst
