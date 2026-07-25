---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/restaurants-update-sort-example.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
