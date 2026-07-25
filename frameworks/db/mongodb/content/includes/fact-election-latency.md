---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-election-latency.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The median time before a cluster elects a new primary should not typically exceed 12 seconds, assuming default :rsconf:`replica configuration settings <settings>`. This includes time required to mark the primary as `unavailable <replication-auto-failover>` and call and complete an `election <replica-set-elections>`. You can tune this time period by modifying the :rsconf:`settings.electionTimeoutMillis` replication configuration option. Factors such as network latency may extend the time required for replica set elections to complete, which in turn affects the amount of time your cluster may operate without a primary. These factors are dependent on your particular cluster architecture.
