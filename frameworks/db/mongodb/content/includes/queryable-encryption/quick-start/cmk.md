---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/quick-start/cmk.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

You must create a {+cmk-long+} ({+cmk-abbr+}) to perform {+qe+}.

Create a 96-byte {+cmk-long+} and save it to your filesystem as the file `master-key.txt`:

.. include:: /includes/queryable-encryption/qe-warning-local-keys.rst

.. include:: /includes/in-use-encryption/cmk-bash.rst
