---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/planCacheSetFilter.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================================

# planCacheSetFilter (database command)

## Definition

### Query Settings

.. include:: /includes/persistent-query-settings-avoid-index-filters.rst

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   {
      planCacheSetFilter: <collection>,
      query: <query>,
      sort: <sort>,
      projection: <projection>,
      collation: { <collation> },
      indexes: [ <index1>, <index2>, ...],
      comment: <any>
   }
)
```

The plan cache query shape for the index filter is the combination of:

- `query`
- `sort`
- `projection`
- `collation`
## Command Fields

The command has the following fields:

Index filters only exist for the duration of the server process and do not persist after shutdown. To clear the index filters, use the :dbcommand:`planCacheClearFilters` command.

## Required Access

A user must have access that includes the :authaction:`planCacheIndexFilter` action.

## Examples

### Set Filter on Plan Cache Query Shape Consisting of Predicate Only

The following example creates an index filter on the `orders` collection such that for queries that consist only of an equality match on the `status` field without any projection and sort, the query optimizer evaluates only the two specified indexes and the collection scan for the winning plan:

```javascript
db.runCommand(
   {
      planCacheSetFilter: "orders",
      query: { status: "A" },
      indexes: [
         { cust_id: 1, status: 1 },
         { status: 1, order_date: -1 }
      ]
   }
)
```

In the query predicate, only the structure of the predicate, including the field names, are significant; the values are insignificant. As such, the created filter applies to the following operations:

```javascript
db.orders.find( { status: "D" } )
db.orders.find( { status: "P" } )
```

To see whether MongoDB will apply an index filter for a plan cache query shape, check the `explain.queryPlanner.indexFilterSet` field of either the :method:`db.collection.explain()` or the :method:`cursor.explain()` method.

### Set Filter on Plan Cache Query Shape Consisting of Predicate, Projection, and Sort

The following example creates an index filter for the `orders` collection. The filter applies to queries whose predicate is an equality match on the `item` field, where only the `quantity` field is projected and an ascending sort by `order_date` is specified.

```javascript
db.runCommand(
   {
      planCacheSetFilter: "orders",
      query: { item: "ABC" },
      projection: { quantity: 1, _id: 0 },
      sort: { order_date: 1 },
      indexes: [
         { item: 1, order_date: 1 , quantity: 1 }
      ]
   }
)
```

For the plan cache query shape, the query optimizer will only consider indexed plans which use the index `{ item: 1, order_date: 1, quantity: 1 }`.

### Set Filter on Plan Cache Query Shape Consisting of Predicate and Collation

The following example creates an index filter for the `orders` collection. The filter applies to queries whose predicate is an equality match on the `item` field and the collation `en_US` (English United States).

```javascript
db.runCommand(
   {
      planCacheSetFilter: "orders",
      query: { item: "Movie" },
      collation: { locale: "en_US" },
      indexes: [
         { item: 1, order_date: 1 , quantity: 1 }
      ]
   }
)
```

For the plan cache query shape, the query optimizer only uses indexed plans that use the index `{ item: 1, order_date: 1, quantity: 1 }`.

.. include:: /includes/index-filters-and-collations.rst

> **Seealso:** - :dbcommand:`planCacheClearFilters`
- :dbcommand:`planCacheListFilters`
- :pipeline:`$planCacheStats`
