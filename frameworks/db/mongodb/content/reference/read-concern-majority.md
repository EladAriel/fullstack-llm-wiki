---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/read-concern-majority.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================

# Read Concern "majority"

For read operations not associated with `multi-document transactions </core/transactions>`, read concern `"majority"` guarantees that the data read has been acknowledged by a majority of the replica set members. The documents read are durable and guaranteed to not roll back.

For operations in `multi-document transactions </core/transactions>`, read concern `"majority"` provides its guarantees only if the transaction commits with `write concern "majority" <transactions-write-concern>`. Otherwise, the :readconcern:`"majority"` read concern provides no guarantees about the data read in transactions.

.. include:: /includes/fact-readConcern-most-recent-data-in-node.rst

For more information about what happens if a primary fails, see `replication-auto-failover`.

## Performance

Each replica set member maintains, in memory, a view of the data at the majority-commit point; the majority-commit point is calculated by the primary. To fulfill read concern `"majority"`, the node returns data from this view and is comparable in performance to other read concerns.

## Latency

Read concern `"majority"` does not decrease the performance of queries; it only modifies what returns to the client. Read concern `"majority"` allows only data that is durably stored on a majority of nodes in the replica set to return to the client. In comparison, queries with read concern `"local"` can return data that may be lost in certain scenarios, such as a rollback.

## Availability

Read concern :readconcern:`"majority"` is available for use with or without causally consistent sessions and transactions.

> **Warning:** .. include:: /includes/fact-psa-performance-issues.rst

## Example

.. include:: /includes/fact-read-concern-write-timeline.rst

Then, the following tables summarizes the state of the data that a read operation with :readconcern:`"majority"` read concern would see at time `T`.

.. figure:: /images/read-concern-write-timeline.svg

## Storage Engine Support

Read concern :readconcern:`"majority"` is available for the WiredTiger storage engine.

> **Tip:** The :dbcommand:`serverStatus` command returns the
:serverstatus:`storageEngine.supportsCommittedReads` field, which
indicates whether the storage engine supports `"majority"` read
concern.

## Read Concern `"majority"` and Transactions

> **Note:** You set the read concern at the transaction level, not at the
individual operation level. To set the read concern for
transactions, see `transactions-read-concern`.

For operations in `multi-document transactions </core/transactions>`, read concern `"majority"` provides its guarantees only if the transaction commits with `write concern "majority" <transactions-write-concern>`. Otherwise, the :readconcern:`"majority"` read concern provides no guarantees about the data read in transactions.

## Read Concern `"majority"` and Aggregation

.. include:: /includes/fact-aggregate-readConcern.rst

## Read Your Own Writes

.. include:: /includes/fact-read-own-writes.rst

## Primary-Secondary-Arbiter Replica Sets

.. include:: /includes/fact-eMRC-always-true-in-5.0.rst

.. include:: /includes/fact-psa-performance-issues.rst
