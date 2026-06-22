---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/sharding-field-note.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

In MongoDB versions earlier than 6.2, this field is included in the `config.version` collection, but in `mongosh` 2.0.0 and later, the field is not returned in the `sh.status()` output. Starting in MongoDB 6.2, this field is removed and not returned in any `mongosh` version or other client application. Instead, to obtain version information, see the `feature compatibility version (fcv) <view-fcv>`.
