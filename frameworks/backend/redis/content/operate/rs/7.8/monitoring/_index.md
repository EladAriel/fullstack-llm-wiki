---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/monitoring/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Monitoring with metrics and alerts
alwaysopen: false
categories:
- docs
- operate
- rs
- kubernetes
description: Use the metrics that measure the performance of your Redis Enterprise Software clusters, nodes, databases, and shards to track the performance of your databases.
hideListLinks: true
linkTitle: Monitoring
weight: 70
url: '/operate/rs/7.8/monitoring/'
---

You can use the metrics that measure the performance of your Redis Enterprise Software clusters, nodes, databases, and shards
to monitor the performance of your databases.

## View metrics and configure alerts

In the Redis Enterprise Cluster Manager UI, you can view metrics, configure alerts, and send notifications based on alert parameters. You can also access metrics and configure alerts through the REST API.

See [Metrics and alerts for monitoring v1]({{<relref "/operate/rs/7.8/monitoring/v1_monitoring">}}) for more information.

## Metrics stream engine preview

A preview of the new metrics stream engine is available as of [Redis Enterprise Software version 7.8.2](https://redis.io/docs/latest/operate/rs/release-notes/rs-7-8-releases). This new engine exposes the v2 Prometheus scraping endpoint at `https://<IP>:8070/v2`, exports all time-series metrics to external monitoring tools, and enables real-time monitoring.

See [Metrics stream engine preview for monitoring v2]({{<relref "/operate/rs/7.8/monitoring/metrics_stream_engine">}}) for more information.

## Integrate with external monitoring tools

To integrate Redis Enterprise metrics into your monitoring environment, see the integration guides for [Prometheus and Grafana]({{< relref "/operate/rs/7.8/monitoring/prometheus_and_grafana" >}}).

Filter [Libraries and tools]({{<relref "/integrate">}}) by "observability" for additional tools and guides.

## Metrics reference

Make sure you read the [definition of each metric]({{< relref "/operate/rs/7.8/references/metrics/" >}})
so that you understand exactly what it represents.
