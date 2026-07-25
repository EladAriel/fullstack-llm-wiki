---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/create-chunks-in-sharded-cluster.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==================================

# Create Ranges in a Sharded Cluster

In most situations a `sharded cluster` will create, split, and distribute ranges automatically without user intervention. However, in some cases, MongoDB cannot create enough ranges or distribute data fast enough to support the required throughput.

For example, if you want to ingest a large volume of data into a cluster where you have inserts distributed across shards, pre-splitting the ranges of an empty sharded collection can improve throughput.

> **Note:** Starting in MongoDB 6.0, the balancer does not distribute empty
ranges. To pre-split the collection, use :dbcommand:`moveRange` to
distribute the empty ranges across the shards in the cluster.
`moveRange` automatically splits the range to be moved, meaning
`moveRange` performs both splitting and moving. You don't need to
manually split the range with :dbcommand:`split`.

Alternatively, by defining the `zones and zone ranges </core/zone-sharding>` before sharding an empty or a non-existing collection, the shard collection operation creates ranges for the defined zone ranges as well as any additional ranges to cover the entire range of the shard key values and performs an initial range distribution based on the zone ranges. For more information, see `initial-ranges-empty-collection`.

> **Warning:** Only pre-split ranges for an empty collection. Manually splitting
ranges for a populated collection can lead to unpredictable range
ranges and sizes as well as inefficient or ineffective balancing
behavior.

## Steps

The following example shows how to manually generate and distribute ranges. The example uses a collection in the `sample.documents` namespace and shards that collection on the `email` field.

## Results

The `moveRange` command distributes the empty ranges across the shards in the cluster. The cluster is now optimized for bulk inserts.

## Next Steps

To further improve performance, create additional indexes to support your application's common queries.

## Learn More

- `bulk-write-sharded-collection`
- :method:`sh.balancerCollectionStatus()`
- Initial ranges created and distributed by the sharding command,
see `initial-ranges-empty-collection`.

- Balancer and automatic distribution of ranges across shards,
see `sharding-balancing-internals` and `sharding-range-migration`.

- Manually migrate ranges, see `<migrate-chunks-sharded-cluster>`.
