---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/reshard-collection-commit.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

During the commit phase:

- The resharding coordinator waits for all shards to reach strict consistency,
then commits the resharding operation.

- The resharding coordinator instructs each donor and recipient shard
primary, independently, to rename the temporary sharded collection. The temporary collection becomes the new resharded collection.

- Each donor shard drops the old sharded collection.
