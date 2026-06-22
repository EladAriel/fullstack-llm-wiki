---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/ShardingTaskExecutorPoolSizeForConfigServers-parameter.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Optional override for |parameter| to set the |maximum-or-minimum| number of outbound connections each TaskExecutor connection pool can open to a `configuration server <sharding-config-server>`.

When set to:

- `-1`, |parameter| is used. This is the default.
- an integer value greater than `-1`, overrides the
|maximum-or-minimum| number of outbound connections each TaskExecutor connection pool can open to a configuration server.

Parameter only applies to sharded deployments.
