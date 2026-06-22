---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/update-documents.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

.. include:: /includes/java-sync-links.rst

.. include:: /includes/java-async-links.rst

================

# Update Documents

You can update documents using:

- Your programming language's driver
- The :atlas:`{+atlas+} UI </>` (see `update-documents-atlas-ui`)
- :compass:`MongoDB Compass </>`
----------

|arrow| Use the **Select your language** drop-down menu in the upper-right to set the language of the following examples.

----------

Connect to a test database in your MongoDB instance then create the `inventory` collection:

.. include:: /includes/driver-examples/driver-example-update-51.rst

## Update Documents in a Collection

> **Note:** MongoDB can accept an aggregation pipeline instead of an update document.
For details, see the method reference page.

### Update a Single Document

.. include:: /includes/driver-examples/driver-example-update-52.rst

### Update Multiple Documents

.. include:: /includes/driver-examples/driver-example-update-53.rst

### Replace a Document

.. include:: /includes/driver-examples/driver-example-update-54.rst

## Update a Document with {+atlas+}

> **Note:** The {+atlas+} UI updates one document at a time. To update multiple
documents or replace an entire document, connect to your Atlas deployment
from :binary:`~bin.mongosh` or a MongoDB driver and follow the example for
your preferred method.

This example uses the :atlas:`sample supplies dataset </sample-data/sample-supplies/>`. To load the sample dataset, see :atlas:`Load Sample Data </sample-data/#std-label-load-sample-data>`.

To update a document in {+atlas+}, follow these steps:

## Behavior

### Atomicity

All write operations are atomic at the document level. For more information, see `transactions-write-atomicity`.

### `_id` Field

Once set, you cannot update the `_id field value nor can you replace a document with one that has a different id` value.

### Idempotent Operations

Use `updateMany()` only for `idempotent` operations.

### Field Order

.. include:: /includes/fact-update-field-order.rst

### Upsert Option

### Write Acknowledgement

Specify the level of acknowledgment requested from MongoDB for write operations with `write concerns <write-concern>`.

## Contents

- Aggregation Pipeline </tutorial/update-documents-with-aggregation-pipeline>
- Methods </reference/update-methods>
- Use MQL to Update an Array </tutorial/use-mql-to-update-an-array>
