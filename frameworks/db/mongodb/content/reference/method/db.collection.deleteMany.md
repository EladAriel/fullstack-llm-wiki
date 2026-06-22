---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.deleteMany.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================================

# db.collection.deleteMany() (mongosh method)

.. include:: /includes/wayfinding/mongosh-method-deleteMany.rst

## Definition

.. include:: /includes/note-drop-faster-than-delete-for-large-collections.rst

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

`db.collection.deleteMany()` has the following syntax:

```javascript
db.collection.deleteMany(
   <filter>,
   {
      writeConcern: <document>,
      collation: <document>,
      hint: <document>|<string>,
      maxTimeMS: <int>,
      let: <document>
   }
)
```

## Behavior

### Sharded Collections

.. include:: /includes/method-targets-all-shards-if-no-txn.rst

> **Warning:** Due to concurrent chunk migrations, |method| might run without deleting all
documents that match the specified filter. To ensure you delete all matching
documents, perform one of the following operations:
- Run the |method| method iteratively until the corresponding find query with
  the same filter returns no documents.
- Run |method| within a transaction.
- Schedule the `balancing window <sharding-schedule-balancing-window>`
  so chunk migrations only occur at specific times, and run any |method|
  operations outside of the specified window.

### Delete a Single Document

To delete a single document, use :method:`db.collection.deleteOne()` instead.

Alternatively, use a field that is a part of a `unique index such as id`.

### Transactions

.. include:: /includes/extracts/transactions-supported-operation.rst

.. include:: /includes/extracts/transactions-operations-write-concern.rst

.. include:: /includes/extracts/transactions-usage.rst

### Primary Node Failure

`deleteMany()` deletes documents one at a time. If the primary node fails during a `deleteMany()` operation, documents that were not yet deleted from secondary nodes are not deleted from the collection.

### Oplog Entries

If a `db.collection.deleteMany()` operation successfully deletes one or more documents, the operation adds an entry for each deleted document on the `oplog` (operations log). If the operation fails or does not find any documents to delete, the operation does not add an entry on the oplog.

## Examples

.. include:: /includes/sample-data-usage.rst

### Delete Multiple Documents

The following operation deletes all documents where `year` is earlier than `1910`:

Similarly, this operation deletes all documents where `rated` equals `"G"` and `year` is earlier than `1950`:

### deleteMany() with a Timeout and Query Variables

The following operation deletes all documents where `year` is earlier than the `cutoffYear` variable. The example also sets a time limit of 3 seconds:

### deleteMany() with Write Concern

Given a three member replica set, the following operation specifies a `w` of `majority` and `wtimeout` of `100`:

If the acknowledgment takes longer than the `wtimeout` limit, MongoDB throws a write concern error.

### Specify Collation

.. include:: /includes/extracts/collation-description.rst

The following operation uses the `collation <collation>` option with English locale and `strength: 2`. The filter `rated: "g"` matches documents with `rated: "G"` stored in the collection:

### Specify `hint` for Delete Operations

Create indexes on the `rated` and `metacritic` fields:

The following delete operation explicitly hints to use the index `{ rated: 1 }`:

> **Note:** If you specify an index that does not exist, the operation errors.

To view the indexes used, you can use the :pipeline:`$indexStats` pipeline:

The `accesses.ops` field in the :pipeline:`$indexStats` output indicates the number of operations that used the index.
