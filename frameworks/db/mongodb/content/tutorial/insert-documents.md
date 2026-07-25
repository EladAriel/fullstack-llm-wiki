---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/insert-documents.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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

## Insert a Single Document

.. include:: /includes/driver-examples/driver-example-insert-1.rst

.. include:: /includes/driver-examples/driver-example-insert-2.rst

## Insert Multiple Documents

.. include:: /includes/driver-examples/driver-example-insert-3.rst

.. include:: /includes/driver-examples/driver-example-query-7.rst

## Insert Documents in the {+atlas+} UI

To insert a document in the {+atlas+} UI, complete the following steps. To learn more about working with documents in the {+atlas+} UI, see :atlas:`Create, View, Update, and Delete Documents </atlas-ui/documents>`.

## Insert Behavior

### Collection Creation

If the collection does not currently exist, insert operations create the collection.

### `_id` Field

.. include:: /includes/fact-id-field.rst

> **Note:** .. include:: /includes/crud/atomicity-write-acknowledgement-note.rst
