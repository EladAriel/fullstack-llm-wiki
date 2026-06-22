---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/references/cli-utilities/crdb-cli/task/cancel.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: crdb-cli task cancel
alwaysopen: false
categories:
- docs
- operate
- rs
description: Attempts to cancel a specified Active-Active database task.
linkTitle: cancel
weight: $weight
url: '/operate/rs/7.4/references/cli-utilities/crdb-cli/task/cancel/'
---

Cancels the Active-Active database task specified by the task ID.

```sh
crdb-cli task cancel --task-id <task_id>
```

### Parameters

| Parameter           | Value  | Description                         |
|---------------------|--------|-------------------------------------|
| task-id \<task_id\>  | string | An Active-Active database task ID (required) |

### Returns

Attempts to cancel an Active-Active database task.

Be aware that tasks may complete before they can be cancelled.

### Example

```sh
$ crdb-cli task cancel --task-id 2901c2a3-2828-4717-80c0-6f27f1dd2d7c 
```
