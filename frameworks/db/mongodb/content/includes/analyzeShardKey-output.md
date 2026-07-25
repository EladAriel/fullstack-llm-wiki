---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/analyzeShardKey-output.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

|analyzeShardKey| returns information regarding |kc-output| and |rw-output|.

- `keyCharacteristics` provides metrics about the cardinality,
frequency, and monotonicity of the shard key.

- `readWriteDistribution` provides metrics about query routing
patterns and the hotness of shard key ranges.
