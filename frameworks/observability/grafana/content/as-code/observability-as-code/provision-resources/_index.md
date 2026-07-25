---
type: "Framework Learn Page"
framework: "Grafana"
source_repo: "https://github.com/grafana/grafana.git"
source_branch: "main"
source_path: "docs/sources/as-code/observability-as-code/provision-resources/_index.md"
source_commit: "d18e58d33aa8741f08fbab4aa73bdaf1f04e3be5"
source_commit_short: "d18e58d3"
source_commit_date: "2026-07-25T13:50:43+02:00"
generated_at: "2026-07-25T19:08:09.057468Z"
---
---
description: Learn about how to provision resources using local file provisioning administration.
keywords:
  - observability
  - configuration
  - as code
labels:
  products:
    - enterprise
    - oss
title: Provision resources on-prem
menuTitle: On-prem file provisioning
weight: 400
canonical: https://grafana.com/docs/grafana/latest/as-code/observability-as-code/provision-resources/
aliases:
  - ../../observability-as-code/provision-resources/ # /docs/grafana/next/observability-as-code/provision-resources/
---

# On-prem file provisioning

{{< admonition type="note" >}}

On-prem file provisioning is available in Grafana v12 and later for open source and Enterprise editions. It's **not available in Grafana Cloud**. This new file provisioning feature is only available for dashboards and doesn't replace classic provisioning for the time being.

For classic provisioning using configuration files refer to [Provision Grafana](https://grafana.com/docs/grafana/<GRAFANA_VERSION>/administration/provisioning/).

{{< /admonition >}}

On-prem local file provisioning allows you to add resources that are stored in your local file system to your Grafana instance. You can
configure how to save your dashboards' JSON and other files from your local file system into a single or multiple folders in a different repository, with up to 10 connections.

To set it up, refer to [Set up file provisioning](https://grafana.com/docs/grafana/<GRAFANA_VERSION>/as-code/observability-as-code/provision-resources/file-path-setup).

## How it works

On-prem file provisioning is only available for dashboards at the moment.

After setting up file provisioning:

- The dashboards saved in your GitHub repository or local folder appear in Grafana in the `provisioned` folder.
- The dashboards and folders saved to the local path are referred to as `provisioned` resources and are labeled as such in the Grafana UI.

You can only modify provisioned dashboards locally.

- Any changes made in the provisioned files are reflected in the Grafana database. The Grafana UI reads the database and updates the UI to reflect these changes.
- You can't use the Grafana UI to edit or delete provisioned resources.
