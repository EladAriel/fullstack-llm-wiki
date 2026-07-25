---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/references/cli-utilities/crdb-cli/crdb/purge-instance.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: crdb-cli crdb purge-instance
alwaysopen: false
categories:
- docs
- operate
- rs
description: Deletes data from a local instance and removes it from the Active-Active
  database.
linkTitle: purge-instance
weight: $weight
url: '/operate/rs/7.4/references/cli-utilities/crdb-cli/crdb/purge-instance/'
---

Deletes data from a local instance and removes the instance from the Active-Active database.

```sh
crdb-cli crdb purge-instance --crdb-guid <guid>
         --instance-id <instance-id>
         [ --no-wait ]
```

Once this command finishes, the other replicas must remove this instance with [`crdb-cli crdb remove-instance --force`]({{< relref "/operate/rs/7.4/references/cli-utilities/crdb-cli/crdb/remove-instance" >}}).

### Parameters

| Parameter                 | Value  | Description                                      |
|---------------------------|--------|--------------------------------------------------|
| crdb-guid        | string | The GUID of the database (required)              |
| instance-id  | string | The ID of the local instance (required) |
| no-wait                   |        | Does not wait for the task to complete           |

### Returns

Returns the task ID of the task that is purging the local instance.

If `--no-wait` is specified, the command exits. Otherwise, it will wait for the instance to be purged and return `finished`.

### Example

```sh
$ crdb-cli crdb purge-instance --crdb-guid db6365b5-8aca-4055-95d8-7eb0105c0b35 --instance-id 2
Task add0705c-87f1-4c28-ad6a-ab5d98e00c58 created
  ---> Status changed: queued -> started
  ---> Status changed: started -> finished
```
