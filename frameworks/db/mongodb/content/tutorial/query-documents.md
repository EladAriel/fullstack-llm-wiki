---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/query-documents.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

.. include:: /includes/java-sync-links.rst

.. include:: /includes/java-async-links.rst

===============

# Query Documents

To query documents, specify a `query predicate` that indicates which documents to return. An empty query predicate `{ }` returns all documents in the collection.

You can query documents in MongoDB with the following methods:

.. include:: /includes/fact-methods.rst

.. include:: /includes/language-selector-instructions.rst

.. include:: /includes/driver-examples/driver-example-query-intro.rst

.. include:: /includes/driver-examples/driver-example-query-6.rst

## Select All Documents in a Collection

.. include:: /includes/driver-examples/driver-example-query-find-method.rst

.. include:: /includes/driver-examples/driver-example-query-7-mflix.rst

This operation uses a query predicate of `{}`, which corresponds to the following SQL statement:

.. include:: /includes/driver-examples/driver-example-query-7-sql.rst

## Specify Equality Condition

.. include:: /includes/extracts/filter-equality.rst

.. include:: /includes/driver-examples/driver-example-query-9-intro.rst

.. include:: /includes/driver-examples/driver-example-query-9.rst

.. include:: /includes/driver-examples/driver-example-query-9-conclusion.rst

## Specify Conditions Using Query Operators

.. include:: /includes/extracts/filter-query-operators.rst

.. include:: /includes/driver-examples/driver-example-query-10-intro.rst

.. include:: /includes/driver-examples/driver-example-query-10.rst

> **Note:** Although you can use the :query:`$or` operator for this query,
use the :query:`$in` operator instead of :query:`$or`
when performing equality checks on the same field.

.. include:: /includes/driver-examples/driver-example-query-10-conclusion.rst

For the complete list of MongoDB query operators, see `query-predicates-ref`.

## Specify `AND` Conditions

A compound query can specify conditions for more than one field in the collection's documents. Implicitly, a logical `AND` conjunction connects the clauses of a compound query so that the query selects the documents in the collection that match all the conditions.

.. include:: /includes/driver-examples/driver-example-query-11-intro.rst

.. include:: /includes/driver-examples/driver-example-query-11.rst

.. include:: /includes/driver-examples/driver-example-query-11-conclusion.rst

See `comparison operators <query-selectors-comparison>` for other MongoDB comparison operators.

## Specify `OR` Conditions

Use the :query:`$or` operator to specify a compound query that joins each clause with a logical `OR` conjunction. The query selects documents that match at least one condition.

.. include:: /includes/driver-examples/driver-example-query-12-intro.rst

.. include:: /includes/driver-examples/driver-example-query-12.rst

.. include:: /includes/driver-examples/driver-example-query-12-conclusion.rst

> **Note:** Queries with :ref:`comparison operators
<query-selectors-comparison>` are subject to `type-bracketing`.

## Specify `AND` as well as `OR` Conditions

.. include:: /includes/driver-examples/driver-example-query-13-intro.rst

.. include:: /includes/driver-examples/driver-example-query-13.rst

The operation uses a query predicate of:

.. include:: /includes/driver-examples/driver-example-query-13-predicate.rst

> **Note:** MongoDB supports regular expressions :query:`$regex` queries to
perform string pattern matches.

## Query Documents with {+atlas+}

This example uses the :atlas:`sample movies dataset </sample-data/sample-mflix/>`. To load the sample dataset into your {+atlas+} deployment, see :atlas:`Load Sample Data </sample-data/#std-label-load-sample-data>`.

To project fields for a query in {+atlas+}, follow these steps:

## Additional Query Tutorials

For more query examples, see:

- `/tutorial/query-embedded-documents`
- `/tutorial/query-arrays`
- `/tutorial/query-array-of-documents`
- `/tutorial/project-fields-from-query-results`
- `/tutorial/query-for-null-fields`
## Behavior

### Cursor

### Concurrent Updates While Using a Cursor

.. include:: /includes/fact-concurrent-updates-cursor.rst

### Read Isolation

For reads to `replica sets <replication>` and replica set `shards <sharding-background>`, read concern lets clients choose an isolation level for their reads. For more information, see `/reference/read-concern`.

### Query Result Format

When you run a find operation with a MongoDB driver or `mongosh`, MongoDB returns a `cursor <cursors>` that manages query results. Query results are not returned as an array of documents.

To learn how to iterate through documents in a cursor, see your :driver:`driver's documentation </>`. If you are using `mongosh`, see `read-operations-cursors`.

## Additional Methods and Options

## Contents

- Embedded Documents </tutorial/query-embedded-documents>
- Arrays </tutorial/query-arrays>
- Arrays of Embedded Documents </tutorial/query-array-of-documents>
- Project Results </tutorial/project-fields-from-query-results>
- Null or Missing Fields </tutorial/query-for-null-fields>
- Timeouts </tutorial/query-documents/specify-query-timeout>
- Long-Running Snapshots </tutorial/long-running-queries>
