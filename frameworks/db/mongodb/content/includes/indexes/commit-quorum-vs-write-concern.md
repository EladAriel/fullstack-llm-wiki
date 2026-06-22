---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/indexes/commit-quorum-vs-write-concern.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

There are important differences between `commit quorums <createIndexes-cmd-commitQuorum>` and `write concerns <write-concern>`:

- Index builds use commit quorums.
- Write operations use write concerns.
Each data-bearing node in a cluster is a voting member.

The commit quorum specifies how many data-bearing voting members, or which voting members, including the primary, must be prepared to commit a `simultaneous index build <index-operations-simultaneous-build>` before the primary will execute the commit.

The write concern is the level of acknowledgment that the write has propagated to the specified number of instances.

.. versionchanged:: 8.0 The commit quorum specifies how many
