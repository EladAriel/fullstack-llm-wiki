---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/cqa-samplesPerSecond-limit.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

### samplesPerSeconds Upper Limit

The upper limit for `samplesPerSecond` is `50`. A higher rate causes the sampled queries to fill up 10GB of disk space in less than four days.

This table shows the estimated disk usage for each sample rate and duration combination:
