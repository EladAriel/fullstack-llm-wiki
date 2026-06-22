---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/setUnion.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# $setUnion (expression operator)

## Definition

Takes two or more arrays and returns a single array containing the unique elements that appear in any input array. `$setUnion` can be used as an aggregation accumulator or an array operator.

## Aggregation Accumulator

`$setUnion` is available as an accumulator in these stages:

- :pipeline:`$bucket`
- :pipeline:`$bucketAuto`
- :pipeline:`$group`
- :pipeline:`$setWindowFields`
### Syntax

When used as an aggregation accumulator, `$setUnion` has the following syntax:

```javascript
{ $setUnion: "<array field>" }
```

### Behavior

.. include:: /includes/important-set-operator-semantics.rst

.. include:: /includes/fact-setUnion-non-recursive.rst

.. include:: /includes/fact-agg-accumulator-null-missing-behavior.rst

### Example

.. include:: /includes/concatArrays-setUnion-accum-example-setup.rst

This example shows how you can use `$setUnion` as an accumulator. This example accumulates all the unique elements in the `items` arrays when grouping on the `location` field:

```javascript
db.sales.aggregate( [ 
   {
      $group: {
         _id: "$location",
         array: { "$setUnion": "$items" }
      }
   }
] )
```

The operation returns the following result:

```javascript
[
   {
      "_id": "NYC",
      "array": [
          "laptop", "tablet", "phone", "desktop", { "accessories": [ "mouse", "keyboard"] }
      ]
   }
]
```

## Array Operator

### Syntax

When used as an array operator, `$setUnion` has the following syntax:

```javascript
{ 
   $setUnion: [ <expression1>, <expression2>, ... ] 
}
```

### Behavior

.. include:: /includes/important-set-operator-semantics.rst

.. include:: /includes/args-can-be-expressions.rst

.. include:: /includes/fact-setUnion-non-recursive.rst

### Example

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

The following operation uses the :expression:`$setUnion` operator to return an array of elements found in the `flowerFieldA` array or the `flowerFieldB` array or both:

```javascript
db.flowers.aggregate(
   [
     { $project: { flowerFieldA:1, flowerFieldB: 1, allValues: { $setUnion: [ "$flowerFieldA", "$flowerFieldB" ] }, _id: 0 } }
   ]
)
```

The operation returns the following results:

```javascript
{ "flowerFieldA": [ "rose", "orchid" ], "flowerFieldB": [ "rose", "orchid" ], "allValues": [ "orchid", "rose" ] }
{ "flowerFieldA": [ "rose", "orchid" ], "flowerFieldB": [ "orchid", "rose", "orchid" ], "allValues": [ "orchid", "rose" ] }
{ "flowerFieldA": [ "rose", "orchid" ], "flowerFieldB": [ "rose", "orchid", "jasmine" ], "allValues": [ "orchid", "rose", "jasmine" ] }
{ "flowerFieldA": [ "rose", "orchid" ], "flowerFieldB": [ "jasmine", "rose" ], "allValues": [ "orchid", "rose", "jasmine" ] }
{ "flowerFieldA": [ "rose", "orchid" ], "flowerFieldB": [ ], "allValues": [ "orchid", "rose" ] }
{ "flowerFieldA": [ "rose", "orchid" ], "flowerFieldB": [ [ "rose" ], [ "orchid" ] ], "allValues": [ "orchid", "rose", [ "rose" ], [ "orchid" ] ] }
{ "flowerFieldA": [ "rose", "orchid" ], "flowerFieldB": [ [ "rose", "orchid" ] ], "allValues": [ "orchid", "rose", [ "rose", "orchid" ] ] }
{ "flowerFieldA": [ ], "flowerFieldB": [ ], "allValues": [ ] }
{ "flowerFieldA": [ ], "flowerFieldB": [ "rose" ], "allValues": [ "rose" ] }
```

## Limitations

- `$setUnion` only supports arrays and expressions that resolve to an
array.

- `$setUnion` does not guarantee the order of the elements in the
output array.

## Learn More

- :pipeline:`$bucket`
- :pipeline:`$bucketAuto`
- :pipeline:`$group`
- :pipeline:`$setWindowFields`
