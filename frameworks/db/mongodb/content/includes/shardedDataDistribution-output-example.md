---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/shardedDataDistribution-output-example.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

```json
[
  {
    "ns": "test.names",
    "shards": [
      {
        "shardName": "shard-1",
        "numOrphanedDocs": 0,
        "numOwnedDocuments": 6,
        "ownedSizeBytes": 366,
        "orphanedSizeBytes": 0
      },
      {
        "shardName": "shard-2",
        "numOrphanedDocs": 0,
        "numOwnedDocuments": 6,
        "ownedSizeBytes": 366,
        "orphanedSizeBytes": 0
      }
    ]
  }
]
```
