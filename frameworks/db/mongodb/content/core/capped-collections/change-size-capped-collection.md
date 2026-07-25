---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/capped-collections/change-size-capped-collection.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

======================================

# Change the Size of a Capped Collection

.. versionadded:: 6.0

To change the size of a `capped collection <manual-capped-collection>`, use the :dbcommand:`collMod` command's `cappedSize` option. `cappedSize` is specified in bytes, and must be greater than `0` and less than or equal to `1024^5` (1 {+pb+}).

If `cappedSize` is less than the current size of the collection, MongoDB removes the excess documents on the next insert operation.

## About this Task

.. include:: /includes/capped-collections/use-ttl-index.rst

## Before you Begin

Create a capped collection called `log` that has a maximum size of 2,621,440 bytes:

```javascript
db.createCollection( "log", { capped: true, size: 2621440 } )
```

## Steps

Run the following command to set the maximum size of the `log` collection to 5,242,880 bytes:

```javascript
db.runCommand( { collMod: "log", cappedSize: 5242880 } )
```

## Learn More

- `capped-collections-change-max-docs`
- `capped-collections-check`
- `capped-collections-query`
