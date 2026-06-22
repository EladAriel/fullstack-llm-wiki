---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/query-for-null-fields.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

.. include:: /includes/java-sync-links.rst

.. include:: /includes/java-async-links.rst

================================

# Query for Null or Missing Fields

Query for `null` or missing fields in MongoDB using the following methods:

.. include:: /includes/fact-methods.rst

.. include:: /includes/language-selector-instructions.rst

Query operators in MongoDB treat `null` values differently.

.. include:: /includes/driver-examples/driver-example-query-intro-no-perl.rst

.. include:: /includes/driver-examples/driver-example-query-38.rst

## Equality Filter

.. include:: /includes/driver-examples/driver-example-query-39.rst

.. include:: /includes/driver-examples/driver-example-query-39-conclusion.rst

## Non-Equality Filter

To query for fields that **exist** and are **not null**, use the `{ $ne : null }` filter.

.. include:: /includes/driver-examples/driver-example-query-ne-null-intro.rst

## Type Check

.. include:: /includes/driver-examples/driver-example-query-40.rst

.. include:: /includes/driver-examples/driver-example-query-40-conclusion.rst

## Existence Check

The following example queries for documents that do not contain a field.

.. include:: /includes/driver-examples/driver-example-query-41.rst

.. include:: /includes/driver-examples/driver-example-query-41-conclusion.rst

.. include:: /includes/reference/exist-op-support-expressions.rst

> **Seealso:** Reference documentation for the :query:`$type` and
:query:`$exists` operators.

## Query for Null or Missing Fields with {+atlas+}

The example in this section uses the :atlas:`sample training dataset </sample-data/sample-training/>`. To learn how to load the sample dataset into your {+atlas+} deployment, see :atlas:`Load Sample Data </sample-data/#std-label-load-sample-data>`.

To query for a `null` or missing field in {+atlas+}, follow these steps:
