---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/update/currentDate.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# $currentDate (update operator)

## Definition

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

The :update:`$currentDate` operator has the form:

```javascript
{ $currentDate: { <field1>: <typeSpecification1>, ... } }
```

`<typeSpecification>` can be either:

- a boolean `true` to set the field value to the current date as a
Date, or

- a document `{ $type: "timestamp" }` or `{ $type: "date" }`
which explicitly specifies the type. The operator is case-sensitive and accepts only the lowercase `"timestamp"` or the lowercase `"date"`.

.. include:: /includes/use-dot-notation.rst

## Behavior

.. include:: /includes/fact-update-operator-processing-order.rst

.. include:: /includes/update-current-date.rst

If the field does not exist, :update:`$currentDate` adds the field to a document.

.. include:: /includes/extracts/update-operation-empty-operand-expressions-current-date.rst

## Example

Create a sample collection `customers` with the following document:

```javascript
db.customers.insertOne( 
   { _id: 1, status: "a", lastModified: ISODate("2013-10-02T01:11:18.965Z") }
)
```

The following operation updates the `lastModified` field to the current date, the `"cancellation.date"` field to the current timestamp as well as updating the `status` field to `"D"` and the `"cancellation.reason"` to `"user request"`.

```javascript
db.customers.updateOne(
   { _id: 1 },
   {
     $currentDate: {
        lastModified: true,
        "cancellation.date": { $type: "timestamp" }
     },
     $set: {
        "cancellation.reason": "user request",
        status: "D"
     }
   }
)
```

.. include:: /includes/update-current-date.rst

To verify the update:

```javascript
db.customers.find()
```

The updated document resembles:

```javascript
{
   "_id" : 1,
   "status" : "D",
   "lastModified" : ISODate("2020-01-22T21:21:41.052Z"),
   "cancellation" : {
      "date" : Timestamp(1579728101, 1),
      "reason" : "user request"
   }
}
```

The `lastModified` field is set to the date when :update:`$currentDate` was run in the update example shown earlier.

### Aggregation Alternative to `$currentDate`

Update methods can accept an aggregation pipeline. Specifically, the previous example can be rewritten as the following using the aggregation stage :pipeline:`$set` and the aggregation variables :variable:`NOW` (for the current datetime) and :variable:`CLUSTER_TIME` (for the current timestamp):

> **Tip:** - To access aggregation variables, prefix the variable with double
  dollar signs `$$` and enclose in quotes.
- :variable:`CLUSTER_TIME` is available only on replica sets and
  sharded clusters.
- The :variable:`NOW` and :variable:`CLUSTER_TIME` values remain the
  same throughout the pipeline.

```javascript
db.customers.updateOne(
  { _id: 1 },
  [
   { $set: { lastModified: "$$NOW", cancellation: {date: "$$CLUSTER_TIME", reason: "user request"}, status: "D" } }
  ]
)
```

After the operation, you can query the collection to verify the update:

```javascript
db.customers.find().pretty()
```

The query should return the following document:

```javascript
{
   "_id" : 1,
   "status" : "D",
   "lastModified" : ISODate("2020-01-22T21:02:18.994Z"),
   "cancellation" : {
      "date" : Timestamp(1579726934, 2),
      "reason" : "user request"
   }
}
```

> **Seealso:** - :method:`db.collection.updateOne()`
- :method:`db.collection.updateMany()`
- :method:`db.collection.findAndModify()`
- :method:`db.collection.findOneAndUpdate()`
