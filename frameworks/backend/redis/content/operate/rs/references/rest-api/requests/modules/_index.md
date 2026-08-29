---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/rest-api/requests/modules/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.589562Z"
---
# _Index

---
Title: Modules requests
alwaysopen: false
categories:
- docs
- operate
- rs
description: Redis modules requests
headerRange: '[1-2]'
hideListLinks: true
linkTitle: modules
weight: $weight
---

| Method | Path | Description |
|--------|------|-------------|
| [GET](#list-modules) | `/v1/modules` | List available modules |
| [GET](#get-module) | `/v1/modules/{uid}` | Get a specific module |

## List modules {#list-modules}

```sh
GET /v1/modules
```

List available modules, i.e. modules stored within the CCS.

#### Permissions

| Permission name | Roles |
|-----------------|-------|
| [view_cluster_modules]({{< relref "/operate/rs/references/rest-api/permissions#view_cluster_modules" >}}) | admin<br />cluster_member<br />cluster_viewer<br />db_member<br />db_viewer<br />user_manager |

### Request {#list-request}

#### Example HTTP request

```sh
GET /v1/modules
```

#### Headers

| Key | Value | Description |
|-----|-------|-------------|
| Host | 127.0.0.1:9443 | Domain name |
| Accept | \*/\* | Accepted media type |

### Response {#list-response}

Returns a JSON array of [module objects]({{< relref "/operate/rs/references/rest-api/objects/module" >}}).

#### Status codes {#list-status-codes}

| Code | Description |
|------|-------------|
| [200 OK](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) | No error |

## Get module {#get-module}

```sh
GET /v1/modules/{string: uid}
```

Get specific available modules, i.e. modules stored within the CCS.

#### Permissions

| Permission name | Roles |
|-----------------|-------|
| [view_cluster_modules]({{< relref "/operate/rs/references/rest-api/permissions#view_cluster_modules" >}}) | admin<br />cluster_member<br />cluster_viewer<br />db_member<br />db_viewer<br />user_manager |

### Request {#get-request}

#### Example HTTP request

```sh
GET /v1/modules/1
```

#### Headers

| Key | Value | Description |
|-----|-------|-------------|
| Host | 127.0.0.1:9443 | Domain name |
| Accept | \*/\* | Accepted media type |

#### URL parameters

| Field | Type | Description |
|-------|------|-------------|
| uid | integer | The module's unique ID. |

### Response {#get-response}

Returns a [module object]({{< relref "/operate/rs/references/rest-api/objects/module" >}}).

### Status codes {#get-status-codes}

| Code | Description |
|------|-------------|
| [200 OK](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) | No error |
| [404 Not Found](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.5) | Module does not exist. |
