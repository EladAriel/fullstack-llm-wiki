---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/acl-whoami.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

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
command_flags:
- noscript
- loading
- stale
complexity: O(1)
description: Returns the authenticated username of the current connection.
group: server
hidden: false
linkTitle: ACL WHOAMI
railroad_diagram: /images/railroad/acl-whoami.svg
since: 6.0.0
summary: Returns the authenticated username of the current connection.
syntax_fmt: ACL WHOAMI
title: ACL WHOAMI
---
Return the username the current connection is authenticated with.
New connections are authenticated with the "default" user. They
can change user using [`AUTH`]({{< relref "/commands/auth" >}}).

## Examples

```
> ACL WHOAMI
"default"
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | Not supported for [scripts]({{<relref "/develop/programmability">}}). |

## Return information

{{< multitabs id="acl-whoami-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

[Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the username of the current connection.

-tab-sep-

[Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the username of the current connection.

{{< /multitabs >}}
