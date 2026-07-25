---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/audit-compression-mode-option.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

.. versionadded:: 5.3

Specifies the compression mode for `audit log encryption <security-encryption-at-rest-audit-log>`. You must also enable audit log encryption using either |audit-encryption-key-identifier-option| or |audit-local-keyfile-option|.

You can set this option to one of these values:

.. include:: /includes/note-audit-in-enterprise.rst
