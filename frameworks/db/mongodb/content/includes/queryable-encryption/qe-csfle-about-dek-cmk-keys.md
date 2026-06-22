---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/qe-csfle-about-dek-cmk-keys.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

In-use encryption uses a multi-level key hierarchy to protect your data, often called "`envelope encryption`" or "wrapping keys".

A {+cmk-long+} ({+cmk-abbr+}), sometimes called a {+kms-long+} ({+kms-abbr+}) key, is the top-level key you create in your customer provisioned key provider, such as a cloud KMS. The {+cmk-abbr+} encrypts {+dek-long+}s ({+dek-abbr+}), which in turn encrypt the fields in your documents. Without access to a {+cmk-abbr+}, your client application cannot decrypt the associated DEKs.

MongoDB stores DEKs, encrypted with your {+cmk-abbr+}, in the {+key-vault-long+} as BSON documents. MongoDB can never decrypt the DEKs, as key management is client-side and customer controlled.

If you delete a {+dek-abbr+}, all fields encrypted with that {+dek-abbr+} become permanently unreadable. If you delete a {+cmk-abbr+}, all fields encrypted with a {+dek-abbr+} using that {+cmk-abbr+} become permanently unreadable.

> **Warning:** The {+cmk-long+} is the most sensitive key in {+qe+}. If your
{+cmk-abbr+} is compromised, all of your encrypted data can be
decrypted. Use a remote {+kms-long+} to store your {+cmk-abbr+}.
