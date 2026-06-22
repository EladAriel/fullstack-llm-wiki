---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-system-buckets-collection-8.0.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

When you upgrade to |version|, if you have any `system.buckets` collections that are not time-series collections, you might need to :method:`drop <db.collection.drop()>` or :method:`rename <db.collection.renameCollection()>` those collections before you upgrade, depending on your 8.0 patch release:

MongoDB 8.0.5 and later You do not need to drop `system.buckets` collections that aren't time-series collections before you upgrade. However, you must drop or rename them after you complete your upgrade.

MongoDB 8.0.4 and earlier You must drop or rename `system.buckets` collections that aren't time-series collections before you upgrade. All `system.buckets` collections must have valid `time series options <cmd-sharded-time-series-collection-options>` configured before you upgrade to versions 8.0.0 - 8.0.4.

To determine whether you have `system.buckets` collections that are not time-series collections, use the :method:`db.getCollectionInfos()` method with a filter:

```javascript
db.getCollectionInfos(
   { 
      $and: [
         { name: { $regex: /^system\.buckets/ } },
         { 'options.timeseries': { $exists: false } }
      ]
   }
)
```
