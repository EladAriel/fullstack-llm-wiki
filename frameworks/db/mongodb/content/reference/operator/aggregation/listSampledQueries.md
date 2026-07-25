---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/listSampledQueries.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
