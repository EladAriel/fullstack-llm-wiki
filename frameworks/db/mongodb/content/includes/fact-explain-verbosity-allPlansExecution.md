---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-explain-verbosity-allPlansExecution.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

MongoDB runs the `query optimizer </core/query-plans>` to choose the winning plan and executes the winning plan to completion. In `"allPlansExecution"` mode, MongoDB returns statistics describing the execution of the winning plan as well as statistics for the other candidate plans captured during `plan selection <query-plans-query-optimization>`.

.. include:: /includes/fact-explain-write-operations.rst

|explain| returns the `explain.queryPlanner` and `explain.executionStats` information for the evaluated |operation|. The `explain.executionStats` includes the completed query execution information for the winning plan.

If the query optimizer considered more than one plan, `explain.executionStats` information also includes the partial execution information captured during the `plan selection phase <query-plans-query-optimization>` for both the winning and rejected candidate plans.
