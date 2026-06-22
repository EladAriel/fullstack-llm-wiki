---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/create-2dsphere-index.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

To create a `2dsphere` index, use the :method:`db.collection.createIndex()` method and specify the string literal `"2dsphere"` as the index type:

```javascript
db.collection.createIndex( { <location field> : "2dsphere" } )
```

where the `<location field>` is a field whose value is either a `GeoJSON object <geospatial-geojson>` or a `legacy coordinates pair <geospatial-legacy>`.

> **Note:** If you try to create an index on a field that contains an array of
geoJSON points, the index build fails and returns the following error:
`MongoServerError: Index build failed`
