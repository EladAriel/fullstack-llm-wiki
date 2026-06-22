---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/hashed-sharding.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============

# Hashed Sharding

Hashed sharding uses either a `single field hashed index <index-hashed-index>` or a `compound hashed index <index-type-compound-hashed>` as the shard key to partition data across your sharded cluster.

Sharding on a Single Field Hashed Index Hashed sharding provides a more even data distribution across the sharded cluster at the cost of reducing `sharding-query-isolation`. Post-hash, documents with "close" shard key values are unlikely to be on the same chunk or shard - the :binary:`~bin.mongos` is more likely to perform `sharding-mongos-broadcast` to fulfill a given ranged query. :binary:`~bin.mongos` can target queries with equality matches to a single shard.

.. include:: /images/sharding-hash-based.rst

Sharding on a Compound Hashed Index MongoDB includes support for creating compound indexes with a single `hashed field <index-type-hashed>`. To create a compound hashed index, specify `hashed` as the value of any single index key when creating the index.

Compound hashed index compute the hash value of a single field in the compound index; this value is used along with the other fields in the index as your shard key.

Compound hashed sharding supports features like `zone sharding <zone-sharding>`, where the prefix (i.e. first) non-hashed field or fields support zone ranges while the hashed field supports more even distribution of the sharded data. Compound hashed sharding also supports shard keys with a hashed prefix for resolving data distribution issues related to `monotonically increasing fields <shard-key-monotonic>`.

.. include:: /includes/tip-applications-do-not-need-to-compute-hashes.rst

.. include:: /includes/warning-hashed-index-floating-point.rst

:binary:`~bin.mongosh` provides the  :method:`convertShardKeyToHashed()` method. This method uses the same hashing function as the hashed index and can be used to see what the hashed value would be for a key.

## Hashed Sharding Shard Key

The field you choose as your hashed shard key should have a good `cardinality<shard-key-range>`, or large number of different values. Hashed keys are ideal for shard keys with fields that change `monotonically<shard-key-monotonic>` like `ObjectId values or timestamps. A good example of this is the default id` field, assuming it only contains `ObjectId` values.

To shard a collection using a hashed shard key, see `deploy-hashed-sharded-cluster-shard-collection`.

## Hashed vs Ranged Sharding

Given a collection using a monotonically increasing value `X` as the shard key, using ranged sharding results in a distribution of incoming inserts similar to the following:

.. include:: /images/sharded-cluster-monotonic-distribution.rst

Since the value of `X` is always increasing, the chunk with an upper bound of :bsontype:`MaxKey` receives the majority incoming writes. This restricts insert operations to the single shard containing this chunk, which reduces or removes the advantage of distributed writes in a sharded cluster.

By using a hashed index on `X`, the distribution of inserts is similar to the following:

.. include:: /images/sharded-cluster-hashed-distribution.rst

Since the data is now distributed more evenly, inserts are efficiently distributed throughout the cluster.

## Shard the Collection

Use the :method:`sh.shardCollection()` method, specifying the full namespace of the collection and the target `hashed index <index-type-hashed>` to use as the `shard key`.

```javascript
sh.shardCollection( "database.collection", { <field> : "hashed" } )
```

To shard a collection on a `compound hashed index <index-type-compound-hashed>`, specify the full namespace of the collection and the target compound hashed index to use as the `shard key`:

```javascript
sh.shardCollection(
  "database.collection",
  { "fieldA" : 1, "fieldB" : 1, "fieldC" : "hashed" }
)
```

> **Important:** - Starting in MongoDB 5.0, you can :ref:`reshard a collection
  <sharding-resharding>` by changing a collection's shard key.
- You can `refine a shard key <shard-key-refine>` by adding a suffix
  field or fields to the existing shard key.

### Shard a Populated Collection

If you shard a populated collection using a hashed shard key:

- The sharding operation creates an initial chunk to cover all of the
shard key values.

- After the initial chunk creation, the balancer moves ranges of the
initial chunk when it needs to balance data.

### Shard an Empty Collection

.. include:: /includes/extracts/zoned-sharding-shard-operation-chunk-distribution.rst

Sharding Empty Collection on Single Field Hashed Shard Key

- With no `zones and zone ranges <zones-sharding>` specified
for the empty or non-existing collection:

- The sharding operation creates an empty chunk to cover the entire
range of the shard key values. Starting in version 8.0, the operation creates 1 chunk per shard by default and migrates across the cluster. This initial creation and distribution of chunks allows for faster setup of sharding.

- After the initial distribution, the balancer manages the chunk
distribution going forward.

- With zones and zone ranges specified
for the empty or a non-existing collection:

- The sharding operation creates empty chunks for the defined zone
ranges as well as any additional chunks to cover the entire range of the shard key values and performs an initial chunk distribution based on the zone ranges. This initial creation and distribution of chunks allows for faster setup of zoned sharding.

- After the initial distribution, the balancer manages the chunk
distribution going forward.

Sharding Empty Collection on Compound Hashed Shard Key with Hashed Field Prefix If the compound hashed shard key has the hashed field as the prefix (the hashed field is the first field in the shard key):

- With no zones and zone ranges specified
for the empty or non-existing collection:

- The sharding operation creates empty chunks to cover the entire
range of the shard key values and performs an initial chunk distribution. The value of all non-hashed fields is :bsontype:`MinKey` at each split point. Starting in version 8.0, the operation creates 1 chunk per shard by default and migrates across the cluster. This initial creation and distribution of chunks allows for faster setup of sharding.

- After the initial distribution, the balancer manages the chunk
distribution going forward.

- With a single zone with a
range from `MinKey` to `MaxKey` specified for the empty or a non-existing collection and the `presplitHashedZones` option specified to :method:`sh.shardCollection()`:

- The sharding operation creates empty chunks for the defined zone
range as well as any additional chunks to cover the entire range of the shard key values and performs an initial chunk distribution based on the zone ranges. This initial creation and distribution of chunks allows for faster setup of zoned sharding.

- After the initial distribution, the balancer manages the chunk
distribution going forward.

Sharding Empty Collection on Compound Hashed Shard Key with Non-Hashed Prefix If the compound hashed shard key has one or more non-hashed fields as the prefix (i.e. the hashed field is not the first field in the shard key):

- With no zones and zone ranges specified
for the empty or non-existing collection and `preSplitHashedZones <method-shard-collection-presplitHashedZones>` is `false` or omitted, MongoDB does not perform any initial chunk creation or distribution when sharding the collection.

- With no zones and zone ranges specified
for the empty or non-existing collection and `preSplitHashedZones <method-shard-collection-presplitHashedZones>`, :method:`sh.shardCollection()` / :dbcommand:`shardCollection` returns an error.

- With zones and zone ranges specified
for the empty or a non-existing collection and the `preSplitHashedZones <method-shard-collection-presplitHashedZones>` option specified to :method:`sh.shardCollection()`:

- The sharding operation creates empty chunks for the defined zone
ranges as well as any additional chunks to cover the entire range of the shard key values.

- The sharding operation further subdivides the initial chunk for
each range, such that each shard in the zone is allocated an equal number of chunks.

- This initial creation and distribution of chunks allows for
faster setup of zoned sharding. After the initial distribution, the balancer manages the chunk distribution going forward.

The defined ranges for each zone must meet certain requirements. For a description of the requirements and a complete example, see `pre-define-zone-range-hashed-example`.

### Drop a Hashed Shard Key Index

.. include:: /includes/drop-hashed-shard-key-index.rst

> **Seealso:** To learn how to deploy a sharded cluster and implement hashed
sharding, see `sharding-procedure-setup`.
