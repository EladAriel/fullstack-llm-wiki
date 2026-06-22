---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/rest-api/requests/bdbs/shards.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Database shards requests
alwaysopen: false
categories:
- docs
- operate
- rs
description: REST API requests for database shards
headerRange: '[1-2]'
linkTitle: shards
weight: $weight
---

| Method | Path | Description |
|--------|------|-------------|
| [GET](#get-bdb-shards) | `/v1/bdbs/{bdb_uid}/shards` | Get the status of a database's shards |

## Get database shards {#get-bdb-shards}

	GET /v1/bdbs/{int: bdb_uid}/shards

Gets the status for all shards that belong to the specified database.

### Request {#get-request} 

#### Example HTTP request

	GET /v1/bdbs/1/shards?extra_info_keys=used_memory_rss&extra_info_keys=connected_clients

#### Request headers

| Key | Value | Description |
|-----|-------|-------------|
| Host | cnm.cluster.fqdn | Domain name |
| Accept | application/json | Accepted media type |

#### URL parameters

| Field | Type | Description |
|-------|------|-------------|
| bdb_uid | integer | The unique ID of the database. |

### Response {#get-response} 

The response body contains a JSON array with all shards, represented as [shard objects]({{<relref "/operate/rs/references/rest-api/objects/shard">}}).

#### Example JSON body

```json
[
    {
        "uid": "1",
		"role": "master",
		"assigned_slots": "0-8191",
        "bdb_uid": 1,
        "detailed_status": "ok",
        "loading": {
            "status": "idle"
        },
        "node_uid": "1",
        "redis_info": {
			"connected_clients": 14,
            "used_memory_rss": 12460032
        },
        "report_timestamp": "2024-09-13T15:28:10Z",
        "status": "active"
    },
    {
        "uid": 2,
        "role": "slave",
        // additional fields...
    }
]
```

### Status codes {#get-status-codes} 

| Code | Description |
|------|-------------|
| [200 OK](https://www.rfc-editor.org/rfc/rfc9110.html#name-200-ok) | No error. |
| [404 Not Found](https://www.rfc-editor.org/rfc/rfc9110.html#name-404-not-found) | bdb uid does not exist. |
