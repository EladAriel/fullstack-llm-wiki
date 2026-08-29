---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/rest-api/requests/suffix/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.590806Z"
---
# _Index

---
Title: Suffix requests
alwaysopen: false
categories:
- docs
- operate
- rs
description: DNS suffix requests
headerRange: '[1-2]'
hideListLinks: true
linkTitle: suffix
weight: $weight
---

| Method | Path | Description |
|--------|------|-------------|
| [GET](#get-suffix) | `/v1/suffix/{name}` | Get a single DNS suffix |

## Get suffix {#get-suffix}

	GET /v1/suffix/{string: name}

Get a single DNS suffix.

### Request {#get-request} 

#### Example HTTP request

	GET /v1/suffix/cluster.fqdn 


#### Request headers

| Key | Value | Description |
|-----|-------|-------------|
| Host | cnm.cluster.fqdn | Domain name |
| Accept | application/json | Accepted media type |


#### URL parameters

| Field | Type | Description |
|-------|------|-------------|
| name | string | The unique name of the suffix requested. |

### Response {#get-response} 

Returns a [suffix object]({{< relref "/operate/rs/references/rest-api/objects/suffix" >}}).

#### Example JSON body

```json
{
    "name": "cluster.fqdn",
    "// additional fields..."
}
```

### Status codes {#get-status-codes} 

| Code | Description |
|------|-------------|
| [200 OK](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) | No error |
| [404 Not Found](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.5) | Suffix name does not exist |
