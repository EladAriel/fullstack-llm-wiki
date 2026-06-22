---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-db-createEncryptedCollection-behavior.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The :method:`db.createEncryptedCollection()` method runs in the context of the current `db` and uses the same Queryable Encryption-enabled connection as the current `mongosh` session. Internally, it calls :method:`ClientEncryption.createEncryptedCollection()` with the current database name, the specified collection name, and the provided options document.

When `options.createCollectionOptions.encryptedFields.fields[*].keyId` is `null` or omitted, the method automatically creates the required data keys in the key vault and populates the corresponding `keyId` values in the created collection's `encryptedFields` definition.
