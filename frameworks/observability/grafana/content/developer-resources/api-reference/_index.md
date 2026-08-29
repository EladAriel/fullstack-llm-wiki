---
type: "Framework Learn Page"
framework: "Grafana"
source_repo: "https://github.com/grafana/grafana.git"
source_branch: "main"
source_path: "docs/sources/developer-resources/api-reference/_index.md"
source_commit: "5e3a02f81d2aadf4bf24fe49ed97d872556f5bf9"
source_commit_short: "5e3a02f8"
source_commit_date: "2026-08-29T10:58:19+09:00"
generated_at: "2026-08-29T09:39:37.543905Z"
---
---
keywords:
  - grafana
  - documentation
  - developers
  - resources
  - data model
title: Grafana APIs
weight: 300
cards:
  items:
    - title: HTTP API
      height: 24
      href: ./http-api/
      description: Every Grafana instance exposes an HTTP API, used by the Grafana frontend to manage resources like saving dashboards, creating users, updating data sources, deleting alerts, and more. You can use the HTTP API to programmatically access or manage resources from your Grafana instance.
    - title: Grafana Cloud API
      height: 24
      href: ./cloud-api/
      description: The Grafana Cloud API, also known as the Grafana.com API or GCOM API, allows you to interact with resources from your Grafana Cloud Stack programmatically.
    - title: Tracing API
      height: 24
      href: ./tracing-api/
      description: Tempo exposes an API for pushing and querying traces, and operating the cluster itself.
    - title: Synthetic Monitoring API
      height: 24
      href: ./synthetic-monitoring-api/
      description: The Grafana Cloud Synthetic Monitoring REST API provides programmatic access to Synthetic Monitoring resources.
---

# Grafana APIs

Refer to the following API reference guides:

{{< card-grid key="cards" type="simple" >}}
