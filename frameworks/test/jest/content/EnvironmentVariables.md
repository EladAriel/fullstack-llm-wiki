---
type: "Framework Learn Page"
framework: "Jest"
source_repo: "https://github.com/jestjs/jest"
source_branch: "main"
source_path: "docs/EnvironmentVariables.md"
source_commit: "be425a0b0e3bd60a74e4a7e350aa38c63a2d25ef"
source_commit_short: "be425a0"
source_commit_date: "2026-08-28T13:51:49+02:00"
generated_at: "2026-08-29T09:40:10.460847Z"
---
# Environmentvariables

---
id: environment-variables
title: Environment Variables
---

Jest sets the following environment variables:

### `NODE_ENV`

Set to `'test'` if it's not already set to something else.

### `JEST_WORKER_ID`

Each worker process is assigned a unique id (index-based that starts with `1`). This is set to `1` for all tests when [`runInBand`](CLI.md#--runinband) is set to true.
