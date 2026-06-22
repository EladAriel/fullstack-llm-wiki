---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/alerts/alerts-v1-to-v2.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

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
---

As Redis Software transitions from the [deprecated monitoring system]({{<relref "/operate/rs/monitoring/v1_monitoring">}}) to the [new metrics stream engine]({{<relref "/operate/rs/monitoring/metrics_stream_engine">}}), some internal cluster manager alerts were deprecated in favor of external monitoring solutions.

You can use the following table to transition from the deprecated alerts and set up equivalent alerts in Prometheus with [PromQL (Prometheus Query Language)](https://prometheus.io/docs/prometheus/latest/querying/basics/):

{{<embed-md "rs-alerts-transition-plan.md">}}