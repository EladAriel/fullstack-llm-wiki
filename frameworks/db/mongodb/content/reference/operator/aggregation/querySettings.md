---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/querySettings.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# $querySettings (aggregation stage)

## Definition

.. versionadded:: 8.0

Returns query settings previously added with :dbcommand:`setQuerySettings`. The settings apply to the entire cluster. The cluster retains the settings after shutdown.

## Syntax

If you use multiple pipeline stages, put `$querySettings` first in the pipeline.

```javascript
db.aggregate( [
   { $querySettings: { showDebugQueryShape: <boolean> } },
   // Add any additional pipeline stages after $querySettings
   ... 
] )
```

## Command Fields

`$querySettings` takes this field:

## Examples

## Learn More

- `query-plans-query-optimization`
- :dbcommand:`setQuerySettings`
- :dbcommand:`removeQuerySettings`
- :pipeline:`$queryStats`
- `query-shapes`
- `Query statistics for query shapes <queryStats-queryShape>`
- `operation-rejection-filters`
