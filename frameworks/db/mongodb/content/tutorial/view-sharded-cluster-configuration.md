---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/view-sharded-cluster-configuration.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==========================

# View Cluster Configuration

## List Databases

To list your databases, query the `databases` collection in the `config-database`. Connect :binary:`~bin.mongosh` to a :binary:`~bin.mongos` instance and run the following operation to get a full list of the databases in your cluster:

```javascript
use config
db.databases.find()
```

## List Shards

To list the current set of configured shards, use the :dbcommand:`listShards` command, as follows:

```javascript
db.adminCommand( { listShards : 1 } )
```

## View Cluster Details

To view cluster details, issue :method:`db.printShardingStatus()` or :method:`sh.status()`. Both methods return the same output.
