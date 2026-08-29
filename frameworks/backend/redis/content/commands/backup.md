---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/backup.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.087292Z"
---
# Backup

---
acl_categories:
- '@slow'
arity: 2
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
description: A container for backup management commands.
group: server
hidden: true
linkTitle: BACKUP
railroad_diagram: /images/railroad/backup.svg
since: 8.10.0
summary: A container for backup management commands.
syntax_fmt: BACKUP
title: BACKUP
---
This is a container command for backup management commands.

To see the list of available commands you can call [`BACKUP HELP`]({{< relref "/commands/backup-help" >}}).

For a conceptual overview of how the `BACKUP` command family creates online backups, see [Redis persistence]({{< relref "/operate/oss_and_stack/management/persistence" >}}#online-backups-with-the-backup-command-family).
