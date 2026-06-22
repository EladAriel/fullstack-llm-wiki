---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/audit-compression-mode-option.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

.. versionadded:: 5.3

Specifies the compression mode for `audit log encryption <security-encryption-at-rest-audit-log>`. You must also enable audit log encryption using either |audit-encryption-key-identifier-option| or |audit-local-keyfile-option|.

|audit-compression-mode-option| can be set to one of these values:

.. include:: /includes/note-audit-in-enterprise.rst
