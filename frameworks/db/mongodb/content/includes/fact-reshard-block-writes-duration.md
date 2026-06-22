---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-reshard-block-writes-duration.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

|method-or-command| blocks writes early and forces resharding operations to complete.

During a resharding operation, MongoDB does not block writes until the estimated duration to complete the resharding operation is below a certain value. In MongoDB 8.0.12 or earlier, this value is two seconds. In MongoDB 8.0.13 or later, this value is 500 milliseconds.

If the current estimated duration is above the threshold but the time frame is acceptable to you, you can finish resharding faster by calling |method-or-command|. This blocks writes early and forces the resharding operation to complete.
