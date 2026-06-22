---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/query-arrays.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

.. include:: /includes/java-sync-links.rst

.. include:: /includes/java-async-links.rst

==============

# Query an Array

You can query arrays in MongoDB using the following methods:

.. include:: /includes/fact-methods.rst

.. include:: /includes/language-selector-instructions.rst

.. include:: /includes/driver-examples/driver-example-query-intro.rst

.. include:: /includes/driver-examples/driver-example-query-20.rst

## Match an Array

.. include:: /includes/extracts/filter-equality-array.rst

.. include:: /includes/driver-examples/driver-example-query-21-intro.rst

.. include:: /includes/driver-examples/driver-example-query-21.rst

.. include:: /includes/driver-examples/driver-example-query-22-intro.rst

.. include:: /includes/driver-examples/driver-example-query-22.rst

## Query an Array for an Element

.. include:: /includes/extracts/filter-equality-array-element.rst

.. include:: /includes/driver-examples/driver-example-query-23-intro.rst

.. include:: /includes/driver-examples/driver-example-query-23.rst

.. include:: /includes/extracts/filter-query-operators-array.rst

.. include:: /includes/driver-examples/driver-example-query-24-intro.rst

.. include:: /includes/driver-examples/driver-example-query-24.rst

## Specify Multiple Conditions for Array Elements

When you specify compound conditions on array elements, you can query for documents where either:

- A single array element meets all the specified conditions
- Different array elements collectively meet all the conditions, with each
element satisfying one or more conditions

### Query an Array with Compound Filter Conditions on the Array Elements

.. include:: /includes/driver-examples/driver-example-query-25-intro.rst

.. include:: /includes/driver-examples/driver-example-query-25.rst

### Query for an Array Element that Meets Multiple Criteria

Use the :query:`$elemMatch` operator to specify multiple criteria on array elements so that at least one array element satisfies all the specified criteria.

.. include:: /includes/driver-examples/driver-example-query-26-intro.rst

.. include:: /includes/driver-examples/driver-example-query-26.rst

### Query for an Element by the Array Index Position

Use `dot notation` to specify query conditions for an element at a particular index or position of the array. The array uses zero-based indexing.

> **Note:** When you query using dot notation, the field and nested field must be
inside quotation marks.

.. include:: /includes/driver-examples/driver-example-query-27-intro.rst

.. include:: /includes/driver-examples/driver-example-query-27.rst

### Query an Array by Array Length

Use the :query:`$size` operator to query for arrays by number of elements.

.. include:: /includes/driver-examples/driver-example-query-28-intro.rst

.. include:: /includes/driver-examples/driver-example-query-28.rst

## Query an Array with {+atlas+}

The example in this section uses the :atlas:`sample movies dataset </sample-data/sample-mflix/>`. To learn how to load the sample dataset into your {+atlas+} deployment, see :atlas:`Load Sample Data </sample-data/#std-label-load-sample-data>`.

To query an array in {+atlas+}, follow these steps:

## Additional Query Tutorials

For additional query examples, see:

- `/tutorial/query-documents`
- `/tutorial/query-embedded-documents`
- `/tutorial/query-array-of-documents`
