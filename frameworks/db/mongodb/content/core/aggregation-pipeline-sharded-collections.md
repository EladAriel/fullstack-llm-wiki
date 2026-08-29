---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/aggregation-pipeline-sharded-collections.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.546647Z"
---
.. _aggregation-pipeline-sharded-collection:

# Aggregation Pipeline and Sharded Collections

**meta:** :description: Explore how the aggregation pipeline operates on sharded collections, including behaviors and optimizations for efficient processing.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

The aggregation pipeline supports operations on :term:`sharded
<sharded cluster>` collections. This section describes behaviors
specific to the :ref:`aggregation pipeline <aggregation-pipeline>` and
sharded collections.

## Behavior

If the pipeline starts with an exact :pipeline:`$match` on a
:term:`shard key`, and the pipeline does not contain :pipeline:`$out` or
:pipeline:`$lookup` stages, the entire pipeline runs on the matching
shard only.

When aggregation operations run on multiple shards, the results are 
routed to the :binary:`~bin.mongos` to be merged, except in the
following cases:

- If the pipeline includes the :pipeline:`$out` stage, the merge runs 
  on the shard where the output collection lives. 

- If the pipeline includes the :pipeline:`$lookup` stage that references
  an unsharded collection, the merge runs on the shard where the 
  unsharded collection lives.

- If the pipeline includes a sorting or grouping stage, and the
  :ref:`allowDiskUse <aggregate-cmd-allowDiskUse>` setting is enabled,
  the merge runs on a randomly-selected shard.

## Optimization

When splitting the aggregation pipeline into two parts, the pipeline is
split to ensure that the shards perform as many stages as possible with
consideration for optimization.

To see how the pipeline was split, include the :method:`explain
<db.collection.aggregate()>` option in the
:method:`db.collection.aggregate()` method.

**include:** /includes/fact-optimizations-subject-to-change.rst