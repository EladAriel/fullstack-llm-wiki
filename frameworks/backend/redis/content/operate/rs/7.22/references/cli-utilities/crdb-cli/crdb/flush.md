---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/cli-utilities/crdb-cli/crdb/flush.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: crdb-cli crdb flush
alwaysopen: false
categories:
- docs
- operate
- rs
description: Clears all keys from an Active-Active database.
linkTitle: flush
weight: $weight
url: '/operate/rs/7.22/references/cli-utilities/crdb-cli/crdb/flush/'
---

Clears all keys from an Active-Active database.

```sh
crdb-cli crdb flush --crdb-guid <guid>
         [ --no-wait ]
```

This command is irreversible. If the data in your database is important, back it up before you flush the database.

Run flush from only one participating cluster. The flush operation propagates to all other clusters automatically.

### Parameters

| Parameter           | Value  | Description                         |
|---------------------|--------|-------------------------------------|
| crdb-guid  | string | The GUID of the database (required) |
| no-wait             |        | Does not wait for the task to complete |

### Returns

Returns the task ID of the task clearing the database.

If `--no-wait` is specified, the command exits. Otherwise, it will wait for the database to be cleared and return `finished`.

### Example

```sh
$ crdb-cli crdb flush --crdb-guid d84f6fe4-5bb7-49d2-a188-8900e09c6f66
Task 53cdc59e-ecf5-4564-a8dd-448d71f9e568 created
  ---> Status changed: queued -> started
  ---> Status changed: started -> finished
```
