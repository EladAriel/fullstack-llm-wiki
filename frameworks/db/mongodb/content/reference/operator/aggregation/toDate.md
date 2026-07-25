---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/toDate.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=============================

# $toDate (expression operator)

## Definition

## Behavior

The following table lists the input types that can be converted to a date:

The following table lists some conversion to date examples:

## Example

Create a collection `orders` with the following documents:

```javascript
db.orders.insertMany( [
   { _id: 1, item: "apple", qty: 5, price: 2, order_date: new Date( "2018-03-20" ) },
   { _id: 2, item: "pie", qty: 10, price: 3, order_date: new Date( "2018-03-22" ) },
   { _id: 3, item: "ice cream", qty: 2, price: 4, order_date: "2018-03-15" },
   { _id: 4, item: "almonds" , qty: 5, price: 7, order_date: "2018-03-15 +10:00" }
] )
```

The following aggregation operation on the `orders` collection converts the `order_date` to date before sorting by the date value:

```javascript
// Define stage to add convertedDate field with the converted order_date value

dateConversionStage = { 
   $addFields: { 
      convertedDate: { $toDate: "$order_date" }
   }
};

// Define stage to sort documents by the converted date

sortStage = {
   $sort: { "convertedDate": 1 }
};

db.orders.aggregate( [
   dateConversionStage,
   sortStage
] )
```

The operation returns the following documents:

```javascript
{
   _id: 4,
   item: 'almonds',
   qty: 5,
   price: 7,
   order_date: '2018-03-15 +10:00',
   convertedDate: ISODate("2018-03-14T14:00:00.000Z")
},
{
   _id: 3,
   item: 'ice cream',
   qty: 2,
   price: 4,
   order_date: '2018-03-15',
   convertedDate: ISODate("2018-03-15T00:00:00.000Z")
},
{
   _id: 1,
   item: 'apple',
   qty: 5,
   price: 2,
   order_date: ISODate("2018-03-20T00:00:00.000Z"),
   convertedDate: ISODate("2018-03-20T00:00:00.000Z")
},
{
   _id: 2,
   item: 'pie',
   qty: 10,
   price: 3,
   order_date: ISODate("2018-03-22T00:00:00.000Z"),
   convertedDate: ISODate("2018-03-22T00:00:00.000Z")
}
```

.. include:: /includes/note-conversion-error-use-convert.rst
