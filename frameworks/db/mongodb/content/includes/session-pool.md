---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/session-pool.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

A session is checked out from a session pool to run database operations.

:parameter:`AbortExpiredTransactionsSessionCheckoutTimeout` sets the maximum number of milliseconds for a session to be checked out when attempting to end an expired transaction.

If the expired transaction is successfully ended, MongoDB increments :serverstatus:`metrics.abortExpiredTransactions.successfulKills`. If the transaction isn't successfully ended because it timed out when attempting to check out a session, MongoDB increments :serverstatus:`metrics.abortExpiredTransactions.timedOutKills`.
