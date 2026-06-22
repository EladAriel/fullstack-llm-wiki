---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/collation-replace-example.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
