---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/metrics/prometheus-metrics-v1.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Prometheus metrics v1
alwaysopen: false
categories:
- docs
- integrate
- rs
description: V1 metrics available to Prometheus.
group: observability
linkTitle: Prometheus metrics v1
summary: You can use Prometheus and Grafana to collect and visualize your Redis Enterprise Software metrics.
type: integration
weight: 48
tocEmbedHeaders: true
url: '/operate/rs/7.8/references/metrics/prometheus-metrics-v1/'
---

You can [integrate Redis Enterprise Software with Prometheus and Grafana]({{<relref "/operate/rs/7.8/monitoring/prometheus_and_grafana">}}) to create dashboards for important metrics.

As of Redis Enterprise Software version 7.8.2, v1 metrics are deprecated but still available. For help transitioning from v1 metrics to v2 PromQL, see [Prometheus v1 metrics and equivalent v2 PromQL]({{<relref "/operate/rs/7.8/references/metrics/prometheus-metrics-v1-to-v2">}}).

{{<embed-md "rs-prometheus-metrics-v1.md">}}
