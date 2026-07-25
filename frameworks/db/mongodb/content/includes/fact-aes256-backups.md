---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-aes256-backups.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

For `encrypted storage engines <encrypted-storage-engine>` that use `AES256-GCM` encryption mode, `AES256-GCM` requires that every process use a unique counter block value with the key.

.. include:: /includes/extracts/4.2-changes-ese-key-rollover.rst
