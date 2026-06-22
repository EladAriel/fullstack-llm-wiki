---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-2dsphere-index-limitations.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

To generate keys for a 2dsphere index, :binary:`mongod` maps `GeoJSON shapes <geospatial-indexes-store-geojson>` to an internal representation. The resulting internal representation may be a large array of values.

When :binary:`mongod` generates index keys on a field that holds an array, :binary:`mongod` generates an index key for each array element. For compound indexes, :binary:`mongod` calculates the `cartesian product` of the sets of keys that are generated for each field. If both sets are large, then calculating the cartesian product could cause the operation to exceed memory limits.

:parameter:`indexMaxNumGeneratedKeysPerDocument` limits the maximum number of keys generated for a single document to prevent out of memory errors. The default is 100000 index keys per document. It is possible to raise the limit, but if an operation requires more keys than the :parameter:`indexMaxNumGeneratedKeysPerDocument` parameter specifies, the operation will fail.
