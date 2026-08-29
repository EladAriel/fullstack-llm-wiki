---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/8.0/references/cli-utilities/crdb-cli/task/cancel.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.668218Z"
---
# Cancel

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
url: '/operate/rs/8.0/references/cli-utilities/crdb-cli/task/cancel/'
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
