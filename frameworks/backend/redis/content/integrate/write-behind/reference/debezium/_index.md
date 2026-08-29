---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/write-behind/reference/debezium/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:56.195571Z"
---
# _Index

---
Title: Debezium Server configuration file
aliases:
- /integrate/redis-data-integration/write-behind/reference/debezium/
- /integrate/redis-data-integration/reference/debezium/
alwaysopen: false
categories:
  - docs
  - integrate
  - rs
  - rdi
description:
  Application properties settings used to configure Debezim Server for
  source database servers
group: di
hideListLinks: false
linkTitle: Debezium Server configuration
summary:
  Redis Data Integration keeps Redis in sync with the primary database in near
  real time.
type: integration
weight: 50
---

The `application.properties` file configures Debezium Server configuration to support source databases. It contains sections that define the sink connector (Redis) configuration and the source connector configuration.
This file needs to be saved in the host running Debezium Server.

The following topics describe `application.properties` for specific database servers:
