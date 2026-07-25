---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-db-createEncryptedCollection-behavior.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The :method:`db.createEncryptedCollection()` method runs in the context of the current `db` and uses the same Queryable Encryption-enabled connection as the current `mongosh` session. Internally, it calls :method:`ClientEncryption.createEncryptedCollection()` with the current database name, the specified collection name, and the provided options document.

When `options.createCollectionOptions.encryptedFields.fields[*].keyId` is `null` or omitted, the method automatically creates the required data keys in the key vault and populates the corresponding `keyId` values in the created collection's `encryptedFields` definition.
