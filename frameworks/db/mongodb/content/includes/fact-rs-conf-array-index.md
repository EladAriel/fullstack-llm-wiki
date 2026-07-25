---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-rs-conf-array-index.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

When updating the replica configuration object, access the replica set members in the :rsconf:`members` array with the **array index**. The array index begins with `0`. Do **not** confuse this index value with the value of the :rsconf:`members[n]._id` field in each document in the :rsconf:`members` array.
