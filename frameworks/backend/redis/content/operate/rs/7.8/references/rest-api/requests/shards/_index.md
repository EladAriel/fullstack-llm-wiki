---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/rest-api/requests/shards/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Shard requests
alwaysopen: false
categories:
- docs
- operate
- rs
description: REST API requests for database shards
headerRange: '[1-2]'
hideListLinks: true
linkTitle: shards
weight: $weight
url: '/operate/rs/7.8/references/rest-api/requests/shards/'
---

| Method | Path | Description |
|--------|------|-------------|
| [GET](#get-all-shards) | `/v1/shards` | Get all shards |
| [GET](#get-shard) | `/v1/shards/{uid}` | Get a specific shard |

## Get all shards {#get-all-shards}

	GET /v1/shards

Get information about all shards in the cluster.

### Request {#get-all-request} 

#### Example HTTP request

	GET /v1/shards?extra_info_keys=used_memory_rss&extra_info_keys=connected_clients

#### Request headers

| Key | Value | Description |
|-----|-------|-------------|
| Host | cnm.cluster.fqdn | Domain name |
| Accept | application/json | Accepted media type |

#### Query parameters

| Field | Type | Description |
|-------|------|-------------|
| extra_info_keys | list of strings | A list of extra keys to be fetched (optional) |

### Response {#get-all-response} 

Returns a JSON array of [shard objects]({{<relref "/operate/rs/7.8/references/rest-api/objects/shard">}}).

#### Example JSON body

```json
[
  {
    "uid": "1",
    "role": "master",
    "assigned_slots": "0-16383",
    "bdb_uid": 1,
    "detailed_status": "ok",
    "loading": {
      "status": "idle"
    },
    "node_uid": "1",
    "redis_info": {
			"connected_clients": 14,
			"used_memory_rss": 12263424
		},
    "report_timestamp": "2024-06-28T18:44:01Z",
    "status": "active"
  },
  {
    "uid": 2,
    "role": "slave",
    // additional fields...
  }
]
```

### Status codes {#get-all-status-codes} 

| Code | Description |
|------|-------------|
| [200 OK](https://www.rfc-editor.org/rfc/rfc9110.html#name-200-ok) | No error. |

## Get shard {#get-shard}

	GET /v1/shards/{int: uid}

Gets information about a single shard.

### Request {#get-request} 

#### Example HTTP request

	GET /v1/shards/1?extra_info_keys=used_memory_rss&extra_info_keys=connected_clients

#### Request headers

| Key | Value | Description |
|-----|-------|-------------|
| Host | cnm.cluster.fqdn | Domain name |
| Accept | application/json | Accepted media type |

#### URL parameters

| Field | Type | Description |
|-------|------|-------------|
| uid | integer | The unique ID of the requested shard. |

#### Query parameters

| Field | Type | Description |
|-------|------|-------------|
| extra_info_keys | list of strings | A list of extra keys to be fetched (optional) |

### Response {#get-response} 

Returns a [shard object]({{<relref "/operate/rs/7.8/references/rest-api/objects/shard">}}).

#### Example JSON body

```json
{
  "assigned_slots": "0-16383",
  "bdb_uid": 1,
  "detailed_status": "ok",
  "loading": {
    "status": "idle"
  },
  "node_uid": "1",
  "redis_info": {
		"connected_clients": 14,
		"used_memory_rss": 12263424
	},
  "role": "master",
  "report_timestamp": "2024-06-28T18:44:01Z",
  "status": "active",
  "uid": "1"
}
```

### Status codes {#get-status-codes} 

| Code | Description |
|------|-------------|
| [200 OK](https://www.rfc-editor.org/rfc/rfc9110.html#name-200-ok) | No error. |
| [404 Not Found](https://www.rfc-editor.org/rfc/rfc9110.html#name-404-not-found) | Shard UID does not exist. |
