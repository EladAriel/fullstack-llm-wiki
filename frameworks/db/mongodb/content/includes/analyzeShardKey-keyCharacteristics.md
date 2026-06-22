---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/analyzeShardKey-keyCharacteristics.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

This is the structure of the `keyCharacteristics` document that is returned when `keyCharacteristics` is set to `true`:

```javascript
{
   keyCharacteristics: {
      numDocsTotal: <integer>,
      numOrphanDocs: <integer>, 
      avgDocSizeBytes: <integer>,
      numDocsSampled: <integer>,
      isUnique: <bool>,
      numDistinctValues: <integer>,
      mostCommonValues: [
        { value: <shardkeyValue>, frequency: <integer> },
        ...
      ],
      monotonicity: {
        recordIdCorrelationCoefficient: <double>,
        type: "monotonic"|"not monotonic"|"unknown",
    }
  }
}
```
