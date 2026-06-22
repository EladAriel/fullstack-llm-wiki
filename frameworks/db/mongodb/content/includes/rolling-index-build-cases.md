---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/rolling-index-build-cases.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
