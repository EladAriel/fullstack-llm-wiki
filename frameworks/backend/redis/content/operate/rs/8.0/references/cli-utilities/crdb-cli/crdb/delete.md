---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/8.0/references/cli-utilities/crdb-cli/crdb/delete.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

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
url: '/operate/rs/8.0/references/cli-utilities/crdb-cli/crdb/delete/'
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
