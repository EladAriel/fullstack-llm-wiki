---
type: "Framework Learn Page"
framework: "Grafana"
source_repo: "https://github.com/grafana/grafana.git"
source_branch: "main"
source_path: "docs/sources/developer-resources/api-reference/http-api/api-legacy/preferences.md"
source_commit: "d18e58d33aa8741f08fbab4aa73bdaf1f04e3be5"
source_commit_short: "d18e58d3"
source_commit_date: "2026-07-25T13:50:43+02:00"
generated_at: "2026-07-25T19:08:09.006596Z"
---
---
aliases:
  - ../../../../http_api/preferences/ # /docs/grafana/next/http_api/preferences/
  - ../../../../developers/http_api/preferences/ # /docs/grafana/next/developers/http_api/preferences/
  - ../../../../developer-resources/api-reference/http-api/preferences/ #legacy folder
canonical: https://grafana.com/docs/grafana/latest/developer-resources/api-reference/http-api/api-legacy/preferences/
description: Grafana HTTP API
keywords:
  - grafana
  - http
  - documentation
  - api
  - preferences
labels:
  products:
    - enterprise
    - oss
    - cloud
title: 'Preferences API'
---

# User and Org Preferences API

{{< docs/shared lookup="developers/deprecated-apis.md" source="grafana" version="<GRAFANA_VERSION>" >}}

Keys:

- **theme** - One of: `light`, `dark`, or an empty string for the default theme
- **homeDashboardId** - Deprecated. Use `homeDashboardUID` instead.
- **homeDashboardUID**: The `:uid` of a dashboard
- **timezone** - Any valid IANA timezone string (e.g., `America/New_York`, `Europe/London`), `utc`, `browser`, or an empty string for the default.

Omitting a key will cause the current value to be replaced with the
system default value.

## Get Current User Prefs

`GET /api/user/preferences`

**Example Request**:

```http
GET /api/user/preferences HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer <SERVICE_ACCOUNT_TOKEN>
```

**Example Response**:

```http
HTTP/1.1 200
Content-Type: application/json

{
    "theme": "",
    "homeDashboardId": 217,
    "homeDashboardUID": "jcIIG-07z",
    "timezone": "utc",
    "weekStart": "",
    "navbar": {
        "bookmarkUrls": null
    },
    "queryHistory": {
        "homeTab": ""
    }
}
```

## Update Current User Prefs

`PUT /api/user/preferences`

**Example Request**:

```http
PUT /api/user/preferences HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer <SERVICE_ACCOUNT_TOKEN>

{
  "theme": "",
  "homeDashboardUID":"home",
  "timezone":"utc"
}
```

**Example Response**:

```http
HTTP/1.1 200
Content-Type: text/plain; charset=utf-8

{"message":"Preferences updated"}
```

## Patch Current User Prefs

Update one or more preferences without modifying the others.

`PATCH /api/user/preferences`

**Example Request**:

```http
PATCH /api/user/preferences HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer <SERVICE_ACCOUNT_TOKEN>

{
  "theme": "dark"
}
```

**Example Response**:

```http
HTTP/1.1 200
Content-Type: text/plain; charset=utf-8

{"message":"Preferences updated"}
```

## Get Current Org Prefs

`GET /api/org/preferences`

**Example Request**:

```http
GET /api/org/preferences HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer <SERVICE_ACCOUNT_TOKEN>
```

**Example Response**:

```http
HTTP/1.1 200
Content-Type: application/json

{
    "theme": "",
    "homeDashboardId": 0,
    "homeDashboardUID": "",
    "timezone": "",
    "weekStart": "",
    "navbar": {
        "bookmarkUrls": null
    },
    "queryHistory": {
        "homeTab": ""
    }
}
```

## Update Current Org Prefs

`PUT /api/org/preferences`

**Example Request**:

```http
PUT /api/org/preferences HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer <SERVICE_ACCOUNT_TOKEN>

{
  "theme": "",
  "homeDashboardUID":"home",
  "timezone":"utc"
}
```

**Example Response**:

```http
HTTP/1.1 200
Content-Type: text/plain; charset=utf-8

{"message":"Preferences updated"}
```

## Patch Current Org Prefs

Update one or more preferences without modifying the others.

`PATCH /api/org/preferences`

**Example Request**:

```http
PATCH /api/org/preferences HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer <SERVICE_ACCOUNT_TOKEN>

{
  "theme": "dark"
}
```

**Example Response**:

```http
HTTP/1.1 200
Content-Type: text/plain; charset=utf-8

{"message":"Preferences updated"}
```
