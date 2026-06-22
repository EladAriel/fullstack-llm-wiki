---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/insert-documents.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

.. include:: /includes/java-sync-links.rst

.. include:: /includes/java-async-links.rst

================

# Insert Documents

.. include:: /includes/language-selector-instructions.rst

This page provides examples of insert operations in MongoDB.

You can insert documents in MongoDB by using the following methods:

.. include:: /includes/fact-methods.rst

> **Note:** If the collection does not currently exist, insert operations will
create the collection.

## Insert Documents in the {+atlas+} UI

To insert a document in the {+atlas+} UI, complete the following steps. To learn more about working with documents in the {+atlas+} UI, see :atlas:`Create, View, Update, and Delete Documents </atlas-ui/documents>`.

## Insert a Single Document

.. include:: /includes/driver-examples/driver-example-insert-1.rst

.. include:: /includes/driver-examples/driver-example-insert-2.rst

## Insert Multiple Documents

.. include:: /includes/driver-examples/driver-example-insert-3.rst

.. include:: /includes/driver-examples/driver-example-query-7.rst

## Insert Behavior

### Collection Creation

If the collection does not currently exist, insert operations create the collection.

### `_id` Field

.. include:: /includes/fact-id-field.rst

### Atomicity

All write operations in MongoDB are atomic on the level of a single document. For more information on MongoDB and atomicity, see `/core/write-operations-atomicity`.

### Write Acknowledgement

With write concerns, you can specify the level of acknowledgment requested from MongoDB for write operations. For more information, see `/reference/write-concern`.
