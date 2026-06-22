---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/sharding.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========

# Sharding

## Contents

- Sharded Cluster Components </core/sharded-cluster-components>
- Shard Keys </core/sharding-shard-key>
- Hashed Sharding </core/hashed-sharding>
- Ranged Sharding </core/ranged-sharding>
- Zones </core/zone-sharding>
- Data Partitioning </core/sharding-data-partitioning>
- Balancer </core/sharding-balancer-administration>
- Long-Running Secondary Reads </core/long-running-secondary-reads>
- Administration </administration/sharded-cluster-administration>
- Reference </reference/sharding>
- mongot Architecture Patterns </tutorial/mongot-sizing/advanced-guidance/architecture>
- mongot Hardware </tutorial/mongot-sizing/advanced-guidance/hardware>
- mongot Resource Allocation </tutorial/mongot-sizing/advanced-guidance/resource-allocation>
- mongot Sizing Introduction </tutorial/mongot-sizing/introduction>
- mongot Sizing Quickstart </tutorial/mongot-sizing/quick-start>

`Sharding<sharding>` is a method for distributing data across multiple machines. MongoDB uses sharding to support deployments with very large data sets and high throughput operations.

Database systems with large data sets or high throughput applications can challenge the capacity of a single server. For example, high query rates can exhaust the CPU capacity of the server. Working set sizes larger than the system's RAM stress the I/O capacity of disk drives.

Two methods address system growth: vertical and horizontal scaling.

Vertical Scaling increases the capacity of a single server by using a more powerful CPU, adding more RAM, or expanding storage. Available technology and cloud provider hardware configurations impose a practical maximum for vertical scaling.

Horizontal Scaling involves dividing the system dataset and load over multiple servers, adding more servers to increase capacity as required. Each machine handles a subset of the overall workload, which can cost less than high-end hardware for a single machine. The trade-off is increased complexity in infrastructure and maintenance.

## Sharded Cluster

> **Note:** .. include:: /includes/fact-sharded-cluster-components.rst

The following graphic describes the interaction of components within a sharded cluster:

.. include:: /images/sharded-cluster-production-architecture.rst

MongoDB shards data at the `collection` level, distributing the collection data across the shards in the cluster.

## Shard Keys

MongoDB uses the `shard key <sharding-shard-key>` to distribute the collection's documents across shards. The shard key consists of a field or multiple fields in the documents.

Documents in sharded collections can be missing the shard key fields. Missing shard key fields are treated as having null values when distributing the documents across shards but not when routing queries. For more information, see `shard-key-missing`.

You select the shard key when `sharding a collection <sharding-shard-key-creation>`.

- Starting in MongoDB 5.0, you can :ref:`reshard a collection
<sharding-resharding>` by changing a collection's shard key.

- You can `refine a shard key <shard-key-refine>` by adding a suffix field
or fields to the existing shard key.

A document's shard key value determines its distribution across the shards. You can update a document's shard key value unless your shard key field is the immutable `_id` field. For more information, see `update-shard-key`.

### Shard Key Index

To shard a populated collection, the collection must have an `index` that starts with the shard key. When sharding an empty collection, MongoDB creates the supporting index if the collection does not already have an appropriate index for the specified shard key. See `sharding-shard-key-indexes`.

### Shard Key Strategy

The choice of shard key and its backing index can also affect the `sharding strategy <sharding-strategy>` that your cluster can use.

> **Seealso:** `sharding-shard-key-selection`

## Chunks

MongoDB partitions sharded data into `chunks<chunk>`. Each chunk has an inclusive lower and exclusive upper range based on the `shard key`.

## Balancer and Even Data Distribution

To achieve an even data distribution across all shards in the cluster, a `balancer <sharding-balancing>` runs in the background to migrate `ranges <range>` across the `shards <shard>`.

> **Seealso:** `sharding-range-migration`

## Advantages of Sharding

### Reads / Writes

MongoDB distributes the read and write workload across the `shards <shard>` in the `sharded cluster`, allowing each shard to process a subset of cluster operations. Both read and write workloads can be scaled horizontally across the cluster by adding more shards.

For queries that include the shard key or the prefix of a `compound <compound index>` shard key, :binary:`~bin.mongos` can target the query at a specific shard or set of shards. These `targeted operations<sharding-mongos-targeted>` are generally more efficient than `broadcasting <sharding-mongos-broadcast>` to every shard in the cluster.

### Storage Capacity

`Sharding <sharding>` distributes data across the `shards <shard>` in the cluster, allowing each shard to contain a subset of the total cluster data. As the data set grows, additional shards increase the storage capacity of the cluster.

### High Availability

The deployment of config servers and shards as replica sets provide increased availability.

Even if one or more shard replica sets become completely unavailable, the sharded cluster can continue to perform partial reads and writes. That is, while data on the unavailable shard(s) cannot be accessed, reads or writes directed at the available shards can still succeed.

## Considerations Before Sharding

Sharded cluster infrastructure requirements and complexity require careful planning, execution, and maintenance.

While you can `reshard your collection <sharding-resharding>` later, carefully consider your shard key choice to avoid scalability and performance issues.

> **Seealso:** `sharding-shard-key-selection`

To understand the operational requirements and restrictions for sharding your collection, see `/core/sharded-cluster-requirements`.

If queries do not include the shard key or the prefix of a `compound <compound index>` shard key, :binary:`~bin.mongos` performs a `broadcast operation <sharding-mongos-broadcast>`, querying all shards in the sharded cluster. These scatter/gather queries can be long running operations.

.. include:: /includes/fact-5.1-fassert-shard-restart-add-CWWC.rst

> **Note:** If you have an active support contract with MongoDB, consider contacting
your account representative for assistance with sharded cluster
planning and deployment.

### Reshard to Balance

.. include:: /includes/fact-reshard-init-shard-mongosh

## Sharded and Non-Sharded Collections

A database can have a mixture of sharded and unsharded collections. Sharded collections are `partitioned<data partition>` and distributed across the `shards<shard>` in the cluster. Unsharded collections can be located on any shard but cannot span across shards.

.. include:: /images/sharded-cluster-primary-shard.rst

## Connecting to a Sharded Cluster

You must connect to a `mongos` router to interact with any collection in the `sharded cluster`. This includes sharded and unsharded collections. Clients should never connect to a single shard to perform read or write operations.

.. include:: /includes/fact-direct-shard-ddls-ops.rst

.. include:: /images/sharded-cluster-mixed.rst

You can connect to a :binary:`~bin.mongos` the same way you connect to a :binary:`~bin.mongod` using the :binary:`~bin.mongosh` or a MongoDB :driver:`driver </>`.

> **Note:** .. include:: /includes/fact-cannot-connect-directly-to-shards.rst

## Sharding Strategy

MongoDB supports two sharding strategies for distributing data across `sharded clusters<sharded cluster>`.

### Hashed Sharding

Hashed Sharding computes a hash of the shard key field's value. Each `chunk` is then assigned a range based on the hashed shard key values.

.. include:: /includes/tip-applications-do-not-need-to-compute-hashes.rst

.. include:: /images/sharding-hash-based.rst

Hashed values are unlikely to share the same `chunk`, providing more even data distribution, especially for shard keys that change `monotonically<shard-key-monotonic>`.

However, hashed distribution means that range-based queries on the shard key are less likely to target a single shard, resulting in more cluster-wide `broadcast operations<sharding-mongos-broadcast>`.

See `/core/hashed-sharding` for more information.

### Ranged Sharding

Ranged sharding divides data into ranges based on the shard key values, with each `chunk` assigned one of those ranges.

.. include:: /images/sharding-range-based.rst

A range of shard keys whose values are "close" are more likely to reside on the same `chunk`. This allows for `targeted operations<sharding-mongos-targeted>` as a :binary:`~bin.mongos` can route the operations to only the shards that contain the required data.

The efficiency of ranged sharding depends on the shard key chosen. Poorly considered shard keys can result in uneven distribution of data, which can negate some benefits of sharding or can cause performance bottlenecks. See `shard key selection for range-based sharding<sharding-ranged-shard-key>`.

See `/core/ranged-sharding` for more information.

## Zones in Sharded Clusters

Zones improve the locality of data for sharded clusters that span multiple data centers.

.. include:: /includes/intro-zone-sharding.rst

Each zone covers one or more ranges of `shard key` values. Each range a zone covers is always inclusive of its lower boundary and exclusive of its upper boundary.

.. include:: /images/sharded-cluster-zones.rst

You must use fields contained in the `shard key` when defining a new range for a zone to cover. If using a `compound <compound index>` shard key, the range must include the prefix of the shard key. See `shard keys in zones <zone-sharding-shard-key>` for more information.

Consider potential future zone use when choosing a shard key.

> **Tip:** Setting up zones and zone ranges before you shard an empty or a
non-existing collection allows for a faster setup of zoned sharding.

See `zones <zone-sharding>` for more information.

## Collations in Sharding

Use the :dbcommand:`shardCollection` command with the `collation : { locale : "simple" }` option to shard a collection which has a `default collation <collation>`. Successful sharding requires that:

- The collection must have an index whose prefix is the shard key
- The index must have the collation `{ locale: "simple" }`
When creating new collections with a collation, ensure these conditions are met before sharding the collection.

.. include:: /includes/note-sharding-collation.rst

See :dbcommand:`shardCollection` for more information about sharding and collation.

## Change Streams

`Change streams <changeStreams>` are available for replica sets and sharded clusters. Change streams allow applications to access real-time data changes without the complexity and risk of tailing the oplog.

## Transactions

`Distributed transactions <transactions>` support multi-document transactions on sharded clusters.

.. include:: /includes/extracts/transactions-committed-visibility.rst

## Learn More

### Practical MongoDB Aggregations E-Book

For more information on how sharding works with `aggregations <aggregation-pipeline>`, read the sharding chapter in the [Practical MongoDB Aggregations](https://www.practical-mongodb-aggregations.com/guides/sharding.html)_ e-book.

### Additional Information

- `/core/transactions`
- `/core/transactions-production-consideration`
- `/core/transactions-sharded-clusters`
