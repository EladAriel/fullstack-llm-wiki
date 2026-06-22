---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-rs-conf-array-index.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

When updating the replica configuration object, access the replica set members in the :rsconf:`members` array with the **array index**. The array index begins with `0`. Do **not** confuse this index value with the value of the :rsconf:`members[n]._id` field in each document in the :rsconf:`members` array.
