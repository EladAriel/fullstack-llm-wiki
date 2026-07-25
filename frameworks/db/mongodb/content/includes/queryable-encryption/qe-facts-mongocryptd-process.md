---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/qe-facts-mongocryptd-process.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The `mongocryptd` process:

- Uses the specified automatic encryption rules to mark fields in
read and write operations for encryption.

- Prevents unsupported operations from executing on encrypted
fields.

- Parses the encryption schema specified for the database connection.
Automatic encryption rules use a strict subset of JSON schema syntax. If the rules contain invalid automatic encryption syntax or any :query:`schema validation <$jsonSchema>` syntax, `mongocryptd` returns an error.

`mongocryptd` only performs the previous functions, and doesn't perform any of the following:

- `mongocryptd` doesn't perform encryption or decryption
- `mongocryptd` doesn't access any encryption key material
- `mongocryptd` doesn't listen over the network
To perform field encryption and automatic decryption, the drivers use the Apache-licensed [libmongocrypt](https://github.com/mongodb/libmongocrypt)_ library.
