---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/remove-documents.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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

### Atomicity

All write operations in MongoDB are atomic on the level of a single document. For more information on MongoDB and atomicity, see `/core/write-operations-atomicity`.

### Write Acknowledgement

With write concerns, you can specify the level of acknowledgment requested from MongoDB for write operations. For details, see `/reference/write-concern`.
