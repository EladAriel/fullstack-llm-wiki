---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-diagnostic-info.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

- :dbcommand:`aggregate`
- :dbcommand:`count`
- :dbcommand:`delete`
- :dbcommand:`distinct`
- `find` (`OP_QUERY<wire-op-query>` and
:dbcommand:`command<find>`)

- :dbcommand:`findAndModify`
- `getMore` (`OP_GET_MORE<wire-op-query>` and
:dbcommand:`command<getMore>`)

- :dbcommand:`insert`
- :dbcommand:`mapReduce`
- :dbcommand:`update`
These operations are also included in the logging of slow queries. See :setting:`~operationProfiling.slowOpThresholdMs` for more information about slow query logging.
