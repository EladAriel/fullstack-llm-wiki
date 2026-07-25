---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/qe-csfle-warning-local-keys.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
