---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/add.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# $add (expression operator)

## Definition

## Behavior

.. include:: /includes/agg-expression-order-of-return-behavior.rst

When mixing `document-bson-type-date` and non-integer operands, the `$add` operator evaluates the array of expressions from left to right and rounds numeric values before adding them to the `Date` value. For more information, see `add-operation-left-associative`.

## Examples

The following examples use a `sales` collection with the following documents:

```javascript
db.sales.insertMany( [
   { _id : 1, "item" : "abc", "price" : 10, "fee" : 2, date: ISODate("2014-03-01T08:00:00Z") },
   { _id : 2, "item" : "jkl", "price" : 20, "fee" : 1, date: ISODate("2014-03-01T09:00:00Z") },
   { _id : 3, "item" : "xyz", "price" : 5,  "fee" : 0, date: ISODate("2014-03-15T09:00:00Z") }
] )
```

### Add Numbers

The following aggregation uses the :expression:`$add` expression in the :pipeline:`$project` pipeline to calculate the total cost:

```javascript
db.sales.aggregate(
   [
     { $project: { item: 1, total: { $add: [ "$price", "$fee" ] } } }
   ]
)
```

The operation returns the following results:

```javascript
{ "_id" : 1, "item" : "abc", "total" : 12 }
{ "_id" : 2, "item" : "jkl", "total" : 21 }
{ "_id" : 3, "item" : "xyz", "total" : 5 }
```

### Perform Addition on a Date

The following aggregation uses the :expression:`$add` expression to compute the `billing_date` by adding `32460*60000` milliseconds (i.e. 3 days) to the `date` field :

```javascript
db.sales.aggregate(
   [
     { $project: { item: 1, billing_date: { $add: [ "$date", 3*24*60*60000 ] } } }
   ]
)
```

The operation returns the following results:

```javascript
{ "_id" : 1, "item" : "abc", "billing_date" : ISODate("2014-03-04T08:00:00Z") }
{ "_id" : 2, "item" : "jkl", "billing_date" : ISODate("2014-03-04T09:00:00Z") }
{ "_id" : 3, "item" : "xyz", "billing_date" : ISODate("2014-03-18T09:00:00Z") }
```

### Add Non-Integer Values to a Date

The following aggregation uses the `$add` expression to compute the `result` field by adding numeric values to the `date` field:

Note that, although the sum of non-date expressions is `6.1` milliseconds, the aggregation results in the initial `$date` field plus `7` milliseconds due to the `$add` operation's left associativity.

When `$add` evaluates the array of expressions from left to right, it first adds the two numeric values `1.5` and `1.6`. The resulting `3.1` is rounded to `3` before being added to the `$date` field. Next, it is added to the rounded value of `1.5` (which is `2`), and then to the rounded value of the final `1.5` (which is also `2`).
