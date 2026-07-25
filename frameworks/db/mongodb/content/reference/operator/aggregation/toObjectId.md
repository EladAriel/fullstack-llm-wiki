---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/toObjectId.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==================================

# $toObjectId  (expression operator)

## Definition

## Behavior

The following table lists the input types that can be converted to an ObjectId:

The following table lists some conversion to date examples:

## Example

Create a collection `orders` with the following documents:

```javascript
db.orders.insertMany( [
   { _id: "5ab9cbe531c2ab715d42129a", item: "apple", qty: 10 },
   { _id: ObjectId("5ab9d0b831c2ab715d4212a8"), item: "pie", qty: 5 },
   { _id: ObjectId("5ab9d2d331c2ab715d4212b3"), item: "ice cream", qty: 20 },
   { _id: "5ab9e16431c2ab715d4212b4", item: "almonds", qty: 50 },
] )
```

The following aggregation operation on the `orders collection converts the id` to ObjectId before sorting by the value:

```javascript
// Define stage to add convertedId field with converted _id value

idConversionStage = { 
   $addFields: { 
      convertedId: { $toObjectId: "$_id" }
   }
};

// Define stage to sort documents by the converted qty values

sortStage = {
   $sort: { "convertedId": -1 }
};

db.orders.aggregate( [
   idConversionStage,
   sortStage
] )
```

The operation returns the following documents:

```javascript
{
  _id: '5ab9e16431c2ab715d4212b4',
  item: 'almonds',
  qty: 50,
  convertedId: ObjectId("5ab9e16431c2ab715d4212b4")
},
{
  _id: ObjectId("5ab9d2d331c2ab715d4212b3"),
  item: 'ice cream',
  qty: 20,
  convertedId: ObjectId("5ab9d2d331c2ab715d4212b3")
},
{
  _id: ObjectId("5ab9d0b831c2ab715d4212a8"),
  item: 'pie',
  qty: 5,
  convertedId: ObjectId("5ab9d0b831c2ab715d4212a8")
},
{
  _id: '5ab9cbe531c2ab715d42129a',
  item: 'apple',
  qty: 10,
  convertedId: ObjectId("5ab9cbe531c2ab715d42129a")
}
```

.. include:: /includes/note-conversion-error-use-convert.rst
