---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/database-profiler.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================

# Database Profiler Output

The database profiler captures data information about read and write operations, cursor operations, and database commands. To configure the database profile and set the thresholds for capturing profile data, see the `database-profiler` section.

The database profiler writes data in the `system.profile <<database>.system.profile>` collection, which is a `capped collection`. To view the profiler's output, use normal MongoDB queries on the `system.profile <<database>.system.profile>` collection.

> **Note:** Because the database profiler writes data to the
`system.profile <<database>.system.profile>` collection in a
database, the profiler profiles some write activity, even for
databases that are otherwise read-only.

:dbcommand:`currentOp` and the database profiler report the same basic diagnostic information for CRUD operations, including the following:

.. include:: /includes/fact-diagnostic-info.rst

When using `Queryable Encryption <qe-manual-feature-qe>`, CRUD operations against encrypted collections are omitted from the `system.profile <<database>.system.profile>` collection. For details, see `qe-redaction`.

It is no longer possible to perform any operation, including reads, on the `system.profile <<database>.system.profile>` collection from within a `transaction <transactions>`.

## Output Fields

For any single operation, the documents created by the database profiler includes a subset of the following fields. The precise selection of fields in these documents depends on the type of operation.

> **Note:** For the output specific to the version of your MongoDB, refer to
the appropriate version of the MongoDB Manual.

## Example `system.profile` Document

The following examples present sample documents found in the `system.profile <<database>.system.profile>` collection for operations on a standalone:
