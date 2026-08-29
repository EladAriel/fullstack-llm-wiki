---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/rest-api/requests/crdbs/flush.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.390237Z"
---
# Flush

---
Title: CRDB flush requests
alwaysopen: false
categories:
- docs
- operate
- rs
description: Flush Active-Active database requests
headerRange: '[1-2]'
linkTitle: flush
weight: $weight
url: '/operate/rs/7.22/references/rest-api/requests/crdbs/flush/'
---

| Method | Path | Description |
|--------|------|-------------|
| [PUT](#put-crdbs-flush) | `/v1/crdbs/{crdb_guid}/flush` | Flush an Active-Active database |

## Flush an Active-Active database {#put-crdbs-flush}

```sh
PUT /v1/crdbs/{crdb_guid}/flush
```

Flush an Active-Active database.

Run flush from only one participating cluster. The flush operation propagates to all other clusters automatically.

### Request {#put-request}

#### Example HTTP request

```sh
PUT /v1/crdbs/552bbccb-99f3-4142-bd17-93d245f0bc79/flush
```

#### Headers

| Key | Value | Description |
|-----|-------|-------------|
| X-Task-ID | string | Specified task ID |
| X-Result-TTL | integer | Time (in seconds) to keep task result |

#### URL parameters

| Field | Type | Description |
|-------|------|-------------|
| crdb_guid | string | Globally unique Active-Active database ID (GUID) |

#### Query parameters

| Field | Type | Description |
|-------|------|-------------|
| async_flush | boolean | Perform asynchronous flush operation (optional) |

### Response {#put-response}

Returns a [CRDB task object]({{< relref "/operate/rs/7.22/references/rest-api/objects/crdb_task" >}}).

#### Status codes {#put-status-codes}

| Code | Description |
|------|-------------|
| [200 OK](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) | Action was successful. |
| [400 Bad Request](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) | The request is invalid or malformed. |
| [401 Unauthorized](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) | Unauthorized request. Invalid credentials |
| [404 Not Found](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.5) | Configuration or Active-Active database not found. |
| [406 Not Acceptable](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.7) | Configuration cannot be accepted, typically because it was already committed. |
