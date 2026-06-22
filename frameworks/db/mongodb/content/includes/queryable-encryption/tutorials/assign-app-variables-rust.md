---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/tutorials/assign-app-variables-rust.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The code samples in this tutorial use the following variables to perform the {+qe+} workflow:

- **kms_provider_name** - The KMS you're using to store your
{+cmk-long+}. Set this variable to `"local"` for this tutorial.

- **uri** - Your MongoDB deployment connection URI. Set your
connection URI in the `MONGODB_URI` environment variable.

- **key_vault_database_name** - The database in MongoDB where
your data encryption keys (DEKs) will be stored. Set this variable to `"encryption"`.

- **key_vault_collection_name** - The collection in MongoDB
where your DEKs will be stored. Set this variable to `"__keyVault"`, which is the convention to help prevent mistaking it for a user collection.

- **key_vault_namespace** - The namespace in MongoDB where your
DEKs will be stored. Set this variable to a `Namespace` struct and pass the values of the `key_vault_database_name` and `key_vault_collection_name` variables.

- **encrypted_database_name** - The database in MongoDB where
your encrypted data will be stored. Set this variable to `"medicalRecords"`.

- **encrypted_collection_name** - The collection in MongoDB
where your encrypted data will be stored. Set this variable to `"patients"`.
