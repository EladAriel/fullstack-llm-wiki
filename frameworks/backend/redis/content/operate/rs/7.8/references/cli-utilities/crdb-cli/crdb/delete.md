---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/cli-utilities/crdb-cli/crdb/delete.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.476931Z"
---
# Delete

---
Title: crdb-cli crdb delete
alwaysopen: false
categories:
- docs
- operate
- rs
description: Deletes an Active-Active database.
linkTitle: delete
weight: $weight
url: '/operate/rs/7.8/references/cli-utilities/crdb-cli/crdb/delete/'
---

Deletes an Active-Active database.

```sh
crdb-cli crdb delete --crdb-guid <guid>
         [ --no-wait ]
```

This command is irreversible. If the data in your database is important, back it up before you delete the database.

### Parameters

| Parameter           | Value  | Description                         |
|---------------------|--------|-------------------------------------|
| crdb-guid | string | The GUID of the database (required) |
| no-wait             |        | Does not wait for the task to complete |

### Returns

Returns the task ID of the task that is deleting the database.

If `--no-wait` is specified, the command exits. Otherwise, it will wait for the database to be deleted and return `finished`.

### Example

```sh
$ crdb-cli crdb delete --crdb-guid db6365b5-8aca-4055-95d8-7eb0105c0b35
Task dfe6cacc-88ff-4667-812e-938fd05fe359 created
  ---> Status changed: queued -> started
  ---> Status changed: started -> finished
```
