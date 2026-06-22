---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/serverStatus/ftdcCollectionMetrics.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Reports aggregate metrics for FTDC (Full-Time Diagnostic Data Capture) collection runs since the MongoDB process started. Use these metrics to detect whether FTDC collections are falling behind the configured sampling period.

```javascript
ftdcCollectionMetrics : {
   collections : Long("<num>"),
   durationMicros : Long("<num>"),
   delayed : Long("<num>")
},
```
