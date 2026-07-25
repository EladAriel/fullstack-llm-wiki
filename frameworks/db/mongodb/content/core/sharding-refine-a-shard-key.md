---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/sharding-refine-a-shard-key.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==================

# Refine a Shard Key

Refining a collection's shard key allows for a more fine-grained data distribution and can address situations where the existing key has led to `jumbo chunks <jumbo-chunks>` due to insufficient `cardinality <shard-key-cardinality>`.

.. include:: /includes/refine-shard-key-index-type.rst

> **Note:** Starting in MongoDB 5.0, you can also :ref:`reshard your collection
<sharding-resharding>` by providing a new shard key for the
collection. To learn whether you should reshard your collection
or refine your shard key, see `change-a-shard-key`.

To refine a collection's shard key, use the :dbcommand:`refineCollectionShardKey` command. The :dbcommand:`refineCollectionShardKey` adds a suffix field or fields to the existing key to create the new shard key.

For example, you may have an existing `orders` collection in a `test` database with the shard key `{ customer_id: 1 }`. You can use the :dbcommand:`refineCollectionShardKey` command to change the shard key to the new shard key `{ customer_id: 1, order_id: 1 }`:

```javascript
db.adminCommand( {
   refineCollectionShardKey: "test.orders",
   key: { customer_id: 1, order_id: 1 }
} )
```
