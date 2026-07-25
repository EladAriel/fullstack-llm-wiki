---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/8.0/references/rest-api/requests/migrations/_index.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Migrations requests
alwaysopen: false
categories:
- docs
- operate
- rs
description: REST API request to get the migration status of a database in the cluster when using Replica Of.
headerRange: '[1-2]'
hideListLinks: true
linkTitle: migrations
weight: $weight
url: '/operate/rs/8.0/references/rest-api/requests/migrations/'
---

| Method | Path | Description |
|--------|------|-------------|
| [GET](#get-migrations) | `/v1/migrations/<uid>` | Get database migration status |

## Get migration status {#get-migrations}

```sh
GET /v1/migrations/<uid>
```

Gets the migration status of a database in the cluster when using Replica Of.

#### Required permissions

| Permission name | Roles |
|-----------------|-------|
| [view_bdb_info]({{< relref "/operate/rs/8.0/references/rest-api/permissions#view_bdb_info" >}}) | admin<br />cluster_member<br />cluster_viewer<br />db_member<br />db_viewer<br />user_manager |

### Request {#get-request}

#### Example HTTP request

```sh
GET /v1/migrations/1
```

#### Headers

| Key | Value | Description |
|-----|-------|-------------|
| Host | cnm.cluster.fqdn | Domain name |
| Accept | application/json | Accepted media type |

#### URL parameters

| Field | Type | Description |
|-------|------|-------------|
| uid | integer | The database's unique ID |

### Response {#get-response}

Returns a JSON array with all data required by the migration orchestrator.

#### Example response body

```json
{
  "migration": {
    "status": "string",
    "lag": 0,
    "rdb_size": 0,
    "rdb_transferred": 0,
    "run_id": "string",
    "flush_counter": 0,
    "source_shards": [
      {
        "replication_id": "string",
        "replication_offset": 0
      }
    ],
    "error": {
      "error_code": "string",
      "message": "string",
      "timestamp": "2019-08-24T14:15:22Z"
    }
  }
}
```

#### Status codes {#get-status-codes}

| Code | Description |
|------|-------------|
| [200 OK](https://www.rfc-editor.org/rfc/rfc9110.html#name-200-ok) | No error |
| [404 Not Found](https://www.rfc-editor.org/rfc/rfc9110.html#name-404-not-found) | Database does not exist |
