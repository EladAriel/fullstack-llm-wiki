---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/regex-operator-collation.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

String matching for |regex-operator| is always case-sensitive and diacritic-sensitive. |regex-operator| ignores the collation specified for the collection, :method:`db.collection.aggregate()`, and the index, if used.

For example, create a collection with collation strength `1`, meaning the collation only compares base characters and ignores differences such as case and diacritics:

```javascript
db.createCollection( "restaurants", { collation: { locale: "fr", strength: 1 } } )
```

Insert the following documents:

```javascript
db.restaurants.insertMany( [
   { _id: 1, category: "café", status: "Open" },
   { _id: 2, category: "cafe", status: "open" },
   { _id: 3, category: "cafE", status: "open" }
] )
```

The following uses the collection's collation to perform a case-insensitive and diacritic-insensitive match:

However, |regex-operator| ignores collation. The following regular expression pattern matching examples are case-sensitive and diacritic sensitive:
