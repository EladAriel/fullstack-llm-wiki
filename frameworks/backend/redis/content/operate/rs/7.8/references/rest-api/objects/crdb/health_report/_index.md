---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/rest-api/objects/crdb/health_report/_index.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: CRDB health report object
alwaysopen: false
categories:
- docs
- operate
- rs
description: An object that represents an Active-Active database health report.
hideListLinks: true
linkTitle: health_report
weight: $weight
url: '/operate/rs/7.8/references/rest-api/objects/crdb/health_report/'
---

An object that represents an Active-Active database health report.

| Name | Type/Value | Description |
|------|------------|-------------|
| active_config_version | integer | Active configuration version |
| cluster_name | string | Name of local Active-Active cluster |
| configurations | array of [health_report_configuration]({{< relref "/operate/rs/7.8/references/rest-api/objects/crdb/health_report/health_report_configuration" >}}) objects | Stored database configurations |
| connection_error | string | Error string if remote cluster is not available |
| connections | {{<code>}}
[{
  "name": string,
  "replication_links": [ 
    {
      "link_uid": "bdb_uid:replica_uid", 
      "status": "up | down" 
    } ],
  "status": string
}, ...] {{</code>}} | Connections to other clusters and their statuses. A replication link's `bdb_uid` is the unique ID of a local database instance ([bdb]({{< relref "/operate/rs/7.8/references/rest-api/objects/bdb" >}})) in the current cluster. The `replica_uid` is the unique ID of the database's remote replica, located in the connected cluster. |
| name | string | Name of the Active-Active database |
