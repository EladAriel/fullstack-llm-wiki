---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/downgrade/single-version-support.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

MongoDB only supports single-version downgrades. You cannot downgrade to a release that is multiple versions behind your current release.

For example, you can downgrade a |newseries| to a |oldseries| deployment. However, further downgrading that |oldseries| deployment to a |olderseries| deployment is not supported.
