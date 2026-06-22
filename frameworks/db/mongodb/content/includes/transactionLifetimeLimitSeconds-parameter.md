---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/transactionLifetimeLimitSeconds-parameter.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 5.0, if you change the :parameter:`transactionLifetimeLimitSeconds` parameter, you must also change :parameter:`transactionLifetimeLimitSeconds` to the same value on all config server replica set members. Keeping this value consistent:

- Ensures the routing table history is retained for at least as long as
the transaction lifetime limit on the shard replica set members.

- Reduces the transaction retry frequency and therefore improves
performance.
