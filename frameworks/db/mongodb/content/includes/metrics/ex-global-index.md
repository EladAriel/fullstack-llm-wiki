---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/metrics/ex-global-index.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

### Global Index Example

```javascript
{
    type: "op",
    desc: "GlobalIndex{Donor, Recipient, Coordinator}Service <globalIndexUUID}",
    op: "command",
    ns: "<database>.<collection>",
    originatingCommand: {
        createIndexes: "<database>.<collection>",
        key: <indexkeypattern>,
        unique: <boolean>,
        <Additional createIndexes options>
    },
   {donor, coordinator, recipient}State : "<service state>",
   approxDocumentsToScan: Long(<count>),
   approxBytesToScan: Long(<count>),
   bytesWrittenFromScan: Long(<count>),
   countWritesToStashCollections: Long(<count>),
   countWritesDuringCriticalSection : Long(<count>),
   countReadsDuringCriticalSection: Long(<count>),
   keysWrittenFromScan: Long(<count>),
   remainingOperationTimeEstimatedSecs: Long(<count>),
   allShardsLowestRemainingOperationTimeEstimatedSecs: Long(<estimate>),
   allShardsHighestRemainingOperationTimeEstimatedSecs: Long(<estimate>),
   totalCopyTimeElapsedSecs: Long(<count>),
   totalCriticalSectionTimeElapsedSecs : Long(<count>),
   totalOperationTimeElapsedSecs: Long(<count>),
}
```
