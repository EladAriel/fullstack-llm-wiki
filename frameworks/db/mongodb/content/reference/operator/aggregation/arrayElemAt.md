---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/arrayElemAt.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# $arrayElemAt (expression operator)

## Definition

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

:expression:`$arrayElemAt` has the following syntax:

```javascript
{ $arrayElemAt: [ <array>, <idx> ] }
```

The `<array>` expression can be any valid `expression <aggregation-expressions>` that resolves to an array.

The `<idx>` expression can be any valid `expression <aggregation-expressions>` that resolves to an integer.

For more information on expressions, see `aggregation-expressions`.

## Behavior

- If the `<idx>` expression resolves to zero or a positive integer,
:expression:`$arrayElemAt` returns the element at the `idx` position, counting from the start of the array.

- If the `<idx>` expression resolves to a negative integer,
:expression:`$arrayElemAt` returns the element at the `idx` position, counting from the end of the array.

- If `idx` exceeds the array bounds, :expression:`$arrayElemAt` does
not return a result.

- If the `<array>` expression resolves to an undefined array,
:expression:`$arrayElemAt` returns `null`.

## Example

A collection named `users` contains the following documents:

```javascript
db.users.insertMany( [
   { _id: 1, name: "dave123", favorites: [ "chocolate", "cake", "butter", "apples" ] },
   { _id: 2, name: "li", favorites: [ "apples", "pudding", "pie" ] },
   { _id: 3, name: "ahn", favorites: [ "pears", "pecans", "chocolate", "cherries" ] },
   { _id: 4, name: "ty", favorites: [ "ice cream" ] }
] )
```

The following example returns the first and last element in the `favorites` array:

```javascript
db.users.aggregate([
   {
     $project:
      {
         name: 1,
         first: { $arrayElemAt: [ "$favorites", 0 ] },
         last: { $arrayElemAt: [ "$favorites", -1 ] }
      }
   }
])
```

The operation returns the following results:

```javascript
[
   { _id: 1, name: "dave123", first: "chocolate", "last" : "apples" },
   { _id: 2, name: "li", first: "apples", "last" : "pie" },
   { _id: 3, name: "ahn", first: "pears", "last" : "cherries" },
   { _id: 4, name: "ty", first: "ice cream", "last" : "ice cream" }
]
```

## See Also

- :expression:`$slice`
- :group:`$first`
- :group:`$last`
- `agg-quick-ref-operator-array`
