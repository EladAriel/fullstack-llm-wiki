---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/index-sparse.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============

# Sparse Indexes

Sparse indexes in MongoDB differ from [block-level](http://en.wikipedia.org/wiki/Database_index#Sparse_index)_ sparse indexes in other databases. Sparse indexes only contain entries for documents that have the indexed field, even if the index field contains a null value. The index skips over any document that is missing the indexed field. The index is "sparse" because it does not include all documents of a collection. By contrast, non-sparse indexes contain all documents in a collection, storing null values for those documents that do not contain the indexed field.

> **Important:** `Partial indexes <partial-sparse-index-comparison>` can function as
sparse indexes, but also support filter expressions for conditions beyond
whether a field exists. Use a partial index for greater
control if you need precise filtering.

## Create a Sparse Index

To create a sparse index, use the :method:`db.collection.createIndex()` method with the `sparse` option set to `true`.

For example, the following operation in :binary:`~bin.mongosh` creates a sparse index on the `plot` field of the `movies` collection:

The index does not index documents that do not include the `plot` field.

## Behavior

### Sparse Index and Incomplete Results

If a sparse index would result in an incomplete result set for queries and sort operations, MongoDB will not use that index unless a :method:`~cursor.hint()` explicitly specifies the index. See `sparse-index-incomplete-results` for an example.

.. include:: /includes/fact-sparse-index-hint-count.rst

### Indexes that are Sparse by Default

The following index types are always sparse:

- `2d <2d-index>`
- `2dsphere (version 2) <2dsphere-v2>`
- `Text <index-feature-text>`
- `Wildcard <wildcard-index-core>`
### Sparse Compound Indexes

.. include:: /includes/indexes/sparse-compound-indexes.rst

### Sparse and Unique Properties

An index that is both sparse and `unique <index-type-unique>` prevents a collection from having documents with duplicate values for a field but allows multiple documents that omit the key.

## Examples

### Create a Sparse Index On A Collection

The following example creates a sparse index on the `password` field:

Then, the following query on the `users` collection uses the sparse index to return the documents that have the `password` field:

If a document does not contain the `password` field, the query does not return that document.

### Sparse Index On A Collection Cannot Return Complete Results

Consider the `movies` collection where some documents do not have a `plot` field.

The following example creates a sparse index on the `plot` field:

Consider the following query to return **all** documents in the `movies` collection, sorted by the `plot` field:

Even though the sort is by the indexed field, if some documents in the `movies` collection do not have a `plot` field, MongoDB does **not** select the sparse index to fulfill the query in order to return complete results.

To use the sparse index, explicitly specify the index with :method:`~cursor.hint()`:

This query only returns documents in the `movies` collection that contain the `plot` field.

> **Seealso:** - :method:`~cursor.explain()`
- `/tutorial/analyze-query-plan`

### Sparse Index with Unique Constraint

The following operation creates an index with a `unique constraint <index-type-unique>` and sparse filter on the `password` field in the `users`:

This index permits inserting documents that either have unique values for the `password` field, or don't include a `password` field. For the example documents in the `users` collection, the index permits the following `insert operations </tutorial/insert-documents>`:

However, the index doesn't allow inserting documents that have email addresses that already exist in the collection.

### Sparse and Non-Sparse Unique Indexes

.. include:: /includes/fact-5.0-sparse-unique-index-updates.rst
