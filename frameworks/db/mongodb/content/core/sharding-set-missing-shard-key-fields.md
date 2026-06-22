---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/sharding-set-missing-shard-key-fields.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# Set Missing Shard Key Fields

## Chunk Range and Missing Shard Key Fields

Missing shard key fields fall within the same chunk range as shard keys with null values. For example, if the shard key is on the fields `{ x: 1, y: 1 }`, then:

## Read/Write Operations and Missing Shard Key Fields

To target documents with missing shard key fields, you can use the :query:`{ $exists: false } <$exists>` filter condition on the shard key fields. For example, if the shard key is on the fields `{ x: 1, y: 1 }`, you can find the documents with missing shard key fields by running this query:

```javascript
db.shardedcollection.find( { $or: [ { x: { $exists: false } }, { y: { $exists: false } } ] } )
```

If you specify a `null equality match </tutorial/query-for-null-fields>` filter condition (e.g. `{ x: null }`), the filter matches :red:`both` those documents with missing shard key fields :red:`and` those with shard key fields set to `null`.

Some write operations, such as a write with an `upsert` specification, require an equality match on the shard key. In those cases, to target a document that is missing the shard key, include another filter condition in addition to the `null` equality match. For example:

```javascript
{ _id: <value>, <shardkeyfield>: null } // _id of the document missing shard key
```

## Set the Missing Shard Key Fields

If you have missing shard key fields, you can set the shard key field to `null`. If you want to set the missing shard key field to a non-`null` value, see `update-shard-key`.

To perform the update, you can use the following operations on a :binary:`~bin.mongos`:

## Example

Consider a `sales` collection which is sharded on the `location` field. Some documents in the collection have no `location` field. A missing field is considered the same as a null value for the field. To explicitly set these fields to `null`, run the following command:

```javascript
db.sales.updateOne(
  { _id: 12345, location: null },
  { $set: { location: null } }
)
```

When setting missing shard key fields with :method:`db.collection.updateOne()` or another method that explicitly updates only one document, the update **must** meet one of the following requirements:

- the filter of the query contains an equality condition on the full
shard key in the query

- the filter of the query contains an exact match on _id
- the update targets a single Shard
