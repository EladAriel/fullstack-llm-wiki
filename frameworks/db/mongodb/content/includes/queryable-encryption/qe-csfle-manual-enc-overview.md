---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/qe-csfle-manual-enc-overview.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

{+manual-enc-first+} provides fine-grained control over security, at the cost of increased complexity when configuring collections and writing code for MongoDB Drivers. With {+manual-enc+}, you specify how to encrypt fields in your document for each operation you perform on the database, and you include this logic throughout your application.
