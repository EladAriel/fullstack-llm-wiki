---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/pizza-example-collection.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

```javascript
db.pizzas.insertMany( [
   { _id: 0, type: "pepperoni", size: "small", price: 4 },
   { _id: 1, type: "cheese", size: "medium", price: 7 },
   { _id: 2, type: "vegan", size: "large", price: 8 }
] )
```
