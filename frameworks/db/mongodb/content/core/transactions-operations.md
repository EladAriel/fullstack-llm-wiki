---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/transactions-operations.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================

# Transactions and Operations

MongoDB provides the ability to use transactions across multiple operations, collections, databases, documents, and shards.

## Operations Supported in Multi-Document Transactions

### CRUD Operations

The following read/write operations are allowed in transactions:

.. include:: /includes/table-transactions-operations.rst

> **Note:** You can update a document's shard key value (unless the shard key
field is the immutable `_id` field) by issuing single-document
update / findAndModify operations either in a transaction or as a
`retryable write <retryable-writes>`. For details, see
`update-shard-key`.

### Count Operation

.. include:: /includes/extracts/transactions-count.rst

### Distinct Operation

.. include:: /includes/extracts/transactions-distinct.rst

### Administration Operations

You can create collections and indexes in transactions. For details, see `transactions-create-collections-indexes`. The collections used in a transaction can be in different databases.

> **Note:** .. include:: /includes/extracts/transactions-cross-shard-collection-restriction.rst

.. include:: /includes/transactions/create-collections-indexes-in-transaction.rst

Explicit Create Operations ``````````````````````````

> **Note:** For explicit creation of a collection or an index inside a
transaction, the transaction read concern level must be
:readconcern:`"local"`.

For more information on creating collections and indexes in a transaction, see `transactions-create-collections-indexes`.

Implicit Create Operations ``````````````````````````

You can also implicitly create a collection through the following write operations against a :red:`non-existing` collection:

For other CRUD operations allowed in transactions, see `transactions-operations-crud`.

For more information on creating collections and indexes in a transaction, see `transactions-create-collections-indexes`.

### Informational Operations

.. include:: /includes/extracts/transactions-operations-restrictions-info.rst

## Restricted Operations

The following operations are not allowed in transactions:

- Creating new collections in cross-shard write transactions. For
example, if you write to an existing collection in one shard and implicitly create a collection in a different shard, MongoDB cannot perform both operations in the same transaction.

- :ref:`Explicit creation of collections
<transactions-operations-ddl-explicit>`, e.g. :method:`db.createCollection()` method, and indexes, e.g. :method:`db.collection.createIndexes()` and :method:`db.collection.createIndex()` methods, when using a read concern level other than :readconcern:`"local"`.

- The :dbcommand:`listCollections` and :dbcommand:`listIndexes`
commands and their helper methods.

- Other non-CRUD and non-informational operations, such as
:dbcommand:`createUser`, :dbcommand:`getParameter`, :dbcommand:`count` and their helpers.

- Parallel operations. To update multiple namespaces concurrently, consider
using the :dbcommand:`bulkWrite` command instead.

- Writes to `capped <manual-capped-collection>` collections.
- Using read concern :readconcern:`"snapshot"` when reading
from a `capped <manual-capped-collection>` collection. (Starting in MongoDB 5.0)

- Reads/writes to collections in the `config`, `admin`, or `local`
databases.

- Writes to `system.*` collections.
- Using `explain` or similar commands to return the supported operation's
query plan.

- Calling :dbcommand:`getMore` on cursors created outside of a transaction,
or calling :dbcommand:`getMore` outside of a transaction on cursors created within a transaction.

- Specifying the :dbcommand:`killCursors` command as the first operation
in a `transaction <transactions>`.

> **Note:**  If you run the `killCursors` command within a
 transaction, the server immediately stops the specified
 cursors. It does **not** wait for the transaction to commit.

> **Seealso:** `txn-prod-considerations-ddl`
