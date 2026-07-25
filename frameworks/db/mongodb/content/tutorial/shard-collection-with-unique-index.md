---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/shard-collection-with-unique-index.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=======================================

# Sharded Collections with Unique Indexes

Unique indexes are not supported on sharded collections unless the index is the shard key or includes it as a prefix.

## About this Task

The uniqueness constraint on an index ensures that documents in the collection have a unique value set on the field. With sharded collections, MongoDB does not enforce the uniqueness constraint on the field unless the index is the shard key or it includes the shard key as a prefix. To prevent issues:

- For sharded collections, if you create a unique index that
doesn't use the shard key, MongoDB returns an error when you run the :dbcommand:`createIndexes` command.

- If you shard a collection and the collection contains a unique
index that doesn't use the shard key, MongoDB returns an error when you run the :dbcommand:`shardCollection` command.

## Steps

## Learn More

- `index-type-unique`
- `sharding-introduction`
- :dbcommand:`shardCollection`
- :dbcommand:`createIndexes`
- :method:`sh.shardCollection`
- :method:`db.collection.createIndex`
