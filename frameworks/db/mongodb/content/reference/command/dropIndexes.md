---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/dropIndexes.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# dropIndexes (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   { 
     dropIndexes: <string>, 
     index: <string|document|arrayofstrings>, 
     writeConcern: <document>, comment: <any> 
   }
)
```

## Command Fields

The command takes the following fields:

## Behavior

.. include:: /includes/fact-drop-indexes-6.0.rst

.. include:: /includes/fact-drop-index-5.2.rst

### Kill related queries only

.. include:: /includes/extracts/fact-command-dropIndexes-query-behavior.rst

### Resource Locking

.. include:: /includes/extracts/dropIndexes-resource-lock.rst

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

## Examples

- To drop all non-`_id` indexes , specify `"*"` for the `index`.
```javascript
  db.runCommand( { dropIndexes: "collection", index: "*" } )
```

- To drop a single index, issue the command by specifying the name of
the index you want to drop. For example, to drop the index named `age_1`, use the following command:

```javascript
  db.runCommand( { dropIndexes: "collection", index: "age_1" })

:binary:`~bin.mongosh` provides the helper methods
:method:`db.collection.dropIndex()` and
:method:`db.collection.dropIndexes()`:

.. code-block:: javascript

  db.collection.dropIndex("age_1");
```

- To drop multiple indexes, issue the command by specifying an array of
the index names:

```javascript
  db.runCommand( { dropIndexes: "collection", index: [ "age_1", "age_1_status_1" ] } )
```

> **Seealso:** - :method:`db.collection.dropIndexes()`
- :method:`db.collection.dropIndex()`
