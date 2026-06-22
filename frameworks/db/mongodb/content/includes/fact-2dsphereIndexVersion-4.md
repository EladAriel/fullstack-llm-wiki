---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-2dsphereIndexVersion-4.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 8.3, `2dsphereIndexVersion <2dsphere-index-versions>` is set to version `4` by default.

If you need to downgrade the `FCV <view-fcv>` to anything below 8.3, you must first drop the `2dsphere` version `4` indexes.
