---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-explain-verbosity-executionStats.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

MongoDB runs the `query optimizer <read-operations-query-optimization>` to choose the winning plan, executes the winning plan to completion, and returns statistics describing the execution of the winning plan.

.. include:: /includes/fact-explain-write-operations.rst

|explain| returns the `explain.queryPlanner` and `explain.executionStats` information for the evaluated |operation|. However, `explain.executionStats` does not provide query execution information for the rejected plans.
