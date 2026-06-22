---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/rest-api/objects/bdb/timeseries.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Timeseries configuration object
alwaysopen: false
categories:
- docs
- operate
- rs
description: Configuration object timeseries.
linkTitle: timeseries
weight: $weight
---

Configuration fields for timeseries.

| Field | Type/Value | Description |
|-------|------------|-------------|
| ts-num-threads | integer (range: 1-16) | Number of threads for time series operations. Requires a database restart to take effect. |
| ts-compaction-policy | string  | Default compaction rules. This default value is applied to each new time series upon its creation |
| ts-retention-policy | integer (range: 0-9223372036854775807) (default: 0) | Default retention period, in milliseconds. This default value is applied to each new time series upon its creation, but if COMPACTION_POLICY is specified, it is overridden for created compactions as specified in COMPACTION_POLICY. |
| ts-duplicate-policy | "BLOCK"<br />"FIRST"<br />"LAST"<br />"MIN"<br />"MAX"<br />"SUM"<br />(default: "BLOCK") | Default policy for handling insertion of multiple samples with identical timestamps. This default value is applied to each new time series upon its creation. |
| ts-encoding | "COMPRESSED"<br />"UNCOMPRESSED"<br />(default: "COMPRESSED") | Default chunk encoding for automatically-created compacted time series. This default value is applied to each new compacted time series automatically created due to the creation of a new time series when COMPACTION_POLICY is specified. |
| ts-chunk-size-bytes | integer (range: 48-1048576) (default: 4096) | Default initial allocation size, in bytes, for the data part of each new chunk. This default value is applied to each new time series upon its creation. |
| ts-ignore-max-time-diff | integer (range: 0-9223372036854775807) (default: 0) | Default maximum time difference that can be expired to consider a new insertion to be a duplicate. This default value is applied to each new time series upon its creation. |
| ts-ignore-max-val-diff | number (default: 0) | Default maximum value difference for a new insertion to be considered a duplicate. This default value is applied to each new time series upon its creation. |
