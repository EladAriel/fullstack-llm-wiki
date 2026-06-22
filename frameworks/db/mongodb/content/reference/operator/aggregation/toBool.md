---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/toBool.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# $toBool (expression operator)

## Definition

## Behavior

The following table lists the input types that can be converted to a boolean:

.. include:: /includes/aggregation/convert-to-bool-table.rst

The following table lists some conversion to boolean examples:

## Example

Create a collection `orders` with the following documents:

```javascript
db.orders.insertMany( [
   { _id: 1, item: "apple",  qty: 5, shipped: true },
   { _id: 2, item: "pie",  qty: 10, shipped: 0  },
   { _id: 3, item: "ice cream", shipped: 1 },
   { _id: 4, item: "almonds", qty: 2, shipped: "true" },
   { _id: 5, item: "pecans", shipped: "false" },  // Note: All strings convert to true
   { _id: 6, item: "nougat", shipped: ""  }       // Note: All strings convert to true
] )
```

The following aggregation operation on the `orders` collection converts the `shipped` to a boolean value before finding the unshipped orders:

```javascript
// Define stage to add convertedShippedFlag field with the converted shipped value
// Because all strings convert to true, include specific handling for "false" and "" 

shippedConversionStage = {
   $addFields: {
      convertedShippedFlag: { 
         $switch: { 
            branches: [
              { case: { $eq: [ "$shipped", "false" ] }, then: false } , 
              { case: { $eq: [ "$shipped", "" ] }, then: false }
            ],
            default: { $toBool: "$shipped" }
        }
      }
   }
};

// Define stage to filter documents and pass only the unshipped orders

unshippedMatchStage = {
   $match: { "convertedShippedFlag": false }
};

db.orders.aggregate( [
  shippedConversionStage,
  unshippedMatchStage
] )
```

The operation returns the following document:

```javascript
{ "_id" : 2, "item" : "pie", "qty" : 10, "shipped" : 0, "convertedShippedFlag" : false }
{ "_id" : 5, "item" : "pecans", "shipped" : "false", "convertedShippedFlag" : false }
{ "_id" : 6, "item" : "nougat", "shipped" : "", "convertedShippedFlag" : false }
```

.. include:: /includes/note-conversion-error-use-convert.rst
