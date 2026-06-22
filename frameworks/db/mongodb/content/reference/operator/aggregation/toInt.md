---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/toInt.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# $toInt (expression operator)

## Definition

## Behavior

The following table lists the input types that can be converted to an integer:

.. include:: /includes/strings-to-non-decimal.rst

The following table lists some conversion to integer examples:

## Example

Create a collection `orders` with the following documents:

```javascript
db.orders.insertMany( [
   { _id: 1, item: "apple", qty: "5", price: 10 },
   { _id: 2, item: "pie", qty: "10", price: Decimal128("20.0") },
   { _id: 3, item: "ice cream", qty: "2", price: "4.99" },
   { _id: 4, item: "almonds" ,  qty: "5", price: 5 }
] )
```

The following aggregation operation:

- converts `qty` to an integer,
- converts `price` to a decimal,
- calculates the total price:
```javascript
// Define stage to add convertedPrice and convertedQty fields with the converted price and qty values

priceQtyConversionStage = { 
   $addFields: { 
      convertedPrice: { $toDecimal: "$price" },
      convertedQty: { $toInt: "$qty" },
   }
};

// Define stage to calculate total price by multiplying convertedPrice and convertedQty fields 

totalPriceCalculationStage = { 
   $project: { item: 1, totalPrice: { $multiply: [ "$convertedPrice", "$convertedQty" ] } }
};

db.orders.aggregate( [
   priceQtyConversionStage,
   totalPriceCalculationStage
] )
```

The operation returns the following documents:

```javascript
{ _id: 1, item: 'apple', totalPrice: Decimal128("50") },
{ _id: 2, item: 'pie', totalPrice: Decimal128("200.0") },
{ _id: 3, item: 'ice cream', totalPrice: Decimal128("9.98") },
{ _id: 4, item: 'almonds', totalPrice: Decimal128("25") }
```

.. include:: /includes/note-conversion-error-use-convert.rst
