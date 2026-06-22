---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/qe-csfle-warning-azure-keyversion.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Warning:**  If you do not include a `keyVersion` field, {+azure-kv+} attempts
 to decrypt {+dek-long+}s using the latest {+cmk-long+}. If you
 rotate the {+cmk-abbr+} but do not :ref:`rewrap the
 {+dek-long+}s <qe-fundamentals-manage-keys>` with the new
 master key, attempting to decrypt an existing {+dek-abbr+}
 fails, since the {+dek-abbr+} is encrypted with the previous
 version of the {+cmk-abbr+}.
