---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.dropIndexes.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
