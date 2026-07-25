---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/sharded-cluster-metadata-up-to-date.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

For an operation to succeed, the view of the metadata on the specific shard member must be up-to-date. The shard and the router issuing the request must have the same version of the chunks metadata.

If the metadata is not up-to-date, the operation fails with the `StaleConfig` error and the metadata refresh process is triggered. Refreshing the metadata can introduce additional operational latency.

On a secondary, a metadata refresh can take a long time if there is significant replication lag. For secondary reads, set `maxStalenessSeconds` to minimize the impact of replication lag.
