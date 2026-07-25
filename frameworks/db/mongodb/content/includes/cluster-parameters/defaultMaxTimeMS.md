---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/cluster-parameters/defaultMaxTimeMS.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Specifies a default time limit in milliseconds for individual read operations to complete. If a query specifies a :method:`~cursor.maxTimeMS()` option, that value overrides the `defaultMaxTimeMS` value.

`defaultMaxTimeMS` applies to the following read operations:

- :dbcommand:`aggregate` (except :pipeline:`$merge` and :pipeline:`$out`
stages)

- :dbcommand:`count`
- :dbcommand:`dbHash`
- :dbcommand:`distinct`
- :dbcommand:`find`
