---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-aes256-backups.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

For `encrypted storage engines <encrypted-storage-engine>` that use `AES256-GCM` encryption mode, `AES256-GCM` requires that every process use a unique counter block value with the key.

.. include:: /includes/extracts/4.2-changes-ese-key-rollover.rst
