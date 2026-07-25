---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/capped-collections/convert-collection-to-capped.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==============================

# Convert a Collection to Capped

To convert a non-capped collection to a `capped collection <manual-capped-collection>`, use the :dbcommand:`convertToCapped` database command.

The `convertToCapped` command holds a database-exclusive lock for the duration of the operation. Other operations that lock the same database are blocked until the `convertToCapped` operation completes.

## About this Task

.. include:: /includes/capped-collections/use-ttl-index.rst

## Before you Begin

Create a non-capped collection called `log2`:

```javascript
db.createCollection("log2")
```

## Steps

## Learn More

- `faq-concurrency-database-lock`
- `capped-collections-change-size`
- `capped-collections-query`
