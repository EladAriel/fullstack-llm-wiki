---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/qe-csfle-schema-validation-warning.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

MongoDB uses `schema validation <schema-validation-overview>` to enforce encryption of specific fields in a collection. Without a client-side schema, the client downloads the server-side schema for the collection to determine which fields to encrypt. To avoid this issue, use client-side schema validation.

Because {+csfle-abbrev+} and {+qe+} do not provide a mechanism to verify the integrity of a schema, relying on a server-side schema means trusting that the server's schema has not been tampered with. If an adversary compromises the server, they can modify the schema so that a previously encrypted field is no longer labeled for encryption. This causes the client to send plaintext values for that field.
