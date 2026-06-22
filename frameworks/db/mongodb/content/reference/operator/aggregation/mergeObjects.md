---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/mergeObjects.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================

# $mergeObjects (accumulator operator)

## Definition

Combines multiple documents into a single document.

:expression:`$mergeObjects` is available in these stages:

- :pipeline:`$bucket`
- :pipeline:`$bucketAuto`
- :pipeline:`$group`
- :pipeline:`$replaceRoot`
## Syntax

When used as a :pipeline:`$bucket`, :pipeline:`$bucketAuto`, or :pipeline:`$group` stage accumulator, :expression:`$mergeObjects` has this syntax:

```none
{ $mergeObjects: <document> }
```

When used in other expressions (including in :pipeline:`$bucket`, :pipeline:`$bucketAuto`, and :pipeline:`$group` stages) but not as an accumulator, :expression:`$mergeObjects` has this syntax:

```none
{ $mergeObjects: [ <document1>, <document2>, ... ] }
```

The `<document>` can be any valid `expression <aggregation-expressions>` that resolves to a document.

## Behavior

:expression:`$mergeObjects` ignores `null` operands. If all the operands to :expression:`$mergeObjects` resolves to null, :expression:`$mergeObjects` returns an empty document `{ }`.

:expression:`$mergeObjects` overwrites the field values as it merges the documents. If documents to merge include the same field name, the field, in the resulting document, has the value from the last document merged for the field.

## Examples

### `$mergeObjects`

Create a collection `orders` with the following documents:

```javascript
db.orders.insertMany( [
  { "_id" : 1, "item" : "abc", "price" : 12, "ordered" : 2 },
  { "_id" : 2, "item" : "jkl", "price" : 20, "ordered" : 1 }
] )
```

Create another collection `items` with the following documents:

```javascript
db.items.insertMany( [
  { "_id" : 1, "item" : "abc", description: "product 1", "instock" : 120 },
  { "_id" : 2, "item" : "def", description: "product 2", "instock" : 80 },
  { "_id" : 3, "item" : "jkl", description: "product 3", "instock" : 60 }
] )
```

The following operation first uses the :pipeline:`$lookup` stage to join the two collections by the `item` fields and then uses :expression:`$mergeObjects` in the :pipeline:`$replaceRoot` to merge the joined documents from `items` and `orders`:

```javascript
db.orders.aggregate( [
   {
      $lookup: {
         from: "items",
         localField: "item",    // field in the orders collection
         foreignField: "item",  // field in the items collection
         as: "fromItems"
      }
   },
   {
      $replaceRoot: { newRoot: { $mergeObjects: [ { $arrayElemAt: [ "$fromItems", 0 ] }, "$$ROOT" ] } }
   },
   { $project: { fromItems: 0 } }
] )
```

The operation returns the following documents:

```javascript
{
  _id: 1,
  item: 'abc',
  description: 'product 1',
  instock: 120,
  price: 12,
  ordered: 2
},
{
  _id: 2,
  item: 'jkl',
  description: 'product 3',
  instock: 60,
  price: 20,
  ordered: 1
}
```

### `$mergeObjects` as an Accumulator

Create a collection `sales` with the following documents:

```javascript
db.sales.insertMany( [
   { _id: 1, year: 2017, item: "A", quantity: { "2017Q1": 500, "2017Q2": 500 } },
   { _id: 2, year: 2016, item: "A", quantity: { "2016Q1": 400, "2016Q2": 300, "2016Q3": 0, "2016Q4": 0 } } ,
   { _id: 3, year: 2017, item: "B", quantity: { "2017Q1": 300 } },
   { _id: 4, year: 2016, item: "B", quantity: { "2016Q3": 100, "2016Q4": 250 } } 
] )
```

The following operation uses :expression:`$mergeObjects` as a accumulator in a :pipeline:`$group` stage that groups documents by the `item` field:

> **Note:** When used as an accumulator, :expression:`$mergeObjects` operator
accepts a single operand.

```javascript
db.sales.aggregate( [
   { $group: { _id: "$item", mergedSales: { $mergeObjects: "$quantity" } } }
] )
```

The operation returns the following documents:

```javascript
{
  _id: 'A',
  mergedSales: { '2017Q1': 500, '2017Q2': 500, '2016Q1': 400, '2016Q2': 300, '2016Q3': 0, '2016Q4': 0 }
},
{
  _id: 'B',
  mergedSales: { '2017Q1': 300, '2016Q3': 100, '2016Q4': 250 }
}
```

> **Note:** If the documents to merge include the same field name, the field in
the resulting document has the value from the last document merged
for the field.
