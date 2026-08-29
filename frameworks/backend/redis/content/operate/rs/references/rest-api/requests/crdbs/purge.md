---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/rest-api/requests/crdbs/purge.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.588369Z"
---
# Purge

---
Title: CRDB purge requests
alwaysopen: false
categories:
- docs
- operate
- rs
description: Purge removed Active-Active database requests
headerRange: '[1-2]'
linkTitle: purge
weight: $weight
---

| Method | Path | Description |
|--------|------|-------------|
| [PUT](#put-crdbs-purge) | `/v1/crdbs/{crdb_guid}/purge` | Purge data from an instance that was forcibly removed from the Active-Active database |

## Purge data from removed instance {#put-crdbs-purge}

	PUT /v1/crdbs/{crdb_guid}/purge

Purge the data from an instance that was removed from the
Active-Active database by force.

When you force the removal of an instance from an Active-Active
database, the removed instance keeps the data and configuration
according to the last successful synchronization.

To delete the data and configuration from the forcefully removed
instance you must use this API (Must be executed locally on the
removed instance).

### Request {#put-request} 

#### Example HTTP request

    PUT /v1/crdbs/1/purge

#### URL parameters

| Field | Type | Description |
|-------|------|-------------|
| crdb_guid | string | Globally unique Active-Active database ID (GUID) |

#### Request body

| Field | Type | Description |
|-------|------|-------------|
| instances | array of integers | Array of unique instance IDs |

### Response {#put-response} 

Returns a [CRDB task object]({{< relref "/operate/rs/references/rest-api/objects/crdb_task" >}}).

### Status codes {#put-status-codes} 

| Code | Description |
|------|-------------|
| [200 OK](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) | Action was successful. |
| [400 Bad Request](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) | The request is invalid or malformed. |
| [401 Unauthorized](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) | Unauthorized request. Invalid credentials |
| [404 Not Found](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.5) | Configuration, instance, or Active-Active database not found. |
