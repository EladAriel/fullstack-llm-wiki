---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/qe-tutorials/java-autoencryption.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

If you omit `keyVaultClient` or set `bypassAutomaticEncryption` to false in your `AutoEncryptionSettings` object, the driver creates a separate, internal `MongoClient`. The internal `MongoClient` configuration differs from the parent `MongoClient` by setting the `minPoolSize` to  0 and omitting the `AutoEncryptionSettings`.
