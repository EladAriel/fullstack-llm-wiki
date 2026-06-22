---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/measure-index-use.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================

# Measure Index Use

## Get Index Access Information with `$indexStats`

Use the :pipeline:`$indexStats` aggregation stage to get statistics regarding the use of each index for a collection. For example, the following aggregation operation returns statistics on the index use on the `orders` collection:

```javascript
db.orders.aggregate( [ { $indexStats: { } } ] )
```

.. include:: /includes/indexes/index-usage-only-current-node.rst

> **Seealso:** :pipeline:`$indexStats`

## Return Query Plan with `explain()`

Use the :method:`db.collection.explain()` or the :method:`cursor.explain()` method in `executionStats <explain-method-executionStats>` mode to return statistics about the query process, including the index used, the number of documents scanned, and the time the query takes to process in milliseconds.

Run :method:`db.collection.explain()` or the :method:`cursor.explain()` method in `allPlansExecution <explain-method-allPlansExecution>` mode to view partial execution statistics collected during plan selection.

> **Seealso:** `plan-cache-key`

## Control Index Use with `hint()`

To force MongoDB to use a particular index for a :method:`db.collection.find()` operation, specify the index with the :method:`~cursor.hint()` method. Append the :method:`~cursor.hint()` method to the :method:`~db.collection.find()` method. Consider the following example:

```javascript
db.people.find(
   { name: "John Doe", zipcode: { $gt: "63000" } }
).hint( { zipcode: 1 } )
```

To view the execution statistics for a specific index, append to the :method:`db.collection.find()` the :method:`~cursor.hint()` method followed by :method:`cursor.explain()`, e.g.:

```javascript
db.people.find(
   { name: "John Doe", zipcode: { $gt: "63000" } }
).hint( { zipcode: 1 } ).explain("executionStats")
```

Or, append :method:`~cursor.hint()` method to :method:`db.collection.explain().find() <db.collection.explain()>`:

```javascript
db.people.explain("executionStats").find(
   { name: "John Doe", zipcode: { $gt: "63000" } }
).hint( { zipcode: 1 } )
```

Specify the `$natural` operator to the :method:`~cursor.hint()` method to prevent MongoDB from using any index:

```javascript
db.people.find(
   { name: "John Doe", zipcode: { $gt: "63000" } }
).hint( { $natural: 1 } )
```

## Index Metrics

In addition to the :pipeline:`$indexStats` aggregation stage, MongoDB provides various index statistics that you may want to consider when analyzing index use for your database:

- In the output of :dbcommand:`serverStatus`:
- :serverstatus:`metrics.queryExecutor.scanned`
- :serverstatus:`metrics.operation.scanAndOrder`
- In the output of :dbcommand:`collStats`:
- `collStats.totalIndexSize`
- `collStats.indexSizes`
- In the output of :dbcommand:`dbStats`:
- `dbStats.indexes`
- `dbStats.indexSize`
