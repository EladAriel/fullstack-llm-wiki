---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/listSampledQueries.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================================

# $listSampledQueries (aggregation stage)

## Definition

## Syntax

`$listSampledQueries` has this syntax:

```javascript
{  
   $listSampledQueries: { namespace: <namespace> } 
}
```

## Behavior

- To list sampled queries for a single collection, specify
the collection in the `namespace` argument.

- To list sampled queries for all collections, omit the `namespace`
argument.

## Access Control

`$listSampledQueries` requires the :authrole:`clusterMonitor` role on the cluster.

## Limitations

- You cannot use `$listSampledQueries` on Atlas
:atlas:`multi-tenant </build-multi-tenant-arch>` configurations.

- You cannot use `$listSampledQueries` on standalone deployments.
- You cannot use `$listSampledQueries` directly against a
:option:`--shardsvr <mongod --shardsvr>` replica set. When running on a sharded cluster, `$listSampledQueries` must run against a `mongos`.

## Examples

## Output

The output fields differ for read and write queries.

### Read Queries

```none
{
   _id: <uuid>,  
   ns: "<database>.<collection>",
   collectionUuid: <collUUID>,
   cmdName: <find|aggregate|count|distinct>,
   cmd: {
     filter: <object>,
     collation: <object>,
     let: <object>
   },
   expireAt: <date>
}
```

### Write Queries

```none
{
   _id: <uuid>,
   ns: "<database>.<collection>",
   collectionUuid: <collUUID>,
   cmdName: <update|delete|findAndModify>,
   cmd: <object>,
   expireAt: <date>
}
```
