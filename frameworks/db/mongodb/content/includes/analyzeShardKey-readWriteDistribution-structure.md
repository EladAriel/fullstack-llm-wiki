---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/analyzeShardKey-readWriteDistribution-structure.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
