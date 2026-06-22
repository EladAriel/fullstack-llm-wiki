---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/shardCollection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# shardCollection (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

.. include:: /includes/fact-dbcommand.rst

The command has the following form:

```javascript
db.adminCommand(
   {
     shardCollection: "<database>.<collection>",
     key: { <field1>: <1|"hashed">, ... },
     unique: <boolean>,
     presplitHashedZones: <boolean>,
     collation: { locale: "simple" },
     timeseries: <object>
   }
 )
```

> **Note:** .. versionchanged:: 6.0
Starting in MongoDB 6.0, sharding a collection does **not** require you to
first run the :dbcommand:`enableSharding` command to configure the database.

## Command Fields

The command takes the following fields:

### Time Series Options

.. versionadded:: 5.1

To create a new `time series collection <manual-timeseries-collection>` that is sharded, specify the `timeseries <cmd-shard-collection-timeseries>` option to :dbcommand:`shardCollection`.

The `timeseries <cmd-shard-collection-timeseries>` option takes the following fields:

## Considerations

### Shard Keys

While you can `change your shard key <change-a-shard-key>` later, it is important to carefully consider your shard key choice to avoid scalability and perfomance issues.

> **Seealso:** - `sharding-shard-key-selection`
- `sharding-shard-key`

Shard Keys on Time Series Collections `````````````````````````````````````

.. include:: /includes/time-series/fact-shard-key-limitations.rst

.. include:: /includes/time-series/timeseries-timeField-deprecated.rst

### Hashed Shard Keys

`Hashed shard keys <sharding-hashed-sharding>` use a `hashed index <index-type-hashed>` or a `compound hashed index <index-type-compound-hashed>` as the shard key.

Use the form `field: "hashed"` to specify a hashed shard key field.

.. include:: /includes/note-hashed-shard-key-during-chunk-migration.rst

> **Seealso:** `/core/hashed-sharding`

### Reshard to Balance

.. include:: /includes/fact-reshard-init-shard

### Zone Sharding and Initial Chunk Distribution

.. include:: /includes/extracts/zoned-sharding-shard-operation-chunk-distribution-with-links.rst

To shard a collection using a `compound hashed index <index-type-compound-hashed>`, see `shardCollection-zones-compound-hashed`.

Zone Sharding and Compound Hashed Indexes `````````````````````````````````````````

.. include:: /includes/extracts/zoned-sharding-shard-operation-chunk-distribution-hashed-short.rst

See `pre-define-zone-range-hashed-example` for an example.

> **Seealso:** - `initial-chunks`
- :dbcommand:`balancerCollectionStatus`

### Uniqueness

If specifying `unique: true`:

.. include:: /includes/extracts/shard-collection-unique-restriction-command.rst

See also `Sharded Collection and Unique Indexes <sharding-shard-key-unique>`

.. include:: /includes/fact-shardCollection-collation.rst

### Write Concern

.. include:: /includes/extracts/mongos-operations-wc-shard-collection.rst

## Example

The following operation enables sharding for the `people` collection in the `records` database and uses the `zipcode` field as the `shard key <shard-key>`:

```javascript
db.adminCommand( { shardCollection: "records.people", key: { zipcode: 1 } } )
```

## Learn More

- :dbcommand:`refineCollectionShardKey`
- :method:`sh.balancerCollectionStatus()`
- :method:`sh.shardCollection()`
- `/sharding`
- `reshard-to-same-key`
