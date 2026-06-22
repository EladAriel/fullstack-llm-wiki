---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/planCacheClearFilters.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================================

# planCacheClearFilters (database command)

## Definition

### Query Settings

.. include:: /includes/persistent-query-settings-avoid-index-filters-intro.rst

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
      planCacheClearFilters: <collection>,
      query: <query pattern>,
      sort: <sort specification>,
      projection: <projection specification>,
      collation: { <collation> },
      comment: <any>
   }
)
```

## Command Fields

The command has the following fields:

## Required Access

A user must have access that includes the :authaction:`planCacheIndexFilter` action.

## Examples

### Clear Specific Index Filter on Collection

The `orders` collection contains the following index filters:

```javascript
{
  "query" : { "status" : "A" },
  "sort" : { "ord_date" : -1 },
  "projection" : { },
  "indexes" : [ { "status" : 1, "cust_id" : 1 } ]
}

{
  "query" : { "status" : "A" },
  "sort" : { },
  "projection" : { },
  "indexes" : [ { "status" : 1, "cust_id" : 1 } ]
}

{
  "query": { "item": "Movie" },
  "collation": { locale: "en_US" },
  "indexes": [ { "item": 1, "order_date": 1 , "quantity": 1 } ]
}
```

> **Note:** .. include:: /includes/index-filters-and-collations.rst

The following command removes the second index filter only:

```javascript
db.runCommand(
   {
      planCacheClearFilters: "orders",
      query: { "status" : "A" }
   }
)
```

Because the values in the `query` predicate are insignificant in determining the plan cache query shape, the following command would also remove the second index filter:

```javascript
db.runCommand(
   {
      planCacheClearFilters: "orders",
      query: { "status" : "P" }
   }
)
```

### Clear all Index Filters on a Collection

The following example clears all index filters on the `orders` collection:

```javascript
db.runCommand(
   {
      planCacheClearFilters: "orders"
   }
)
```

### Clear Index Filter Containing a Query and a Collation

The following example clears the index filter containing the query on `Movie` and the collation `en_US` for the `orders` collection:

```javascript
db.runCommand(
   {
      planCacheClearFilters: "orders",
      query: { item: "Movie" },
      collation: { locale: "en_US" }
   }
)
```

> **Seealso:** - :dbcommand:`planCacheListFilters`
- :dbcommand:`planCacheSetFilter`
