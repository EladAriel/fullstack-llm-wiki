---
type: "Framework Learn Page"
framework: "Grafana"
source_repo: "https://github.com/grafana/grafana.git"
source_branch: "main"
source_path: "docs/sources/alerting/monitor-status/_index.md"
source_commit: "d18e58d33aa8741f08fbab4aa73bdaf1f04e3be5"
source_commit_short: "d18e58d3"
source_commit_date: "2026-07-25T13:50:43+02:00"
generated_at: "2026-07-25T19:08:08.943031Z"
---
---
aliases:
  - ./manage-notifications/ # /docs/grafana/<GRAFANA_VERSION>/alerting/manage-notifications/
canonical: https://grafana.com/docs/grafana/latest/alerting/monitor-status/
description: Detect and respond for day-to-day triage and analysis of what’s going on and action you need to take
keywords:
  - grafana
  - detect
  - respond
labels:
  products:
    - cloud
    - enterprise
    - oss
title: Monitor alerts
weight: 130
refs:
  configure-alert-rules:
    - pattern: /docs/grafana/
      destination: /docs/grafana/<GRAFANA_VERSION>/alerting/alerting-rules/
    - pattern: /docs/grafana-cloud/
      destination: /docs/grafana-cloud/alerting-and-irm/alerting/alerting-rules/
  configure-notifications:
    - pattern: /docs/grafana/
      destination: /docs/grafana/<GRAFANA_VERSION>/alerting/configure-notifications/
    - pattern: /docs/grafana-cloud/
      destination: /docs/grafana-cloud/alerting-and-irm/alerting/configure-notifications/
---

# Monitor alerts

Alerts and alert notifications should provide key information to help alert responders and incident participants understand what happened in their system and how to respond.

Grafana Alerting offers the ability to monitor your alerts and manage your alerting setup. You can get an overview of your alerts, track the history of alert states, and monitor notification statuses. These can help you start investigating alert issues within Grafana and improve the reliability of your alerting implementation.

{{< figure src="/media/docs/alerting/alert-history-page.png" max-width="750px" alt="History page in Grafana Alerting" >}}

The previous sections explain how to [configure alert rules](ref:configure-alert-rules) and [configure notifications](ref:configure-notifications) to generate alerts and send their notifications.

This section focuses on finding and understanding the state of your alert rules, alert instances, and their notifications. For more details, refer to:

{{< section >}}
