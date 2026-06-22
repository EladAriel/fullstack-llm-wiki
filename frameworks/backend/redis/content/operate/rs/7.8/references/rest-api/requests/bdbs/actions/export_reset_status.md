---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/rest-api/requests/bdbs/actions/export_reset_status.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Export resets status database action requests
alwaysopen: false
categories:
- docs
- operate
- rs
description: Reset database export status requests
headerRange: '[1-2]'
linkTitle: export_reset_status
weight: $weight
url: '/operate/rs/7.8/references/rest-api/requests/bdbs/actions/export_reset_status/'
---

| Method | Path | Description |
|--------|------|-------------|
| [PUT](#put-bdbs-actions-export-reset-status) | `/v1/bdbs/{uid}/actions/export_reset_status` | Reset database export status |

## Reset database export status {#put-bdbs-actions-export-reset-status}

	PUT /v1/bdbs/{int: uid}/actions/export_reset_status

Resets the database's `export_status` to idle if an export is not in progress and clears the value of the `export_failure_reason` field.

### Permissions

| Permission name | Roles |
|-----------------|-------|
| [reset_bdb_current_export_status]({{< relref "/operate/rs/7.8/references/rest-api/permissions#reset_bdb_current_export_status" >}}) | admin<br />cluster_member<br />db_member |

### Request {#put-request}

#### Example HTTP request

```sh
PUT /v1/bdbs/1/actions/export_reset_status
```

#### Request headers

| Key | Value | Description |
|-----|-------|-------------|
| Host | cnm.cluster.fqdn | Domain name |
| Accept | application/json | Accepted media type |

#### URL parameters

| Field | Type | Description |
|-------|------|-------------|
| uid | integer | The unique ID of the database |

### Response {#put-response}

Returns a status code.

#### Status codes {#put-status-codes}

| Code | Description |
|------|-------------|
| [200 OK](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) | The request is accepted and is being processed. |
| [404 Not Found](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.5) | Attempting to perform an action on a nonexistent database. |
| [406&nbsp;Not&nbsp;Acceptable](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.7) | Not all the modules loaded to the database support 'backup_restore' capability |
| [409 Conflict](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.10) | Database is currently busy with another action. In this context, this is a temporary condition and the request should be reattempted later. |
