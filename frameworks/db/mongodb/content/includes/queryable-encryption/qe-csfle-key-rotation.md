---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/qe-csfle-key-rotation.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

You rotate your {+cmk-abbr+} either manually or automatically on your provisioned key provider. MongoDB has no visibility into this process. Once you rotate the {+cmk-abbr+}, MongoDB uses it to wrap all new DEKs. It does not re-wrap existing encrypted DEKs. These are still wrapped with the prior {+cmk-abbr+}.

To rotate some or all of the encrypted DEKs in your key vault, use the :method:`KeyVault.rewrapManyDataKey()` method. It seamlessly re-wraps keys with the new {+cmk-abbr+} specified, without interrupting your application. The DEKs themselves are left unchanged after re-wrapping them with the new {+cmk-abbr+}.
