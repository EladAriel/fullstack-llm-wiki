---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/cli-utilities/crdb-cli/crdb/list.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

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
url: '/operate/rs/7.22/references/cli-utilities/crdb-cli/crdb/list/'
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
