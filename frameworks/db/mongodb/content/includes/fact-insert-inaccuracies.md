---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-insert-inaccuracies.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Even if you encounter a server error during an insert, some documents may have been inserted.

After a successful insert, the system returns |writeResult|, the number of documents inserted into the collection. If the insert operation is interrupted by a replica set state change, the system may continue inserting documents. As a result, |writeResult| may report fewer documents than actually inserted.
