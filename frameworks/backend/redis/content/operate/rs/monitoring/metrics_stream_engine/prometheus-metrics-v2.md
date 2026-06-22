---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/monitoring/metrics_stream_engine/prometheus-metrics-v2.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Prometheus metrics v2
alwaysopen: false
categories:
- docs
- integrate
- rs
description: V2 metrics available to Prometheus as of Redis Software version 7.8.2.
group: observability
linkTitle: Prometheus metrics v2
summary: V2 metrics available to Prometheus as of Redis Software version 7.8.2.
type: integration
weight: 50
tocEmbedHeaders: true
---

You can integrate Redis Software with Prometheus and tools such as [Grafana]({{<relref "/integrate/prometheus-with-redis-enterprise">}}), [Datadog]({{<relref "/integrate/datadog-with-redis-enterprise">}}), [Dynatrace]({{<relref "/integrate/dynatrace-with-redis-enterprise">}}), or [New Relic]({{<relref "/integrate/new-relic-with-redis-enterprise">}}) to create dashboards for important metrics.

The v2 metrics in the following tables are available as of Redis Software version 7.8.0. For help transitioning from v1 metrics to v2 PromQL, see [Prometheus v1 metrics and equivalent v2 PromQL]({{<relref "/operate/rs/monitoring/metrics_stream_engine/prometheus-metrics-v1-to-v2">}}).

The v2 scraping endpoint also exposes metrics for `node_exporter` version 1.8.1. For more information, see the [Prometheus node_exporter GitHub repository](https://github.com/prometheus/node_exporter).

{{<embed-md "rs-prometheus-metrics-v2.md">}}
