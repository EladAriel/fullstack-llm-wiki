---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/rolling-index-build-cases.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Only use a `rolling index build <rolling-index-build>` if your deployment matches one of the following cases:

- If your average CPU utilization exceeds (N-1)/N-10% where where N is
the number of CPU threads available to mongod

- If your WiredTiger cache fill ratio regularly exceeds 90%
.. include:: /includes/warning-simultaneous-index-builds.rst

> **Note:** If your deployment does not meet this criteria, use the
`default index build <index-operations>`.

> **Tip:** With Atlas, you can temporarily [scale](https://www.mongodb.com/docs/atlas/scale-cluster/)
your cluster to meet the requirements for a traditional index build. However,
Atlas charges to scale your cluster. See [Cluster Configuration Costs](https://www.mongodb.com/docs/atlas/billing/cluster-configuration-costs/)
for more information.
