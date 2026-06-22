---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/example-addToSet-each.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
