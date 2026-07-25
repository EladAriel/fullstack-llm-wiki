---
type: "Framework Learn Page"
framework: "Grafana"
source_repo: "https://github.com/grafana/grafana.git"
source_branch: "main"
source_path: "docs/sources/developer-resources/api-reference/http-api/api-legacy/short_url.md"
source_commit: "d18e58d33aa8741f08fbab4aa73bdaf1f04e3be5"
source_commit_short: "d18e58d3"
source_commit_date: "2026-07-25T13:50:43+02:00"
generated_at: "2026-07-25T19:08:09.005824Z"
---
---
aliases:
  - ../../../../http_api/short_url/ # /docs/grafana/next/http_api/short_url/
  - ../../../../developers/http_api/short_url/ # /docs/grafana/next/developers/http_api/short_url/
  - ../../../../developer-resources/api-reference/http-api/short_url/ #legacy folder
canonical: https://grafana.com/docs/grafana/latest/developer-resources/api-reference/http-api/api-legacy/short_url/
description: Grafana Short URL HTTP API
keywords:
  - grafana
  - http
  - documentation
  - api
  - shortUrl
labels:
  products:
    - enterprise
    - oss
    - cloud
title: 'Short URL HTTP API '
---

# Short URL API

{{< docs/shared lookup="developers/deprecated-apis.md" source="grafana" version="<GRAFANA_VERSION>" >}}

Use this API to create shortened URLs. A short URL represents a longer URL containing complex query parameters in a smaller and simpler format.

## Create short URL

`POST /api/short-urls`

Creates a short URL.

**Example request:**

```http
POST /api/short-urls HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer <SERVICE_ACCOUNT_TOKEN>

{
  "path": "d/TxKARsmGz/new-dashboard?orgId=1&from=1599389322894&to=1599410922894"
}
```

JSON body schema:

- **path** – The path to shorten, relative to the Grafana [root_url](/docs/grafana/latest/setup-grafana/configure-grafana/#root_url).

**Example response:**

```http
HTTP/1.1 200
Content-Type: application/json

{
  "uid": AT76wBvGk,
  "url": http://localhost:3000/goto/AT76wBvGk?orgId=1
}

```

Status codes:

- **200** – Created
- **400** – Errors (invalid JSON, missing or invalid fields)
