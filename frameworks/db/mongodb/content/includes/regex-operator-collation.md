---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/regex-operator-collation.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
