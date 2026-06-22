---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/storage.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======

# Storage

The `storage engine <storage-engines>` is the primary component of MongoDB responsible for managing data. MongoDB provides a variety of storage engines, allowing you to choose one most suited to your application.

The `journal` is a log that helps the database recover in the event of a hard shutdown. There are several configurable options that allows the journal to strike a balance between performance and reliability that works for your particular use case.

`/core/gridfs` is a versatile storage system that is suited to handling large files, such as those exceeding the 16 MB document size limit.

## Contents

- WiredTiger </core/wiredtiger>
- Journaling </core/journaling>
