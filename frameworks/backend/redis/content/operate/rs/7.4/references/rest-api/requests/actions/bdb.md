---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/references/rest-api/requests/actions/bdb.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Database actions requests
alwaysopen: false
categories:
- docs
- operate
- rs
description: Database actions requests
headerRange: '[1-2]'
linkTitle: bdb
weight: $weight
url: '/operate/rs/7.4/references/rest-api/requests/actions/bdb/'
---

| Method | Path | Description |
|--------|------|-------------|
| [GET](#get-db-actions) | `/v1/actions/bdb/{bdb_uid}` | Get the status of a specific database's actions |

## Get database actions {#get-db-actions}

```
GET /v1/actions/bdb/{bdb_uid}
```

Get the status of all currently executing, pending, or completed state-machine-related actions for a specific database. This API tracks short-lived API requests that return `action_uid`.

#### Required permissions

| Permission name |
|-----------------|
| [view_status_of_cluster_action]({{< relref "/operate/rs/7.4/references/rest-api/permissions#view_status_of_cluster_action" >}}) |

### Request {#get-request}

#### Example HTTP request

```
GET /v1/actions/bdb/1
```

#### URL parameters

| Field | Type | Description |
|-------|------|-------------|
| bdb_uid | string | Unique database ID |

### Response {#get-response}

Returns an array of JSON objects with attributes from [actions]({{< relref "/operate/rs/7.4/references/rest-api/objects/action" >}}) and [state machines]({{< relref "/operate/rs/7.4/references/rest-api/objects/state-machine" >}}).

Each action contains the following attributes: `name`, `action_uid`, `status`, and `progress`.

#### Example JSON body

```json
[
    {
        "action_uid": "8afc7f70-f3ae-4244-a5e9-5133e78b2e97",
        "heartbeat": 1703067908,
        "name": "SMUpdateBDB",
        "object_name": "bdb:1",
        "pending_ops": {},
        "progress": 50.0,
        "state": "proxy_policy",
        "status": "active"
    }
]
```

### Status codes {#get-status-codes}

| Code | Description |
|------|-------------|
| [200 OK](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) | No error, response provides info about state-machine actions |
| [404 Not Found](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.5) | bdb not found |
