---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/sharding-field-note.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

In MongoDB versions earlier than 6.2, this field is included in the `config.version` collection, but in `mongosh` 2.0.0 and later, the field is not returned in the `sh.status()` output. Starting in MongoDB 6.2, this field is removed and not returned in any `mongosh` version or other client application. Instead, to obtain version information, see the `feature compatibility version (fcv) <view-fcv>`.
