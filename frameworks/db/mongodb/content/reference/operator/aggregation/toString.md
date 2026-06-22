---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/toString.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================

# $toString  (expression operator)

## Definition

## Behavior

.. include:: /includes/convert-string-types.rst

.. include:: /includes/strings-to-non-decimal.rst

The following table lists some conversion to string examples:

## Example

Create a collection `orders` with the following documents:

```javascript
db.orders.insertMany( [
   { _id: 1, item: "apple",  qty: 5, zipcode: 93445 },
   { _id: 2, item: "almonds", qty: 2, zipcode: "12345-0030" },
   { _id: 3, item: "peaches",  qty: 5, zipcode: 12345 },
] )
```

The following aggregation operation on the `orders` collection converts the `zipcode` to string before sorting by the string value:

```javascript
// Define stage to add convertedZipCode field with the converted zipcode value

zipConversionStage = {
   $addFields: {
      convertedZipCode: { $toString: "$zipcode" }
   }
};

// Define stage to sort documents by the converted zipcode

sortStage = {
   $sort: { "convertedZipCode": 1 }
};

db.orders.aggregate( [
  zipConversionStage,
  sortStage
] )
```

The operation returns the following documents:

```javascript
{
  _id: 3,
  item: 'peaches',
  qty: 5,
  zipcode: 12345,
  convertedZipCode: '12345'
},
{
  _id: 2,
  item: 'almonds',
  qty: 2,
  zipcode: '12345-0030',
  convertedZipCode: '12345-0030'
},
{
  _id: 1,
  item: 'apple',
  qty: 5,
  zipcode: 93445,
  convertedZipCode: '93445'
}
```

.. include:: /includes/note-conversion-error-use-convert.rst
