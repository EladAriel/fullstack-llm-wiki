---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/crud/c-delete-documents.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

This page uses the following [MongoDB C Driver](https://mongoc.org/libmongoc/current/index.html)_ methods:

- `mongoc_collection_delete_one
<https://mongoc.org/libmongoc/current/mongoc_collection_delete_one.html>`__

- `mongoc_collection_delete_many
<https://mongoc.org/libmongoc/current/mongoc_collection_delete_many.html>`__

.. include:: /includes/driver-examples/examples-intro.rst

## Delete All Documents

To delete all documents from a collection, pass the [mongoc_collection_t](https://mongoc.org/libmongoc/current/mongoc_collection_t.html)_ and a [bson_t](https://mongoc.org/libbson/current/bson_t.html)_ that matches all documents to the [mongoc_collection_delete_many](https://mongoc.org/libmongoc/current/mongoc_collection_delete_many.html)_ method.

.. include:: /includes/fact-delete-all-inventory.rst

The [mongoc_collection_delete_many](https://mongoc.org/libmongoc/current/mongoc_collection_delete_many.html)_ method returns `true` if successful, or returns `false` and sets an error if there are invalid arguments or a server or network error occurs.

## Delete All Documents that Match a Condition

.. include:: /includes/fact-delete-condition-inventory.rst

To specify equality conditions, use `<field>:<value>` expressions in the `query filter document <document-query-filter>`:

```c
{ <field1>: <value1>, ... }
```

A `query filter document <document-query-filter>` can use the `query operators <query-selectors>` to specify conditions in the following form:

```c
{ <field1>: { <operator1>: <value1> }, ... }
```

To delete all documents that match a deletion criteria, pass the [mongoc_collection_t](https://mongoc.org/libmongoc/current/mongoc_collection_t.html)_ and a [bson_t](https://mongoc.org/libbson/current/bson_t.html)_ that matches the documents you want to delete to the [mongoc_collection_delete_many](https://mongoc.org/libmongoc/current/mongoc_collection_delete_many.html)_ method.

The [mongoc_collection_delete_many](https://mongoc.org/libmongoc/current/mongoc_collection_delete_many.html)_ method returns `true` if successful, or returns `false` and sets an error if there are invalid arguments or a server or network error occurs.

## Delete Only One Document that Matches a Condition

To delete a single document from a collection, pass the [mongoc_collection_t](https://mongoc.org/libmongoc/current/mongoc_collection_t.html)_ and a [bson_t](https://mongoc.org/libbson/current/bson_t.html)_ that matches the document you want to delete to the [mongoc_collection_delete_one](https://mongoc.org/libmongoc/current/mongoc_collection_delete_one.html)_ method.

.. include:: /includes/fact-remove-one-condition-inv-example.rst

.. include:: /includes/driver-examples/driver-example-c-cleanup.rst

> **Seealso:** - `mongoc_collection_delete_one
  <https://mongoc.org/libmongoc/current/mongoc_collection_delete_one.html>`__
- `mongoc_collection_delete_many
  <https://mongoc.org/libmongoc/current/mongoc_collection_delete_many.html>`__
- `additional-deletes`
