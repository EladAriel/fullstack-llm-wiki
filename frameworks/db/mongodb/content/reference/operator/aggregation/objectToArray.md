---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/objectToArray.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================

# $objectToArray (expression operator)

## Definition

## Behavior

For more information on expressions, see `aggregation-expressions`.

## Examples

### `$objectToArray` Example

Consider a `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [
   { _id: 1, item: "ABC1",  dimensions: { l: 25, w: 10, uom: "cm" } },
   { _id: 2, item: "ABC2",  dimensions: { l: 50, w: 25, uom: "cm" } },
   { _id: 3, item: "XYZ1",  dimensions: { l: 70, w: 75, uom: "cm" } }
] )
```

The following aggregation pipeline operation use the :expression:`$objectToArray` to return the `dimensions` field as an array:

```javascript
db.inventory.aggregate(
   [
      {
         $project: {
            item: 1,
            dimensions: { $objectToArray: "$dimensions" }
         }
      }
   ]
)
```

The operation returns the following:

```javascript
{ _id: 1, item: "ABC1", dimensions: [ { "k" : "l", "v" : 25 }, { "k" : "w", "v" : 10 }, { "k" : "uom", "v" : "cm" } ] }
{ _id: 2, item: "ABC2", dimensions: [ { "k" : "l", "v" : 50 }, { "k" : "w", "v" : 25 }, { "k" : "uom", "v" : "cm" } ] }
{ _id: 3, item: "XYZ1", dimensions: [ { "k" : "l", "v" : 70 }, { "k" : "w", "v" : 75 }, { "k" : "uom", "v" : "cm" } ] }
```

### `$objectToArray` to Sum Nested Fields

Consider a `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [ 
   { _id: 1, item: "ABC1", instock: { warehouse1: 2500, warehouse2: 500 } }
   { _id: 2, item: "ABC2", instock: { warehouse2: 500, warehouse3: 200} }
] )
```

The following aggregation pipeline operation uses the :expression:`$objectToArray` along with :pipeline:`$unwind` and :pipeline:`$group` to calculate the total items in stock per warehouse.

```javascript
db.inventory.aggregate([
   { $project: { warehouses: { $objectToArray: "$instock" } } },
   { $unwind: "$warehouses" },
   { $group: { _id: "$warehouses.k", total: { $sum: "$warehouses.v" } } } 
])
```

The operation returns the following:

```javascript
{ _id: "warehouse3", total: 200 }
{ _id: "warehouse2", total: 1000 }
{ _id: "warehouse1", total: 2500 }
```

### `$objectToArray` + `$arrayToObject` Example

.. include:: /includes/example-objectToArray-arrayToObject.rst

> **Seealso:** :expression:`$arrayToObject`
