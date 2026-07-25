---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/audit-local-key-file-option.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

.. versionadded:: 5.3

Specifies the path and file name for a local audit key file for `audit log encryption <security-encryption-at-rest-audit-log>`.

> **Note:** Only use this option for testing because the key is
not secured. To secure the key, use
|audit-encryption-key-identifier-option| and an external Key
Management Interoperability Protocol (KMIP) server.

You cannot use both options together.

.. include:: /includes/note-audit-in-enterprise.rst
