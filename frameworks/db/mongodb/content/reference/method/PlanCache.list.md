---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/PlanCache.list.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================

# PlanCache.list() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Considerations

### Query Settings

.. include:: /includes/persistent-query-settings-avoid-index-filters-intro.rst

### Restrictions

:method:`PlanCache.list()` is not allowed in `transactions </core/transactions>`.

### Query Hash and Plan Cache Query Shapes

.. include:: /includes/extracts/4.2-changes-query-shapes.rst

.. include:: /includes/fact-query-optimizer-cache-behavior.rst

Each entry in the plan cache is associated with a `planCacheShapeHash`.

> **Warning:** .. include:: /includes/plan-cache-rename.rst

### Read Preference

:method:`PlanCache.list()` observes the `read preference </core/read-preference>` in selecting the host(s) from which to return the plan cache information.

Applications may target different members of a replica set. As such, each replica set member might receive different read commands and have plan cache information that differs from other members. Nevertheless, running :method:`PlanCache.list()` on a replica set or a sharded cluster obeys the normal read preference rules. That is, on a replica set, the operation gathers plan cache information from just one member of replica set, and on a sharded cluster, the operation gathers plan cache information from just one member of each shard replica set.

## Required Access

On systems running with :setting:`~security.authorization`, the user must have the :authaction:`planCacheRead` privilege for the collection.

## Examples

> **Note:** - Not all queries automatically place a query plan in the cache.
  :method:`PlanCache.list()` returns an empty array if
  there are currently no query shapes with cached query plans.
- For details on the output, see :ref:`$planCacheStats output
  <planCacheStats-output>`.

The examples in this section use the following `orders` collection:

```javascript
db.orders.insertMany( [
   { "_id" : 1, "item" : "abc", "price" : Decimal128("12"), "quantity" : 2, "type": "apparel" },
   { "_id" : 2, "item" : "jkl", "price" : Decimal128("20"), "quantity" : 1, "type": "electronics" },
   { "_id" : 3, "item" : "abc", "price" : Decimal128("10"), "quantity" : 5, "type": "apparel" },
   { "_id" : 4, "item" : "abc", "price" : Decimal128("8"), "quantity" : 10, "type": "apparel" },
   { "_id" : 5, "item" : "jkl", "price" : Decimal128("15"), "quantity" : 15, "type": "electronics" }
] )
```

Create the following indexes on the collection:

```javascript
db.orders.createIndex( { item: 1 } );
db.orders.createIndex( { item: 1, quantity: 1 } );
db.orders.createIndex( { item: 1, price: 1 }, { partialFilterExpression: { price: { $gte: Decimal128("10")} } } );
db.orders.createIndex( { quantity: 1 } );
db.orders.createIndex( { quantity: 1, type: 1 } );
```

> **Note:** Index `{ item: 1, price: 1 }` is a :doc:`partial index
</core/index-partial>` and only indexes documents with `price`
field greater than or equal to `Decimal128("10")`.

Run some queries against the collection:

```javascript
db.orders.find( { item: "abc", price: { $gte: Decimal128("10") } } )
db.orders.find( { item: "abc", price: { $gte: Decimal128("5") } } )
db.orders.find( { quantity: { $gte: 20 } } )
db.orders.find( { quantity: { $gte: 5 }, type: "apparel" } )
```

### Return Information for All Entries in the Query Cache

The following returns the `plan cache query shapes <plan cache query shape>` that have cached plans for the `orders` collection:

```javascript
db.orders.getPlanCache().list()
```

The method returns an array of the plan cache query shapes currently in the cache. In the example, the `orders` collection had cached query plans associated with the following shapes:

```javascript
[
   {
      "createdFromQuery" : {
         "query" : { "quantity" : { "$gte" : 5 }, "type" : "apparel" },
         "sort" : { },
         "projection" : { }
      },
      "planCacheShapeHash" : "4D151C4C",
      "planCacheKey" : "DD67E353",
      "isActive" : false,
      "works" : Long(4),
      "cachedPlan" : {
         "stage" : "FETCH",
         "filter" : { "type" : { "$eq" : "apparel" } },
         "inputStage" : {
            "stage" : "IXSCAN",
            "keyPattern" : { "quantity" : 1 },
            "indexName" : "quantity_1",
            "isMultiKey" : false,
            "multiKeyPaths" : { "quantity" : [ ] },
            "isUnique" : false,
            "isSparse" : false,
            "isPartial" : false,
            "indexVersion" : 2,
            "direction" : "forward",
            "indexBounds" : { "quantity" : [ "[5.0, inf.0]" ] }
         }
      },
      "timeOfCreation" : ISODate("2020-02-06T15:57:18.219Z"),
      "creationExecStats" : [
         {
            "nReturned" : 2,
            "executionTimeMillisEstimate" : 0,
            "totalKeysExamined" : 3,
            "totalDocsExamined" : 3,
            "executionStages" : {
               "stage" : "FETCH",
               "filter" : { "type" : { "$eq" : "apparel" } },
               "nReturned" : 2,
               "executionTimeMillisEstimate" : 0,
               "works" : 4,
               ...
            }
         },
         {
            "nReturned" : 2,
            "executionTimeMillisEstimate" : 0,
            "peakTrackedMemBytes" : 795,  // Available starting in MongoDB 8.3
            "totalKeysExamined" : 3,
            "totalDocsExamined" : 2,
            "executionStages" : {
               "stage" : "FETCH",
               "nReturned" : 2,
               "executionTimeMillisEstimate" : 0,
               "works" : 4,
               ...
            }
         }
      ],
      "candidatePlanScores" : [
         1.5002,
         1.5002
      ],
      "indexFilterSet" : false,
      "estimatedSizeBytes" : Long(3160),   // Available starting in MongoDB 5.0
      "host" : "mongodb1.example.net:27018",
      "shard" : "shardA"                         // Available if run on sharded cluster
   },

   {
      "createdFromQuery" : {
         "query" : { "quantity" : { "$gte" : 20 } },
         "sort" : { },
         "projection" : { }
      },
      "planCacheShapeHash" : "23B19B75",
      "planCacheKey" : "6F23F858",
      "isActive" : false,
      "works" : Long(1),
      ...
   },
   {
      "createdFromQuery" : {
         "query" : { "item" : "abc", "price" : { "$gte" : Decimal128("5") } },
         "sort" : { },
         "projection" : { }
      },
      "planCacheShapeHash" : "117A6B10",
      "planCacheKey" : "A1824628",
      "isActive" : false,
      "works" : Long(4),
      ...
   },
   {
      "createdFromQuery" : {
         "query" : { "item" : "abc", "price" : { "$gte" : Decimal128("10") } },
         "sort" : { },
         "projection" : { }
      },
      "planCacheShapeHash" : "117A6B10",
      "planCacheKey" : "2E6E536B",
      "isActive" : false,
      "works" : Long(3),
      ...
   }
]
```

> **Warning:** .. include:: /includes/plan-cache-rename.rst

For details on the output, see `$planCacheStats output <planCacheStats-output>`.

### List Plan Cache Query Shapes

To obtain a list of all of the query shapes for which there is a cached plan, you can use the :method:`PlanCache.list()`. For example, the following operation passes in a pipeline with a :pipeline:`$project` stage to only output the `createdFromQuery <plancachestats-createdFromQuery>` field and the `planCacheShapeHash <plancachestats-planCacheShapeHash>` field.

```javascript
db.orders.getPlanCache().list( [ { $project: {createdFromQuery: 1, planCacheShapeHash: 1 } } ] )
```

> **Warning:** .. include:: /includes/plan-cache-rename.rst

The operation returns the following plan cache query shapes:

```javascript
[
   { "createdFromQuery" : { "query" : { "quantity" : { "$gte" : 5 }, "type" : "apparel" }, "sort" : { }, "projection" : { } }, "planCacheShapeHash" : "4D151C4C" },
   { "createdFromQuery" : { "query" : { "quantity" : { "$gte" : 20 } }, "sort" : { }, "projection" : { } }, "planCacheShapeHash" : "23B19B75" },
   { "createdFromQuery" : { "query" : { "item" : "abc", "price" : { "$gte" : Decimal128("5") } }, "sort" : { }, "projection" : { } }, "planCacheShapeHash" : "117A6B10" },
   { "createdFromQuery" : { "query" : { "item" : "abc", "price" : { "$gte" : Decimal128("10") } }, "sort" : { }, "projection" : { } }, "planCacheShapeHash" : "117A6B10" }
]
```

For details on the output, see `$planCacheStats output <planCacheStats-output>`.

### Find Cache Entry Details for a Plan Cache Query Shape

To return plan cache information for a particular query shape, pass in a pipeline with a :pipeline:`$match` on the `planCacheKey <plancachestats-planCacheKey>` field.

```javascript
db.orders.getPlanCache().list([ { $match: { planCacheKey: "DD67E353"} } ] )
```

The operation returns the following:

```javascript
[
   {
      "createdFromQuery" : {
         "query" : {
            "quantity" : {
               "$gte" : 5
            },
            "type" : "apparel"
         },
         "sort" : {

         },
         "projection" : {

         }
      },
      "planCacheShapeHash" : "4D151C4C",
      "planCacheKey" : "DD67E353",
      "isActive" : false,
      "works" : Long(4),
      "cachedPlan" : {
         "stage" : "FETCH",
         "filter" : {
            "type" : {
               "$eq" : "apparel"
            }
         },
         "inputStage" : {
            "stage" : "IXSCAN",
            "keyPattern" : {
               "quantity" : 1
            },
            "indexName" : "quantity_1",
            "isMultiKey" : false,
            "multiKeyPaths" : {
               "quantity" : [ ]
            },
            "isUnique" : false,
            "isSparse" : false,
            "isPartial" : false,
            "indexVersion" : 2,
            "direction" : "forward",
            "indexBounds" : {
               "quantity" : [
                  "[5.0, inf.0]"
               ]
            }
         }
      },
      "timeOfCreation" : ISODate("2020-02-11T17:14:33.873Z"),
      "creationExecStats" : [
         {
            "nReturned" : 2,
            "executionTimeMillisEstimate" : 0,
            "peakTrackedMemBytes" : 795,  // Available starting in MongoDB 8.3
            "totalKeysExamined" : 3,
            "totalDocsExamined" : 3,
            "executionStages" : {
               "stage" : "FETCH",
               "filter" : {
                  "type" : {
                     "$eq" : "apparel"
                  }
               },
               "nReturned" : 2,
               "executionTimeMillisEstimate" : 0,
               "works" : 4,
               "advanced" : 2,
               "needTime" : 1,
               "needYield" : 0,
               "saveState" : 0,
               "restoreState" : 0,
               "isEOF" : 1,
               "docsExamined" : 3,
               "alreadyHasObj" : 0,
               "inputStage" : {
                  "stage" : "IXSCAN",
                  "nReturned" : 3,
                  "executionTimeMillisEstimate" : 0,
                  "works" : 4,
                  "advanced" : 3,
                  "needTime" : 0,
                  "needYield" : 0,
                  "saveState" : 0,
                  "restoreState" : 0,
                  "isEOF" : 1,
                  "keyPattern" : {
                     "quantity" : 1
                  },
                  "indexName" : "quantity_1",
                  "isMultiKey" : false,
                  "multiKeyPaths" : {
                     "quantity" : [ ]
                  },
                  "isUnique" : false,
                  "isSparse" : false,
                  "isPartial" : false,
                  "indexVersion" : 2,
                  "direction" : "forward",
                  "indexBounds" : {
                     "quantity" : [
                        "[5.0, inf.0]"
                     ]
                  },
                  "keysExamined" : 3,
                  "seeks" : 1,
                  "dupsTested" : 0,
                  "dupsDropped" : 0
               }
            }
         },
         {
            "nReturned" : 2,
            "executionTimeMillisEstimate" : 0,
            "totalKeysExamined" : 3,
            "totalDocsExamined" : 2,
            "executionStages" : {
               "stage" : "FETCH",
               "nReturned" : 2,
               "executionTimeMillisEstimate" : 0,
               "works" : 4,
               "advanced" : 2,
               "needTime" : 1,
               "needYield" : 0,
               "saveState" : 0,
               "restoreState" : 0,
               "isEOF" : 1,
               "docsExamined" : 2,
               "alreadyHasObj" : 0,
               "inputStage" : {
                  "stage" : "IXSCAN",
                  "nReturned" : 2,
                  "executionTimeMillisEstimate" : 0,
                  "peakTrackedMemBytes" : 795,  // Available starting in MongoDB 8.3
                  "works" : 4,
                  "advanced" : 2,
                  "needTime" : 1,
                  "needYield" : 0,
                  "saveState" : 0,
                  "restoreState" : 0,
                  "isEOF" : 1,
                  "keyPattern" : {
                     "quantity" : 1,
                     "type" : 1
                  },
                  "indexName" : "quantity_1_type_1",
                  "isMultiKey" : false,
                  "multiKeyPaths" : {
                     "quantity" : [ ],
                     "type" : [ ]
                  },
                  "isUnique" : false,
                  "isSparse" : false,
                  "isPartial" : false,
                  "indexVersion" : 2,
                  "direction" : "forward",
                  "indexBounds" : {
                     "quantity" : [
                        "[5.0, inf.0]"
                     ],
                     "type" : [
                        "[\"apparel\", \"apparel\"]"
                     ]
                  },
                  "keysExamined" : 3,
                  "seeks" : 2,
                  "dupsTested" : 0,
                  "dupsDropped" : 0
               }
            }
         }
      ],
      "candidatePlanScores" : [
         1.5002,
         1.5002
      ],
      "indexFilterSet" : false,
      "estimatedSizeBytes" : Long(3160),   // Available starting in MongoDB 5.0
      "host" : "mongodb1.example.net:27018",
      "shard" : "shardA"                         // Available if run on sharded cluster
   }
]
```

> **Warning:** .. include:: /includes/plan-cache-rename.rst

For details on the output, see `$planCacheStats output <planCacheStats-output>`.
