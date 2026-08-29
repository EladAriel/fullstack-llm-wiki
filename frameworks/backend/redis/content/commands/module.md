---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/module.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.057608Z"
---
# Module

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
