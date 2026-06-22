---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/write-operations-atomicity.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# Atomicity and Transactions

In MongoDB, write operations are `atomic <atomic operation>` on the single-document level, even if modifying multiple values. For parallel updates, each command ensures the query condition still matches.

To prevent conflicts during concurrent updates, include the expected current value in the update filter.

## Use Cases

.. include:: /includes/sample-data-usage.rst

Consider a collection with this document:

These update operations occur concurrently:

One update sets `num_mflix_comments` to `90` or `100`. The second update then fails to match `{ num_mflix_comments: 80 }` and does not run.

> **Warning:** Filtering on a field you do not update can cause unexpected results
during concurrent updates. Consider these operations:
.. literalinclude:: /code-examples/tested/command-line/mongosh/crud-tutorials/atomicity/update-overwrite-risk.snippet.update-overwrite-risk.js
   :language: javascript
   :copyable: false
   :category: usage example
Both updates match `{ _id: 1 }`, so both run. The second update
overwrites the first. The first client receives no warning that its
update was lost.

To avoid conflicts when filtering on non-updated fields, use :update:`$inc`.

For example, consider the following concurrent update operations:

Both updates match `{ _id: 1 }`. Because they increment rather than set the value, they do not overwrite each other. The final `num_mflix_comments` is `110`.

> **Tip:** To enforce uniqueness, create a :ref:`unique index
<index-type-unique>`. This prevents duplicate data in inserts and
updates. You can also create unique indexes on multiple fields. See
`index-unique-create`.

## Details

This section describes additional details for multi-document transactions.

.. include:: /includes/extracts/concurrent-operations-multi-document-writes.rst

.. include:: /includes/extracts/transactions-usage.rst

## Learn More

`/core/read-isolation-consistency-recency`
