---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/setIntersection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================================

# $setIntersection  (expression operator)

## Definition

## Behavior

.. include:: /includes/important-set-operator-semantics.rst

If no intersections are found (i.e. the input arrays contain no common elements), :expression:`$setIntersection` returns an empty array.

.. include:: /includes/extracts/fact-agg-top-level-expressions-setIntersection.rst

## Examples

This section contains examples that show the use of `$setIntersection` with collections.

### Elements Array Example

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

The following operation uses the :expression:`$setIntersection` operator to return an array of elements common to both the `flowerFieldA` array and the `flowerFieldB` array:

```javascript
db.flowers.aggregate(
   [
     { $project: { flowerFieldA: 1, flowerFieldB: 1, commonToBoth: { $setIntersection: [ "$flowerFieldA", "$flowerFieldB" ] }, _id: 0 } }
   ]
)
```

The operation returns the following results:

```javascript
{ "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ "rose", "orchid" ], "commonToBoth" : [ "orchid", "rose" ] }
{ "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ "orchid", "rose", "orchid" ], "commonToBoth" : [ "orchid", "rose" ] }
{ "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ "rose", "orchid", "jasmine" ], "commonToBoth" : [ "orchid", "rose" ] }
{ "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ "jasmine", "rose" ], "commonToBoth" : [ "rose" ] }
{ "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ ], "commonToBoth" : [ ] }
{ "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ [ "rose" ], [ "orchid" ] ], "commonToBoth" : [ ] }
{ "flowerFieldA" : [ "rose", "orchid" ], "flowerFieldB" : [ [ "rose", "orchid" ] ], "commonToBoth" : [ ] }
{ "flowerFieldA" : [ ], "flowerFieldB" : [ ], "commonToBoth" : [ ] }
{ "flowerFieldA" : [ ], "flowerFieldB" : [ "rose" ], "commonToBoth" : [ ] }
```

### Retrieve Documents for Roles Granted to the Current User

.. include:: /includes/user-roles-system-variable-introduction.rst

Perform the following steps to retrieve the documents accessible to `John`:

Perform the following steps to retrieve the documents accessible to `Jane`:
