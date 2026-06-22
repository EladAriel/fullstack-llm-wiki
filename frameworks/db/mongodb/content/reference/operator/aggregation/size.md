---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/size.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# $size  (expression operator)

## Definition

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

:expression:`$size` has the following syntax:

```javascript
{ $size: <expression> }
```

The argument for :expression:`$size` can be any `expression <aggregation-expressions>` as long as it resolves to an array. For more information on expressions, see `aggregation-expressions`.

## Behavior

The argument for :expression:`$size` must resolve to an array. If the argument for :expression:`$size` is missing or does not resolve to an array, :expression:`$size` errors.

## Example

Consider an `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [
   { _id: 1, item: "ABC1", description: "product 1", colors: [ "blue", "black", "red" ] },
   { _id: 2, item: "ABC2", description: "product 2", colors: [ "purple" ] },
   { _id: 3, item: "XYZ1", description: "product 3", colors: [ ] },
   { _id: 4, item: "ZZZ1", description: "product 4 - missing colors" },
   { _id: 5, item: "ZZZ2", description: "product 5 - colors is string", colors: "blue,red" }
] )
```

The following aggregation pipeline operation uses the :expression:`$size` operator to return the number of elements in the `colors` array:

```javascript
db.inventory.aggregate([
   {
      $project: {
         item: 1,
         numberOfColors: { $cond: { if: { $isArray: "$colors" }, then: { $size: "$colors" }, else: "NA"} }
      } 
   }
] )
```

The operation returns the following:

```javascript
{ _id: 1, item: "ABC1", numberOfColors: 3 }
{ _id: 2, item: "ABC2", numberOfColors: 1 }
{ _id: 3, item: "XYZ1", numberOfColors: 0 }
{ _id: 4, item: "ZZZ1", numberOfColors: "NA" }
{ _id: 5, item: "ZZZ2", numberOfColors: "NA" }
```
