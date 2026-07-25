---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/remove-documents.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

.. include:: /includes/java-sync-links.rst

.. include:: /includes/java-async-links.rst

================

# Delete Documents

You can delete documents in MongoDB using the following methods:

.. include:: /includes/fact-methods.rst

## Behavior

### Indexes

Delete operations do not drop indexes, even if deleting all documents from a collection.

> **Note:** .. include:: /includes/crud/atomicity-write-acknowledgement-note.rst
