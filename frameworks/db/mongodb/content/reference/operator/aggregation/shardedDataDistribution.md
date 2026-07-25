---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/shardedDataDistribution.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
