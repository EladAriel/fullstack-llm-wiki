---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/zip.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===========================

# $zip  (expression operator)

## Definition

## Behavior

The input arrays do not need to be of the same length. By default, the output array has the length of the shortest input array, but the `useLongestLength` option instructs :expression:`$zip` to output an array as long as the longest input array.

## Example

### Matrix Transposition

A collection called `matrices` contains the following documents:

```javascript
db.matrices.insertMany([
  { matrix: [[1, 2], [2, 3], [3, 4]] },
  { matrix: [[8, 7], [7, 6], [5, 4]] },
])
```

To compute the transpose of each 3x2 matrix in this collection, you can use the following aggregation operation:

```javascript
db.matrices.aggregate([{
  $project: {
    _id: false,
    transposed: {
      $zip: {
        inputs: [
          { $arrayElemAt: [ "$matrix", 0 ] },
          { $arrayElemAt: [ "$matrix", 1 ] },
          { $arrayElemAt: [ "$matrix", 2 ] },
        ]
      }
    }
  }
}])
```

This will return the following 2x3 matrices:

```javascript
{ "transposed" : [ [ 1, 2, 3 ], [ 2, 3, 4 ] ] }
{ "transposed" : [ [ 8, 7, 5 ], [ 7, 6, 4 ] ] }
```

### Filtering and Preserving Indexes

You can use `$zip` with :expression:`$filter` to obtain a subset of elements in an array, saving the original index alongside each retained element.

A collection called `pages` contains the following document:

```javascript
db.pages.insertOne( {
  "category": "unix",
  "pages": [
    { "title": "awk for beginners", reviews: 5 },
    { "title": "sed for newbies", reviews: 0 },
    { "title": "grep made simple", reviews: 2 },
] } )
```

The following aggregation pipeline will first zip the elements of the `pages` array together with their index, and then filter out only the pages with at least one review:

```javascript
db.pages.aggregate([{
  $project: {
    _id: false,
    pages: {
      $filter: {
        input: {
          $zip: {
            inputs: [ "$pages", { $range: [0, { $size: "$pages" }] } ]
          }
        },
        as: "pageWithIndex",
        cond: {
          $let: {
            vars: {
              page: { $arrayElemAt: [ "$$pageWithIndex", 0 ] }
            },
            in: { $gte: [ "$$page.reviews", 1 ] }
          }
        }
      }
    }
  }
}])
```

This will return the following document:

```javascript
{
  "pages" : [
    [ { "title" : "awk for beginners", "reviews" : 5 }, 0 ],
    [ { "title" : "grep made simple", "reviews" : 2 }, 2 ] ]
}
```
