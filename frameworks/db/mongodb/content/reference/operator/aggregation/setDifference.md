---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/setDifference.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================================

# $setDifference  (expression operator)

## Definition

## Behavior

.. include:: /includes/important-set-operator-semantics.rst

.. include:: /includes/extracts/fact-agg-top-level-expressions-setDifference.rst

## Example

Consider an `flowers` collection with the following documents:

```javascript
db.flowers.insertMany( [
   { "_id" : 1, "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ "rose", "orchid" ] },
   { "_id" : 2, "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ "orchid", "rose", "orchid" ] },
   { "_id" : 3, "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ "rose", "orchid", "jasmine" ] },
   { "_id" : 4, "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ "jasmine", "rose" ] },
   { "_id" : 5, "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ ] },
   { "_id" : 6, "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ [ "rose" ], [ "orchid" ] ] },
   { "_id" : 7, "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ [ "rose", "orchid" ] ] },
   { "_id" : 8, "flowerFieldA" : [ ], "flowerFieldB" : [ ] },
   { "_id" : 9, "flowerFieldA" : [ ], "flowerFieldB" : [ "rose" ] }
] ) 
```

The following operation uses the :expression:`$setDifference` operator to return an array of elements found in the `flowerFieldB` array but not in the `flowerFieldA` array:

```javascript
db.flowers.aggregate(
   [
     { $project: { flowerFieldA: 1, flowerFieldB: 1, inBOnly: { $setDifference: [ "$flowerFieldB", "$flowerFieldA" ] }, _id: 0 } }
   ]
)
```

The operation returns the following results:

```javascript
{ "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ "rose", "orchid" ], "inBOnly" : [ ] }
{ "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ "orchid", "rose", "orchid" ], "inBOnly" : [ ] }
{ "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ "rose", "orchid", "jasmine" ], "inBOnly" : [ "jasmine" ] }
{ "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ "jasmine", "rose" ], "inBOnly" : [ "jasmine" ] }
{ "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ ], "inBOnly" : [ ] }
{ "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ [ "rose" ], [ "orchid" ] ], "inBOnly" : [ [ "rose" ], [ "orchid" ] ] }
{ "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ [ "rose", "orchid" ] ], "inBOnly" : [ [ "rose", "orchid" ] ] }
{ "flowerFieldA" : [ ], "flowerFieldB" : [ ], "inBOnly" : [ ] }
{ "flowerFieldA" : [ ], "flowerFieldB" : [ "rose" ], "inBOnly" : [ "rose" ] }
```
