---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/known-issue-mongrocryptd-size-limit.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

:issue:`SERVER-118428`: Changes to `mongocryptd` limit the maximum size of messages that `mongocryptd` can receive to 16 KiB. Users may encounter this issue when they send commands larger than 16 KiB through automatic Client-Side Field Level Encryption (CSFLE) or Queryable Encryption.

| To avoid this bug, skip these versions when you upgrade `mongocryptd` or use the `crypt_shared library <qe-reference-shared-library>`.
