---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/indexes/template-commit-quorum-intro.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

To set the `commit quorum <createIndexes-cmd-commitQuorum>`, use |updateMethod-name| to specify the `commitQuorum` value.

`commitQuorum` specifies how many data-bearing voting members, or which voting members, including the primary, must be prepared to commit the index build before the primary will execute the commit. The default commit quorum is `votingMembers`, which means all data-bearing members.
