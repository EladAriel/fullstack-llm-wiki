---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-insert-inaccuracies.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Even if you encounter a server error during an insert, some documents may have been inserted.

After a successful insert, the system returns |writeResult|, the number of documents inserted into the collection. If the insert operation is interrupted by a replica set state change, the system may continue inserting documents. As a result, |writeResult| may report fewer documents than actually inserted.
