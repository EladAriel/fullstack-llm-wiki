---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/ShardingTaskExecutorPoolSizeForConfigServers-parameter.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Optional override for |parameter| to set the |maximum-or-minimum| number of outbound connections each TaskExecutor connection pool can open to a `configuration server <sharding-config-server>`.

When set to:

- `-1`, |parameter| is used. This is the default.
- an integer value greater than `-1`, overrides the
|maximum-or-minimum| number of outbound connections each TaskExecutor connection pool can open to a configuration server.

Parameter only applies to sharded deployments.
