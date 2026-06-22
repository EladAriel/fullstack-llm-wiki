---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/crud.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================

# MongoDB CRUD Operations

CRUD operations create, read, update, and delete `documents <bson-document-format>`.

You can connect with driver methods and perform CRUD operations for deployments hosted in the following environments:

## Create Operations

Create or insert operations add new `documents <bson-document-format>` to a `collection <collections>`. If the collection does not currently exist, insert operations will create the collection.

MongoDB provides the following methods to insert documents into a collection:

- :method:`db.collection.insertOne()`
- :method:`db.collection.insertMany()`
In MongoDB, insert operations target a single `collection`. All write operations in MongoDB are `atomic </core/write-operations-atomicity>` on the level of a single `document <bson-document-format>`.

.. include:: /images/crud-annotated-mongodb-insertOne.rst

For examples, see `/tutorial/insert-documents`.

## Read Operations

Read operations retrieve `documents <bson-document-format>` from a `collection <collections>`; i.e. query a collection for documents. MongoDB provides the following methods to read documents from a collection:

- :method:`db.collection.find()`
You can specify `query filters or criteria <read-operations-query-argument>` that identify the documents to return.

.. include:: /images/crud-annotated-mongodb-find.rst

For examples, see:

- `/tutorial/query-documents`
- `/tutorial/query-embedded-documents`
- `/tutorial/query-arrays`
- `/tutorial/query-array-of-documents`
## Update Operations

Update operations modify existing `documents <bson-document-format>` in a `collection <collections>`. MongoDB provides the following methods to update documents of a collection:

- :method:`db.collection.updateOne()`
- :method:`db.collection.updateMany()`
- :method:`db.collection.replaceOne()`
In MongoDB, update operations target a single collection. All write operations in MongoDB are `atomic </core/write-operations-atomicity>` on the level of a single document.

You can specify criteria, or filters, that identify the documents to update. These `filters <document-query-filter>` use the same syntax as read operations.

.. include:: /images/crud-annotated-mongodb-updateMany.rst

For examples, see `/tutorial/update-documents`.

## Delete Operations

Delete operations remove documents from a collection. MongoDB provides the following methods to delete documents of a collection:

- :method:`db.collection.deleteOne()`
- :method:`db.collection.deleteMany()`
In MongoDB, delete operations target a single `collection`. All write operations in MongoDB are `atomic </core/write-operations-atomicity>` on the level of a single document.

You can specify criteria, or filters, that identify the documents to remove. These `filters <document-query-filter>` use the same syntax as read operations.

.. include:: /images/crud-annotated-mongodb-deleteMany.rst

For examples, see `/tutorial/remove-documents`.

## Bulk Write

MongoDB provides the ability to perform write operations in bulk. For details, see `/core/bulk-write-operations`.

## Contents

- Insert </tutorial/insert-documents>
- Query </tutorial/query-documents>
- Update </tutorial/update-documents>
- Remove </tutorial/remove-documents>
- Bulk Write </core/bulk-write-operations>
- Retryable Writes </core/retryable-writes>
- Retryable Reads </core/retryable-reads>
- SQL to MongoDB </reference/sql-comparison>
- Natural Language to MongoDB </natural-language-to-mongodb>
- Text Search </text-search>
- Geospatial Queries </geospatial-queries>
- Read Concern </reference/read-concern>
- Write Concern </reference/write-concern>
- CRUD Concepts </core/crud>
