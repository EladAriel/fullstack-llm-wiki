---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/views/specify-collation.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================

# Create a View with Default Collation

`Collation <manual-collation>` allows you to specify language-specific rules for string comparison, such as rules for letter-case and accent marks.

This page explains how to specify a default collation for a view.

## Example

Create a `places` collection with the following documents:

```javascript
db.places.insertMany([
   { _id: 1, category: "café" },
   { _id: 2, category: "cafe" },
   { _id: 3, category: "cafE" }
])
```

The following operation creates a view, specifying collation at the view level:

```javascript
db.createView(
   "placesView", 
   "places",
   [ { $project: { category: 1 } } ],
   { collation: { locale: "fr", strength: 1 } } 
)
```

The following operation uses the view's collation:

```javascript
db.placesView.countDocuments( { category: "cafe" } )
```

The operation returns `3`.

> **Note:** .. include:: /includes/extracts/views-collation-behavior.rst
