---
type: "Framework Learn Page"
framework: "Grafana"
source_repo: "https://github.com/grafana/grafana.git"
source_branch: "main"
source_path: "docs/sources/developer-resources/api-reference/http-api/api-legacy/dashboard_versions.md"
source_commit: "5e3a02f81d2aadf4bf24fe49ed97d872556f5bf9"
source_commit_short: "5e3a02f8"
source_commit_date: "2026-08-29T10:58:19+09:00"
generated_at: "2026-08-29T09:39:37.553785Z"
---
---
aliases:
  - ../../../../http_api/dashboard_versions/ # /docs/grafana/next/http_api/dashboard_versions/
  - ../../../../http_api/dashboardversions/ # /docs/grafana/next/http_api/dashboardversions/
  - ../../../../developers/http_api/dashboard_versions/ # /docs/grafana/next/developers/http_api/dashboard_versions/
  - ../../../../developer-resources/api-reference/http-api/dashboard_versions/ #legacy folder
canonical: https://grafana.com/docs/grafana/latest/developer-resources/api-reference/http-api/api-legacy/dashboard_versions/
description: Grafana Dashboard Versions HTTP API
keywords:
  - grafana
  - http
  - documentation
  - api
  - dashboard
  - versions
labels:
  products:
    - enterprise
    - oss
    - cloud
title: 'Dashboard Versions HTTP API '
---

# Dashboard Versions

{{< docs/shared lookup="developers/deprecated-apis.md" source="grafana" version="<GRAFANA_VERSION>" >}}

## Get all dashboard versions by dashboard UID

Query parameters:

- **limit** - Maximum number of results to return. Defaults to 1000 if not set, or if an invalid value is passed in.
- **start** - Version to start from when returning queries

`GET /api/dashboards/uid/:uid/versions`

Gets all existing dashboard versions for the dashboard with the given `uid`.

**Example request for getting all dashboard versions**:

```http
GET /api/dashboards/uid/QA7wKklGz/versions?limit=2?start=0 HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer <SERVICE_ACCOUNT_TOKEN>
```

**Example Response**

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
Content-Length: 428

{
  "continueToken": "",
  "versions": [
    {
      "id": 2,
      "dashboardId": 1,
      "uid": "QA7wKklGz",
      "parentVersion": 1,
      "restoredFrom": 0,
      "version": 2,
      "created": "2017-06-08T17:24:33-04:00",
      "createdBy": "admin",
      "message": "Updated panel title"
    },
    {
      "id": 1,
      "dashboardId": 1,
      "uid": "QA7wKklGz",
      "parentVersion": 0,
      "restoredFrom": 0,
      "version": 1,
      "created": "2017-06-08T17:23:33-04:00",
      "createdBy": "admin",
      "message": "Initial save"
    }
  ]
}
```

Status Codes:

- **200** - Ok
- **400** - Errors
- **401** - Unauthorized
- **404** - Dashboard version not found

## Get dashboard version by dashboard UID

`GET /api/dashboards/uid/:uid/versions/:version`

Get the dashboard version with the given version, for the dashboard with the given UID.

**Example request for getting a dashboard version**:

```http
GET /api/dashboards/uid/QA7wKklGz/versions/1 HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer <SERVICE_ACCOUNT_TOKEN>
```

**Example response**:

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
Content-Length: 1300

{
  "id": 1,
  "dashboardId": 1,
  "uid": "QA7wKklGz",
  "parentVersion": 0,
  "restoredFrom": 0,
  "version": 1,
  "created": "2017-04-26T17:18:38-04:00",
  "message": "Initial save",
  "data": {
    "annotations": {
      "list": [

      ]
    },
    "editable": true,
    "gnetId": null,
    "graphTooltip": 0,
    "id": 1,
    "links": [

    ],
    "rows": [
      {
        "collapse": false,
        "height": "250px",
        "panels": [

        ],
        "repeat": null,
        "repeatIteration": null,
        "repeatRowId": null,
        "showTitle": false,
        "title": "Dashboard Row",
        "titleSize": "h6"
      }
    ],
    "schemaVersion": 14,
      "tags": [

    ],
    "templating": {
      "list": [

      ]
    },
    "time": {
      "from": "now-6h",
      "to": "now"
    },
    "timepicker": {},
    "timezone": "browser",
    "title": "test",
    "version": 1
  },
  "createdBy": "admin"
}
```

Status Codes:

- **200** - Ok
- **401** - Unauthorized
- **404** - Dashboard version not found
