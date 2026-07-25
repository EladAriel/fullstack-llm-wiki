---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/create-indexes-stable-api-compatibility.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

When using `Stable API <stable-api>` V1, all :dbcommand:`createIndexes` fields are available with the following exceptions:

- The following fields in the |paramName| are not available in
Stable API V1:

- `background`
- `bucketSize`
- `sparse`
- `storageEngine`
- `Text <index-type-text>` indexes are not available in
Stable API V1.

- The above unsupported index types are ignored by the
`query planner<query-plans-query-optimization>` in `strict mode<stable-api-strict-client>`. For example, attempting to use a `sparse` index with :method:`cursor.hint()` results in the following `BadValue` error:

```
  planner returned error :: caused by :: hint provided does not 
  correspond to an existing index
```
