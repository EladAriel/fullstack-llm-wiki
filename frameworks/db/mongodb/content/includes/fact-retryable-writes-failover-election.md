---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-retryable-writes-failover-election.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Your application connection logic should include tolerance for automatic failovers and the subsequent elections. MongoDB drivers can detect the loss of the primary and automatically `retry certain write operations <retryable-writes>` a single time, providing additional built-in handling of automatic failovers and elections:

Compatible drivers enable retryable writes by default
