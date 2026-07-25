---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/getMore-slow-queries.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 5.1, when a :dbcommand:`getMore` command is logged as a `slow query <log-message-slow-ops>`, the `queryHash <query-hash>` and `planCacheKey <plan-cache-key>` fields are added to the `slow query log message <log-message-slow-ops>` and the `profiler log message <database-profiler>`.

.. include:: /includes/plan-cache-rename.rst
