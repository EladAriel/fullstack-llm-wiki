---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/auc-considerations.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

- |uc| can only be run on sharded clusters.
- |uc| can only operate on sharded collections.
- |uc| can only operate on a single collection at a time.
- You cannot make topology changes, such as adding or removing shards
or transitioning between embedded and dedicated config servers, until |uc| completes.

- You cannot run the following operations on the collection that
is being unsharded while |uc| is in progress:

- :dbcommand:`collMod`
- :dbcommand:`convertToCapped`
- :dbcommand:`createIndexes`
- :method:`db.collection.createIndexes()`
- :dbcommand:`drop`
- :method:`db.collection.drop()`
- :dbcommand:`dropIndexes`
- :method:`db.collection.dropIndex()`
- :dbcommand:`renameCollection`
- :method:`db.collection.renameCollection()`
- You cannot run the following operations on the cluster while
`unshardCollection` is in progress:

- :dbcommand:`addShard`
- :dbcommand:`removeShard`
- :method:`db.createCollection()`
- :dbcommand:`dropDatabase`
- :dbcommand:`transitionToDedicatedConfigServer`
- :dbcommand:`transitionFromDedicatedConfigServer`
- Index builds that occur while |uc| is in progress might silently fail.
- Do not create indexes while |uc| is in progress.
- Do not call |uc| if there are ongoing index builds.
