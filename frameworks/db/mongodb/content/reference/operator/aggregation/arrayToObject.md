---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/arrayToObject.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

====================================

# $arrayToObject (expression operator)

## Definition

## Behavior

If you pass in an empty array to `$arrayToObject`, MongoDB creates an empty object.

If the name of a field repeats in the array,

- Starting in 4.0.5, :expression:`$arrayToObject` uses the last value
for that field. For 4.0.0-4.0.4, the value used depends on the driver.

- Starting in 3.6.10, :expression:`$arrayToObject` uses the last value
for that field. For 3.6.0-3.6.9, the value used depends on the driver.

- Starting in 3.4.19, :expression:`$arrayToObject` uses the last value
for that field. For 3.4.0-3.4.19, the value uses depends on the driver.

## Examples

### `$arrayToObject`  Example

Consider a `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [
   { _id: 1, item: "ABC1",  dimensions: [ { "k": "l", "v": 25} , { "k": "w", "v": 10 }, { "k": "uom", "v": "cm" } ] },
   { _id: 2, item: "ABC2",  dimensions: [ [ "l", 50 ], [ "w",  25 ], [ "uom", "cm" ] ] },
   { _id: 3, item: "ABC3",  dimensions: [ [ "l", 25 ], [ "l",  "cm" ], [ "l", 50 ] ] }
] )
```

The following aggregation pipeline operation use the :expression:`$arrayToObject` to return the `dimensions` field as a document:

```javascript
db.inventory.aggregate(
   [
      {
         $project: {
            item: 1,
            dimensions: { $arrayToObject: "$dimensions" }
         }
      }
   ]
)
```

The operation returns the following:

```javascript
{ _id: 1, item: "ABC1", dimensions: { "l" : 25, "w" : 10, "uom" : "cm" } }
{ _id: 2, item: "ABC2", dimensions: { "l" : 50, "w" : 25, "uom" : "cm" } }
{ _id: 3, item: "ABC3", dimensions: { "l" : 50 } }
```

Starting in versions 4.0.5+ (3.6.10+ and 3.4.19+), if the name of a field repeats in the array, :expression:`$arrayToObject` uses the last value for that field.

### `$objectToArray` + `$arrayToObject` Example

.. include:: /includes/example-objectToArray-arrayToObject.rst

> **Seealso:** :expression:`$objectToArray`
