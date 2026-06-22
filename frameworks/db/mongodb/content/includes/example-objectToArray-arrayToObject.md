---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/example-objectToArray-arrayToObject.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
