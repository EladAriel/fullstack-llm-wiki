---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/capped-collections/change-size-capped-collection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
