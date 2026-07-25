---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/sharding/shard-key-indexes-unique-indexes.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
