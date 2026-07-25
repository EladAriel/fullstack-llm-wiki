---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/qe-csfle-warning-azure-keyversion.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Warning:**  If you do not include a `keyVersion` field, {+azure-kv+} attempts
 to decrypt {+dek-long+}s using the latest {+cmk-long+}. If you
 rotate the {+cmk-abbr+} but do not :ref:`rewrap the
 {+dek-long+}s <qe-fundamentals-manage-keys>` with the new
 master key, attempting to decrypt an existing {+dek-abbr+}
 fails, since the {+dek-abbr+} is encrypted with the previous
 version of the {+cmk-abbr+}.
