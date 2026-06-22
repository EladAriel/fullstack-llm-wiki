---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/faq/concurrency.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

:orphan:

================

# FAQ: Concurrency

MongoDB allows multiple clients to read and write the same data. To ensure consistency, MongoDB uses locking and `concurrency control` to prevent clients from modifying the same data simultaneously. Writes to a single document occur either in full or not at all, and clients always see consistent data.

## What type of locking does MongoDB use?

.. include:: /includes/extracts/lock-general.rst

In addition to a shared (S) locking mode for reads and an exclusive (X) locking mode for write operations, intent shared (IS) and intent exclusive (IX) modes indicate an intent to read or write a resource using a finer granularity lock. When locking at a certain granularity, all higher levels are locked using an `intent lock`.

For example, when locking a collection for writing (using mode X), both the corresponding database lock and the global lock must be locked in intent exclusive (IX) mode. A single database can simultaneously be locked in IS and IX mode, but an exclusive (X) lock cannot coexist with any other modes, and a shared (S) lock can only coexist with intent shared (IS) locks.

Locks are fair, with lock requests for reads and writes queued in order. However, to optimize throughput, when one lock request is granted, all other compatible lock requests are granted at the same time, potentially releasing the locks before a conflicting lock request is performed. For example, consider a situation where an X lock was just released and the conflict queue contains these locks:

IS |rarr| IS |rarr| X |rarr| X |rarr| S |rarr| IS

In strict first-in, first-out (FIFO) ordering, only the first two IS modes would be granted. Instead MongoDB will actually grant all IS and S modes, and once they all drain, it will grant X, even if new IS or S requests have been queued in the meantime. As a grant will always move all other requests ahead in the queue, no starvation of any request is possible.

In :method:`db.serverStatus()` and :method:`db.currentOp()` output, the lock modes are represented as follows:

.. include:: /includes/fact-lock-modes.rst

[Multiple granularity locking](http://en.wikipedia.org/wiki/Multiple_granularity_locking) for more information.

## How granular are locks in MongoDB?

.. include:: /includes/fact-wiredtiger-locks.rst

## How do I see the status of locks on my :binary:`~bin.mongod` instances?

To view lock utilization, use any of these methods:

- :method:`db.serverStatus()`
- :method:`db.currentOp()`
- :binary:`~bin.mongotop`
- :binary:`~bin.mongostat`
- |mms-home| or :products:`Ops Manager, an on-premises solution
available in MongoDB Enterprise Advanced </mongodb-enterprise-advanced>`

Specifically, the :serverstatus:`locks` document in the `output of serverStatus <server-status-output>`, or the `currentOp.locks` field in the :method:`current operation reporting <db.currentOp>` provides insight into the type of locks and amount of lock contention in your :binary:`~bin.mongod` instance.

To terminate an operation, use :method:`db.killOp()`.

.. include:: /includes/replacement-mms.rst

## Does a read or write operation ever yield the lock?

In some situations, read and write operations can yield their locks.

Long running read and write operations, such as queries, updates, and deletes, yield locks under many conditions. MongoDB operations can also yield locks between individual document modifications in write operations that affect multiple documents.

For storage engines supporting document level `concurrency control`, such as `WiredTiger <storage-wiredtiger>`, yielding is not necessary when accessing storage as the `intent locks <intent lock>`, held at the global, database and collection level, do not block other readers and writers. However, operations will periodically yield, such as:

- to avoid long-lived storage transactions because these can
potentially require holding a large amount of data in memory;

- to serve as interruption points so that you can kill long running
operations;

- to allow operations that require exclusive access to a collection
such as index/collection drops and creations.

## What locks are taken by some common client operations?

The following table lists some operations and the types of locks they use for document level locking storage engines:

> **Note:** Creating an index requires an exclusive (W) lock on a collection.
However, the lock is not retained for the full duration of the index
build process.
For more information, see `index-operations`.

## Which administrative commands lock a database?

Some administrative commands can exclusively lock a database for extended time periods. For large clusters, consider taking the :binary:`~bin.mongod` instance offline so that clients are not affected. For example, if a :binary:`~bin.mongod` is part of a `replica set`, take the :binary:`~bin.mongod` offline and let other members of the replica set process requests while maintenance is performed.

### Administrative Commands Taking Extended Locks

These administrative operations require an exclusive lock at the database level for extended periods:

- :dbcommand:`cloneCollectionAsCapped` command
- :dbcommand:`convertToCapped` command
In addition, the :dbcommand:`renameCollection` command and corresponding :method:`db.collection.renameCollection()` shell method take the following locks:

## Which administrative commands lock a collection?

These administrative operations require an exclusive lock at the collection level:

- The :dbcommand:`create` command and corresponding
:method:`db.createCollection()` and :method:`db.createView()` shell methods.

- The :dbcommand:`createIndexes` command and corresponding
:method:`db.collection.createIndex()` and :method:`db.collection.createIndexes()` shell methods. The build process only holds an exclusive lock on the collection at the beginning and end of the index build.

- The :dbcommand:`drop` command and corresponding
:method:`db.collection.drop()` shell methods.

- The :dbcommand:`dropIndexes` command and corresponding
:method:`db.collection.dropIndex()` and :method:`db.collection.dropIndexes()` shell methods.

- The :dbcommand:`renameCollection` command and corresponding
:method:`db.collection.renameCollection()` shell method take the following locks, depending on version:

- For :dbcommand:`renameCollection` and
:method:`db.collection.renameCollection()`: If renaming a collection within the same database, the operation takes an exclusive (W) lock on the source and target collections.

- For :dbcommand:`renameCollection` only: If the target namespace
is in a different database as the source collection, the operation takes an exclusive (W) lock on the target database when renaming a collection across databases and blocks other operations on that database until it finishes.

- The :dbcommand:`reIndex` command and corresponding
:method:`db.collection.reIndex()` shell method obtain an exclusive (W) lock on the collection and block other operations on the collection until finished.

- The :dbcommand:`replSetResizeOplog` command takes an exclusive
(W) lock on the `oplog <local.oplog.rs>` collection and blocks other operations on the collection until it finishes.

## Does a MongoDB operation ever lock more than one database?

These MongoDB operations may obtain and hold a lock on more than one database:

## How does sharding affect concurrency?

`Sharding <sharding>` improves concurrency by distributing collections over multiple :binary:`~bin.mongod` instances, allowing shard servers (specifically, :binary:`~bin.mongos` processes) to run concurrently with the downstream :binary:`~bin.mongod` instances.

.. include:: /includes/extracts/lock-sharding.rst

## How does concurrency affect a replica set primary?

With replica sets, when MongoDB writes to a collection on the `primary`, MongoDB also writes to the primary's `oplog`, which is a special collection in the `local` database. Therefore, MongoDB must lock both the collection's database and the `local` database. The :binary:`~bin.mongod` must lock both databases at the same time to keep the database consistent and ensure that write operations, even with replication, are all or nothing operations.

.. include:: /includes/extracts/lock-replica-set-primary.rst

## How does concurrency affect secondaries?

In `replication`, MongoDB does not apply writes serially to `secondaries <secondary>`. Secondaries collect oplog entries in batches and then apply those batches in parallel. Writes are applied in the order that they appear in the oplog.

Reads that `target secondaries <replica-set-read-preference>` read from a `WiredTiger<storage-wiredtiger>` snapshot of the data if the secondary is undergoing replication. This allows the read to occur simultaneously with replication, while still guaranteeing a consistent view of the data.

## What isolation guarantees does MongoDB provide?

Depending on the read concern, clients can see the results of writes before the writes are `durable`. To control whether the data read may be rolled back or not, clients can use the `readConcern` option.

## What are lock-free read operations?

.. versionadded:: 5.0

A lock-free read operation runs immediately: it is not blocked when another operation has an exclusive (X) write lock on the collection.

.. include:: /includes/lock-free-commands.rst

For information, see:

- `/core/read-isolation-consistency-recency`
- `/core/write-operations-atomicity`
- `/reference/read-concern`
