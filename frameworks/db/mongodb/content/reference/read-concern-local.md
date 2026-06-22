---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/read-concern-local.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================

# Read Concern `"local"`

A query with read concern `"local"` returns data from the instance with no guarantee that the data has been written to a majority of the replica set members (i.e. may be rolled back).

Read concern `"local"` is the default for read operations against the primary and secondaries.

.. include:: /includes/fact-readConcern-most-recent-data-in-node.rst

## Availability

Read concern :readconcern:`"local"` is available for use with or without causally consistent sessions and transactions.

## Read Concern local and Transactions

You set the read concern at the transaction level, not at the individual operation level. To set the read concern for transactions, see `transactions-read-concern`.

.. include:: /includes/extracts/transactions-create-collections-read-concern.rst

.. include:: /includes/transactions/read-isolation-levels.rst

## Example

.. include:: /includes/fact-read-concern-write-timeline.rst

Then, the following tables summarizes the state of the data that a read operation with :readconcern:`"local"` read concern would see at time `T`.

.. figure:: /images/read-concern-write-timeline.svg
