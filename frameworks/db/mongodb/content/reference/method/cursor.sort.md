---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.sort.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# cursor.sort() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The :method:`~cursor.sort()` method has the following parameter:

The `sort` parameter contains field and value pairs, in the following form:

```javascript
{ field: value }
```

The sort document can specify `ascending or descending sort on existing fields <sort-asc-desc>` or `sort on text score metadata <sort-metadata>`.

## Behavior

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
] );
```

The following command uses the :method:`~cursor.sort()` method to sort on the `borough` field:

```js
db.restaurants.find().sort( { "borough": 1 } )
```

In this example, sort order may be inconsistent, since the `borough` field contains duplicate values for both `Manhattan` and `Brooklyn`. Documents are returned in alphabetical order by `borough`, but the order of those documents with duplicate values for `borough` might not be the same across multiple executions of the same sort. For example, here are the results from two different executions of the above command:

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

To achieve a consistent sort, add a field which contains exclusively unique values to the sort. The following command uses the :method:`~cursor.sort()` method to sort on both the `borough field and the id` field:

```js
db.restaurants.find().sort( { "borough": 1, "_id": 1 } )
```

Since the `_id` field is always guaranteed to contain exclusively unique values, the returned sort order will always be the same across multiple executions of the same sort.

> **Important:** .. include:: /includes/8.0-non-existent-field-sort.rst

### Ascending/Descending Sort

Specify in the sort parameter the field or fields to sort by and a value of `1` or `-1` to specify an ascending or descending sort respectively.

The following operation sorts the documents first by the `age` field in descending order and then by the `posts` field in ascending order:

```javascript
db.users.find({ }).sort( { age : -1, posts: 1 } )
```

.. include:: /includes/fact-sort-order.rst

For details on the comparison/sort order for specific types, see `bson-types-comparison-order`.

### Text Score Metadata Sort

.. include:: /includes/text-search-legacy-atlas-section.rst

If you use :query:`$text`, you can sort by descending relevance score using the :expression:`{ $meta: "textScore" } <$meta>` expression.

The following sample document specifies a descending sort by the `"textScore"` metadata:

```javascript
db.users.find(
   { $text: { $search: "operating" } },
   { score: { $meta: "textScore" }}  
).sort({ score: { $meta: "textScore" } })
```

The `"textScore"` metadata sorts in descending order.

For more information, see :expression:`$meta` for details.

### Sort by an Array Field

.. include:: /includes/array-sort-example-setup.rst

The following queries sort the documents by the `sizes` field in ascending and descending order:

```javascript
// Ascending sort
db.shoes.find().sort( { sizes: 1 } )

// Descending sort
db.shoes.find().sort( { sizes: -1 } )
```

.. include:: /includes/array-sort-example-explanation.rst

Filter and Sort by an Array Field `````````````````````````````````

.. include:: /includes/array-filter-and-sort-example-setup.rst

```javascript
db.shoes.find( { sizes: { $gt: 9 } } ).sort( { sizes: 1 } )
```

.. include:: /includes/array-filter-and-sort-example-explanation.rst

> **Tip:** To only consider matched values as potential sort keys, you can
generate a new field containing the matched values and sort on that
field. For more information, see these pipeline stages and
expressions:
- :pipeline:`$addFields`
- :expression:`$filter`
- :pipeline:`$sort`

### Sort and Index Use

MongoDB can obtain the results of a sort operation from an index which includes the sort fields. MongoDB may use multiple indexes to support a sort operation if the sort uses the same indexes as the query predicate.

If MongoDB cannot use an index or indexes to obtain the sort order, MongoDB must perform an in-memory sort operation on the data.

Sort operations that use an index often have better performance than in-memory sorts. For more information on creating indexes to support sort operations, see `sorting-with-indexes`.

To check if MongoDB must perform an in-memory sort, append :method:`cursor.explain()` to the query and check the `explain results <explain-results>`. If the query plan contains a `SORT` stage, then MongoDB must perform an in-memory sort operation.

To prevent in-memory sorts from consuming too much memory:

- Create an index to support the sort operation. See
`/tutorial/sort-results-with-indexes` for more information and examples.

- Limit the amount of data to sort by using :method:`cursor.limit()`
with :method:`cursor.sort()`. See `sort-limit-results` for more information and examples.

> **Seealso:** :limit:`Memory Limits on Sort Operations <Sort Operations>`

### Limit Results

You can use :method:`~cursor.sort()` in conjunction with :method:`~cursor.limit()` to return the first (in terms of the sort order) `k` documents, where `k` is the specified limit.

If MongoDB cannot obtain the sort order via an index scan, then MongoDB uses a top-k sort algorithm. This algorithm buffers the first `k` results (or last, depending on the sort order) seen so far by the underlying index or collection access. If at any point the memory footprint of these `k` results exceeds 100 megabytes, the query will fail unless the query specifies :method:`cursor.allowDiskUse()`.

> **Seealso:** :limit:`Memory Limits on Sort Operations <Sort Operations>`

### Interaction with Projection

When an operation both sorts and `projects <projection>` with the same fields, MongoDB sorts on the original field values before applying the projection.

## Examples

A collection `orders` contain the following documents:

```javascript
db.orders.insertMany( [
   { _id: 1, item: { category: "cake", type: "chiffon" }, amount: 10 },
   { _id: 2, item: { category: "cookies", type: "chocolate chip" }, amount: 50 },
   { _id: 3, item: { category: "cookies", type: "chocolate chip" }, amount: 15 },
   { _id: 4, item: { category: "cake", type: "lemon" }, amount: 30 },
   { _id: 5, item: { category: "cake", type: "carrot" }, amount: 20 },
   { _id: 6, item: { category: "brownies", type: "blondie" }, amount: 10 }
] )
```

The following query, which returns all documents from the `orders` collection, does not specify a sort order:

```javascript
db.orders.find()
```

The query returns the documents in indeterminate order:

```javascript
{ _id: 1, item: { category: "cake", type: "chiffon" }, amount: 10 }
{ _id: 2, item: { category: "cookies", type: "chocolate chip" }, amount: 50 }
{ _id: 3, item: { category: "cookies", type: "chocolate chip" }, amount: 15 }
{ _id: 4, item: { category: "cake", type: "lemon" }, amount: 30 }
{ _id: 5, item: { category: "cake", type: "carrot" }, amount: 20 }
{ _id: 6, item: { category: "brownies", type: "blondie" }, amount: 10 }
```

The following query specifies a sort on the `amount` field in descending order.

```javascript
db.orders.find().sort( { amount: -1 } )
```

The query returns the following documents, in descending order of `amount`:

```javascript
{ _id: 2, item: { category: "cookies", type: "chocolate chip" }, amount: 50 }
{ _id: 4, item: { category: "cake", type: "lemon" }, amount: 30 }
{ _id: 5, item: { category: "cake", type: "carrot" }, amount: 20 }
{ _id: 3, item: { category: "cookies", type: "chocolate chip" }, amount: 15 }
{ _id: 1, item: { category: "cake", type: "chiffon" }, amount: 10 }
{ _id: 6, item: { category: "brownies", type: "blondie" }, amount: 10 }
```

The following query specifies the sort order using the fields from an embedded document `item`. The query sorts first by the `category` field in ascending order, and then within each `category`, by the `type` field in ascending order.

```javascript
db.orders.find().sort( { "item.category": 1, "item.type": 1 } )
```

The query returns the following documents, ordered first by the `category` field, and within each category, by the `type` field:

```javascript
{ _id: 6, item: { category: "brownies", type: "blondie" }, amount: 10 }
{ _id: 5, item: { category: "cake", type: "carrot" }, amount: 20 }
{ _id: 1, item: { category: "cake", type: "chiffon" }, amount: 10 }
{ _id: 4, item: { category: "cake", type: "lemon" }, amount: 30 }
{ _id: 2, item: { category: "cookies", type: "chocolate chip" }, amount: 50 }
{ _id: 3, item: { category: "cookies", type: "chocolate chip" }, amount: 15 }
```

## Return in Natural Order

The :operator:`$natural` parameter returns items according to their `natural order` within the database. This ordering is an internal implementation feature, and you should not rely on any particular ordering of the documents.

> **Note:** .. include:: /includes/natural-sort-7.0-breaking-change.rst

### Index Use

Queries that include a sort by :operator:`$natural order do **not** use indexes to fulfill the query predicate with the following exception: If the query predicate is an equality condition on the id` field `{ _id: <value> }`, then the query with the sort by :operator:`$natural order can use the id` index.

> **Seealso:** :operator:`$natural`
