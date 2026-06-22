---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.shardCollection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================================

# sh.shardCollection() (mongosh method)

## Definition

### Time Series Options

.. versionadded:: 5.1

To create a new `time series collection <manual-timeseries-collection>` that is sharded, specify the `timeseries <cmd-shard-collection-timeseries>` option to :method:`sh.shardCollection()`.

The `timeseries <cmd-shard-collection-timeseries>` option takes the following fields:

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Considerations

### Shard Keys

While you can `change your shard key <change-a-shard-key>` later, it is important to carefully consider your shard key choice to avoid scalability and perfomance issues.

Shard Keys on Time Series Collections `````````````````````````````````````

.. include:: /includes/time-series/fact-shard-key-limitations.rst

> **Seealso:** - `sharding-shard-key`
- `sharding-shard-key-selection`

### Hashed Shard Keys

`Hashed shard keys <sharding-hashed-sharding>` use a `hashed index <index-type-hashed>` or  a `compound hashed index <index-type-compound-hashed>` as the shard key.

Use the form `field: "hashed"` to specify a hashed shard key field.

.. include:: /includes/note-hashed-shard-key-during-chunk-migration.rst

> **Seealso:** `/core/hashed-sharding`

### Zone Sharding and Initial Chunk Distribution

.. include:: /includes/extracts/zoned-sharding-shard-operation-chunk-distribution-with-links.rst

To shard a collection using a `compound hashed index <index-type-compound-hashed>`, see `sh.shardCollection-zones-compound-hashed`.

Initial Chunk Distribution with Compound Hashed Indexes ```````````````````````````````````````````````````````

.. include:: /includes/extracts/zoned-sharding-shard-operation-chunk-distribution-hashed-short.rst

See `pre-define-zone-range-hashed-example` for an example.

> **Seealso:** `initial-ranges`

### Uniqueness

If specifying `unique: true`:

.. include:: /includes/extracts/shard-collection-unique-restriction-method.rst

See also `Sharded Collection and Unique Indexes <sharding-shard-key-unique>`

.. include:: /includes/fact-shardCollection-collation.rst

### Write Concern

.. include:: /includes/extracts/mongos-operations-wc-shard-collection.rst

### Reshard to Balance

.. include:: /includes/fact-reshard-init-shard-mongosh

## Examples

### Simple Usage

Given a collection named `people` in a database named `records`, the following command shards the collection by the `zipcode` field:

```javascript
sh.shardCollection("records.people", { zipcode: 1 } )
```

### Usage with Options

The `phonebook` database has a collection `contacts` with no default `collation <createCollection-collation-example>`. The following example uses :method:`sh.shardCollection()` to shard the `phonebook.contacts` with:

- a `hashed shard key <sharding-hashed-sharding>` on the
`last_name` field,

- `5` initial chunks, and
- a collation of `simple`.
```javascript
sh.shardCollection(
  "phonebook.contacts",
  { last_name: "hashed" },
  false,
  {
    collation: { locale: "simple" }
  }
)
```

> **Seealso:** - :dbcommand:`refineCollectionShardKey`
- :method:`sh.balancerCollectionStatus()`
- :dbcommand:`shardCollection`
- `/sharding`
