---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.dropIndexes.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

============================================

# db.collection.dropIndexes() (mongosh method)

.. include:: /includes/wayfinding/mongosh-method-dropIndexes.rst

## Definition

### Parameters

The :method:`db.collection.dropIndexes()` method takes the following optional parameter:

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

.. include:: /includes/fact-drop-indexes-6.0.rst

.. include:: /includes/fact-drop-index-5.2.rst

### Kill related queries only

.. include:: /includes/extracts/fact-method-dropIndexes-query-behavior.rst

### Resource Locking

.. include:: /includes/extracts/dropIndexes-method-resource-lock.rst

### Index Names

If the method is passed an array of index names that includes a non-existent index, the method errors without dropping any of the specified indexes.

### `_id` Index

You cannot drop the default index on the `_id` field.

### text Indexes

To drop a `text <index-type-text>` index, specify the index name instead of the index specification document.

### Stop In-Progress Index Builds

.. include:: /includes/fact-stop-in-progress-index-builds.rst

### Hidden Indexes

.. include:: /includes/fact-hidden-indexes.rst
