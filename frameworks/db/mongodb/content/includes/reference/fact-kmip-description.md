---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/reference/fact-kmip-description.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

When `true`, `mongod` uses KMIP protocol version 1.0 or 1.1 instead of the default version. The default KMIP protocol is version 1.2.

To use `audit log encryption <security-encryption-at-rest-audit-log>` with KMIP version 1.0 or 1.1, you must specify :parameter:`auditEncryptKeyWithKMIPGet` at startup.
