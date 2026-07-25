---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/config-shard-use-cases.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

You can consider using a config shard if your cluster has three or fewer shards.

If your application has demanding availability and resiliency requirements, consider deploying a dedicated config server. A dedicated config server provides isolation, dedicated resources, and consistent performance for critical cluster operations.

You should use a dedicated config server if you satisfy one or more of the following conditions:

- You plan to use more than three :ref:`shards
<sharding-sharded-cluster>`.

- You plan to use :ref:`Queryable Encryption
<qe-manual-feature-qe>` collections.

- You plan to use :opsmgr:`queryable backups
</tutorial/query-backup>` (on-prem).
