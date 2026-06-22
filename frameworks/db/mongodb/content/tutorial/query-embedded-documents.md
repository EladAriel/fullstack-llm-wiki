---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/query-embedded-documents.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

.. include:: /includes/java-sync-links.rst

.. include:: /includes/java-async-links.rst

==================================

# Query on Embedded/Nested Documents

Query embedded documents in MongoDBwith the following methods:

.. include:: /includes/fact-methods.rst

.. include:: /includes/language-selector-instructions.rst

.. include:: /includes/driver-examples/driver-example-query-intro.rst

.. include:: /includes/driver-examples/driver-example-query-14.rst

## Query Nested Fields with Dot Notation

Specify query conditions on fields in an embedded/nested document with `dot notation` `"field.nestedField"`.

> **Note:** When you query with dot notation, the field and nested field must be
inside quotation marks.

### Specify Equality Match on a Nested Field

The following example selects all documents where the field `uom` nested in the `size` field equals `"in"`:

.. include:: /includes/driver-examples/driver-example-query-17.rst

### Specify Match using Query Operator

.. include:: /includes/extracts/filter-query-operators.rst

The following query uses the less than operator (:query:`$lt`) on the field `h` embedded in the `size` field:

.. include:: /includes/driver-examples/driver-example-query-18.rst

### Specify `AND` Condition

The following query selects all documents where the nested field `h` is less than `15`, the nested field `uom` equals `"in"`, and the `status` field equals `"D"`:

.. include:: /includes/driver-examples/driver-example-query-19.rst

## Match an Embedded/Nested Document

.. include:: /includes/extracts/filter-equality-embedded.rst

For example, the following query selects all documents where the field `size` equals the document `{ h: 14, w: 21, uom: "cm" }`:

.. include:: /includes/driver-examples/driver-example-query-15.rst

> **Warning:** MongoDB does not recommend `comparisons <query-comparison>` on embedded
documents because the operations require an exact match of the specified
`<value>` document, including the field order.
For example, the following query does not match any documents in the
`inventory` collection:
.. include:: /includes/driver-examples/driver-example-query-16.rst
Queries that use comparisons on embedded documents can result in
unpredictable behavior when used with a driver that does not use ordered data
structures for expressing queries.

## Query Embedded Documents with {+atlas+}

This example uses the :atlas:`sample movies dataset </sample-data/sample-mflix/>`. To load the sample dataset into your {+atlas+} deployment, see :atlas:`Load Sample Data </sample-data/#std-label-load-sample-data>`.

To query an embedded document in {+atlas+}, follow these steps:

## Additional Query Tutorials

For additional query examples, see:

- `match-values-with-all`
- `all-with-elemMatch`
- `read-operations-queries`
- `read-operations-arrays`
- `array-match-embedded-documents`
