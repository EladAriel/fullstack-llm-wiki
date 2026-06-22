---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.dropIndex.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================================

# db.collection.dropIndex() (mongosh method)

.. include:: /includes/wayfinding/mongosh-method-dropIndex.rst

## Definition

### Parameters

The :method:`db.collection.dropIndex()` method takes the following parameter:

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

.. include:: /includes/fact-drop-index-5.2.rst

### Resource Locking

.. include:: /includes/extracts/dropIndex-method-resource-lock.rst

### Stop In-Progress Index Builds

.. include:: /includes/fact-stop-in-progress-index-builds.rst

### Hidden Indexes

.. include:: /includes/fact-hidden-indexes.rst

## Example

In a `pets` collection, create a descending index on the `cat` field:

```javascript
db.pets.createIndex( { cat: -1 }, { name: "catIdx" } )
```

To see the indexes in the `pets` collection, run the :method:`~db.collection.getIndexes()` method:

The single field index on the field `cat` has the user-specified name of `catIdx` and the index specification document of `{ "cat" : -1 }`.

To drop the index `catIdx`, you can use either the index name:

```javascript
db.pets.dropIndex( "catIdx" )
```

Or you can use the index specification document `{ "cat" : -1 }`:

```javascript
db.pets.dropIndex( { "cat" : -1 } )
```

The `dropIndex` command returns the number of indexes in the collection prior to the command being run, and indicates whether the command was successful:

```javascript
{ nIndexesWas: 2, ok: 1 }
```

To confirm that the index was dropped, run the `getIndexes()` method again:
