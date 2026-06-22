---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/reverseArray.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================

# $reverseArray  (expression operator)

## Definition

## Behavior

.. include:: /includes/extracts/agg-expression-null-operand-reverseArray.rst

`$reverseArray` returns an empty array when the argument is an empty array.

If the argument contains subarrays, `$reverseArray` only operates on the top level array elements and will not reverse the contents of subarrays.

The examples in the table take a literal argument. To avoid parsing ambiguity if the literal argument is an array, you must wrap the literal array in a :expression:`$literal` expression or keep the outer array that designates the argument list (e.g. `[ [ 1, 2, 3 ] ]` ) to pass in the literal array `[1, 2, 3]`.

## Example

A collection named `users` contains the following documents:

```javascript
db.users.insertMany( [
   { _id: 1, name: "dave123", favorites: [ "chocolate", "cake", "butter", "apples" ] },
   { _id: 2, name: "li", favorites: [ "apples", "pudding", "pie" ] },
   { _id: 3, name: "ahn", favorites: [ ] },
   { _id: 4, name: "ty" }
] )
```

The following example returns an array containing the elements of the `favorites` array in reverse order:

```javascript
db.users.aggregate([
   {
     $project:
      {
         name: 1,
         reverseFavorites: { $reverseArray: "$favorites" }
      }
   }
])
```

The operation returns the following results:

```javascript
[
   { _id: 1, name: "dave123", reverseFavorites: [ "apples", "butter", "cake", "chocolate" ] },
   { _id: 2, name: "li", reverseFavorites: [ "pie", "pudding", "apples" ] },
   { _id: 3, name: "ahn", reverseFavorites: [ ] },
   { _id: 4, name: "ty", reverseFavorites: null },
]
```
