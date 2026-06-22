---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.explain.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================================

# db.collection.explain() (mongosh method)

.. include:: /includes/wayfinding/mongosh-method-explain.rst

## Description

### Parameters

The :method:`db.collection.explain()` method has the following parameter:

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Required Access

.. include:: /includes/explain-required-access.rst

## Behavior

.. include:: includes/explain-ignores-cache-plan.rst

### Verbosity Modes

The behavior of :method:`db.collection.explain()` and the amount of information returned depend on the `verbosity` mode.

### Explain and Write Operations

For write operations, :method:`db.collection.explain()` returns information about the write operation that would be performed but does not actually modify the database.

### Restrictions

.. include:: /includes/extracts/4.2-changes-agg-out-explain.rst

### `explain()` Mechanics

The :method:`db.collection.explain()` method wraps the :dbcommand:`explain` command and is the preferred way to run :dbcommand:`explain`.

.. include:: /includes/fact-explain-methods-differences.rst

:method:`db.collection.explain().aggregate() <db.collection.explain()>` is equivalent to passing the `explain <example-aggregate-method-explain-option>` option to the :method:`db.collection.aggregate()` method.

### `help()`

To see the list of operations supported by :method:`db.collection.explain()`, run:

```javascript
db.collection.explain().help()
```

:method:`db.collection.explain().find() <db.collection.explain()>` returns a cursor, which allows for the chaining of query modifiers. To see the list of query modifiers supported by :method:`db.collection.explain().find() <db.collection.explain()>` as well as cursor-related methods, run:

```javascript
db.collection.explain().find().help()
```

You can chain multiple modifiers to `db.collection.explain().find()`. For an example, see `explain-find-modifiers`.

### Sharded Clusters

.. versionadded:: 8.3

If you run `db.collection.explain()` against a database that does not exist on a sharded cluster, the execution stage reaches the end-of-stream and the operation does not create the database. For more information on end-of-stream execution stats, see `explain.executionStats.executionStages.isEOF`.

## Output

.. include:: /includes/fact-explain-results-categories.rst

For details on the output, see `/reference/explain-results`.

## Examples

### `queryPlanner` Mode

By default, :method:`db.collection.explain()` runs in `"queryPlanner"` verbosity mode.

The following example runs :method:`db.collection.explain()` in `"queryPlanner"` verbosity mode to return the query planning information for the specified :method:`~db.collection.count()` operation:

```javascript
db.products.explain().count( { quantity: { $gt: 50 } } )
```

### `executionStats`  Mode

The following example runs :method:`db.collection.explain()` in `"executionStats"` verbosity mode to return the query planning and execution information for the specified :method:`~db.collection.find()` operation:

```javascript
db.products.explain("executionStats").find(
   { quantity: { $gt: 50 }, category: "apparel" }
)
```

### `allPlansExecution` Mode

The following example runs :method:`db.collection.explain()` in `"allPlansExecution"` verbosity mode. :method:`db.collection.explain()` returns the `explain.queryPlanner` and `explain.executionStats` for all considered plans for the specified :method:`~db.collection.findAndModify()` operation:

> **Note:** The execution of this explain will not modify data but runs the
query predicate of the update operation. For candidate plans,
MongoDB returns the execution information captured during the
`plan selection phase <query-plans-query-optimization>`.

```javascript
db.products.explain( "allPlansExecution" ).findAndModify( {
   query: { name: "Tom", state: "active", rating: { $gt: 10 } },
   sort: { rating: 1 },
   update: { $inc: { score: 1 } }
} )
```

### Explain `find()` with Modifiers

:method:`db.collection.explain().find() <db.collection.explain()>` construct allows for the chaining of query modifiers. For example, the following operation provides information on the :method:`~db.collection.find()` method with :method:`~cursor.sort()` and :method:`~cursor.hint()` query modifiers.

```javascript
db.products.explain("executionStats").find(
   { quantity: { $gt: 50 }, category: "apparel" }
).sort( { quantity: -1 } ).hint( { category: 1, quantity: -1 } )
```

For a list of query modifiers available, run the following in :binary:`~bin.mongosh`:

```javascript
db.collection.explain().find().help()
```

### Access the `explain()` Results with `finish()` Method

The :method:`db.collection.explain().find() <db.collection.explain()>` returns the `explain()` results. If run interactively in :binary:`~bin.mongosh` you can use the `.finish()` method to access the query plan:

```javascript
db.products.explain().find( { category: "apparel" } ).finish().queryPlanner.winningPlan;
```
