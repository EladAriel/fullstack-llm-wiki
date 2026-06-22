---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.getIndexes.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================================

# db.collection.getIndexes() (mongosh method)

.. include:: includes/wayfinding/mongosh-method-getIndexes.rst

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

### {+fts+} Indexes

`getIndexes()` does not return information on :atlas:`{+fts+} indexes </atlas-search/atlas-search-overview/#fts-indexes>`. For information on Atlas Search indexes, use :pipeline:`$listSearchIndexes`.

### Client Disconnection

.. include:: /includes/extracts/4.2-changes-disconnect.rst

### Replica Set Member State Restriction

.. include:: /includes/extracts/4.4-changes-repl-state-restrictions-operation.rst

### Wildcard Indexes

.. include:: /includes/indexes/fact-wildcard-index-ordering.rst

## Required Access

To run :method:`db.collection.getIndexes()` when access control is enforced, users must have privileges to :authaction:`listIndexes` on the collection.

The built-in role :authrole:`read` provides the required privileges to run :method:`db.collection.getIndexes()` for the collections in a database.

## Output

:method:`db.collection.getIndexes()` returns an array of documents that hold index information for the collection. For example:

```javascript
[
   {
      "v" : 2,
      "key" : {
         "_id" : 1
      },
      "name" : "_id_"
   },
   {
      "v" : 2,
      "key" : {
         "status" : 1
      },
      "name" : "status_1"
   },
   {
      "v" : 2,
      "key" : {
         "points" : 1
      },
      "name" : "points_1"
   }
]
```

Index information includes the keys and options used to create the index. The index option `hidden` is only available if the value is `true`.

For information on the keys and index options, see :method:`db.collection.createIndex()`.
