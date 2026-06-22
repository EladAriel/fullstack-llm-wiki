---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/qe-warning-local-keys.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Warning:** We recommend storing your {+cmk-long+}s in a remote :wikipedia:`{+kms-long+}
<Key_management#Key_management_system>` ({+kms-abbr+}). To learn how to use
a remote {+kms-abbr+} in your {+qe+} implementation, see the
`<qe-tutorial-automatic-encryption>` guide.
If you choose to use a local key provider in production, exercise great
caution and do not store it on the file system. Consider injecting the key
into your client application using a sidecar process, or use another
approach that keeps the key secure.
