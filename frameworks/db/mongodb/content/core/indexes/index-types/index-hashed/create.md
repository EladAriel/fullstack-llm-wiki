---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/index-hashed/create.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================

# Create a Hashed Index

To enable sharding for a collection that already contains data, you must create an index that supports the shard key. To enable sharding for an empty collection, you can instead specify the shard key index when you `shard the collection <sharding-shard-key-creation>`.

Hashed indexes support `hashed sharding <sharding-hashed>`, where data is distributed across shards based on the hashes of shard key values.

To create a single-field hashed index, specify `hashed` as the value of the index key:

```javascript
db.<collection>.createIndex(
   {
      <field>: "hashed"
   }
)
```

To create a hashed index that contains multiple fields (a compound hashed index), specify `hashed` as the value of a single index key. For other index keys, specify the sort order (`1` or `-1`):

```javascript
db.<collection>.createIndex(
   {
      <field1>: "hashed",
      <field2>: "<sort order>",
      <field3>: "<sort order>",
      ...
   }
)
```

## About this Task

.. include:: /includes/indexes/hashed-sharding-use-cases.rst

### Choose a Hashed Shard Key

Consider the following guidelines for your hashed shard key:

- The field you choose for your hashed shard key should have a high
`cardinality <shard-key-range>`, meaning a large number of different values.

- If your data model does not contain a single field with high
cardinality, consider creating a `compound hashed index <compound-hashed-index-example>`. A compound hashed index provides more unique indexed values and can increase cardinality.

- Your shard key should support common query patterns. Range queries
(like :query:`$gt` and :query:`$lt`) cannot use a hashed index. If your application often performs range queries on the fields included in your shard key, consider range-based sharding instead.

A hashed index can contain up to 32 fields.

## Before You Begin

To implement hashed sharding, you must `deploy a sharded cluster <sharding-procedure-setup>`.

## Examples

The following examples show you how to:

- `single-hashed-index-example`
- `compound-hashed-index-example`
### Create a Single-Field Hashed Index

Consider an `orders` collection that already contains data. Create a hashed index in the `orders collection on the id` field:

```javascript
db.orders.createIndex( { _id: "hashed" } )
```

The `_id field increases monotonically, which makes it a good candidate for a hashed index key. Although id values incrementally increase, when MongoDB generates a hash for individual id` values, those hashed values are unlikely to be on the same `chunk`.

After you create the index, you can shard the `orders` collection:

```javascript
sh.shardCollection(
   "<database>.orders",
   { _id: "hashed" }
)
```

### Create a Compound Hashed Index

Consider a `customers` collection that already contains data. Create a compound hashed index in the `customers` collection on the `name`, `address`, and `birthday` fields:

```javascript
db.customers.createIndex(
   {
      "name" : 1
      "address" : "hashed",
      "birthday" : -1
   }
)
```

When you create a compound hashed index, you must specify `hashed` as the value of a single index key. For other index keys, specify the sort order (`1` or `-1`). In the preceding index, `address` is the hashed field.

After you create the index, you can shard the `customers` collection:

```javascript
sh.shardCollection(
   "<database>.customers",
   {
      "name" : 1
      "address" : "hashed",
      "birthday" : -1
   }
)
```

## Learn More

- `sharding-hashed`
- `sharding-shard-key-selection`
- `hashed-versus-ranged-sharding`
- `sharding-procedure-setup`
