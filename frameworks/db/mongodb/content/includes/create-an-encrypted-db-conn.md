---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/create-an-encrypted-db-conn.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The :binary:`~bin.mongosh` client-side field level and queryable encryption methods require a database connection configured for client-side encryption. If the current database connection was not initiated with client-side field level encryption enabled, either:

- Use the :method:`Mongo()` constructor from the `mongosh`
to establish a connection with the required client-side field level encryption options. The `Mongo()` method supports the following Key Management Service (KMS) providers for Customer Master Key (CMK) management:

- `Amazon Web Services KMS <qe-fundamentals-kms-providers-aws>`
- `Azure Key Vault <qe-fundamentals-kms-providers-azure>`
- `Google Cloud Platform KMS <qe-fundamentals-kms-providers-gcp>`
- `Locally Managed Key <qe-fundamentals-kms-providers-local>`
or

- Use the `mongosh` :ref:`command line options
<mongosh-client-side-field-level-encryption-options>` to establish a connection with the required options. The command line options only support the `Amazon Web Services KMS <qe-fundamentals-kms-providers-aws>` provider for CMK management.
