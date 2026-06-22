---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/query-plans.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========

# Query Plans

For any given query, the MongoDB query planner chooses and caches an efficient query plan given the available indexes. The planner can use either the classic multi-planner or the cost-based ranker (CBR) to select a plan.

### Query Plan Options

In the classic multi-planner, the winning plan is the query plan that produces the most results during the trial period while performing the least amount of work.

Starting in MongoDB 8.3, multi-planning with a cost-based ranker backup is the default plan selection mechanism for eligible queries. For a short trial period, the multi-planner attempts to find a plan capable of returning a result within the timeframe.

If the attempt is unsuccessful, MongoDB applies a set of rules to decide whether the multi-planner should continue or if CBR should evaluate the plans to determine the optimal solution. CBR evaluates each node in a plan based on a cost function and its cardinality estimations. MongoDB selects the plan with the lowest overall cost as the winning plan. Currently, MongoDB only invokes the CBR for a small amount of queries.

Both ranking mechanisms store the chosen plan in the **query plan cache** and reuse it for subsequent queries with the same `plan cache query shape`. The rest of this page describes plan cache behavior and related concepts that apply to both mechanisms.

The following diagram illustrates the query planner logic:

.. include:: /images/general-query-planner-logic.rst

.. include:: includes/explain-ignores-cache-plan.rst

## Plan Cache Entry State

Each plan cache query shape is associated with one of three states in the cache:

See `query-plans-plan-cache-flushes` for additional scenarios that trigger changes to the plan cache.

## Query Plan and Cache Information

To view the query plan information for a given query, you can use :method:`db.collection.explain()` or the :method:`cursor.explain()` .

To view plan cache information for a collection, you can use the :pipeline:`$planCacheStats` aggregation stage.

## Plan Cache Flushes

The query plan cache does not persist if a :binary:`~bin.mongod` restarts or shuts down. In addition:

- Any DDL event clears the plan cache for the relevant collection.
Example DDL events include dropping a collection, and creating, deleting, or hiding an index.

- Least recently used (LRU) cache replacement mechanism clears the
least recently accessed cache entry, regardless of state.

Users can also:

- Manually clear the entire plan cache using the
:method:`PlanCache.clear()` method.

- Manually clear specific plan cache entries using the
:method:`PlanCache.clearPlansByQuery()` method.

> **Seealso:** `query-hash-plan-cache-key`

## Plan Cache Debug Info Size Limit

Starting in MongoDB 5.0, the `plan cache <query-plans-query-optimization>` will save full `plan cache` entries only if the cumulative size of the `plan caches` for all collections is lower than 0.5 GB. When the cumulative size of the `plan caches` for all collections exceeds this threshold, additional `plan cache` entries are stored without the following debug information:

- `createdFromQuery <plancachestats-createdFromQuery>`
- `cachedPlan <plancachestats-cachedPlan>`
- `creationExecStats <plancachestats-creationExecStats>`
- `candidatePlanScores <plancachestats-candidatePlanScores>`
The estimated size in bytes of a `plan cache` entry is available in the output of :pipeline:`$planCacheStats`.

## planCacheShapeHash and planCacheKey

### planCacheShapeHash

.. include:: /includes/extracts/4.2-changes-query-shapes.rst

### planCacheKey

.. include:: /includes/extracts/4.2-changes-plan-cache-key.rst

For example, consider a collection `foo` with the following indexes:

```javascript
db.foo.createIndex( { x: 1 } )
db.foo.createIndex( { x: 1, y: 1 } )
db.foo.createIndex( { x: 1, z: 1 }, { partialFilterExpression: { x: { $gt: 10 } } } )
```

The following queries on the collection have the same shape:

```javascript
db.foo.explain().find( { x: { $gt: 5 } } )  // Query Operation 1
db.foo.explain().find( { x: { $gt: 20 } } ) // Query Operation 2
```

Given these queries, the index with the `partial filter expression <partial-index-query-coverage>` can support query operation 2 but not support query operation 1. Since the indexes available to support query operation 1 differs from query operation 2, the two queries have different `planCacheKey`.

If one of the indexes were dropped, or if a new index `{ x: 1, a: 1 }` were added, the `planCacheKey` for both query operations will change.

### Availability

The `planCacheShapeHash` and `planCacheKey` are available in:

- `explain() output <explain-results>` fields:
- `queryPlanner.planCacheShapeHash <explain.queryPlanner.planCacheShapeHash>`
- `queryPlanner.planCacheKey <explain.queryPlanner.planCacheKey>`
.. include:: /includes/plan-cache-rename.rst

- `profiler log messages <database-profiler>`
and `diagnostic log messages (i.e. mongod/mongos log messages)<log-messages-ref>` when logging slow queries.

- :pipeline:`$planCacheStats` aggregation stage
- `PlanCache.listQueryShapes()`
method/`planCacheListQueryShapes` command

- `PlanCache.getPlansByQuery()`
method/`planCacheListPlans` command

## Index Filters

Index filters are set with the :dbcommand:`planCacheSetFilter` command and determine which indexes the planner evaluates for a `query shape`. A plan cache query shape consists of a combination of query, sort, and projection specifications. If an index filter exists for a given query shape, the planner only considers those indexes specified in the filter.

When an index filter exists for the plan cache query shape, MongoDB ignores the :method:`~cursor.hint()`. To see whether MongoDB applied an index filter for a query shape, check the `explain.queryPlanner.indexFilterSet` field of either the :method:`db.collection.explain()` or the :method:`cursor.explain()` method.

Index filters only affect which indexes the planner evaluates; the planner may still select the collection scan as the winning plan for a given plan cache query shape.

Index filters exist for the duration of the server process and do not persist after shutdown. MongoDB also provides a command to manually remove filters.

Because index filters override the expected behavior of the planner as well as the :method:`~cursor.hint()` method, use index filters sparingly.

.. include:: /includes/index-filters-and-collations.rst

> **Seealso:** - :dbcommand:`planCacheListFilters`
- :dbcommand:`planCacheClearFilters`
- :dbcommand:`planCacheSetFilter`
- `/applications/indexes`
