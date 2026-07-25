---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/8.0/references/rest-api/requests/cluster/certificates/rotate.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Rotate cluster certificates requests
alwaysopen: false
categories:
- docs
- operate
- rs
description: Rotate cluster certificates requests
headerRange: '[1-2]'
linkTitle: rotate
weight: $weight
url: '/operate/rs/8.0/references/rest-api/requests/cluster/certificates/rotate/'
---

| Method | Path | Description |
|--------|------|-------------|
| [POST](#post-cluster-certificates-rotate) | `/v1/cluster/certificates/rotate` | Regenerate all internal cluster certificates |

## Rotate cluster certificates {#post-cluster-certificates-rotate}

	POST /v1/cluster/certificates/rotate

Regenerates all _internal_ cluster certificates.

The certificate rotation will be performed on all nodes within the cluster. If
"name" is provided, only rotate the specified certificate on all nodes within the cluster.

### Request {#post-request} 

#### Example HTTP request

	POST /v1/cluster/certificates/rotate

#### Request headers

| Key | Value | Description |
|-----|-------|-------------|
| Host | cnm.cluster.fqdn | Domain name |
| Accept | application/json | Accepted media type |

### Response {#post-response} 

Responds with a `200 OK` status code if the internal certificates successfully rotate across the entire cluster.

### Status codes {#post-status-codes} 

| Code | Description |
|------|-------------|
| [200 OK](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) | No error |
| [400 Bad Request](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) | Failed, not all nodes have been updated. |
| [403 Forbidden](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) | Unsupported internal certificate rotation. |
