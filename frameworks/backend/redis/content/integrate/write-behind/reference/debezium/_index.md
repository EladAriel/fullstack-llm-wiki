---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/integrate/write-behind/reference/debezium/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Debezium Server configuration file
aliases: /integrate/redis-data-integration/write-behind/reference/debezium/
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
