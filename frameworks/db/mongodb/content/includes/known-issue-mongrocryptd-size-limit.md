---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/known-issue-mongrocryptd-size-limit.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

:issue:`SERVER-118428`: Changes to `mongocryptd` limit the maximum size of messages that `mongocryptd` can receive to 16 KiB. Users may encounter this issue when they send commands larger than 16 KiB through automatic Client-Side Field Level Encryption (CSFLE) or Queryable Encryption.

| To avoid this bug, skip these versions when you upgrade `mongocryptd` or use the `crypt_shared library <qe-reference-shared-library>`.
