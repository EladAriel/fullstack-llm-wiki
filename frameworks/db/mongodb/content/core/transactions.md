---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/transactions.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============

# Transactions

In MongoDB, an operation on a single document is atomic. Because you can use embedded documents and arrays to capture relationships between data in a single document structure instead of normalizing across multiple documents and collections, multi-document transactions are not necessary for many practical use cases.

For situations that require atomicity of operations on multiple documents, MongoDB supports transactions. You can use transactions across multiple operations, collections, databases, documents, and shards.

## Transactions API

----------

|arrow| Use the **Select your language** drop-down menu in the upper-right to set the language of the following example.

----------

> **Seealso:** For an example in :binary:`~bin.mongosh`, see
`txn-mongo-shell-example`.

## Transactions and Atomicity

.. include:: /includes/transactions/distributed-transaction-repl-shard-support.rst

Distributed transactions are atomic:

- Transactions either apply all data changes or roll back the changes.
- If a transaction commits, all data changes made in the transaction
are saved and are visible outside of the transaction.

.. include:: /includes/extracts/transactions-committed-visibility.rst

- When a transaction aborts, all data changes made in the transaction
are discarded without ever becoming visible.

.. include:: /includes/extracts/transactions-usage.rst

> **Seealso:** `transactions-prod-consideration-outside-reads`

## Transactions and Operations

Transactions can be used across multiple operations, collections, databases, documents, and shards.

For transactions:

.. include:: /includes/extracts/transactions-operations-crud.rst

For a list of operations not supported in transactions, see `transactions-ops-restricted`.

.. include:: /includes/extracts/transactions-operations-catalog-tip.rst

> **Seealso:** `Transactions and Operations Reference <transactions-operations-ref>`

### Create Collections and Indexes in a Transaction

You can perform the following operations in a `transaction <transactions>` if it is not a cross-shard write transaction:

- Create collections.
- Create indexes on new empty collections created earlier in the same
transaction.

When creating a collection inside a transaction:

- You can :ref:`implicitly create a collection
<transactions-operations-ddl-implicit>`, such as with:

- an `insert operation <transactions-operations-ddl-implicit>`
for a non-existent collection, or

- an :ref:`update/findAndModify operation
<transactions-operations-ddl-implicit>` with `upsert: true` for a non-existent collection.

- You can :ref:`explicitly create a collection
<transactions-operations-ddl-explicit>` using the :dbcommand:`create` command or its helper :method:`db.createCollection()`.

When `creating an index inside a transaction <transactions-operations-ddl-explicit>` [#create-existing-index]_, the index to create must be on either:

- a non-existent collection. The collection is created as part of the
operation.

- a new empty collection created earlier in the same transaction.
You can also run :method:`db.collection.createIndex()` and :method:`db.collection.createIndexes()` on existing indexes to check for existence. These operations return successfully without creating the index.

Restrictions ````````````

- .. include:: /includes/extracts/transactions-cross-shard-collection-restriction.rst
- .. include:: /includes/graphLookup-sharded-coll-transaction-note.rst
- For explicit creation of a collection or an index inside a
transaction, the transaction read concern level must be :readconcern:`"local"`.

To explicitly create collections and indexes, use the following commands and methods:

> **Seealso:** `transactions-ops-restricted`

### Count Operation

.. include:: /includes/extracts/transactions-count.rst

### Distinct Operation

.. include:: /includes/extracts/transactions-distinct.rst

### Informational Operations

.. include:: /includes/extracts/transactions-operations-restrictions-info.rst

### Restricted Operations

.. include:: /includes/extracts/transactions-operations-restrictions.rst

> **Seealso:** - `txn-prod-considerations-ddl`
- `Transactions and Operations Reference <transactions-operations-ref>`

## Transactions and Sessions

- Transactions are associated with a session.
- You can have at most one open transaction at a time for a session.
- When using the drivers, each operation in the transaction must be
associated with the session. Refer to your driver specific documentation for details.

- If a session ends and it has an open transaction, the transaction
aborts.

## Read Concern, Write Concern, and Read Preference

### Transactions and Read Preference

Operations in a transaction use the transaction-level `read preference <replica-set-read-preference>`.

Using the drivers, you can set the transaction-level `read preference <replica-set-read-preference>` at the transaction start:

- If the transaction-level read preference is unset, the transaction
uses the session-level read preference.

- If transaction-level and the session-level read preference are unset,
the transaction uses the client-level read preference. By default, the client-level read preference is :readmode:`primary`.

.. include:: /includes/extracts/transactions-read-pref.rst

### Transactions and Read Concern

Operations in a transaction use the transaction-level `read concern <read-concern>`. This means a read concern set at the collection and database level is ignored inside the transaction.

You can set the transaction-level `read concern <read-concern>` at the transaction start.

- If the transaction-level read concern is unset, the transaction-level
read concern defaults to the session-level read concern.

- If transaction-level and the session-level read concern are unset,
the transaction-level read concern defaults to the client-level read concern. By default, the client-level read concern is :readconcern:`"local"` for reads on the primary. See also:

- `transactions-read-preference`
- `MongoDB Defaults <default-mongodb-read-write-concerns>`
Transactions support the following read concern levels:

`"local"` ```````````

- Read concern :readconcern:`"local"` returns the most recent data
available from the node but can be rolled back.

- .. include:: /includes/transactions/read-isolation-levels.rst
- For transactions on sharded cluster, :readconcern:`"local"` read
concern cannot guarantee that the data is from the same snapshot view across the shards. If snapshot isolation is required, use `transactions-read-concern-snapshot` read concern.

- .. include:: /includes/extracts/transactions-create-collections-read-concern.rst
`"majority"` ``````````````

- If the transaction commits with :ref:`write concern "majority"
<transactions-write-concern>`, read concern :readconcern:`"majority"` returns data that has been acknowledged by a majority of the replica set members and can't be rolled back. Otherwise, read concern :readconcern:`"majority"` provides no guarantees that read operations read majority-committed data.

- For transactions on sharded cluster, read concern
:readconcern:`"majority"` can't guarantee that the data is from the same snapshot view across the shards. If snapshot isolation is required, use read concern `transactions-read-concern-snapshot`.

`"snapshot"` ``````````````

- Read concern :readconcern:`"snapshot"` returns data from a
snapshot of majority committed data **if** the transaction commits with `write concern "majority" <transactions-write-concern>`.

- If the transaction does not use :ref:`write concern "majority"
<transactions-write-concern>` for the commit, the :readconcern:`"snapshot"` read concern provides **no** guarantee that read operations used a snapshot of majority-committed data.

- For transactions on sharded clusters, the
:readconcern:`"snapshot"` view of the data **is** synchronized across shards.

### Transactions and Write Concern

Transactions use the transaction-level `write concern <write-concern>` to commit the write operations. Write operations inside transactions must be run without an explicit write concern specification and use the default write concern. At commit time, the writes are committed using the transaction-level write concern.

> **Tip:** Don't explicitly set the write concern for the individual write
operations inside a transaction. Setting write concerns for the
individual write operations inside a transaction returns an error.

You can set the transaction-level `write concern <write-concern>` at the transaction start:

- If the transaction-level write concern is unset, the
transaction-level write concern defaults to the session-level write concern for the commit.

- If the transaction-level write concern and the session-level write
concern are unset, the transaction-level write concern defaults to the client-level write concern of:

- :writeconcern:`w: "majority" <"majority">` in MongoDB 5.0 and later,
with differences for deployments containing `arbiters <replica-set-arbiter-configuration>`. See `wc-default-behavior`.

- :writeconcern:`w: 1 <\<number\>>`
> **Seealso:** `MongoDB Defaults <default-mongodb-read-write-concerns>`

Transactions support all write concern `w <wc-w>` values, including:

`w: 1` ````````

- Write concern :writeconcern:`w: 1 <\<number\>>` returns
acknowledgment after the commit has been applied to the primary.

> **Important:**   When you commit with :writeconcern:`w: 1 <\<number\>>`, your
  transaction can be :ref:`rolled back if there is a failover
  <replica-set-rollbacks>`.

- When you commit with :writeconcern:`w: 1 <\<number\>>` write
concern, transaction-level :readconcern:`"majority"` read concern provides **no** guarantees that read operations in the transaction read majority-committed data.

- When you commit with :writeconcern:`w: 1 <\<number\>>` write
concern, transaction-level :readconcern:`"snapshot"` read concern provides **no** guarantee that read operations in the transaction used a snapshot of majority-committed data.

`w: "majority"` `````````````````

- Write concern :writeconcern:`w: "majority" <"majority">` returns
acknowledgment after the commit has been applied to a majority of voting members.

- When you commit with :writeconcern:`w: "majority" <"majority">`
write concern, transaction-level :readconcern:`"majority"` read concern guarantees that operations have read majority-committed data. For transactions on sharded clusters, this view of the majority-committed data is not synchronized across shards.

- When you commit with :writeconcern:`w: "majority" <"majority">`
write concern, transaction-level :readconcern:`"snapshot"` read concern guarantees that operations have read from a synchronized snapshot of majority-committed data.

> **Note:** .. include:: /includes/extracts/transactions-sharded-clusters-commit-writeconcern.rst
.. include:: /includes/return-commit-decision-parameter.rst
.. include:: /includes/write-concern-majority-and-transactions.rst
Regardless of the :ref:`write concern specified for the
transaction <transactions-write-concern>`, the driver applies
:writeconcern:`w: "majority" <"majority">` as the write concern when
retrying :dbcommand:`commitTransaction`.

## Transactions Considerations

The following sections describe transaction requirements and considerations that vary by deployment type, storage engine, and MongoDB version.

### Production Considerations

For transactions in production environments, see `production-considerations`. In addition, for sharded clusters, see `production-considerations-sharded`.

### Arbiters

.. include:: /includes/extracts/transactions-arbiters.rst

### Shard Configuration Restriction

.. include:: /includes/extracts/transactions-shards-wcmajority-disabled.rst

> **Note:** .. include:: /includes/extracts/transactions-sharded-clusters-commit-writeconcern.rst

### Diagnostics

To obtain transaction status and metrics, use the following methods:

### Feature Compatibility Version (FCV)

To use transactions, the `featureCompatibilityVersion <view-fcv>` for all members of the deployment must be at least:

To check the FCV for a member, connect to the member and run the following command:

```javascript
db.adminCommand( { getParameter: 1, featureCompatibilityVersion: 1 } )
```

For more information, see the :dbcommand:`setFeatureCompatibilityVersion` reference page.

### Storage Engines

.. include:: /includes/extracts/transactions-inmemory-txn-page.rst

### Limit Critical Section Wait Time

Starting in MongoDB 5.2 (and 5.0.4):

- When a query accesses a shard, a :ref:`chunk migration
<migrate-chunks-sharded-cluster>` or `DDL operation <transactions-operations-ddl>` may hold the critical section for the collection.

- To limit the time a shard waits for a critical section within a
transaction, use the :parameter:`metadataRefreshInTransactionMaxWaitMS` parameter.

> **Note:**   .. include:: /includes/transaction-wait-time-parameter-deprecated.rst

## Learn More

- `Drivers API <transactions-drivers>`
- `Production Considerations <production-considerations>`
- `Sharded Clusters <production-considerations-sharded>`
- `Transactions and Operations <transactions-operations-ref>`
## Contents

- Drivers API </core/transactions-in-applications>
- Operations </core/transactions-operations>
- Production Considerations </core/transactions-production-consideration>
- Sharded Clusters </core/transactions-sharded-clusters>
