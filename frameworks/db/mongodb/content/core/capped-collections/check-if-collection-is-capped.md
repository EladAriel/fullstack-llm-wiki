---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/capped-collections/check-if-collection-is-capped.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# Check if a Collection is Capped

To check if a collection is capped, use the :method:`~db.collection.isCapped()` method.

## About this Task

.. include:: /includes/capped-collections/use-ttl-index.rst

## Before you Begin

Create a non-capped collection and a capped collection:

```javascript
db.createCollection("nonCappedCollection1")

db.createCollection("cappedCollection1", { capped: true, size: 100000 } )
```

## Steps

To check if the collections are capped, use the :method:`~db.collection.isCapped()` method:

## Learn More

- `capped-collections-create`
- `capped-collections-convert`
- :pipeline:`$collStats`
