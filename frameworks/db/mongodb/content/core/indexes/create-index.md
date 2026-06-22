---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/create-index.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============

# Create an Index

If your application repeatedly runs queries on the same fields, create an index on those fields to improve performance.

To create an index, use the :method:`~db.collection.createIndex()` shell method or equivalent method for your driver. This page shows examples for the MongoDB Shell and drivers.

## About this Task

When you run a create index command in the MongoDB Shell or a driver, MongoDB only creates the index if an index of the same specification does not exist.

Although indexes improve query performance, adding an index has negative performance impact for write operations. For collections with a high write-to-read ratio, indexes are expensive because each insert and update must also update any indexes.

> **Warning:** .. include:: /includes/queryable-encryption/qe-index-performance-warning.rst

## Procedure

----------

|arrow| To set the language of the examples on this page, use the **Select your language** drop-down menu in the right navigation pane.

----------

.. include:: /includes/driver-examples/driver-procedure-indexes-1.rst

## Example

.. include:: /includes/driver-examples/driver-example-indexes-1.rst

## Results

Use :binary:`mongosh` to monitor index creation.

To see what indexes exist on your collection, including indexes that are currently being built, run the :method:`db.collection.getIndexes()` method:

To check whether your index is building, use :pipeline:`$currentOp` with :method:`db.aggregate()` on the `admin` database.

The following aggregation pipeline uses the :pipeline:`$match` stage to show an active operation building a descending index on the `name` field:

MongoDB marks index builds in various stages, including waiting on commit quorum, as an idle connection by setting the `active` field to `false`. The `idleConnections: true` setting includes these idle connections in the `$currentOp` output.

To view information on existing indexes using a driver, refer to your :driver:`driver's documentation </>`.

## Learn More

- To learn how to create indexes in |compass|, see :ref:`Manage Indexes
<compass-indexes>` in the Compass documentation.

- To see how often your indexes are used, see
`index-measure-index-use`.

- To learn how to specify the name of your index, see `specify-index-name`.
- To learn how MongoDB builds indexes, see `index-build-process`.
## Contents

- Specify a Name </core/indexes/create-index/specify-index-name>
