---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/session-pool.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

A session is checked out from a session pool to run database operations.

:parameter:`AbortExpiredTransactionsSessionCheckoutTimeout` sets the maximum number of milliseconds for a session to be checked out when attempting to end an expired transaction.

If the expired transaction is successfully ended, MongoDB increments :serverstatus:`metrics.abortExpiredTransactions.successfulKills`. If the transaction isn't successfully ended because it timed out when attempting to check out a session, MongoDB increments :serverstatus:`metrics.abortExpiredTransactions.timedOutKills`.
