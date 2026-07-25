---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/ts-query-collection-mongosh.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

You query a time series collection the same way you query a standard MongoDB collection.

To return one document from a time series collection, you can use the :method:`db.collection.findOne()` method. The following example uses the `projection field in the query to omit the id` field from the returned documents:

For more information on time series queries, see `tsc-best-practice-optimize-query-performance`.
