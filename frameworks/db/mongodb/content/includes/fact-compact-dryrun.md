---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-compact-dryrun.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

If enabled, the `compact` command returns an estimate of how much space, in bytes, compaction can reclaim from the targeted collection. If you run `compact` with `dryRun` set to `true`, MongoDB only returns the estimated value and does not perform any kind of compaction.
