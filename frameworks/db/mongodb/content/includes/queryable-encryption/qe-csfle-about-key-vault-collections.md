---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/qe-csfle-about-key-vault-collections.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Your {+key-vault-long+} is the MongoDB collection you use to store encrypted {+dek-long+} ({+dek-abbr+}) documents. {+dek-abbr+} documents are BSON documents that contain DEKs and have the following structure:

You create your {+key-vault-long+} as you would a standard MongoDB collection. Your {+key-vault-long+} must have a `unique index <index-type-unique>` on the `keyAltNames` field. To check if the unique index exists, run the :dbcommand:`listIndexes` command against the {+key-vault-long+}:

If the unique index does not exist, your application must create it before performing {+dek-abbr+} management.

To learn how to create a MongoDB collection, see `Databases and Collections <collections>`.

> **Tip:** The :binary:`~bin.mongosh` method
:method:`KeyVault.createKey()` automatically creates a
unique index on the `keyAltNames` field if one does not exist.
