---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/create-indexes-stable-api-compatibility.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

When using `Stable API <stable-api>` V1:

- You cannot specify any of the following fields in the |paramName|:
- `background`
- `bucketSize`
- `sparse`
- `storageEngine`
- You cannot create `text <index-type-text>` indexes.
- The above unsupported index types are ignored by the
`query planner<query-plans-query-optimization>` in `strict mode<stable-api-strict-client>`. For example, attempting to use a `sparse` index with :method:`cursor.hint()` will result in the following `BadValue` error:

```
  planner returned error :: caused by :: hint provided does not 
  correspond to an existing index
```
