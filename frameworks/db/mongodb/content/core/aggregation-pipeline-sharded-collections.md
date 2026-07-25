---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/aggregation-pipeline-sharded-collections.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

============================================

# Aggregation Pipeline and Sharded Collections

The aggregation pipeline supports operations on `sharded <sharded cluster>` collections. This section describes behaviors specific to the `aggregation pipeline <aggregation-pipeline>` and sharded collections.

## Behavior

If the pipeline starts with an exact :pipeline:`$match` on a `shard key`, and the pipeline does not contain :pipeline:`$out` or :pipeline:`$lookup` stages, the entire pipeline runs on the matching shard only.

When aggregation operations run on multiple shards, the results are routed to the :binary:`~bin.mongos` to be merged, except in the following cases:

- If the pipeline includes the :pipeline:`$out` stage, the merge runs
on the shard where the output collection lives.

- If the pipeline includes the :pipeline:`$lookup` stage that references
an unsharded collection, the merge runs on the shard where the unsharded collection lives.

- If the pipeline includes a sorting or grouping stage, and the
`allowDiskUse <aggregate-cmd-allowDiskUse>` setting is enabled, the merge runs on a randomly-selected shard.

## Optimization

When splitting the aggregation pipeline into two parts, the pipeline is split to ensure that the shards perform as many stages as possible with consideration for optimization.

To see how the pipeline was split, include the :method:`explain <db.collection.aggregate()>` option in the :method:`db.collection.aggregate()` method.

.. include:: /includes/fact-optimizations-subject-to-change.rst
