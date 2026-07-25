---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/analyzeShardKey-readWriteDistribution-structure.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

This is the structure of the document that is returned when `readWriteDistribution` is set to `true`:

```javascript
{
   readDistribution: {
     sampleSize: {
       total: <integer>,
       find: <integer>,
       aggregate: <integer>,
       count: <integer>,
       distinct: <integer>
     },
     percentageOfSingleShardReads: <double>,
     percentageOfMultiShardReads: <double>,
     percentageOfScatterGatherReads: <double>,
     numReadsByRange: [
       <integer>,
       ...
     ]
   },
   writeDistribution: {
     sampleSize: {
       total: <integer>,
       update: <integer>,
       delete: <integer>,
       findAndModify: <integer>
     },
     percentageOfSingleShardWrites: <double>,
     percentageOfMultiShardWrites: <double>,
     percentageOfScatterGatherWrites: <double>,
     numWritesByRange: [
       <integer>,
       ...     
     ],
     percentageOfShardKeyUpdates: <double>,
     percentageOfSingleWritesWithoutShardKey: <double>,
     percentageOfMultiWritesWithoutShardKey: <double>
   }
}
```

.. include:: /includes/analyzeShardKey-read-and-write-distribution-metrics.rst
