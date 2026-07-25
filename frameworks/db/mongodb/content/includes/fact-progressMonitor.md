---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-progressMonitor.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

`Progress Monitor <health-managers-progress-monitor>` runs tests to ensure that |HM| checks do not become stuck or unresponsive. Progress Monitor runs these tests in intervals specified by `interval`. If a health check begins but does not complete within the timeout given by `deadline`, Progress Monitor stops the `mongos <mongos>` and removes it from the cluster.
