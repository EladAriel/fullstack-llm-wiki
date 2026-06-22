---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Bulk.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================

# Bulk() (mongosh method)

.. include:: /includes/fact-bulkwrite.rst

## Description

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

## Ordered and Unordered Bulk Operations

The builder can construct the list of operations as ordered or unordered.

### Ordered Operations

With an ordered operations list, MongoDB executes the write operations in the list serially. If an error occurs during the processing of one of the write operations, MongoDB will return without processing any remaining write operations in the list.

Use :method:`db.collection.initializeOrderedBulkOp()` to create a builder for an ordered list of write commands.

.. include:: /includes/fact-bulk-operation-ordered-list.rst

.. include:: /includes/fact-bulk-operation-batches.rst

.. include:: /includes/fact-bulk-operation-sharded-cluster.rst

### Unordered Operations

With an unordered operations list, MongoDB can execute in parallel, as well as in a nondeterministic order, the write operations in the list. If an error occurs during the processing of one of the write operations, MongoDB will continue to process remaining write operations in the list.

Use :method:`db.collection.initializeUnorderedBulkOp()` to create a builder for an unordered list of write commands.

.. include:: /includes/fact-bulk-operation-unordered-list.rst

.. include:: /includes/fact-bulk-operation-batches.rst

### Transactions

.. include:: /includes/extracts/transactions-supported-operation.rst

For :method:`Bulk.insert()` operations, the collection must already exist.

For :method:`Bulk.find.upsert()`, if the operation results in an upsert, the collection must already exist.

.. include:: /includes/extracts/transactions-operations-write-concern.rst

.. include:: /includes/extracts/transactions-usage.rst

## Methods

The :method:`Bulk()` builder has the following methods:
