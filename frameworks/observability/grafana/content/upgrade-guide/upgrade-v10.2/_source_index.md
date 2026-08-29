---
type: "Framework Learn Page"
framework: "Grafana"
source_repo: "https://github.com/grafana/grafana.git"
source_branch: "main"
source_path: "docs/sources/upgrade-guide/upgrade-v10.2/index.md"
source_commit: "5e3a02f81d2aadf4bf24fe49ed97d872556f5bf9"
source_commit_short: "5e3a02f8"
source_commit_date: "2026-08-29T10:58:19+09:00"
generated_at: "2026-08-29T09:39:37.426678Z"
---
---
description: Upgrade to Grafana v10.2
keywords:
  - grafana
  - configuration
  - documentation
  - upgrade
title: Upgrade to Grafana v10.2
menuTitle: Upgrade to v10.2
weight: 1500
---

# Upgrade to Grafana v10.2

{{< docs/shared lookup="upgrade/intro.md" source="grafana" version="<GRAFANA VERSION>" >}}

{{< docs/shared lookup="back-up/back-up-grafana.md" source="grafana" version="<GRAFANA VERSION>" leveloffset="+1" >}}

{{< docs/shared lookup="upgrade/upgrade-common-tasks.md" source="grafana" version="<GRAFANA VERSION>" >}}

## Technical notes

- From Grafana v10.2 onwards, `/api/datasources/:id/` is removed and replaced with `/api/access-control/datasources/:uid`. For more information about the new API endpoints for the data source permission API, refer to the [documentation](https://grafana.com/docs/grafana/<GRAFANA_VERSION>/developers/http_api/datasource_permissions/).
