---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/subtract.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# $subtract (expression operator)

## Definition

## Behavior

.. include:: /includes/agg-expression-order-of-return-behavior.rst

.. include:: /includes/agg-expression-mixed-input-types-with-date.rst

## Examples

Consider a `sales` collection with the following documents:

```javascript
db.sales.insertMany([
   { "_id" : 1, "item" : "abc", "price" : 10, "fee" : 2, "discount" : 5, "date" : ISODate("2014-03-01T08:00:00Z") },
   { "_id" : 2, "item" : "jkl", "price" : 20, "fee" : 1, "discount" : 2, "date" : ISODate("2014-03-01T09:00:00Z") }
])
```

### Subtract Numbers

The following aggregation uses the :expression:`$subtract` expression to compute the `total` by subtracting the `discount` from the subtotal of `price` and `fee`.

```javascript
db.sales.aggregate( [ { $project: { item: 1, total: { $subtract: [ { $add: [ "$price", "$fee" ] }, "$discount" ] } } } ] )
```

The operation returns the following results:

```javascript
{ "_id" : 1, "item" : "abc", "total" : 7 }
{ "_id" : 2, "item" : "jkl", "total" : 19 }
```

### Subtract Two Dates

The following aggregation uses the :expression:`$subtract` expression to subtract `$date` from the current date, using the system :variable:`NOW` and returns the difference in milliseconds:

```javascript
db.sales.aggregate( [ { $project: { item: 1, dateDifference: { $subtract: [ "$$NOW", "$date" ] } } } ] )
```

Alternatively, you can use the :method:`Date()` for the current date:s

```javascript
db.sales.aggregate( [ { $project: { item: 1, dateDifference: { $subtract: [ new Date(), "$date" ] } } } ] )
```

Both operations return documents that resemble the following:

```javascript
{ "_id" : 1, "item" : "abc", "dateDifference" : Long("186136746187") }
{ "_id" : 2, "item" : "jkl", "dateDifference" : Long("186133146187") }
```

### Subtract Milliseconds from a Date

The following aggregation uses the :expression:`$subtract` expression to subtract 5  60  1000 milliseconds (5 minutes) from the "$date" field:

```javascript
db.sales.aggregate( [ { $project: { item: 1, dateDifference: { $subtract: [ "$date", 5 * 60 * 1000 ] } } } ] )
```

The operation returns the following results:

```javascript
{ "_id" : 1, "item" : "abc", "dateDifference" : ISODate("2014-03-01T07:55:00Z") }
{ "_id" : 2, "item" : "jkl", "dateDifference" : ISODate("2014-03-01T08:55:00Z") }
```
