---
type: "Framework Learn Page"
framework: "jest"
source_repo: "https://github.com/jestjs/jest"
source_branch: "main"
source_path: "docs/EnvironmentVariables.md"
source_commit: "1865dd8659f5131715c780fa92f40623fce2f9c9"
source_commit_short: "1865dd86"
source_commit_date: "2026-06-21T13:50:36+02:00"
generated_at: "2026-06-21T11:51:37Z"
---

---
id: environment-variables
title: Environment Variables
---

Jest sets the following environment variables:

### `NODE_ENV`

Set to `'test'` if it's not already set to something else.

### `JEST_WORKER_ID`

Each worker process is assigned a unique id (index-based that starts with `1`). This is set to `1` for all tests when [`runInBand`](CLI.md#--runinband) is set to true.
