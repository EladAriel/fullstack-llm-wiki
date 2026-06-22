---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/shardedDataDistribution.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================================

# $shardedDataDistribution (aggregation stage)

## Definition

## Syntax

The `shardedDataDistribution` stage has the following syntax:

```javascript
db.aggregate( [
   { $shardedDataDistribution: { } }
] )
```

## Output Fields

The `$shardedDataDistribution` stage outputs an array of documents for each sharded collection in the database.  These documents contain the following fields:

.. include:: /includes/sharding/shardedDataDistribution-output.rst

.. include:: /includes/sharding/shardedDataDistribution-output-limitation.rst

## Behavior

.. include:: /includes/fact-unexpected-shutdown-accuracy.rst

## Examples
