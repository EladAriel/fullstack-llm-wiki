---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/sharding/balancer-status-defrag-example.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

If the queried namespace is going through chunk defragmentation, the |balancer-command| returns output similar to the following:

```javascript
{
   "chunkSize": Long("128"),
   "balancerCompliant": false,
   "firstComplianceViolation": "defragmentingChunks",
   "details": {
      "currentPhase": "moveAndMergeChunks",
      "progress": { "remainingChunksToProcess": 1 }
   }
}
```

> **Note:** Chunk defragmentation occurs in multiple phases. The `progress` field
only pertains to the current phase.
