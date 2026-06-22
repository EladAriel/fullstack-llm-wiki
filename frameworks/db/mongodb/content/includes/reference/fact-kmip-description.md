---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/reference/fact-kmip-description.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

When `true`, `mongod` uses KMIP protocol version 1.0 or 1.1 instead of the default version. The default KMIP protocol is version 1.2.

To use `audit log encryption <security-encryption-at-rest-audit-log>` with KMIP version 1.0 or 1.1, you must specify :parameter:`auditEncryptKeyWithKMIPGet` at startup.
