---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/restaurants-update-sort-example-description-and-output.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The example:

- Finds restaurants with a `rating` of `4`, which are ``"Pizza
Place"` and `"Taco Shop"``.

- Sorts the found restaurants by `violations` in descending order,
which places `"Pizza Place"` in the first position.

- Replaces `"Pizza Place"` with `"Clean Eats"`.
The following query returns the restaurants:

```javascript
db.restaurantsSort.find()
```

Output shows `"Pizza Place"` was replaced with `"Clean Eats"`:

```javascript
[
   { _id: 1, name: 'Clean Eats', rating: 4, violations: 2 },
   { _id: 2, name: 'Burger Joint', rating: 3, violations: 5 },
   { _id: 3, name: 'Taco Shop', rating: 4, violations: 1 }
]
```
