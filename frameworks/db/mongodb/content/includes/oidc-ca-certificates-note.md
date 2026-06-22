---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/oidc-ca-certificates-note.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

For environments using X509 TLS certificates signed by an internal Certificate Authority (CA), you must add the CA certificate to the system CA certificate bundle so that :binary:`~bin.mongod` can communicate with the identity provider. This applies to user authentication and to workload authentication when using the callback method. Omitting this step might result in OIDC SSL Certificate or JWT Key Verification errors.
