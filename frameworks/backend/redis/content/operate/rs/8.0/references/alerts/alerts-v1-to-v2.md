---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/8.0/references/alerts/alerts-v1-to-v2.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.655153Z"
---
# Alerts V1 To V2

---
Title: Transition cluster manager alerts to Prometheus alerts
alwaysopen: false
categories:
- docs
- operate
- rs
description: Transition from internal cluster manager alerts to external monitoring alerts using Prometheus.
linkTitle: Transition cluster manager alerts to Prometheus
weight: 50
url: '/operate/rs/8.0/references/alerts/alerts-v1-to-v2/'
---

As Redis Software transitions from the [deprecated monitoring system]({{<relref "/operate/rs/8.0/monitoring/v1_monitoring">}}) to the [new metrics stream engine]({{<relref "/operate/rs/8.0/monitoring/metrics_stream_engine">}}), some internal cluster manager alerts were deprecated in favor of external monitoring solutions.

You can use the following table to transition from the deprecated alerts and set up equivalent alerts in Prometheus with [PromQL (Prometheus Query Language)](https://prometheus.io/docs/prometheus/latest/querying/basics/):

{{<embed-md "rs-alerts-transition-plan.md">}}