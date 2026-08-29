---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/rest-api/requests/migrations/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.396421Z"
---
# _Index

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
url: '/operate/rs/7.22/references/rest-api/requests/migrations/'
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
| [view_bdb_info]({{< relref "/operate/rs/7.22/references/rest-api/permissions#view_bdb_info" >}}) | admin<br />cluster_member<br />cluster_viewer<br />db_member<br />db_viewer<br />user_manager |

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
"migration": {
    "status": "foo",
    "lag": 123,
    "run_id": "5",
    "flush_counter": 2,
    "source_shards": [{"replication_id": "1", "replication_offset": 2}]
}
```

#### Status codes {#get-status-codes}

| Code | Description |
|------|-------------|
| [200 OK](https://www.rfc-editor.org/rfc/rfc9110.html#name-200-ok) | No error |
| [404 Not Found](https://www.rfc-editor.org/rfc/rfc9110.html#name-404-not-found) | Database does not exist |
