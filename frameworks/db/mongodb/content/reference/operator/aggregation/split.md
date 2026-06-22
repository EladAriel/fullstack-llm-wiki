---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/split.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# $split  (expression operator)

## Definition

## Behavior

The :expression:`$split` operator returns an array. The `<string expression>` input must be a string and the `<delimiter>` input must be a string or a regex pattern. Otherwise, the operation fails with an error.

## Example

A collection named `deliveries` contains the following documents:

```javascript
db.deliveries.insertMany( [
   { _id: 1, city: "Berkeley, CA", qty: 648 },
   { _id: 2, city: "Bend, OR", qty: 491 },
   { _id: 3, city: "Kensington, CA", qty: 233 },
   { _id: 4, city: "Eugene, OR", qty: 842 },
   { _id: 5, city: "Reno, NV", qty: 655 },
   { _id: 6, city: "Portland, OR", qty: 408 },
   { _id: 7, city: "Sacramento, CA", qty: 574 }
] )
```

The goal of following aggregation operation is to find the total quantity of deliveries for each state and sort the list in descending order. It has five pipeline stages:

- The :pipeline:`$project` stage produces documents with two fields,
`qty` (integer) and `city_state` (array). The `$split` operator creates an array of strings by splitting the `city` field, using a comma followed by a space (`", "`) as a delimiter.

- The :pipeline:`$unwind` stage creates a separate record for each
element in the `city_state` field.

- The :pipeline:`$match` stage uses a regular expression to filter out
the city documents, leaving only those containing a state.

- The :pipeline:`$group` stage groups all the states together and sums the
`qty` field.

- The :pipeline:`$sort` stage sorts the results by `total_qty` in
descending order.

```javascript
db.deliveries.aggregate( [
  { $project: { city_state: { $split: ["$city", ", "] }, qty: 1 } },
  { $unwind: "$city_state" },
  { $match: { city_state: /[A-Z]{2}/ } },
  { $group: { _id: { state: "$city_state" }, total_qty: { $sum: "$qty" } } },
  { $sort: { total_qty: -1 } }
] )
```

The operation returns the following results:

```javascript
[
   { _id: { state: "OR" }, total_qty: 1741 },
   { _id: { state: "CA" }, total_qty: 1455 },
   { _id: { state: "NV" }, total_qty: 655 }
]
```
