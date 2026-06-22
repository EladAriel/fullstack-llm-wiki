---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/confirm-use-config-shard.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
