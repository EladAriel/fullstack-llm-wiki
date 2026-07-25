---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/transactionLifetimeLimitSeconds-parameter.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 5.0, if you change the :parameter:`transactionLifetimeLimitSeconds` parameter, you must also change :parameter:`transactionLifetimeLimitSeconds` to the same value on all config server replica set members. Keeping this value consistent:

- Ensures the routing table history is retained for at least as long as
the transaction lifetime limit on the shard replica set members.

- Reduces the transaction retry frequency and therefore improves
performance.
