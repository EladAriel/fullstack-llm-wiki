---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/tutorials/automatic/named-kms-note-rust.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

You can also provide a custom name for your KMS provider by passing the name as a string to the `with_name()` function. Providing a unique name for a KMS provider allows you to specify multiple KMS providers of the same type.

For example, you can name your |kms-provider| KMS provider |kms-provider-name| in your KMS credentials variable as shown in the following code:
