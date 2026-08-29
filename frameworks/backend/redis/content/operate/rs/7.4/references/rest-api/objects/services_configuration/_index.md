---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/references/rest-api/objects/services_configuration/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.781600Z"
---
# _Index

---
Title: Services configuration object
alwaysopen: false
categories:
- docs
- operate
- rs
description: An object for optional cluster services settings
hideListLinks: true
linkTitle: services_configuration
weight: $weight
url: '/operate/rs/7.4/references/rest-api/objects/services_configuration/'
---

Optional cluster services settings

| Name | Type/Value | Description |
|------|------------|-------------|
| alert_mgr | [alert_mgr]({{< relref "/operate/rs/7.4/references/rest-api/objects/services_configuration/alert_mgr" >}}) object | Whether to enable/disable the alert manager processes |
| cm_server | [cm_server]({{< relref "/operate/rs/7.4/references/rest-api/objects/services_configuration/cm_server" >}}) object | Whether to enable/disable the CM server |
| crdb_coordinator | [crdb_coordinator]({{< relref "/operate/rs/7.4/references/rest-api/objects/services_configuration/crdb_coordinator" >}}) object | Whether to enable/disable the CRDB coordinator process |
| crdb_worker | [crdb_worker]({{< relref "/operate/rs/7.4/references/rest-api/objects/services_configuration/crdb_worker" >}}) object | Whether to enable/disable the CRDB worker processes |
| mdns_server | [mdns_server]({{< relref "/operate/rs/7.4/references/rest-api/objects/services_configuration/mdns_server" >}}) object | Whether to enable/disable the multicast DNS server |
| pdns_server | [pdns_server]({{< relref "/operate/rs/7.4/references/rest-api/objects/services_configuration/pdns_server" >}}) object | Whether to enable/disable the PDNS server |
| stats_archiver | [stats_archiver]({{< relref "/operate/rs/7.4/references/rest-api/objects/services_configuration/stats_archiver" >}}) object | Whether to enable/disable the stats archiver service |
