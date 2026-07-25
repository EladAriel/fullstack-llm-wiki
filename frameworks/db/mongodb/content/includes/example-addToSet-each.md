---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/example-addToSet-each.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

A collection `inventory` has the following document:

```javascript
db.inventory.insertOne (
   { _id: 2, item: "cable", tags: [ "electronics", "supplies" ] }
)
```

Then the following operation uses the :update:`$addToSet` operator with the :update:`$each` modifier to add multiple elements to the `tags` array:

```javascript
db.inventory.updateOne(
   { _id: 2 },
   { $addToSet: { tags: { $each: [ "camera", "electronics", "accessories" ] } } }
 )
```

The operation only adds `"camera"` and `"accessories"` to the `tags` array. `"electronics"` was already in the array:

```javascript
{
  _id: 2,
  item: "cable",
  tags: [ "electronics", "supplies", "camera", "accessories" ]
}
```
