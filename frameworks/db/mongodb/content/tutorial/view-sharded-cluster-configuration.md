---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/view-sharded-cluster-configuration.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
