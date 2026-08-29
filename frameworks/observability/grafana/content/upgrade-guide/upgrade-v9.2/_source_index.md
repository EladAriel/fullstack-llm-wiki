---
type: "Framework Learn Page"
framework: "Grafana"
source_repo: "https://github.com/grafana/grafana.git"
source_branch: "main"
source_path: "docs/sources/upgrade-guide/upgrade-v9.2/index.md"
source_commit: "5e3a02f81d2aadf4bf24fe49ed97d872556f5bf9"
source_commit_short: "5e3a02f8"
source_commit_date: "2026-08-29T10:58:19+09:00"
generated_at: "2026-08-29T09:39:37.428878Z"
---
---
description: Upgrade to Grafana v9.2
keywords:
  - grafana
  - configuration
  - documentation
  - upgrade
labels:
  products:
    - enterprise
    - oss
menutitle: Upgrade to v9.2
title: Upgrade to Grafana v9.2
weight: 2100
---

# Upgrade to Grafana v9.2

{{< docs/shared lookup="upgrade/intro.md" source="grafana" version="<GRAFANA VERSION>" >}}

{{< docs/shared lookup="back-up/back-up-grafana.md" source="grafana" version="<GRAFANA VERSION>" leveloffset="+1" >}}

{{< docs/shared lookup="upgrade/upgrade-common-tasks.md" source="grafana" version="<GRAFANA VERSION>" >}}

## Technical notes

Beginning in v9.2, Grafana has a [supported database versions policy](../../setup-grafana/installation/#supported-databases). As of this release, MySQL versions from 5.7, postgres versions from v10, and SQLite 3 are supported databases.
