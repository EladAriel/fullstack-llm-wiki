---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-atlas-enable-autoscaling.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

For MongoDB Atlas, it is recommended to `configure storage auto-scaling <cluster-autoscaling>` to prevent long-running queries from filling up storage with temporary files.

If your Atlas cluster uses storage auto-scaling, the temporary files may cause your cluster to scale to the next storage tier.
