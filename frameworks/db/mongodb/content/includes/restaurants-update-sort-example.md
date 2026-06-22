---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/restaurants-update-sort-example.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Create the following `restaurantsSort` collection:

```javascript
db.restaurantsSort.insertMany( [
   { _id: 1, name: "Pizza Place", rating: 4, violations: 2 },
   { _id: 2, name: "Burger Joint", rating: 3, violations: 5 },
   { _id: 3, name: "Taco Shop", rating: 4, violations: 1 }
] )
```

The following example replaces `"Pizza Place"` with `"Clean Eats"`:
