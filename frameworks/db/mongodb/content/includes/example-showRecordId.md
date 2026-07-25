---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/example-showRecordId.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The example uses this `pizzas` collection:

```javascript
db.pizzas.insertMany( [
   { type: "pepperoni", size: "small", price: 4 },
   { type: "cheese", size: "medium", price: 7 },
   { type: "vegan", size: "large", price: 8 }
] )
```

The following :method:`~db.collection.find()` example uses :method:`~cursor.showRecordId()` to append the `$recordId` to the `pizza` document fields in the output:

```javascript
db.pizzas.find().showRecordId()
```

Example output:

```javascript
[
   {
      _id: ObjectId("62ffc70660b33b68e8f30435"),
      type: 'pepperoni',
      size: 'small',
      price: 4,
      '$recordId': Long("1")
   },
   {
      _id: ObjectId("62ffc70660b33b68e8f30436"),
      type: 'cheese',
      size: 'medium',
      price: 7,
      '$recordId': Long("2")
   },
   {
      _id: ObjectId("62ffc70660b33b68e8f30437"),
      type: 'vegan',
      size: 'large',
      price: 8,
      '$recordId': Long("3")
   }
]
```
