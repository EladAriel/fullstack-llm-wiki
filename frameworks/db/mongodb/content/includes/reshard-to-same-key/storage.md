---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/reshard-to-same-key/storage.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Calculate the required storage space for the resharding operation by adding your collection size and index size, assuming a minimum oplog window of 24 hours by using this formula:

```none
Available storage required on each shard = [(collection size + index size) *2 ] / number of shards the collection will be distributed across.
```

For example, a 2TB collection and 400GB of indexes distributed across 4 shards will need a minimum of 1.2TB of available storage per shard:

```none
[ (2 TB + 400GB) * 2 ] / 4 shards = 1.2 TB / shard
```

You must confirm that you have the available storage space in your cluster.

If there is insufficient space or I/O headroom available, you must increase the storage size. If there is insufficient CPU headroom, you must scale up the cluster by selecting a higher instance size.

> **Tip:** If your MongoDB cluster is hosted on Atlas, you can use the Atlas UI to
review storage, CPU, and I/O headroom metrics.
