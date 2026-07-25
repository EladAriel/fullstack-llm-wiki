---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/rest-api/requests/ocsp/status.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: OCSP status requests
alwaysopen: false
categories:
- docs
- operate
- rs
description: OCSP status requests
headerRange: '[1-2]'
linkTitle: status
weight: $weight
url: '/operate/rs/7.22/references/rest-api/requests/ocsp/status/'
---

| Method | Path | Description |
|--------|------|-------------|
| [GET](#get-status) | `/v1/ocsp/status` | Get OCSP status |

## Get OCSP status {#get-status}

	GET /v1/ocsp/status

Gets the latest cached status of the proxy certificate’s OCSP response.

#### Required permissions

| Permission name |
|-----------------|
| [view_ocsp_status]({{< relref "/operate/rs/7.22/references/rest-api/permissions#view_ocsp_status" >}}) |

### Request {#get-request} 

#### Example HTTP request

	GET /v1/ocsp/status 


#### Request headers

| Key | Value | Description |
|-----|-------|-------------|
| Host | cnm.cluster.fqdn | Domain name |
| Accept | application/json | Accepted media type |

### Response {#get-response} 

Returns an [OCSP status object]({{< relref "/operate/rs/7.22/references/rest-api/objects/ocsp_status" >}}).

#### Example JSON body

```json
{
    "responder_url": "http://responder.ocsp.url.com",
    "cert_status": "REVOKED",
    "produced_at": "Wed, 22 Dec 2021 12:50:11 GMT",
    "this_update": "Wed, 22 Dec 2021 12:50:11 GMT",
    "next_update": "Wed, 22 Dec 2021 14:50:00 GMT",
    "revocation_time": "Wed, 22 Dec 2021 12:50:04 GMT"
}
```

### Error codes {#get-error-codes} 

When errors occur, the server returns a JSON object with `error_code` and `message` fields that provide additional information. The following are possible `error_code` values:

| Code | Description |
|------|-------------|
| ocsp_unsupported_by_capability | Not all nodes support OCSP capability | 
| invalid_ocsp_response | The server returned a response that is not OCSP-compatible |

### Status codes {#get-status-codes} 

| Code | Description |
|------|-------------|
| [200 OK](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) | Success |
| [406 Not Acceptable](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.7) | Feature not supported in all nodes |