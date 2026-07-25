---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/sharding/sharding-unique-index-constraints.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The unique index constraints mean that:

- For a to-be-sharded collection, you cannot shard the collection if
the collection has multiple unique indexes unless the shard key is the prefix for all the unique indexes.

- For an already-sharded collection, you cannot create unique indexes
on other fields unless the shard key is included as the prefix.

- A unique index stores a null value for a document missing the
indexed field; that is a missing index field is treated as another instance of a `null` index key value. For more information, see `unique-index-and-missing-field`.
