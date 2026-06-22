---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/qe-csfle-warning-local-keys.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Warning:** A local key file in your filesystem is insecure and is
**not recommended** for production. Instead,
you should store your {+cmk-long+}s in a remote
:wikipedia:`{+kms-long+} <Key_management#Key_management_system>`
({+kms-abbr+}).
To learn how to use a remote {+kms-abbr+} in your
{+in-use-encryption+} enabled application,
see the :ref:`{+qe+} Automatic Encryption Tutorial
<qe-tutorial-automatic-encryption>` or :ref:`{+csfle-abbrev+}
Automatic Encryption Tutorial <csfle-tutorial-automatic-encryption>`.
