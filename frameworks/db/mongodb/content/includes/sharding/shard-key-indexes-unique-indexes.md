---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/sharding/shard-key-indexes-unique-indexes.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

MongoDB can enforce a uniqueness constraint on a ranged shard key index. Using a unique index on the shard key enforces uniqueness on the entire key combination and not individual components of the shard key.

For a ranged sharded collection, only the following indexes can be `unique <index-type-unique>`:

- The index on the shard key
- A `compound index` where the shard key is a :ref:`prefix
<compound-index-prefix>`

- The default `_id index; however, the id` index only
enforces the uniqueness constraint **per shard** if the `_id` field is not the shard key.

.. include:: /includes/sharding/shard-collection-uniqueness-enforcement-note.rst

.. include:: /includes/sharding/sharding-unique-index-constraints.rst

To enforce uniqueness on the shard key values, pass the `unique` parameter as `true` to the :method:`sh.shardCollection()` method:

.. include:: /includes/extracts/shard-collection-unique-restriction-method.rst

You cannot specify a unique constraint on a `hashed index <index-type-hashed>`.

To maintain uniqueness on a field that is not your shard key, see `shard-key-arbitrary-uniqueness`.
