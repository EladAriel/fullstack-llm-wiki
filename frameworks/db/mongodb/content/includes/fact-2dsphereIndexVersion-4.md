---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-2dsphereIndexVersion-4.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 8.3, `2dsphereIndexVersion <2dsphere-index-versions>` is set to version `4` by default.

If you need to downgrade the `FCV <view-fcv>` to anything below 8.3, you must first drop the `2dsphere` version `4` indexes.
