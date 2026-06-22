---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/getMore-slow-queries.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 5.1, when a :dbcommand:`getMore` command is logged as a `slow query <log-message-slow-ops>`, the `queryHash <query-hash>` and `planCacheKey <plan-cache-key>` fields are added to the `slow query log message <log-message-slow-ops>` and the `profiler log message <database-profiler>`.

.. include:: /includes/plan-cache-rename.rst
