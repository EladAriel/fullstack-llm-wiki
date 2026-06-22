---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-explain-verbosity-executionStats.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

MongoDB runs the `query optimizer <read-operations-query-optimization>` to choose the winning plan, executes the winning plan to completion, and returns statistics describing the execution of the winning plan.

.. include:: /includes/fact-explain-write-operations.rst

|explain| returns the `explain.queryPlanner` and `explain.executionStats` information for the evaluated |operation|. However, `explain.executionStats` does not provide query execution information for the rejected plans.
