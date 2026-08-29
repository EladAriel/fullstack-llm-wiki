---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/hotkeys-reset.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.018891Z"
---
# Hotkeys Reset

---
acl_categories:
- '@admin'
- '@slow'
- '@dangerous'
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
command_flags:
- admin
- noscript
complexity: O(1)
container: HOTKEYS
description: Release the resources used for hotkey tracking.
function: hotkeysCommand
group: server
hidden: false
linkTitle: HOTKEYS RESET
railroad_diagram: /images/railroad/hotkeys-reset.svg
since: 8.6.0
summary: Release the resources used for hotkey tracking.
syntax_fmt: HOTKEYS RESET
title: HOTKEYS RESET
---
Release the resources used for hotkey tracking.

This command can only be executed when hotkey tracking is stopped. It will return an error if tracking is currently active. Use [`HOTKEYS STOP`]({{< relref "/commands/hotkeys-stop" >}}) first to stop tracking, then use `HOTKEYS RESET` to free the allocated resources.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="return-info"
    tab1="RESP2"
    tab2="RESP3" >}}

One of the following:

- [Simple string reply]({{< relref "/develop/reference/protocol-spec#simple-strings" >}}): `OK` when resources are successfully released.
- [Simple error reply]({{< relref "/develop/reference/protocol-spec#simple-errors" >}}): when tracking is currently active.

-tab-sep-

One of the following:

- [Simple string reply]({{< relref "/develop/reference/protocol-spec#simple-strings" >}}): `OK` when resources are successfully released.
- [Simple error reply]({{< relref "/develop/reference/protocol-spec#simple-errors" >}}): when tracking is currently active.

{{< /multitabs >}}
