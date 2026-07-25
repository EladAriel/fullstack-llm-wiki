---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/capped-collections/change-max-docs-capped-collection.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
