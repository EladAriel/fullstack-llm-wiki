---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/module.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
acl_categories:
- '@slow'
arity: -2
categories:
- docs
- develop
- stack
- oss
- rs
- rc
- oss
- kubernetes
- clients
complexity: Depends on subcommand.
description: A container for module commands.
group: server
hidden: true
linkTitle: MODULE
railroad_diagram: /images/railroad/module.svg
since: 4.0.0
summary: A container for module commands.
syntax_fmt: MODULE
title: MODULE
---
This is a container command for module management commands.

To see the list of available commands you can call [`MODULE HELP`]({{< relref "/commands/module-help" >}}).
