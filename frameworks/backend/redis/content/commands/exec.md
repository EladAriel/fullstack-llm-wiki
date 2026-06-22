---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/exec.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
acl_categories:
- '@slow'
- '@transaction'
arity: 1
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
- noscript
- loading
- stale
- skip_slowlog
complexity: Depends on commands in the transaction
description: Executes all commands in a transaction.
group: transactions
hidden: false
linkTitle: EXEC
railroad_diagram: /images/railroad/exec.svg
since: 1.2.0
summary: Executes all commands in a transaction.
syntax_fmt: EXEC
title: EXEC
---
{{< note >}}
This command's behavior varies in clustered Redis environments. See the [multi-key operations]({{< relref "/develop/using-commands/multi-key-operations" >}}) page for more information.
{{< /note >}}


Executes all previously queued commands in a [transaction][tt] and restores the
connection state to normal.

[tt]: /develop/interact/transactions

When using [`WATCH`]({{< relref "/commands/watch" >}}), `EXEC` will execute commands only if the watched keys were
not modified, allowing for a [check-and-set mechanism][ttc].

[ttc]: /develop/interact/transactions#cas

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="exec-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

One of the following:
* [Array reply](../../develop/reference/protocol-spec#arrays): each element being the reply to each of the commands in the atomic transaction.
* [Nil reply](../../develop/reference/protocol-spec#bulk-strings): the transaction was aborted because a `WATCH`ed key was touched.

-tab-sep-

One of the following:
* [Array reply](../../develop/reference/protocol-spec#arrays): each element being the reply to each of the commands in the atomic transaction.
* [Null reply](../../develop/reference/protocol-spec#nulls): the transaction was aborted because a `WATCH`ed key was touched.

{{< /multitabs >}}
