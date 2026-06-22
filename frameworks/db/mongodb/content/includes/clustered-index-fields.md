---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/clustered-index-fields.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
