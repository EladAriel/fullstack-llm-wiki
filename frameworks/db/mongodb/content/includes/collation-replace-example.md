---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/collation-replace-example.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

String matching for |replace-operator| expressions is always case-sensitive and diacritic-sensitive. Any `collation <collation>` configured is ignored when performing string comparisons with |replace-operator|.

For example, create a sample collection with collation strength `1`:

```javascript
db.createCollection( "restaurants", { collation: { locale: "fr", strength: 1 } } )
```

A collation strength of `1` compares base character only and ignores other differences such as case and diacritics.

Next, insert example documents:

```javascript
db.restaurants.insertMany( [
   { _id: 1, name: "cafe" },
   { _id: 2, name: "Cafe" },
   { _id: 3, name: "café" }
] )
```
