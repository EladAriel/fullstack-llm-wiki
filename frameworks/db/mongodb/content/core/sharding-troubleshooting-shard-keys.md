---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/sharding-troubleshooting-shard-keys.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================

# Troubleshoot Shard Keys

The ideal shard key allows MongoDB to distribute documents evenly throughout the cluster while facilitating common query patterns. A suboptimal shard key can lead to the following problems:

- `Jumbo chunks <sharding-troubleshooting-jumbo-chunks>`
- :ref:`Uneven load distribution
<sharding-troubleshooting-monotonicity>`

- :ref:`Decreased query performance over time
<sharding-troubleshooting-scatter-gather>`

In the following you can find out more about common problems with shard keys and how to resolve them.

## Jumbo Chunks

If you are seeing `jumbo chunks <jumbo-chunks>`, either the `cardinality <shard-key-cardinality>` of your shard key is insufficient or the `frequency<shard-key-frequency>` of the shard key values is unevenly distributed.

To increase the cardinality of your shard key or change the distribution of your shard key values, you can:

- `refine your shard key <shard-key-refine>` by adding a suffix
field or fields to the existing key to increase cardinality

- `reshard your collection <sharding-resharding>` using a
different shard key with higher cardinality

To learn whether you should reshard your collection or refine your shard key, see `change-a-shard-key`.

To only change the distribution of your shard key values, you can also consider using `/core/hashed-sharding` to distribute your data more evenly.

For advice on choosing a shard key see `sharding-shard-key-selection`.

## Uneven Load Distribution

If your cluster is experiencing uneven load distribution, check if your shard key increases `monotonically <shard-key-monotonic>`. A shard key that is a monotonically increasing field, leads to an uneven read and write distribution.

Consider an `orders` collection that is sharded on an `order_id` field. The `order_id` is an integer which increases by one with each order.

- New documents are generally written to the same shard and chunk. The
shard and chunk that receive the writes are called hot shard and hot chunk. The hot shard changes over time. When chunks are split, the hot chunk moves to a different shard to optimize data distribution.

- If users are more likely to interact with recent orders, which are all
on the same shard, the shard that contains recent orders will receive most of the traffic.

If you have a monotonically increasing shard key, consider `resharding your collection <sharding-resharding>`. For advice on choosing a shard key see `sharding-shard-key-selection`.

If your data model requires sharding on a key that changes monotonically, consider using `/core/hashed-sharding`.

## Decreased Query Performance Over Time

If you are noticing decreased query performance over time, it is possible that your cluster is performing `scatter-gather queries <sharding-query-patterns>`.

To evaluate if your cluster is performing scatter-gather queries, check if your most common queries include the shard key.

If you include the shard key in your queries, check if your shard key is hashed. With `/core/hashed-sharding`, documents are not stored in ascending or descending order of the shard key field value. Performing range based queries on the shard key value on data that is not stored in ascending or descending order results in less performant scatter-gather queries. If range based queries on your shard key are a common access pattern, consider `resharding your collection <sharding-resharding>`.

If you do not include the shard key in your most common queries, it is possible that you could increase performance by `resharding your collection <sharding-resharding>`. For advice on choosing a shard key see `sharding-shard-key-selection`.
