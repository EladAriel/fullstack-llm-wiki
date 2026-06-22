---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/indexStats.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# $indexStats (aggregation stage)

## Definition

## Behavior

### Accesses Field

The statistics reported by the `accesses <indexStats-output-accesses>` field only apply to the node where the query is being run and only include index access driven by user requests. It does not include internal operations like deletion via `TTL indexes <index-feature-ttl>` or chunk split and migration operations.

### Restrictions

- `$indexStats` must be the first stage in an aggregation pipeline.
- `$indexStats` is not allowed in :doc:`transactions
</core/transactions>`.

### Index Statistics Reset Considerations

- Statistics for an index reset on :binary:`~bin.mongod`
restart or index drop and recreation.

- Modification of an existing index (see :collflag:`collMod <index>`
command) resets the statistics for that index.

## Examples
