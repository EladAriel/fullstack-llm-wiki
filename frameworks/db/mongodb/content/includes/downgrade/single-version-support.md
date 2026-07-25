---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/downgrade/single-version-support.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

MongoDB only supports single-version downgrades. You cannot downgrade to a release that is multiple versions behind your current release.

For example, you can downgrade a |newseries| to a |oldseries| deployment. However, further downgrading that |oldseries| deployment to a |olderseries| deployment is not supported.
