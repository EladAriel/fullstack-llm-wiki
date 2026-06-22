---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/graphLookup.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================

# $graphLookup (aggregation stage)

## Definition

## Considerations

### Sharded Collections

Starting in MongoDB 5.1, you can specify `sharded collections <sharding-sharded-cluster>` in the `from` parameter of :pipeline:`$graphLookup` stages.

.. include:: /includes/graphLookup-sharded-coll-transaction-note.rst

### Max Depth

Setting the `maxDepth` field to `0` is equivalent to a non-recursive :pipeline:`$graphLookup` search stage.

### Memory

.. include:: /includes/fact-graphlookup-memory-restrictions.rst

See `aggregation pipeline limits <agg-pipeline-limits>` for more information.

### Unsorted Results

The `$graphLookup` stage does not return sorted results. To sort your results, use the :expression:`$sortArray` operator.

### Views and Collation

.. include:: /includes/extracts/views-collation-agg.rst

## Examples

## Learn More

To learn more about how to use :pipeline:`$graphLookup`, see [Working with Graph Data in MongoDB.](https://www.mongodb.com/resources/basics/databases/mongodb-graph-database/)_
