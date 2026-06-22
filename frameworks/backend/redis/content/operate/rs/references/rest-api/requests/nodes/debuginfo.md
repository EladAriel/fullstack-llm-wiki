---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/rest-api/requests/nodes/debuginfo.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Node debug info requests
alwaysopen: false
categories:
- docs
- operate
- rs
description: Documents the Redis Software REST API /nodes/debuginfo requests.
headerRange: '[1-2]'
linkTitle: debuginfo
weight: $weight
---

| Method | Path | Description |
|--------|------|-------------|
| [GET](#get-debuginfo-all-nodes) | `/v1/nodes/debuginfo` | Get debug info from all nodes |
| [GET](#get-debuginfo-node) | `/v1/nodes/{node_uid}/debuginfo` | Get debug info from a specific node |

## Get debug info from all nodes {#get-debuginfo-all-nodes}

	GET /v1/nodes/debuginfo

Downloads a tar file that contains debug info from all nodes.

#### Required permissions

| Permission name |
|-----------------|
| [view_debugging_info]({{< relref "/operate/rs/references/rest-api/permissions#view_debugging_info" >}}) |

### Request {#get-all-request} 

#### Example HTTP request

	GET /v1/nodes/debuginfo

### Response {#get-all-response} 

Downloads the debug info in a tar file called `filename.tar.gz`. Extract the files from the tar file to access the debug info.

#### Response headers

| Key | Value | Description |
|-----|-------|-------------|
| Content-Type | application/x-gzip | Media type of request/response body |
| Content-Length | 653350 | Length of the response body in octets |
| Content-Disposition | attachment; filename=debuginfo.tar.gz | Display response in browser or download as attachment |

### Status codes {#get-all-status-codes} 

| Code | Description |
|------|-------------|
| [200 OK](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) | Success. |
| [500 Internal Server Error](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) | Failed to get debug info. |

## Get node debug info {#get-debuginfo-node}

	GET /v1/nodes/{int: node_uid}/debuginfo

Downloads a tar file that contains debug info from a specific node.

#### Required permissions

| Permission name |
|-----------------|
| [view_debugging_info]({{< relref "/operate/rs/references/rest-api/permissions#view_debugging_info" >}}) |

### Request {#get-request} 

#### Example HTTP request

	GET /v1/nodes/1/debuginfo

### Response {#get-response} 

Downloads the debug info in a tar file called `filename.tar.gz`. Extract the files from the tar file to access the debug info.

#### Response headers

| Key | Value | Description |
|-----|-------|-------------|
| Content-Type | application/x-gzip | Media type of request/response body |
| Content-Length | 653350 | Length of the response body in octets |
| Content-Disposition | attachment; filename=debuginfo.tar.gz | Display response in browser or download as attachment |

### Status codes {#get-status-codes} 

| Code | Description |
|------|-------------|
| [200 OK](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) | Success. |
| [500 Internal Server Error](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) | Failed to get debug info. |
