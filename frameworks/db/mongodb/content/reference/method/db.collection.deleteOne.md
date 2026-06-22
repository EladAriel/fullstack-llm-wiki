---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.deleteOne.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================================

# db.collection.deleteOne() (mongosh method)

.. include:: /includes/wayfinding/mongosh-method-deleteOne.rst

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

`db.collection.deleteOne()` has the following form:

```javascript
db.collection.deleteOne(
    <filter>,
    {
      writeConcern: <document>,
      collation: <document>,
      hint: <document|string>,
      maxTimeMS: <int>,
      let: <document>
    }
)
```

`db.collection.deleteOne()` takes the following parameters:

## Behavior

### Deletion Order

`deleteOne()` deletes the first document that matches the filter. Use a field that is part of a `unique index such as id` for precise deletions.

### Sharded Collections

To use `deleteOne()` on a sharded collection:

- If you only target one shard, you can use a partial shard key in the query
specification.

- You do not need to provide the `shard key or id` field in the query
specification, because `deleteOne()` inherently uses a limit of 1.

### Transactions

.. include:: /includes/extracts/transactions-supported-operation.rst

.. include:: /includes/extracts/transactions-operations-write-concern.rst

.. include:: /includes/extracts/transactions-usage.rst

### Oplog Entries

If a `db.collection.deleteOne()` operation successfully deletes a document, the operation adds an entry on the `oplog` (operations log). If the operation fails or does not find a document to delete, the operation does not add an entry on the oplog.

## Examples

.. include:: /includes/sample-data-usage.rst

### Delete a Single Document

The following operation deletes the first document where `year` is earlier than `1910`:

### deleteOne() with a Timeout and Query Variables

The following operation deletes the first document where `year` is earlier than the `cutoffYear` variable and sets a time limit of 3 seconds:

### deleteOne() with Write Concern

Given a three member replica set, the following operation specifies a `w` of `majority` and `wtimeout` of `100`:

### Specify Collation

.. include:: /includes/extracts/collation-description.rst

The following operation uses the `collation <collation>` option with English locale and `strength: 2`, which makes comparisons case-insensitive. The filter `title: "the dark knight"` matches the document with the title `"The Dark Knight"` in the collection:

### Specify `hint` for Delete Operations

Create indexes on the `rated` and `metacritic` fields:

The following delete operation explicitly hints to use the index `{ rated: 1 }`:

> **Note:** If you specify an index that does not exist, the operation errors.

To view the indexes used, you can use the :pipeline:`$indexStats` pipeline:

The `accesses.ops` field in the :pipeline:`$indexStats` output indicates the number of operations that used the index.
