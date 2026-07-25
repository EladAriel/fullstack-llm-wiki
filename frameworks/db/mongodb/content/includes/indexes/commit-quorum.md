---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/indexes/commit-quorum.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Index creation is a `multistage process <index-build-process>`. The index creation process uses the `commit quorum` to minimize replication lag on secondary nodes.

When a secondary node receives a `commitIndexBuild` oplog entry, the node stops further oplog applications until the local index build can be committed. Index builds can take anywhere from moments to days to complete, so the replication lag can be significant if the secondary node builds more slowly than the primary.

To manage the replication lag, the commit quorum delays committing the index build on the primary node until a minimum number of secondaries are also ready to commit the index build.

The commit quorum does not guarantee that indexes on secondaries are ready for use when the command completes. To ensure that a specific number of secondaries are ready for use, set an appropriate `write concern <write-concern>`.

If a secondary node that is not included in the commit quorum receives a `commitIndexBuild` oplog entry, the node may block replication until its index build is complete.
