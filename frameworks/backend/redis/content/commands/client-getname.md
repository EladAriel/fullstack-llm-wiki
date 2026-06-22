---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/client-getname.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
acl_categories:
- '@slow'
- '@connection'
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
- noscript
- loading
- stale
complexity: O(1)
description: Returns the name of the connection.
group: connection
hidden: false
linkTitle: CLIENT GETNAME
railroad_diagram: /images/railroad/client-getname.svg
since: 2.6.9
summary: Returns the name of the connection.
syntax_fmt: CLIENT GETNAME
title: CLIENT GETNAME
---
The `CLIENT GETNAME` returns the name of the current connection as set by [`CLIENT SETNAME`]({{< relref "/commands/client-setname" >}}). Since every new connection starts without an associated name, if no name was assigned nil is returned.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="client-getname-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

One of the following:
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the connection name of the current connection.
* [Nil reply](../../develop/reference/protocol-spec#bulk-strings): the connection name was not set.

-tab-sep-

One of the following:
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the connection name of the current connection.
* [Null reply](../../develop/reference/protocol-spec#nulls): the connection name was not set.

{{< /multitabs >}}
