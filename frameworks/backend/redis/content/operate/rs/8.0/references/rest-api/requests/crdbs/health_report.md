---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/8.0/references/rest-api/requests/crdbs/health_report.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.679614Z"
---
# Health_Report

---
Title: CRDB health report requests
alwaysopen: false
categories:
- docs
- operate
- rs
description: Active-Active database health report requests
headerRange: '[1-2]'
linkTitle: health_report
weight: $weight
url: '/operate/rs/8.0/references/rest-api/requests/crdbs/health_report/'
---

| Method | Path | Description |
|--------|------|-------------|
| [GET](#get-crdbs-health) | `/v1/crdbs/{crdb_guid}/health_report` | Get a health report for an Active-Active database |

## Get health report {#get-crdbs-health}

	GET /v1/crdbs/{crdb_guid}/health_report

Get a health report for an Active-Active database.

### Request {#get-request} 

#### Example HTTP request

    GET /v1/crdbs/{crdb_guid}/health_report

#### URL parameters

| Field | Type | Description |
|-------|------|-------------|
| crdb_guid | string | Globally unique Active-Active database ID (GUID) |

#### Query parameters

| Field | Type | Description |
|-------|------|-------------|
| instance_id | integer | The request retrieves information from the specified Active-Active database instance. If this instance doesn’t exist, the request retrieves information from all instances. (optional) |

### Response {#get-response} 

Returns a JSON array of [CRDB health report objects]({{< relref "/operate/rs/8.0/references/rest-api/objects/crdb/health_report" >}}).

### Status codes {#get-status-codes} 

| Code | Description |
|------|-------------|
| [200 OK](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) | Action was successful. |
| [404 Not Found](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.5) | Configuration or Active-Active database not found. |
