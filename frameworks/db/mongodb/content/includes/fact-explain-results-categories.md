---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-explain-results-categories.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

|explain| operations can return information regarding:

- `explainVersion`, the output format version (for example, `"1"`).
- `command`, which details the command being explained.
- `queryShapeHash`, starting in MongoDB 8.0, which is a hexadecimal
string with the hash of a `query shape`. For details, see `query-shapes`, `explain-output-query-shape-hash`, and `explain.queryShapeHash`.

- `queryPlanner`, which details the plan selected by the
`query optimizer <read-operations-query-optimization>` and lists the rejected plans.

- `executionStats`, which details the execution of the winning
plan and the rejected plans.

- `serverInfo`, which provides information on the
MongoDB instance.

- `serverParameters`, which details internal parameters.
The verbosity mode (i.e. `queryPlanner`, `executionStats`, `allPlansExecution`) determines whether the results include `executionStats` and whether `executionStats` includes data captured during `plan selection <query-plans-query-optimization>`.

Explain output is limited by the maximum :limit:`Nested Depth for BSON Documents`, which is 100 levels of nesting. Explain output that exceeds the limit is truncated.
