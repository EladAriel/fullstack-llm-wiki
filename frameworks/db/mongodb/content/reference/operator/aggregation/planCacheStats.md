---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/planCacheStats.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===============

# $planCacheStats

## Definition

> **Seealso:** `query-plans-query-optimization`

## Considerations

### Pipeline

`$planCacheStats` must be the first stage in an aggregation pipeline.

### Restrictions

- `$planCacheStats` is not allowed in:
- `transactions <transactions>`
- :pipeline:`$facet` aggregation stage
- `$planCacheStats` requires read concern level
:readconcern:`"local"`.

### Access Control

On systems running with :setting:`~security.authorization`, the user must have the :authaction:`planCacheRead` privilege for the collection.

### Redaction

When using `Queryable Encryption <qe-manual-feature-qe>`, the `$planCacheStats` stage omits operations against encrypted collections, even though the operations are cached as normal.

### Read Preference

When the `allHosts` option is set to `false`, :pipeline:`$planCacheStats` follows the `read preference <read-preference>` in selecting the host(s) from which to return the plan cache information.

Applications may target different members of a replica set. As such, each replica set member might receive different read commands and have plan cache information that differs from other members. Nevertheless, running `$planCacheStats` on a replica set or a sharded cluster obeys the normal read preference rules. That is, on a replica set, the operation gathers plan cache information from just one member of replica set, and on a sharded cluster, the operation gathers plan cache information from just one member of each shard replica set.

## Output

.. versionchanged:: 8.3

The output of `$planCacheStats` depends on the query engine used to complete the query. The value of the `version` field of the `$planCacheStats` indicates which query engine was used:

- `1` indicates that the classic engine was used.
- `2` indicates that the `{+sbe+} <sbe-landing>` was used.
## Examples
