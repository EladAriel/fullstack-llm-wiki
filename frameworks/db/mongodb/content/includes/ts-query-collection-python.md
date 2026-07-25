---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/ts-query-collection-python.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

You query a time series collection the same way you query a standard MongoDB collection.

To return one document from a time series collection, you can use the `find_one()` method. This returns a `cursor <cursors>`.

The following example uses `"_id": 0 in the query to omit the id` field from the results:

The `find_one()` method returns a single document that matches the query:

For more information on querying your collection, see :languages:`MongoDB PyMongo Driver documentation </python/pymongo-driver/current/crud/query/>`.

> **Tip:** To learn how to optimize queries on your time series collection, see
`tsc-best-practice-optimize-query-performance`.
