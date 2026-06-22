---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/capped-collections/change-max-docs-capped-collection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================================

# Change Maximum Documents in a Capped Collection

.. versionadded:: 6.0

To change the maximum number of documents in a `capped collection <manual-capped-collection>`, use the :dbcommand:`collMod` command's `cappedMax` option.

- If `cappedMax` is less than or equal to `0`, there is no maximum
document limit.

- If `cappedMax` is less than the current number of documents in the
collection, MongoDB removes the excess documents on the next insert operation.

## About this Task

.. include:: /includes/capped-collections/use-ttl-index.rst

## Before you Begin

Create a capped collection called `log` that can store a maximum of 20,000 documents:

```javascript
db.createCollection( "log", { capped: true, size: 5242880, max: 20000 } )
```

## Steps

Run the following command to set the maximum number of documents in the `log` collection to 5,000:

```javascript
db.runCommand( { collMod: "log", cappedMax: 5000 } )
```

## Learn More

- `capped-collections-change-size`
- `capped-collections-check`
- `capped-collections-query`
