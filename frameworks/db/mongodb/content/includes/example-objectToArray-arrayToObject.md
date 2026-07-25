---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/example-objectToArray-arrayToObject.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Consider an `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [
   { _id: 1, item: "ABC1", instock: { warehouse1: 2500, warehouse2: 500 } },
   { _id: 2, item: "ABC2", instock: { warehouse2: 500, warehouse3: 200},
   }
] )
```

The following aggregation pipeline operation calculates the total in stock for each item and adds to the `instock` document:

```javascript
db.inventory.aggregate( [
   { $addFields: { instock: { $objectToArray: "$instock" } } },
   { $addFields: { instock: { $concatArrays: [ "$instock", [ { "k": "total", "v": { $sum: "$instock.v" } } ] ] } } } ,
   { $addFields: { instock: { $arrayToObject: "$instock" } } }
] )
```

The operation returns the following:

```javascript
{ _id: 1, item: "ABC1", instock: { warehouse1: 2500, warehouse2: 500, total: 3000 } }
{ _id: 2, item: "ABC2", instock: { warehouse2: 500, warehouse3: 200, total: 700 } }
```
