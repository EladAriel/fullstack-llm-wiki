---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/refineCollectionShardKey.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================================

# refineCollectionShardKey (database command)

## Definition

> **Note:** As part of refining the shard key, the
:dbcommand:`refineCollectionShardKey` command updates the
`chunk ranges <sharding-data-partitioning>` and
`zone ranges <zone-sharding>` to incorporate the new
fields without modifying the range values of the existing key
fields. That is, the refinement of the shard key does not
immediately affect the distribution of chunks across shards or
zones. Any future chunk splits or migration occur as part of the
routine sharding operations.

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-m10.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

> **Note:** To use the :dbcommand:`refineCollectionShardKey` command, the sharded
cluster must have `feature compatibility version (fcv) <view-fcv>`
of `4.4`.

The command has the following syntax:

```javascript
db.adminCommand( 
   { 
     refineCollectionShardKey: "<database>.<collection>", 
     key: { <existing key specification>, <suffix1>: <1|"hashed">, ... }
   } 
)
```

## Command Fields

The command takes the following fields:

> **Seealso:** `/core/sharding-shard-key`

## Access Control

When running with access control, the user must have the :authaction:`refineCollectionShardKey` privilege actions on `database and/or collection <resource-specific-db-and-or-collection>` to run the command. That is, a user must have a `role <roles>` that grants the following `privilege <privileges>`:

```javascript
{ resource: { db: <database>, collection: <collection> }, actions: [ "refineCollectionShardKey" ] }
```

The built-in :authrole:`clusterManager` role provides the appropriate privileges.

## Considerations

### Index Considerations

- Index Existence
An index that supports the command's specified `key <refineCollectionShardKey-key>` must exist :red:`prior` to running the command.

A supporting index is an index that starts with the new shard key specification; i.e. the `index prefix <compound-index-prefix>` matches the new shard key specification. That is, to change the shard key to `{ x: 1, y: 1 }` from `{ x: 1 }`, and index that starts with `{ x: 1, y: 1 }` must exist; e.g.

- `{ x: 1, y: 1 }`
- `{ x: 1, y: 1, a: 1, b: 1}`
> **Note:**       - The supporting index cannot be a `partial index <index-type-partial>`.
      - The supporting index cannot be a `sparse index <index-type-sparse>`.
      - If the collection uses a non-`simple` collation, the supporting
        index must specify `{ locale: "simple" }` collation.

- Unique Index
If the current shard index has a `uniqueness constraint </core/index-unique>`, the new shard key index must also have a unique constraint.

| After creating the unique index to support the new shard key, **drop** the old shard key index :red:`before` running :dbcommand:`refineCollectionShardKey`.

| Also, if the current shard index has a `unique constraint </core/index-unique>`, then the new shard key cannot specify `"hashed"` for any of its fields.

| See also `Sharded Collection and Unique Indexes <sharding-shard-key-unique>`.

- Index Collation
If the sharded collection has a non-`simple` default `collation <collation>`, then the index must include a collation document with `{ locale : "simple" }`. At least one of the indexes whose fields support the shard key pattern must have the simple collation.

.. include:: /includes/refine-shard-key-index-type.rst

## Examples

To set up the example in the `test` database:

#. Use following :dbcommand:`shardCollection` operation to shard the `orders` collection in the `test` database. The operation uses the `customer_id` field as the initial `shard key <shard-key>`:

```javascript
   db.adminCommand( { shardCollection: "test.orders", key: { customer_id: 1 } } )
```

To modify the shard key to be the `customer_id` field and the `order_id` field `{ customer_id: 1, order_id: 1 }`,

#. :method:`Create the index <db.collection.createIndex()>` to support the new shard key if the index does not already exist.

```javascript
   db.getSiblingDB("test").orders.createIndex( { customer_id: 1, order_id: 1 } )
```

#. Run :dbcommand:`refineCollectionShardKey` command to add the `order_id` field as a suffix:

```javascript
   db.adminCommand( { 
      refineCollectionShardKey: "test.orders", 
      key: { customer_id: 1, order_id: 1 }
   } )
```

Upon successful completion of the command, the shard key for the collection has changed to `{ customer_id: 1, order_id: 1 }`. To verify, you can run :method:`sh.status()`.

> **Tip:** After you refine the shard key, it may be that not all documents in
the collection have the suffix field(s). To populate the missing
shard key field(s), see `shard-key-missing`.
Before refining the shard key, ensure that all or most documents in
the collection have the suffix fields, if possible, to avoid having
to populate the field afterwards.

### Collection with non-`simple` Collation

To set up the example in the `test` database:

#. Create the `cafés` collection in the `test` database, specifying French `fr` as the default collation.

```javascript
   db.getSiblingDB("test").createCollection( "cafés", { collation: { locale: "fr" } } );
```

#. Shard the collection using `customer_id` field as the initial `shard key <shard-key>`. Because the collection has a default `fr` collation and not a `simple` collation, the :dbcommand:`shardCollection` command must include a `collation: { locale: "simple" }` option:

```javascript
   db.adminCommand( { 
      shardCollection: "test.cafés", 
      key: { customer_id: 1 },
      collation: { locale: "simple" } 
   } )
```

To modify the shard key to be both the `customer_id` field and the `order_id` field `{ customer_id: 1, order_id: 1 }`,

#. :method:`Create the index <db.collection.createIndex()>` to support the new shard key if the index does not already exist. Because the collection uses a non-simple collation, the index must include the `collation: { locale: "simple" }` option.

```javascript
   db.getSiblingDB("test").cafés.createIndex( 
      { customer_id: 1, order_id: 1 }, 
      { collation: { locale: "simple" } } 
   )
```

#. Run :dbcommand:`refineCollectionShardKey` command to add the `order_id` field as a suffix:

```javascript
   db.adminCommand( { 
      refineCollectionShardKey: "test.cafés",
      key: { customer_id: 1, order_id: 1 } 
   } )
```

Upon successful completion of the command, the shard key for the collection has changed to `{ customer_id: 1, order_id: 1 }`. To verify, you can run :method:`sh.status()`.

> **Tip:** After you refine the shard key, it may be that not all documents in
the collection have the suffix field(s). To populate the missing
shard key field(s), see `shard-key-missing`.
Before refining the shard key, ensure that all or most documents in
the collection have the suffix fields, if possible, to avoid having
to populate the field afterwards.

> **Seealso:** `/core/sharding-shard-key/`
