---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-compact-dryrun.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

If enabled, the `compact` command returns an estimate of how much space, in bytes, compaction can reclaim from the targeted collection. If you run `compact` with `dryRun` set to `true`, MongoDB only returns the estimated value and does not perform any kind of compaction.
