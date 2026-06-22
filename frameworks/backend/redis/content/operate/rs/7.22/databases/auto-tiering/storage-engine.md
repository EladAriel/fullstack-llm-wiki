---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/databases/auto-tiering/storage-engine.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Manage Auto Tiering storage engine
alwaysopen: false
categories:
- docs
- operate
- rs
description: Manage the storage engine used for your database with auto tiering enabled.
linkTitle: Manage storage engine
weight: 100
url: '/operate/rs/7.22/databases/auto-tiering/storage-engine/'
aliases: /operate/rs/7.22/databases/flash/storage-engine/
---

## Manage the storage engine

Redis Enterprise Auto Tiering supports two storage engines:

- Speedb: Redis proprietary storage engine. The default and recommended storage engine as of Redis Enterprise Software version 7.2.4.

- [RocksDB](https://rocksdb.org/): Used up to Redis version 6.2. Deprecated for later Redis versions.

{{<warning>}}Switching between storage engines requires guidance by Redis Support or your Account Manager.{{</warning>}}

### Change the storage engine

1. Change the cluster level configuration for default storage engine.

  * API:

      ``` sh
      curl -k -u <username>:<password> -X PUT -H "Content-Type: application/json" -d '{"bigstore_driver":"speedb"}' https://localhost:9443/v1/cluster
     ```

  * CLI:

      ```sh
      rladmin cluster config bigstore_driver {speedb | rocksdb}
      ```

2. Restart the each database on the cluster one by one.

     ```sh
     rladmin restart db { db:<id> | <name> }
     ```

{{<note>}} We recommend restarting your database at times with low usage and avoiding peak hours. For databases without persistence enabled, we also recommend using export to backup your database first.{{</note>}}

## Monitor the storage engine

To get the current cluster level default storage engine run:

* Use the `rladmin info cluster` command look for ‘bigstore_driver’.

* Use the REST API:

     ```sh
     curl -k -u <username>:<password> -X GET -H "Content-Type: application/json" https://localhost:9443/v1/cluster
     ```

Versions of Redis Enterprise 7.2 and later provide a metric called `bdb_bigstore_shard_count` to help track the shard count per database, filtered by `bdb_id` and by storage engine as shown below:


  ```sh
  bdb_bigstore_shard_count{bdb="1",cluster="mycluster.local",driver="rocksdb"} 1.0
  bdb_bigstore_shard_count{bdb="1",cluster="mycluster.local",driver="speedb"} 2.0
  ```

For more about metrics for Redis Enterprise’s integration with Prometheus, see [Prometheus integration]({{< relref "/integrate/prometheus-with-redis-enterprise/prometheus-metrics-definitions" >}}).
