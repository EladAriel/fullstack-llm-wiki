---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-reshard-block-writes-duration.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

|method-or-command| blocks writes early and forces resharding operations to complete.

During a resharding operation, MongoDB does not block writes until the estimated duration to complete the resharding operation is below a certain value. In MongoDB 8.0.12 or earlier, this value is two seconds. In MongoDB 8.0.13 or later, this value is 500 milliseconds.

If the current estimated duration is above the threshold but the time frame is acceptable to you, you can finish resharding faster by calling |method-or-command|. This blocks writes early and forces the resharding operation to complete.
