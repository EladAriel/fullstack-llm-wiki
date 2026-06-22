---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/explain-results.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============

# Explain Results

To return information on `query plans <query-plans-query-optimization>` and execution statistics of the query plans, MongoDB provides the following methods:

- :method:`db.collection.explain()`
- :method:`cursor.explain()`
To learn about important explain result fields and how to interpret them, see `interpret-explain-plan`.

> **Important:** `explain` ignores the plan cache. Instead, a set
of candidate plans are generated, and a winner is chosen without consulting
the plan cache. Furthermore, `explain` prevents the MongoDB query planner
from caching the winning plan.

> **Note:** Only the most important output fields are shown on this page, and fields for
internal use are not documented. The fields listed in the output are subject
to change.

## Explain Output Structure

The `explain` results present the query plans as a tree of stages. The output structure can differ based on which query engine the operation uses. Operations can use the classic query engine or the `slot-based execution query engine <sbe-landing>`.

To see how the output structure can differ between the two execution engines, see the following examples:

Each stage passes its resulting documents or index keys to the parent node. The leaf nodes access the collection or the indices. The internal nodes use the documents or the index keys that result from the child nodes. The root node indicates the stage that MongoDB ultimately derives the result set from.

Stages are descriptive of the operation. For example:

- `COLLSCAN` for a collection scan
- `IXSCAN` for scanning index keys
- `FETCH` for retrieving documents
- `GROUP` for grouping documents
- `SHARD_MERGE` for merging results from shards
- `SHARDING_FILTER` for filtering out orphan documents from shards
- `TS_MODIFY` for modifying a time series collection
- `BATCHED_DELETE` for multiple document deletions that are batched
together internally (starting in MongoDB 6.1)

- `EOF` for when a stage is end-of-stream
- `EXPRESS` stages for a limited set of queries that can bypass
regular query planning to use optimized index scan plans (New in version 8.0.)

`EXPRESS` stages can be one of the following:

- `EXPRESS_CLUSTERED_IXSCAN`
- `EXPRESS_DELETE`
- `EXPRESS_IXSCAN`
- `EXPRESS_UPDATE`
## Explain Output for MongoDB 5.1 and Later

This section shows the `explain` output for MongoDB 5.1 and later. To see the explain output for older versions of MongoDB, refer to the documentation for that version.

### `queryPlanner`

`explain.queryPlanner` information details the plan selected by the `query optimizer <read-operations-query-optimization>`.

> **Note:** .. include:: /includes/cbr-default-plan.rst
For more information, see `query-plan-options`.

These examples may combine the output structures of MongoDB's classic and slot-based execution engines. They are not meant to be representative. Your output may differ significantly.

### `executionStats`

The returned `explain.executionStats` information details the execution of the winning plan. In order to include `executionStats` in the results, you must run the explain in either:

- `executionStats <explain-method-executionStats>` or
- `allPlansExecution <explain-method-allPlansExecution>`
verbosity mode. Use `allPlansExecution` mode to include partial execution data captured during `plan selection <query-plans-query-optimization>`.

These examples may combine the output structures of MongoDB's classic and slot-based execution engines. They are not meant to be representative. Your output may differ significantly.

### `serverInfo`

## Execution Plan Statistics for Query with `$lookup` Pipeline Stage

.. versionadded:: 5.0

The `explain results <explain-results>` can include execution statistics for queries that use a :pipeline:`$lookup` pipeline stage. To include those execution statistics, you must run the explain operation in one of these execution verbosity modes:

- `executionStats <explain-method-executionStats>`
- `allPlansExecution <explain-method-allPlansExecution>`
The following fields are included in the explain results for a :pipeline:`$lookup` query:

```none
'$lookup': {
   from: <string>,
   as: <string>,
   localField: <string>,
   foreignField: <string>
},
totalDocsExamined: <long>,
totalKeysExamined: <long>,
collectionScans: <long>,
indexesUsed: [ <string_1>, <string_2>, ..., <string_n> ],
executionTimeMillisEstimate: <long>
```

To see the descriptions for the fields in the `$lookup` section, see the :pipeline:`$lookup` page.

The other fields are:

## Execution Plan Statistics for Search Queries

.. versionadded:: 8.1

The explain results includes `execution statistics <executionStats>` for queries that use a :pipeline:`$search`, :pipeline:`$searchMeta`, or :pipeline:`$vectorSearch` pipeline stage. To include execution statistics for search queries, run the `explain` command in one of the following execution verbosity modes:

- `executionStats <explain-method-executionStats>`
- `allPlansExecution <explain-method-allPlansExecution>`
MongoDB returns execution statistics for search and vector search queries that use the classic engine only.

For more details on search and vector search query explain results, see:

- `Explain Search Results <explain-ref>`
- `avs-explain-ref`
## Collection Scan

If the query planner selects a collection scan, the explain result includes a `COLLSCAN` stage.

If the query planner selects an index, the explain result includes a `IXSCAN` stage. The stage includes information such as the index key pattern, direction of traversal, and index bounds.

Starting in MongoDB 5.3, if the query planner selects a `clustered index <db.createCollection.clusteredIndex>` for a `clustered collection <clustered-collections>` and the query contains bounds that define the portion of the index to search, the explain result includes a `CLUSTERED_IXSCAN` stage. The stage includes information about the clustered index key and index bounds.

If the query planner selects a `clustered index <db.createCollection.clusteredIndex>` for a `clustered collection <clustered-collections>` and the query does not contain bounds, the query performs an unbounded collection scan and the explain result includes a `COLLSCAN` stage.

> **Note:** The :parameter:`notablescan` parameter does not allow unbounded
queries that use a clustered index because the queries require a
full collection scan.

For more information on execution statistics of collection scans, see `/tutorial/analyze-query-plan`.

## Covered Queries

When an index `covers <indexes-covered-queries>` a query, MongoDB can both match the query conditions **and** return the results using only the index keys. MongoDB does not need to examine documents from the collection to perform any part of the query.

When an index covers a query, the explain result has an `IXSCAN` stage that is **not** a descendant of a `FETCH` stage.

## `$or` Expression

If MongoDB uses indexes for an :query:`$or` expression, the result will include the `OR` stage with an `explain.queryPlanner.winningPlan.inputStages` array that details the indexes; e.g.:

```javascript
{
   stage: 'OR',
   inputStages: [
      {
         stage: 'IXSCAN',
         ...
      },
      {
         stage : 'IXSCAN',
         ...
      },
      ...
   ]
}
```

In previous versions of MongoDB, `cursor.explain()` returned the `clauses` array that detailed the indexes.

## Aggregation Stages with Spill Metrics

When `explain` is run in either `executionStats <explain-method-executionStats>` or `allPlansExecution <explain-method-allPlansExecution>` verbosity mode, certain aggregation stages that may spill to disk have additional output. These stages include :pipeline:`$sort`, :pipeline:`$group`, :pipeline:`$setWindowFields`, :pipeline:`$bucketAuto`, :pipeline:`$graphLookup`, and :pipeline:`$lookup` (when using the slot-based execution engine).

## Sort Stage

If MongoDB cannot use an index or indexes to obtain the sort order, the results include a `SORT` stage indicating an in-memory sort operation. If the explain plan does not contain an explicit `SORT` stage, then MongoDB used an index to obtain the sort order.

## Query Shape Hash

Starting in MongoDB 8.0, `explain` outputs the following field:

## Contents

- Interpret Results </tutorial/analyze-query-plan>
- Explain Slow Queries </tutorial/explain-slow-queries>
