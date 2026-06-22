---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-diagnostic-info.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
