---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/confirm-use-config-shard.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

.. include:: /includes/confirm-sharded-cluster-config-server-intro.rst

The following example runs the `listShards command and tries to find a document where id` is set to `"config"`.

```javascript
db.adminCommand({ listShards: 1 })["shards"].find(element => element._id === "config")
```

In this example, the returned document has `_id` set to `"config"` which confirms that this cluster uses a config shard.

```javascript
{
  _id: "config",
  host: "configRepl/localhost:27018",
  state: 1,
  topologyTime: Timestamp({ t: 1732218671, i: 13 }),
  replSetConfigVersion: Long('-1')
}
```
