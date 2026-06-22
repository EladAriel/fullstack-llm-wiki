---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/cli-utilities/rladmin/help.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: rladmin help
alwaysopen: false
categories:
- docs
- operate
- rs
description: Shows available commands or specific command usage.
headerRange: '[1-2]'
linkTitle: help
toc: 'true'
weight: $weight
url: '/operate/rs/7.22/references/cli-utilities/rladmin/help/'
---

Lists all options and parameters for `rladmin` commands.

``` sh
rladmin help [command]
```

### Parameters

| Parameter | Description |
|-----------|-------------|
|  command   |  Display help for this `rladmin` command (optional)  |

### Returns

Returns a list of available `rladmin` commands.

If a `command` is specified, returns a list of all the options and parameters for that `rladmin` command.

### Example

```sh
$ rladmin help
usage: rladmin [options] [command] [command args]

Options:
  -y  Assume Yes for all required user confirmations.

Commands:
  bind      Bind an endpoint
  cluster   Cluster management commands
  exit      Exit admin shell
  failover  Fail-over master to slave
  help      Show available commands, or use help <command> for a specific command
  info      Show information about tunable parameters
  migrate   Migrate elements between nodes
  node      Node management commands
  placement Configure shards placement policy
  recover   Recover databases
  restart   Restart database shards
  status    Show status information
  suffix    Suffix management
  tune      Tune system parameters
  upgrade   Upgrade entity version
  verify    Cluster verification reports

Use "rladmin help [command]" to get more information on a specific command.
```
