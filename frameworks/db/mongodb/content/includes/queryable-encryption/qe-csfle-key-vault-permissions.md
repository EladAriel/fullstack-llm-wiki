---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/qe-csfle-key-vault-permissions.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Applications with :authrole:`read` access to the {+key-vault-long+} can retrieve encrypted {+dek-long+} ({+dek-abbr+})s by querying the collection. However, only applications with access to the {+cmk-long+} ({+cmk-abbr+}) used to encrypt a {+dek-abbr+} can use that {+dek-abbr+} for encryption or decryption. You must grant your application access to both the {+key-vault-long+}  and your {+cmk-abbr+} to encrypt and decrypt documents with a {+dek-abbr+}.

To learn how to grant access to a MongoDB collection, see :manual:`Manage Users and Roles </tutorial/manage-users-and-roles/>` in the MongoDB manual.
