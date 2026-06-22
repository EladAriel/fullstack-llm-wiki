---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/metrics/ex-resharding.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

### Resharding Output Example

```javascript
{
    shard: '<string>',
    totalCopyTimeElapsedSecs: Long('<count>'),
    totalApplyTimeElapsedSecs: Long('<count>'),
    totalCriticalSectionTimeElapsedSecs: Long('<count>'),
    totalIndexBuildTimeElapsedSecs: Long('<count>'),
    indexesToBuild: Long('<count>'),
    indexesBuilt: Long('<count>'),
    oplogEntriesFetched: Long('<count>'),
    oplogEntriesApplied: Long('<count>'),
    insertsApplied: Long('<count>'),
    updatesApplied: Long('<count>'),
    deletesApplied: Long('<count>'),
    type: 'op',
    desc: 'ReshardingMetrics{Donor|Recipient|Coordinator}Service <reshardingUUID>',
    op: 'command',
    ns: '<database>.<collection>',
    originatingCommand: {
       reshardCollection: '<database>.<collection>',
       key: '<shardkey>',
       unique:'<boolean>',
       collation: { locale: 'simple' }
    },
    totalOperationTimeElapsedSecs: Long('<count>'),
    recipientState: '<service state>',
    remainingOperationTimeEstimatedSecs: Long('<count>'),
    approxDocumentsToCopy: Long('<count>'),
    approxBytesToCopy: Long('<count>'),
    bytesCopied: Long('<count>'),
    countWritesToStashCollections: Long('<count>'),
    documentsCopied: Long('<count>'),
    provenance: 'reshardCollection'
}
```
