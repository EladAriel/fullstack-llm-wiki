---
type: "Framework Learn Page"
framework: "Grafana"
source_repo: "https://github.com/grafana/grafana.git"
source_branch: "main"
source_path: "docs/sources/upgrade-guide/upgrade-v10.4/index.md"
source_commit: "5e3a02f81d2aadf4bf24fe49ed97d872556f5bf9"
source_commit_short: "5e3a02f8"
source_commit_date: "2026-08-29T10:58:19+09:00"
generated_at: "2026-08-29T09:39:37.432400Z"
---
---
description: Guide for upgrading to Grafana v10.4
keywords:
  - grafana
  - configuration
  - documentation
  - upgrade
  - '10.4'
title: Upgrade to Grafana v10.4
menuTitle: Upgrade to v10.4
weight: 1300
---

# Upgrade to Grafana v10.4

{{< docs/shared lookup="upgrade/intro.md" source="grafana" version="<GRAFANA VERSION>" >}}

{{< docs/shared lookup="back-up/back-up-grafana.md" source="grafana" version="<GRAFANA VERSION>" leveloffset="+1" >}}

{{< docs/shared lookup="upgrade/upgrade-common-tasks.md" source="grafana" version="<GRAFANA VERSION>" >}}

## Technical notes

### Legacy alerting -> Grafana Alerting dry-run on start

If you haven't already upgraded to Grafana Alerting from legacy Alerting, Grafana will initiate a dry-run of the upgrade every time the instance starts. This is in preparation for the removal of legacy Alerting in Grafana v11. The dry-run logs the results of the upgrade attempt and identifies any issues requiring attention before you can successfully execute the upgrade. No changes are made during the dry-run.

You can disable this behavior using the feature flag `alertingUpgradeDryrunOnStart`:

```toml
[feature_toggles]
alertingUpgradeDryrunOnStart=false
```

{{< admonition type="note" >}}
We strongly encourage you to review the [upgrade guide](https://grafana.com/docs/grafana/v10.4/alerting/set-up/migrating-alerts/) and perform the necessary upgrade steps prior to v11.
{{< /admonition >}}
