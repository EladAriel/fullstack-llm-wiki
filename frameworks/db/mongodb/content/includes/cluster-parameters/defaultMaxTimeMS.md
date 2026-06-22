---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/cluster-parameters/defaultMaxTimeMS.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Specifies a default time limit in milliseconds for individual read operations to complete. If a query specifies a :method:`~cursor.maxTimeMS()` option, that value overrides the `defaultMaxTimeMS` value.

`defaultMaxTimeMS` applies to the following read operations:

- :dbcommand:`aggregate` (except :pipeline:`$merge` and :pipeline:`$out`
stages)

- :dbcommand:`count`
- :dbcommand:`dbHash`
- :dbcommand:`distinct`
- :dbcommand:`find`
