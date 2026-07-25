---
type: "Framework Learn Page"
framework: "Grafana"
source_repo: "https://github.com/grafana/grafana.git"
source_branch: "main"
source_path: "docs/sources/alerting/monitor-status/alerts-page.md"
source_commit: "d18e58d33aa8741f08fbab4aa73bdaf1f04e3be5"
source_commit_short: "d18e58d3"
source_commit_date: "2026-07-25T13:50:43+02:00"
generated_at: "2026-07-25T19:08:08.942649Z"
---
---
canonical: https://grafana.com/docs/grafana/latest/alerting/monitor-status/alerts-page/
title: Alerts overview page
description: Use the Alert page to assess, prioritize, and take action on alerts quickly in Grafana Cloud.
weight: 405
keywords:
  - Grafana Cloud
  - alerting
  - triage
  - incidents
  - monitoring
  - Grafana-managed alerts
labels:
  products:
    - cloud
    - enterprise
    - oss
---

{{< docs/public-preview product="Alerts page" >}}

# Alert view

Grafana Alerting provides a consolidated snapshot of your firing and pending Grafana-managed alerts in a simplified view. For users with complex deployments, it can be difficult to monitor and prioritize critical incidents among a large volume of firing or pending alerts. With the Alert page, you have a view where you can quickly explore and sort your recent alert history and see what alerts require review or action.

To see your firing and pending alerts in the alert page, go to **Alerts & IRM** > **Alerting** > **Alert activity**.

{{< figure src="/media/docs/alerting/alerts-page.png" max-width="750px" alt="Filter your firing and pending alerts in the Alert view." >}}

## How it works

The Alerts page only shows alerts from Grafana-managed alert rules. Grafana uses a metric called `GRAFANA_ALERTS`, which is recorded in the default Mimir data source that is provisioned for cloud users.

{{< admonition type="note" >}}
OSS users need to manually configure this. To configure alert state history for OSS, refer to the <a href="https://grafana.com/docs/grafana/latest/alerting/set-up/configure-alert-state-history/#configure-loki-and-prometheus-for-alert-state">configure Loki and Prometheus for alert state</a> documentation.
{{< /admonition >}}

## Filter alerts in the Alerts page

The page displays the count of alert rules and instances that are both firing and pending. Use the filters to group your alerts and find specific alerts by label.

To group alerts by label, click the **Group by** field and select the labels from the dropdown menu. You can select multiple labels for alert grouping.

To filter by specific label values, click the **Filters** field and select a label to filter by, followed by an expression of what label value you want to use. You can enter multiple label values in your search.

You can also select a time range from the time picker to further adjust your results. Click the **time range** field and enter an absolute time range or select a period from the quick ranges list to apply a new time window to the display results.
