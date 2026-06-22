---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/indexes/template-commit-quorum-intro.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

To set the `commit quorum <createIndexes-cmd-commitQuorum>`, use |updateMethod-name| to specify the `commitQuorum` value.

`commitQuorum` specifies how many data-bearing voting members, or which voting members, including the primary, must be prepared to commit the index build before the primary will execute the commit. The default commit quorum is `votingMembers`, which means all data-bearing members.
