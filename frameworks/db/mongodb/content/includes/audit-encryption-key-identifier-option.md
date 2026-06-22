---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/audit-encryption-key-identifier-option.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

.. versionadded:: 6.0

Specifies the unique identifier of the Key Management Interoperability Protocol (KMIP) key for `audit log encryption <security-encryption-at-rest-audit-log>`.

You cannot use |audit-encryption-key-identifier-option| and |audit-local-keyfile-option| together.

.. include:: /includes/note-audit-in-enterprise.rst
