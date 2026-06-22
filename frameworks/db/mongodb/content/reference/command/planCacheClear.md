---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/planCacheClear.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================

# planCacheClear (database command)

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
      planCacheClear: <collection>,
      query: <query>,
      sort: <sort>,
      collation: <collation>,
      projection: <projection>,
      comment: <any>
   }
)
```

## Command Fields

The command takes the following optional fields:

To see the query shapes for which cached query plans exist, see `planCacheStats-examples`.

## Required Access

On systems running with :setting:`~security.authorization`, a user must have access that includes the :authaction:`planCacheWrite` action.

## Examples

### Clear Cached Plans for a Plan Cache Query Shape

If a collection `orders` has the following plan cache query shape:

```javascript
  {
    "query" : { "qty" : { "$gt" : 10 } },
    "sort" : { "ord_date" : 1 },
    "collation" : { locale : "fr" },
    "projection" : { },
    "planCacheShapeHash" : "9AAD95BE" 
  }
```

> **Warning:** .. include:: /includes/plan-cache-rename.rst

The following operation clears the query plan cached for the shape:

```javascript
db.runCommand(
   {
      planCacheClear: "orders",
      query: { "qty" : { "$gt" : 10 } },
      sort: { "ord_date" : 1 },
      collation: { locale : "fr" }
   }
)
```

### Clear All Cached Plans for a Collection

The following example clears all the cached query plans for the `orders` collection:

```javascript
db.runCommand(
   {
      planCacheClear: "orders"
   }
)
```

> **Seealso:** - :method:`PlanCache.clearPlansByQuery()`
- :method:`PlanCache.clear()`
