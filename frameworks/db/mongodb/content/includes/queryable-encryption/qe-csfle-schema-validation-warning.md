---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/qe-csfle-schema-validation-warning.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

MongoDB uses `schema validation <schema-validation-overview>` to enforce encryption of specific fields in a collection. Without a client-side schema, the client downloads the server-side schema for the collection to determine which fields to encrypt. To avoid this issue, use client-side schema validation.

Because {+csfle-abbrev+} and {+qe+} do not provide a mechanism to verify the integrity of a schema, relying on a server-side schema means trusting that the server's schema has not been tampered with. If an adversary compromises the server, they can modify the schema so that a previously encrypted field is no longer labeled for encryption. This causes the client to send plaintext values for that field.
