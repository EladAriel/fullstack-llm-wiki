---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/qe-warning-local-keys.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Warning:** We recommend storing your {+cmk-long+}s in a remote :wikipedia:`{+kms-long+}
<Key_management#Key_management_system>` ({+kms-abbr+}). To learn how to use
a remote {+kms-abbr+} in your {+qe+} implementation, see the
`<qe-tutorial-automatic-encryption>` guide.
If you choose to use a local key provider in production, exercise great
caution and do not store it on the file system. Consider injecting the key
into your client application using a sidecar process, or use another
approach that keeps the key secure.
