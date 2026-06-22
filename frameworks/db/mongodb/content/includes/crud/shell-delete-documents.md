---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/crud/shell-delete-documents.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

This page uses the following :binary:`~bin.mongosh` methods:

- :method:`db.collection.deleteMany()`
- :method:`db.collection.deleteOne()`
.. include:: /includes/sample-data-usage.rst

## Delete All Documents

To delete all documents from a collection, pass an empty `filter <document-query-filter>` document `{}` to the :method:`db.collection.deleteMany()` method.

The following example deletes all documents from the `movies` collection:

```javascript
db.movies.deleteMany({})
```

The method returns a document with the status of the operation. For more information and examples, see :method:`~db.collection.deleteMany()`.

## Delete All Documents that Match a Condition

.. include:: /includes/fact-delete-condition-inventory.rst

To specify equality conditions, use `<field>:<value>` expressions in the `query filter document <document-query-filter>`:

```javascript
{ <field1>: <value1>, ... }
```

A `query filter document <document-query-filter>` can use the `query operators <query-selectors>` to specify conditions in the following form:

```javascript
{ <field1>: { <operator1>: <value1> }, ... }
```

To delete all documents that match a deletion criteria, pass a `filter <document-query-filter>` parameter to the :method:`~db.collection.deleteMany()` method.

The following example removes all documents from the `movies` collection where `year` equals `2023`:

The method returns a document with the status of the operation. For more information and examples, see :method:`~db.collection.deleteMany()`.

## Delete Only One Document that Matches a Condition

To delete at most a single document that matches a specified filter (even though multiple documents may match the specified filter) use the :method:`db.collection.deleteOne()` method.

The following example deletes the first document from the `movies` collection where the `title` field equals `"Dune: Part Two"`:

> **Seealso:** - :method:`db.collection.deleteMany()`
- :method:`db.collection.deleteOne()`
- `additional-deletes`
