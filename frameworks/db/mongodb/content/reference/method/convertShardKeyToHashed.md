---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/convertShardKeyToHashed.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

========================================

# convertShardKeyToHashed (mongosh method)

## Description

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Example

Consider a sharded collection that uses a `hashed shard key </core/hashed-sharding>` [#populated]_

```javascript
use test

db.orders.createIndex( { _id: "hashed" } )

sh.shardCollection( "test.orders", { _id : "hashed" } )
```

If the following document exists in the collection, the hashed value of the `_id` field is used to distribute the document:

```javascript
{
  _id: ObjectId("5b2be413c06d924ab26ff9ca"),
  "item" : "Chocolates",
  "qty" : 25
}
```

To determine the hashed value of `_id` field used to distribute the document across the shards, you can use the :method:`convertShardKeyToHashed` method:

```javascript
convertShardKeyToHashed( ObjectId("5b2be413c06d924ab26ff9ca") )
```

If the collection already contains data, you must create a hashed index on the shard key before you shard the collection. For an empty collection, MongoDB creates the index as part of :method:`sh.shardCollection()`.
