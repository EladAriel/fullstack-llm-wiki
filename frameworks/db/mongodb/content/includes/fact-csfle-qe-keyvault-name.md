---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-csfle-qe-keyvault-name.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

You may use any non-admin `namespace` to store your {+key-vault-long+}. By convention, the examples throughout this documentation use the  `encryption.__keyVault` `namespace`.

> **Warning:** Do not use the `admin` database to store encryption-related
collections. If you use the admin database for this collection, your
MongoDB client may not be able to access or decrypt your data due to
lack of permissions.
