---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/sort.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================

# $sort (aggregation stage)

## Definition

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

The :pipeline:`$sort` stage has the following prototype form:

```javascript
{ $sort: { <field1>: <sort order>, <field2>: <sort order> ... } }
```

:pipeline:`$sort` takes a document that specifies the field(s) to sort by and the respective sort order. `<sort order>` can have one of the following values:

If sorting on multiple fields, sort order is evaluated from left to right. For example, in the form above, documents are first sorted by `<field1>`. Then documents with the same `<field1>` values are further sorted by `<field2>`.

## Behavior

### Performance

.. include:: /includes/blocking-performance.rst

### Limits

.. include:: /includes/sort-limits.rst

### Sort Consistency

.. include:: /includes/fact-sort-consistency.rst

Consider the following `restaurant` collection:

```js
db.restaurants.insertMany( [
   { _id: 1, name: "Central Park Cafe", borough: "Manhattan"},
   { _id: 2, name: "Rock A Feller Bar and Grill", borough: "Queens"},
   { _id: 3, name: "Empire State Pub", borough: "Brooklyn"},
   { _id: 4, name: "Stan's Pizzaria", borough: "Manhattan"},
   { _id: 5, name: "Jane's Deli", borough: "Brooklyn"},
] )
```

The following command uses the :pipeline:`$sort` stage to sort on the `borough` field:

```js
db.restaurants.aggregate(
   [
     { $sort : { borough : 1 } }
   ]
)
```

In this example, sort order may be inconsistent, since the `borough` field contains duplicate values for both `Manhattan` and `Brooklyn`. Documents are returned in alphabetical order by `borough`, but the order of those documents with duplicate values for `borough` might not the be the same across multiple executions of the same sort. For example, here are the results from two different executions of the above command:

```js
{ _id: 3, name: "Empire State Pub", borough: "Brooklyn" }
{ _id: 5, name: "Jane's Deli", borough: "Brooklyn" }
{ _id: 1, name: "Central Park Cafe", borough: "Manhattan" }
{ _id: 4, name: "Stan's Pizzaria", borough: "Manhattan" }
{ _id: 2, name: "Rock A Feller Bar and Grill", borough: "Queens" }

{ _id: 5, name: "Jane's Deli", borough: "Brooklyn" }
{ _id: 3, name: "Empire State Pub", borough: "Brooklyn" }
{ _id: 4, name: "Stan's Pizzaria", borough: "Manhattan" }
{ _id: 1, name: "Central Park Cafe", borough: "Manhattan" }
{ _id: 2, name: "Rock A Feller Bar and Grill", borough: "Queens" }
```

While the values for `borough` are still sorted in alphabetical order, the order of the documents containing duplicate values for `borough` (i.e. `Manhattan` and `Brooklyn`) is not the same.

To achieve a consistent sort, add a field which contains exclusively unique values to the sort. The following command uses the :pipeline:`$sort` stage to sort on both the `borough field and the id` field:

```js
db.restaurants.aggregate(
   [
     { $sort : { borough : 1, _id: 1 } }
   ]
)
```

Since the `_id` field is always guaranteed to contain exclusively unique values, the returned sort order is always the same across multiple executions of the same sort.

### Sort by an Array Field

.. include:: /includes/array-sort-example-setup.rst

The following queries sort the documents by the `sizes` field in ascending and descending order:

```javascript
// Ascending sort
db.shoes.aggregate( [
   {
      $sort: { sizes: 1 }
   }
] )

// Descending sort
db.shoes.aggregate( [
   {
      $sort: { sizes: -1 }
   }
] )
```

.. include:: /includes/array-sort-example-explanation.rst

Filter and Sort by an Array Field `````````````````````````````````

.. include:: /includes/array-filter-and-sort-example-setup.rst

```javascript
db.shoes.aggregate( [
   {
      $match: { sizes: { $gt: 9 } }
   },
   {
      $sort: { sizes: 1 }
   }
] )
```

.. include:: /includes/array-filter-and-sort-example-explanation.rst

> **Tip:** To only consider matched values as potential sort keys, you can
generate a new field containing the matched values and sort on that
field. For more information, see these pipeline stages and
expressions:
- :pipeline:`$addFields`
- :expression:`$filter`

## `$sort` Operator and Memory

### `$sort` + `$limit` Memory Optimization

.. include:: /includes/fact-agg-sort-limit.rst

.. include:: /includes/fact-optimizations-subject-to-change.rst

### `$sort` and Memory Restrictions

.. include:: /includes/fact-allowDiskUseByDefault.rst

> **Note:** .. include:: /includes/fact-atlas-enable-autoscaling.rst

For additional details, see `agg-pipeline-limits`.

## `$sort` Operator and Performance

The :pipeline:`$sort` operator can take advantage of an index if it's used in the first stage of a pipeline or if it's only preceded by a :pipeline:`$match` stage.

When you use the :pipeline:`$sort` on a sharded cluster, each shard sorts its result documents using an index where available. Then the :binary:`~bin.mongos` or one of the shards performs a streamed merge sort.

## Examples

## Learn More

To see full aggregation examples that use the :pipeline:`$sort` stage, see the `aggregation-complete-examples`.
