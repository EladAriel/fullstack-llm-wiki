---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/PlanCache.clearPlansByQuery.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================================

# PlanCache.clearPlansByQuery() (mongosh method)

## Definition

.. include:: /includes/persistent-query-settings-avoid-index-filters-intro.rst

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Required Access

On systems running with :setting:`~security.authorization`, a user must have access that includes the :authaction:`planCacheWrite` action.

## Example

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

The following operation removes the query plan cached for the shape:

```javascript
db.orders.getPlanCache().clearPlansByQuery(
   { "qty" : { "$gt" : 10 } },
   { },
   { "ord_date" : 1 },
   { locale: "fr" }
)
```

> **Seealso:** - :method:`db.collection.getPlanCache()`
- `PlanCache.listQueryShapes()`
- :method:`PlanCache.clear()`
