---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/write-performance.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.524941Z"
---
.. _write-operation-perf:

# Write Operation Performance

**meta:** :description: Optimize write performance by managing indexes and understanding the impact of journaling on MongoDB's write operations.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Indexes

Each index on a collection adds some amount of overhead to the
performance of write operations.

For each :dbcommand:`insert` or :dbcommand:`delete` write operation
on a collection, MongoDB either inserts or removes the corresponding
document keys from each index in the target collection. An
:dbcommand:`update` operation may result in updates to a subset of
indexes on the collection, depending on the keys affected by the update.

**note:** MongoDB only updates a :ref:`sparse <index-type-sparse>` or
   :ref:`partial <index-type-partial>` index if the documents involved
   in a write operation are included in the index.

In general, the performance gains that indexes provide for *read
operations* are worth the insertion penalty. However, in order to
optimize write performance when possible, be careful when creating new
indexes and evaluate the existing indexes to ensure that your queries
actually use these indexes.

For indexes and queries, see :doc:`/core/query-optimization`. For more
information on indexes, see :doc:`/indexes` and
:doc:`/applications/indexes`.

## Journaling

To provide durability in the event of a crash, MongoDB uses *write
ahead logging* to an on-disk :term:`journal`. MongoDB writes the
in-memory changes first to the on-disk journal files. If MongoDB should
terminate or encounter an error before committing the changes to the
data files, MongoDB can use the journal files to apply the write
operation to the data files.

While the durability assurance provided by the journal typically
outweigh the performance costs of the additional write operations,
consider the following interactions between the journal and
performance:

- If the journal and the data file reside on the same block device,
  the data files and the journal may have to contend for a finite
  number of available I/O resources. Moving the journal to a
  separate device may increase the capacity for write operations.

- If applications specify :ref:`write concerns <write-concern>`
  that include the :writeconcern:`j option <j>`,
  :binary:`~bin.mongod` will decrease the duration between journal
  writes, which can increase the overall write load.

- The duration between journal writes is configurable using the
  :setting:`~storage.journal.commitIntervalMs` run-time option. Decreasing the
  period between journal commits will increase the number of write
  operations, which can limit MongoDB's capacity for write
  operations. Increasing the amount of time between journal commits may
  decrease the total number of write operation, but also increases the
  chance that the journal will not record a write operation in the
  event of a failure.

For additional information on journaling, see
:doc:`/core/journaling`.