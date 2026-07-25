---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/listClusterCatalog.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===================

# $listClusterCatalog

## Definition

.. versionadded:: 8.0.10

> **Warning:** The `$listClusterCatalog` aggregation stage is unsupported and is not
guaranteed to be stable in a future release. Don't build
functionality that relies on a specific output format of this stage,
since the output may change in a future release.

The `$listClusterCatalog` aggregation stage outputs information for collections in a cluster, including names and creation options.

`$listClusterCatalog` must be the first stage in the pipeline.

You must call this stage against a database. When you run this stage against the `admin database`, it returns information about all collections in the cluster. When you run it against any other database, it returns information about all collections within that database.

## Syntax

The stage has the following syntax:

```javascript
 { 
   $listClusterCatalog: {
      shards: true,
      balancingConfiguration: true
   }
 }
```

The `$listClusterCatalog` stage takes a document with the following optional fields:

## Output

`$listClusterCatalog` returns a document per collection. Each document can contain the following fields:

```javascript
{
    "ns" : <string>,
    "db" : <string>,
    "type" : <string>,
    "idIndex" : <document>,
    "options" : <document>,
    "info" : <document>,
    "sharded" : <boolean>,
    "shardKey" : <document>,
    "shards" : [<string>],
    "balancingEnabled" : <boolean>,
    "balancingEnabledReason" : <document>,
    "autoMergingEnabled" : <boolean>,
    "chunkSize" : <int>
 }
```

The following table contains information about the fields that `$listClusterCatalog` returns:

## Restrictions

If you execute this command against the `admin` database, you need the :authaction:`listClusterCatalog` privilege action, which is included in the :authrole:`clusterMonitor` role.

To run this command against a specific database, you need the :authaction:`listCollections` privilege action, which is included in the :authrole:`read` role.

## Examples
