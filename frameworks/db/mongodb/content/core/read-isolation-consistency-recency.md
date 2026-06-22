---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/read-isolation-consistency-recency.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================================

# Read Isolation, Consistency, and Recency

## Isolation Guarantees

### Read Uncommitted

.. include:: /includes/extracts/concurrent-operations-read-uncommitted.rst

Read uncommitted is the default isolation level and applies to :binary:`~bin.mongod` standalone instances, replica sets, and sharded clusters.

### Read Uncommitted And Single Document Atomicity

.. include:: /includes/extracts/concurrent-operations-single-document-write.rst

### Read Uncommitted And Multiple Document Write

.. include:: /includes/extracts/concurrent-operations-multi-document-writes.rst

.. include:: /includes/extracts/transactions-usage.rst

Without isolating the multi-document write operations, MongoDB exhibits the following behavior:

.. include:: /includes/extracts/concurrent-operations-multi-document-writes-no-isolation.rst

### Cursor Snapshot

.. include:: /includes/extracts/isolate-cursor-snapshot.rst

Use read isolation to improve consistency. To learn more, see `read-concern-snapshot`.

## Monotonic Writes

.. include:: /includes/extracts/monotonic-writes.rst

Writes that don't modify any documents are known as no-operation `noop` writes. No-operation writes:

- Occur if the filter for the write doesn't match any documents, or the
matched documents are unchanged after applying the write.

- Don't increase the `optime` value.
- Return `WriteResult.nModified` equal to `0`, which indicates
that the write operation didn't modify any documents.

To ensure monotonicity with no-operation writes, use `causal consistency guarantees <causal-consistency-guarantees>`. For all other writes, the following sections describe the monotonicity guarantees.

## Real Time Order

For read and write operations on the primary, issuing :readconcern:`"linearizable"` read concern for reads and :writeconcern:`"majority"` write concern for writes enables multiple threads to read and write a single document as if a single thread performed these operations in real time. The resulting schedule for these reads and writes is linearizable.

> **Seealso:** `causal-consistency`

## Causal Consistency

Operations that logically depend on a preceding operation have a causal relationship. For example, a write that deletes all documents matching a specified condition and a subsequent read that verifies the delete operation have a causal relationship.

With causally consistent sessions, MongoDB executes causal operations in an order that respects their causal relationships. Clients observe results consistent with those relationships.

### Client Sessions and Causal Consistency Guarantees

MongoDB enables causal consistency through client sessions. A causally consistent session ensures that read operations with :readconcern:`"majority"` read concern and write operations with :writeconcern:`"majority"` write concern have a causal relationship reflected in their ordering. :red:`Applications must ensure that only one thread at a time executes these operations in a client session.`

For causally related operations:

#. A client starts a client session.

> **Important:**    Client sessions only guarantee causal consistency for:
   - Read operations with :readconcern:`"majority"` read concern.
     The return data has been acknowledged by a majority of the
     replica set members and is durable.
   - Write operations with :writeconcern:`"majority"` write concern.
     These operations request acknowledgment that the write has been
     applied to a majority of the replica set's voting members.
   For more information on causal consistency and various read and
   write concerns, see
   `/core/causal-consistency-read-write-concerns`.

#. As the client issues read operations with :readconcern:`"majority"` read concern and write operations with :writeconcern:`"majority"` write concern, the client includes session information with each operation.

#. For each read operation with :readconcern:`"majority"` read concern and write operation with :writeconcern:`"majority"` write concern associated with the session, MongoDB returns the operation time and the cluster time, even if the operation errors. The client session tracks the operation time and the cluster time.

> **Note:**    MongoDB does not return the operation time and the cluster time
   for unacknowledged (`w: 0`) write operations. Unacknowledged
   writes do not imply any causal relationship.
   MongoDB returns the operation time and the cluster time for read
   operations and acknowledged write operations in a client session.
   Only read operations with :readconcern:`"majority"` read concern
   and write operations with :writeconcern:`"majority"` write concern
   guarantee causal consistency. For details, see
   `/core/causal-consistency-read-write-concerns`.

#. The associated client session tracks these two time fields.

> **Note:**    Operations can be causally consistent across different sessions.
   MongoDB drivers and :binary:`~bin.mongosh` provide methods to
   advance the operation time and the cluster time for a client
   session. A client can advance the cluster time and the operation
   time of one client session to be consistent with the operations
   of another client session.

Causal Consistency Guarantees `````````````````````````````

The following table describes the causal consistency guarantees for causally consistent sessions that use :readconcern:`"majority"` read concern for read operations and :writeconcern:`"majority"` write concern for write operations.

Read Preference ```````````````

These guarantees hold across all members of the MongoDB deployment. For example, in a causally consistent session, if you issue a write with :writeconcern:`"majority"` write concern followed by a read from a secondary with read preference :readmode:`secondary` and :readconcern:`"majority"` read concern, the read operation reflects the state of the database after the write operation.

Isolation `````````

Operations within a causally consistent session are not isolated from operations outside the session. If a concurrent write operation interleaves between the session's write and read operations, the session's read operation may return results that reflect a write operation that occurred after the session's write operation.

### MongoDB Drivers

> **Tip:** Applications must ensure that only one thread at a time executes
these operations in a client session.

Clients require MongoDB drivers updated for MongoDB 3.6 or later:

.. include:: /includes/3.6-drivers.rst

### Examples

> **Important:** Causally consistent sessions only guarantee causal consistency for
reads with :readconcern:`"majority"` read concern and writes with
:writeconcern:`"majority"` write concern.

Consider a collection `items` that maintains current and historical data for various items. Only historical data has a non-null `end` date. If the `sku` value for an item changes, update the document with the old `sku` value to add the `end` date, then insert a new document with the current `sku` value. Use a causally consistent session to ensure that the update occurs before the insert.

----------

|arrow| Use the **Select your language** drop-down menu in the upper-right to set the language of this example.

----------

To read all current `sku` values from another client, advance the cluster time and the operation time to match the other session. This ensures that the client is causally consistent with the other session and reads after the two writes:

### Limitations

The following operations build in-memory structures and are not causally consistent:

## Contents

- Causal Consistency </core/causal-consistency-read-write-concerns>
