---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/reshard-collection-clone.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

During the clone phase:

- Each recipient shard creates a temporary, empty sharded collection with the
same collection options as the donor sharded collection. This new collection is the target for where recipient shards write the new data. The recipient shards do not create any index except the `_id` index until the index phase.

- Each recipient shard clones collection data from the donor shard,
including all documents that the recipient shard owns under the new shard key.
