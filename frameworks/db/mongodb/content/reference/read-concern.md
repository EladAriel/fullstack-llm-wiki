---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/read-concern.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============

# Read Concern

Use the `readConcern` option to control the consistency and isolation of data read from `replica sets <replication>` and `sharded clusters <sharding-background>`.

Through effective use of `write concerns <write-concern>` and read concerns, you can adjust the level of consistency and availability guarantees. For example, you can wait for stronger consistency guarantees or loosen consistency requirements for higher availability.

Replica sets and sharded clusters support a global default read concern. Operations without an explicit read concern inherit the global default. See :dbcommand:`setDefaultRWConcern` for more information.

## Read Concern Levels

The following read concern levels are available:

.. include:: /includes/fact-readConcern-most-recent-data-in-node.rst

For more information on each read concern level, see:

- `/reference/read-concern-local`
- `/reference/read-concern-available`
- `/reference/read-concern-majority`
- `/reference/read-concern-linearizable`
- `/reference/read-concern-snapshot`
- `/reference/mongodb-defaults`
## `readConcern` Support

### Read Concern Option

For operations not in `multi-document transactions </core/transactions>`, you can specify a `readConcern` level as an option to commands and methods that support read concern:

```javascript
readConcern: { level: <level> }
```

To specify the read concern level for :binary:`~bin.mongosh` method :method:`db.collection.find()`, use the :method:`cursor.readConcern()` method:

```javascript
db.collection.find().readConcern(<level>)
```

### Transactions and Available Read Concerns

For `multi-document transactions <transactions>`, set the read concern at the transaction level, not at the individual operation level. Transaction operations use the transaction-level read concern. Read concerns set at the collection and database level are ignored inside the transaction. If you explicitly set the transaction-level read concern, the client-level read concern is also ignored.

> **Important:** Do not explicitly set the read concern for individual operations.
To set the read concern for transactions, see
`transaction-options`.

You can set the read concern at the transaction start:

- Multi-document transactions support the following read concern levels:
- :readconcern:`"local"`
- :readconcern:`"majority"`
- :readconcern:`"snapshot"`
- Write commands that are part of a :doc:`multi-document transactions
</core/transactions>` can support the transaction-level read concern.

- .. include:: /includes/extracts/transactions-create-collections-read-concern.rst
If unspecified at the transaction start, transactions use the session-level read concern or, if that is unset, the client-level read concern.

For more information, see `Transaction Read Concern <transactions-read-concern>`.

### Causally Consistent Sessions and Available Read Concerns

For operations in a `causally consistent session <causal-consistency>`, the :readconcern:`"local"`, :readconcern:`"majority"`, and :readconcern:`"snapshot"` levels are available. To guarantee causal consistency, use :readconcern:`"majority"`. For details, see `causal-consistency`.

### Operations That Support Read Concern

The following operations support read concern:

> **Important:** To set read concern for operations in a transaction, you set the
read concern at the transaction level, not at the individual
operation level. Do not explicitly set the read concern for the
individual operations in a transaction. For more information, see
`transactions-read-concern`.

.. include:: /includes/extracts/4.2-changes-linearizable-agg.rst

Read concern :readconcern:`"snapshot"` is available only for certain read operations and for multi-document transactions. In a transaction, you cannot use the `distinct` command or its helpers on a sharded collection.

The following write operations can also accept a read concern if part of a multi-document transaction:

> **Important:** To set read concern for operations in a transaction, you set the
read concern at the transaction level, not at the individual
operation level.

Read concern :readconcern:`"snapshot"` is available only for certain read operations and multi-document transactions. For transactions, set the read concern at the transaction level. Transaction operations that support :readconcern:`"snapshot"` correspond to the CRUD operations available in transactions. For more information, see `transactions-read-concern`.

### Read Concern not Supported on `local` Database

The `local database <replica-set-local-database>` does not support read concerns. MongoDB silently ignores any configured read concern for operations on collections in the local database.

## Considerations

### Read Your Own Writes

.. include:: /includes/fact-read-own-writes.rst

### Real Time Order

Combined with :writeconcern:`"majority"` write concern, :readconcern:`"linearizable"` read concern enables multiple threads to perform reads and writes on a single document as if a single thread performed these operations in real time. The corresponding schedule for these reads and writes is considered linearizable.

### Performance Comparisons

Unlike :readconcern:`"majority"`, :readconcern:`"linearizable"` read concern confirms with secondary members that the read operation reads from a primary capable of confirming writes with :writeconcern:`{ w: "majority" } <"majority">` write concern. [#edge-cases-2-primaries]_ Reads with linearizable read concern may be significantly slower than reads with :readconcern:`"majority"` or :readconcern:`"local"` read concerns.

Always use `maxTimeMS` with linearizable read concern if a majority of data-bearing members are unavailable. `maxTimeMS` ensures that the operation returns an error if the read concern cannot be fulfilled, rather than blocking indefinitely.

For example:

```javascript
db.restaurants.find( { _id: 5 } ).readConcern("linearizable").maxTimeMS(10000)

db.runCommand( {
     find: "restaurants",
     filter: { _id: 5 },
     readConcern: { level: "linearizable" },
     maxTimeMS: 10000
} )
```

.. include:: /includes/footnote-two-primaries-edge-cases.rst

### Read Operations and `afterClusterTime`

MongoDB supports `causally consistent sessions <sessions>`. For read operations in causally consistent sessions, drivers automatically set the `afterClusterTime` read concern option.

> **Important:** Do not manually set `afterClusterTime` for a read operation.
MongoDB drivers set this value automatically for operations
in causally consistent sessions. However, you can
advance the operation time and the cluster time for the session,
such as to be consistent with the operations of another client
session. For an example, see `causal-consistency-examples`.

> **Note:** You cannot specify `atClusterTime <atClusterTime>` together
with `afterClusterTime`. To use :ref:`atClusterTime
<atClusterTime>` with read concern `"snapshot"`, disable
`causally consistent sessions <sessions>`.

To satisfy a read request with an `afterClusterTime` value of `T`, a :binary:`~bin.mongod` must perform the request after its oplog reaches time `T`. If its oplog has not reached time `T`, the :binary:`~bin.mongod` waits to service the request.

Read operations with a specified `afterClusterTime` return data that meets both the `read concern level <read-concern-levels>` requirement and the specified `afterClusterTime` requirement.

For read operations not associated with causally consistent sessions, `afterClusterTime` is unset.

### Read Concern Provenance

MongoDB tracks read concern `provenance`, which indicates the source of a read concern. The `provenance` value appears in the :serverstatus:`getLastError <metrics.getLastError>` metrics, read concern error objects, and MongoDB logs.

The following table shows the possible read concern `provenance` values and their significance:

.. include:: /includes/fact-rc-provenance-table.rst

.. include:: /includes/unicode-checkmark.rst

## Contents

- "local" </reference/read-concern-local>
- "available" </reference/read-concern-available>
- "majority" </reference/read-concern-majority>
- "linearizable" </reference/read-concern-linearizable>
- "snapshot" </reference/read-concern-snapshot>
