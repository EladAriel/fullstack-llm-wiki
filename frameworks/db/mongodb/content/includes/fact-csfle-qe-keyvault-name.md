---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-csfle-qe-keyvault-name.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

You may use any non-admin `namespace` to store your {+key-vault-long+}. By convention, the examples throughout this documentation use the  `encryption.__keyVault` `namespace`.

> **Warning:** Do not use the `admin` database to store encryption-related
collections. If you use the admin database for this collection, your
MongoDB client may not be able to access or decrypt your data due to
lack of permissions.
