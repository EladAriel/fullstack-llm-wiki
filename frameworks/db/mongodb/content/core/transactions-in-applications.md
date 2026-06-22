---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/transactions-in-applications.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========

# Drivers API

## Callback API vs Core API

The `txn-callback-api`:

- Starts a transaction, executes the specified operations, and commits
(or aborts on error).

- Automatically incorporates error handling logic for
`transient-transaction-error` and `unknown-transaction-commit-result`.

The `txn-core-api`:

- Requires explicit call to start the transaction and commit the
transaction.

- Does not incorporate error handling logic for
`transient-transaction-error` and `unknown-transaction-commit-result`, and instead provides the flexibility to incorporate custom error handling for these errors.

## Callback API

The callback API incorporates logic:

- To retry the transaction as a whole if the transaction encounters a
`transient-transaction-error` error.

- To retry the commit operation if the commit encounters an
`unknown-transaction-commit-result` error.

Starting in MongoDB 6.2, the server does not retry the transaction if it receives a `transactionTooLargeForCache-error` error.

### Example

----------

|arrow| Use the **Select your language** drop-down menu in the upper-right to set the language of the examples on this page.

----------

## Core API

The core transaction API does not incorporate retry logic for errors labeled:

- `transient-transaction-error`. If an operation in a transaction
returns an error labeled `transient-transaction-error`, the transaction as a whole can be retried.

To handle `transient-transaction-error`, applications should explicitly incorporate retry logic for the error.

- `unknown-transaction-commit-result`. If the commit returns an
error labeled `unknown-transaction-commit-result`, the commit can be retried.

To handle `unknown-transaction-commit-result`, applications should explicitly incorporate retry logic for the error.

### Example

----------

|arrow| Use the **Select your language** drop-down menu in the upper-right to set the language of the examples on this page.

----------

The following example incorporates logic to retry the transaction for transient errors and retry the commit for unknown commit error:

.. include:: /includes/driver-examples/driver-example-transactions-retry-3.rst

## Driver Versions

.. include:: /includes/list-4.2-drivers.rst

## Transaction Error Handling

Regardless of the database system, whether MongoDB or relational databases, applications should take measures to handle errors during transaction commits and incorporate retry logic for transactions.

### `TransientTransactionError`

The individual write operations inside the transaction are not retryable, regardless of the value of :urioption:`retryWrites`. If an operation encounters an error [associated with the label](https://github.com/mongodb/specifications/blob/master/source/transactions/transactions.rst#error-labels) `"TransientTransactionError"`, such as when the primary steps down, the transaction as a whole can be retried.

- The callback API incorporates retry logic for
`"TransientTransactionError"`.

- The core transaction API does not incorporate retry logic
for `"TransientTransactionError"`. To handle `"TransientTransactionError"`, applications should explicitly incorporate retry logic for the error. To view an example that incorporates retry logic for transient errors, see `Core API Example <txn-core-api-retry>`.

### `UnknownTransactionCommitResult`

Commit operations are `retryable write operations <retryable-writes>`. If the commit operation encounters an error, MongoDB drivers retry the commit regardless of the value of :urioption:`retryWrites`.

If the commit operation encounters an error labeled `"UnknownTransactionCommitResult"`, the commit can be retried.

- The callback API incorporates retry logic for
`"UnknownTransactionCommitResult"`.

- The core transaction API does not incorporate retry logic for
`"UnknownTransactionCommitResult"`. To handle `"UnknownTransactionCommitResult"`, applications should explicitly incorporate retry logic for the error. To view an example that incorporates retry logic for unknown commit errors, see `Core API Example <txn-core-api-retry>`.

### `TransactionTooLargeForCache`

.. versionadded:: 6.2

Starting in MongoDB 6.2, the server does not retry the transaction if it receives a `TransactionTooLargeForCache` error. This error means the cache is too small and a retry is likely to fail.

The default value for the :parameter:`transactionTooLargeForCacheThreshold` threshold is `0.75`. The server returns `TransactionTooLargeForCache` instead of retrying the transaction when the transaction uses more than 75% of the cache.

In earlier versions of MongoDB, the server returns `TemporarilyUnavailable` or `WriteConflict` instead of `TransactionTooLargeForCache`.

Use the :dbcommand:`setParameter` command to modify the error threshold.

## Additional Information

### `mongosh` Example

The following :binary:`~bin.mongosh` methods are available for transactions:

- :method:`Session.startTransaction()`
- :method:`Session.commitTransaction()`
- :method:`Session.abortTransaction()`
> **Note:** The :binary:`~bin.mongosh` example omits retry logic
and robust error handling for simplicity's sake. For a
more practical example of incorporating transactions in
applications, see `transactions-retry` instead.

```javascript
// Create collections:
db.getSiblingDB("mydb1").foo.insertOne(
    {abc: 0},
    { writeConcern: { w: "majority", wtimeout: 2000 } }
)
db.getSiblingDB("mydb2").bar.insertOne(
   {xyz: 0},
   { writeConcern: { w: "majority", wtimeout: 2000 } }
)

// Start a session.
session = db.getMongo().startSession( { readPreference: { mode: "primary" } } );

coll1 = session.getDatabase("mydb1").foo;
coll2 = session.getDatabase("mydb2").bar;

// Start a transaction
session.startTransaction( { readConcern: { level: "local" }, writeConcern: { w: "majority" } } );

// Operations inside the transaction
try {
   coll1.insertOne( { abc: 1 } );
   coll2.insertOne( { xyz: 999 } );
} catch (error) {
   // Abort transaction on error
   session.abortTransaction();
   throw error;
}

// Commit the transaction using write concern set at transaction start
session.commitTransaction();

session.endSession();
```
