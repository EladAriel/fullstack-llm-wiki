---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/references/rest-api/requests/cluster/module-capabilities.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Cluster module capabilities requests
alwaysopen: false
categories:
- docs
- operate
- rs
description: Redis module capabilities requests
headerRange: '[1-2]'
linkTitle: module-capabilities
weight: $weight
url: '/operate/rs/7.4/references/rest-api/requests/cluster/module-capabilities/'
---

| Method | Path | Description |
|--------|------|-------------|
| [GET](#get-cluster-module-capabilities) | `/v1/cluster/module-capabilities` | List possible Redis module capabilities |

## List Redis module capabilities {#get-cluster-module-capabilities}

	GET /v1/cluster/module-capabilities

List possible Redis module capabilities.

#### Required permissions

| Permission name |
|-----------------|
| [view_cluster_modules]({{< relref "/operate/rs/7.4/references/rest-api/permissions#view_cluster_modules" >}}) |

### Request {#get-request} 

#### Example HTTP request

	GET /v1/cluster/module-capabilities 

#### Request headers

| Key | Value | Description |
|-----|-------|-------------|
| Host | cnm.cluster.fqdn | Domain name |
| Accept | \*/\* | Accepted media type |

### Response {#get-response} 

Returns a JSON object that contains a list of capability names and descriptions.

#### Example JSON body

```json
{
  "all_capabilities": [
    {"name": "types", "desc": "module has its own types and not only operate on existing redis types"},
    {"name": "no_multi_key", "desc": "module has no methods that operate on multiple keys"}
    "// additional capabilities..."
  ]
}
```

### Status codes {#get-status-codes} 

| Code | Description |
|------|-------------|
| [200 OK](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) | No error |

