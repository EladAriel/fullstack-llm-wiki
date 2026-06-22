---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/aggregation-pipeline-optimization.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================

# Aggregation Pipeline Optimization

Aggregation pipeline operations have an optimization phase that reshapes the pipeline for improved performance.

To see how the optimizer transforms a pipeline, include the :method:`explain <db.collection.aggregate()>` option in the :method:`db.collection.aggregate()` method.

.. include:: /includes/fact-optimizations-subject-to-change.rst

This page also describes how to improve performance using `indexes and document filters <aggregation-pipeline-optimization-indexes-and-filters>`.

## Projection Optimization

The aggregation pipeline can determine if it requires only a subset of the fields in the documents to obtain the results. If so, the pipeline only uses those fields, reducing the amount of data passing through the pipeline.

### `$project` Stage Placement

.. include:: /includes/aggregation/fact-project-stage-placement.rst

## Pipeline Sequence Optimization

### (`$project` or `$unset` or `$addFields` or `$set`) + `$match` Sequence Optimization

For an aggregation pipeline that contains a projection stage (:pipeline:`$addFields`, :pipeline:`$project`, :pipeline:`$set`, or :pipeline:`$unset`) followed by a :pipeline:`$match` stage, MongoDB moves any filters in the `$match` stage that do not require values computed in the projection stage to a new `$match` stage before the projection.

If an aggregation pipeline contains multiple projection or `$match` stages, MongoDB performs this optimization for each `$match` stage, moving each `$match` filter before all projection stages that the filter does not depend on.

Consider a pipeline with the following stages:

```javascript
{
   $addFields: {
      maxTime: { $max: "$times" },
      minTime: { $min: "$times" }
   }
},
{
   $project: {
      _id: 1,
      name: 1,
      times: 1,
      maxTime: 1,
      minTime: 1,
      avgTime: { $avg: ["$maxTime", "$minTime"] }
   }
},
{
   $match: {
      name: "Joe Schmoe",
      maxTime: { $lt: 20 },
      minTime: { $gt: 5 },
      avgTime: { $gt: 7 }
   }
}
```

The optimizer breaks up the `$match` stage into four individual filters, one for each key in the `$match` query document. The optimizer then moves each filter before as many projection stages as possible, creating new `$match` stages as needed.

Given this example, the optimizer automatically produces the following optimized pipeline:

```javascript
{ $match: { name: "Joe Schmoe" } },
{ $addFields: {
    maxTime: { $max: "$times" },
    minTime: { $min: "$times" }
} },
{ $match: { maxTime: { $lt: 20 }, minTime: { $gt: 5 } } },
{ $project: {
    _id: 1, name: 1, times: 1, maxTime: 1, minTime: 1,
    avgTime: { $avg: ["$maxTime", "$minTime"] }
} },
{ $match: { avgTime: { $gt: 7 } } }
```

> **Note:** The optimized pipeline is not intended to be run manually. The
original and optimized pipelines return the same results.
You can see the optimized pipeline in the :ref:`explain plan
<example-aggregate-method-explain-option>`.

The :pipeline:`$match` filter `{ avgTime: { $gt: 7 } }` depends on the :pipeline:`$project` stage to compute the `avgTime` field. The :pipeline:`$project` stage is the last projection stage in this pipeline, so the :pipeline:`$match` filter on `avgTime` could not be moved.

The `maxTime` and `minTime` fields are computed in the :pipeline:`$addFields` stage but have no dependency on the :pipeline:`$project` stage. The optimizer created a new :pipeline:`$match` stage for the filters on these fields and placed it before the :pipeline:`$project` stage.

The :pipeline:`$match` filter `{ name: "Joe Schmoe" }` does not use any values computed in either the :pipeline:`$project` or :pipeline:`$addFields` stages so it was moved to a new :pipeline:`$match` stage before both of the projection stages.

After optimization, the filter `{ name: "Joe Schmoe" }` is in a :pipeline:`$match` stage at the beginning of the pipeline. This has the added benefit of allowing the aggregation to use an index on the `name` field when initially querying the collection.

### `$sort` + `$match` Sequence Optimization

When you have a sequence with :pipeline:`$sort` followed by a :pipeline:`$match`, the :pipeline:`$match` moves before the :pipeline:`$sort` to minimize the number of objects to sort. For example, if the pipeline consists of the following stages:

```javascript
{ $sort: { age : -1 } },
{ $match: { status: 'A' } }
```

During the optimization phase, the optimizer transforms the sequence to the following:

```javascript
{ $match: { status: 'A' } },
{ $sort: { age : -1 } }
```

### `$redact` + `$match` Sequence Optimization

When a :pipeline:`$redact` stage is immediately followed by a :pipeline:`$match`, the optimizer can sometimes add a portion of the `$match` before the `$redact`. If the added `$match` is at the start of the pipeline, the aggregation can use an index and query the collection to limit the documents that enter the pipeline. See `aggregation-pipeline-optimization-indexes-and-filters`.

For example, if the pipeline consists of the following stages:

```javascript
{ $redact: { $cond: { if: { $eq: [ "$level", 5 ] }, then: "$$PRUNE", else: "$$DESCEND" } } },
{ $match: { year: 2014, category: { $ne: "Z" } } }
```

The optimizer can add the same :pipeline:`$match` stage before the :pipeline:`$redact` stage:

```javascript
{ $match: { year: 2014 } },
{ $redact: { $cond: { if: { $eq: [ "$level", 5 ] }, then: "$$PRUNE", else: "$$DESCEND" } } },
{ $match: { year: 2014, category: { $ne: "Z" } } }
```

### `$project`/`$unset` + `$skip` Sequence Optimization

When you have a sequence with :pipeline:`$project` or :pipeline:`$unset` followed by :pipeline:`$skip`, the :pipeline:`$skip` moves before :pipeline:`$project`. For example, if the pipeline consists of the following stages:

```javascript
{ $sort: { age : -1 } },
{ $project: { status: 1, name: 1 } },
{ $skip: 5 }
```

During the optimization phase, the optimizer transforms the sequence to the following:

```javascript
{ $sort: { age : -1 } },
{ $skip: 5 },
{ $project: { status: 1, name: 1 } }
```

## Pipeline Coalescence Optimization

When possible, the optimization phase coalesces a pipeline stage into its predecessor. Generally, coalescence occurs after any sequence reordering optimization.

### `$sort` + `$limit` Coalescence

When a :pipeline:`$sort` precedes a :pipeline:`$limit`, the optimizer can coalesce the `$limit` into the `$sort` if no intervening stages modify the number of documents (for example, :pipeline:`$unwind` or :pipeline:`$group`). MongoDB does not coalesce the `$limit` into the `$sort` if intervening stages change the document count.

For example, if the pipeline consists of the following stages:

```javascript
{ $sort : { age : -1 } },
{ $project : { age : 1, status : 1, name : 1 } },
{ $limit: 5 }
```

During the optimization phase, the optimizer coalesces the sequence to the following:

```javascript
{
    "$sort" : {
       "sortKey" : {
          "age" : -1
       },
       "limit" : Long(5)
    }
},
{ "$project" : { 
         "age" : 1, 
         "status" : 1, 
         "name" : 1 
  } 
}
```

This allows the sort operation to only maintain the top `n` results as it progresses, where `n` is the specified limit, and MongoDB only needs to store `n` items in memory [#coalescence-allowDiskUse]_. See `sort-and-memory` for more information.

> **Note:** If a :pipeline:`$skip` stage sits between the :pipeline:`$sort` and
:pipeline:`$limit` stages, MongoDB coalesces the `$limit` into the
`$sort` and increases the `$limit` value by the `$skip`
amount. See `agg-sort-skip-limit-sequence` for an example.

`allowDiskUse` is `true` and the `n` items exceed the `aggregation memory limit <agg-memory-restrictions>`.

### `$limit` + `$limit` Coalescence

When a :pipeline:`$limit` immediately follows another :pipeline:`$limit`, the two stages can coalesce into a single :pipeline:`$limit` where the limit amount is the smaller of the two initial limit amounts. For example, a pipeline contains the following sequence:

```javascript
{ $limit: 100 },
{ $limit: 10 }
```

Then the second :pipeline:`$limit` stage can coalesce into the first :pipeline:`$limit` stage and result in a single :pipeline:`$limit` stage where the limit amount `10` is the minimum of the two initial limits `100` and `10`.

```javascript
{ $limit: 10 }
```

### `$skip` + `$skip` Coalescence

When a :pipeline:`$skip` immediately follows another :pipeline:`$skip`, the two stages can coalesce into a single :pipeline:`$skip` where the skip amount is the sum of the two initial skip amounts. For example, a pipeline contains the following sequence:

```javascript
{ $skip: 5 },
{ $skip: 2 }
```

Then the second :pipeline:`$skip` stage can coalesce into the first :pipeline:`$skip` stage and result in a single :pipeline:`$skip` stage where the skip amount `7` is the sum of the two initial limits `5` and `2`.

```javascript
{ $skip: 7 }
```

### `$match` + `$match` Coalescence

When a :pipeline:`$match` immediately follows another :pipeline:`$match`, the two stages can coalesce into a single :pipeline:`$match` combining the conditions with an :expression:`$and`. For example, a pipeline contains the following sequence:

```javascript
{ $match: { year: 2014 } },
{ $match: { status: "A" } }
```

Then the second :pipeline:`$match` stage can coalesce into the first :pipeline:`$match` stage and result in a single :pipeline:`$match` stage

```javascript
{ $match: { $and: [ { "year" : 2014 }, { "status" : "A" } ] } }
```

### `$lookup`, `$unwind`, and `$match` Coalescence

When :pipeline:`$unwind` immediately follows :pipeline:`$lookup`, and the :pipeline:`$unwind` operates on the `as` field of the :pipeline:`$lookup`, the optimizer coalesces the :pipeline:`$unwind` into the :pipeline:`$lookup` stage. This avoids creating large intermediate documents. Furthermore, if :pipeline:`$unwind` is followed by a :pipeline:`$match` on any `as` subfield of the :pipeline:`$lookup`, the optimizer also coalesces the :pipeline:`$match`.

For example, a pipeline contains the following sequence:

```javascript
{
   $lookup: {
     from: "otherCollection",
     as: "resultingArray",
     localField: "x",
     foreignField: "y"
   }
},
{ $unwind: "$resultingArray"  },
{ $match: {
    "resultingArray.foo": "bar"
  }
}
```

The optimizer coalesces the :pipeline:`$unwind` and :pipeline:`$match` stages into the :pipeline:`$lookup` stage. If you run the aggregation with `explain` option, the `explain` output shows the coalesced stages:

```javascript
{
   $lookup: {
     from: "otherCollection",
     as: "resultingArray",
     localField: "x",
     foreignField: "y",
     let: {},
     pipeline: [
       {
         $match: {
           "foo": {
             "$eq": "bar"
           }
         }
       }
     ],
     unwinding: {
       "preserveNullAndEmptyArrays": false
     }
   }
}
```

You can see this optimized pipeline in the `explain plan <example-aggregate-method-explain-option>`.

The `unwinding` field shown in the previous `explain` output differs from the `$unwind` stage. The `unwinding` field shows how the pipeline is internally optimized. The `$unwind` stage deconstructs an array field from the input documents and outputs a document for each element.

## |sbe-title| Pipeline Optimizations

MongoDB can use the `slot-based query execution engine <sbe-landing>` to execute certain pipeline stages when specific conditions are met. In most cases, the |sbe-short| provides improved performance and reduced CPU and memory costs compared to the classic query engine.

To verify that the |sbe-short| is used, run the aggregation with the `explain` option. This option outputs information on the aggregation's query plan. For more information on using `explain` with aggregations, see `example-aggregate-method-explain-option`.

The following sections describe:

- The conditions when the |sbe-short| is used for aggregation.
- How to verify if the |sbe-short| was used.
### `$group` Optimization

.. versionadded:: 5.2

.. include:: /includes/fact-sbe-group-overview.rst

When the |sbe| is used for :pipeline:`$group`, the `explain results <explain-results>` include `queryPlanner.winningPlan.queryPlan.stage: "GROUP"`.

The location of the `queryPlanner` object depends on whether the pipeline contains stages after the `$group` stage that cannot be executed using the |sbe-short|.

- If `$group` is the last stage or all stages after `$group` can
be executed using the |sbe-short|, the `queryPlanner` object is in the top-level `explain` output object (`explain.queryPlanner`).

- If the pipeline contains stages after `$group` that cannot be
executed using the |sbe-short|, the `queryPlanner` object is in `explain.stages[0].$cursor.queryPlanner`.

### `$lookup` Optimization

.. versionadded:: 6.0

.. include:: /includes/fact-sbe-lookup-overview.rst

When the |sbe| is used for :pipeline:`$lookup`, the `explain results <explain-results>` include `queryPlanner.winningPlan.queryPlan.stage: "EQ_LOOKUP"`. `EQ_LOOKUP` means "equality lookup".

The location of the `queryPlanner` object depends on whether the pipeline contains stages after the `$lookup` stage that cannot be executed using the |sbe-short|.

- If `$lookup` is the last stage or all stages after `$lookup` can
be executed using the |sbe-short|, the `queryPlanner` object is in the top-level `explain` output object (`explain.queryPlanner`).

- If the pipeline contains stages after `$lookup` that cannot be
executed using the |sbe-short|, the `queryPlanner` object is in `explain.stages[0].$cursor.queryPlanner`.

## Improve Performance with Indexes and Document Filters

The following sections show how you can improve aggregation performance using indexes and document filters.

### Indexes

An aggregation pipeline can use `indexes <indexes>` from the input collection to improve performance. Using an index limits the amount of documents a stage processes. Ideally, an index can `cover <read-operations-covered-query>` the stage query. A covered query has especially high performance, since the index returns all matching documents.

For example, a pipeline that consists of :pipeline:`$match`, :pipeline:`$sort`, :pipeline:`$group` can benefit from indexes at every stage:

- An index on the `$match` query field efficiently
identifies the relevant data

- An index on the sorting field returns data in sorted order for the
`$sort` stage

- An index on the grouping field that matches the `$sort`
order returns all of the field values needed for the `$group` stage, making it a covered query.

To determine whether a pipeline uses indexes, review the query plan and look for `IXSCAN` or `DISTINCT_SCAN` plans.

> **Note:** In some cases, the query planner uses a `DISTINCT_SCAN` index plan
that returns one document per index key value. `DISTINCT_SCAN`
executes faster than `IXSCAN` if there are multiple documents per
key value. However, index scan parameters might affect the time
comparison of `DISTINCT_SCAN` and `IXSCAN`.

For early stages in your aggregation pipeline, consider indexing the query fields. Stages that can benefit from indexes are:

:pipeline:`$match` stage During the `$match` stage, the server can use an index if `$match` is the first stage in the pipeline, after any optimizations from the `query planner <query-plans-query-optimization>`.

:pipeline:`$sort` stage During the `$sort` stage, the server can use an index if the stage is not preceded by a :pipeline:`$project`, :pipeline:`$unwind`, or :pipeline:`$group` stage.

:pipeline:`$group` stage During the `$group` stage, the server can use an index to quickly find the :group:`$first <$first>` or :group:`$last <$last>` document in each group if the stage meets both of these conditions:

- The pipeline :pipeline:`sorts <$sort>` and :pipeline:`groups
<$group>` by the same field.

- The `$group` stage only uses the :group:`$first` or
:group:`$last` accumulator operator.

See `$group Performance Optimizations <group-pipeline-optimization>` for an example.

:pipeline:`$geoNear` stage The server always uses an index for the `$geoNear` stage, since it requires a `geospatial index <index-feature-geospatial>`.

Additionally, stages later in the pipeline that retrieve data from other, unmodified collections can use indexes on those collections for optimization. These stages include:

- :pipeline:`$lookup`
- :pipeline:`$graphLookup`
- :pipeline:`$unionWith`
### Document Filters

If your aggregation operation requires only a subset of the documents in a collection, filter the documents first:

- Use the :pipeline:`$match`, :pipeline:`$limit`, and :pipeline:`$skip`
stages to restrict the documents that enter the pipeline.

- When possible, put :pipeline:`$match` at the beginning of the pipeline
to use indexes that scan the matching documents in a collection.

- :pipeline:`$match` followed by :pipeline:`$sort` at the start of the
pipeline is equivalent to a single query with a sort, and can use an index.

## Example

### `$sort` + `$skip` + `$limit` Sequence

A pipeline contains a sequence of :pipeline:`$sort` followed by a :pipeline:`$skip` followed by a :pipeline:`$limit`:

```javascript
{ $sort: { age : -1 } },
{ $skip: 10 },
{ $limit: 5 }
```

The optimizer performs `agg-sort-limit-coalescence` to transforms the sequence to the following:

```javascript
{
   "$sort" : {
      "sortKey" : {
         "age" : -1
      },
      "limit" : Long(15)
   }
},
{
   "$skip" : Long(10)
}
```

MongoDB increases the :pipeline:`$limit` amount with the reordering.

> **Seealso:** :method:`explain <db.collection.aggregate()>` option in the
:method:`db.collection.aggregate()`
