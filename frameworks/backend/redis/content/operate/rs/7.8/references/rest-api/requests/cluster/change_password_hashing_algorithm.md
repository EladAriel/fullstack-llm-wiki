---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/rest-api/requests/cluster/change_password_hashing_algorithm.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Change password hashing algorithm requests
alwaysopen: false
categories:
- docs
- operate
- rs
description: REST API requests to change the hashing algorithm for user passwords.
headerRange: '[1-2]'
linkTitle: change_password_hashing_algorithm
weight: $weight
url: '/operate/rs/7.8/references/rest-api/requests/cluster/change_password_hashing_algorithm/'
---

| Method | Path | Description |
|--------|------|-------------|
| [PATCH](#patch-change-password-hashing-algorithm) | `/v1/cluster/change_password_hashing_algorithm` | Change the hashing policy for user passwords |

## Change password hashing algorithm {#patch-change-password-hashing-algorithm}

	PATCH /v1/cluster/change_password_hashing_algorithm

Changes the password hashing algorithm for the entire cluster. When you change the hashing algorithm, it rehashes the administrator password and passwords for all users, including default users.

The hashing algorithm options are `SHA-256` or `PBKDF2`. The default hashing algorithm is `SHA-256`.

#### Required permissions

| Permission name |
|-----------------|
| [update_cluster]({{< relref "/operate/rs/7.8/references/rest-api/permissions#update_cluster" >}}) |

### Request {#patch-request} 

#### Example HTTP request

	PATCH /v1/cluster/change_password_hashing_algorithm

#### Example JSON body

```json
{ "algorithm": "PBKDF2" }
```

#### Request headers

| Key | Value | Description |
|-----|-------|-------------|
| Host | cnm.cluster.fqdn | Domain name |
| Accept | application/json | Accepted media type |

#### Request body

Include a JSON object `{ "algorithm": "<option>" }` in the request body. The hashing algorithm options are `SHA-256` or `PBKDF2`.

### Response {#patch-response} 

Returns a status code that indicates the success or failure of the update.

### Status codes {#patch-status-codes} 

| Code | Description |
|------|-------------|
| [200 OK](https://www.rfc-editor.org/rfc/rfc9110.html#name-200-ok) | Success |
| [400 Bad Request](https://www.rfc-editor.org/rfc/rfc9110.html#name-400-bad-request) | Supported algorithm must be provided, or this algorithm is already set |
