---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-encryption-options-create-collection.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 7.2, you can't specify `wiredTiger` storage engine encryption options when you create a collection with :method:`db.createCollection()`. To configure encryption for the WiredTiger storage engine, see `security-encryption-at-rest`.
