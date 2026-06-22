---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-progressMonitor.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

`Progress Monitor <health-managers-progress-monitor>` runs tests to ensure that |HM| checks do not become stuck or unresponsive. Progress Monitor runs these tests in intervals specified by `interval`. If a health check begins but does not complete within the timeout given by `deadline`, Progress Monitor stops the `mongos <mongos>` and removes it from the cluster.
