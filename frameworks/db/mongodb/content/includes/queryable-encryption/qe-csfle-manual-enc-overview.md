---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/qe-csfle-manual-enc-overview.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

{+manual-enc-first+} provides fine-grained control over security, at the cost of increased complexity when configuring collections and writing code for MongoDB Drivers. With {+manual-enc+}, you specify how to encrypt fields in your document for each operation you perform on the database, and you include this logic throughout your application.
