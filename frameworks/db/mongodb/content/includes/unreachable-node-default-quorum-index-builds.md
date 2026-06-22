---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/unreachable-node-default-quorum-index-builds.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Important:** If a data-bearing voting node becomes unreachable and the
`commitQuorum <createIndexes-cmd-commitQuorum>` is set to the
default `votingMembers`, index builds can hang until that node
comes back online.
