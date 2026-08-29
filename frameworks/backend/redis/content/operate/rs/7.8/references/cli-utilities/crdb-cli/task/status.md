---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/cli-utilities/crdb-cli/task/status.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.477811Z"
---
# Status

---
Title: crdb-cli task status
alwaysopen: false
categories:
- docs
- operate
- rs
description: Shows the status of a specified Active-Active database task.
linkTitle: status
weight: $weight
url: '/operate/rs/7.8/references/cli-utilities/crdb-cli/task/status/'
---

Shows the status of a specified Active-Active database task.

```sh
crdb-cli task status --task-id <task_id>
```

### Parameters

| Parameter           | Value  | Description                         |
|---------------------|--------|-------------------------------------|
| task-id \<task_id\>  | string | An Active-Active database task ID (required) |
| verbose              | N/A    | Returns detailed information when specified |
| no-verbose           | N/A    | Returns limited information when specified |

The `--verbose` and `--no-verbose` options are mutually incompatible; specify one or the other.

The `404 Not Found` error indicates an invalid task ID.  Use the [`task list`]({{< relref "/operate/rs/7.8/references/cli-utilities/crdb-cli/task/list" >}}) command to determine available task IDs.

### Returns

Returns the status of an Active-Active database task.

### Example

```sh
$ crdb-cli task status --task-id e1c49470-ae0b-4df8-885b-9c755dd614d0
Task-ID: e1c49470-ae0b-4df8-885b-9c755dd614d0
CRDB-GUID: 1d7741cc-1110-4e2f-bc6c-935292783d24
Operation: create_crdb
Status: finished
Worker-Name: crdb_worker:1:0
Started: 2022-10-12T09:33:41Z
Ended: 2022-10-12T09:33:55Z
```
