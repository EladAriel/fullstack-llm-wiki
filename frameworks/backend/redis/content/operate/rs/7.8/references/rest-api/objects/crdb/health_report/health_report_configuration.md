---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/rest-api/objects/crdb/health_report/health_report_configuration.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.513230Z"
---
# Health_Report_Configuration

---
Title: CRDB health report configuration object
alwaysopen: false
categories:
- docs
- operate
- rs
description: An object that represents the database configuration to include in an
  Active-Active database health report.
linkTitle: health_report_configuration
weight: $weight
url: '/operate/rs/7.8/references/rest-api/objects/crdb/health_report/health_report_configuration/'
---

An object that represents the database configuration to include in an Active-Active database health report.

| Name | Type/Value | Description |
|------|------------|-------------|
| causal_consistency | boolean | Enables causal consistency across Active-Active replicas |
| encryption | boolean | Intercluster encryption |
| featureset_version | integer | CRDB active FeatureSet version |
| instances | {{<code>}}[{
  // Unique instance ID
  "id": integer,
  // Local database instance ID
  "db_uid": string,
  "cluster": {
    // Cluster FQDN
    "name": string
    // Cluster access URL
    "url": string
  }
}, ...] {{</code>}} | Local database instances  |
| name | string | Name of database |
| protocol_version | integer | CRDB active protocol version |
| status | string | Current status of the configuration.<br/>Possible values:<br/>**posted:**  Configuration was posted to all replicas<br/>**ready:** All replicas have finished processing posted configuration (create a database)<br/>**committed**: Posted configuration is now active on all replicas<br/>**commit-completed:** All replicas have finished processing committed configuration (database is active)<br/>**failed:** Configuration failed to post |
| version | integer | Database configuration version |
