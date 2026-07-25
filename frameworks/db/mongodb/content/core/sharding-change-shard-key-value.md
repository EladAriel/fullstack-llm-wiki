---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/sharding-change-shard-key-value.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===================================

# Change a Document's Shard Key Value

You can update a document's shard key value unless the shard key field is the immutable `_id` field.

> **Important:** - You **must** be on a :binary:`~bin.mongos`. Do **not** issue the
  operation directly on the shard.
- You **must** run either in a :doc:`transaction
  </core/transactions>` or as a :doc:`retryable write
  </core/retryable-writes>`.
- You **must** include an equality condition on the full shard
  key in the query filter. For example, consider a `messages`
  collection that uses `{ activityid: 1, userid : 1 }` as the
  shard key. To update the shard key value for a document, you must
  include `activityid: <value>, userid: <value>` in the query
  filter. You can include additional fields in the query as
  appropriate.
See also the specific write command/methods for additional
operation-specific requirements when run against a sharded
collection.

To update a shard key value, use the following operations:

.. include:: /includes/shard-key-modification-warning.rst

## Example

Consider a `sales` collection which is sharded on the `location field. The collection contains a document with the id` `12345` and the `location` `""`. To update the field value for this document, you can run the following command:

```javascript
db.sales.updateOne(
  { _id: 12345, location: "" },
  { $set: { location: "New York"} }
)
```

> **Seealso:** `shard-key-missing-set`
