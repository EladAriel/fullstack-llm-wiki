---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/create-2d-index.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

To create a `2d` index, use the :method:`db.collection.createIndex()` method, specifying the location field as the key and the string literal `"2d"` as the index type:

```javascript
db.collection.createIndex( { <location field> : "2d" } )
```

where the `<location field>` is a field whose value is a `legacy coordinates pair <geospatial-legacy>`.
