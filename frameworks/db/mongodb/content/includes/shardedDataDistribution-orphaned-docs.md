---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/shardedDataDistribution-orphaned-docs.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 6.0.3, you can run an aggregation using the :pipeline:`$shardedDataDistribution` stage to confirm no orphaned documents remain:

```javascript
db.aggregate([
   { $shardedDataDistribution: { } },
   { $match: { "ns": "<database>.<collection>" } }
])
```

`$shardedDataDistribution` has output similar to the following:

.. include:: /includes/shardedDataDistribution-output-example.rst

Ensure that `"numOrphanedDocs"` is `0` for each shard in the cluster.
