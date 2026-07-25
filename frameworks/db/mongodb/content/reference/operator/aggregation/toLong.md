---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/toLong.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==============================

# $toLong  (expression operator)

## Definition

## Behavior

The following table lists the input types that can be converted to a long:

.. include:: /includes/strings-to-non-decimal.rst

The following table lists some conversion to long examples:

## Example

Create a collection `orders` with the following documents:

```javascript
db.orders.insertMany( [
   { _id: 1, item: "apple", qty: Int32(5) },
   { _id: 2, item: "pie", qty: "100" },
   { _id: 3, item: "ice cream", qty: Long("500") },
   { _id: 4, item: "almonds", qty: "50" },
] )
```

The following aggregation operation on the `orders` collection converts the `qty` to long before sorting by the value:

```javascript
// Define stage to add convertedQty field with converted qty value

qtyConversionStage = { 
   $addFields: { 
      convertedQty: { $toLong: "$qty" }
   }
};

// Define stage to sort documents by the converted qty values

sortStage = {
   $sort: { "convertedQty": -1 }
};

db.orders.aggregate( [
   qtyConversionStage,
   sortStage
])
```

The operation returns the following documents:

```javascript
{ _id: 3, item: 'ice cream', qty: Long("500"), convertedQty: Long("500") },
{ _id: 2, item: 'pie', qty: '100', convertedQty: Long("100") },
{ _id: 4, item: 'almonds', qty: '50', convertedQty: Long("50") },
{ _id: 1, item: 'apple', qty: 5, convertedQty: Long("5") }
```

.. include:: /includes/note-conversion-error-use-convert.rst
