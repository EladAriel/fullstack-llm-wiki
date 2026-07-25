---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/sharding/resharding-limitations.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

- Only one collection can be resharded at a time.
- :rsconf:`writeConcernMajorityJournalDefault` must be `true`.
- To reshard a collection that has a :ref:`uniqueness
<index-type-unique>` constraint, the new shard key must satisfy the `unique index requirements <sharding-shard-key-unique>` for any existing unique indexes.

- The following commands and corresponding shell methods are not
supported on the collection that is being resharded while the resharding operation is in progress:

- :dbcommand:`collMod`
- :dbcommand:`convertToCapped`
- :dbcommand:`createIndexes`
- :method:`~db.collection.createIndex()`
- :dbcommand:`drop`
- :method:`~db.collection.drop()`
- :dbcommand:`dropIndexes`
- :method:`~db.collection.dropIndex()`
- :dbcommand:`renameCollection`
- :method:`~db.collection.renameCollection()`
- If you run one of the following operations, the operation waits until
resharding completes before executing:

- :dbcommand:`addShard`
- :dbcommand:`removeShard`
- :dbcommand:`dropDatabase` on the database hosting the collection undergoing resharding
- If the collection you're resharding uses :atlas:`{+fts+}
</atlas-search>`, the search index becomes unavailable when the resharding operation completes. You need to manually rebuild the search index once the resharding operation completes.

- If the collection you're resharding is archived in :ref:`Atlas Online
Archives <manage-online-archive>`, the online archive files are marked as `Orphaned` once the resharding operation completes. You can :atlas:`create </online-archive/configure-online-archive/>` another online archive for the same database, collection, and fields as the orphaned archive as long as there is no other archive for that same combination in the `Active` state.
