---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/rest-api/requests/jsonschema/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.582335Z"
---
# _Index

---
Title: JSON schema requests
alwaysopen: false
categories:
- docs
- operate
- rs
description: API object JSON schema requests
headerRange: '[1-2]'
hideListLinks: true
linkTitle: jsonschema
weight: $weight
---

| Method | Path | Description |
|--------|------|-------------|
| [GET](#get-jsonschema) | `/v1/jsonschema` | Get JSON schema of API objects |

## Get object JSON schema {#get-jsonschema}

	GET /v1/jsonschema

Get the JSON schema of various [Redis Software REST API objects]({{< relref "/operate/rs/references/rest-api/objects" >}}).

### Request {#get-request} 

#### Example HTTP request

	GET /v1/jsonschema?object=bdb 

#### Request headers

| Key | Value | Description |
|-----|-------|-------------|
| Host | cnm.cluster.fqdn | Domain name |
| Accept | application/json | Accepted media type |

#### Query parameters

| Field | Type | Description |
|-------|------|-------------|
| object | string | Optional. The API object name: 'cluster', 'node', 'bdb' etc. |

### Response {#get-response} 

Returns the JSON schema of the specified API object.

#### Example JSON body

```json
{
     "type": "object",
     "description": "An API object that represents a managed database in the cluster.",
     "properties": {
          "...."
     },
     "...."
}
```

### Status codes {#get-status-codes} 

| Code | Description |
|------|-------------|
| [200 OK](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) | Success. |
| [406 Not Acceptable](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.7) | Invalid object. |
