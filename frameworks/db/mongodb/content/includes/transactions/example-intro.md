---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/transactions/example-intro.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

This example highlights the key components of the transactions API. In particular, it uses the callback API. The callback API:

- starts a transaction
- executes the specified operations
- commits the result or ends the transaction on error
Errors in server-side operations, such as the `DuplicateKeyError`, can end the transaction and result in a command error to alert the user that the transaction has ended. This behavior is expected and occurs even if the client never calls :method:`Session.abortTransaction()`. To incorporate custom error handling, use the `Core API <txn-core-api>` on your transaction.

The callback API incorporates retry logic for certain errors. The driver tries to rerun the transaction after a `TransientTransactionError <transient-transaction-error>` or `UnknownTransactionCommitResult <unknown-transaction-commit-result>` commit error.

Starting in MongoDB 6.2, the server does not retry the transaction if it receives a `TransactionTooLargeForCache <transactionTooLargeForCache-error>` error.
