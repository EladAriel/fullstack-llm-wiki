---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/8.0/references/rest-api/requests/suffixes/_index.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Suffixes requests
alwaysopen: false
categories:
- docs
- operate
- rs
description: DNS suffixes requests
headerRange: '[1-2]'
hideListLinks: true
linkTitle: suffixes
weight: $weight
url: '/operate/rs/8.0/references/rest-api/requests/suffixes/'
---

| Method | Path | Description |
|--------|------|-------------|
| [GET](#get-all-suffixes) | `/v1/suffixes` | Get all DNS suffixes |

## Get all suffixes {#get-all-suffixes}

	GET /v1/suffixes

Get all DNS suffixes in the cluster.

### Request {#get-all-request} 

#### Example HTTP request

	GET /v1/suffixes 


#### Request headers

| Key | Value | Description |
|-----|-------|-------------|
| Host | cnm.cluster.fqdn | Domain name |
| Accept | application/json | Accepted media type |

### Response {#get-all-response} 

The response body contains a JSON array with all suffixes, represented as [suffix objects]({{< relref "/operate/rs/8.0/references/rest-api/objects/suffix" >}}).

#### Example JSON body

```json
[
    {
        "name": "cluster.fqdn",
        "// additional fields..."
    },
    {
        "name": "internal.cluster.fqdn",
        "// additional fields..."
    }
]
```

### Status codes {#get-all-status-codes} 

| Code | Description |
|------|-------------|
| [200 OK](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) | No error |
