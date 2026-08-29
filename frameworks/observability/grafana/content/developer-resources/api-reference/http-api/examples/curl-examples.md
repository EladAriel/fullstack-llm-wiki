---
type: "Framework Learn Page"
framework: "Grafana"
source_repo: "https://github.com/grafana/grafana.git"
source_branch: "main"
source_path: "docs/sources/developer-resources/api-reference/http-api/examples/curl-examples.md"
source_commit: "5e3a02f81d2aadf4bf24fe49ed97d872556f5bf9"
source_commit_short: "5e3a02f8"
source_commit_date: "2026-08-29T10:58:19+09:00"
generated_at: "2026-08-29T09:39:37.548162Z"
---
---
aliases:
  - ../../../../http_api/curl-examples/ # /docs/grafana/next/http_api/curl-examples/
  - ../../../../developers/http_api/curl-examples/ # /docs/grafana/next/developers/http_api/curl-examples/
  - ../../../../developers/http_api/examples/curl-examples/ # /docs/grafana/next/developers/http_api/examples/curl-examples/
canonical: https://grafana.com/docs/grafana/latest/developer-resources/api-reference/http-api/examples/curl-examples/
description: cURL examples
keywords:
  - grafana
  - http
  - documentation
  - api
  - curl
labels:
  products:
    - enterprise
    - oss
title: cURL examples
---

# cURL examples

This page provides examples of calls to the Grafana API using cURL.

The most basic example for a dashboard for which there is no authentication. You can test the following on your local machine, assuming a default installation and anonymous access enabled, required:

```
curl http://localhost:3000/api/search
```

Here's a cURL command that works for getting the home dashboard when you are running Grafana locally with [basic authentication](/docs/grafana/<GRAFANA_VERSION>/setup-grafana/configure-access/configure-authentication/#basic-auth) enabled using the default admin credentials:

```
curl http://admin:admin@localhost:3000/api/search
```

To pass a username and password with [HTTP basic authorization](/docs/grafana/<GRAFANA_VERSION>/administration/roles-and-permissions/access-control/manage-rbac-roles/), encode them as base64.
You can't use authorization tokens in the request.

For example, to [list permissions associated with roles](/docs/grafana/<GRAFANA_VERSION>/administration/roles-and-permissions/access-control/manage-rbac-roles/) given a username of `user` and password of `password`, use:

```
curl --location '<grafana_url>/api/access-control/builtin-roles' --user 'user:password'
```
