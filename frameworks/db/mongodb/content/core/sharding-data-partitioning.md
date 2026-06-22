---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/sharding-data-partitioning.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# Data Partitioning with Chunks

MongoDB uses the `shard key` associated to the collection to partition the data into `chunks<chunk>` owned by a specific shard. A `chunk` consists of a `range` of sharded data. Each chunk has inclusive lower and exclusive upper limits based on the `shard key`.

.. include:: /images/sharding-range-based.rst

The smallest unit of data a chunk can represent is a single unique shard key value.

## Initial Chunks

### Populated Collection

- The sharding operation creates one large initial chunk to cover all
of the shard key values.

- After the initial chunk creation, the balancer moves ranges off of
the initial chunk when it needs to start balancing data.

### Empty Collection

- If you have `zones and zone ranges <zone-sharding>` defined
for an empty or non-existing collection.

- The sharding operation creates empty chunks for the defined zone
ranges and any additional chunks to cover the entire range of the shard key values and performs an initial chunk distribution based on the zone ranges. This initial creation and distribution of chunks allows for faster setup of zoned sharding.

- After the initial distribution, the balancer manages the chunk
distribution going forward.

- If you do not have zones and zone ranges defined
for an empty or non-existing collection:

- For hashed sharding:
- The sharding operation creates empty chunks to cover the
entire range of the shard key values and performs an initial chunk distribution. By default, the operation creates 2 chunks per shard and migrates across the cluster.

- After the initial distribution, the balancer manages the chunk
distribution going forward.

- For ranged sharding:
- The sharding operation creates a single empty chunk to cover the
entire range of the shard key values.

- After the initial chunk creation, the balancer migrates the
initial chunk across the shards as appropriate and manages the chunk distribution going forward.

> **Seealso:** :method:`sh.balancerCollectionStatus()`

## Range Size

The default `range` size in MongoDB is 128 megabytes. You can `increase or reduce the chunk size <tutorial-modifying-range-size>`. Consider the implications of changing the default chunk size:

#. Small ranges lead to a more even distribution of data at the expense of more frequent migrations, which adds overhead at the query routing (:binary:`~bin.mongos`) layer.

#. Large ranges lead to fewer migrations, reducing networking and internal overhead at the query routing layer, but may result in an uneven distribution of data.

#. Range size affects the :limit:`Maximum Number of Documents Per Range to Migrate`.

For most deployments, a slightly uneven data distribution is preferable to frequent migrations.

## Range Migration

MongoDB migrates data ranges in a `sharded cluster` to distribute the data of a sharded collection evenly among shards. Migrations may be either:

- Manual. Only use manual migration in limited cases, such as
to distribute data during bulk inserts. See `Migrating Chunks Manually <migrate-chunks-sharded-cluster>` for more details.

- Automatic. The `balancer <sharding-balancing>` process
automatically migrates data when there is an uneven distribution of a sharded collection's data across the shards. See `Migration Thresholds <sharding-migration-thresholds>` for more details.

For more information on the sharded cluster `balancer`, see `sharding-balancing`.

> **Seealso:** :serverstatus:`shardingStatistics.countDonorMoveChunkLockTimeout`

### Balancing

The `balancer <sharding-balancing-internals>` is a background process that manages data migrations. If the data imbalance between the largest and smallest shard exceeds the `migration thresholds<sharding-migration-thresholds>`, the balancer begins migrating data across the cluster.

.. include:: /images/sharding-migrating.rst

You can `manage <sharded-cluster-balancer>` certain aspects of the balancer. The balancer also respects any `zones <zone>` created as a part of configuring zones in a sharded cluster.

See `sharding-balancing` for more information on the `balancer`.

### Reshard to Balance

.. include:: /includes/fact-reshard-init-shard-mongosh

## Indivisible/Jumbo Chunks

Chunks that grow beyond the `specified chunk size <sharding-chunk-size>` but cannot be split are called **jumbo** chunks. The most common cause is when a chunk represents a single shard key value. Jumbo chunks can become a performance bottleneck, especially if the shard key value occurs with high `frequency<shard-key-frequency>`.

Starting in MongoDB 5.0, you can `reshard a collection <sharding-resharding>` by changing a document's shard key.

The :dbcommand:`refineCollectionShardKey` command enables more fine-grained data distribution and can resolve jumbo chunks caused by insufficient shard key cardinality.

To learn whether you should reshard your collection or refine your shard key, see `change-a-shard-key`.

For more information, see:

- `<clear-jumbo-flag>`
- `migration-chunk-size-limit`
## Contents

- Create Ranges </tutorial/create-chunks-in-sharded-cluster>
- Split Chunks </tutorial/split-chunks-in-sharded-cluster>
- Merge Chunks </tutorial/merge-chunks-in-sharded-cluster>
- Modify Range Size </tutorial/modify-chunk-size-in-sharded-cluster>
- Moveable Collections </core/moveable-collections>
