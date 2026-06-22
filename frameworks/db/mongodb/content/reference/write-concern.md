---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/write-concern.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============

# Write Concern

Write concern describes the level of acknowledgment requested from MongoDB for write operations to a standalone :binary:`~bin.mongod`, `replica sets <replication>`, or `sharded clusters <sharding-background>`. In sharded clusters, :binary:`~bin.mongos` instances pass the write concern to the shards.

> **Note:** For `multi-document transactions <transactions>`, you set
the write concern at the transaction level, :red:`not at the individual
operation level`. Do not explicitly set the write concern for
individual write operations in a transaction.

Replica sets and sharded clusters support a global default write concern. Operations without an explicit write concern inherit the global default. The default global write concern is majority. See :dbcommand:`setDefaultRWConcern` for more information.

To learn more about setting the write concern for deployments hosted in {+atlas+}, see :atlas:`Build a Resilient Application with {+atlas+} </resilient-application/#write-concern>`

## Write Concern Specification

Write concern can include the following fields:

```javascript
{ w: <value>, j: <boolean>, wtimeout: <number> }
```

- `w <wc-w>`: Requests acknowledgment that the write operation
has propagated to a specified number of :binary:`~bin.mongod` instances or to :binary:`~bin.mongod` instances with specified tags.

- `j <wc-j>`: Requests acknowledgment that the write operation
has been written to the on-disk journal.

- `wtimeout <wc-wtimeout>`: Specifies a time limit to prevent
write operations from blocking indefinitely.

### `w` Option

The `w` option requests acknowledgment that the write operation has propagated to a specified number of :binary:`~bin.mongod` instances or to :binary:`~bin.mongod` instances with specified tags. If the write concern is missing the `w` field, MongoDB sets the `w` option to the default write concern.

> **Note:** If you use the :dbcommand:`setDefaultRWConcern` to set the default
write concern, you must specify a `w` field value.

The `w` option supports the following `w: <value>` write concerns:

> **Seealso:** - `default-mongodb-read-write-concerns`
- `replica-set-protocol-version`

### `j` Option

The `j` option requests acknowledgment from MongoDB that the write operation has been written to the `on-disk journal <journaling-internals>`.

> **Note:** - Specifying a write concern that includes `j: true` to a
  :binary:`~bin.mongod` instance running without journaling produces
  an error.
- If journaling is enabled, :writeconcern:`w:
  "majority" <"majority">` may imply `j: true`. The
  :rsconf:`writeConcernMajorityJournalDefault` replica set
  configuration setting determines the behavior. See
  `wc-ack-behavior` for details.
- A write concern that includes or implies `j: true` causes an
  immediate journal synchronization. See `journal-process`.

### `wtimeout`

This option specifies a time limit, in milliseconds, for a write operation to propagate to enough members to achieve the write concern after the operation succeeds on the primary. `wtimeout` does not apply if `w` is less than or equal to `1`. If the write operation does not achieve the write concern within this time limit, MongoDB returns a write concern error.

`wtimeout` causes write operations to return with a write concern error after the specified limit, even if the required write concern will eventually succeed. When these write operations return, MongoDB **does not** undo successful data modifications performed before the write concern exceeded the `wtimeout` time limit.

If you do not specify the `wtimeout` option and the level of write concern is unachievable, the write operation will block indefinitely. Specifying a `wtimeout` value of `0` is equivalent to a write concern without the `wtimeout` option.

> **Note:** To set a time limit on the primary write operation, use the
:method:`~cursor.maxTimeMS()` method.

## Implicit Default Write Concern

.. include:: /includes/5.0-default-wc.rst

.. include:: /includes/ddl-ops-write-concern-sharded-clusters.rst

## Acknowledgment Behavior

The `w <wc-w>` option and the `j <wc-j>` option determine when :binary:`~bin.mongod` instances acknowledge write operations.

### Standalone

A standalone :binary:`~bin.mongod` acknowledges a write operation after applying the write in memory or after writing to the on-disk journal. The following table lists the acknowledgment behavior for a standalone with the relevant write concerns:

> **Note:** .. include:: /includes/extracts/no-journaling-rollback.rst

### Replica Sets

The `w <wc-w>` value determines the number of replica set members that must acknowledge the write before returning success. For each eligible member, the `j <wc-j>` option determines whether the member acknowledges writes after applying the write in memory or after writing to the on-disk journal.

`w: "majority"` Any data-bearing voting member of the replica set can contribute to write acknowledgment of :writeconcern:`"majority"` write operations.

The following table lists when the member can acknowledge the write based on the `j <wc-j>` value:

`w: <number>` Any data-bearing member of the replica set can contribute to write acknowledgment of `w: \<number\> <wc-w>` write operations.

The following table lists when the member can acknowledge the write based on the `j <wc-j>` value:

> **Note:** `Hidden <replica-set-hidden-members>`,
`delayed <replica-set-delayed-members>`,
and `priority 0 <replica-set-secondary-only-members>`
members can acknowledge
:writeconcern:`w: \<number\> <\<number\>>` write operations.
Delayed secondaries can return write acknowledgment no earlier
than the configured :rsconf:`~members[n].secondaryDelaySecs`.

### Reads after { w: "majority" } Writes

Starting in MongoDB 8.0, `{ w: "majority" }` writes return an acknowledgment after a majority of data-bearing members durably write the oplog entry. Members then asynchronously apply the changes as they read them from their local oplogs. In earlier releases, MongoDB waited until members applied the write before returning the acknowledgment.

Queries on secondaries immediately after a `{ w: "majority" }` write acknowledgment may read from the collection before the secondary applies changes from the write.

If your application reads from secondaries and requires immediate access to changes from `{ w: "majority" }` writes, run these operations in a `causally consistent <causal-consistency>` session.

## Additional Information

### Read and Write Concern Recommendations

To read your own writes on the primary, use the :readconcern:`"majority"` read concern and the `{ w: "majority" }` write concern.

If you use a `{ w: n }` write concern where `n` is greater than the `calculated majority <calculating-majority-count>` of the cluster's nodes and the cluster uses the default settings, enable the `write concern "j" option <wc-j>` to acknowledge the write to the journal. The `"majority"` read concern only allows you to read updates that are `durable` on a majority of nodes in the replica set.

> **Note:** If you perform writes with a `{ w: n }` write concern and `n` is
greater than the calculated majority, without journaling and with
the default cluster settings, you may receive a write acknowledgement
before the write is durable on a majority of nodes.

### Causally Consistent Sessions and Write Concerns

`Causally consistent client sessions <sessions>` guarantee causal consistency only if:

- the associated read operations use :readconcern:`"majority"` read
concern, and

- the associated write operations use :writeconcern:`"majority"`
write concern.

For details, see `causal-consistency`.

### `w: "majority"` Behavior

- .. include:: /includes/extracts/no-journaling-rollback.rst
- `Hidden <replica-set-hidden-members>`,
`delayed <replica-set-delayed-members>`, and `priority 0 <replica-set-secondary-only-members>` members with :rsconf:`members[n].votes` greater than `0` can acknowledge :writeconcern:`"majority"` write operations.

- Delayed secondaries can return write acknowledgment no earlier
than the configured :rsconf:`~members[n].secondaryDelaySecs`.

- Starting in MongoDB 5.0, replica set members in the
:replstate:`STARTUP2` state do not participate in write majorities.

### Write Concern not Supported on `local` Database

The `local database <replica-set-local-database>` does not support write concerns. MongoDB silently ignores any configured write concern for operations on collections in the local database.

### Calculating Majority for Write Concern

> **Tip:** The :method:`rs.status()` returns the
`replSetGetStatus.writeMajorityCount` field which contains
the calculated majority number.

The majority for write concern :writeconcern:`"majority"` is calculated as the smaller of the following values:

- the majority of all voting members, including arbiters
- the number of all **data-bearing** voting members
> **Warning:** If the calculated majority equals the number of all
**data-bearing** voting members, such as in a 3-member
Primary-Secondary-Arbiter deployment, write concern
:writeconcern:`"majority"` may time out or never be acknowledged if
a data-bearing voting member is down or unreachable. If possible,
use a data-bearing voting member instead of an arbiter.

For example, consider:

- A replica set with 3 voting members, Primary-Secondary-Secondary
(P-S-S):

- The majority of all voting members is 2.
- The number of all data-bearing voting members is 3.
| The calculated majority is 2, the minimum of 2 and 3. The write must propagate to the primary and one of the secondaries to acknowledge the write concern :writeconcern:`"majority"` to the client.

- A replica set with 3 voting members, Primary-Secondary-Arbiter
(P-S-A):

- The majority of all voting members is 2.
- The number of all data-bearing voting members is 2.
| The calculated majority is 2, the minimum of 2 and 2. Since the write can only be applied to data-bearing members, the write must propagate to the primary and the secondary to acknowledge write concern :writeconcern:`"majority"` to the client.

> **Tip:**   Avoid using :writeconcern:`"majority"` write concern with P-S-A
  or other topologies that require all data-bearing voting members
  to be available to acknowledge writes. For the durability
  guarantees of a :writeconcern:`"majority"` write concern, deploy a
  topology that does not require all data-bearing voting members to
  be available, such as P-S-S.

.. include:: /includes/admonition-multiple-arbiters.rst

### Write Concern Provenance

MongoDB tracks write concern `provenance`, which indicates the source of a particular write concern. You may see `provenance` shown in the :serverstatus:`getLastError <metrics.getLastError>` metrics, write concern error objects, and MongoDB logs.

The following table shows the possible write concern `provenance` values and their significance:

.. include:: /includes/fact-wc-provenance-table.rst

### Write Concern Contrasted with Commit Quorum

.. include:: /includes/indexes/commit-quorum-vs-write-concern.rst

## Contents

- Lifecycle Diagrams </reference/write-concern/write-lifecycle>
