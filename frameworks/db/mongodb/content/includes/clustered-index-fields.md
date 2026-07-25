---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/clustered-index-fields.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 5.3, you can create a collection with a **clustered index**. Clustered indexes are stored in the same `WiredTiger <storage-wiredtiger>` file as the collection. The resulting collection is called a `clustered collection <clustered-collections>`.

The `clusteredIndex` field has the following syntax:

```javascript
clusteredIndex: {
   key: <object>,
   unique: <boolean>,
   name: <string>
}
```

`key` Required. The clustered index key field. Must be set to `{ _id: 1 }. The default value for the id` field is an automatically generated unique `object identifier <objectid>`, but you can set your own `clustered index key values <clustered-collections-clustered-index-key-values>`.

`unique` Required. Must be set to `true`. A unique index indicates the collection will not accept inserted or updated documents where the clustered index key value matches an existing value in the index.

`name` Optional. A name that uniquely identifies the clustered index.

.. versionadded:: 5.3
