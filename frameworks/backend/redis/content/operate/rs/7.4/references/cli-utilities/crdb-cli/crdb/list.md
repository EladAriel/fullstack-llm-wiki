---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/references/cli-utilities/crdb-cli/crdb/list.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.752748Z"
---
# List

---
Title: crdb-cli crdb list
alwaysopen: false
categories:
- docs
- operate
- rs
description: Shows a list of all Active-Active databases.
linkTitle: list
weight: $weight
url: '/operate/rs/7.4/references/cli-utilities/crdb-cli/crdb/list/'
---

Shows a list of all Active-Active databases.

```sh
crdb-cli crdb list
```

### Parameters

None

### Returns

Returns a list of all Active-Active databases that the cluster participates in. Each database is represented with a unique GUID, the name of the database, an instance ID, and the FQDN of the cluster that hosts the instance.

### Example

```sh
$ crdb-cli crdb list
CRDB-GUID                             NAME       REPL-ID  CLUSTER-FQDN
d84f6fe4-5bb7-49d2-a188-8900e09c6f66  database1  1        cluster1.redis.local
d84f6fe4-5bb7-49d2-a188-8900e09c6f66  database1  2        cluster2.redis.local
```
