---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/csfle/reference/server-side-schema.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================

# CSFLE Server-Side Schema Enforcement

In {+csfle+} ({+csfle-abbrev+})-enabled client applications, you can use :manual:`schema validation </core/schema-validation>` to have your MongoDB instance enforce encryption of specific fields. To specify which fields require encryption, use the `automatic encryption rule keywords <field-level-encryption-json-schema>` with the :query:`$jsonSchema` validation object. The server rejects any write operations to that collection where the specified fields are not :bsontype:`Binary (BinData) <Binary>` subtype 6 objects.

To learn how a {+csfle-abbrev+}-enabled client configured to use automatic encryption behaves when it encounters a server-side schema, see `field-level-encryption-automatic-remote-schema`.

To learn how a {+csfle-abbrev+}-enabled client configured to use {+manual-enc+} behaves when it encounters a server-side schema, see `csfle-fundamentals-manual-encryption-server-side-schema`.

## Example

Consider an `hr` database with an `employees` collection. Documents in the `employees` collection have the following form:

You want to enforce the following behavior for client applications using your collection:

with the incorrect encryption algorithm into this collection. Does schema validation not check the encryption algorithm used?

- When encrypting the `age` field, clients must follow these
encryption rules:

- Use the {+dek-long+} with an `_id` of
`UUID("e114f7ad-ad7a-4a68-81a7-ebcb9ea0953a")`.

- Use the
`randomized <field-level-encryption-random>` encryption algorithm.

- The `age` field must be an integer.
- When encrypting the `name` field, clients must follow these
encryption rules:

- Use the {+dek-long+} with an `_id` of
`UUID("33408ee9-e499-43f9-89fe-5f8533870617")`.

- Use the
`deterministic <field-level-encryption-deterministic>` encryption algorithm.

- The `name` field must be a string.
The following :binary:`~bin.mongosh` code uses the :dbcommand:`collMod` command to update the `hr.employees` collection to include a `validator` to enforce the preceding behavior:

## Learn More

To learn more about the encryption algorithms {+csfle-abbrev+} supports, see `csfle-reference-encryption-algorithms`.

To learn more about encryption schemas and encryption rules, see `csfle-reference-encryption-schemas`.
