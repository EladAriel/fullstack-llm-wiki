---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/8.0/monitoring/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.626323Z"
---
# _Index

---
Title: Monitoring with metrics and alerts
alwaysopen: false
categories:
- docs
- operate
- rs
- kubernetes
description: Use the metrics that measure the performance of your Redis Software clusters, nodes, databases, and shards to track the performance of your databases.
hideListLinks: true
linkTitle: Monitoring
weight: 70
aliases: [/operate/rs/clusters/monitoring/, /operate/rs/7.4/clusters/monitoring/]
url: '/operate/rs/8.0/monitoring/'
---

You can use the metrics that measure the performance of your Redis Software clusters, nodes, databases, and shards
to monitor the performance of your databases.

## View metrics and configure alerts

In the Redis Software Cluster Manager UI, you can view metrics, configure alerts, and send notifications based on alert parameters. You can also access metrics and configure alerts through the REST API.

See [Metrics and alerts for monitoring v1]({{<relref "/operate/rs/8.0/monitoring/v1_monitoring">}}) for more information.

## Metrics stream engine

The new metrics stream engine is generally available as of [Redis Software version 8.0]({{<relref "/operate/rs/release-notes/rs-8-0-releases">}}) This new engine exposes the v2 Prometheus scraping endpoint at `https://<IP>:8070/v2`, exports all time-series metrics to external monitoring tools, and enables real-time monitoring.

See [Metrics stream engine for monitoring v2]({{<relref "/operate/rs/8.0/monitoring/metrics_stream_engine">}}) for more information.

## Integrate with external monitoring tools

To integrate Redis Software metrics into your monitoring environment, see the following integration guides:

- [Grafana]({{<relref "/integrate/prometheus-with-redis-enterprise">}})

- [Datadog]({{<relref "/integrate/datadog-with-redis-enterprise">}})

- [Dynatrace]({{<relref "/integrate/dynatrace-with-redis-enterprise">}})

- [New Relic]({{<relref "/integrate/new-relic-with-redis-enterprise">}})

For a detailed tutorial to deploy a complete monitoring stack with Prometheus and Grafana, see [Redis Software Observability with Prometheus and Grafana](https://redis.io/learn/operate/observability/redis-software-prometheus-and-grafana).

Filter [Libraries and tools]({{<relref "/integrate">}}) by "observability" for additional tools and guides.

## Metrics reference

Make sure you read the [definition of each metric]({{< relref "/operate/rs/8.0/references/metrics/" >}})
so that you understand exactly what it represents.
