---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/references/rest-api/objects/alert.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.757644Z"
---
# Alert

---
Title: Alert object
alwaysopen: false
categories:
- docs
- operate
- rs
description: An object that contains alert info
linkTitle: alert
weight: $weight
url: '/operate/rs/7.4/references/rest-api/objects/alert/'
---

You can view, configure, and enable various alerts for the cluster.

Alerts are bound to a cluster object (such as a [BDB]({{< relref "/operate/rs/7.4/references/rest-api/objects/bdb" >}}) or [node]({{< relref "/operate/rs/7.4/references/rest-api/objects/node" >}})), and the cluster's state determines whether the alerts turn on or off.

  Name  | Type/Value | Description | Writable
|-------|------------|-------------|----------|
| change_time | string | Timestamp when alert state last changed | |
| change_value | object | Contains data relevant to the evaluation time when the alert went on/off (thresholds, sampled values, etc.) | |
| enabled | boolean | If true, alert is enabled | x |
| severity | 'DEBUG'<br />'INFO'<br />'WARNING'<br />'ERROR'<br />'CRITICAL' | The alert's severity | |
| state | boolean | If true, alert is currently triggered | |
| threshold | string | Represents an alert threshold when applicable | x |
