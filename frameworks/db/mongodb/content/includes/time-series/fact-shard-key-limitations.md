---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/time-series/fact-shard-key-limitations.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

When sharding time series collections, you can only specify the following fields in the shard key:

- The `metaField`
- Sub-fields of `metaField`
- The `timeField`
You may specify combinations of these fields in the shard key. No other fields, including `_id`, are allowed in the shard key pattern.

When you specify the shard key:

- `metaField` can be either a:
- `Hashed shard key <sharding-hashed-sharding>`
- `Ranged shard key <sharding-ranged>`
- `timeField` must be:
- A `ranged shard key <sharding-ranged>`
- At the end of the shard key pattern
> **Tip:** Avoid specifying **only** the `timeField` as the shard key. Since
the `timeField` :ref:`increases monotonically
<shard-key-monotonic>`, it may result in all writes appearing on a
single chunk within the cluster. Ideally, data is evenly distributed
across chunks.
To learn how to best choose a shard key, see:
- `sharding-shard-key-requirements`
- `MongoDB Blog: On Selecting a Shard Key for MongoDB
  <https://www.mongodb.com/blog/post/on-selecting-a-shard-key-for-mongodb>`__.
