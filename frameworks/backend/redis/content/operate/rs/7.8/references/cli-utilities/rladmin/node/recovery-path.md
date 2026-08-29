---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/cli-utilities/rladmin/node/recovery-path.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.473946Z"
---
# Recovery Path

---
Title: rladmin node recovery_path set
alwaysopen: false
categories:
- docs
- operate
- rs
description: Sets a node's local recovery path.
headerRange: '[1-2]'
linkTitle: recovery_path
toc: 'true'
weight: $weight
url: '/operate/rs/7.8/references/cli-utilities/rladmin/node/recovery-path/'
---

Sets the node's local recovery path, which specifies the directory where [persistence files]({{< relref "/operate/rs/7.8/databases/configure/database-persistence" >}}) are stored. You can use these persistence files to [recover a failed database]({{< relref "/operate/rs/7.8/databases/recover" >}}).

```sh
rladmin node <ID> recovery_path set <path>
```

### Parameters

| Parameter | Type/Value                     | Description                                                                                   |
|-----------|--------------------------------|-----------------------------------------------------------------------------------------------|
| node      | integer                        | Sets the recovery path for the specified node                                            |
| path      | filepath                       | Path to the folder where persistence files are stored                                         |

### Returns

Returns `Updated successfully` if the recovery path was set. Otherwise, it returns an error.

### Example

```sh
$ rladmin node 2 recovery_path set /var/opt/redislabs/persist/redis
Updated successfully.
```
