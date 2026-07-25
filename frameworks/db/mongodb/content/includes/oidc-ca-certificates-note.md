---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/oidc-ca-certificates-note.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

For environments using X509 TLS certificates signed by an internal Certificate Authority (CA), you must add the CA certificate to the system CA certificate bundle so that :binary:`~bin.mongod` can communicate with the identity provider. This applies to user authentication and to workload authentication when using the callback method. Omitting this step might result in OIDC SSL Certificate or JWT Key Verification errors.
