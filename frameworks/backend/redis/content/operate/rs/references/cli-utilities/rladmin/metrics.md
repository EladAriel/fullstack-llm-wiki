---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/cli-utilities/rladmin/metrics.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: rladmin metrics
alwaysopen: false
categories:
- docs
- operate
- rs
description: Configures the cluster-wide metrics stream engine settings.
headerRange: '[1-2]'
linkTitle: metrics
toc: 'true'
weight: $weight
---

Manages the cluster-wide [metrics configuration]({{<relref "/operate/rs/monitoring/metrics_stream_engine/metrics-configuration">}}) for the v2 metrics stream engine.

## `metrics config`

Updates the cluster's metrics configuration. Specify one or more field/value pairs; at least one pair is required.

```sh
rladmin metrics config <field> <value> [ <field> <value> ... ]
```

To view the current configuration, use [`rladmin info metrics`]({{<relref "/operate/rs/references/cli-utilities/rladmin/info#info-metrics">}}).

### Parameters

For the available fields and their types, defaults, and validation, see the [metrics configuration object]({{<relref "/operate/rs/references/rest-api/objects/metrics_config">}}).

On the command line, boolean fields take `enabled` or `disabled`, list fields take a comma-separated set of values, and an empty value (`""`) clears a list field.

### Returns

Returns a confirmation message when the update succeeds.

### Example

```sh
$ rladmin metrics config expose_db_tags enabled metrics_tag_keys_exposed env,team
Metrics configuration updated successfully
```
