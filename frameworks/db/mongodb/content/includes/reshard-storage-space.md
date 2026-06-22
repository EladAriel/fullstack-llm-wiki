---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/reshard-storage-space.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Ensure that the available storage space on each recipient shard is at least twice the storage size of the collection that you want to |op| plus its total index size, divided by the number of shards:

```none
( ( collection_storage_size + index_size ) * 2 ) / shard_count = storage_req
```

For example, consider a collection with a storage size of 2 TB data and a 400 GB index. To distribute it across four shards you'd need:

```none
( ( 2 TB collection + 0.4 TB index ) * 2 ) / 4 shards = 1.2 TB storage
```

To |op| this collection, each shard requires 1.2 TB of available storage.

On MongoDB Atlas, you may need to upgrade to the next tier of storage for the |op| operation. You can downgrade once the operation completes.
