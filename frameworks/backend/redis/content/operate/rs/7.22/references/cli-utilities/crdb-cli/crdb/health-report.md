---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/cli-utilities/crdb-cli/crdb/health-report.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: crdb-cli crdb health-report
alwaysopen: false
categories:
- docs
- operate
- rs
description: Shows the health report of an Active-Active database.
linkTitle: health-report
weight: $weight
url: '/operate/rs/7.22/references/cli-utilities/crdb-cli/crdb/health-report/'
---

Shows the health report of the API management layer of an Active-Active database.

```sh
crdb-cli crdb health-report --crdb-guid <guid>
```

### Parameters

| Parameter           | Value  | Description                         |
|---------------------|--------|-------------------------------------|
| crdb-guid  | string | The GUID of the database (required) |

### Returns

Returns the health report of the API management layer of the database.

### Example

```sh
$ crdb-cli crdb health-report --crdb-guid d84f6fe4-5bb7-49d2-a188-8900e09c6f66
[
  {
    "active_config_version":1,
    "cluster_name":"cluster2.redis.local",
    "configurations":[
      {
        "causal_consistency":false,
        "encryption":false,
        "featureset_version":5,
        "instances":[
          {
            "cluster":{
              "name":"cluster1.redis.local",
              "url":"https:\/\/cluster1.redis.local:9443"
            },
            "db_uid":"",
            "id":1
          },
          {
            "cluster":{
              "name":"cluster2.redis.local",
              "url":"https:\/\/cluster2.redis.local:9443"
            },
            "db_uid":"1",
            "id":2
          }
        ],
        "name":"database1",
        "protocol_version":1,
        "status":"commit-completed",
        "version":1
      }
    ],
    "connections":[
      {
        "name":"cluster1.redis.local",
        "status":"ok"
      },
      {
        "name":"cluster2.redis.local",
        "status":"ok"
      }
    ],
    "guid":"d84f6fe4-5bb7-49d2-a188-8900e09c6f66",
    "name":"database1",
    "connection_error":null
  },
  {
    "active_config_version":1,
    "cluster_name":"cluster1.redis.local",
    "configurations":[
      {
        "causal_consistency":false,
        "encryption":false,
        "featureset_version":5,
        "instances":[
          {
            "cluster":{
              "name":"cluster1.redis.local",
              "url":"https:\/\/cluster1.redis.local:9443"
            },
            "db_uid":"4",
            "id":1
          },
          {
            "cluster":{
              "name":"cluster2.redis.local",
              "url":"https:\/\/cluster2.redis.local:9443"
            },
            "db_uid":"",
            "id":2
          }
        ],
        "name":"database1",
        "protocol_version":1,
        "status":"commit-completed",
        "version":1
      }
    ],
    "connections":[
      {
        "name":"cluster1.redis.local",
        "status":"ok"
      },
      {
        "name":"cluster2.redis.local",
        "status":"ok"
      }
    ],
    "guid":"d84f6fe4-5bb7-49d2-a188-8900e09c6f66",
    "name":"database1",
    "connection_error":null
  }
]
```
