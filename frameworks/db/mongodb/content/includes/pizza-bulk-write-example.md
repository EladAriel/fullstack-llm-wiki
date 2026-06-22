---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/pizza-bulk-write-example.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The following :method:`db.collection.bulkWrite()` example runs the following operations on the `pizzas` collection:

- Adds two documents using `insertOne`.
- Updates a document using `updateOne`.
- Deletes a document using `deleteOne`.
- Replaces a document using `replaceOne`.
```javascript
try {
   db.pizzas.bulkWrite( [
      { insertOne: { document: { _id: 3, type: "beef", size: "medium", price: 6 } } },
      { insertOne: { document: { _id: 4, type: "sausage", size: "large", price: 10 } } },
      { updateOne: {
         filter: { type: "cheese" },
         update: { $set: { price: 8 } }
      } },
      { deleteOne: { filter: { type: "pepperoni"} } },
      { replaceOne: {
         filter: { type: "vegan" },
         replacement: { type: "tofu", size: "small", price: 4 }
      } }
   ] )
} catch( error ) {
   print( error )
}
```

Example output, which includes a summary of the completed operations:

```javascript
{
   acknowledged: true,
   insertedCount: 2,
   insertedIds: { '0': 3, '1': 4 },
   matchedCount: 2,
   modifiedCount: 2,
   deletedCount: 1,
   upsertedCount: 0,
   upsertedIds: {}
}
```
