---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/rest-api/requests/debuginfo/all/bdb.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: All nodes database debug info requests
alwaysopen: false
categories:
- docs
- operate
- rs
description: Documents the Redis Enterprise Software REST API debuginfo/all/bdb requests.
headerRange: '[1-2]'
linkTitle: bdb
weight: $weight
url: '/operate/rs/7.22/references/rest-api/requests/debuginfo/all/bdb/'
---

{{<banner-article>}}
This REST API path is deprecated as of Redis Enterprise Software version 7.4.2. Use the new path [`/v1/bdbs/debuginfo`]({{< relref "/operate/rs/7.22/references/rest-api/requests/bdbs/debuginfo" >}}) instead.
{{</banner-article>}}

| Method | Path | Description |
|--------|------|-------------|
| [GET](#get-all-debuginfo-bdb) | `/v1/debuginfo/all/bdb/{bdb_uid}` | Get debug info for a database from all nodes |

## Get database debug info for all nodes {#get-all-debuginfo-bdb}

	GET /v1/debuginfo/all/bdb/{int: bdb_uid}

Downloads a tar file that contains debug info for the specified database (`bdb_uid`) from all nodes.

#### Required permissions

| Permission name |
|-----------------|
| [view_debugging_info]({{< relref "/operate/rs/7.22/references/rest-api/permissions#view_debugging_info" >}}) |

### Request {#get-all-request} 

#### Example HTTP request

	GET /v1/debuginfo/all/bdb/1 

### Response {#get-all-response} 

Downloads the debug info in a tar file called `filename.tar.gz`. Extract the files from the tar file to access the debug info.

#### Response headers

| Key | Value | Description |
|-----|-------|-------------|
| Content-Type | application/x-gzip | Media type of request/response body |
| Content-Length | 653350 | Length of the response body in octets |
| Content-Disposition | attachment; filename=debuginfo.tar.gz | Display response in browser 

### Status codes {#get-all-status-codes} 

| Code | Description |
|------|-------------|
| [200 OK](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) | Success. |
| [500 Internal Server Error](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) | Failed to get debug info. |
