---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.updateZoneKeyRange.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================================

# sh.updateZoneKeyRange() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

You cannot create a range of shard key values whose lower and upper boundaries overlap with an existing range for the sharded collection. For example, given an existing range of `1` to `10`, you cannot create a new range of `5` to `20`, as the new range would overlap with the existing range.

A zone can have multiple ranges of data associated with it, but a range can at most be associated with a single zone.

See the `zone <zone-sharding>` manual page for more information on zones in sharded clusters.

### Initial Chunk Distribution for Empty or Non-Existing Collections

If you are considering performing `zone sharding <zone-sharding>` on an empty or non-existent collection, use :method:`sh.updateZoneKeyRange()` to create the zones and zone ranges before sharding the collection (since 4.0.2). Starting in version 4.0.3, creating zones and zone ranges on empty or non-existing collections allows MongoDB to optimize the initial chunk creation and distribution process when sharding the collection. This optimized process supports faster setup of zoned sharding with less balancer overhead than creating zones after sharding. The `balancer <sharding-balancing>` performs all chunk management after the optimized initial chunk creation and distribution.

For an example of defining zones and zone ranges for initial chunk distribution, see `pre-define-zone-range-example`.

Initial Chunk Distribution with Compound Hashed Shard Keys ``````````````````````````````````````````````````````````

MongoDB supports sharding collections on `compound hashed indexes <index-type-compound-hashed>`. MongoDB can perform optimized initial chunk creation and distribution when sharding the empty or non-existing collection on a compound hashed shard key.

For a more complete example of defining zones and zone ranges for initial chunk distribution on a compound hashed shard key, see `pre-define-zone-range-hashed-example`.

> **Seealso:** :method:`sh.balancerCollectionStatus()`

### Balancer

After associating a range to a zone, the `balancer <sharding-balancing-internals>` must first run in order to migrate any chunks whose ranges are covered by the zone to shards inside of that zone. Until balancing completes, some chunks may reside on the wrong shard given the configured zones for the sharded cluster. See `zone-sharding-balancer` for more information.

See the `sharded cluster balancer <sharding-balancing>` manual page for more information on how migrations work in a sharded cluster.

### Bounds

.. include:: /includes/fact-shard-ranges-inclusive-exclusive.rst

### Dropped Collections

.. include:: /includes/extracts/zoned-sharding-drop-collection-change.rst

In earlier versions, MongoDB does not remove the tag associations for a dropped collection, and if you later create a new collection with the same name, the old tag associations will apply to the new collection.

### Security

For sharded clusters running with `authentication <authentication>`, you must authenticate as either:

- a user whose privileges include the specified actions on various
collections in the `config` database:

- :authaction:`find` on the `config.shards` collection
- :authaction:`find` and :authaction:`update` on the `config.tags`
collection;

or, alternatively,

- a user whose privileges include :authaction:`enableSharding` on the
`cluster <resource-specific-collection>` resource.

The :authrole:`clusterAdmin` or :authrole:`clusterManager` built-in roles have the appropriate permissions for issuing :method:`sh.updateZoneKeyRange()`. See the documentation page for `Role-Based Access Control <authorization>` for more information.

## Examples

Given a sharded collection `exampledb.collection` with a shard key of `{ a : 1 }`, the following operation creates a range with a lower bound of `1` and an upper bound of `10` on the `alpha` zone:

```javascript
sh.updateZoneKeyRange(
   "exampledb.collection",
   { a : 1 },
   { a : 10 },
   "alpha"
)
```

The following operation removes the previously created range by passing `null` to the `zone` field.

```javascript
sh.updateZoneKeyRange( 
   "exampledb.collection",
   { a : 1 },
   { a : 10 },
   null
)
```

The `min` and `max` must match exactly the bounds of the target range. The following operation attempts to remove the previously created range, but specifies `{ a : 0 }` as the `min` bound:

```javascript
sh.updateZoneKeyRange(
   "exampledb.collection",
   { a : 0 },
   { a : 10 },
   null
)
```

While the range of `{ a : 0 }` and `{ a : 10 }` encompasses the existing range, it is not an exact match and therefore :dbcommand:`updateZoneKeyRange` does not remove anything.

### Compound Shard Key

Given a sharded collection `exampledb.collection` with a shard key of `{ a : 1, b : 1 }`, the following operation creates a range covering the lower bound of `{ a: 1, b : 1 }` and an upper bound of `{ a : 10, b : 10}` and associates it with the `alpha` zone:

```javascript
sh.updateZoneKeyRange(
   "exampledb.collection",
   { a : 1, b : 1 },
   { a : 10, b : 10 },
   "alpha"
)
```

### Pre-Define Zones and Zone Ranges for an Empty or Non-Existing Collection

If you create zones and zone ranges on empty or non-existing collections, MongoDB may optimize the initial chunk creation and distribution process when sharding the collection. This optimized process supports faster setup of zoned sharding with less balancer overhead than creating zones after sharding. The `balancer <sharding-balancing>` performs all chunk management after the optimized initial chunk creation and distribution. For more information, see `updateZoneKeyRange-method-init-chunk-distribution-compound-hashed` for more information.

The sections below contain examples for three different shard key types.

Consider the following examples, which explore pre-defining zones or zone ranges for three different shard key types:

- `updatezonekeyrange-single-or-compound-example`
- `updatezonekeyrange-compound-prefix-hashed-example`
- `updatezonekeyrange-compound-non-prefix-hashed-example`
Single or Compound Shard Keys `````````````````````````````

> **Note:** This example only applies to single-field or compound shard keys
without a hashed field.
For example, `{ "zip" : 1 }` or
`{ "zip" : 1, "account" : 1}`

.. include:: /includes/steps/zones-initial-chunk-distribution-single-compound.rst

Compound Hashed Shard Key with Hashed Prefix ````````````````````````````````````````````

> **Note:** This example only applies to compound hashed shard keys where the
hashed field is the prefix of the shard key (i.e. the first field in
the shard key is hashed).
For example, `{ "_id" : "hashed", "facility" : 1 }`

MongoDB supports sharding collections on `compound hashed indexes <index-type-compound-hashed>`. When sharding on a compound hashed shard key, MongoDB can perform optimized initial chunk creation and distribution on the empty or non-existing collection only if the defined zone ranges meet `additional requirements <updateZoneKeyRange-method-init-chunk-distribution>`.

Consider an empty collection `examples.metrics` which will store analytics from one of two manufacturing facilities. The planned shard key is `{ "_id" : "hashed", "facility" : 1}`, where the hashed field is the shard key prefix.

.. include:: /includes/steps/zones-initial-chunk-distribution-compound-hashed-prefix.rst

Compound Hashed Shard Key with Non-Prefix Hashed Field ``````````````````````````````````````````````````````

> **Note:** This example only applies to compound hashed shard keys where the
hashed field is not the prefix of the shard key (i.e. the first
field in the shard key is not hashed).
For example, `{ "facility" : 1, "_id" : "hashed" }`

MongoDB supports sharding collections on `compound hashed indexes <index-type-compound-hashed>`. When sharding on a compound hashed shard key, MongoDB can perform optimized initial chunk creation and distribution on the empty or non-existing collection only if the defined zone ranges meet `additional requirements <updateZoneKeyRange-method-init-chunk-distribution>`.

Consider an empty collection `examples.metrics` which will store analytics from one of two manufacturing facilities. The planned shard key is `{ "facility" : 1, "_id" : "hashed" }`, where the hashed field is not the shard key prefix.

- The `facility` field stores the name of the facility:
`"FacilityAlpha"` or `"FacilityBaker"`.  The collection requires zone ranges on `facility` to help isolate data for each facility to specific shards.

- The `_id` field compensates for the low-cardinality of the
`facility field. Hashing compensates for the monotonically-increasing nature of the id` field.

.. include:: /includes/steps/zones-initial-chunk-distribution-compound-hashed-non-prefix.rst

> **Seealso:** - :method:`sh.addShardToZone()`
- :method:`sh.removeRangeFromZone()`
