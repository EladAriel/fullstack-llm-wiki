---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.shardAndDistributeCollection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================================

# sh.shardAndDistributeCollection() (mongosh method)

## Definition

## Parameters

`sh.shardAndDistributeCollection()` takes the following parameters:

The `options` argument supports the following options:

## Considerations

The following factors can impact performance or the distribution of your data.

### Shard Keys

Although you can `change your shard key <change-a-shard-key>` later, carefully consider your shard key choice to optimize scalability and perfomance.

Shard Keys on Time Series Collections `````````````````````````````````````

.. include:: /includes/time-series/fact-shard-key-limitations.rst

> **Seealso:** - `sharding-shard-key`
- `sharding-shard-key-selection`

### Hashed Shard Keys

`Hashed shard keys <sharding-hashed-sharding>` use a `hashed index <index-type-hashed>` or a `compound hashed index <index-type-compound-hashed>` as the shard key.

To specify a hashed shard key field, use `field: "hashed"` .

.. include:: /includes/note-hashed-shard-key-during-chunk-migration.rst

> **Seealso:** `sharding-hashed`

### Zone Sharding and Initial Chunk Distribution

.. include:: /includes/extracts/zoned-sharding-shard-operation-chunk-distribution-with-links.rst

For an example, see `pre-define-zone-range-example`. If sharding a collection using a ranged or single-field hashed shard key, the `numInitialChunks` option has no effect if zones and zone ranges have been defined for the empty collection.

To shard a collection using a `compound hashed index <index-type-compound-hashed>`, see `sh.shardCollection-zones-compound-hashed`.

Initial Chunk Distribution with Compound Hashed Indexes ```````````````````````````````````````````````````````

.. include:: /includes/extracts/zoned-sharding-shard-operation-chunk-distribution-hashed-short.rst

The `numInitialChunks` option has no effect if zones and zone ranges have been defined for the empty collection and `presplitHashedZones <method-shard-collection-presplitHashedZones>` is `false`.

For an example, see `pre-define-zone-range-hashed-example`.

> **Seealso:** `initial-ranges`

### Uniqueness

If you specify `unique: true`, you must create the index before using `sh.shardAndDistributeCollection()`.

Although you can have a unique `compound index` where the shard key is a `prefix <compound-index-prefix>`, if you use the `unique` parameter, the collection must have a unique index that is on the shard key.

> **Seealso:** `Sharded Collection and Unique Indexes <sharding-shard-key-unique>`

.. include:: /includes/fact-shardCollection-collation.rst

### Write Concern

.. include:: /includes/extracts/mongos-operations-wc-shard-collection.rst

## Examples

The following examples show how you can use the `sh.shardAndDistributeCollection()` method with or without optional parameters.

### Simple Usage

A database named `records` contains a collection named `people`. The following command shards the collection by the `zipcode` field and immediately redistributes the data in the `records.people` collection:

```javascript
sh.shardAndDistributeCollection("records.people", { zipcode: 1 } )
```

### Usage with Options

The `phonebook` database has a `contacts` collection with no default `collation <createCollection-collation-example>`. The following example uses `sh.shardAndDistributeCollection()` to shard and redistribute the `phonebook.contacts` collection with:

- A `Hashed shard key <sharding-hashed-sharding>` on the
`last_name` field.

- `5` initial chunks.
- `simple` collation.
```javascript
sh.shardAndDistributeCollection(
  "phonebook.contacts",
  { last_name: "hashed" },
  false,
  {
    numInitialChunks: 5,
    collation: { locale: "simple" }
  }
)
```

## Learn More

- :dbcommand:`reshardCollection`
- :method:`sh.balancerCollectionStatus()`
- :dbcommand:`shardCollection`
- `sharding-background`
