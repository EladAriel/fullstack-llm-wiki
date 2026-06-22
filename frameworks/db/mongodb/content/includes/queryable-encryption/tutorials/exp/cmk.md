---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/tutorials/exp/cmk.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

You must create a {+cmk-long+} ({+cmk-abbr+}) to perform {+qe+}.

Create a 96-byte {+cmk-long+} and save it to the file `master-key.txt`:

.. include:: /includes/queryable-encryption/qe-warning-local-keys.rst

.. include:: /includes/in-use-encryption/cmk-bash.rst
