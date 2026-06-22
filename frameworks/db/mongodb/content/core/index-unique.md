---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/index-unique.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============

# Unique Indexes

A unique index ensures that the indexed fields do not store duplicate values, and that a value appears at most once for a given field. A unique compound index ensures that any given combination of the index key values appears at most once. By default, MongoDB creates a unique index on the `_id <document-id-field>` field during the creation of a collection.

## Create a Unique Index

To create a unique index, use the :method:`db.collection.createIndex()` method with the `unique` option set to `true`.

```javascript
db.collection.createIndex( <key and index type specification>, { unique: true } )
```

### Unique Index on a Single Field

For example, to create a unique index on the `email` field of the `users` collection, use the following operation in :binary:`~bin.mongosh`:

### Unique Compound Index

You can also enforce a unique constraint on the combination of index key values for a `compound index <index-type-compound>`.

For example, to create a unique index on `name`, `email`, and `password` fields of the `users` collection, use the following operation in :binary:`~bin.mongosh`:

Create a unique compound `multikey <index-type-multikey>` index on `email` and `name`:

The unique index permits the insertion of the following documents into the collection since the index enforces uniqueness for the combination of `email` and `name` values:

Even though both documents have `"catelyn@gameofthron.es"` in their `email` arrays, the operation succeeds because the combination of each email value with the `name` field is unique.

> **Seealso:** - `unique-separate-documents`
- `unique-index-and-missing-field`

## Behavior

### Restrictions

MongoDB cannot create a `unique index <index-type-unique>` on the specified index field(s) if the collection already contains data that would violate the unique constraint for the index.

You cannot specify a unique constraint on a `hashed index <index-type-hashed>`.

### Building Unique Index on Replica Sets and Sharded Clusters

For replica sets and sharded clusters, using a `rolling procedure <index-build-on-replica-sets>` to create a unique index requires that you stop all writes to the collection during the procedure. If you cannot stop all writes to the collection during the procedure, do not use the rolling procedure. Instead, to build your unique index on the collection you must either:

- Run `db.collection.createIndex()` on the primary for a
replica set

- Run `db.collection.createIndex()` on the :binary:`~bin.mongos`
for a sharded cluster

### Unique Constraint Across Separate Documents

The unique index prevents different documents in the collection from having the same value for the indexed key.

Because the constraint applies to separate documents, for a unique `multikey <index-type-multikey>` index, a document may have array elements that result in repeating index key values as long as the index key values for that document do not duplicate those of another document. In this case, the repeated index entry is inserted into the index only once.

For example, create a unique compound multikey index on `email` and `name`:

The unique index permits the insertion of the following document into the collection if no other document in the collection has an index key value of `{ "email": "arya@winterfell.com", "name": null }`.

### Missing Document Field in a Unique Single-Field Index

If a document has a `null` or missing value for the indexed field in a unique single-field index, the index stores a `null` value for that document. Because of the unique constraint, a single-field unique index can only contain one document that contains a `null` value in its index entry. If there is more than one document with a `null` value in its index entry, the index build fails with a duplicate key error.

For example, a collection has a unique single-field index on `email`:

The unique index allows the insertion of a document without the `email` field if the collection does not already contain a document missing the `email` field:

However, you cannot insert a second document without the `email` field if the collection already contains a document missing the `email` field. A second operation that attempts to insert another document without the `email` field fails to insert the document because of the violation of the unique constraint on `email` field.

### Unique Partial Indexes

If you use both the `partialFilterExpression` and a unique constraint, the unique constraint only applies to documents that meet the filter expression. For an example, see `partial-index-with-unique-constraints`.

### Sharded Clusters and Unique Indexes

You cannot specify a unique constraint on a `hashed index <index-type-hashed>`.

For a ranged sharded collection, only the following indexes can be `unique <index-type-unique>`:

- the index on the shard key
- a `compound index` where the shard key is a :ref:`prefix
<compound-index-prefix>`

- The default `_id index; however, the id` index only
enforces the uniqueness constraint **per shard** if the `_id` field is not the shard key.

Additionally, if there is a collation on the index key, you can only ensure uniqueness if the collation is simple.

.. include:: /includes/sharding/shard-collection-uniqueness-enforcement-note.rst

.. include:: /includes/sharding/sharding-unique-index-constraints.rst

To maintain uniqueness on a field that is not your shard key, see `shard-key-arbitrary-uniqueness`.

### Sparse and Non-Sparse Unique Indexes

.. include:: /includes/fact-5.0-sparse-unique-index-updates.rst

### Basic and Unique Indexes With Duplicate Key Patterns

Basic and unique indexes can exist with the same `key pattern <key_patterns>`.

For example, you can create both of the following indexes that use the same key pattern:

## Contents

- Create Single-Field </core/index-unique/create>
- Create Compound </core/index-unique/create-compound>
- Convert to Unique </core/index-unique/convert-to-unique>
- Shard Collection </tutorial/shard-collection-with-unique-index>
