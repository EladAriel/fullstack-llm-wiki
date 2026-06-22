---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/tutorials/assign-app-variables-python.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The code samples in this tutorial use the following variables to perform the {+qe+} workflow:

- **kms_provider_name** - The KMS you use to store your
{+cmk-long+}. Set this to your key provider: `"aws"`, `"azure"`, `"gcp"`, or `"kmip"`.

- **uri** - Your MongoDB deployment connection URI. Set your
connection URI in the `MONGODB_URI` environment variable or replace the value directly.

- **key_vault_database_name** - The MongoDB database where your
data encryption keys (DEKs) will be stored. Set this to `"encryption"`.

- **key_vault_collection_name** - The collection in MongoDB
where your DEKs will be stored. Set this to `"__keyVault"`.

- **key_vault_namespace** - The namespace in MongoDB where your
DEKs will be stored. Set this to the values of the `key_vault_database_name` and `key_vault_collection_name` variables, separated by a period.

- **encrypted_database_name** - The MongoDB database where your
encrypted data will be stored. Set this to `"medicalRecords"`.

- **encrypted_collection_name** - The collection in MongoDB
where your encrypted data will be stored. Set this to `"patients"`.
