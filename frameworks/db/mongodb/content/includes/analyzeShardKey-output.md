---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/analyzeShardKey-output.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

|analyzeShardKey| returns information regarding |kc-output| and |rw-output|.

- `keyCharacteristics` provides metrics about the cardinality,
frequency, and monotonicity of the shard key.

- `readWriteDistribution` provides metrics about query routing
patterns and the hotness of shard key ranges.
